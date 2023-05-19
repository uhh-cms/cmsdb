# coding: utf-8

"""
Higgs datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14198289,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=12974000,
)

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14198046,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2876240,
)

# H radiation
cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14336755,
    processes=[procs.zh_tautau],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4757708,
)

cpn.add_dataset(
    name="zh_bb_powheg",
    id=14354874,
    processes=[procs.zh_bb],
    keys=[
        "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=9991620,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14275937,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4958035,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14198100,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3985990,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14198107,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3828192,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14336238,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4833000,
)

# ttH
cpn.add_dataset(
    name="tth_tautau_powheg",
    id=14198429,
    processes=[procs.tth_tautau],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=21700000,
)

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14260234,
    processes=[procs.tth_bb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=7825000,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14261680,
    processes=[procs.tth_nonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=5070989,
)
