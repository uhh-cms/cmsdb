# coding: utf-8

"""
HH -> bbWW datasets for the 2023 postBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

#
# ggf, HH -> bbVV inclusive
#


# No SM (kl=1, kt=1) sample found as of now

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_hbbhvv_powheg",
    id=14951647,
    processes=[procs.ggHH_kl_2p45_kt_1_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=594432,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV single lepton
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_qqlnu_hbbhvv_powheg",
    id=14854361,
    processes=[procs.ggHH_kl_1_kt_1_qqlnu_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=495374,
    aux={"allow_uppercase_name": True},
)

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_qqlnu_hbbhvv_powheg",
    id=14945507,
    processes=[procs.ggHH_kl_2p45_kt_1_qqlnu_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=149445,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV dilepton
#

# No SM (kl=1, kt=1) sample found as of now

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_2l2nu_hbbhvv_powheg",
    id=14932796,
    processes=[procs.ggHH_kl_2p45_kt_1_2l2nu_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=149854,
    aux={"allow_uppercase_name": True},
)
