# coding: utf-8

"""
Helpful utilities.
"""

__all__ = ["DotDict", "multiply_xsecs", "add_xsecs"]

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
