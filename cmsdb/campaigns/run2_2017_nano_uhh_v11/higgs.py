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
    name="h_ggf_htt_powheg",
    id=14198289,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=12974000,
)

# vbf
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14198046,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2876240,
)

# H radiation
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14336755,
    processes=[procs.zh_zll_hbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4757708,
)

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14354874,
    processes=[procs.zh_zqq_hbb],
    keys=[
        "/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=9991620,
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=14275937,
    processes=[procs.zh_htt],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4958035,
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14198100,
    processes=[procs.wph_htt],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3985990,
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14198107,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3828192,
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14336238,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4833000,
)

# ttH
cpn.add_dataset(
    name="tth_htt_powheg",
    id=14198429,
    processes=[procs.tth_htt],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=21700000,
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14260234,
    processes=[procs.tth_hbb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=7825000,
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14261680,
    processes=[procs.tth_hnonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=5070989,
)
