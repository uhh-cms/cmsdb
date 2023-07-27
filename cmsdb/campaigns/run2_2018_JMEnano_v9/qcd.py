# coding: utf-8

"""
QCD datasets for the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_JMEnano_v9 import campaign_run2_2018_JMEnano_v9 as cpn


#
# QCD HT-binned
#

# HT-binned samples

cpn.add_dataset(
    name="qcd_ht50to100_madgraph",
    id=14296686,
    processes=[procs.qcd_ht50to100],
    keys=[
        "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=99,
    n_events=38485273,
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14286202,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=175,
    n_events=83416014,
)

cpn.add_dataset(
    name="qcd_ht200to300_madgraph",
    id=14288453,
    processes=[procs.qcd_ht200to300],
    keys=[
        "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=104,
    n_events=57336623,
)

cpn.add_dataset(
    name="qcd_ht300to500_madgraph",
    id=14296771,
    processes=[procs.qcd_ht300to500],
    keys=[
        "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=235,
    n_events=61491618,
)

cpn.add_dataset(
    name="qcd_ht500to700_madgraph",
    id=14293400,
    processes=[procs.qcd_ht500to700],
    keys=[
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=106,
    n_events=49070152,
)

cpn.add_dataset(
    name="qcd_ht700to1000_madgraph",
    id=14275579,
    processes=[procs.qcd_ht700to1000],
    keys=[
        "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=99,
    n_events=48220920,
)

cpn.add_dataset(
    name="qcd_ht1000to1500_madgraph",
    id=14296761,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=14127722,
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14300066,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=10583770,
)

cpn.add_dataset(
    name="qcd_ht2000_madgraph",
    id=14299583,
    processes=[procs.qcd_ht2000],
    keys=[
        "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=5202244,
)
