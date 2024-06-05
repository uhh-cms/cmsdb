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
    name="h_ggf_htt_powheg",
    id=14283350,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=6439000,
)

cpn.add_dataset(
    name="h_ggf_htt_amcatnlo",
    id=14243280,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M-125_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2928748,
)

# vbf
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14262211,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1500000,
)

# H radiation
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14335727,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2209078,
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14351964,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=4583850,
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14265971,
    processes=[procs.zh_htt],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2419675,
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14262287,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2000000,
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14262330,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1995182,
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14336166,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/zh_gg_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2189000,
)

# ttH

cpn.add_dataset(
    name="tth_htt_powheg",
    id=14254825,
    processes=[procs.tth_htt],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=10789000,
)

cpn.add_dataset(
    name="tthjet_hbb_amcatnlo",
    id=14211716,
    processes=[procs.tth_hbb],
    keys=[
        "/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=5172661,
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14275551,
    processes=[procs.tth_hbb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=4937000,
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14275559,
    processes=[procs.tth_hnonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2240994,
)
