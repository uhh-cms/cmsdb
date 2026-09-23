# coding: utf-8

"""
EWK-related process definitions.

Some DY processes contain phasespace ranges in auxiliary fields. Each each is inclusive in the lower
bound and exclusive in the upper bound, i.e. (a, b) means a <= x < b:

- mll: dilepton invariant mass range
- ptll: dilepton pt range
- njets: number of extra jets on generator level (mostly NLO)
"""

__all__ = [  # noqa: F822
    "dy",
    "dy_m4to10",
    "dy_m10to50",
    "dy_m50toinf", "dy_m50toinf_0j", "dy_m50toinf_1j", "dy_m50toinf_2j", "dy_m50toinf_ge3j",
    "dy_m50toinf_3j", "dy_m50toinf_4j", "dy_m50toinf_ge3j",
    "dy_m50toinf_1j_pt0to40", "dy_m50toinf_1j_pt40to100", "dy_m50toinf_1j_pt100to200",
    "dy_m50toinf_1j_pt200to400", "dy_m50toinf_1j_pt400to600", "dy_m50toinf_1j_pt600toinf",
    "dy_m50toinf_2j_pt0to40", "dy_m50toinf_2j_pt40to100", "dy_m50toinf_2j_pt100to200",
    "dy_m50toinf_2j_pt200to400", "dy_m50toinf_2j_pt400to600", "dy_m50toinf_2j_pt600toinf",
    "dy_0j", "dy_1j", "dy_2j",
    "dy_m50toinf_ht70to100", "dy_m50toinf_ht100to200", "dy_m50toinf_ht200to400",
    "dy_m50toinf_ht400to600", "dy_m50toinf_ht600to800", "dy_m50toinf_ht800to1200",
    "dy_m50toinf_ht1200to2500", "dy_m50toinf_ht2500toinf",
    "dy_pt0to50", "dy_pt50to100", "dy_pt100to250", "dy_pt250to400",
    "dy_pt400to650", "dy_pt650toinf",
    "dy_m4to50_ht40to70", "dy_m4to50_ht70to100", "dy_m4to50_ht100to400", "dy_m4to50_ht400to800",
    "dy_m4to50_ht800to1500", "dy_m4to50_ht1500to2500", "dy_m4to50_ht2500toinf",
    "dy_m50toinf_pt40to100", "dy_m50toinf_pt100to200", "dy_m50toinf_pt200to400",
    "dy_m50toinf_pt400to600", "dy_m50toinf_pt600toinf",
    "dy_ee", "dy_mumu", "dy_tautau",
    "dy_ee_m10to50", "dy_ee_m50toinf", "dy_ee_m50to120", "dy_ee_m120to200", "dy_ee_m200to400",
    "dy_ee_m400to800", "dy_ee_m800to1500", "dy_ee_m1500to2500", "dy_ee_m2500to4000",
    "dy_ee_m4000to6000", "dy_ee_m6000toinf",
    "dy_mumu_m10to50", "dy_mumu_m50toinf", "dy_mumu_m50to120", "dy_mumu_m120to200", "dy_mumu_m200to400",
    "dy_mumu_m400to800", "dy_mumu_m800to1500", "dy_mumu_m1500to2500", "dy_mumu_m2500to4000",
    "dy_mumu_m4000to6000", "dy_mumu_m6000toinf",
    "dy_tautau_m10to50", "dy_tautau_m50toinf", "dy_tautau_m50to120", "dy_tautau_m120to200", "dy_tautau_m200to400",
    "dy_tautau_m400to800", "dy_tautau_m800to1500", "dy_tautau_m1500to2500", "dy_tautau_m2500to4000",
    "dy_tautau_m4000to6000", "dy_tautau_m6000toinf",
    *[
        f"dy_{ll}_m50toinf_{nj}j"
        for ll in ["ee", "mumu", "tautau"]
        for nj in ["0", "1", "2", "ge3"]
    ],
    *[
        f"dy_{ll}_m50toinf_{nj}j_pt{pt}"
        for ll in ["ee", "mumu", "tautau"]
        for nj in ["1", "2"]
        for pt in ["0to40", "40to100", "100to200", "200to400", "400to600", "600toinf"]
    ],
    *[
        f"dy_tautau_m50toinf_{nj}j_{fname}"
        for nj in ["0", "1", "2", "ge3"]
        for fname in ["filtered", "nonfiltered"]
    ],
    *[
        f"dy_tautau_m50toinf_{nj}j_pt{pt}_{fname}"
        for nj in ["1", "2"]
        for pt in ["0to40", "40to100", "100to200", "200to400", "400to600", "600toinf"]
        for fname in ["filtered", "nonfiltered"]
    ],
    "z",
    "z_nunu",
    "z_nunu_ht100to200", "z_nunu_ht200to400", "z_nunu_ht400to600",
    "z_nunu_ht600to800", "z_nunu_ht800to1200", "z_nunu_ht1200to2500",
    "z_nunu_ht2500toinf",
    "z_qq",
    "z_qq_ht200to400", "z_qq_ht400to600", "z_qq_ht600to800", "z_qq_ht800toinf",
    "z_qq_pt100toinf", "z_qq_pt200toinf", "z_qq_pt400toinf", "z_qq_pt600toinf",
    "z_qq_1j_pt100to200", "z_qq_2j_pt100to200", "z_qq_1j_pt200to400", "z_qq_2j_pt200to400",
    "z_qq_1j_pt400to600", "z_qq_2j_pt400to600", "z_qq_1j_pt600toinf", "z_qq_2j_pt600toinf",
    "z_vbf", "z_vbf_zll", "z_vbf_zll_m50toinf", "z_vbf_zqq",
    "w",
    "w_taunu", "w_munu",
    "w_lnu",
    "w_lnu_0j",
    "w_lnu_ht70to100", "w_lnu_ht100to200", "w_lnu_ht200to400", "w_lnu_ht400to600",
    "w_lnu_ht600to800", "w_lnu_ht800to1200", "w_lnu_ht1200to2500", "w_lnu_ht2500toinf",
    "w_lnu_1j", "w_lnu_1j_pt0to40", "w_lnu_1j_pt40to100", "w_lnu_1j_pt100to200", "w_lnu_1j_pt200to400",
    "w_lnu_1j_pt400to600", "w_lnu_1j_pt600toinf",
    "w_lnu_2j", "w_lnu_2j_pt0to40", "w_lnu_2j_pt40to100", "w_lnu_2j_pt100to200", "w_lnu_2j_pt200to400",
    "w_lnu_2j_pt400to600", "w_lnu_2j_pt600toinf", "w_lnu_ge3j", "w_lnu_3j", "w_lnu_4j",
    "w_vbf", "w_vbf_wlnu", "w_vbf_wqq",
    "ewk",
    "ewk_wp_lnu_m50toinf", "ewk_wm_lnu_m50toinf", "ewk_z_ll_m50toinf",
    "vv",
    "zz", "qqzz", "ggzz",
    "zz_zqq_zll", "zz_zll_znunu", "zz_zll_zll", "zz_zqq_zqq", "zz_znunu_zqq",
    "zz_zee_zee", "zz_zee_zmm", "zz_zee_ztt", "zz_zmm_zmm", "zz_zmm_ztt", "zz_ztt_ztt",
    "wz", "wz_wlnu_zll", "wz_wqq_zll", "wz_wqq_zqq", "wz_wlnu_zqq",
    "wzg", "wzg_wlnu",
    "wg_wlnu",
    "dyg",
    "dyg_m50toinf", "dyg_m50toinf_ptg10to100", "dyg_m50toinf_ptg100to200",
    "dyg_m50toinf_ptg200to400", "dyg_m50toinf_ptg400to600", "dyg_m50toinf_ptg600toinf",
    "dyg_m50toinf_ptg100toinf", "dyg_m50toinf_ptg200toinf", "dyg_m50toinf_ptg400toinf",
    "dyg_m4to50", "dyg_m4to50_ptg10to100", "dyg_m4to50_ptg100to200", "dyg_m4to50_ptg200toinf",
    "ww", "qqww", "ggww",
    "ww_dl", "ww_sl", "ww_fh",
    "ww_wenu_wenu", "ww_wenu_wmnu", "ww_wenu_wtnu", "ww_wmnu_wmnu", "ww_wmnu_wtnu", "ww_wtnu_wtnu",
    "ww_ss_2j",
    "vvv",
    "zzz", "wzz", "wwz", "www",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.processes.stitching import get_stitched_dy_m50toinf_br, get_stitched_w_lnu_br


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
# and for 13.6 TeV, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV?rev=12

# if needed for scaling from NLO to NNLO:
# NLO cross section, based on GenXSecAnalyzer for
# DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_m50toinf_nlo_13tev_xsec = Number(6421.0, {"tot": 11.25})

# if needed for scaling from LO to NNLO:
# LO cross section, based on GenXSecAnalyzer for DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_m50toinf_lo_13tev_xsec = Number(5395.0, {"tot": 1.858})

# 13.6 TeV LO and NLO cross sections are based on GenXSecAnalyzer with CMSSW_13_0_13
# using command ./calculateXsectionAndFilterEfficiency.sh -f datasets.txt -c Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2 -n 5000000  # noqa
# or -c Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v1 when needed
dy_m4to10_nlo_13p6tev_xsec = Number(141600, {"tot": 79.81})  # xsdb: Number(141500, {"tot": 301.9})
dy_m10to50_nlo_13p6tev_xsec = Number(21170.0, {"tot": 18.38})  # xsdb: Number(20950.0, {"tot": 183.5})
dy_m50toinf_nlo_13p6tev_xsec = Number(6728.0, {"tot": 6.981})  # xsdb: Number(6688.0, {"tot": 83.99})

dy_m10to50_lo_13p6tev_xsec = Number(17410, {"tot": 2.393})
dy_m50toinf_lo_13p6tev_xsec = Number(5450, {"tot": 1.872})

dy_m50toinf = dy.add_process(
    name="dy_m50toinf",
    id=51100,
    xsecs={
        # nnlo
        13: Number(6077.22, {
            "integration": 1.49,
            "scale": 0.02j,
            "pdf": 14.78,
        }),
        # nnlo
        13.6: const.n_leps * Number(2094.2, {
            "scale": (0.007j, 0.011j),
            "pdf": 0.01j,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
    },
)

# compute k-factors for scaling from LO and NLO to NNLO (which is used for the process cross section above)
# ! NOTE: this assumes that the k-factor does not significantly depend on mll
# ! NOTE: this was tested for 10to50 w.r.t. 50toinf
dy_k_factor_lo_to_nnlo = {
    13: dy_m50toinf.get_xsec(13) / dy_m50toinf_lo_13tev_xsec,
    13.6: dy_m50toinf.get_xsec(13.6) / dy_m50toinf_lo_13p6tev_xsec,
}
dy_k_factor_nlo_to_nnlo = {
    13: dy_m50toinf.get_xsec(13) / dy_m50toinf_nlo_13tev_xsec,
    13.6: dy_m50toinf.get_xsec(13.6) / dy_m50toinf_nlo_13p6tev_xsec,
}

dy_m4to10 = dy.add_process(
    name="dy_m4to10",
    id=51002,
    xsecs={
        13.6: dy_m4to10_nlo_13p6tev_xsec * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 10.0),
    },
)

dy_m4to50 = dy.add_process(
    name="dy_m4to50",
    id=51004,
    aux={
        "mll": (4.0, 50.0),
    },
)

dy_m10to50 = dy.add_process(
    name="dy_m10to50",
    id=51001,
    xsecs={
        13.6: dy_m10to50_nlo_13p6tev_xsec * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (10.0, 50.0),
    },
)

#
# N-jet binned Drell-Yan (scaled to NNLO)
#

# 13.6 TeV xsecs based on XSDB for datasets DYto2L-4Jets_MLL-50_{i}J_TuneCP5_13p6TeV_madgraphMLM-pythia8
# e.g. https://xsdb-temp.app.cern.ch/xsdb/?columns=39911424&currentPage=0&pageSize=10&searchQuery=DAS%3DDYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8  # noqa
# 13 TeV: based on GenXSecAnalyzer
# for datasets DY{i}JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa

dy_m50toinf_0j = dy_m50toinf.add_process(
    name="dy_m50toinf_0j",
    id=51110,
    xsecs={
        # NLO xsec taken from https://xsdb-temp.app.cern.ch/xsdb/?columns=39911424&currentPage=0&pageSize=10&searchQuery=DAS%3DDYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8  # noqa
        13.6: Number(5378, {"tot": 8.007}) * dy_k_factor_nlo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (0, 1),
    },
)

dy_m50toinf_1j = dy_m50toinf.add_process(
    name="dy_m50toinf_1j",
    id=51111,
    xsecs={
        13: Number(926.8, {
            "tot": 0.3597,
        }) * dy_k_factor_lo_to_nnlo[13],
        # 13.6: Number(1017, {"tot": 6.264}) * dy_k_factor_nlo_to_nnlo[13.6],
        13.6: Number(973.1, {"tot": 2.613}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
    },
)

dy_m50toinf_2j = dy_m50toinf.add_process(
    name="dy_m50toinf_2j",
    id=51112,
    xsecs={
        13: Number(294.5, {
            "tot": 0.1223,
        }) * dy_k_factor_lo_to_nnlo[13],
        # 13.6: Number(385.5, {"tot": 3.858}) * dy_k_factor_nlo_to_nnlo[13.6],
        13.6: Number(312.4, {"tot": 0.915}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
    },
)

dy_m50toinf_3j = dy_m50toinf.add_process(
    name="dy_m50toinf_3j",
    id=51113,
    xsecs={
        13: Number(86.53, {
            "tot": 0.03853,
        }) * dy_k_factor_lo_to_nnlo[13],
        13.6: Number(93.93, {"tot": 0.2858}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (3, 4),
    },
)

dy_m50toinf_4j = dy_m50toinf.add_process(
    name="dy_m50toinf_4j",
    id=51114,
    xsecs={
        13: Number(41.21, {
            "tot": 0.02392,
        }) * dy_k_factor_lo_to_nnlo[13],
        13.6: Number(45.43, {"tot": 0.1393}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "njets": (4, 5),
    },
)

dy_m50toinf_ge3j = dy_m50toinf.add_process(
    name="dy_m50toinf_ge3j",
    id=51115,
    aux={
        "mll": (50.0, const.inf),
        "njets": (3, const.inf),
    },
)

# based on GenXSecAnalyzer
# for DYJetsToLL_{i}J_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
dy_0j = dy.add_process(
    name="dy_0j",
    id=51200,
    xsecs={
        13: Number(5134.0, {
            "tot": 5.365,
        }),
    },
    aux={
        "njets": (0, 1),
    },
)

dy_1j = dy.add_process(
    name="dy_1j",
    id=51300,
    xsecs={
        13: Number(952.7, {
            "tot": 2.174,
        }),
    },
    aux={
        "njets": (1, 2),
    },
)

dy_2j = dy.add_process(
    name="dy_2j",
    id=51400,
    xsecs={
        13: Number(359.1, {
            "tot": 1.533,
        }),
    },
    aux={
        "njets": (2, 3),
    },
)

dy_m50toinf_1j_pt0to40 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt0to40",
    id=511110,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (0.0, 40.0),
    },
)

dy_m50toinf_1j_pt40to100 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt40to100",
    id=511111,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (40.0, 100.0),
    },
)

dy_m50toinf_1j_pt100to200 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt100to200",
    id=511112,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (100.0, 200.0),
    },
)

