# coding: utf-8

'''
Multi boson datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn

cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14270880,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=74676454,
)

cpn.add_dataset(
    name="w_lnu_ht2500ToInf_madgraph",
    id=14266888,
    processes=[procs.w_lnu_ht2500ToInf],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=808649,
)

cpn.add_dataset(
    name="w_lnu_ht70To100_madgraph",
    id=14300594,
    processes=[procs.w_lnu_ht70To100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=16931765,
)

cpn.add_dataset(
    name="w_lnu_ht100To200_madgraph",
    id=14221276,
    processes=[procs.w_lnu_ht100To200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=21734530,
)

cpn.add_dataset(
    name="w_lnu_ht1200To2500_madgraph",
    id=14226935,
    processes=[procs.w_lnu_ht1200To2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2119975,
)

cpn.add_dataset(
    name="w_lnu_ht400To600_madgraph",
    id=14213493,
    processes=[procs.w_lnu_ht400To600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2467498,
)

cpn.add_dataset(
    name="w_lnu_ht600To800_madgraph",
    id=14227116,
    processes=[procs.w_lnu_ht600To800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2344130,
)

cpn.add_dataset(
    name="w_lnu_ht800To1200_madgraph",
    id=14212489,
    processes=[procs.w_lnu_ht800To1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2510487,
)

cpn.add_dataset(
    name="w_lnu_ht200To400_madgraph",
    id=14212310,
    processes=[procs.w_lnu_ht200To400_madgraph],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=17870845,
)