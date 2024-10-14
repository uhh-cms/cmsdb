# coding: utf-8

"""
HH -> bbtautau datasets for the 2023 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14931248,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-tsg_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=985000,
)

# BSM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=14931313,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=959000,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_c21_powheg",
    id=14931215,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1_c21],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=994000,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p10_powheg",
    id=14931140,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p10],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=990960,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=14931233,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=998174,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=14930778,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=992000,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=14931022,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=990000,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=14931153,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=995107,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=14930961,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=991000,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_lheweights_powheg",
    id=14940620,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=236,
    n_events=2860485,
)
