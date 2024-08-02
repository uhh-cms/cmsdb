# coding: utf-8

"""
Higgs datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


#
# Single Higgs
#

# ggf

# samples do not exist for preBPix

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=15022683,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=3900000,
)

# H radiation
cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14838001,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=202,
    n_events=10925000,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14900724,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=216,
    n_events=11060000,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14927610,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=67552,
)

# Maybe merge the Zfiltered and regular samples?
cpn.add_dataset(
    name="zh_tautau_filtered_powheg",
    id=14927389,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHto2TauUncorrelatedDecay_Filtered_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=268,
    n_events=1789875,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14927427,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=70000,
)

cpn.add_dataset(
    name="wmh_tautau_filtered_powheg",
    id=14927577,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=1290200,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14927461,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=68000,
)

cpn.add_dataset(
    name="wph_tautau_filtered_powheg",
    id=14927100,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=1887577,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14900026,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=143,
    n_events=11066000,
)

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14901069,
    processes=[procs.tth_bb],
    keys=[
        "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=131,
    n_events=10846000,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14919222,
    processes=[procs.tth_nonbb],
    keys=[
        "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=236,
    n_events=11901980,
)


# This too?
# cpn.add_dataset(
#     name="tth_nonbb_m1q_powheg",
#     id=14920051,
#     processes=[procs.tth_nonbb],
#     keys=[
#         "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=161,
#     n_events=11083178,
# )
