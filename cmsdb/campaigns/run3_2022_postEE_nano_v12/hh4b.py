# coding: utf-8

"""
HH -> 4b datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# ttHH -> 4b
#

cpn.add_dataset(
    name="tthh_4b_madgraph",
    id=15292837,
    processes=[procs.tthh_4b],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHHto4B_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=41,  # 41-0
            n_events=3492168,
        ),
    ),
)


#
# VHH -> 4b
#

cpn.add_dataset(
    name="whh_4b_k2v1p0kl0p0kv1p0_madgraph",
    id=15382278,
    processes=[procs.whh_4b_k2v1p0kl0p0kv1p0],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WHH_HHto4B_CV_1_0_C2V_1_0_C3_0_0_13p6TeV_TuneCP5_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=3064698,
        ),
    ),
)

cpn.add_dataset(
    name="zhh_4b_k2v1p0kl0p0kv1p0_madgraph",
    id=15325097,
    processes=[procs.zhh_4b_k2v1p0kl0p0kv1p0],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHH_HHto4B_CV_1_0_C2V_1_0_C3_0_0_13p6TeV_TuneCP5_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,  # 26-0
            n_events=2824392,
        ),
    ),
)
