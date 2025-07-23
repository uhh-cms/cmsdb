# coding: utf-8

"""
Higgs datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn


#
# single Higgs
#

cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=14849349,
    processes=[procs.h_ggf_hww2l2nu],
    keys=[
        "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=4_980_263,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14802769,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-Poisson70KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=288_000,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14876615,
    processes=[procs.h_ggf_hbb],
    keys=[
        "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=15_489_920,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14849308,
    processes=[procs.h_vbf_hww2l2nu],
    keys=[
        "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=4_987_403,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14796264,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-Poisson70KeepRAW_130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=296_000,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14857768,
    processes=[procs.h_vbf_hbb],
    keys=[
        "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=12_207_120,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=14850112,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=502_646,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14796154,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4 + 22,
    n_events=2_006_504 + 13_000_000,
    aux={
        "merging_factors": {
            "nominal": 21,
            "nominal_ext1": 31,
        },
    },
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14803894,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4 + 22,
    n_events=2_120_400 + 12_773_482,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 29,
        },
    },
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14925738,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=70_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14925239,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=67_580,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14810634,
    processes=[procs.wph_wqq_hbb],
    keys=[
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7 + 19,
    n_events=4_085_059 + 11_324_561,
    aux={
        "merging_factors": {
            "nominal": 12,
            "nominal_ext1": 37,
        },
    },
)

cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14801252,
    processes=[procs.wmh_wqq_hbb],
    keys=[
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7 + 19,
    n_events=3_954_095 + 11_272_563,
    aux={
        "merging_factors": {
            "nominal": 13,
            "nominal_ext1": 30,
        },
    },
)

cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14918166,
    processes=[procs.zh_hww2l2nu],
    keys=[
        "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_499_224,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14802578,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4 + 26,
    n_events=2_062_940 + 12_922_762,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 22,
        },
    },
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14790774,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=7 + 20,
    n_events=4_090_842 + 11_235_300,
    aux={
        "merging_factors": {
            "nominal": 12,
            "nominal_ext1": 19,
        },
    },
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927557,
    processes=[procs.zh_htt],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=69_650,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14796534,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=5 + 31,
    n_events=2_068_050 + 13_375_416,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 15,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14792576,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=4 + 28,
    n_events=1_974_279 + 13_444_960,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 20,
        },
    },
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14805746,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=3 + 21,
    n_events=2_000_334 + 13_464_950,
    aux={
        "merging_factors": {
            "nominal": 20,
            "nominal_ext1": 19,
        },
    },
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14868529,
    processes=[procs.tth_hbb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=11_319_724,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14845758,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=13_925_798,
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
    id=15043181,
    processes=[procs.thq],
    keys=[
        "/THQ_ctcvcp_HIncl_M-125_4FS_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=13_805_781,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="thw_madgraph",
    id=15043227,
    processes=[procs.thw],
    keys=[
        "/THW_ctcvcp_HIncl_M-125_5FS_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=6_936_630,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

#
# ttVH
#

cpn.add_dataset(
    name="ttzh_madgraph",
    id=14859451,
    processes=[procs.ttzh],
    keys=[
        "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2_785_771,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=14855575,
    processes=[procs.ttwh],
    keys=[
        "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2_800_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)
