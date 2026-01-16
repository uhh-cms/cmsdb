# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

# Z'->ttbar samples generated with MadGraph

# 1% width samples
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
    name="zprime_tt_m4000_w40_madgraph",
    id=15460714,
    processes=[procs.zprime_tt_m4000_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-40_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=32,  # 32-0
            n_events=1985000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w45_madgraph",
    id=15459031,
    processes=[procs.zprime_tt_m4500_w45],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-45_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,  # 33-0
            n_events=1999000,
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

# 10% width samples
cpn.add_dataset(
    name="zprime_tt_m2000_w200_madgraph",
    id=15510487,
    processes=[procs.zprime_tt_m2000_w200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w800_madgraph",
    id=15497172,
    processes=[procs.zprime_tt_m8000_w800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=32,  # 32-0
            n_events=2000000,
        ),
    ),
)

# 30% width samples
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
