# coding: utf-8

"""
HH -> bbVV datasets for the 2022 post-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v13 import campaign_run3_2022_postEE_nano_v13 as cpn


#
# ggf, HH -> bbVV
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=15023164,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=300095,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=15005111,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=779997,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=15005726,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=777917,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=15008540,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=309321,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=15023099,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=305116,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=15006081,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv13-133X_mcRun3_2022_realistic_postEE_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=298369,
        ),
    ),
)

#
# vbf, HH -> bbVV
#

# nothing yet.
