# coding: utf-8

"""
Higgs datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14802020,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=295_722,
    aux={
        "nominal_merging_factor": 16,
    },
)

# vbf
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14792119,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=299_337,
    aux={
        "nominal_merging_factor": 12,
    },
)

# H radiation
cpn.add_dataset(
    name="vh_hnonbb_amcatnlo",
    id=14836666,
    processes=[procs.vh_hnonbb],
    keys=[
        "/VH_HtoNonbb_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=147_250,
    aux={
        "nominal_merging_factor": 6,
    },
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14805330,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 15,
    n_events=599_100 + 4_363_648,
    aux={
        "nominal_merging_factor": 20,
    },
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14803771,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=4 + 10,
    n_events=1_144_560 + 3_177_722,
    aux={
        "nominal_merging_factor": 8,
    },
)

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14805243,
    processes=[procs.wmh_wlnu_hbb],
    keys=[
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 13,
    n_events=590_044 + 4_400_000,
    aux={
        "nominal_merging_factor": 12,
    },
)

cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14802236,
    processes=[procs.wph_wlnu_hbb],
    keys=[
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 13,
    n_events=565_746 + 4_186_150,
    aux={
        "nominal_merging_factor": 13,
    },
)

# ggZH
cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14801535,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=3 + 14,
    n_events=582_250 + 3_782_190,
    aux={
        "nominal_merging_factor": 9,
    },
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14805531,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=2 + 11,
    n_events=581_016 + 3_785_194,
    aux={
        "nominal_merging_factor": 11,
    },
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14803209,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=2 + 14,
    n_events=578_672 + 3_796_788,
    aux={
        "nominal_merging_factor": 13,
    },
)

# ttH
cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14857728,
    processes=[procs.tth_hbb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=3_180_918,
    aux={
        "nominal_merging_factor": 8,
    },
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14849148,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=3_958_795,
    aux={
        "nominal_merging_factor": 8,
    },
)
