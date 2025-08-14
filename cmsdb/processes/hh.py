# coding: utf-8

"""
Di-Higgs process definitions.

- hh: inclusive di-Higgs production
- hh_ggf: di-Higgs production via gluon-gluon fusion
- hh_vbf: di-Higgs production via vector boson fusion
- radion: radion production
- graviton: graviton production

Di-Higgs production channels:
- 20xxx: HH
- 21xxx: hh_ggf
- 22xxx: hh_vbf
- 23xxx: radion HH
- 24xxx: graviton HH
- 25xxx: radion VBF
- 26xxx: graviton VBF

"""

from __future__ import annotations

from order import Process
from scinum import Number

from cmsdb.util import add_xsecs


__all__ = [
    # Di-Higgs
    "hh",
    "hh_ggf", "hh_ggf_kl0_kt1", "hh_ggf_kl1_kt1", "hh_ggf_kl2p45_kt1", "hh_ggf_kl5_kt1",
    "hh_ggf_kl0_kt1_c21", "hh_ggf_kl1_kt1_c20p10", "hh_ggf_kl1_kt1_c20p35",
    "hh_ggf_kl1_kt1_c23", "hh_ggf_kl1_kt1_c2m2",
    "hh_vbf", "hh_vbf_kv1_k2v1_kl1", "hh_vbf_kv1_k2v1_kl0", "hh_vbf_kv1_k2v1_kl2",
    "hh_vbf_kv1_k2v0_kl1", "hh_vbf_kv1_k2v2_kl1", "hh_vbf_kv0p5_k2v1_kl1", "hh_vbf_kv1p5_k2v1_kl1",
    "hh_vbf_kv1p74_k2v1p37_kl14p4", "hh_vbf_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_kvm0p758_k2v1p44_klm19p3", "hh_vbf_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_kvm1p21_k2v1p94_klm0p94", "hh_vbf_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_kvm1p83_k2v3p57_klm3p39", "hh_vbf_kv2p12_k2v3p87_klm5p96",
    "radion_hh_ggf", "graviton_hh_ggf",
    "radion_hh_vbf", "graviton_hh_vbf",
]

####################################################################################################
#
# HH
#
####################################################################################################


# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=98#Current_recommendations_for_HH_c
# scale is according to recommendation: scale + mtop unc
# pdf is according to recommendation: pdf + aS
# NNLO

# scaling formula in fb
hh_xsec_13p0 = lambda kl: 68.5624 - 48.3673 * kl + 10.5635 * kl**2
hh_unc_scale_hi_13p0 = lambda kl: 75.4551 - 55.401 * kl + 12.4555 * kl**2
hh_unc_scale_lo_13p0 = lambda kl: 56.5063 - 41.9131 * kl + 9.30669 * kl**2
hh_unc_scale_up_13p0 = lambda kl: max(hh_unc_scale_hi_13p0(kl), hh_unc_scale_lo_13p0(kl))
hh_unc_scale_down_13p0 = lambda kl: min(hh_unc_scale_hi_13p0(kl), hh_unc_scale_lo_13p0(kl))

hh_xsec_13p6 = lambda kl: 75.7617 - 53.2855 * kl + 11.6126 * kl**2
hh_unc_scale_hi_13p6 = lambda kl: 83.3897 - 61.0213 * kl + 13.6898 * kl**2
hh_unc_scale_lo_13p6 = lambda kl: 62.4328 - 46.1854 * kl + 10.2342 * kl**2
hh_unc_scale_up_13p6 = lambda kl: max(hh_unc_scale_hi_13p6(kl), hh_unc_scale_lo_13p6(kl))
hh_unc_scale_down_13p6 = lambda kl: min(hh_unc_scale_hi_13p6(kl), hh_unc_scale_lo_13p6(kl))

hh = Process(
    name="hh",
    id=20000,
    label="HH",
)

hh_ggf = hh.add_process(
    name="hh_ggf",
    id=21000,
    label=r"$HH_{ggf}$",
    aux={"production_mode_parent": hh},
)

# Naming conventions, cross sections and uncertainties are based on:
# https://gitlab.cern.ch/hh/naming-conventions

