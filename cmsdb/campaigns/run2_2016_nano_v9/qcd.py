# coding: utf-8

"""
QCD datasets for the 2016 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn

#
# QCD PSWeights samples (HT-binned)
#

cpn.add_dataset(
    name="qcd_ht50to100_madgraph",
    id=14339351,
    processes=[procs.qcd_ht50to100],
    keys=[
        "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=35474117,
)


cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14234937,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=73506112,
)


cpn.add_dataset(
    name="qcd_ht200to300_madgraph",
    id=14235126,
    processes=[procs.qcd_ht200to300],
    keys=[
        "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=43280518,
)


cpn.add_dataset(
    name="qcd_ht300to500_madgraph",
    id=14318340,
    processes=[procs.qcd_ht300to500],
    keys=[
        "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=46335846,
)


cpn.add_dataset(
    name="qcd_ht500to700_madgraph",
    id=14339826,
    processes=[procs.qcd_ht500to700],
    keys=[
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=74,
    n_events=52661606,
)


cpn.add_dataset(
    name="qcd_ht700to1000_madgraph",
    id=14339827,
    processes=[procs.qcd_ht700to1000],
    keys=[
        "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=41664730,
)


cpn.add_dataset(
    name="qcd_ht1000to1500_madgraph",
    id=14245012,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=12254238,
)


cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14244346,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=9376965,
)


cpn.add_dataset(
    name="qcd_ht2000_madgraph",
    id=14235577,
    processes=[procs.qcd_ht2000],
    keys=[
        "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=4867995,
)

