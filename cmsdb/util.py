# coding: utf-8

"""
Helpful utilities.
"""

from __future__ import annotations

__all__ = ["DotDict", "multiply_xsecs", "add_xsecs", "add_decay_process", "add_sub_decay_process"]


from functools import partial
from scinum import Number

from order import Process
from collections import OrderedDict


class DotDict(OrderedDict):
    """
    Subclass of *OrderedDict* that provides read and write access to items via attributes by
    implementing ``__getattr__`` and ``__setattr__``. In case a item is accessed via attribute and
    it does not exist, an *AttriuteError* is raised rather than a *KeyError*. Example:

    .. code-block:: python

        d = DotDict()
        d["foo"] = 1

        print(d["foo"])
        # => 1

        print(d.foo)
        # => 1

        print(d["bar"])
        # => KeyError

        print(d.bar)
        # => AttributeError

        d.bar = 123
        print(d.bar)
        # => 123

        # use wrap() to convert a nested dict
        d = DotDict({"foo": {"bar": 1}})
        print(d.foo.bar)
        # => 1
    """

    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        self[attr] = value

    def copy(self):
        """"""
        return self.__class__(self)

    @classmethod
    def wrap(cls, *args, **kwargs) -> "DotDict":
        """
        Takes a dictionary *d* and recursively replaces it and all other nested dictionary types
        with :py:class:`DotDict`'s for deep attribute-style access.
        """
        wrap = lambda d: cls((k, wrap(v)) for k, v in d.items()) if isinstance(d, dict) else d
        return wrap(OrderedDict(*args, **kwargs))


def multiply_xsecs(base_proc: Process, factor: float | int | Number) -> dict[float, Number]:
    """
    Helper to multiply all cross sections of a base process *base_proc*
    with some value *factor*
    """
    xsecs = {
        ecm: base_proc.get_xsec(ecm) * factor
        for ecm in base_proc.xsecs.keys()
    }
    return xsecs


def add_xsecs(*processes: tuple[Process]) -> dict[float, Number]:
    """
    Helper to add all cross sections of multiple processes *processes*. Only the
    cross sections from center of mass energies that are available for all processes are added.
    """
    valid_ecms = set.intersection(*[set(proc.xsecs.keys()) for proc in processes])
    xsecs = {
        ecm: sum([proc.get_xsec(ecm) for proc in processes])
        for ecm in valid_ecms
    }
    return xsecs


def add_the_production_mode_parent(child: Process, parent: Process) -> Process:
    """
    Takes all processes from the *production_mode_parent* aux of the *parent* process and adds their
    child processes with the same final state to the *child* process, both as parent and as aux.
    If the *parent* process has no *production_mode_parent* aux, it is assumed that the *parent*
    process only has a single parent process, which is then used as the production mode parent.

    Example:

    .. code-block:: python
        h_ggf_hzz = h_ggf.add_process(name="h_hzz", id=1, production_mode_parent="h_hzz")
        h_ggf_hzz4l = h_ggf_hzz.add_process(name="h_ggf_hzz4l", id=2)
        add_the_production_mode_parent(h_ggf_hzz4l, h_ggf_hzz)

        h_ggf_hzz4l.parent_processes.names() # => ["h_ggf_hzz", "h_hzz4l"]

    :param child: Child process to which the production mode parent should be added.
    :param parent: Parent process from which the production mode parents parent should be taken.
    :return: The child process with production mode parents added.
    """
    if parent.has_aux("production_mode_parent"):
        grandparents = parent.aux["production_mode_parent"]
        if isinstance(grandparents, str) or isinstance(grandparents, Process):
            grandparents = [grandparents]
        grandparents = [parent.get_parent_process(gp) for gp in grandparents]
    elif len(parent.parent_processes) == 1:
        grandparents = parent.parent_processes
    else:
        raise ValueError(
            f"Parent process {parent.name} either needs the *production_mode_parent* aux or it "
            "must have exactly one parent process, but has "
            f"{parent.parent_processes.names()} ({len(parent.parent_processes)}).",
        )
    for grandparent in grandparents:
        production_mode_parent = grandparent.get_process(child.name.replace(parent.name, grandparent.name))
        production_mode_parent.add_process(child)
        child.x.production_mode_parent = child.x("production_mode_parent", []) + [production_mode_parent.name]

    return child


def add_decay_process(
    parent: Process,
    decay_map: DotDict,
    add_production_mode_parent: bool = True,
    name_separator: str = "_",
    label_separator: str = ", ",
    **kwargs,
) -> Process:
    """
    Add a subprocess to the *parent* Process for a certain decay channel encoded via the *decay_map*.

    :param parent: Parent process.
    :param decay_map: Dictionary with decay channel information. Needs to include the keys
    *name*, *id*, *br*, and *label*. When passing the *custom_id* parameter, the *id* key is ignored.
    :param add_production_mode_parent: Whether to add the process with the same final state but different
    production mode as parent. Also adds the *production_mode_parent* attribute to the subprocess.
    :param name_separator: Separator to be used for the subprocess name.
    :param label_separator: Separator to be used for the subprocess label.
    :return: The resulting child process.
    """

    # get default kwargs from parent + decay map
    child_kwargs = {
        "name": f"{parent.name}{name_separator}{decay_map.name}",
        "id": parent.id + decay_map["id"],
        "label": rf"{parent.label}{label_separator}{decay_map['label']}",
        "xsecs": multiply_xsecs(parent, decay_map["br"]),
    }

    # overwrite kwargs with custom kwargs
    child_kwargs.update(kwargs)

    # add process
    child = parent.add_process(**child_kwargs)
    if add_production_mode_parent:
        add_the_production_mode_parent(child, parent)

    return child


add_sub_decay_process = partial(add_decay_process, name_separator="", label_separator="")
