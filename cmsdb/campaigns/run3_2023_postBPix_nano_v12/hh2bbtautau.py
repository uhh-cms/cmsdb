# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
HH -> bbtautau datasets for the 2023 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn


#
# ggF -> H -> HH
#


# SM
cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_1_kt_1_c2_0_powheg",
    id=14931120,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-tsg_130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=494000,
)


# BSM
cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_0_kt_1_c2_1_powheg",
    id=14930533,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=490000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_1_kt_1_c2_3_powheg",
    id=14931408,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=496000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_5_kt_1_c2_0_powheg",
    id=14931619,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=496000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_1_kt_1_c2_m2_powheg",
    id=14930980,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=498000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_0_kt_1_c2_0_powheg",
    id=14931073,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=492000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_1_kt_1_c2_0p35_powheg",
    id=14931113,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=496000,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_1_kt_1_c2_0p10_powheg",
    id=14930917,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=496409,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_2p45_kt_1_c2_0_powheg",
    id=14930553,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=499198,
)

cpn.add_dataset(
    name="ggf_hh_bbtautau_kl_2p45_kt_1_c2_0_LHEweights_powheg",
    id=14943641,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=1497480,
)