hh_ggf_kl1_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1",
    id=21002,
    label=r"$HH_{ggf}^{\kappa_\lambda=1}$",
    xsecs={
        # sm values taken from summary table on twiki
        13: 0.001 * Number(30.77, {
            "pdf": 0.023j,
            "scale": (0.06j, 0.23j),
        }),
        13.6: 0.001 * Number(34.13, {
            "pdf": 0.023j,
            "scale": (0.06j, 0.23j),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl0_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl0_kt1",
    id=21001,
    label=r"$HH_{ggf}^{\kappa_\lambda=0}$",
    xsecs={
        13: 0.001 * Number(hh_xsec_13p0(0), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p0(0), hh_unc_scale_down_13p0(0)),
        }),
        13.6: 0.001 * Number(hh_xsec_13p6(0), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p6(0), hh_unc_scale_down_13p6(0)),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl2p45_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl2p45_kt1",
    id=21003,
    label=r"$HH_{ggf}^{\kappa_\lambda=2.45}$",
    xsecs={
        13: 0.001 * Number(hh_xsec_13p0(2.45), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p0(2.45), hh_unc_scale_down_13p0(2.45)),
        }),
        13.6: 0.001 * Number(hh_xsec_13p6(2.45), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p6(2.45), hh_unc_scale_down_13p6(2.45)),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl5_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl5_kt1",
    id=21004,
    label=r"$HH_{ggf}^{\kappa_\lambda=5}$",
    xsecs={
        13: 0.001 * Number(hh_xsec_13p0(5), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p0(5), hh_unc_scale_down_13p0(5)),
        }),
        13.6: 0.001 * Number(hh_xsec_13p6(5), {
            "pdf": 0.023j,
            "scale": (hh_unc_scale_up_13p6(5), hh_unc_scale_down_13p6(5)),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl0_kt1_c21 = hh_ggf.add_process(
    name="hh_ggf_kl0_kt1_c21",
    id=21005,
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl1_kt1_c20p10 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1_c20p10",
    id=21006,
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl1_kt1_c20p35 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1_c20p35",
    id=21007,
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl1_kt1_c23 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1_c23",
    id=21008,
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl1_kt1_c2m2 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1_c2m2",
    id=21009,
    aux={"production_mode_parent": hh_ggf},
)

"""
Source: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=98#HHjj_VBF
Extraction workflow for VBF cross sections:
- values are taken for m_H = 125 GeV
- LO values from XSDB, see e.g.:
https://xsdb-temp.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=process_name%3D%5EVBFHHto2B2Tau_CV.%2B_C2V.%2B_C3.%2B_.%2A13p6TeV.%2A%24  # noqa
- xsecs were given in fb but are converted to pb
- k-factor derived by comparing SM LO value to N3LO value from Twiki above
- it is assumed to be constant across all other kappas and multiplied to corresponding LO values
- uncertainties are constant and taken from the Twiki above
"""

hh_vbf_uncs_13p0 = {
    "scale": (0.0005j, 0.0004j),
    "pdf": 0.027j,
}
hh_vbf_uncs_13p6 = {
    "scale": (0.0005j, 0.0003j),
    "pdf": 0.027j,
}

hh_vbf = hh.add_process(
    name="hh_vbf",
    id=22000,
    label=r"$HH_{vbf}$",
    aux={"production_mode_parent": hh},
)

hh_vbf_kv1_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl1",
    id=22001,
    xsecs={
        13: Number(1.687, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(1.874, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

# the kappa values are defined as the N3LO cross section divided by the LO cross section as taken
# from XSDB (see link above), with all kappas at 1 (SM configuration)
hh_vbf_k_13p0 = hh_vbf_kv1_k2v1_kl1.get_xsec(13).nominal / (1.626 * 0.001)
hh_vbf_k_13p6 = hh_vbf_kv1_k2v1_kl1.get_xsec(13.6).nominal / (1.912 * 0.001)

hh_vbf_kv1_k2v1_kl0 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl0",
    id=22002,
    xsecs={
        13: Number(4.337 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        # no 13p6TeV sample generated, but we could use the scaling formula in the hh tools
        # 13.6: Number(TODO * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v1_kl2 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl2",
    id=22003,
    xsecs={
        13: Number(1.325 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(1.593 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v0_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v0_kl1",
    id=22004,
    xsecs={
        13: Number(26.08 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(29.32 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v2_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v2_kl1",
    id=22005,
    xsecs={
        13: Number(14.05 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(15.71 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv0p5_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv0p5_k2v1_kl1",
    id=22006,
    xsecs={
        13: Number(10.47 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        # no 13p6TeV sample generated, but we could use the scaling formula in the hh tools
        # 13.6: Number(TODO * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1p5_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1p5_k2v1_kl1",
    id=22007,
    xsecs={
        13: Number(63.99 * hh_vbf_k_13p0, hh_vbf_uncs_13p0) * 0.001,
        # no 13p6TeV sample generated, but we could use the scaling formula in the hh tools
        # 13.6: Number(TODO * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1p74_k2v1p37_kl14p4 = hh_vbf.add_process(
    name="hh_vbf_kv1p74_k2v1p37_kl14p4",
    id=22008,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(395.4 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm0p012_k2v0p03_kl10p2 = hh_vbf.add_process(
    name="hh_vbf_kvm0p012_k2v0p03_kl10p2",
    id=22009,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(0.01257 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm0p758_k2v1p44_klm19p3 = hh_vbf.add_process(
    name="hh_vbf_kvm0p758_k2v1p44_klm19p3",
    id=22010,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(355.0 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm0p962_k2v0p959_klm1p43 = hh_vbf.add_process(
    name="hh_vbf_kvm0p962_k2v0p959_klm1p43",
    id=22011,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(1.114 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm1p21_k2v1p94_klm0p94 = hh_vbf.add_process(
    name="hh_vbf_kvm1p21_k2v1p94_klm0p94",
    id=22012,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(3.753 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm1p6_k2v2p72_klm1p36 = hh_vbf.add_process(
    name="hh_vbf_kvm1p6_k2v2p72_klm1p36",
    id=22013,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(11.56 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kvm1p83_k2v3p57_klm3p39 = hh_vbf.add_process(
    name="hh_vbf_kvm1p83_k2v3p57_klm3p39",
    id=22014,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(16.65 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv2p12_k2v3p87_klm5p96 = hh_vbf.add_process(
    name="hh_vbf_kv2p12_k2v3p87_klm5p96",
    id=22015,
    xsecs={
        # no 13p0TeV sample generated, but we could use the scaling formula in the hh tools
        # 13: Number(TODO, hh_vbf_uncs_13p0) * 0.001,
        13.6: Number(671.9 * hh_vbf_k_13p6, hh_vbf_uncs_13p6) * 0.001,
    },
    aux={"production_mode_parent": hh_vbf},
)

hh.xsecs = add_xsecs(hh_ggf, hh_vbf)

####################################################################################################
#
# Resonant BSM HH production
#
####################################################################################################

# cross sections values chosen for inference tools, 1pb for inclusive process as documented in:
# https://cms-hh.web.cern.ch/cms-hh/tools/inference/tasks/resonant.html#resonant-limits

radion_hh_ggf = hh_ggf.add_process(
    name="radion_hh_ggf",
    id=23000,
    label=r"Radion $\rightarrow HH_{ggf}$",
    xsecs={
        13: Number(1.0),  # value for inference tools
        13.6: Number(1.0),  # value for inference tools
    },
)

graviton_hh_ggf = hh_ggf.add_process(
    name="graviton_hh_ggf",
    id=24000,
    label=r"Graviton $\rightarrow HH_{ggf}$",
    xsecs={
        13: Number(1.0),  # value for inference tools
        13.6: Number(1.0),  # value for inference tools
    },
)

radion_hh_vbf = hh_vbf.add_process(
    name="radion_hh_vbf",
    id=25000,
    label=r"Radion $\rightarrow HH_{vbf}$",
    xsecs={
        13: Number(1.0),  # value for inference tools
        13.6: Number(1.0),  # value for inference tools
    },
)

graviton_hh_vbf = hh_vbf.add_process(
    name="graviton_hh_vbf",
    id=26000,
    label=r"Graviton $\rightarrow HH_{vbf}$",
    xsecs={
        13: Number(1.0),  # value for inference tools
        13.6: Number(1.0),  # value for inference tools
    },
)