dy_m50toinf_1j_pt200to400 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt200to400",
    id=511113,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (200.0, 400.0),
    },
)

dy_m50toinf_1j_pt400to600 = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt400to600",
    id=511114,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (400.0, 600.0),
    },
)

dy_m50toinf_1j_pt600toinf = dy_m50toinf_1j.add_process(
    name="dy_m50toinf_1j_pt600toinf",
    id=511115,
    aux={
        "mll": (50.0, const.inf),
        "njets": (1, 2),
        "ptll": (600.0, const.inf),
    },
)

dy_m50toinf_2j_pt0to40 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt0to40",
    id=511120,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (0.0, 40.0),
    },
)

dy_m50toinf_2j_pt40to100 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt40to100",
    id=511121,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (40.0, 100.0),
    },
)

dy_m50toinf_2j_pt100to200 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt100to200",
    id=511122,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (100.0, 200.0),
    },
)

dy_m50toinf_2j_pt200to400 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt200to400",
    id=511123,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (200.0, 400.0),
    },
)

dy_m50toinf_2j_pt400to600 = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt400to600",
    id=511124,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (400.0, 600.0),
    },
)

dy_m50toinf_2j_pt600toinf = dy_m50toinf_2j.add_process(
    name="dy_m50toinf_2j_pt600toinf",
    id=511125,
    aux={
        "mll": (50.0, const.inf),
        "njets": (2, 3),
        "ptll": (600.0, const.inf),
    },
)

# LO cross sections, scaled to NNLO

# based on xsecdb:
# https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=58393344&currentPage=0&pageSize=10&searchQuery=process_name%3DDYto2L-4Jets_MLL-50_PT.%2A
# based on xsecdb:
# https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=58393344&currentPage=0&pageSize=10&searchQuery=process_name%3DDYto2L-4Jets_MLL-4to50.%2A

