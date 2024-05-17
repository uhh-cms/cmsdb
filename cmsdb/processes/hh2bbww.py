# coding: utf-8

"""
HH -> bbVV process definitions.

IDs are assigned in the range 21200-21499 for ggHH and 22200-22499 for qqHH.
bbWW processes are assigned IDs in the range 21200-21299 and 22200-22299.
bbZZ processes are assigned IDs in the range 21300-21399 and 22300-22399.
bbVV processes are assigned IDs in the range 21400-21499 and 22400-22499.
SL processes are assigned the ranges from 10-19 and DL processes from 20-29 (FH still missing)
The merged processes are assigned the ranges from 1-9.
"""

__all__ = [
    "ggHH_hbbhvv", "qqHH_hbbhvv", "ggHH_hbbhww", "qqHH_hbbhww", "ggHH_hbbhzz", "qqHH_hbbhzz",
    # HH -> bbVV, ggf
    "ggHH_kl_0_kt_1_hbbhvv", "ggHH_kl_1_kt_1_hbbhvv",
    "ggHH_kl_2p45_kt_1_hbbhvv", "ggHH_kl_5_kt_1_hbbhvv",
    # HH -> bbVV, vbf
    "qqHH_CV_0p5_C2V_1_kl_1_hbbhvv", "qqHH_CV_1p5_C2V_1_kl_1_hbbhvv",
    "qqHH_CV_1_C2V_0_kl_1_hbbhvv", "qqHH_CV_1_C2V_1_kl_0_hbbhvv", "qqHH_CV_1_C2V_1_kl_1_hbbhvv",
    "qqHH_CV_1_C2V_1_kl_2_hbbhvv", "qqHH_CV_1_C2V_2_kl_1_hbbhvv",
    # HH -> bbVV(2l2v), ggf
    "ggHH_dl_hbbhvv", "ggHH_kl_0_kt_1_dl_hbbhvv", "ggHH_kl_1_kt_1_dl_hbbhvv",
    "ggHH_kl_2p45_kt_1_dl_hbbhvv", "ggHH_kl_5_kt_1_dl_hbbhvv",
    # HH -> bbVV(2l2v), vbf
    "qqHH_dl_hbbhvv", "qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv", "qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv",
    "qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv", "qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv", "qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv",
    "qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv", "qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv",
    # HH -> bbWW(qqlv), ggf
    "ggHH_sl_hbbhww", "ggHH_kl_0_kt_1_sl_hbbhww", "ggHH_kl_1_kt_1_sl_hbbhww",
    "ggHH_kl_2p45_kt_1_sl_hbbhww", "ggHH_kl_5_kt_1_sl_hbbhww",
    # HH -> bbWW(lvlv), ggf
    "ggHH_dl_hbbhww", "ggHH_kl_0_kt_1_dl_hbbhww", "ggHH_kl_1_kt_1_dl_hbbhww",
    "ggHH_kl_2p45_kt_1_dl_hbbhww", "ggHH_kl_5_kt_1_dl_hbbhww",
    # HH -> bbZZ(lvlv), ggf
    "ggHH_dl_hbbhzz", "ggHH_kl_0_kt_1_dl_hbbhzz", "ggHH_kl_1_kt_1_dl_hbbhzz",
    "ggHH_kl_2p45_kt_1_dl_hbbhzz", "ggHH_kl_5_kt_1_dl_hbbhzz",
    # HH -> bbWW(qqlv), vbf
    "qqHH_sl_hbbhww", "qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww", "qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_0_kl_1_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_0_sl_hbbhww", "qqHH_CV_1_C2V_1_kl_1_sl_hbbhww",
    "qqHH_CV_1_C2V_1_kl_2_sl_hbbhww", "qqHH_CV_1_C2V_2_kl_1_sl_hbbhww",
    # HH -> bbWW(lvlv), vbf
    "qqHH_dl_hbbhww", "qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww", "qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww",
    "qqHH_CV_1_C2V_0_kl_1_dl_hbbhww", "qqHH_CV_1_C2V_1_kl_0_dl_hbbhww", "qqHH_CV_1_C2V_1_kl_1_dl_hbbhww",
    "qqHH_CV_1_C2V_1_kl_2_dl_hbbhww", "qqHH_CV_1_C2V_2_kl_1_dl_hbbhww",
    # HH -> bbZZ(lvlv), vbf
    "qqHH_dl_hbbhzz", "qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhzz", "qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhzz",
    "qqHH_CV_1_C2V_0_kl_1_dl_hbbhzz", "qqHH_CV_1_C2V_1_kl_0_dl_hbbhzz", "qqHH_CV_1_C2V_1_kl_1_dl_hbbhzz",
    "qqHH_CV_1_C2V_1_kl_2_dl_hbbhzz", "qqHH_CV_1_C2V_2_kl_1_dl_hbbhzz",
    # Resonant HH -> bbWW: radion
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
    # Resonant HH -> bbWW: graviton
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
from cmsdb.util import multiply_xsecs
from cmsdb.processes.higgs import (
    hh_ggf, ggHH_kl_0_kt_1, ggHH_kl_1_kt_1, ggHH_kl_2p45_kt_1, ggHH_kl_5_kt_1,
    hh_vbf, qqHH_CV_1_C2V_1_kl_1, qqHH_CV_1_C2V_1_kl_0, qqHH_CV_1_C2V_1_kl_2,
    qqHH_CV_1_C2V_0_kl_1, qqHH_CV_1_C2V_2_kl_1, qqHH_CV_0p5_C2V_1_kl_1, qqHH_CV_1p5_C2V_1_kl_1,
    radion_hh_ggf, graviton_hh_ggf,
)

#
# Helper
#

br_bbvv = const.br_hh.bbww + const.br_hh.bbzz
br_bbvv_dl = const.br_hh.bbww * const.br_ww.dl + const.br_hh.bbzz * const.br_z.clep ** 2
br_bbww_sl = const.br_hh.bbww * const.br_ww.sl
br_bbww_dl = const.br_hh.bbww * const.br_ww.dl
br_bbzz_dl = const.br_hh.bbzz * const.br_ww.dl

#
# HH -> bbVV
#

ggHH_hbbhvv = hh_ggf.add_process(
    name="ggHH_hbbhvv",
    id=21400,
    label=r"$HH_{ggf} \rightarrow bbVV$",
)

qqHH_hbbhvv = hh_vbf.add_process(
    name="qqHH_hbbhvv",
    id=22400,
    label=r"$HH_{vbf} \rightarrow bbVV$",
)

ggHH_hbbhww = ggHH_hbbhvv.add_process(
    name="ggHH_hbbhww",
    id=21200,
    label=r"$HH_{ggf} \rightarrow bbWW$",
)

qqHH_hbbhww = qqHH_hbbhvv.add_process(
    name="qqHH_hbbhww",
    id=22200,
    label=r"$HH_{vbf} \rightarrow bbWW$",
)

ggHH_hbbhzz = ggHH_hbbhvv.add_process(
    name="ggHH_hbbhzz",
    id=21300,
    label=r"$HH_{ggf} \rightarrow bbZZ$",
)

qqHH_hbbhzz = qqHH_hbbhvv.add_process(
    name="qqHH_hbbhzz",
    id=22300,
    label=r"$HH_{vbf} \rightarrow bbZZ$",

)
#
# HH -> bbVV, ggf
#

ggHH_kl_0_kt_1_hbbhvv = ggHH_kl_0_kt_1.add_process(
    name="ggHH_kl_0_kt_1_hbbhvv",
    id=21401,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbVV$",
    xsecs=multiply_xsecs(ggHH_kl_0_kt_1, br_bbvv),
)

ggHH_kl_1_kt_1_hbbhvv = ggHH_kl_1_kt_1.add_process(
    name="ggHH_kl_1_kt_1_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbVV$",
    id=21402,
    xsecs=multiply_xsecs(ggHH_kl_1_kt_1, br_bbvv),
)

ggHH_kl_2p45_kt_1_hbbhvv = ggHH_kl_2p45_kt_1.add_process(
    name="ggHH_kl_2p45_kt_1_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbVV$",
    id=21403,
    xsecs=multiply_xsecs(ggHH_kl_2p45_kt_1, br_bbvv),
)

ggHH_kl_5_kt_1_hbbhvv = ggHH_kl_5_kt_1.add_process(
    name="ggHH_kl_5_kt_1_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbVV$",
    id=21404,
    xsecs=multiply_xsecs(ggHH_kl_5_kt_1, br_bbvv),
)

# add process dependencies
ggHH_hbbhvv.add_process(ggHH_kl_0_kt_1_hbbhvv)
ggHH_hbbhvv.add_process(ggHH_kl_1_kt_1_hbbhvv)
ggHH_hbbhvv.add_process(ggHH_kl_2p45_kt_1_hbbhvv)
ggHH_hbbhvv.add_process(ggHH_kl_5_kt_1_hbbhvv)

#
# HH -> bbVV, vbf
#

qqHH_CV_1_C2V_1_kl_1_hbbhvv = qqHH_CV_1_C2V_1_kl_1.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_hbbhvv",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbVV$",
    id=22401,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_1, br_bbvv),
)

