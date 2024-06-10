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
    name="hh_ggf_kl_1_kt_1_hbb_hvv_powheg",
    id=14863914,
    processes=[procs.hh_ggf_kl_1_kt_1_hbb_hvv],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=229178,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV single lepton
#

cpn.add_dataset(
    name="hh_ggf_kl_1_kt_1_hbb_hvvqqlnu_powheg",
    id=14868316,
    processes=[procs.hh_ggf_kl_1_kt_1_hbb_hvvqqlnu],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=89899,
    aux={"allow_uppercase_name": True},
)

#
# ggf, HH -> bbVV dilepton
#

cpn.add_dataset(
    name="hh_ggf_kl_1_kt_1_hbb_hvv2l2nu_powheg",
    id=14847284,
    processes=[procs.hh_ggf_kl_1_kt_1_hbb_hvv2l2nu],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=86800,
    aux={"allow_uppercase_name": True},
)
