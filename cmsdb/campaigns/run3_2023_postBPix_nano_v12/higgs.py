# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
Higgs datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14845308,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=3922000,
)

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_v2_powheg",
    id=14845831,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=3988000,
)
# v2 vs v6?
cpn.add_dataset(
    name="h_vbf_tautau_v6_powheg",
    id=15022496,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=3834000,
)

# H radiation
cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14836898,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=5556000,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14902790,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=104,
    n_events=5556305,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14927596,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=29949,
)

# Maybe merge the filtered and regular samples?
cpn.add_dataset(
    name="zh_tautau_filtered_powheg",
    id=14927498,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_Filtered_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=230,
    n_events=1009433,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14927422,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=30000,
)

cpn.add_dataset(
    name="wmh_tautau_filtered_powheg",
    id=14927570,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=753115,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14927431,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=30000,
)

cpn.add_dataset(
    name="wph_tautau_filtered_powheg",
    id=14926515,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=1015644,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14900235,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=5570000,
)

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14900362,
    processes=[procs.tth_bb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=68,
    n_events=5576000,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14920188,
    processes=[procs.tth_nonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=138,
    n_events=5887987,
)


# cpn.add_dataset(
#     name="tth_nonbb_m1q_powheg",
#     id=14918806,
#     processes=[procs.tth_nonbb],
#     keys=[
#         "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=140,
#     n_events=5595534,
# )