qqHH_CV_1_C2V_1_kl_0_hbbhvv = qqHH_CV_1_C2V_1_kl_0.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_hbbhvv",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbVV$",
    id=22402,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_0, br_bbvv),
)

qqHH_CV_1_C2V_1_kl_2_hbbhvv = qqHH_CV_1_C2V_1_kl_2.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_hbbhvv",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbVV$",
    id=22403,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_2, br_bbvv),
)

qqHH_CV_1_C2V_0_kl_1_hbbhvv = qqHH_CV_1_C2V_0_kl_1.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_hbbhvv",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbVV$",
    id=22404,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_0_kl_1, br_bbvv),
)

qqHH_CV_1_C2V_2_kl_1_hbbhvv = qqHH_CV_1_C2V_2_kl_1.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_hbbhvv",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbVV$",
    id=22405,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_2_kl_1, br_bbvv),
)

qqHH_CV_0p5_C2V_1_kl_1_hbbhvv = qqHH_CV_0p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_hbbhvv",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbVV$",
    id=22406,
    xsecs=multiply_xsecs(qqHH_CV_0p5_C2V_1_kl_1, br_bbvv),
)

qqHH_CV_1p5_C2V_1_kl_1_hbbhvv = qqHH_CV_1p5_C2V_1_kl_1.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_hbbhvv",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbVV$",
    id=22407,
    xsecs=multiply_xsecs(qqHH_CV_1p5_C2V_1_kl_1, br_bbvv),
)

