# coding: utf-8

"""
HH -> bbWW process definitions.
"""

__all__ = [
    # Single Lepton HHbbWW, ggH
    "ggHH_sl_hbbhww", "ggHH_kl_0_kt_1_sl_hbbhww", "ggHH_kl_1_kt_1_sl_hbbhww",
    "ggHH_kl_2p45_kt_1_sl_hbbhww", "ggHH_kl_5_kt_1_sl_hbbhww",
    # Dilepton HHbbWW, ggH
    "ggHH_dl_hbbhww", "ggHH_kl_0_kt_1_dl_hbbhww", "ggHH_kl_1_kt_1_dl_hbbhww",
    "ggHH_kl_2p45_kt_1_dl_hbbhww", "ggHH_kl_5_kt_1_dl_hbbhww",
    # Single Lepton HHbbWW, qqH
    "qqHH_sl_hbbhww", "qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww", "qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_0_kl_1_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_0_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_1_kl_2_sl_hbbhww", "qqHH_CV_1_C2V_2_kl_1_sl_hbbhww",
    # Dilepton HHbbWW, qqH
    "qqHH_dl_hbbhww", "qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww", "qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww",
    "qqHH_CV_1_C2V_0_kl_1_dl_hbbhww", "qqHH_CV_1_C2V_1_kl_0_dl_hbbhww", "qqHH_CV_1_C2V_1_kl_1_dl_hbbhww",
    "qqHH_CV_1_C2V_1_kl_2_dl_hbbhww", "qqHH_CV_1_C2V_2_kl_1_dl_hbbhww",
    # Resonant HHbbWW: radion
    "radion_hh_ggf_bbww",
    "radion_hh_ggf_bbww_m250", "radion_hh_ggf_bbww_m260", "radion_hh_ggf_bbww_m270",
    "radion_hh_ggf_bbww_m280", "radion_hh_ggf_bbww_m300", "radion_hh_ggf_bbww_m320",
    "radion_hh_ggf_bbww_m350", "radion_hh_ggf_bbww_m400", "radion_hh_ggf_bbww_m450",
    "radion_hh_ggf_bbww_m500", "radion_hh_ggf_bbww_m550", "radion_hh_ggf_bbww_m600",
    "radion_hh_ggf_bbww_m650", "radion_hh_ggf_bbww_m700", "radion_hh_ggf_bbww_m750",
    "radion_hh_ggf_bbww_m800", "radion_hh_ggf_bbww_m850", "radion_hh_ggf_bbww_m900",
    "radion_hh_ggf_bbww_m1000", "radion_hh_ggf_bbww_m1250", "radion_hh_ggf_bbww_m1500",
    "radion_hh_ggf_bbww_m1750", "radion_hh_ggf_bbww_m2000", "radion_hh_ggf_bbww_m2500",
    "radion_hh_ggf_bbww_m3000",
    # Resonant HHbbWW: graviton
    "graviton_hh_ggf_bbww",
    "graviton_hh_ggf_bbww_m250", "graviton_hh_ggf_bbww_m260",
    "graviton_hh_ggf_bbww_m270", "graviton_hh_ggf_bbww_m280",
    "graviton_hh_ggf_bbww_m300", "graviton_hh_ggf_bbww_m320",
    "graviton_hh_ggf_bbww_m350", "graviton_hh_ggf_bbww_m400",
    "graviton_hh_ggf_bbww_m450", "graviton_hh_ggf_bbww_m500",
    "graviton_hh_ggf_bbww_m550", "graviton_hh_ggf_bbww_m600",
    "graviton_hh_ggf_bbww_m650", "graviton_hh_ggf_bbww_m700",
    "graviton_hh_ggf_bbww_m750", "graviton_hh_ggf_bbww_m800",
    "graviton_hh_ggf_bbww_m850", "graviton_hh_ggf_bbww_m900",
    "graviton_hh_ggf_bbww_m1000", "graviton_hh_ggf_bbww_m1250",
    "graviton_hh_ggf_bbww_m1500", "graviton_hh_ggf_bbww_m1750",
    "graviton_hh_ggf_bbww_m2000", "graviton_hh_ggf_bbww_m2500",
    "graviton_hh_ggf_bbww_m3000",
]

from scinum import Number

import cmsdb.constants as const
from cmsdb.processes.higgs import (
    hh_ggf, ggHH_kl_0_kt_1, ggHH_kl_1_kt_1, ggHH_kl_2p45_kt_1, ggHH_kl_5_kt_1,
    hh_vbf, qqHH_CV_1_C2V_1_kl_1, qqHH_CV_1_C2V_1_kl_0, qqHH_CV_1_C2V_1_kl_2,
    qqHH_CV_1_C2V_0_kl_1, qqHH_CV_1_C2V_2_kl_1, qqHH_CV_0p5_C2V_1_kl_1, qqHH_CV_1p5_C2V_1_kl_1,
    radion_hh_ggf, graviton_hh_ggf,
)


#
# HH -> bbWW -> bbWWqqlnu
#

#
# ggf, single lepton
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
# ggf, dilepton
#

