# coding: utf-8

'''
Z boson datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIMP_nano_uhh_v12 import campaign_run2_2016_HIMP_nano_uhh_v12 as cpn

cpn.add_dataset(
    name="z_nunu_ht600To800_madgraph",
    id=14238483,
    processes=[procs.z_nunu_ht600To800],
    keys=[
        "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2030858,
)

cpn.add_dataset(
    name="z_nunu_ht400To600_madgraph",
    id=14238470,
    processes=[procs.z_nunu_ht400To600],
    keys=[
        "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=6632524,
)

cpn.add_dataset(
    name="z_nunu_ht200To400_madgraph",
    id=14216548,
    processes=[procs.z_nunu_ht200To400],
    keys=[
        "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=7531529,
)

cpn.add_dataset(
    name="z_nunu_ht800To1200_madgraph",
    id=14285553,
    processes=[procs.z_nunu_ht800To1200],
    keys=[
        "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=703970,
)

cpn.add_dataset(
    name="z_nunu_ht1200To2500_madgraph",
    id=14240780,
    processes=[procs.z_nunu_ht1200To2500],
    keys=[
        "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=136393,
)

cpn.add_dataset(
    name="z_nunu_ht2500ToInf_madgraph",
    id=14242842,
    processes=[procs.z_nunu_ht2500ToInf],
    keys=[
        "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=111838,
)

cpn.add_dataset(
    name="z_nunu_ht100To200_madgraph",
    id=14212946,
    processes=[procs.z_nunu_ht100To200],
    keys=[
        "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=7784090,
)

cpn.add_dataset(
    name="z_qq_ht200To400_madgraph",
    id=14303395,
    processes=[procs.z_qq_ht200To400],
    keys=[
        "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=8753905,
)

cpn.add_dataset(
    name="z_qq_ht400To600_madgraph",
    id=14284977,
    processes=[procs.z_qq_ht400To600],
    keys=[
        "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=7709128,
)

cpn.add_dataset(
    name="z_qq_ht600To800_madgraph",
    id=14275517,
    processes=[procs.z_qq_ht600To800],
    keys=[
        "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=6116617,
)

cpn.add_dataset(
    name="z_qq_ht800ToInf_madgraph",
    id=14305027,
    processes=[procs.z_qq_ht800ToInf],
    keys=[
        "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3726992,
)