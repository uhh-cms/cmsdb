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
    name="hh_ggf_kl1_kt1_hbb_hvv_powheg",
    id=14857512,
    processes=[procs.hh_ggf_kl1_kt1_hbb_hvv],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=769320,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV single lepton
#

cpn.add_dataset(
    name="hh_ggf_kl1_kt1_hbb_hvvqqlnu_powheg",
    id=14870918,
    processes=[procs.hh_ggf_kl1_kt1_hbb_hvvqqlnu],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=307250,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV dilepton
#

cpn.add_dataset(
    name="hh_ggf_kl1_kt1_hbb_hvv2l2nu_powheg",
    id=14857784,
    processes=[procs.hh_ggf_kl1_kt1_hbb_hvv2l2nu],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=302033,
    aux={"allow_uppercase_name": True},
)
