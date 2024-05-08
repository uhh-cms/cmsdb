# coding: utf-8

"""
Higgs datasets for the 2018 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_uhh_v12 import campaign_run2_2018_nano_uhh_v12 as cpn


#
# Single Higgs
#

# ggf

cpn.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14198264,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v3/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=12966000,
)


# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14198305,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2987000,
)

# H radiation

cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14336743,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4885835,
)

# z -> ll , h -> bb
cpn.add_dataset(
    name="gg_zh_zll_hbb_powheg",
    id=14340023,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4891000,
)

cpn.add_dataset(
    name="zh_qqbb_powheg",
    id=14355708,
    processes=[procs.zh_qqbb],
    keys=[
        "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=9957048,
)

cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14314109,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=4900155,
)


cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14198104,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3972496,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14198147,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3831952,
)


# ttH
cpn.add_dataset(
    name="tth_tautau_powheg",
    id=14198975,
    processes=[procs.tth_tautau],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v3/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=21621000,
)


cpn.add_dataset(
    name="tth_bb_powheg",
    id=14196265,
    processes=[procs.tth_bb],
    keys=[
        "/ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=10020658,
)


cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14265773,
    processes=[procs.tth_nonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=7328993,
)