# add process dependencies
qqHH_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_1_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_0_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_2_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_1_C2V_0_kl_1_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_1_C2V_2_kl_1_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_0p5_C2V_1_kl_1_hbbhvv)
qqHH_hbbhvv.add_process(qqHH_CV_1p5_C2V_1_kl_1_hbbhvv)

#
# HH -> bbVV(2l2v), ggf
#

ggHH_dl_hbbhvv = ggHH_hbbhvv.add_process(
    name="ggHH_dl_hbbhvv",
    id=21320,
    label=r"$HH_{ggf} \rightarrow bbVV(2l2\nu)$",
)

ggHH_kl_0_kt_1_dl_hbbhvv = ggHH_kl_0_kt_1_hbbhvv.add_process(
    name="ggHH_kl_0_kt_1_dl_hbbhvv",
    id=21321,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbVV(2l2\nu)$",
    xsecs=multiply_xsecs(ggHH_kl_0_kt_1, br_bbvv_dl),
)

ggHH_kl_1_kt_1_dl_hbbhvv = ggHH_kl_1_kt_1_hbbhvv.add_process(
    name="ggHH_kl_1_kt_1_dl_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbVV(2l2\nu)$",
    id=21322,
    xsecs=multiply_xsecs(ggHH_kl_1_kt_1, br_bbvv_dl),
)

