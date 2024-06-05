# coding: utf-8

"""
Higgs datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# Single Higgs
#

# ggf
cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14230587,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=12974000,
)

# vbf
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14232168,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=2811630,
)

# H radiation
cpn.add_dataset(
    name="zh_htt_powheg",
    id=14363472,
    processes=[procs.zh_htt],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=4614054,
)

cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14275939,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4958035,
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14232214,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=3985990,
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14231275,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=3828192,
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14355451,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/zh_gg_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=4673000,
)

# ttH
cpn.add_dataset(
    name="tth_htt_powheg",
    id=14230113,
    processes=[procs.tth_htt],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=68,
    n_events=21165000,
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14260809,
    processes=[procs.tth_hbb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7825000,
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14261730,
    processes=[procs.tth_hnonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=5070989,
)
