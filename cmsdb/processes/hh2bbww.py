# coding: utf-8

"""
HH -> bbWW process definitions.
"""

__all__ = [
    "ggHH_sl_hbbhww", "ggHH_kl_0_kt_1_sl_hbbhww", "ggHH_kl_1_kt_1_sl_hbbhww",
    "ggHH_kl_2p45_kt_1_sl_hbbhww", "ggHH_kl_5_kt_1_sl_hbbhww",
    "qqHH_sl_hbbhww", "qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww", "qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_0_kl_1_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_0_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_1_kl_2_sl_hbbhww", "qqHH_CV_1_C2V_2_kl_1_sl_hbbhww",
]

import cmsdb.constants as const
from cmsdb.processes.higgs import (
    hh_ggf, ggHH_kl_0_kt_1, ggHH_kl_1_kt_1, ggHH_kl_2p45_kt_1, ggHH_kl_5_kt_1,
    hh_vbf, qqHH_CV_1_C2V_1_kl_1, qqHH_CV_1_C2V_1_kl_0, qqHH_CV_1_C2V_1_kl_2,
    qqHH_CV_1_C2V_0_kl_1, qqHH_CV_1_C2V_2_kl_1, qqHH_CV_0p5_C2V_1_kl_1, qqHH_CV_1p5_C2V_1_kl_1,
)


#
# HH -> bbWW -> bbWWqqlnu
#

#
# ggf
#

ggHH_sl_hbbhww = hh_ggf.add_process(
    name="ggHH_sl_hbbhww",
    id=21210,
    label=r"$HH_{ggf} \rightarrow bbWW(qql\nu)$",
    xsecs={
        13: hh_ggf.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

ggHH_kl_0_kt_1_sl_hbbhww = ggHH_kl_0_kt_1.add_process(
    name="ggHH_kl_0_kt_1_sl_hbbhww",
    id=21211,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbWW(qql\nu)$",
    xsecs={
        13: ggHH_kl_0_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

ggHH_kl_1_kt_1_sl_hbbhww = ggHH_kl_1_kt_1.add_process(
    name="ggHH_kl_1_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbWW(qql\nu)$",
    id=21212,
    xsecs={
        13: ggHH_kl_1_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

ggHH_kl_2p45_kt_1_sl_hbbhww = ggHH_kl_2p45_kt_1.add_process(
    name="ggHH_kl_2p45_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbWW(qql\nu)$",
    id=21213,
    xsecs={
        13: ggHH_kl_2p45_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

ggHH_kl_5_kt_1_sl_hbbhww = ggHH_kl_5_kt_1.add_process(
    name="ggHH_kl_5_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbWW(qql\nu)$",
    id=21214,
    xsecs={
        13: ggHH_kl_5_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

#
# VBF
#

qqHH_sl_hbbhww = hh_vbf.add_process(
    name="qqHH_sl_hbbhww",
    label=r"$HH_{vbf} \rightarrow bbWW(qql\nu)$",
    id=22210,
    xsecs={
        13: hh_vbf.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1_C2V_1_kl_1_sl_hbbhww = qqHH_CV_1_C2V_1_kl_1.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbWW(qql\nu)$",
    id=22211,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1_C2V_1_kl_0_sl_hbbhww = qqHH_CV_1_C2V_1_kl_0.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbWW(qql\nu)$",
    id=22212,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1_C2V_1_kl_2_sl_hbbhww = qqHH_CV_1_C2V_1_kl_2.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbWW(qql\nu)$",
    id=22213,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_2.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1_C2V_0_kl_1_sl_hbbhww = qqHH_CV_1_C2V_0_kl_1.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbWW(qql\nu)$",
    id=22214,
    xsecs={
        13: qqHH_CV_1_C2V_0_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1_C2V_2_kl_1_sl_hbbhww = qqHH_CV_1_C2V_2_kl_1.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbWW(qql\nu)$",
    id=22215,
    xsecs={
        13: qqHH_CV_1_C2V_2_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)


qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww = qqHH_CV_0p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22216,
    xsecs={
        13: qqHH_CV_0p5_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww = qqHH_CV_1p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22217,
    xsecs={
        13: qqHH_CV_1p5_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)