ggHH_kl_2p45_kt_1_dl_hbbhvv = ggHH_kl_2p45_kt_1_hbbhvv.add_process(
    name="ggHH_kl_2p45_kt_1_dl_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbVV(2l2\nu)$",
    id=21323,
    xsecs=multiply_xsecs(ggHH_kl_2p45_kt_1, br_bbvv_dl),
)

ggHH_kl_5_kt_1_dl_hbbhvv = ggHH_kl_5_kt_1_hbbhvv.add_process(
    name="ggHH_kl_5_kt_1_dl_hbbhvv",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbVV(2l2\nu)$",
    id=21324,
    xsecs=multiply_xsecs(ggHH_kl_5_kt_1, br_bbvv_dl),
)


# add process dependencies
ggHH_dl_hbbhvv.add_process(ggHH_kl_0_kt_1_dl_hbbhvv)
ggHH_dl_hbbhvv.add_process(ggHH_kl_1_kt_1_dl_hbbhvv)
ggHH_dl_hbbhvv.add_process(ggHH_kl_2p45_kt_1_dl_hbbhvv)
ggHH_dl_hbbhvv.add_process(ggHH_kl_5_kt_1_dl_hbbhvv)


#
# HH -> bbVV(2l2v), vbf
#

qqHH_dl_hbbhvv = qqHH_hbbhvv.add_process(
    name="qqHH_dl_hbbhvv",
    label=r"$HH_{vbf} \rightarrow bbVV(2l2\nu)$",
    id=22420,
)

qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv = qqHH_CV_1_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbVV(2l2\nu)$",
    id=22421,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_1, br_bbvv_dl),
)

qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv = qqHH_CV_1_C2V_1_kl_0_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbVV(2l2\nu)$",
    id=22422,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_0, br_bbvv_dl),
)

qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv = qqHH_CV_1_C2V_1_kl_2_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbVV(2l2\nu)$",
    id=22423,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_2, br_bbvv_dl),
)

qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv = qqHH_CV_1_C2V_0_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbVV(2l2\nu)$",
    id=22424,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_0_kl_1, br_bbvv_dl),
)

qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv = qqHH_CV_1_C2V_2_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbVV(2l2\nu)$",
    id=22425,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_2_kl_1, br_bbvv_dl),
)

qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv = qqHH_CV_0p5_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbVV(2l2\nu)$",
    id=22426,
    xsecs=multiply_xsecs(qqHH_CV_0p5_C2V_1_kl_1, br_bbvv_dl),
)

qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv = qqHH_CV_1p5_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbVV(2l2\nu)$",
    id=22427,
    xsecs=multiply_xsecs(qqHH_CV_1p5_C2V_1_kl_1, br_bbvv_dl),
)

# add process dependencies
qqHH_dl_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv)
qqHH_dl_hbbhvv.add_process(qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv)

#
# NOTE: HH -> bbWW(incl) not yet included
#

#
# HH -> bbWW(qqlv), ggf
#

ggHH_sl_hbbhww = ggHH_hbbhww.add_process(
    name="ggHH_sl_hbbhww",
    id=21210,
    label=r"$HH_{ggf} \rightarrow bbWW(qql\nu)$",
)

ggHH_kl_0_kt_1_sl_hbbhww = ggHH_kl_0_kt_1_hbbhvv.add_process(
    name="ggHH_kl_0_kt_1_sl_hbbhww",
    id=21211,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbWW(qql\nu)$",
    xsecs=multiply_xsecs(ggHH_kl_0_kt_1, br_bbww_sl),
)

ggHH_kl_1_kt_1_sl_hbbhww = ggHH_kl_1_kt_1_hbbhvv.add_process(
    name="ggHH_kl_1_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbWW(qql\nu)$",
    id=21212,
    xsecs=multiply_xsecs(ggHH_kl_1_kt_1, br_bbww_sl),
)

