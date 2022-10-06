# coding: utf-8

"""
HH -> bbWW process definitions.
"""

__all__ = [
    "hh_ggf_bbww_sl", "hh_ggf_kt_1_kl_0_bbww_sl", "hh_ggf_kt_1_kl_1_bbww_sl",
    "hh_ggf_kt_1_kl_2p45_bbww_sl", "hh_ggf_kt_1_kl_5_bbww_sl",
    "hh_vbf_bbww_sl", "hh_vbf_cv_0p5_c2v_1_c3_1_bbww_sl", "hh_vbf_cv_1p5_c2v_1_c3_1_bbww_sl",
    "hh_vbf_cv_1_c2v_0_c3_1_bbww_sl", "hh_vbf_cv_1_c2v_1_c3_0_bbww_sl", "hh_vbf_cv_1_c2v_1_c3_1_bbww_sl",
    "hh_vbf_cv_1_c2v_1_c3_2_bbww_sl", "hh_vbf_cv_1_c2v_2_c3_1_bbww_sl",
]

import cmsdb.constants as const
from cmsdb.processes.higgs import (
    hh_ggf, hh_ggf_kt_1_kl_0, hh_ggf_kt_1_kl_1, hh_ggf_kt_1_kl_2p45, hh_ggf_kt_1_kl_5,
    hh_vbf, hh_vbf_cv_0p5_c2v_1_c3_1, hh_vbf_cv_1p5_c2v_1_c3_1, hh_vbf_cv_1_c2v_0_c3_1,
    hh_vbf_cv_1_c2v_1_c3_0, hh_vbf_cv_1_c2v_1_c3_1, hh_vbf_cv_1_c2v_1_c3_2, hh_vbf_cv_1_c2v_2_c3_1,
)


#
# HH -> bbWW -> bbWWqqlnu
#

#
# ggf
#

hh_ggf_bbww_sl = hh_ggf.add_process(
    name="hh_ggf_bbww_sl",
    id=21120,
    label=r"$HH_{ggf} \rightarrow bbWW(qql\nu)$",
    xsecs={
        13: hh_ggf.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_0_bbww_sl = hh_ggf_kt_1_kl_0.add_process(
    name="hh_ggf_kt_1_kl_0_bbww_sl",
    id=21221,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbWW(qql\nu)$",
    xsecs={
        13: hh_ggf_kt_1_kl_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_1_bbww_sl = hh_ggf_kt_1_kl_1.add_process(
    name="hh_ggf_kt_1_kl_1_bbww_sl",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbWW(qql\nu)$",
    id=21222,
    xsecs={
        13: hh_ggf_kt_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_2p45_bbww_sl = hh_ggf_kt_1_kl_2p45.add_process(
    name="hh_ggf_kt_1_kl_2p45_bbww_sl",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbWW(qql\nu)$",
    id=21223,
    xsecs={
        13: hh_ggf_kt_1_kl_2p45.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_5_bbww_sl = hh_ggf_kt_1_kl_5.add_process(
    name="hh_ggf_kt_1_kl_5_bbww_sl",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbWW(qql\nu)$",
    id=21224,
    xsecs={
        13: hh_ggf_kt_1_kl_5.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

#
# VBF
#

hh_vbf_bbww_sl = hh_vbf.add_process(
    name="hh_vbf_bbww_sl",
    label=r"$HH_{vbf} \rightarrow bbWW(qql\nu)$",
    id=22200,
    xsecs={
        13: hh_vbf.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_0p5_c2v_1_c3_1_bbww_sl = hh_vbf_cv_0p5_c2v_1_c3_1.add_process(
    name="hh_vbf_cv_0p5_c2v_1_c3_1_bbww_sl",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22201,
    xsecs={
        13: hh_vbf_cv_0p5_c2v_1_c3_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1p5_c2v_1_c3_1_bbww_sl = hh_vbf_cv_1p5_c2v_1_c3_1.add_process(
    name="hh_vbf_cv_1p5_c2v_1_c3_1_bbww_sl",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22202,
    xsecs={
        13: hh_vbf_cv_1p5_c2v_1_c3_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1_c2v_0_c3_1_bbww_sl = hh_vbf_cv_1_c2v_0_c3_1.add_process(
    name="hh_vbf_cv_1_c2v_0_c3_1_bbww_sl",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbWW(qql\nu)$",
    id=22203,
    xsecs={
        13: hh_vbf_cv_1_c2v_0_c3_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1_c2v_1_c3_0_bbww_sl = hh_vbf_cv_1_c2v_1_c3_0.add_process(
    name="hh_vbf_cv_1_c2v_1_c3_0_bbww_sl",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbWW(qql\nu)$",
    id=22204,
    xsecs={
        13: hh_vbf_cv_1_c2v_1_c3_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1_c2v_1_c3_1_bbww_sl = hh_vbf_cv_1_c2v_1_c3_1.add_process(
    name="hh_vbf_cv_1_c2v_1_c3_1_bbww_sl",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbWW(qql\nu)$",
    id=22205,
    xsecs={
        13: hh_vbf_cv_1_c2v_1_c3_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1_c2v_1_c3_2_bbww_sl = hh_vbf_cv_1_c2v_1_c3_2.add_process(
    name="hh_vbf_cv_1_c2v_1_c3_2_bbww_sl",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbWW(qql\nu)$",
    id=22206,
    xsecs={
        13: hh_vbf_cv_1_c2v_1_c3_2.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_vbf_cv_1_c2v_2_c3_1_bbww_sl = hh_vbf_cv_1_c2v_2_c3_1.add_process(
    name="hh_vbf_cv_1_c2v_2_c3_1_bbww_sl",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbWW(qql\nu)$",
    id=22207,
    xsecs={
        13: hh_vbf_cv_1_c2v_2_c3_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)