ggHH_dl_hbbhww = hh_ggf.add_process(
    name="ggHH_dl_hbbhww",
    id=21220,
    label=r"$HH_{ggf} \rightarrow bbWW(l\nu l\nu)$",
    xsecs={
        13: hh_ggf.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

ggHH_kl_0_kt_1_dl_hbbhww = ggHH_kl_0_kt_1.add_process(
    name="ggHH_kl_0_kt_1_dl_hbbhww",
    id=21221,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbWW(l\nu l\nu)$",
    xsecs={
        13: ggHH_kl_0_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

ggHH_kl_1_kt_1_dl_hbbhww = ggHH_kl_1_kt_1.add_process(
    name="ggHH_kl_1_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbWW(l\nu l\nu)$",
    id=21222,
    xsecs={
        13: ggHH_kl_1_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

ggHH_kl_2p45_kt_1_dl_hbbhww = ggHH_kl_2p45_kt_1.add_process(
    name="ggHH_kl_2p45_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbWW(l\nu l\nu)$",
    id=21223,
    xsecs={
        13: ggHH_kl_2p45_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

ggHH_kl_5_kt_1_dl_hbbhww = ggHH_kl_5_kt_1.add_process(
    name="ggHH_kl_5_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbWW(l\nu l\nu)$",
    id=21224,
    xsecs={
        13: ggHH_kl_5_kt_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

#
# VBF, single lepton
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

#
# VBF, dilepton
#

qqHH_dl_hbbhww = hh_vbf.add_process(
    name="qqHH_dl_hbbhww",
    label=r"$HH_{vbf} \rightarrow bbWW(l\nu l\nu)$",
    id=22220,
    xsecs={
        13: hh_vbf.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1_C2V_1_kl_1_dl_hbbhww = qqHH_CV_1_C2V_1_kl_1.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22221,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1_C2V_1_kl_0_dl_hbbhww = qqHH_CV_1_C2V_1_kl_0.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbWW(l\nu l\nu)$",
    id=22222,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1_C2V_1_kl_2_dl_hbbhww = qqHH_CV_1_C2V_1_kl_2.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbWW(l\nu l\nu)$",
    id=22223,
    xsecs={
        13: qqHH_CV_1_C2V_1_kl_2.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1_C2V_0_kl_1_dl_hbbhww = qqHH_CV_1_C2V_0_kl_1.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22224,
    xsecs={
        13: qqHH_CV_1_C2V_0_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1_C2V_2_kl_1_dl_hbbhww = qqHH_CV_1_C2V_2_kl_1.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22225,
    xsecs={
        13: qqHH_CV_1_C2V_2_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)


qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww = qqHH_CV_0p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22226,
    xsecs={
        13: qqHH_CV_0p5_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww = qqHH_CV_1p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22227,
    xsecs={
        13: qqHH_CV_1p5_C2V_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.dl,
    },
)

#
# ggF -> radion -> HH
#

radion_hh_ggf_bbww = radion_hh_ggf.add_process(
    name="radion_hh_ggf_bbww",
    id=23200,
    label=rf"{radion_hh_ggf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m250",
    id=23201,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m260 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m260",
    id=23202,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m270 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m270",
    id=23203,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m280 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m280",
    id=23204,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m300 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m300",
    id=23205,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m320 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m320",
    id=23206,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m350 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m350",
    id=23207,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m400 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m400",
    id=23208,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m450 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m450",
    id=23209,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m500",
    id=23210,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m550 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m550",
    id=23211,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m600 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m600",
    id=23212,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m650 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m650",
    id=23213,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m700 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m700",
    id=23214,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m750",
    id=23215,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m800 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m800",
    id=23216,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m850 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m850",
    id=23217,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m900 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m900",
    id=23218,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1000",
    id=23219,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1250",
    id=23220,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1500",
    id=23221,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1750",
    id=23222,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m2000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2000",
    id=23223,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m2500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2500",
    id=23224,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m3000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m3000",
    id=23225,
    xsecs={13: Number(0.1)},  # TODO
)


#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf_bbww = graviton_hh_ggf.add_process(
    name="graviton_hh_ggf_bbww",
    id=24200,
    label=rf"{graviton_hh_ggf.label} $\rightarrow bbWW$",
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m250",
    id=24201,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m260 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m260",
    id=24202,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m270 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m270",
    id=24203,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m280 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m280",
    id=24204,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m300 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m300",
    id=24205,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m320 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m320",
    id=24206,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m350 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m350",
    id=24207,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m400 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m400",
    id=24208,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m450 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m450",
    id=24209,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m500",
    id=24210,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m550 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m550",
    id=24211,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m600 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m600",
    id=24212,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m650 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m650",
    id=24213,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m700 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m700",
    id=24214,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m750",
    id=24215,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m800 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m800",
    id=24216,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m850 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m850",
    id=24217,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m900 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m900",
    id=24218,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1000",
    id=24219,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1250",
    id=24220,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1500",
    id=24221,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1750",
    id=24222,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m2000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2000",
    id=24223,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m2500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2500",
    id=24224,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m3000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m3000",
    id=24225,
    xsecs={13: Number(0.1)},  # TODO
)