ggHH_kl_2p45_kt_1_sl_hbbhww = ggHH_kl_2p45_kt_1_hbbhvv.add_process(
    name="ggHH_kl_2p45_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbWW(qql\nu)$",
    id=21213,
    xsecs=multiply_xsecs(ggHH_kl_2p45_kt_1, br_bbww_sl),
)

ggHH_kl_5_kt_1_sl_hbbhww = ggHH_kl_5_kt_1_hbbhvv.add_process(
    name="ggHH_kl_5_kt_1_sl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbWW(qql\nu)$",
    id=21214,
    xsecs=multiply_xsecs(ggHH_kl_5_kt_1, br_bbww_sl),
)

# add process dependencies
ggHH_sl_hbbhww.add_process(ggHH_kl_0_kt_1_sl_hbbhww)
ggHH_sl_hbbhww.add_process(ggHH_kl_1_kt_1_sl_hbbhww)
ggHH_sl_hbbhww.add_process(ggHH_kl_2p45_kt_1_sl_hbbhww)
ggHH_sl_hbbhww.add_process(ggHH_kl_5_kt_1_sl_hbbhww)

#
# HH -> bbWW(lvlv), ggf
#

ggHH_dl_hbbhww = ggHH_hbbhww.add_process(
    name="ggHH_dl_hbbhww",
    id=21220,
    label=r"$HH_{ggf} \rightarrow bbWW(l\nu l\nu)$",
)

ggHH_kl_0_kt_1_dl_hbbhww = ggHH_kl_0_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_0_kt_1_dl_hbbhww",
    id=21221,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbWW(l\nu l\nu)$",
    xsecs=multiply_xsecs(ggHH_kl_0_kt_1, br_bbww_dl),
)

ggHH_kl_1_kt_1_dl_hbbhww = ggHH_kl_1_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_1_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbWW(l\nu l\nu)$",
    id=21222,
    xsecs=multiply_xsecs(ggHH_kl_1_kt_1, br_bbww_dl),
)

ggHH_kl_2p45_kt_1_dl_hbbhww = ggHH_kl_2p45_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_2p45_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbWW(l\nu l\nu)$",
    id=21223,
    xsecs=multiply_xsecs(ggHH_kl_2p45_kt_1, br_bbww_dl),
)

ggHH_kl_5_kt_1_dl_hbbhww = ggHH_kl_5_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_5_kt_1_dl_hbbhww",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbWW(l\nu l\nu)$",
    id=21224,
    xsecs=multiply_xsecs(ggHH_kl_5_kt_1, br_bbww_dl),
)


# add process dependencies
ggHH_dl_hbbhww.add_process(ggHH_kl_0_kt_1_dl_hbbhww)
ggHH_dl_hbbhww.add_process(ggHH_kl_1_kt_1_dl_hbbhww)
ggHH_dl_hbbhww.add_process(ggHH_kl_2p45_kt_1_dl_hbbhww)
ggHH_dl_hbbhww.add_process(ggHH_kl_5_kt_1_dl_hbbhww)

#
# HH -> bbWW(qqlv), vbf
#

qqHH_sl_hbbhww = qqHH_hbbhww.add_process(
    name="qqHH_sl_hbbhww",
    label=r"$HH_{vbf} \rightarrow bbWW(qql\nu)$",
    id=22210,
)

qqHH_CV_1_C2V_1_kl_1_sl_hbbhww = qqHH_CV_1_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbWW(qql\nu)$",
    id=22211,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_1, br_bbww_sl),
)

qqHH_CV_1_C2V_1_kl_0_sl_hbbhww = qqHH_CV_1_C2V_1_kl_0_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbWW(qql\nu)$",
    id=22212,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_0, br_bbww_sl),
)

qqHH_CV_1_C2V_1_kl_2_sl_hbbhww = qqHH_CV_1_C2V_1_kl_2_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_sl_hbbhww",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbWW(qql\nu)$",
    id=22213,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_2, br_bbww_sl),
)

qqHH_CV_1_C2V_0_kl_1_sl_hbbhww = qqHH_CV_1_C2V_0_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbWW(qql\nu)$",
    id=22214,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_0_kl_1, br_bbww_sl),
)

