# coding: utf-8

"""
A->ZH->Ztt datasets for the 2024 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

from order import DatasetInfo

#
# A->ZH->lltt
#

cpn.add_dataset(
    name="azh_htt_zll_a1000_h330_madgraph",
    id=15555060,
    processes=[procs.azh_htt_zll_a1000_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h350_madgraph",
    id=15543788,
    processes=[procs.azh_htt_zll_a1000_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h400_madgraph",
    id=15554961,
    processes=[procs.azh_htt_zll_a1000_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h450_madgraph",
    id=15541930,
    processes=[procs.azh_htt_zll_a1000_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h500_madgraph",
    id=15550981,
    processes=[procs.azh_htt_zll_a1000_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h550_madgraph",
    id=15551078,
    processes=[procs.azh_htt_zll_a1000_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h600_madgraph",
    id=15554793,
    processes=[procs.azh_htt_zll_a1000_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=144000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h650_madgraph",
    id=15542555,
    processes=[procs.azh_htt_zll_a1000_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h700_madgraph",
    id=15555115,
    processes=[procs.azh_htt_zll_a1000_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=146000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h750_madgraph",
    id=15555172,
    processes=[procs.azh_htt_zll_a1000_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h800_madgraph",
    id=15542330,
    processes=[procs.azh_htt_zll_a1000_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h850_madgraph",
    id=15550214,
    processes=[procs.azh_htt_zll_a1000_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h900_madgraph",
    id=15547367,
    processes=[procs.azh_htt_zll_a1000_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1000-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h350_madgraph",
    id=15546279,
    processes=[procs.azh_htt_zll_a1600_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h400_madgraph",
    id=15545259,
    processes=[procs.azh_htt_zll_a1600_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h500_madgraph",
    id=15554986,
    processes=[procs.azh_htt_zll_a1600_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h600_madgraph",
    id=15549867,
    processes=[procs.azh_htt_zll_a1600_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h900_madgraph",
    id=15550039,
    processes=[procs.azh_htt_zll_a1600_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1000_madgraph",
    id=15548590,
    processes=[procs.azh_htt_zll_a1600_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1100_madgraph",
    id=15547076,
    processes=[procs.azh_htt_zll_a1600_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1200_madgraph",
    id=15553154,
    processes=[procs.azh_htt_zll_a1600_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1300_madgraph",
    id=15548689,
    processes=[procs.azh_htt_zll_a1600_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1400_madgraph",
    id=15554973,
    processes=[procs.azh_htt_zll_a1600_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1500_madgraph",
    id=15547908,
    processes=[procs.azh_htt_zll_a1600_h1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1600-MH-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a430_h330_madgraph",
    id=15556764,
    processes=[procs.azh_htt_zll_a430_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-430-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h350_madgraph",
    id=15546489,
    processes=[procs.azh_htt_zll_a2100_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h400_madgraph",
    id=15542934,
    processes=[procs.azh_htt_zll_a2100_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h500_madgraph",
    id=15559225,
    processes=[procs.azh_htt_zll_a2100_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,  # 26-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h600_madgraph",
    id=15549792,
    processes=[procs.azh_htt_zll_a2100_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h700_madgraph",
    id=15561643,
    processes=[procs.azh_htt_zll_a2100_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h800_madgraph",
    id=15541981,
    processes=[procs.azh_htt_zll_a2100_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h900_madgraph",
    id=15546540,
    processes=[procs.azh_htt_zll_a2100_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1000_madgraph",
    id=15549501,
    processes=[procs.azh_htt_zll_a2100_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1100_madgraph",
    id=15552667,
    processes=[procs.azh_htt_zll_a2100_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1200_madgraph",
    id=15548711,
    processes=[procs.azh_htt_zll_a2100_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1300_madgraph",
    id=15557093,
    processes=[procs.azh_htt_zll_a2100_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1400_madgraph",
    id=15552604,
    processes=[procs.azh_htt_zll_a2100_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1500_madgraph",
    id=15549477,
    processes=[procs.azh_htt_zll_a2100_h1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1700_madgraph",
    id=15546574,
    processes=[procs.azh_htt_zll_a2100_h1700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1800_madgraph",
    id=15544333,
    processes=[procs.azh_htt_zll_a2100_h1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=4,  # 4-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1900_madgraph",
    id=15547224,
    processes=[procs.azh_htt_zll_a2100_h1900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-1900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h2000_madgraph",
    id=15556417,
    processes=[procs.azh_htt_zll_a2100_h2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2100-MH-2000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h330_madgraph",
    id=15546858,
    processes=[procs.azh_htt_zll_a500_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-500-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h350_madgraph",
    id=15549696,
    processes=[procs.azh_htt_zll_a500_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-500-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h400_madgraph",
    id=15545346,
    processes=[procs.azh_htt_zll_a500_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-500-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h330_madgraph",
    id=15557745,
    processes=[procs.azh_htt_zll_a1050_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h350_madgraph",
    id=15547422,
    processes=[procs.azh_htt_zll_a1050_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h400_madgraph",
    id=15551925,
    processes=[procs.azh_htt_zll_a1050_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h450_madgraph",
    id=15543982,
    processes=[procs.azh_htt_zll_a1050_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h500_madgraph",
    id=15542250,
    processes=[procs.azh_htt_zll_a1050_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h550_madgraph",
    id=15547709,
    processes=[procs.azh_htt_zll_a1050_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=147000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h600_madgraph",
    id=15541949,
    processes=[procs.azh_htt_zll_a1050_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h700_madgraph",
    id=15547642,
    processes=[procs.azh_htt_zll_a1050_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=147000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h750_madgraph",
    id=15543200,
    processes=[procs.azh_htt_zll_a1050_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h800_madgraph",
    id=15540834,
    processes=[procs.azh_htt_zll_a1050_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h850_madgraph",
    id=15544756,
    processes=[procs.azh_htt_zll_a1050_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h900_madgraph",
    id=15558728,
    processes=[procs.azh_htt_zll_a1050_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h950_madgraph",
    id=15547481,
    processes=[procs.azh_htt_zll_a1050_h950],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1050-MH-950_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h330_madgraph",
    id=15547955,
    processes=[procs.azh_htt_zll_a1100_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h350_madgraph",
    id=15547787,
    processes=[procs.azh_htt_zll_a1100_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h400_madgraph",
    id=15545354,
    processes=[procs.azh_htt_zll_a1100_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h450_madgraph",
    id=15558920,
    processes=[procs.azh_htt_zll_a1100_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h500_madgraph",
    id=15550259,
    processes=[procs.azh_htt_zll_a1100_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h550_madgraph",
    id=15541863,
    processes=[procs.azh_htt_zll_a1100_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h600_madgraph",
    id=15553611,
    processes=[procs.azh_htt_zll_a1100_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=145000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h650_madgraph",
    id=15541991,
    processes=[procs.azh_htt_zll_a1100_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h700_madgraph",
    id=15559844,
    processes=[procs.azh_htt_zll_a1100_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h750_madgraph",
    id=15541836,
    processes=[procs.azh_htt_zll_a1100_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h800_madgraph",
    id=15557250,
    processes=[procs.azh_htt_zll_a1100_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h850_madgraph",
    id=15542365,
    processes=[procs.azh_htt_zll_a1100_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h900_madgraph",
    id=15554573,
    processes=[procs.azh_htt_zll_a1100_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h950_madgraph",
    id=15554893,
    processes=[procs.azh_htt_zll_a1100_h950],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-950_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h1000_madgraph",
    id=15548969,
    processes=[procs.azh_htt_zll_a1100_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1100-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h330_madgraph",
    id=15547248,
    processes=[procs.azh_htt_zll_a1150_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h350_madgraph",
    id=15554938,
    processes=[procs.azh_htt_zll_a1150_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h450_madgraph",
    id=15547138,
    processes=[procs.azh_htt_zll_a1150_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h550_madgraph",
    id=15543007,
    processes=[procs.azh_htt_zll_a1150_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h650_madgraph",
    id=15555105,
    processes=[procs.azh_htt_zll_a1150_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=148000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h750_madgraph",
    id=15540787,
    processes=[procs.azh_htt_zll_a1150_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h850_madgraph",
    id=15555364,
    processes=[procs.azh_htt_zll_a1150_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h950_madgraph",
    id=15557220,
    processes=[procs.azh_htt_zll_a1150_h950],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-950_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h1050_madgraph",
    id=15548946,
    processes=[procs.azh_htt_zll_a1150_h1050],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1150-MH-1050_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h330_madgraph",
    id=15542977,
    processes=[procs.azh_htt_zll_a1200_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h350_madgraph",
    id=15557458,
    processes=[procs.azh_htt_zll_a1200_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h400_madgraph",
    id=15550730,
    processes=[procs.azh_htt_zll_a1200_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h500_madgraph",
    id=15541729,
    processes=[procs.azh_htt_zll_a1200_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h600_madgraph",
    id=15548911,
    processes=[procs.azh_htt_zll_a1200_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h700_madgraph",
    id=15555963,
    processes=[procs.azh_htt_zll_a1200_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=148000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h800_madgraph",
    id=15544998,
    processes=[procs.azh_htt_zll_a1200_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h850_madgraph",
    id=15554984,
    processes=[procs.azh_htt_zll_a1200_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h900_madgraph",
    id=15546221,
    processes=[procs.azh_htt_zll_a1200_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1000_madgraph",
    id=15557045,
    processes=[procs.azh_htt_zll_a1200_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1100_madgraph",
    id=15544904,
    processes=[procs.azh_htt_zll_a1200_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1200-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h350_madgraph",
    id=15553319,
    processes=[procs.azh_htt_zll_a1300_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h400_madgraph",
    id=15544656,
    processes=[procs.azh_htt_zll_a1300_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h500_madgraph",
    id=15549470,
    processes=[procs.azh_htt_zll_a1300_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h600_madgraph",
    id=15541733,
    processes=[procs.azh_htt_zll_a1300_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h700_madgraph",
    id=15548933,
    processes=[procs.azh_htt_zll_a1300_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h800_madgraph",
    id=15541858,
    processes=[procs.azh_htt_zll_a1300_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h900_madgraph",
    id=15556813,
    processes=[procs.azh_htt_zll_a1300_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1000_madgraph",
    id=15555039,
    processes=[procs.azh_htt_zll_a1300_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1100_madgraph",
    id=15550790,
    processes=[procs.azh_htt_zll_a1300_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1200_madgraph",
    id=15556770,
    processes=[procs.azh_htt_zll_a1300_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1300-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h350_madgraph",
    id=15561908,
    processes=[procs.azh_htt_zll_a1400_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h400_madgraph",
    id=15549531,
    processes=[procs.azh_htt_zll_a1400_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h500_madgraph",
    id=15545355,
    processes=[procs.azh_htt_zll_a1400_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h600_madgraph",
    id=15543219,
    processes=[procs.azh_htt_zll_a1400_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h700_madgraph",
    id=15555061,
    processes=[procs.azh_htt_zll_a1400_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h800_madgraph",
    id=15542650,
    processes=[procs.azh_htt_zll_a1400_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h900_madgraph",
    id=15546407,
    processes=[procs.azh_htt_zll_a1400_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1000_madgraph",
    id=15546820,
    processes=[procs.azh_htt_zll_a1400_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1100_madgraph",
    id=15559362,
    processes=[procs.azh_htt_zll_a1400_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1300_madgraph",
    id=15556843,
    processes=[procs.azh_htt_zll_a1400_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1400-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h350_madgraph",
    id=15548998,
    processes=[procs.azh_htt_zll_a1500_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h400_madgraph",
    id=15549305,
    processes=[procs.azh_htt_zll_a1500_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h500_madgraph",
    id=15557321,
    processes=[procs.azh_htt_zll_a1500_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h600_madgraph",
    id=15556496,
    processes=[procs.azh_htt_zll_a1500_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h700_madgraph",
    id=15547064,
    processes=[procs.azh_htt_zll_a1500_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h900_madgraph",
    id=15542166,
    processes=[procs.azh_htt_zll_a1500_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1000_madgraph",
    id=15554942,
    processes=[procs.azh_htt_zll_a1500_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=148000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1100_madgraph",
    id=15555000,
    processes=[procs.azh_htt_zll_a1500_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1200_madgraph",
    id=15546467,
    processes=[procs.azh_htt_zll_a1500_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1300_madgraph",
    id=15556261,
    processes=[procs.azh_htt_zll_a1500_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=148000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1400_madgraph",
    id=15546717,
    processes=[procs.azh_htt_zll_a1500_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1500-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h350_madgraph",
    id=15546403,
    processes=[procs.azh_htt_zll_a1700_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h400_madgraph",
    id=15548829,
    processes=[procs.azh_htt_zll_a1700_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h500_madgraph",
    id=15555149,
    processes=[procs.azh_htt_zll_a1700_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h600_madgraph",
    id=15545408,
    processes=[procs.azh_htt_zll_a1700_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h700_madgraph",
    id=15556792,
    processes=[procs.azh_htt_zll_a1700_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h800_madgraph",
    id=15549897,
    processes=[procs.azh_htt_zll_a1700_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1000_madgraph",
    id=15549787,
    processes=[procs.azh_htt_zll_a1700_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1100_madgraph",
    id=15542627,
    processes=[procs.azh_htt_zll_a1700_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1200_madgraph",
    id=15483771,
    processes=[procs.azh_htt_zll_a1700_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1300_madgraph",
    id=15555033,
    processes=[procs.azh_htt_zll_a1700_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1400_madgraph",
    id=15544659,
    processes=[procs.azh_htt_zll_a1700_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1500_madgraph",
    id=15544454,
    processes=[procs.azh_htt_zll_a1700_h1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1600_madgraph",
    id=15556743,
    processes=[procs.azh_htt_zll_a1700_h1600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1700-MH-1600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h350_madgraph",
    id=15562188,
    processes=[procs.azh_htt_zll_a1800_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h400_madgraph",
    id=15557703,
    processes=[procs.azh_htt_zll_a1800_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h500_madgraph",
    id=15541901,
    processes=[procs.azh_htt_zll_a1800_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h600_madgraph",
    id=15544749,
    processes=[procs.azh_htt_zll_a1800_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h700_madgraph",
    id=15555215,
    processes=[procs.azh_htt_zll_a1800_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h800_madgraph",
    id=15554912,
    processes=[procs.azh_htt_zll_a1800_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h900_madgraph",
    id=15546555,
    processes=[procs.azh_htt_zll_a1800_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1000_madgraph",
    id=15549002,
    processes=[procs.azh_htt_zll_a1800_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1100_madgraph",
    id=15549009,
    processes=[procs.azh_htt_zll_a1800_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1200_madgraph",
    id=15565367,
    processes=[procs.azh_htt_zll_a1800_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1300_madgraph",
    id=15545908,
    processes=[procs.azh_htt_zll_a1800_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1400_madgraph",
    id=15540730,
    processes=[procs.azh_htt_zll_a1800_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1500_madgraph",
    id=15547253,
    processes=[procs.azh_htt_zll_a1800_h1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1600_madgraph",
    id=15542186,
    processes=[procs.azh_htt_zll_a1800_h1600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1700_madgraph",
    id=15547267,
    processes=[procs.azh_htt_zll_a1800_h1700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1800-MH-1700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h350_madgraph",
    id=15555410,
    processes=[procs.azh_htt_zll_a1900_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h400_madgraph",
    id=15559212,
    processes=[procs.azh_htt_zll_a1900_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h500_madgraph",
    id=15548643,
    processes=[procs.azh_htt_zll_a1900_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h600_madgraph",
    id=15549770,
    processes=[procs.azh_htt_zll_a1900_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h700_madgraph",
    id=15556957,
    processes=[procs.azh_htt_zll_a1900_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h800_madgraph",
    id=15541892,
    processes=[procs.azh_htt_zll_a1900_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h900_madgraph",
    id=15546850,
    processes=[procs.azh_htt_zll_a1900_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1000_madgraph",
    id=15547054,
    processes=[procs.azh_htt_zll_a1900_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1100_madgraph",
    id=15555226,
    processes=[procs.azh_htt_zll_a1900_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1200_madgraph",
    id=15547047,
    processes=[procs.azh_htt_zll_a1900_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1300_madgraph",
    id=15565360,
    processes=[procs.azh_htt_zll_a1900_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1400_madgraph",
    id=15550921,
    processes=[procs.azh_htt_zll_a1900_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1500_madgraph",
    id=15541735,
    processes=[procs.azh_htt_zll_a1900_h1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1600_madgraph",
    id=15547252,
    processes=[procs.azh_htt_zll_a1900_h1600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1700_madgraph",
    id=15544883,
    processes=[procs.azh_htt_zll_a1900_h1700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1800_madgraph",
    id=15541879,
    processes=[procs.azh_htt_zll_a1900_h1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-1900-MH-1800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h350_madgraph",
    id=15551147,
    processes=[procs.azh_htt_zll_a2000_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h400_madgraph",
    id=15548356,
    processes=[procs.azh_htt_zll_a2000_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h500_madgraph",
    id=15546905,
    processes=[procs.azh_htt_zll_a2000_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h600_madgraph",
    id=15554881,
    processes=[procs.azh_htt_zll_a2000_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h700_madgraph",
    id=15555053,
    processes=[procs.azh_htt_zll_a2000_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h800_madgraph",
    id=15557754,
    processes=[procs.azh_htt_zll_a2000_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h900_madgraph",
    id=15543172,
    processes=[procs.azh_htt_zll_a2000_h900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1000_madgraph",
    id=15542410,
    processes=[procs.azh_htt_zll_a2000_h1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1000_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1100_madgraph",
    id=15548607,
    processes=[procs.azh_htt_zll_a2000_h1100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1100_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1200_madgraph",
    id=15555050,
    processes=[procs.azh_htt_zll_a2000_h1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1200_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1300_madgraph",
    id=15550729,
    processes=[procs.azh_htt_zll_a2000_h1300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1300_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1400_madgraph",
    id=15547079,
    processes=[procs.azh_htt_zll_a2000_h1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1600_madgraph",
    id=15541779,
    processes=[procs.azh_htt_zll_a2000_h1600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1700_madgraph",
    id=15555071,
    processes=[procs.azh_htt_zll_a2000_h1700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1800_madgraph",
    id=15544810,
    processes=[procs.azh_htt_zll_a2000_h1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1900_madgraph",
    id=15549012,
    processes=[procs.azh_htt_zll_a2000_h1900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-2000-MH-1900_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h330_madgraph",
    id=15546350,
    processes=[procs.azh_htt_zll_a450_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-450-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h350_madgraph",
    id=15542319,
    processes=[procs.azh_htt_zll_a450_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-450-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h330_madgraph",
    id=15543981,
    processes=[procs.azh_htt_zll_a550_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-550-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h350_madgraph",
    id=15543429,
    processes=[procs.azh_htt_zll_a550_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-550-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h400_madgraph",
    id=15542894,
    processes=[procs.azh_htt_zll_a550_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-550-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h450_madgraph",
    id=15545206,
    processes=[procs.azh_htt_zll_a550_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-550-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h330_madgraph",
    id=15548944,
    processes=[procs.azh_htt_zll_a600_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-600-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h350_madgraph",
    id=15547992,
    processes=[procs.azh_htt_zll_a600_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-600-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h400_madgraph",
    id=15542023,
    processes=[procs.azh_htt_zll_a600_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-600-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h450_madgraph",
    id=15544193,
    processes=[procs.azh_htt_zll_a600_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-600-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h500_madgraph",
    id=15508113,
    processes=[procs.azh_htt_zll_a600_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-600-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h330_madgraph",
    id=15541924,
    processes=[procs.azh_htt_zll_a650_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h350_madgraph",
    id=15542102,
    processes=[procs.azh_htt_zll_a650_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h400_madgraph",
    id=15544275,
    processes=[procs.azh_htt_zll_a650_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h450_madgraph",
    id=15548402,
    processes=[procs.azh_htt_zll_a650_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h500_madgraph",
    id=15550519,
    processes=[procs.azh_htt_zll_a650_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h550_madgraph",
    id=15541861,
    processes=[procs.azh_htt_zll_a650_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-650-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h330_madgraph",
    id=15548042,
    processes=[procs.azh_htt_zll_a700_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h350_madgraph",
    id=15547205,
    processes=[procs.azh_htt_zll_a700_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h400_madgraph",
    id=15555144,
    processes=[procs.azh_htt_zll_a700_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h450_madgraph",
    id=15555073,
    processes=[procs.azh_htt_zll_a700_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h500_madgraph",
    id=15554944,
    processes=[procs.azh_htt_zll_a700_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h550_madgraph",
    id=15549928,
    processes=[procs.azh_htt_zll_a700_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-700-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h330_madgraph",
    id=15546037,
    processes=[procs.azh_htt_zll_a750_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h350_madgraph",
    id=15543482,
    processes=[procs.azh_htt_zll_a750_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h400_madgraph",
    id=15543234,
    processes=[procs.azh_htt_zll_a750_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h450_madgraph",
    id=15540539,
    processes=[procs.azh_htt_zll_a750_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h500_madgraph",
    id=15541950,
    processes=[procs.azh_htt_zll_a750_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h550_madgraph",
    id=15541877,
    processes=[procs.azh_htt_zll_a750_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h600_madgraph",
    id=15548621,
    processes=[procs.azh_htt_zll_a750_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h650_madgraph",
    id=15544414,
    processes=[procs.azh_htt_zll_a750_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-750-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h330_madgraph",
    id=15549031,
    processes=[procs.azh_htt_zll_a800_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h350_madgraph",
    id=15545245,
    processes=[procs.azh_htt_zll_a800_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h400_madgraph",
    id=15553087,
    processes=[procs.azh_htt_zll_a800_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h450_madgraph",
    id=15556744,
    processes=[procs.azh_htt_zll_a800_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=147000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h500_madgraph",
    id=15546546,
    processes=[procs.azh_htt_zll_a800_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h550_madgraph",
    id=15547085,
    processes=[procs.azh_htt_zll_a800_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h600_madgraph",
    id=15550713,
    processes=[procs.azh_htt_zll_a800_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h650_madgraph",
    id=15541715,
    processes=[procs.azh_htt_zll_a800_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h700_madgraph",
    id=15556001,
    processes=[procs.azh_htt_zll_a800_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-800-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h330_madgraph",
    id=15546538,
    processes=[procs.azh_htt_zll_a850_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h350_madgraph",
    id=15546380,
    processes=[procs.azh_htt_zll_a850_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h400_madgraph",
    id=15544710,
    processes=[procs.azh_htt_zll_a850_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h450_madgraph",
    id=15542770,
    processes=[procs.azh_htt_zll_a850_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h500_madgraph",
    id=15555202,
    processes=[procs.azh_htt_zll_a850_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h550_madgraph",
    id=15554906,
    processes=[procs.azh_htt_zll_a850_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h600_madgraph",
    id=15549888,
    processes=[procs.azh_htt_zll_a850_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h650_madgraph",
    id=15548576,
    processes=[procs.azh_htt_zll_a850_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h700_madgraph",
    id=15563889,
    processes=[procs.azh_htt_zll_a850_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h750_madgraph",
    id=15540531,
    processes=[procs.azh_htt_zll_a850_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-850-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h330_madgraph",
    id=15555126,
    processes=[procs.azh_htt_zll_a900_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=146000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h350_madgraph",
    id=15545499,
    processes=[procs.azh_htt_zll_a900_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h400_madgraph",
    id=15543608,
    processes=[procs.azh_htt_zll_a900_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h450_madgraph",
    id=15556839,
    processes=[procs.azh_htt_zll_a900_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=149000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h500_madgraph",
    id=15547646,
    processes=[procs.azh_htt_zll_a900_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h550_madgraph",
    id=15543079,
    processes=[procs.azh_htt_zll_a900_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h600_madgraph",
    id=15559239,
    processes=[procs.azh_htt_zll_a900_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h650_madgraph",
    id=15546823,
    processes=[procs.azh_htt_zll_a900_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h700_madgraph",
    id=15543064,
    processes=[procs.azh_htt_zll_a900_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h750_madgraph",
    id=15548962,
    processes=[procs.azh_htt_zll_a900_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h800_madgraph",
    id=15554914,
    processes=[procs.azh_htt_zll_a900_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-900-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h330_madgraph",
    id=15555962,
    processes=[procs.azh_htt_zll_a950_h330],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-330_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=148000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h350_madgraph",
    id=15543601,
    processes=[procs.azh_htt_zll_a950_h350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-350_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h400_madgraph",
    id=15554681,
    processes=[procs.azh_htt_zll_a950_h400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-400_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h450_madgraph",
    id=15545067,
    processes=[procs.azh_htt_zll_a950_h450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-450_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h500_madgraph",
    id=15543203,
    processes=[procs.azh_htt_zll_a950_h500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-500_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h550_madgraph",
    id=15541629,
    processes=[procs.azh_htt_zll_a950_h550],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-550_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h600_madgraph",
    id=15546511,
    processes=[procs.azh_htt_zll_a950_h600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-600_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h650_madgraph",
    id=15552575,
    processes=[procs.azh_htt_zll_a950_h650],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-650_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h700_madgraph",
    id=15548949,
    processes=[procs.azh_htt_zll_a950_h700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-700_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h750_madgraph",
    id=15550685,
    processes=[procs.azh_htt_zll_a950_h750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-750_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h800_madgraph",
    id=15543610,
    processes=[procs.azh_htt_zll_a950_h800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-800_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=150000,
        ),
    ),
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h850_madgraph",
    id=15547509,
    processes=[procs.azh_htt_zll_a950_h850],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/AToZHToLLTTbar_Par-MA-950-MH-850_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=149000,
        ),
    ),
)
