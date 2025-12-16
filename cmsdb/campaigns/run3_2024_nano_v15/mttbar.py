# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

cpn.add_dataset(
    name="zprime_tt_m500_w5_madgraph",
    id=15441783,
    processes=[procs.zprime_tt_m500_w5],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-5_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=1996000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w1500_madgraph",
    id=15451351,
    processes=[procs.zprime_tt_m5000_w1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=32,  # 32-0
            n_events=1998000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w70_madgraph",
    id=15431947,
    processes=[procs.zprime_tt_m7000_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-70_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=30,  # 30-0
            n_events=1992000,
        ),
    ),
)
