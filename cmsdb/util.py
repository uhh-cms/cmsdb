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


def multiply_xsecs(base_proc: Process, factor: float) -> dict[float, Number]:
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


def add_decay_process(
    parent: Process,
    decay_map: DotDict,
    custom_id: int | None = None,
    add_production_mode_parent: bool = False,
    name_separator: str = "_",
    label_separator: str = ", ",
) -> Process:
    """
    Add a subprocess to the *parent* Process for a certain decay channel encoded via the *decay_map*.

    :param parent: Parent process.
    :param decay_map: Dictionary with decay channel information. Needs to include the keys
    *name*, *id*, *br*, and *label*. When passing the *custom_id* parameter, the *id* key is ignored.
    :param custom_id: Optional custom ID to be used for the subprocess.
    :param add_production_mode_parent: Whether to add the process with the same final state but different
    production mode as parent. Als adds the *production_mode_parent* attribute to the subprocess.
    :param name_separator: Separator to be used for the subprocess name.
    :param label_separator: Separator to be used for the subprocess label.
    :return: The resulting child process.
    """
    _id = custom_id if custom_id else parent.id + decay_map["id"]
    label = rf"{parent.label}{label_separator}{decay_map['label']}"

    child = parent.add_process(
        name=f"{parent.name}{name_separator}{decay_map.name}",
        id=_id,
        label=label,
        xsecs=multiply_xsecs(parent, decay_map["br"]),
    )
    if add_production_mode_parent:
        if parent.has_aux("production_mode_parent"):
            grandparent = parent.get_parent_process(parent.aux["production_mode_parent"])
        elif len(parent.parent_processes) == 1:
            grandparent = parent.parent_processes.get_first()
        else:
            raise ValueError(
                f"Parent process {parent.name} either needs the *production_mode_parent* aux or it "
                "must have exactly one parent process, but has "
                f"{parent.parent_processes.names()} ({len(parent.parent_processes)}).",
            )
        production_mode_parent = grandparent.get_process(f"{grandparent.name}{name_separator}{decay_map.name}")
        production_mode_parent.add_process(child)
        child.x.production_mode_parent = production_mode_parent.name

    return child


add_sub_decay_process = partial(add_decay_process, name_separator="", label_separator="")
