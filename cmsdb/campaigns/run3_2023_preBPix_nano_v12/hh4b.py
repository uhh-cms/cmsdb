# coding: utf-8

"""
HH -> 4b datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


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
                "/TTHHto4B_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=1973000,
        ),
    ),
)


#
# VHH -> 4b
#

# cpn.add_dataset(
#     name="whh_4b_k2v1p0kl0p0kv1p0_madgraph",
#     id=15382278,
#     processes=[procs.whh_4b_k2v1p0kl0p0kv1p0],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WHH-HHto4B_Par-C2V-1p0-C3-0p0-CV-1p0_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=7,  # 7-0
#             n_events=497807,
#         ),
#     ),
# )

# cpn.add_dataset(
#     name="zhh_4b_k2v1p0kl0p0kv1p0_madgraph",
#     id=15325097,
#     processes=[procs.zhh_4b_k2v1p0kl0p0kv1p0],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/ZHH-HHto4B_Par-C2V-1p0-C3-0p0-CV-1p0_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=8,  # 8-0
#             n_events=491937,
#         ),
#     ),
# )
