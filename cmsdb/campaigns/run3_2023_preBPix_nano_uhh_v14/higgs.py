# coding: utf-8

"""
Higgs datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn


#
# Single Higgs
#

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=15020867,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3_375_274,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14920330,
    processes=[procs.h_ggf_hbb],
    keys=[
        "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=10_911_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=15022656,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_843_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14900090,
    processes=[procs.h_vbf_hbb],
    keys=[
        "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=11_049_000,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14900025,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=11_066_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14845320,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=10_848_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14900022,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=11_054_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927609,
    processes=[procs.zh_htt],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=69_949,
    aux={
        "merging_factors": {
            "nominal": 33,
        },
    },
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14837706,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=10_970_000,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14900377,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=11_061_000,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14927426,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=70_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14905185,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=10_881_782,
    aux={
        "merging_factors": {
            "nominal": 35,
        },
    },
)

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14900822,
    processes=[procs.wmh_wqq_hbb],
    keys=[
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=11_064_878,
    aux={
        "merging_factors": {
            "nominal": 35,
        },
    },
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14927451,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=68_000,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14845614,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=11_042_360,
    aux={
        "merging_factors": {
            "nominal": 34,
        },
    },
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14900184,
    processes=[procs.wph_wqq_hbb],
    keys=[
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=11_032_400,
    aux={
        "merging_factors": {
            "nominal": 34,
        },
    },
)

cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=15021983,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=518_559,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14901065,
    processes=[procs.tth_hbb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=10_916_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14918969,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=11_901_980,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)
