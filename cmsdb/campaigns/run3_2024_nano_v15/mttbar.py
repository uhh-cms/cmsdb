# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

# Z'->ttbar samples generated with MadGraph
cpn.add_dataset(
    name="zprime_tt_m1000_w100_madgraph",
    id=15542033,
    processes=[procs.zprime_tt_m1000_w100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=1999000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w10_madgraph",
    id=15538460,
    processes=[procs.zprime_tt_m1000_w10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-10_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=1999000,
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
    name="zprime_tt_m1200_w12_madgraph",
    id=15551207,
    processes=[procs.zprime_tt_m1200_w12],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-12_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=50,  # 50-0
            n_events=1991000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w360_madgraph",
    id=15541424,
    processes=[procs.zprime_tt_m1200_w360],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-360_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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
    name="zprime_tt_m1400_w140_madgraph",
    id=15548014,
    processes=[procs.zprime_tt_m1400_w140],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-140_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
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
    name="zprime_tt_m1400_w420_madgraph",
    id=15542876,
    processes=[procs.zprime_tt_m1400_w420],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-420_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=1963000,
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
    name="zprime_tt_m1600_w480_madgraph",
    id=15541147,
    processes=[procs.zprime_tt_m1600_w480],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-480_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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
    name="zprime_tt_m1800_w18_madgraph",
    id=15541497,
    processes=[procs.zprime_tt_m1800_w18],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-18_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=52,  # 52-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w540_madgraph",
    id=15538142,
    processes=[procs.zprime_tt_m1800_w540],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-540_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=52,  # 52-0
            n_events=2000000,
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
    name="zprime_tt_m2500_w750_madgraph",
    id=15538349,
    processes=[procs.zprime_tt_m2500_w750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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
    name="zprime_tt_m3000_w300_madgraph",
    id=15540497,
    processes=[procs.zprime_tt_m3000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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
    name="zprime_tt_m3000_w30_madgraph",
    id=15540510,
    processes=[procs.zprime_tt_m3000_w30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-30_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w900_madgraph",
    id=15546946,
    processes=[procs.zprime_tt_m3000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=1973000,
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
    name="zprime_tt_m3500_w350_madgraph",
    id=15541463,
    processes=[procs.zprime_tt_m3500_w350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=57,  # 57-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w35_madgraph",
    id=15538200,
    processes=[procs.zprime_tt_m3500_w35],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-35_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=2000000,
        ),
    ),
)

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
    name="zprime_tt_m400_w40_madgraph",
    id=15541553,
    processes=[procs.zprime_tt_m400_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-40_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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
    name="zprime_tt_m400_w4_madgraph",
    id=15541387,
    processes=[procs.zprime_tt_m400_w4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=52,  # 52-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w1200_madgraph",
    id=15551398,
    processes=[procs.zprime_tt_m4000_w1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=45,  # 45-0
            n_events=1992000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w400_madgraph",
    id=15541821,
    processes=[procs.zprime_tt_m4000_w400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=77,  # 77-0
            n_events=1910000,
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
    name="zprime_tt_m4500_w1350_madgraph",
    id=15550275,
    processes=[procs.zprime_tt_m4500_w1350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-1350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=57,  # 57-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w450_madgraph",
    id=15548885,
    processes=[procs.zprime_tt_m4500_w450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=1979000,
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
    name="zprime_tt_m500_w150_madgraph",
    id=15547805,
    processes=[procs.zprime_tt_m500_w150],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-150_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=2000000,
        ),
    ),
)

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
    id=15468893,
    processes=[procs.zprime_tt_m5000_w1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=1999000,
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
    name="zprime_tt_m600_w180_madgraph",
    id=15542829,
    processes=[procs.zprime_tt_m600_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-180_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
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
    name="zprime_tt_m600_w6_madgraph",
    id=15551178,
    processes=[procs.zprime_tt_m600_w6],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-6_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=50,  # 50-0
            n_events=1990000,
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
    name="zprime_tt_m6000_w60_madgraph",
    id=15544735,
    processes=[procs.zprime_tt_m6000_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-60_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w210_madgraph",
    id=15545126,
    processes=[procs.zprime_tt_m700_w210],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-210_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=55,  # 55-0
            n_events=1999000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w70_madgraph",
    id=15541173,
    processes=[procs.zprime_tt_m700_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-70_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=1999000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w7_madgraph",
    id=15542553,
    processes=[procs.zprime_tt_m700_w7],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-7_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=55,  # 55-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w2100_madgraph",
    id=15538155,
    processes=[procs.zprime_tt_m7000_w2100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-2100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=1997000,
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
    name="zprime_tt_m800_w80_madgraph",
    id=15550207,
    processes=[procs.zprime_tt_m800_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-80_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=50,  # 50-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w8_madgraph",
    id=15548009,
    processes=[procs.zprime_tt_m800_w8],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-8_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=1996000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w2400_madgraph",
    id=15541886,
    processes=[procs.zprime_tt_m8000_w2400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-2400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
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

cpn.add_dataset(
    name="zprime_tt_m8000_w80_madgraph",
    id=15538326,
    processes=[procs.zprime_tt_m8000_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-80_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
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
    name="zprime_tt_m900_w90_madgraph",
    id=15551026,
    processes=[procs.zprime_tt_m900_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-90_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=1999000,
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
    name="zprime_tt_m9000_w2700_madgraph",
    id=15547277,
    processes=[procs.zprime_tt_m9000_w2700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-2700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w900_madgraph",
    id=15547106,
    processes=[procs.zprime_tt_m9000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
            n_events=2000000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w90_madgraph",
    id=15539382,
    processes=[procs.zprime_tt_m9000_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-90_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=1988000,
        ),
    ),
)