qqHH_CV_1_C2V_2_kl_1_sl_hbbhww = qqHH_CV_1_C2V_2_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbWW(qql\nu)$",
    id=22215,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_2_kl_1, br_bbww_sl),
)

qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww = qqHH_CV_0p5_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22216,
    xsecs=multiply_xsecs(qqHH_CV_0p5_C2V_1_kl_1, br_bbww_sl),
)

qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww = qqHH_CV_1p5_C2V_1_kl_1_hbbhvv.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbWW(qql\nu)$",
    id=22217,
    xsecs=multiply_xsecs(qqHH_CV_1p5_C2V_1_kl_1, br_bbww_sl),
)

# add process dependencies
qqHH_sl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_1_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_0_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_2_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_1_C2V_0_kl_1_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_1_C2V_2_kl_1_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhww)
qqHH_sl_hbbhww.add_process(qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhww)

#
# HH -> bbWW(lvlv), vbf
#

qqHH_dl_hbbhww = qqHH_hbbhww.add_process(
    name="qqHH_dl_hbbhww",
    label=r"$HH_{vbf} \rightarrow bbWW(l\nu l\nu)$",
    id=22220,
)

qqHH_CV_1_C2V_1_kl_1_dl_hbbhww = qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22221,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_1, br_bbww_dl),
)

qqHH_CV_1_C2V_1_kl_0_dl_hbbhww = qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbWW(l\nu l\nu)$",
    id=22222,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_0, br_bbww_dl),
)

qqHH_CV_1_C2V_1_kl_2_dl_hbbhww = qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_dl_hbbhww",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbWW(l\nu l\nu)$",
    id=22223,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_2, br_bbww_dl),
)

qqHH_CV_1_C2V_0_kl_1_dl_hbbhww = qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22224,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_0_kl_1, br_bbww_dl),
)

qqHH_CV_1_C2V_2_kl_1_dl_hbbhww = qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22225,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_2_kl_1, br_bbww_dl),
)

qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww = qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22226,
    xsecs=multiply_xsecs(qqHH_CV_0p5_C2V_1_kl_1, br_bbww_dl),
)

qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww = qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbWW(l\nu l\nu)$",
    id=22227,
    xsecs=multiply_xsecs(qqHH_CV_1p5_C2V_1_kl_1, br_bbww_dl),
)

# add process dependencies
qqHH_dl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_1_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_0_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_1_C2V_1_kl_2_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_1_C2V_0_kl_1_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_1_C2V_2_kl_1_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhww)
qqHH_dl_hbbhww.add_process(qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhww)

#
# HH -> bbZZ, ggf
#

ggHH_dl_hbbhzz = ggHH_hbbhzz.add_process(
    name="ggHH_dl_hbbhzz",
    id=21320,
    label=r"$HH_{ggf} \rightarrow bbZZ(ll \nu \nu)$",
)

ggHH_kl_0_kt_1_dl_hbbhzz = ggHH_kl_0_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_0_kt_1_dl_hbbhzz",
    id=21321,
    label=r"$HH_{ggf}^{\kappa\lambda=0} \rightarrow bbZZ(ll \nu \nu)$",
    xsecs=multiply_xsecs(ggHH_kl_0_kt_1, br_bbzz_dl),
)

ggHH_kl_1_kt_1_dl_hbbhzz = ggHH_kl_1_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_1_kt_1_dl_hbbhzz",
    label=r"$HH_{ggf}^{\kappa\lambda=1} \rightarrow bbZZ(ll \nu \nu)$",
    id=21322,
    xsecs=multiply_xsecs(ggHH_kl_1_kt_1, br_bbzz_dl),
)

ggHH_kl_2p45_kt_1_dl_hbbhzz = ggHH_kl_2p45_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_2p45_kt_1_dl_hbbhzz",
    label=r"$HH_{ggf}^{\kappa\lambda=2.45} \rightarrow bbZZ(ll \nu \nu)$",
    id=21323,
    xsecs=multiply_xsecs(ggHH_kl_2p45_kt_1, br_bbzz_dl),
)

