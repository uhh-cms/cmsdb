# coding: utf-8

"""
QCD datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_JMEnano_v9 import campaign_run2_2017_JMEnano_v9 as cpn


#
# QCD HT-binned
#

# HT-binned samples

can.add_dataset(
    name='qcd_ht50to100_madgraph',
    id=14281497,
    processes=procs.qcd_ht50to100,
    keys=[
        '/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=52,
    n_events=26129826
)

can.add_dataset(
    name='qcd_ht100to200_madgraph',
    id=14300506,
    processes=procs.qcd_ht100to200,
    keys=[
        '/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=99,
    n_events=54705747
)

can.add_dataset(
    name='qcd_ht200to300_madgraph',
    id=14289012,
    processes=procs.qcd_ht200to300,
    keys=[
        '/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=85,
    n_events=42679193
)

can.add_dataset(
    name='qcd_ht300to500_madgraph',
    id=14288347,
    processes=procs.qcd_ht300to500,
    keys=[
        '/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=94,
    n_events=43589739
)

can.add_dataset(
    name='qcd_ht500to700_madgraph',
    id=14279003,
    processes=procs.qcd_ht500to700,
    keys=[
        '/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=85,
    n_events=36082941
)

can.add_dataset(
    name='qcd_ht700to1000_madgraph',
    id=14281356,
    processes=procs.qcd_ht700to1000,
    keys=[
        '/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=84,
    n_events=32788396
)

can.add_dataset(
    name='qcd_ht1000to1500_madgraph',
    id=14296775,
    processes=procs.qcd_ht1000to1500,
    keys=[
        '/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=65,
    n_events=10256089
)

can.add_dataset(
    name='qcd_ht1500to2000_madgraph',
    id=14270490,
    processes=procs.qcd_ht1500to2000,
    keys=[
        '/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=43,
    n_events=7540039
)

can.add_dataset(
    name='qcd_ht2000toinf_madgraph',
    id=14296752,
    processes=procs.qcd_ht2000toinf,
    keys=[
        '/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM'
    ],
    n_files=38,
    n_events=4055223
)
