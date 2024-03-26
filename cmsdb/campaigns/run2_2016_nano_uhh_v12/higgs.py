# coding: utf-8

"""
Higgs datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_uhh_v12 import campaign_run2_2016_nano_uhh_v12 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14283350,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=6439000,
)

cpn.add_dataset(
    name="h_ggf_tautau_amcatnlo",
    id=14243280,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2928748,
)

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14262211,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1500000,
)

# H radiation
cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14335727,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2209078,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14351964,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=4583850,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14265971,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2419675,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14262287,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2000000,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14262330,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1995182,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14336166,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2189000,
)

# ttH

cpn.add_dataset(
    name="tth_tautau_powheg",
    id=14254825,
    processes=[procs.tth_tautau],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=10789000,
)

cpn.add_dataset(
    name="tthjet_bb_amcatnlo",
    id=14211716,
    processes=[procs.tth_bb],
    keys=[
        "/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=5172661,
)

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14275551,
    processes=[procs.tth_bb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=4937000,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14275559,
    processes=[procs.tth_nonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2240994,
)
