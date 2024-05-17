# coding: utf-8

"""
HH -> bbWW datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# ggf, HH -> bbVV inclusive
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_hbbhvv_powheg",
    id=14857512,
    processes=[procs.ggHH_kl_1_kt_1_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=769320,
)

#
# ggf, HH -> bbVV single lepton
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_sl_hbbhvv_powheg",
    id=14870918,
    processes=[procs.ggHH_kl_1_kt_1_sl_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=307250,
)

#
# ggf, HH -> bbVV dilepton
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_dl_hbbhvv_powheg",
    id=14857784,
    processes=[procs.ggHH_kl_1_kt_1_dl_hbbhvv],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=302033,
)
