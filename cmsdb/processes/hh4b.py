# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) process definitions.
"""

__all__ = [
    "tthh_4b", "tthh_2b2t_dl", "tthh_2b2t_sl", "tthh_2b2w_dl", "tthh_2b2w_sl", "tthh_2b2z_dl", "tthh_2b2z_sl",
    "vhh_4b", "whh_4b_k2v1p0kl0p0kv1p0", "zhh_4b_k2v1p0kl0p0kv1p0",
]

# import cmsdb.constants as const
from scinum import Number

from cmsdb.processes.hh import (
    hh,
)
from cmsdb.util import multiply_xsecs
import cmsdb.constants as const
# from cmsdb.util import multiply_xsecs


#
# ggF -> HH -> 4tau
#

# BR for HH
br_2b2t = 0.0731
br_2b2w = 0.2489
br_2b2z = 0.0305
br_4b = 0.03392


# placeholder for the general process, not used as parent process and should not have a cross section
tthh = hh.add_process(
    name="tthh",
    id=101000,
    label=r"$ttHH$",
    xsecs={
        13.6: 0.001 * Number(0.86, {
            "scale": (14.0, 4.2),
            "pdf": 3.3,
        }),
    },
)
tthh_4b = tthh.add_process(
    name="tthh_4b",
    id=101001,
    label=r"$ttHH$",
    xsecs=multiply_xsecs(tthh, br_4b),
)
tthh_2b2t_dl = tthh.add_process(
    name="tthh_2b2t_dl",
    id=101002,
    label=r"$ttHH (2b2 \tau, DL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.dl * br_2b2t),
)
tthh_2b2t_sl = tthh.add_process(
    name="tthh_2b2t_sl",
    id=101003,
    label=r"$ttHH (2b2 \tau, SL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.sl * br_2b2t),
)
tthh_2b2w_dl = tthh.add_process(
    name="tthh_2b2w_dl",
    id=101004,
    label=r"$ttHH (2b2W, DL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.dl * br_2b2w),
)
tthh_2b2w_sl = tthh.add_process(
    name="tthh_2b2w_sl",
    id=101005,
    label=r"$ttHH (2b2W, SL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.sl * br_2b2w),
)
tthh_2b2z_dl = tthh.add_process(
    name="tthh_2b2z_dl",
    id=101006,
    label=r"$ttHH (2b2z, DL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.dl * br_2b2z),
)
tthh_2b2z_sl = tthh.add_process(
    name="tthh_2b2z_sl",
    id=101007,
    label=r"$ttHH (2b2z, SL)$",
    xsecs=multiply_xsecs(tthh, const.br_ww.sl * br_2b2z),
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
