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
    name="zprime_tt_m900_w9_madgraph",
    id=15537707,
    processes=[procs.zprime_tt_m900_w9],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-9_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w14_madgraph",
    id=15538618,
    processes=[procs.zprime_tt_m1400_w14],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-14_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w16_madgraph",
    id=15541112,
    processes=[procs.zprime_tt_m1600_w16],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-16_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w20_madgraph",
    id=15541592,
    processes=[procs.zprime_tt_m2000_w20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-20_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=1994000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w25_madgraph",
    id=15538151,
    processes=[procs.zprime_tt_m2500_w25],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-25_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=63,  # 63-0
            n_events=2000000,
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
    name="zprime_tt_m5000_w50_madgraph",
    id=15538245,
    processes=[procs.zprime_tt_m5000_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=2000000,
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
    name="zprime_tt_m500_w50_madgraph",
    id=15537300,
    processes=[procs.zprime_tt_m500_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w60_madgraph",
    id=15541038,
    processes=[procs.zprime_tt_m600_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-60_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w120_madgraph",
    id=15541182,
    processes=[procs.zprime_tt_m1200_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-120_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=1962000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w160_madgraph",
    id=15538163,
    processes=[procs.zprime_tt_m1600_w160],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-160_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w180_madgraph",
    id=15540988,
    processes=[procs.zprime_tt_m1800_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-180_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=1987000,
        ),
    ),
)

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
    name="zprime_tt_m2500_w250_madgraph",
    id=15538306,
    processes=[procs.zprime_tt_m2500_w250],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-250_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w500_madgraph",
    id=15541348,
    processes=[procs.zprime_tt_m5000_w500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=40,  # 40-0
            n_events=1999000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w600_madgraph",
    id=15538268,
    processes=[procs.zprime_tt_m6000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=1998000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w700_madgraph",
    id=15538396,
    processes=[procs.zprime_tt_m7000_w700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
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
    name="zprime_tt_m400_w120_madgraph",
    id=15541524,
    processes=[procs.zprime_tt_m400_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-120_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w240_madgraph",
    id=15538093,
    processes=[procs.zprime_tt_m800_w240],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-240_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=63,  # 63-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w270_madgraph",
    id=15537681,
    processes=[procs.zprime_tt_m900_w270],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-270_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=55,  # 55-0
            n_events=1990000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w300_madgraph",
    id=15541572,
    processes=[procs.zprime_tt_m1000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w600_madgraph",
    id=15542844,
    processes=[procs.zprime_tt_m2000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=53,  # 53-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w1050_madgraph",
    id=15541612,
    processes=[procs.zprime_tt_m3500_w1050],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-1050_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=2000000,
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
    name="zprime_tt_m6000_w1800_madgraph",
    id=15537302,
    processes=[procs.zprime_tt_m6000_w1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-1800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=2000000,
        ),
    ),
)