ggHH_kl_5_kt_1_dl_hbbhzz = ggHH_kl_5_kt_1_dl_hbbhvv.add_process(
    name="ggHH_kl_5_kt_1_dl_hbbhzz",
    label=r"$HH_{ggf}^{\kappa\lambda=5} \rightarrow bbZZ(ll \nu \nu)$",
    id=21324,
    xsecs=multiply_xsecs(ggHH_kl_5_kt_1, br_bbzz_dl),
)


# add process dependencies
ggHH_dl_hbbhzz.add_process(ggHH_kl_0_kt_1_dl_hbbhzz)
ggHH_dl_hbbhzz.add_process(ggHH_kl_1_kt_1_dl_hbbhzz)
ggHH_dl_hbbhzz.add_process(ggHH_kl_2p45_kt_1_dl_hbbhzz)
ggHH_dl_hbbhzz.add_process(ggHH_kl_5_kt_1_dl_hbbhzz)


#
# HH -> bbZZ(lvlv), vbf
#

qqHH_dl_hbbhzz = qqHH_hbbhzz.add_process(
    name="qqHH_dl_hbbhzz",
    label=r"$HH_{vbf} \rightarrow bbZZ(ll \nu \nu)$",
    id=22320,
)

qqHH_CV_1_C2V_1_kl_1_dl_hbbhzz = qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_1_dl_hbbhzz",
    label=r"$HH_{vbf}^{1,1,1} \rightarrow bbZZ(ll \nu \nu)$",
    id=22321,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_1, br_bbzz_dl),
)

qqHH_CV_1_C2V_1_kl_0_dl_hbbhzz = qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_0_dl_hbbhzz",
    label=r"$HH_{vbf}^{1,1,0} \rightarrow bbZZ(ll \nu \nu)$",
    id=22322,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_0, br_bbzz_dl),
)

qqHH_CV_1_C2V_1_kl_2_dl_hbbhzz = qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_1_kl_2_dl_hbbhzz",
    label=r"$HH_{vbf}^{1,1,2} \rightarrow bbZZ(ll \nu \nu)$",
    id=22323,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_1_kl_2, br_bbzz_dl),
)

qqHH_CV_1_C2V_0_kl_1_dl_hbbhzz = qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_0_kl_1_dl_hbbhzz",
    label=r"$HH_{vbf}^{1,0,1} \rightarrow bbZZ(ll \nu \nu)$",
    id=22324,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_0_kl_1, br_bbzz_dl),
)

qqHH_CV_1_C2V_2_kl_1_dl_hbbhzz = qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1_C2V_2_kl_1_dl_hbbhzz",
    label=r"$HH_{vbf}^{1,2,1} \rightarrow bbZZ(ll \nu \nu)$",
    id=22325,
    xsecs=multiply_xsecs(qqHH_CV_1_C2V_2_kl_1, br_bbzz_dl),
)

qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhzz = qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhzz",
    label=r"$HH_{vbf}^{0.5,1,1} \rightarrow bbZZ(ll \nu \nu)$",
    id=22326,
    xsecs=multiply_xsecs(qqHH_CV_0p5_C2V_1_kl_1, br_bbzz_dl),
)

qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhzz = qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv.add_process(
    name="qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhzz",
    label=r"$HH_{vbf}^{1.5,1,1} \rightarrow bbZZ(ll \nu \nu)$",
    id=22327,
    xsecs=multiply_xsecs(qqHH_CV_1p5_C2V_1_kl_1, br_bbzz_dl),
)

# add process dependencies
qqHH_dl_hbbhzz.add_process(qqHH_CV_1_C2V_1_kl_1_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_1_C2V_1_kl_0_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_1_C2V_1_kl_2_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_1_C2V_0_kl_1_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_1_C2V_2_kl_1_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhzz)
qqHH_dl_hbbhzz.add_process(qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhzz)

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
