# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) process definitions.
"""

__all__ = [
    "tthh_4b", "vhh_4b", "whh_4b_k2v1p0kl0p0kv1p0", "zhh_4b_k2v1p0kl0p0kv1p0",
]

# import cmsdb.constants as const
from scinum import Number

from cmsdb.processes.hh import (
    hh,
)
# from cmsdb.util import multiply_xsecs


#
# ggF -> HH -> 4tau
#

# placeholder for the general process, not used as parent process and should not have a cross section
tthh_4b = hh.add_process(
    name="tthh_4b",
    id=101000,
    label=r"$ttHH$",
    xsecs={
        13.6: 0.001 * Number(0.7554, {
            "scale": 0.0001602j,
        }),
    },
)
vhh_4b = hh.add_process(
    name="vhh_4b",
    id=102000,
    label=r"$VHH$",
    xsecs={
        13.6: 0.001 * Number(0.4368, {
            "scale": 0.0001437j,
        }),
    },
)
whh_4b_k2v1p0kl0p0kv1p0 = vhh_4b.add_process(
    name="whh_4b_k2v1p0kl0p0kv1p0",
    id=102001,
    label=r"$WHH",
    xsecs={
        13.6: 0.001 * Number(0.2644, {
            "scale": 0.00006437j,
        }),
    },
)
zhh_4b_k2v1p0kl0p0kv1p0 = vhh_4b.add_process(
    name="zhh_4b_k2v1p0kl0p0kv1p0",
    id=102002,
    label=r"$ZHH \rightarrow$",
    xsecs={
        13.6: 0.001 * Number(0.1724, {
            "scale": 0.0000416j,
        }),
    },
)
