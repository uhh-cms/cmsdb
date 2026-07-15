# coding: utf-8

""""
QCD datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_JMEnano_v15 import campaign_run3_2024_JMEnano_v15 as cpn


#
# QCD (Madgraph, HT-binned)
#

cpn.add_dataset(
    name="qcd_ht40to70_madgraph",
    id=15334405,
    processes=[procs.qcd_ht40to70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=187,  # 187-0
            n_events=110777315,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht70to100_madgraph",
    id=15333764,
    processes=[procs.qcd_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=194,  # 194-0
            n_events=108584880,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=15334472,
    processes=[procs.qcd_ht100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=270,  # 270-0
            n_events=120388125,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht200to400_madgraph",
    id=15333552,
    processes=[procs.qcd_ht200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=238,  # 238-0
            n_events=115255250,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht400to600_madgraph",
    id=15333375,
    processes=[procs.qcd_ht400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=232,  # 232-0
            n_events=106725734,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht600to800_madgraph",
    id=15333649,
    processes=[procs.qcd_ht600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=268,  # 268-0
            n_events=128192794,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht800to1000_madgraph",
    id=15333640,
    processes=[procs.qcd_ht800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=351,  # 351-0
            n_events=125650480,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1000to1200_madgraph",
    id=15333677,
    processes=[procs.qcd_ht1000to1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=296,  # 296-0
            n_events=114412542,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1200to1500_madgraph",
    id=15331289,
    processes=[procs.qcd_ht1200to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=285,  # 285-0
            n_events=107835822,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=15333271,
    processes=[procs.qcd_ht1500to2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=294,  # 294-0
            n_events=113208234,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=15333146,
    processes=[procs.qcd_ht2000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-JMENanoV15_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=306,  # 306-0
            n_events=91407008,
        ),
    ),
)