dy_m4to50_ht40to70 = dy_m4to50.add_process(
    name="dy_m4to50_ht40to70",
    id=510040,
    xsecs={
        13.6: Number(911.4, {"tot": 2.547}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (40.0, 70.0),
    },
)

dy_m4to50_ht70to100 = dy_m4to50.add_process(
    name="dy_m4to50_ht70to100",
    id=510041,
    xsecs={
        13.6: Number(346.6, {"tot": 0.9889}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (70.0, 100.0),
    },
)

dy_m4to50_ht100to400 = dy_m4to50.add_process(
    name="dy_m4to50_ht100to400",
    id=510042,
    xsecs={
        13.6: Number(316.8, {"tot": 0.9199}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (100.0, 400.0),
    },
)

dy_m4to50_ht400to800 = dy_m4to50.add_process(
    name="dy_m4to50_ht400to800",
    id=510043,
    xsecs={
        13.6: Number(5.649, {"tot": 0.01686}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (400.0, 800.0),
    },
)

dy_m4to50_ht800to1500 = dy_m4to50.add_process(
    name="dy_m4to50_ht800to1500",
    id=510044,
    xsecs={
        13.6: Number(0.4204, {"tot": 0.001262}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (800.0, 1500.0),
    },
)

dy_m4to50_ht1500to2500 = dy_m4to50.add_process(
    name="dy_m4to50_ht1500to2500",
    id=510045,
    xsecs={
        13.6: Number(0.02079, {"tot": 0.00006233}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (1500.0, 2500.0),
    },
)

dy_m4to50_ht2500toinf = dy_m4to50.add_process(
    name="dy_m4to50_ht2500toinf",
    id=510046,
    xsecs={
        13.6: Number(0.00107, {"tot": 0.000003204}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (4.0, 50.0),
        "htt": (2500.0, const.inf),
    },
)

dy_m50toinf_pt40to100 = dy_m50toinf.add_process(
    name="dy_m50toinf_pt40to100",
    id=511001,
    xsecs={
        13.6: Number(403.7, {"tot": 1.143}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "ptll": (40.0, 100.0),
    },
)

dy_m50toinf_pt100to200 = dy_m50toinf.add_process(
    name="dy_m50toinf_pt100to200",
    id=511002,
    xsecs={
        13.6: Number(58.46, {"tot": 0.173}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "ptll": (100.0, 200.0),
    },
)

dy_m50toinf_pt200to400 = dy_m50toinf.add_process(
    name="dy_m50toinf_pt200to400",
    id=511003,
    xsecs={
        13.6: Number(6.678, {"tot": 0.02018}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "ptll": (200.0, 400.0),
    },
)

dy_m50toinf_pt400to600 = dy_m50toinf.add_process(
    name="dy_m50toinf_pt400to600",
    id=511004,
    xsecs={
        13.6: Number(0.3833, {"tot": 0.00117}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "ptll": (400.0, 600.0),
    },
)

dy_m50toinf_pt600toinf = dy_m50toinf.add_process(
    name="dy_m50toinf_pt600toinf",
    id=511005,
    xsecs={
        13.6: Number(0.06843, {"tot": 0.0002102}) * dy_k_factor_lo_to_nnlo[13.6],
    },
    aux={
        "mll": (50.0, const.inf),
        "ptll": (600.0, const.inf),
    },
)

# based on GenXSecAnalyzer
# for DYJetsToLL_M-50_HT-{i}to{j}_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
dy_m50toinf_ht70to100 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht70to100",
    id=51121,
    xsecs={
        13: Number(139.9, {"tot": 0.5747}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (70.0, 100.0),
    },
)

dy_m50toinf_ht100to200 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht100to200",
    id=51122,
    xsecs={
        13: Number(140.1, {"tot": 0.5875}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (100.0, 200.0),
    },
)

dy_m50toinf_ht200to400 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht200to400",
    id=51123,
    xsecs={
        13: Number(38.38, {"tot": 0.01628}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (200.0, 400.0),
    },
)

dy_m50toinf_ht400to600 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht400to600",
    id=51124,
    xsecs={
        13: Number(5.212, {"tot": 0.003149}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (400.0, 600.0),
    },
)

dy_m50toinf_ht600to800 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht600to800",
    id=51125,
    xsecs={
        13: Number(1.266, {"tot": 0.0007976}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (600.0, 800.0),
    },
)

dy_m50toinf_ht800to1200 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht800to1200",
    id=51126,
    xsecs={
        13: Number(0.5684, {"tot": 0.0003515}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (800.0, 1200.0),
    },
)

dy_m50toinf_ht1200to2500 = dy_m50toinf.add_process(
    name="dy_m50toinf_ht1200to2500",
    id=51127,
    xsecs={
        13: Number(0.1332, {"tot": 0.00009084}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (1200.0, 2500.0),
    },
)

dy_m50toinf_ht2500toinf = dy_m50toinf.add_process(
    name="dy_m50toinf_ht2500toinf",
    id=51128,
    xsecs={
        13: Number(0.002977, {"tot": 0.000003412}) * dy_k_factor_lo_to_nnlo[13],
    },
    aux={
        "mll": (50.0, const.inf),
        "htt": (2500.0, const.inf),
    },
)

# based on GenXSecAnalyzer
# for DYJetsToLL_LHEFilterPtZ-{i}To{j}_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
dy_pt0to50 = dy.add_process(
    name="dy_pt0to50",
    id=51510,
    xsecs={
        13: Number(1494.0, {
            "tot": 1.751,
        }),
    },
    aux={
        "ptll": (0.0, 50.0),
    },
)

dy_pt50to100 = dy.add_process(
    name="dy_pt50to100",
    id=51520,
    xsecs={
        13: Number(398.3, {
            "tot": 0.5600,
        }),
    },
    aux={
        "ptll": (50.0, 100.0),
    },
)

dy_pt100to250 = dy.add_process(
    name="dy_pt100to250",
    id=51530,
    xsecs={
        13: Number(96.58, {
            "tot": 0.1370,
        }),
    },
    aux={
        "ptll": (100.0, 250.0),
    },
)

dy_pt250to400 = dy.add_process(
    name="dy_pt250to400",
    id=51540,
    xsecs={
        13: Number(3.738, {
            "tot": 0.005305,
        }),
    },
    aux={
        "ptll": (250.0, 400.0),
    },
)

dy_pt400to650 = dy.add_process(
    name="dy_pt400to650",
    id=51550,
    xsecs={
        13: Number(0.5050, {
            "tot": 0.0008169,
        }),
    },
    aux={
        "ptll": (400.0, 650.0),
    },
)

dy_pt650toinf = dy.add_process(
    name="dy_pt650toinf",
    id=51560,
    xsecs={
        13: Number(0.04763, {
            "tot": 0.00007206,
        }),
    },
    aux={
        "ptll": (650.0, const.inf),
    },
)

#
# NNLO decays split into specific leptons
# (cross sections from xsdb)
#

dy_ee = dy.add_process(
    name="dy_ee",
    id=50100,
    aux={
        "lep_id": 11,
    },
)

dy_mumu = dy.add_process(
    name="dy_mumu",
    id=50200,
    aux={
        "lep_id": 13,
    },
)

dy_tautau = dy.add_process(
    name="dy_tautau",
    id=50300,
    aux={
        "lep_id": 15,
    },
)

# 2 e
dy_ee_m10to50 = dy_ee.add_process(
    name="dy_ee_m10to50",
    id=51810,
    xsecs={
        13.6: dy_m10to50.get_xsec(13.6) / const.n_leps,
    },
    aux={
        "lep_id": 11,
        "mll": (10.0, 50.0),
    },
)

dy_ee_m50toinf = dy_ee.add_process(
    name="dy_ee_m50toinf",
    id=51800,
    xsecs={
        13.6: dy_m50toinf.get_xsec(13.6) * get_stitched_dy_m50toinf_br("dy_ee_m50toinf*"),
    },
    aux={
        "lep_id": 11,
        "mll": (50.0, const.inf),
    },
)
dy_ee_m50toinf.add_parent_process(dy_m50toinf)

dy_ee_m50to120 = dy_ee_m50toinf.add_process(
    name="dy_ee_m50to120",
    id=51811,
    xsecs={
        13.6: Number(2219, {
            "tot": 0.2327,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (50.0, 120),
    },
)

dy_ee_m120to200 = dy_ee_m50toinf.add_process(
    name="dy_ee_m120to200",
    id=51812,
    xsecs={
        13.6: Number(21.65, {
            "tot": 0.003184,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (120.0, 200.0),
    },
)

dy_ee_m200to400 = dy_ee_m50toinf.add_process(
    name="dy_ee_m200to400",
    id=51813,
    xsecs={
        13.6: Number(3.058, {
            "tot": 0.000465,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (200.0, 400.0),
    },
)

dy_ee_m400to800 = dy_ee_m50toinf.add_process(
    name="dy_ee_m400to800",
    id=51814,
    xsecs={
        13.6: Number(0.2691, {
            "tot": 0.00004215,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (400.0, 800.0),
    },
)

dy_ee_m800to1500 = dy_ee_m50toinf.add_process(
    name="dy_ee_m800to1500",
    id=51815,
    xsecs={
        13.6: Number(0.01915, {
            "tot": 0.000003085,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (800.0, 1500.0),
    },
)

dy_ee_m1500to2500 = dy_ee_m50toinf.add_process(
    name="dy_ee_m1500to2500",
    id=51816,
    xsecs={
        13.6: Number(0.001111, {
            "tot": 1.787e-7,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (1500.0, 2500.0),
    },
)

dy_ee_m2500to4000 = dy_ee_m50toinf.add_process(
    name="dy_ee_m2500to4000",
    id=51817,
    xsecs={
        13.6: Number(0.00005949, {
            "tot": 9.162e-9,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (2500.0, 4000.0),
    },
)

dy_ee_m4000to6000 = dy_ee_m50toinf.add_process(
    name="dy_ee_m4000to6000",
    id=51818,
    xsecs={
        13.6: Number(0.000001558, {
            "tot": 2.078e-10,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (4000.0, 6000.0),
    },
)

dy_ee_m6000toinf = dy_ee_m50toinf.add_process(
    name="dy_ee_m6000toinf",
    id=51619,
    xsecs={
        13.6: Number(3.519e-8, {
            "tot": 6.811e-12,
        }),
    },
    aux={
        "lep_id": 11,
        "mll": (6000.0, const.inf),
    },
)

# normalize ee mll bins to nnlo expectation from inclusive m50toinf / 3
dy_ee_m_procs = [
    dy_ee_m50to120,
    dy_ee_m120to200,
    dy_ee_m200to400,
    dy_ee_m400to800,
    dy_ee_m800to1500,
    dy_ee_m1500to2500,
    dy_ee_m2500to4000,
    dy_ee_m4000to6000,
    dy_ee_m6000toinf,
]
dy_ee_m_corr_13p6 = (
    (dy_m50toinf.get_xsec(13.6) / const.n_leps) /
    sum(proc.get_xsec(13.6) for proc in dy_ee_m_procs)
)
for proc in dy_ee_m_procs:
    proc.xsecs[13.6] *= dy_ee_m_corr_13p6

# 2 mu
dy_mumu_m10to50 = dy_mumu.add_process(
    name="dy_mumu_m10to50",
    id=51620,
    xsecs={
        13.6: dy_m10to50.get_xsec(13.6) / const.n_leps,
    },
    aux={
        "lep_id": 13,
        "mll": (10.0, 50.0),
    },
)

dy_mumu_m50toinf = dy_mumu.add_process(
    name="dy_mumu_m50toinf",
    id=51621,
    xsecs={
        13.6: dy_m50toinf.get_xsec(13.6) * get_stitched_dy_m50toinf_br("dy_mumu_m50toinf*"),
    },
    aux={
        "lep_id": 13,
        "mll": (50.0, const.inf),
    },
)
dy_mumu_m50toinf.add_parent_process(dy_m50toinf)

dy_mumu_m50to120 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m50to120",
    id=51622,
    xsecs={
        13.6: Number(2219, {
            "tot": 0.2327,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (50.0, 120.0),
    },
)

dy_mumu_m120to200 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m120to200",
    id=51623,
    xsecs={
        13.6: Number(21.65, {
            "tot": 0.003184,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (120.0, 200.0),
    },
)

dy_mumu_m200to400 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m200to400",
    id=51624,
    xsecs={
        13.6: Number(3.058, {
            "tot": 0.000465,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (200.0, 400.0),
    },
)

dy_mumu_m400to800 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m400to800",
    id=51625,
    xsecs={
        13.6: Number(0.2691, {
            "tot": 0.00004215,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (400.0, 800.0),
    },
)

dy_mumu_m800to1500 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m800to1500",
    id=51626,
    xsecs={
        13.6: Number(0.01915, {
            "tot": 0.000003085,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (800.0, 1500.0),
    },
)

dy_mumu_m1500to2500 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m1500to2500",
    id=51627,
    xsecs={
        13.6: Number(0.001111, {
            "tot": 1.787e-7,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (1500.0, 2500.0),
    },
)

dy_mumu_m2500to4000 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m2500to4000",
    id=51628,
    xsecs={
        13.6: Number(0.00005949, {
            "tot": 9.162e-9,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (2500.0, 4000.0),
    },
)

dy_mumu_m4000to6000 = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m4000to6000",
    id=51629,
    xsecs={
        13.6: Number(0.000001558, {
            "tot": 2.078e-10,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (4000.0, 6000.0),
    },
)

dy_mumu_m6000toinf = dy_mumu_m50toinf.add_process(
    name="dy_mumu_m6000toinf",
    id=51630,
    xsecs={
        13.6: Number(3.519e-8, {
            "tot": 6.811e-12,
        }),
    },
    aux={
        "lep_id": 13,
        "mll": (6000.0, const.inf),
    },
)

# normalize mumu mll bins to nnlo expectation from inclusive m50toinf / 3
dy_mumu_m_procs = [
    dy_mumu_m50to120,
    dy_mumu_m120to200,
    dy_mumu_m200to400,
    dy_mumu_m400to800,
    dy_mumu_m800to1500,
    dy_mumu_m1500to2500,
    dy_mumu_m2500to4000,
    dy_mumu_m4000to6000,
    dy_mumu_m6000toinf,
]
dy_mumu_m_corr_13p6 = (
    (dy_m50toinf.get_xsec(13.6) / const.n_leps) /
    sum(proc.get_xsec(13.6) for proc in dy_mumu_m_procs)
)
for proc in dy_mumu_m_procs:
    proc.xsecs[13.6] *= dy_mumu_m_corr_13p6

# 2 tau
dy_tautau_m10to50 = dy_tautau.add_process(
    name="dy_tautau_m10to50",
    id=51631,
    xsecs={
        13.6: dy_m10to50.get_xsec(13.6) / const.n_leps,
    },
    aux={
        "lep_id": 15,
        "mll": (10.0, 50.0),
    },
)

dy_tautau_m50toinf = dy_tautau.add_process(
    name="dy_tautau_m50toinf",
    id=51632,
    xsecs={
        13.6: dy_m50toinf.get_xsec(13.6) * get_stitched_dy_m50toinf_br("dy_tautau_m50toinf*"),
    },
    aux={
        "lep_id": 15,
        "mll": (50.0, const.inf),
    },
)
dy_tautau_m50toinf.add_parent_process(dy_m50toinf)

dy_tautau_m50to120 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m50to120",
    id=51633,
    xsecs={
        13.6: Number(2219, {
            "tot": 0.2327,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (50.0, 120.0),
    },
)

dy_tautau_m120to200 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m120to200",
    id=51634,
    xsecs={
        13.6: Number(21.65, {
            "tot": 0.003184,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (120.0, 200.0),
    },
)

dy_tautau_m200to400 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m200to400",
    id=51635,
    xsecs={
        13.6: Number(3.058, {
            "tot": 0.000465,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (200.0, 400.0),
    },
)

dy_tautau_m400to800 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m400to800",
    id=51636,
    xsecs={
        13.6: Number(0.2691, {
            "tot": 0.00004215,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (400.0, 800.0),
    },
)

dy_tautau_m800to1500 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m800to1500",
    id=51637,
    xsecs={
        13.6: Number(0.01915, {
            "tot": 0.000003085,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (800.0, 1500.0),
    },
)

dy_tautau_m1500to2500 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m1500to2500",
    id=51638,
    xsecs={
        13.6: Number(0.001111, {
            "tot": 1.787e-7,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (1500.0, 2500.0),
    },
)

dy_tautau_m2500to4000 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m2500to4000",
    id=51639,
    xsecs={
        13.6: Number(0.00005949, {
            "tot": 9.162e-9,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (2500.0, 4000.0),
    },
)

dy_tautau_m4000to6000 = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m4000to6000",
    id=51640,
    xsecs={
        13.6: Number(0.000001558, {
            "tot": 2.078e-10,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (4000.0, 6000.0),
    },
)

dy_tautau_m6000toinf = dy_tautau_m50toinf.add_process(
    name="dy_tautau_m6000toinf",
    id=51641,
    xsecs={
        13.6: Number(3.519e-8, {
            "tot": 6.811e-12,
        }),
    },
    aux={
        "lep_id": 15,
        "mll": (6000.0, const.inf),
    },
)

# normalize tautau mll bins to nnlo expectation from inclusive m50toinf / 3
dy_tautau_m_procs = [
    dy_tautau_m50to120,
    dy_tautau_m120to200,
    dy_tautau_m200to400,
    dy_tautau_m400to800,
    dy_tautau_m800to1500,
    dy_tautau_m1500to2500,
    dy_tautau_m2500to4000,
    dy_tautau_m4000to6000,
    dy_tautau_m6000toinf,
]
dy_tautau_m_corr_13p6 = (
    (dy_m50toinf.get_xsec(13.6) / const.n_leps) /
    sum(proc.get_xsec(13.6) for proc in dy_tautau_m_procs)
)
for proc in dy_tautau_m_procs:
    proc.xsecs[13.6] *= dy_tautau_m_corr_13p6


# helper to insert stitched xsec info
def get_dy_ll_m50toinf_xsec_13p6(*name):
    return {"xsecs": {13.6: dy_m50toinf.get_xsec(13.6) * get_stitched_dy_m50toinf_br(*name)}}


# lepton decays, with jet multiplicity bins, and optionally also pt bins
dy_ll_m_id = 51660
for ll, lid, split_filtered in [("ee", 11, False), ("mumu", 13, False), ("tautau", 15, True)]:
    dy_ll_m = locals()[f"dy_{ll}_m50toinf"]
    # jet multiplicity bins
    for nj, nj_range, split_pt in [
        ("0j", (0, 1), False),
        ("1j", (1, 2), True),
        ("2j", (2, 3), True),
        ("ge3j", (3, const.inf), False),
    ]:
        dy_ll_m_nj = locals()[n] = dy_ll_m.add_process(
            name=(n := f"dy_{ll}_m50toinf_{nj}"),
            id=(dy_ll_m_id := dy_ll_m_id + 1),
            **(get_dy_ll_m50toinf_xsec_13p6(n + "*")),
            aux={
                "lep_id": lid,
                "mll": (50.0, const.inf),
                "njets": nj_range,
            },
        )
        dy_ll_m_nj.add_parent_process(locals()[f"dy_m50toinf_{nj}"])
        # split into filtered / nonfiltered
        if split_filtered:
            for fname in ["filtered", "nonfiltered"]:
                locals()[n] = dy_ll_m_nj.add_process(
                    name=(n := f"dy_{ll}_m50toinf_{nj}_{fname}"),
                    id=(dy_ll_m_id := dy_ll_m_id + 1),
                    **(get_dy_ll_m50toinf_xsec_13p6(n + "*")),
                    aux={
                        "lep_id": lid,
                        "mll": (50.0, const.inf),
                        "njets": nj_range,
                        "filtered": fname == "filtered",
                    },
                )
        # split into pt bins
        if split_pt:
            for pt, pt_range in [
                ("0to40", (0.0, 40.0)),
                ("40to100", (40.0, 100.0)),
                ("100to200", (100.0, 200.0)),
                ("200to400", (200.0, 400.0)),
                ("400to600", (400.0, 600.0)),
                ("600toinf", (600.0, const.inf)),
            ]:
                dy_ll_m_nj_pt = locals()[n] = dy_ll_m_nj.add_process(
                    name=(n := f"dy_{ll}_m50toinf_{nj}_pt{pt}"),
                    id=(dy_ll_m_id := dy_ll_m_id + 1),
                    **(get_dy_ll_m50toinf_xsec_13p6(n + "*")),
                    aux={
                        "lep_id": lid,
                        "mll": (50.0, const.inf),
                        "njets": nj_range,
                        "ptll": pt_range,
                    },
                )
                dy_ll_m_nj_pt.add_parent_process(locals()[f"dy_m50toinf_{nj}_pt{pt}"])
                # split into filtered / nonfiltered
                # (see fragment in https://cms-pdmv-prod.web.cern.ch/mcm/requests?prepid=HIG-Run3Summer22EEwmLHEGS-01476&page=0&shown=140737488355327)  # noqa
                if split_filtered:
                    for fname in ["filtered", "nonfiltered"]:
                        dy_ll_m_nj_pt_f = locals()[f"dy_{ll}_m50toinf_{nj}_pt{pt}_{fname}"] = dy_ll_m_nj_pt.add_process(
                            name=f"dy_{ll}_m50toinf_{nj}_pt{pt}_{fname}",
                            id=(dy_ll_m_id := dy_ll_m_id + 1),
                            aux={
                                "lep_id": lid,
                                "mll": (50.0, const.inf),
                                "njets": nj_range,
                                "ptll": pt_range,
                                "filtered": fname == "filtered",
                            },
                        )
                        dy_ll_m_nj_pt_f.add_parent_process(locals()[f"dy_{ll}_m50toinf_{nj}_{fname}"])

#
# Z boson (no photon/DY)
#

z = Process(
    name="z",
    id=55000,
    label="Z + jets",
)

# Z -> neutrinos

z_nunu = z.add_process(
    name="z_nunu",
    id=55100,
    label=rf"{z.label} (Z $\rightarrow$ $\nu\nu$)",
)

# 13 TeV Xsecs based on GenXSecAnalyzer
# for ZJetsToNuNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
z_nunu_ht100to200 = z_nunu.add_process(
    name="z_nunu_ht100to200",
    id=55110,
    xsecs={
        13: Number(266.1, {
            "tot": 0.1117,
        }),
    },
)

z_nunu_ht200to400 = z_nunu.add_process(
    name="z_nunu_ht200to400",
    id=55120,
    xsecs={
        13: Number(73.00, {
            "tot": 0.04408,
        }),
    },
)

z_nunu_ht400to600 = z_nunu.add_process(
    name="z_nunu_ht400to600",
    id=55130,
    xsecs={
        13: Number(9.915, {
            "tot": 0.004229,
        }),
    },
)

z_nunu_ht600to800 = z_nunu.add_process(
    name="z_nunu_ht600to800",
    id=55140,
    xsecs={
        13: Number(2.409, {
            "tot": 0.001678,
        }),
    },
)

z_nunu_ht800to1200 = z_nunu.add_process(
    name="z_nunu_ht800to1200",
    id=55150,
    xsecs={
        13: Number(1.077, {
            "tot": 0.001295,
        }),
    },
)

z_nunu_ht1200to2500 = z_nunu.add_process(
    name="z_nunu_ht1200to2500",
    id=55160,
    xsecs={
        13: Number(0.2495, {
            "tot": 0.0007030,
        }),
    },
)

z_nunu_ht2500toinf = z_nunu.add_process(
    name="z_nunu_ht2500toinf",
    id=55170,
    xsecs={
        13: Number(0.005614, {
            "tot": 0.00001616,
        }),
    },
)

# Z -> quarks

# 13 TeV Xsecs based on GenXSecAnalyzer
# for ZJetsToQQ_HT-{i}to{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
z_qq = z.add_process(
    name="z_qq",
    id=55200,
    label=rf"{z.label} (Z $\rightarrow$ $\text{{q}}\overline{{\text{{q}}}}$)",
)

z_qq_ht200to400 = z_qq.add_process(
    name="z_qq_ht200to400",
    id=55210,
    xsecs={
        13: Number(1012.0, {"total": 0.4260}),
    },
    aux={
        "ht": (200.0, 400.0),
    },
)

z_qq_ht400to600 = z_qq.add_process(
    name="z_qq_ht400to600",
    id=55220,
    xsecs={
        13: Number(114.5, {"total": 0.04884}),
    },
    aux={
        "ht": (400.0, 600.0),
    },
)

z_qq_ht600to800 = z_qq.add_process(
    name="z_qq_ht600to800",
    id=55230,
    xsecs={
        13: Number(25.38, {"total": 0.01088}),
    },
    aux={
        "ht": (600.0, 800.0),
    },
)

z_qq_ht800toinf = z_qq.add_process(
    name="z_qq_ht800toinf",
    id=55240,
    xsecs={
        13: Number(12.92, {"total": 0.005923}),
    },
    aux={
        "ht": (800.0, const.inf),
    },
)

z_qq_pt100toinf = z_qq.add_process(
    name="z_qq_pt100toinf",
    id=55251,
    xsecs={
        # XSDB
        13.6: Number(706.5, {"total": 1.906}),
    },
    aux={
        "ptqq": (100.0, const.inf),
    },
)

z_qq_pt200toinf = z_qq.add_process(
    name="z_qq_pt200toinf",
    id=55252,
    xsecs={
        # XSDB
        13.6: Number(70.55, {"total": 0.4536}),
    },
    aux={
        "ptqq": (200.0, const.inf),
    },
)

z_qq_pt400toinf = z_qq.add_process(
    name="z_qq_pt400toinf",
    id=55253,
    xsecs={
        # XSDB
        13.6: Number(3.792, {"total": 0.008495}),
    },
    aux={
        "ptqq": (400.0, const.inf),
    },
)

z_qq_pt600toinf = z_qq.add_process(
    name="z_qq_pt600toinf",
    id=55254,
    xsecs={
        # XSDB
        13.6: Number(0.5073, {"total": 0.001065}),
    },
    aux={
        "ptqq": (600.0, const.inf),
    },
)

z_qq_1j_pt100to200 = z_qq.add_process(
    name="z_qq_1j_pt100to200",
    id=55261,
    xsecs={
        # XSDB
        13.6: Number(302.0, {"total": 1.493}),
    },
    aux={
        "njets": (1, 2),
        "ptqq": (100.0, 200.0),
    },
)

z_qq_2j_pt100to200 = z_qq.add_process(
    name="z_qq_2j_pt100to200",
    id=55262,
    xsecs={
        # XSDB
        13.6: Number(343.9, {"total": 2.979}),
    },
    aux={
        "njets": (2, 3),
        "ptqq": (100.0, 200.0),
    },
)

z_qq_1j_pt200to400 = z_qq.add_process(
    name="z_qq_1j_pt200to400",
    id=55263,
    xsecs={
        # XSDB
        13.6: Number(21.64, {"total": 0.1029}),
    },
    aux={
        "njets": (1, 2),
        "ptqq": (200.0, 400.0),
    },
)

z_qq_2j_pt200to400 = z_qq.add_process(
    name="z_qq_2j_pt200to400",
    id=55264,
    xsecs={
        # XSDB
        13.6: Number(48.36, {"total": 0.375}),
    },
    aux={
        "njets": (2, 3),
        "ptqq": (200.0, 400.0),
    },
)

z_qq_1j_pt400to600 = z_qq.add_process(
    name="z_qq_1j_pt400to600",
    id=55265,
    xsecs={
        # XSDB
        13.6: Number(0.7376, {"total": 0.003183}),
    },
    aux={
        "njets": (1, 2),
        "ptqq": (400.0, 600.0),
    },
)

z_qq_2j_pt400to600 = z_qq.add_process(
    name="z_qq_2j_pt400to600",
    id=55266,
    xsecs={
        # XSDB
        13.6: Number(2.683, {"total": 0.01553}),
    },
    aux={
        "njets": (2, 3),
        "ptqq": (400.0, 600.0),
    },
)

z_qq_1j_pt600toinf = z_qq_pt600toinf.add_process(
    name="z_qq_1j_pt600toinf",
    id=55267,
    xsecs={
        # XSDB
        13.6: Number(0.08717, {"total": 0.0003566}),
    },
    aux={
        "njets": (1, 2),
        "ptqq": (600.0, const.inf),
    },
)

z_qq_2j_pt600toinf = z_qq_pt600toinf.add_process(
    name="z_qq_2j_pt600toinf",
    id=55268,
    xsecs={
        # XSDB
        13.6: Number(0.4459, {"total": 0.002084}),
    },
    aux={
        "njets": (2, 3),
        "ptqq": (600.0, const.inf),
    },
)

# dedicated vbf production (pp -> z + qq)
z_vbf = z.add_process(
    name="z_vbf",
    id=55300,
    label=f"{z.label} (VBF)",
)

z_vbf_zll = z_vbf.add_process(
    name="z_vbf_zll",
    id=55310,
    label=r"Z $\rightarrow ll$ (VBF)",
)

z_vbf_zll_m50toinf = z_vbf_zll.add_process(
    name="z_vbf_zll_m50toinf",
    id=55313,
    xsecs={
        # based on GenXSecAnalyzer
        13.6: Number(7.769000, {"tot": 0.002434}),
    },
    aux={
        "mll": (50.0, const.inf),
    },
)

z_vbf_zqq = z_vbf.add_process(
    name="z_vbf_zqq",
    id=55314,
    label=r"Z $\rightarrow qq$ (VBF)",
    xsecs={
        # XSDB (Run3Summer22)
        13.6: Number(13.67, {"tot": 0.005891}),
    },
)

#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    # TODO, or use w.set_xsec(13, w_lnu.get_xsec(13) / const.br_w.lep) below?
)


w_taunu = w.add_process(
    name="w_taunu",
    id=6010,
    label=rf"{w.label} ($W \rightarrow tau\nu$)",
)

w_munu = w.add_process(
    name="w_munu",
    id=6020,
    label=rf"{w.label} ($W \rightarrow mu\nu$)",
)


# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=27
# and for 13.6 TeV, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MATRIXCrossSectionsat13p6TeV?rev=12

wm_lnu_xs_13p6 = const.n_leps * Number(9013.3, {
    "scale": (0.013j, 0.011j),
    "pdf": 0.008j,
})
wp_lnu_xs_13p6 = const.n_leps * Number(12128.4, {
    "scale": (0.011j, 0.014),
    "pdf": 0.007j,
})

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={
        13: const.n_leps * Number(20508.9, {
            "scale": (165.7, 88.2),
            "pdf": 770.9,
        }),
        # addition necessary due to absence of combined value
        13.6: wm_lnu_xs_13p6 + wp_lnu_xs_13p6,
    },
)

# LO cross section, needed for scaling to NNLO:
# based on GenXSecAnalyzer
# for WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
w_lnu_lo_13tev_xsec = Number(54070.0, {"tot": 18.32})

# ht bins based on GenXSecAnalyzer
# for WJetsToLNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
# LO cross sections, scaled to NNLO
w_lnu_ht70to100 = w_lnu.add_process(
    name="w_lnu_ht70to100",
    id=6110,
    xsecs={
        13: Number(1270.0, {"tot": 0.5259}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (70.0, 100.0),
    },
)

w_lnu_ht100to200 = w_lnu.add_process(
    name="w_lnu_ht100to200",
    id=6120,
    xsecs={
        13: Number(1254.0, {"tot": 0.5274}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (100.0, 200.0),
    },
)

w_lnu_ht200to400 = w_lnu.add_process(
    name="w_lnu_ht200to400",
    id=6130,
    xsecs={
        13: Number(336.6, {"tot": 0.1528}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (200.0, 400.0),
    },
)

w_lnu_ht400to600 = w_lnu.add_process(
    name="w_lnu_ht400to600",
    id=6140,
    xsecs={
        13: Number(45.21, {"tot": 0.02966}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (400.0, 600.0),
    },
)

w_lnu_ht600to800 = w_lnu.add_process(
    name="w_lnu_ht600to800",
    id=6150,
    xsecs={
        13: Number(10.98, {"tot": 0.006997}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (600.0, 800.0),
    },
)

w_lnu_ht800to1200 = w_lnu.add_process(
    name="w_lnu_ht800to1200",
    id=6160,
    xsecs={
        13: Number(4.927, {"tot": 0.003229}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (800.0, 1200.0),
    },
)

w_lnu_ht1200to2500 = w_lnu.add_process(
    name="w_lnu_ht1200to2500",
    id=6170,
    xsecs={
        13: Number(1.157, {"tot": 0.0007663}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (1200.0, 2500.0),
    },
)

# this ht bin needs the command:
# ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2 -n 5000000  # noqa
w_lnu_ht2500toinf = w_lnu.add_process(
    name="w_lnu_ht2500toinf",
    id=6180,
    xsecs={
        13: Number(0.02624, {"tot": 0.00002981}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "ht": (2500.0, const.inf),
    },
)

w_lnu_0j = w_lnu.add_process(
    name="w_lnu_0j",
    id=610000,
    label=rf"{w_lnu.label[:-1]}, 0j)",
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_0j*"),
    },
    aux={
        "njets": (0, 1),
    },
)

w_lnu_1j = w_lnu.add_process(
    name="w_lnu_1j",
    id=610010,
    label=rf"{w_lnu.label[:-1]}, 1j)",
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j*"),
    },
    aux={
        "njets": (1, 2),
    },
)

w_lnu_2j = w_lnu.add_process(
    name="w_lnu_2j",
    id=610020,
    label=rf"{w_lnu.label[:-1]}, 2j)",
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j*"),
    },
    aux={
        "njets": (2, 3),
    },
)

w_lnu_3j = w_lnu.add_process(
    name="w_lnu_3j",
    id=610040,
    label=rf"{w_lnu.label[:-1]}, 3j)",
    xsecs={
        # XSDB (Run3Summer24) LO x 13 TeV k-factor..
        13.6: Number(864.6, {"tot": 2.634}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "njets": (3, 4),
    },
)

w_lnu_4j = w_lnu.add_process(
    name="w_lnu_4j",
    id=610041,
    label=rf"{w_lnu.label[:-1]}, 4j)",
    xsecs={
        # XSDB (Run3Summer24) LO x 13 TeV k-factor..
        13.6: Number(417.8, {"tot": 1.283}) * w_lnu.get_xsec(13) / w_lnu_lo_13tev_xsec,
    },
    aux={
        "njets": (4, 5),
    },
)

w_lnu_1j_pt0to40 = w_lnu_1j.add_process(
    name="w_lnu_1j_pt0to40",
    id=6100100,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt0to40*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (0.0, 40.0),
    },
)

w_lnu_1j_pt40to100 = w_lnu_1j.add_process(
    name="w_lnu_1j_pt40to100",
    id=610011,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt40to100*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (40.0, 100.0),
    },
)

w_lnu_1j_pt100to200 = w_lnu_1j.add_process(
    name="w_lnu_1j_pt100to200",
    id=610012,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt100to200*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (100.0, 200.0),
    },
)

w_lnu_1j_pt200to400 = w_lnu_1j.add_process(
    name="w_lnu_1j_pt200to400",
    id=610013,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt200to400*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (200.0, 400.0),
    },
)

w_lnu_1j_pt400to600 = w_lnu_1j.add_process(
    name="w_lnu_1j_pt400to600",
    id=610014,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt400to600*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (400.0, 600.0),
    },
)

w_lnu_1j_pt600toinf = w_lnu_1j.add_process(
    name="w_lnu_1j_pt600toinf",
    id=610015,
    label=w_lnu_1j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_1j_pt600toinf*"),
    },
    aux={
        "njets": (1, 2),
        "ptll": (600.0, const.inf),
    },
)

w_lnu_2j_pt0to40 = w_lnu_2j.add_process(
    name="w_lnu_2j_pt0to40",
    id=6100200,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt0to40*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (0.0, 40.0),
    },
)

w_lnu_2j_pt40to100 = w_lnu_2j.add_process(
    name="w_lnu_2j_pt40to100",
    id=610021,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt40to100*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (40.0, 100.0),
    },
)

w_lnu_2j_pt100to200 = w_lnu_2j.add_process(
    name="w_lnu_2j_pt100to200",
    id=610022,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt100to200*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (100.0, 200.0),
    },
)

w_lnu_2j_pt200to400 = w_lnu_2j.add_process(
    name="w_lnu_2j_pt200to400",
    id=610023,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt200to400*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (200.0, 400.0),
    },
)

w_lnu_2j_pt400to600 = w_lnu_2j.add_process(
    name="w_lnu_2j_pt400to600",
    id=610024,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt400to600*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (400.0, 600.0),
    },
)

w_lnu_2j_pt600toinf = w_lnu_2j.add_process(
    name="w_lnu_2j_pt600toinf",
    id=610025,
    label=w_lnu_2j.label,
    xsecs={
        13.6: w_lnu.get_xsec(13.6) * get_stitched_w_lnu_br("w_lnu_2j_pt600toinf*"),
    },
    aux={
        "njets": (2, 3),
        "ptll": (600.0, const.inf),
    },
)

w_lnu_ge3j = w_lnu.add_process(
    name="w_lnu_ge3j",
    id=610026,
    aux={
        "njets": (3, const.inf),
    },
)

# dedicated vbf production (pp -> w + qq)
w_vbf = w.add_process(
    name="w_vbf",
    id=6300,
    label=f"{w.label} (VBF)",
)

w_vbf_wlnu = w_vbf.add_process(
    name="w_vbf_wlnu",
    id=6310,
    label=r"W $\rightarrow l\nu$ (VBF)",
    xsecs={
        # based on GenXSecAnalyzer
        13.6: Number(41.0400, {"tot": 0.1968}),
    },
)

w_vbf.set_xsec(13.6, w_vbf_wlnu.get_xsec(13.6) / const.br_w.lep)

w_vbf_wqq = w_vbf.add_process(
    name="w_vbf_wqq",
    id=6311,
    label=r"W $\rightarrow q\bar{q}$ (VBF)",
    xsecs={
        13.6: w_vbf.get_xsec(13.6) * const.br_w.had,
    },
)

#
# EWK radiations
# TODO: EWK is inaccurate, use dedicated z_vbf and w_vbf processes instead
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    # TODO: Sum over the other? maybe with scaled w xsec to inclusive?
)

# based on GenXSecAnalyzer
# for EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_wp_lnu_m50toinf = ewk.add_process(
    name="ewk_wp_lnu_m50toinf",
    id=7100,
    xsecs={
        13: Number(39.07, {"tot": 0.006454}),
    },
)

# based on GenXSecAnalyzer
# for EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_wm_lnu_m50toinf = ewk.add_process(
    name="ewk_wm_lnu_m50toinf",
    id=7200,
    xsecs={
        13: Number(32.10, {"tot": 0.005308}),
    },
)

# based on GenXSecAnalyzer
# for EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
ewk_z_ll_m50toinf = ewk.add_process(
    name="ewk_z_ll_m50toinf",
    id=7300,
    xsecs={
        13: Number(6.206, {"tot": 0.002081}),
    },
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
)

# ZZ
# Theory inclusive XS (qqZZ + ggZZ):
#   13 TeV:   NNLO+NNLL = 16.518 ± 1.84% pb from https://journals.aps.org/prd/abstract/10.1103/2rr7-5xv3, table 1
#   13.6 TeV: NNLO+NNLL = 17.627 ± 1.93% pb from the same paper, table 1
# For the inclusive Pythia sample (ZZ_TuneCP5_13p6TeV_pythia8), XSDB lists 12.75 pb.
# A second XSDB entry explicitly marks the order as LO (typical for Pythia-only samples).
# Applying k=1.51 (LO→NNLO) gives 12.75 × 1.51 = 19.2525 pb.
#
# NOTE on k-factor: k=1.15 is used for NLO→NNLO (powheg/amcatnlo samples);
# k=1.51 is used for LO→NNLO (Pythia-only/inclusive samples).
# See Torben's slides: https://indico.cern.ch/event/1677270/contributions/7200886/attachments/3317393/5938464/ZZXS.pdf
#
# NOTE on per-decay-mode normalization: each dataset is normalized by its own
# XSDB cross section (per decay mode) × k-factor. The per-decay-mode NLO values
# from XSDB do NOT sum to the inclusive (they exceed it due to overlap / different
# phase space cuts / EWK contributions at NLO enhancing leptonic modes).
# If combining multiple ZZ decay-mode samples, stitching would be required.

# k-factors for ZZ
# See Torben's slides: https://indico.cern.ch/event/1677270/contributions/7200886/attachments/3317393/5938464/ZZXS.pdf
zz_k_nlo_to_nnlo = 1.15   # NLO→NNLO (powheg/amcatnlo samples)
zz_k_lo_to_nnlo = 1.51    # LO→NNLO (Pythia-only/inclusive samples)
# ggZZ: k=1.7 (LO MCFM → NLO) from the same slides
zz_gg_k_lo_to_nlo = 1.7

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # NNLO+NNLL from https://journals.aps.org/prd/abstract/10.1103/2rr7-5xv3, table 1
        13: Number(16.518, {"scale": 0.0184j}),
        13.6: Number(17.627, {"scale": 0.0193j}),
    },
)

# qqZZ: each decay mode normalized independently by its NLO XSDB value × k=1.15
# NLO XS values from XSDB for individual powheg/amcatnlo samples
qqzz = zz.add_process(
    name="qqzz",
    id=8170,
    label=r"$q\bar{q} \rightarrow ZZ$",
    xsecs={
        # XSDB inclusive (LO, Pythia-only) × k(LO→NNLO)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS%3DZZ_TuneCP5_13TeV-pythia8
        13: Number(12.14) * zz_k_lo_to_nnlo,
        # XSDB inclusive (LO, Pythia-only) × k(LO→NNLO)
        13.6: Number(12.75) * zz_k_lo_to_nnlo,
    },
)

zz_zll_zll = zz.add_process(
    name="zz_zll_zll",
    id=8130,
    xsecs={
        # 13 TeV: XSDB NLO 1.256 pb (ZZTo4L powheg) × k(NLO→NNLO)
        # NOTE: ZZTo4L amcatnlo is not on XSDB; CMS AN-19-191 gives 1.5 pb × k=1.15 = 1.725 pb (NNLO+NNLL)
        13: Number(1.256) * zz_k_nlo_to_nnlo,
        # 13.6 TeV: XSDB NLO 1.39 pb (ZZto4L powheg) × k(NLO→NNLO)
        13.6: Number(1.39) * zz_k_nlo_to_nnlo,
    },
)

zz_zqq_zll = zz.add_process(
    name="zz_zqq_zll",
    id=8110,
    xsecs={
        # 13 TeV: NLO from GenXSecAnalyzer on UL18 MiniAODv2 (1M events) × k=1.15 (NLO→NNLO)
        # Sample: ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (amcatnloFXFX → NLO)
        # Torben confirmed: XSDB "LO" label is misleading; generator is NLO (amcatnloFXFX)
        # GenXSecAnalyzer After filter: 3.698 ± 0.004 pb × k=1.15 = 4.253 pb
        # (consistent with XSDB value 3.676 pb for same sample)
        # NOTE: 13 TeV sample has mllmin4p0 cut; 13.6 TeV uses powheg without this cut — different phase space
        13: Number(3.698, {"tot": 0.004}) * zz_k_nlo_to_nnlo,
        # 13.6 TeV: XSDB NLO 6.788 pb (ZZto2L2Q powheg) × k(NLO→NNLO)
        13.6: Number(6.788) * zz_k_nlo_to_nnlo,
    },
)

zz_zll_znunu = zz.add_process(
    name="zz_zll_znunu",
    id=8120,
    xsecs={
        # 13 TeV: NLO from GenXSecAnalyzer on UL18 MiniAODv2 (1M events) × k=1.15 (NLO→NNLO)
        # Sample: ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2 (Powheg NLO, ~0% neg. weights)
        # Gridpack: ZZ_slc7_amd64_gcc820_CMSSW_11_0_1_ZZ2L2Nu.tgz (UL v2, mll > 4 GeV)
        # GenXSecAnalyzer After filter: 0.9738 ± 0.001 pb × k=1.15 = 1.1199 pb
        # (sanity: 1.120 pb at 13 TeV < 1.186 pb at 13.6 TeV → ~5.5% energy scaling ✓)
        # NOTE (Torben): the Autumn18 sample (RunIIAutumn18MiniAOD, gridpack v1 with mll > 40 GeV) gives 0.6008 pb —
        # a different phase space; treat as ZZTo2L2Nu_mll40 if needed.
        # The UL value (0.9738 pb, mll > 4 GeV) is used here.
        13: Number(0.9738, {"tot": 0.001}) * zz_k_nlo_to_nnlo,
        # 13.6 TeV: XSDB NLO 1.031 pb (ZZto2L2Nu powheg) × k(NLO→NNLO)
        13.6: Number(1.031) * zz_k_nlo_to_nnlo,
    },
)

zz_znunu_zqq = zz.add_process(
    name="zz_znunu_zqq",
    id=8150,
    xsecs={
        # 13 TeV: NLO from GenXSecAnalyzer on UL18 MiniAODv2 (1M events) × k=1.15 (NLO→NNLO)
        # Sample: ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8 (ZZTo2Q2Nu01j_5f_NLO_FXFX gridpack → amcatnloFXFX)
        # Torben confirmed: XSDB "LO" label is misleading; generator is NLO (amcatnloFXFX)
        # GenXSecAnalyzer After filter: 4.487 ± 0.008 pb × k=1.15 = 5.160 pb
        # (sanity check: 5.160 pb at 13 TeV < 5.5499 pb at 13.6 TeV — physically consistent)
        13: Number(4.487, {"tot": 0.008}) * zz_k_nlo_to_nnlo,
        # 13.6 TeV: XSDB NLO 4.826 pb (ZZto2Nu2Q powheg) × k(NLO→NNLO)
        13.6: Number(4.826) * zz_k_nlo_to_nnlo,
    },
)

zz_zqq_zqq = zz.add_process(
    name="zz_zqq_zqq",
    id=8140,
    xsecs={
        # 13 TeV: NLO from XSDB × k=1.15 (NLO→NNLO)
        # Sample: ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=40&searchQuery=process_name%3D%5EZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8
        # XSDB NLO: 6.912 pb × k(NLO→NNLO)
        # NOTE: GenXSecAnalyzer on ZZTo4Q_5f (no madspin) gives only 3.305 pb — different generator setup,
        # likely a mass cut difference (Torben). The madspin sample is consistent with the 13.6 TeV setup.
        # (sanity: 6.912×k at 13 TeV < 7.832×k at 13.6 TeV → ~12% energy scaling ✓)
        13: Number(6.912) * zz_k_nlo_to_nnlo,
        # 13.6 TeV: XSDB NLO 7.832 pb (ZZto4Q amcatnlo) × k(NLO→NNLO)
        13.6: Number(7.832) * zz_k_nlo_to_nnlo,
    },
)

# ggZZ: each decay mode normalized independently by its LO MCFM value × k=1.7
# LO XS values in fb from XSDB for individual mcfm samples
# See slides: https://indico.cern.ch/event/1677270/contributions/7200886/attachments/3317393/5938464/ZZXS.pdf
#
# Same-flavor modes (4e, 4μ, 4τ) have the same XSDB LO value;
# different-flavor modes (2e2μ, 2e2τ, 2μ2τ) also share a common value.
# Store these as variables to avoid repetition and make the origin clear.

# XSDB LO values (in fb) for same-flavor ggZZ modes (GluGlu2Zto4L mcfm)
gg_zz_lo_same_13 = Number(2.703e-03)    # GluGlu2Zto4E / 4Mu / 4Tau, 13 TeV
gg_zz_lo_same_13p6 = Number(5.199467e-03)  # GluGlu2Zto4E / 4Mu / 4Tau, 13.6 TeV

# XSDB LO values (in fb) for different-flavor ggZZ modes (GluGlu2Zto2L2L' mcfm)
gg_zz_lo_diff_13 = Number(5.423e-03)       # GluGlu2Zto2E2Mu / 2E2Tau / 2Mu2Tau, 13 TeV
gg_zz_lo_diff_13p6 = Number(10.610669e-03)  # GluGlu2Zto2E2Mu / 2E2Tau / 2Mu2Tau, 13.6 TeV

ggzz = zz.add_process(
    name="ggzz",
    id=8180,
    label=r"$gg \rightarrow ZZ$",
    xsecs={
        # sum of ggZZ decay modes: 3 same-flavor + 3 different-flavor
        13: (gg_zz_lo_same_13 + gg_zz_lo_diff_13) * const.n_leps,
        13.6: (gg_zz_lo_same_13p6 + gg_zz_lo_diff_13p6) * const.n_leps,
    },
)

zz_zee_zee = zz.add_process(
    name="zz_zee_zee",
    id=8160,
    xsecs={
        13: gg_zz_lo_same_13,
        13.6: gg_zz_lo_same_13p6,
    },
)

zz_zee_zmm = zz.add_process(
    name="zz_zee_zmm",
    id=8161,
    xsecs={
        13: gg_zz_lo_diff_13,
        13.6: gg_zz_lo_diff_13p6,
    },
)

zz_zee_ztt = zz.add_process(
    name="zz_zee_ztt",
    id=8162,
    xsecs={
        13: gg_zz_lo_diff_13,
        13.6: gg_zz_lo_diff_13p6,
    },
)

zz_zmm_zmm = zz.add_process(
    name="zz_zmm_zmm",
    id=8163,
    xsecs={
        13: gg_zz_lo_same_13,
        13.6: gg_zz_lo_same_13p6,
    },
)

zz_zmm_ztt = zz.add_process(
    name="zz_zmm_ztt",
    id=8164,
    xsecs={
        13: gg_zz_lo_diff_13,
        13.6: gg_zz_lo_diff_13p6,
    },
)

zz_ztt_ztt = zz.add_process(
    name="zz_ztt_ztt",
    id=8165,
    xsecs={
        13: gg_zz_lo_same_13,
        13.6: gg_zz_lo_same_13p6,
    },
)

# WZ inclusive NLO xsec values from https://arxiv.org/pdf/1105.0020.pdf v1
wp_z_xsec = {
    13: Number(28.55, {"scale": (0.041j, 0.032j)}),
}

wm_z_xsec = {
    13: Number(18.19, {"scale": (0.041j, 0.033j)}),
}

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(25.56) (LO)
wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # as a remark, the W cross section calculation from
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
        # shows a permille difference in the values calculated directly and the ones added from w+ and w-
        13: wp_z_xsec[13] + wm_z_xsec[13],
        # 13.6 from GenXSecAnalyzer:
        13.6: Number(29.17, {
            "tot": 0.005941,  # xsdb: Number(29.1, {"tot": 0.1318}),
        }),
    },
)

# WZto3LNu cross sections for the powheg decay-mode sample (W->lnu, Z->ll).
# Each decay mode is normalized independently by its XSDB NLO value × k-factor (NNLO QCD x NLO EW).
# k-factor is between NNLO QCD x NLO EW (MATRIX) and NLO POWHEG (not NLO MATRIX).
# MATRIX paper: https://arxiv.org/abs/1912.00068

# k-factors for WZ decay modes (NLO POWHEG -> NNLO QCD x NLO EW)
wz_k_run2 = 1.19  # from WZ Run2 paper: https://arxiv.org/pdf/2110.11231
wz_k_run3 = 1.08  # from WZ Run3 paper: https://arxiv.org/pdf/2412.02477
wz_wlnu_zll = wz.add_process(
    name="wz_wlnu_zll",
    id=8210,
    xsecs={
        # XSDB NLO (powheg) 4.42965 pb × k(NLO POWHEG -> NNLO QCD x NLO EW)
        # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson (NLO: 4.42965 pb)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS=WZto3LNu_TuneCUETP8M1_13TeV-powheg-pythia8  # noqa
        13: Number(4.42965) * wz_k_run2,
        # XSDB NLO (powheg) 4.924 pb × k(NLO POWHEG -> NNLO QCD x NLO EW)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS=WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8  # noqa
        13.6: Number(4.924) * wz_k_run3,
    },
)

wz_wqq_zll = wz.add_process(
    name="wz_wqq_zll",
    id=8220,
    xsecs={
        13: wz.get_xsec(13) * const.br_w.had * const.br_z.clep,
        # XSDB NLO (powheg) 7.568 pb × k(NLO POWHEG -> NNLO QCD x NLO EW)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/ DAS=WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8
        # verified from CMS AN-2023/179
        # MATRIX paper: https://arxiv.org/abs/1912.00068
        13.6: Number(7.568) * wz_k_run3,
    },
)

wz_wqq_zqq = wz.add_process(
    name="wz_wqq_zqq",
    id=8240,
    xsecs={
        13: wz.get_xsec(13) * const.br_w.had * const.br_z.qq,
        # XSDB labels this as "LO" but it is actually NLO (amcatnloFXFX = NLO + FxFx jet merging):
        #   - 21% negative weights (impossible at LO)
        #   - FxFx matching efficiency ~63% (before: 39.31 pb, after: 24.97 pb)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/ DAS=WZto4Q-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8
        # GenXSecAnalyzer (Run3Summer22EEMiniAODv4, 1M events): 24.97 ± 0.03314 pb (after matching)
        # NLO (amcatnlo) 24.97 pb × k(NLO -> NNLO QCD x NLO EW)
        # MATRIX paper: https://arxiv.org/abs/1912.00068
        13.6: Number(24.97, {"tot": 0.03314}) * wz_k_run3,
    },
)

# GenXSecAnalyzer of WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# -> value: Number(9.159, {"tot": 0.008259}), also available but not used for 13 TeV
wz_wlnu_zqq = wz.add_process(
    name="wz_wlnu_zqq",
    id=8230,
    xsecs={
        13: wz.get_xsec(13) * const.br_w.lep * const.br_z.qq,
        # XSDB NLO (powheg) 15.87 pb × k(NLO POWHEG -> NNLO QCD x NLO EW)
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/ DAS=WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8
        # GenXSecAnalyzer (Run3Summer22EEMiniAODv4, 1M events): 15.87 ± 0.007874 pb — exact match with XSDB
        # MATRIX paper: https://arxiv.org/abs/1912.00068
        13.6: Number(15.87, {"tot": 0.007874}) * wz_k_run3,
    },
)

# wz + photon
wzg = Process(
    name="wzg",
    id=9500,
    label=r"WZ + $\gamma$",
)

wzg_wlnu = wzg.add_process(
    name="wzg_wlnu",
    id=9501,
    label=r"$W(\rightarrow \ell\nu)Z + \gamma$",
    xsecs={
        # XSDB (Run3Summer22)
        13.6: Number(0.08425, {
            "tot": 4.238e-05,
        }),
    },
)

# w + photon
wg_wlnu = Process(
    name="wg_wlnu",
    id=9600,
    label=r"$W\gamma \rightarrow \ell\nu\gamma$",
    xsecs={
        # NLO from XSDB: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=40&searchQuery=process_name%3D%5EWGtoLNuG-1Jets_TuneCP5_13p6TeV  # noqa
        13.6: Number(671.5, {
            "tot": 0.7548,
        }),
    },
)

# DY + photon (Zγ)
# Run 3 naming: DYGto2LG-1Jets (was ZGTo2LG in Run 2)
# NLO cross sections from XSDB for inclusive samples
# LO cross sections from XSDB for PTG-binned samples (bounded bins, 2022/2023)
# NLO cross sections from XSDB for PTG-binned samples (open thresholds, 2024 Bin- convention)

dyg = Process(
    name="dyg",
    id=9700,
    label=r"DY+$\gamma$",
)

dyg_m50toinf = dyg.add_process(
    name="dyg_m50toinf",
    id=9710,
    label=r"DY+$\gamma$ ($m_{\ell\ell} \geq 50$)",
    xsecs={
        # NLO from XSDB: DYGto2LG-1Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8
        13.6: Number(127.0, {
            "tot": 0.1484,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
    },
)

# bounded PTG bins (used in 2022/2023 campaigns)

dyg_m50toinf_ptg10to100 = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg10to100",
    id=9711,
    xsecs={
        # LO from XSDB
        13.6: Number(126.6, {
            "tot": 0.4287,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (10.0, 100.0),
    },
)

dyg_m50toinf_ptg100to200 = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg100to200",
    id=9712,
    xsecs={
        # LO from XSDB
        13.6: Number(0.3493, {
            "tot": 0.001778,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (100.0, 200.0),
    },
)

dyg_m50toinf_ptg200to400 = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg200to400",
    id=9713,
    xsecs={
        # LO from XSDB
        13.6: Number(0.04331, {
            "tot": 0.000221,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (200.0, 400.0),
    },
)

dyg_m50toinf_ptg400to600 = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg400to600",
    id=9714,
    xsecs={
        # LO from XSDB
        13.6: Number(0.00313, {
            "tot": 0.00001539,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (400.0, 600.0),
    },
)

dyg_m50toinf_ptg600toinf = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg600toinf",
    id=9715,
    xsecs={
        # LO from XSDB
        13.6: Number(0.0006528, {
            "tot": 0.000002983,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (600.0, const.inf),
    },
)

# open-threshold PTG bins (used in 2024 Bin- convention)

dyg_m50toinf_ptg100toinf = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg100toinf",
    id=9716,
    xsecs={
        # NLO from XSDB: DYGto2LG-1Jets_Bin-MLL-50-PTG-100
        13.6: Number(0.3942, {
            "tot": 0.0007196,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (100.0, const.inf),
    },
)

dyg_m50toinf_ptg200toinf = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg200toinf",
    id=9717,
    xsecs={
        # NLO from XSDB: DYGto2LG-1Jets_Bin-MLL-50-PTG-200
        13.6: Number(0.04738, {
            "tot": 0.00008731,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (200.0, const.inf),
    },
)

dyg_m50toinf_ptg400toinf = dyg_m50toinf.add_process(
    name="dyg_m50toinf_ptg400toinf",
    id=9718,
    xsecs={
        # NLO from XSDB: DYGto2LG-1Jets_Bin-MLL-50-PTG-400
        13.6: Number(0.003741, {
            "tot": 0.00002272,
        }),
    },
    aux={
        "mll": (50.0, const.inf),
        "ptg": (400.0, const.inf),
    },
)

dyg_m4to50 = dyg.add_process(
    name="dyg_m4to50",
    id=9720,
    label=r"DY+$\gamma$ ($4 \leq m_{\ell\ell} < 50$)",
    xsecs={
        # NLO from XSDB: DYGto2LG-1Jets_Bin-MLL-4to50 (2024)
        13.6: Number(88.13, {
            "tot": 0.09618,
        }),
    },
    aux={
        "mll": (4.0, 50.0),
    },
)

dyg_m4to50_ptg10to100 = dyg_m4to50.add_process(
    name="dyg_m4to50_ptg10to100",
    id=9721,
    xsecs={
        # LO from XSDB
        13.6: Number(88.17, {
            "tot": 0.2807,
        }),
    },
    aux={
        "mll": (4.0, 50.0),
        "ptg": (10.0, 100.0),
    },
)

dyg_m4to50_ptg100to200 = dyg_m4to50.add_process(
    name="dyg_m4to50_ptg100to200",
    id=9722,
    xsecs={
        # LO from XSDB
        13.6: Number(0.2413, {
            "tot": 0.001249,
        }),
    },
    aux={
        "mll": (4.0, 50.0),
        "ptg": (100.0, 200.0),
    },
)

dyg_m4to50_ptg200toinf = dyg_m4to50.add_process(
    name="dyg_m4to50_ptg200toinf",
    id=9723,
    xsecs={
        # LO from XSDB
        13.6: Number(0.02224, {
            "tot": 0.0001052,
        }),
    },
    aux={
        "mll": (4.0, 50.0),
        "ptg": (200.0, const.inf),
    },
)

# NNLO QCD from https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=28
# itself from https://arxiv.org/pdf/1408.5243.pdf v1
#
# 13.6 TeV: WW_TuneCP5_13p6TeV_pythia8 is LO Pythia (WeakDoubleBoson:ffbar2WW, qq only).
# McM fragment: BTV-Run3Summer22GS-00015, crossSection = 75.8 (hardcoded LO).
# GenXSecAnalyzer: 80.22 pb (LO). XSDB: 80.23 pb.
# k(LO→NNLO) ≈ 1.75 from Grazzini et al., JHEP 08 (2016) 140 [arXiv:1605.02716], Table 2:
#   13 TeV: NNLO/LO = 1370.9/778.99 = 1.76
#
# k-factors for WW
#   qqWW: k=1.14 (NLO→NNLO) from arXiv:1605.02716 (Grazzini et al., JHEP 08 (2016) 140)
#   ggWW: k=1.41 (LO→NLO) from arXiv:1511.08617 (Caola et al., Phys. Lett. B 754 (2016) 275)
#   LO→NNLO (Pythia inclusive): k≈1.75 from the same Grazzini et al. paper
ww_k_lo_to_nnlo = 1.75    # LO→NNLO (Pythia inclusive)
ww_k_nlo_to_nnlo = 1.14   # qqWW: NLO→NNLO
ww_gg_k_lo_to_nlo = 1.41  # ggWW: LO MCFM → NLO

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        13: Number(118.7, {"scale": (0.025j, 0.022j)}),
        # 13.6: LO Pythia GenXSecAnalyzer × k(LO→NNLO)
        13.6: Number(80.22, {"tot": 0.01677}) * ww_k_lo_to_nnlo,
    },
)

# update vv cross section
for cme in [13]:
    vv.set_xsec(cme, ww.get_xsec(cme) + wz.get_xsec(cme) + zz.get_xsec(cme))

# qqWW: each decay mode normalized independently by its NLO XSDB value × k(NLO→NNLO)
# NLO XS values from XSDB for individual Powheg samples (WWto2L2Nu, WWtoLNu2Q, WWto4Q)

# XSDB NLO values (pb) for individual qqWW decay modes at 13.6 TeV
ww_dl_nlo_13p6 = Number(11.79, {"tot": 0.004216})
ww_sl_nlo_13p6 = Number(48.94, {"tot": 0.0175})
ww_fh_nlo_13p6 = Number(50.79, {"tot": 0.01816})

qqww = ww.add_process(
    name="qqww",
    id=8370,
    label=r"$q\bar{q} \rightarrow WW$",
    xsecs={
        13: ww.get_xsec(13),  # at 13 TeV, qqWW ≈ inclusive (ggWW is small)
        # 13.6: sum of Powheg NLO decay modes × k(NLO→NNLO)
        13.6: (ww_dl_nlo_13p6 + ww_sl_nlo_13p6 + ww_fh_nlo_13p6) * ww_k_nlo_to_nnlo,
    },
)

# no additional cut found in generator card:
# https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/Powheg/production/2017/13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV.input  # noqa
# therefore, 13 TeV value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 (Summer20UL16, NLO) with Number(11.09, {"tot": 0.00704})
# also available, but not used here
ww_dl = ww.add_process(
    name="ww_dl",
    id=8310,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.dl,  # value around 12.6 for comparison to GenXSecAnalyzer NLO result
        # 13.6: XSDB NLO × k(NLO→NNLO)
        13.6: ww_dl_nlo_13p6 * ww_k_nlo_to_nnlo,
    },
)

# no additional cut found in generator card in MCM:
# dataset: /WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM  # noqa
# therefore, 13 TeV value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(50.94, {"tot": 0.042})
# also available, but not used here
ww_sl = ww.add_process(
    name="ww_sl",
    id=8320,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.sl,  # value around 50.06 for comparison to GenXSecAnalyzer NLO result
        # 13.6: XSDB NLO × k(NLO→NNLO)
        13.6: ww_sl_nlo_13p6 * ww_k_nlo_to_nnlo,
    },
)

# no additional cut found in generator card in MCM:
# dataset: /WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3/MINIAODSIM  # noqa
# therefore, 13 TeV value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# for WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) -> value : Number(51.53, {"tot": 0.04349})
# also available, but not used here
ww_fh = ww.add_process(
    name="ww_fh",
    id=8330,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.fh,  # value around 53.94 for comparison to GenXSecAnalyzer NLO result
        # 13.6: XSDB NLO × k(NLO→NNLO)
        13.6: ww_fh_nlo_13p6 * ww_k_nlo_to_nnlo,
    },
)

# ggWW: each decay mode normalized independently by its LO MCFM value × k(LO→NLO)
# LO XS values in fb from XSDB for individual mcfm samples (XSDB mistakenly lists as pb; MCFM outputs in fb)
# See also CMS AN-2023/179.
#
# NOTE on same-flavor vs different-flavor:
# MCFM gridpacks give the same XS for all channels (per-sample).
# Same-flavor (ee, μμ, ττ): 1 sample per pair → XS = mcfm_lo × k
# Different-flavor (eμ, eτ, μτ): 2 samples per pair (e.g., ENuMuNu + MuNuENu) → XS = 2 × mcfm_lo × k
# Total ggWW→2l2ν = (same + diff) × n_leps

# MCFM LO value (pb, converted from fb) — same for all channels at 13.6 TeV
gg_ww_mcfm_lo_13p6 = Number(49.63e-03)  # 49.63 fb from XSDB

# per-channel: same-flavor = 1× and different-flavor = 2× (two sample orderings)
gg_ww_same_13p6 = gg_ww_mcfm_lo_13p6 * ww_gg_k_lo_to_nlo
gg_ww_diff_13p6 = 2 * gg_ww_mcfm_lo_13p6 * ww_gg_k_lo_to_nlo

ggww = ww.add_process(
    name="ggww",
    id=8380,
    label=r"$gg \rightarrow WW$",
    xsecs={
        # sum of ggWW decay modes: (same + diff) × n_leps
        13.6: (gg_ww_same_13p6 + gg_ww_diff_13p6) * const.n_leps,
    },
)

ww_wenu_wenu = ww.add_process(
    name="ww_wenu_wenu",
    id=8311,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.enuenu,
        13.6: gg_ww_same_13p6,  # same-flavor, 1 sample
    },
)

ww_wenu_wmnu = ww.add_process(
    name="ww_wenu_wmnu",
    id=8312,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.enumnu,
        13.6: gg_ww_diff_13p6,  # different-flavor, 2 samples (ENuMuNu + MuNuENu)
    },
)

ww_wenu_wtnu = ww.add_process(
    name="ww_wenu_wtnu",
    id=8313,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.enutnu,
        13.6: gg_ww_diff_13p6,  # different-flavor, 2 samples
    },
)

ww_wmnu_wmnu = ww.add_process(
    name="ww_wmnu_wmnu",
    id=8314,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.mnumnu,
        13.6: gg_ww_same_13p6,  # same-flavor, 1 sample
    },
)

ww_wmnu_wtnu = ww.add_process(
    name="ww_wmnu_wtnu",
    id=8315,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.mnutnu,
        13.6: gg_ww_diff_13p6,  # different-flavor, 2 samples
    },
)

ww_wtnu_wtnu = ww.add_process(
    name="ww_wtnu_wtnu",
    id=8316,
    xsecs={
        13: ww.get_xsec(13) * const.br_ww.tnutnu,
        13.6: gg_ww_same_13p6,  # same-flavor, 1 sample
    },
)

# same-sign WW (EWK+QCD)
ww_ss_2j = Process(
    name="ww_ss_2j",
    id=8400,
    label=r"$W^{\pm}W^{\pm}jj$",
    xsecs={
        # LO from XSDB: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=40&searchQuery=process_name%3D%5EWpWpJJ-EWK-QCD_TuneCP5_13p6TeV  # noqa
        13.6: Number(0.0587, {
            "tot": 0.00001523,
        }),
    },
)

#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    # xsecs set below as sum over individual processes
)

# based on GenXSecAnalyzer
# for ZZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO)
# remark: calculated xsec has lower error for sample without ext-1 as not all events were used for calculation of ext-1
# therefore the value for the sample without ext-1 is taken
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa
zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={
        13: Number(0.01476, {"tot": 2.347 * 10**(-6)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.01591, {
            "tot": 0.000007828,
        }),
    },
)

# based on GenXSecAnalyzer
# for WZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={
        13: Number(0.05709, {"tot": 6.213 * 10**(-5)}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.06206, {
            "tot": 0.00003689,
        }),
    },
)

# based on GenXSecAnalyzer
# for WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={
        13: Number(0.1707, {"tot": 0.0001757}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.1851, {
            "tot": 0.00009482,
        }),
    },
)

# based on GenXSecAnalyzer
# for WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17_ext1-v1 -n 5000000  # noqa
www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={
        13: Number(0.2158, {"tot": 0.0002479}),
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        # same value as xsdb obtained
        13.6: Number(0.2328, {
            "tot": 0.0001247,
        }),
    },
)

# update vvv cross section
for cme in [13]:
    vvv.set_xsec(cme, www.get_xsec(cme) + wwz.get_xsec(cme) + wzz.get_xsec(cme) + zzz.get_xsec(cme))
