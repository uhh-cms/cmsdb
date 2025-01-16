# coding: utf-8

"""
Higgs datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn


#
# Single Higgs
#

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14845170,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3_922_000,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=15022492,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_822_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=15020701,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=503_175,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14904888,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_392_541,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14914563,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_496_832,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14901029,
    processes=[procs.wmh_wqq_hbb],
    keys=[
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_531_019,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14900906,
    processes=[procs.wph_wqq_hbb],
    keys=[
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_538_021,
    aux={
        "merging_factors": {
            "nominal": 40,
        },
    },
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14927430,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=30_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14927423,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=30_000,
    aux={
        "merging_factors": {
            "nominal": 1,
        },
    },
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14836857,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=5_559_000,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14901097,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_552_421,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927606,
    processes=[procs.zh_htt],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=29_949,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14900234,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=5_570_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14900171,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=5_550_000,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14900182,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=5_564_000,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14900360,
    processes=[procs.tth_hbb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5_574_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14919628,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=5_943_987,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)
