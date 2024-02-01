# coding: utf-8

"""
HH -> bbWW datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

#
# ggf, HH -> bbVV inclusive
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_hbbhww_powheg",
    id=14863914,
    # processes=[procs.ggHH_kl_1_kt_1_hbbhww],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=229178,
)

#
# ggf, HH -> bbVV single lepton
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_sl_hbbhww_powheg",
    id=14868316,
    processes=[procs.ggHH_kl_1_kt_1_sl_hbbhww],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=89899,
)

#
# ggf, HH -> bbVV dilepton
#

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_dl_hbbhww_powheg",
    id=14847284,
    processes=[procs.ggHH_kl_1_kt_1_dl_hbbhww],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=86800,
)
