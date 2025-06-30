# coding: utf-8

"""
Higgs datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14 import campaign_run3_2022_preEE_nano_uhh_v14 as cpn


#
# Single Higgs
#

cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=14849362,
    processes=[procs.h_ggf_hww2l2nu],
    keys=[
        "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1_494_981,
    aux={
        "merging_factors": {
            "nominal": 40,
        },
    },
)

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14802020,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=295_722,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14876199,
    processes=[procs.h_ggf_hbb],
    keys=[
        "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4_353_624,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14849326,
    processes=[procs.h_vbf_hww2l2nu],
    keys=[
        "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_497_840,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14792119,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=299_337,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14870709,
    processes=[procs.h_vbf_hbb],
    keys=[
        "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3_354_955,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=14836666,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=147_250,
    aux={
        "merging_factors": {
            "nominal": 6,
        },
    },
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14805243,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1 + 8,
    n_events=590_044 + 4_400_000,
    aux={
        "merging_factors": {
            "nominal": 24,
            "nominal_ext1": 34,
        },
    },
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14802236,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1 + 8,
    n_events=565_746 + 4_186_150,
    aux={
        "merging_factors": {
            "nominal": 25,
            "nominal_ext1": 32,
        },
    },
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14809863,
    processes=[procs.wph_wqq_hbb],
    keys=[
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 6,
    n_events=1_199_214 + 3_184_502,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 35,
        },
    },
)

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14798338,
    processes=[procs.wmh_wqq_hbb],
    keys=[
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 6,
    n_events=1_147_965 + 3_165_352,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 47,
        },
    },
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14925459,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=30_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14926125,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=29_387,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14918270,
    processes=[procs.zh_hww2l2nu],
    keys=[
        "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=976_619,
    aux={
        "merging_factors": {
            "nominal": 36,
        },
    },
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14805330,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 9,
    n_events=599_100 + 4_363_648,
    aux={
        "merging_factors": {
            "nominal": 20,
            "nominal_ext1": 20,
        },
    },
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14803771,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=2 + 6,
    n_events=1_144_560 + 3_177_722,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 22,
        },
    },
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927153,
    processes=[procs.zh_htt],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=28_992,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14801535,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=2 + 9,
    n_events=582_250 + 3_782_190,
    aux={
        "merging_factors": {
            "nominal": 13,
            "nominal_ext1": 16,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14803209,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=2 + 8,
    n_events=578_672 + 3_796_788,
    aux={
        "merging_factors": {
            "nominal": 13,
            "nominal_ext1": 16,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14805531,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=1 + 6,
    n_events=581_016 + 3_785_194,
    aux={
        "merging_factors": {
            "nominal": 22,
            "nominal_ext1": 19,
        },
    },
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14857728,
    processes=[procs.tth_hbb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=3_180_918,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14849148,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=3_958_795,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

#
# tH
#

cpn.add_dataset(
    name="thq_4f_madgraph",
    id=15043259,
    processes=[procs.thq],
    keys=[
        "/THQ_ctcvcp_HIncl_M-125_4FS_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=3_978_217,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="thw_madgraph",
    id=15043138,
    processes=[procs.thw],
    keys=[
        "/THW_ctcvcp_HIncl_M-125_5FS_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=1_982_933,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

#
# ttVH
#

cpn.add_dataset(
    name="ttzh_madgraph",
    id=14861622,
    processes=[procs.ttzh],
    keys=[
        "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=798_996,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=14860506,
    processes=[procs.ttwh],
    keys=[
        "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=790_196,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)
