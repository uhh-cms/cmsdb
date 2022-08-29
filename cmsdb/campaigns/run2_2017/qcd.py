# coding: utf-8

"""
QCD datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017 import campaign_run2_2017


campaign_run2_2017.add_dataset(
    name="qcd_ht50to100_madgraph",
    id=14165805,
    processes=[procs.qcd_ht50to100],
    keys=[
        "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=40370559,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14165816,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=77551016,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht200to300_madgraph",
    id=14165798,
    processes=[procs.qcd_ht200to300],
    keys=[
        "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=57400723,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht300to500_madgraph",
    id=14165206,
    processes=[procs.qcd_ht300to500],
    keys=[
        "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=56549740,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht500to700_madgraph",
    id=14165524,
    processes=[procs.qcd_ht500to700],
    keys=[
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=14 + 50,
    n_events=9027879 + 57880117,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht700to1000_madgraph",
    id=14165795,
    processes=[procs.qcd_ht700to1000],
    keys=[
        "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=45812757,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht1000to1500_madgraph",
    id=14165562,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=15346629,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14165704,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=10598209,
)

campaign_run2_2017.add_dataset(
    name="qcd_ht2000_madgraph",
    id=14165502,
    processes=[procs.qcd_ht2000],
    keys=[
        "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5457021,
)
