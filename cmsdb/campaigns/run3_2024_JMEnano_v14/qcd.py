# coding: utf-8

""""
QCD datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_JMEnano_v14 import campaign_run3_2024_JMEnano_v14 as cpn


#
# QCD (Madgraph, HT-binned)
#

cpn.add_dataset(
    name="qcd_ht40to70_madgraph",
    id=14966052,
    processes=[procs.qcd_ht40to70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,
            n_events=19198295,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht70to100_madgraph",
    id=15015788,
    processes=[procs.qcd_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,
            n_events=20146328,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=15022979,
    processes=[procs.qcd_ht100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=30,
            n_events=19458869,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht200to400_madgraph",
    id=14966254,
    processes=[procs.qcd_ht200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,
            n_events=18478637,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht400to600_madgraph",
    id=15018185,
    processes=[procs.qcd_ht400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,
            n_events=19101232,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht600to800_madgraph",
    id=14966063,
    processes=[procs.qcd_ht600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=46,
            n_events=19122441,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht800to1000_madgraph",
    id=15015758,
    processes=[procs.qcd_ht800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,
            n_events=18550980,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1000to1200_madgraph",
    id=15015772,
    processes=[procs.qcd_ht1000to1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=43,
            n_events=20564271,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1200to1500_madgraph",
    id=14968928,
    processes=[procs.qcd_ht1200to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=53,
            n_events=19537640,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=15043776,
    processes=[procs.qcd_ht1500to2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,
            n_events=17527147,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=15015724,
    processes=[procs.qcd_ht2000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter24NanoAOD-JMENanoV14_133X_mcRun3_2024_realistic_v10-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=42,
            n_events=19336092,
        ),
    ),
)
