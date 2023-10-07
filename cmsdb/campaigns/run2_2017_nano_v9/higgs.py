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
    name="h_ggf_tautau_powheg",
    id=14230587,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=12974000,
)

# vbf
cpn.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14232168,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=2811630,
)

# H radiation
cpn.add_dataset(
    name="zh_tautau_powheg",
    id=14363472,
    processes=[procs.zh_tautau],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=4614054,
)

cpn.add_dataset(
    name="zh_llbb_powheg",
    id=14275939,
    processes=[procs.zh_llbb],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4958035,
)

cpn.add_dataset(
    name="wph_tautau_powheg",
    id=14232214,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=3985990,
)

cpn.add_dataset(
    name="wmh_tautau_powheg",
    id=14231275,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=3828192,
)

cpn.add_dataset(
    name="ggzh_llbb_powheg",
    id=14355451,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=4673000,
)

# ttH
cpn.add_dataset(
    name="tth_tautau_powheg",
    id=14230113,
    processes=[procs.tth_tautau],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=68,
    n_events=21165000,
)

cpn.add_dataset(
    name="tth_bb_powheg",
    id=14260809,
    processes=[procs.tth_bb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7825000,
)

cpn.add_dataset(
    name="tth_nonbb_powheg",
    id=14261730,
    processes=[procs.tth_nonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=5070989,
)


# -- higgs to ZZ to 4l

cpn.add_dataset(
    name="h_ggf_4l_powheg",
    id=14241695,
    processes=[procs.h_ggf_4l],
    keys=[
        "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=998000,
)

cpn.add_dataset(
    name="h_vbf_4l_powheg",
    id=14253872,
    processes=[procs.h_vbf_4l],
    keys=[
        "/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=499000,
)

cpn.add_dataset(
    name="wph_4l_powheg",
    id=14260949,
    processes=[procs.wph_4l],
    keys=[
        "/WplusH_HToZZTo4L_M125_TuneCP5_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=299992,
)

cpn.add_dataset(
    name="wmh_4l_powheg",
    id=14253971,
    processes=[procs.wmh_4l],
    keys=[
        "/WminusH_HToZZTo4L_M125_TuneCP5_13TeV_powheg2-minlo-HWJ_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=198461,
)

cpn.add_dataset(
    name="zh_4l_powheg",
    id=14275671,
    processes=[procs.zh_4l],
    keys=[
        "/ZH_HToZZ_4LFilter_M125_TuneCP5_13TeV_powheg2-minlo-HZJ_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=520283,
)

cpn.add_dataset(
    name="tth_4l_powheg",
    id=14288341,
    processes=[procs.tth_4l],
    keys=[
        "/ttH_HToZZ_4LFilter_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=502103,
)

cpn.add_dataset(
    name="bbh_4l_powheg",
    id=14260791,
    processes=[procs.bbh_4l],
    keys=[
        "/bbH_HToZZTo4L_M125_TuneCP2_13TeV-jhugenv7011-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=492928,
)

cpn.add_dataset(
    name="thq_4l_powheg",
    id=14243382,
    processes=[procs.thq_4l],
    keys=[
        "/tqH_HToZZTo4L_M125_TuneCP5_13TeV-jhugenv7011-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=1000000,
)


# -- electroweak backgrounds to ggF higgs production

cpn.add_dataset(
    name="ggf_4e_mcfm",
    id=14241895,
    processes=[procs.ggf_4e],
    keys=[
        "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=997000,
)

cpn.add_dataset(
    name="ggf_4mu_mcfm",
    id=14241935,
    processes=[procs.ggf_4mu],
    keys=[
        "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=975090,
)

cpn.add_dataset(
    name="ggf_4tau_mcfm",
    id=14241899,
    processes=[procs.ggf_4tau],
    keys=[
        "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=499000,
)

cpn.add_dataset(
    name="ggf_2e2mu_mcfm",
    id=14242048,
    processes=[procs.ggf_2e2mu],
    keys=[
        "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=500000,
)

cpn.add_dataset(
    name="ggf_2e2tau_mcfm",
    id=14243002,
    processes=[procs.ggf_2e2tau],
    keys=[
        "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=498000,
)

cpn.add_dataset(
    name="ggf_2mu2tau_mcfm",
    id=14243395,
    processes=[procs.ggf_2mu2tau],
    keys=[
        "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=500000,
)
