# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
HH -> bbWW datasets for the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# ggf, HH -> bbVV inclusive
#

# No SM (kl=1, kt=1) sample found as of now

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_hbbhvv_powheg",
    id=14940655,
    processes=[procs.ggHH_kl_2p45_kt_1_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=161,
    n_events=1191452,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV single lepton
#


# No SM (kl=1, kt=1) sample found as of now

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_qqlnu_hbbhvv_powheg",
    id=14940898,
    processes=[procs.ggHH_kl_2p45_kt_1_qqlnu_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=299199,
    aux={"allow_uppercase_name": True},
)


#
# ggf, HH -> bbVV dilepton
#

# No SM (kl=1, kt=1) sample found as of now

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_2l2nu_hbbhvv_powheg",
    id=14932681,
    processes=[procs.ggHH_kl_2p45_kt_1_2l2nu_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=299375,
    aux={"allow_uppercase_name": True},
)