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

generator = "TuneCP5_PSWeights_13TeV-madgraph-pythia8"
cmssw = "106X_mc2017_realistic_v9-v1"

cpn.add_dataset(
    name="qcd_ht50to100_madgraph",
    id=14281497,
    processes=[procs.qcd_ht50to100],
    keys=[
        f"/QCD_HT50to100_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=52,
    n_events=26129826,
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14300506,
    processes=[procs.qcd_ht100to200],
    keys=[
        f"/QCD_HT100to200_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=99,
    n_events=54705747,
)

cpn.add_dataset(
    name="qcd_ht200to300_madgraph",
    id=14289012,
    processes=[procs.qcd_ht200to300],
    keys=[
        f"/QCD_HT200to300_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=85,
    n_events=42679193,
)

cpn.add_dataset(
    name="qcd_ht300to500_madgraph",
    id=14288347,
    processes=[procs.qcd_ht300to500],
    keys=[
        f"/QCD_HT300to500_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=94,
    n_events=43589739,
)

cpn.add_dataset(
    name="qcd_ht500to700_madgraph",
    id=14279003,
    processes=[procs.qcd_ht500to700],
    keys=[
        f"/QCD_HT500to700_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=85,
    n_events=36082941,
)

cpn.add_dataset(
    name="qcd_ht700to1000_madgraph",
    id=14281356,
    processes=[procs.qcd_ht700to1000],
    keys=[
        f"/QCD_HT700to1000_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=84,
    n_events=32788396,
)

cpn.add_dataset(
    name="qcd_ht1000to1500_madgraph",
    id=14296775,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        f"/QCD_HT1000to1500_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=65,
    n_events=10256089,
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14270490,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        f"/QCD_HT1500to2000_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=43,
    n_events=7540039,
)

cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=14296752,
    processes=[procs.qcd_ht2000toinf],
    keys=[
        f"/QCD_HT2000toInf_{generator}/RunIISummer20UL17NanoAODv9-20UL17JMENano_{cmssw}/NANOAODSIM",
    ],
    n_files=38,
    n_events=4055223,
)
