# coding: utf-8

"""
Electroweak datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# Drell-Yan
#

# jet binned, madgraph
cpn.add_dataset(
    name="dy_m50toinf_1j_madgraph",
    id=14242968,
    processes=[procs.dy_m50toinf_1j],
    keys=[
        "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=65903452,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_madgraph",
    id=14235404,
    processes=[procs.dy_m50toinf_2j],
    keys=[
        "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=27099640,
)

cpn.add_dataset(
    name="dy_m50toinf_3j_madgraph",
    id=14235548,
    processes=[procs.dy_m50toinf_3j],
    keys=[
        "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=20165687,
)

cpn.add_dataset(
    name="dy_m50toinf_4j_madgraph",
    id=14235551,
    processes=[procs.dy_m50toinf_4j],
    keys=[
        "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=10872554,
)

# jet binned, amcatnlo
cpn.add_dataset(
    name="dy_0j_amcatnlo",
    id=14302706,
    processes=[procs.dy_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=78288099,
)

cpn.add_dataset(
    name="dy_1j_amcatnlo",
    id=14300055,
    processes=[procs.dy_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=84321311,
)

cpn.add_dataset(
    name="dy_2j_amcatnlo",
    id=14231469,
    processes=[procs.dy_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=46395058,
)

# ht binned
cpn.add_dataset(
    name="dy_m50toinf_ht70to100_madgraph",
    id=14235248,
    processes=[procs.dy_m50toinf_ht70to100],
    keys=[
        "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=12205958,
)

cpn.add_dataset(
    name="dy_m50toinf_ht100to200_madgraph",
    id=14235412,
    processes=[procs.dy_m50toinf_ht100to200],
    keys=[
        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=18648544,
)

cpn.add_dataset(
    name="dy_m50toinf_ht200to400_madgraph",
    id=14235285,
    processes=[procs.dy_m50toinf_ht200to400],
    keys=[
        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=12451701,
)

cpn.add_dataset(
    name="dy_m50toinf_ht400to600_madgraph",
    id=14234754,
    processes=[procs.dy_m50toinf_ht400to600],
    keys=[
        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5384252,
)

cpn.add_dataset(
    name="dy_m50toinf_ht600to800_madgraph",
    id=14234976,
    processes=[procs.dy_m50toinf_ht600to800],
    keys=[
        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=5118706,
)

cpn.add_dataset(
    name="dy_m50toinf_ht800to1200_madgraph",
    id=14234833,
    processes=[procs.dy_m50toinf_ht800to1200],
    keys=[
        "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4347168,
)

cpn.add_dataset(
    name="dy_m50toinf_ht1200to2500_madgraph",
    id=14243239,
    processes=[procs.dy_m50toinf_ht1200to2500],
    keys=[
        "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=4725936,
)

cpn.add_dataset(
    name="dy_m50toinf_ht2500toinf_madgraph",
    id=14244972,
    processes=[procs.dy_m50toinf_ht2500toinf],
    keys=[
        "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=1480047,
)

#
# W boson production
#

# inclusive
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14233715,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=81,
    n_events=78307186,
)

# ht binned
cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    id=14245091,
    processes=[procs.w_lnu_ht70to100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=44576510,
)

cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    id=14231627,
    processes=[procs.w_lnu_ht100to200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=47424468,
)

cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    id=14239255,
    processes=[procs.w_lnu_ht200to400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=42281979,
)

cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    id=14231356,
    processes=[procs.w_lnu_ht400to600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=5468473,
)

cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    id=14230638,
    processes=[procs.w_lnu_ht600to800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5545298,
)

cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    id=14346984,
    processes=[procs.w_lnu_ht800to1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=5088483,
)

cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    id=14231551,
    processes=[procs.w_lnu_ht1200to2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=4752118,
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    id=14267094,
    processes=[procs.w_lnu_ht2500toinf],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=1185699,
)


#
# EWK
# (vector boson emissions)
#

cpn.add_dataset(
    name="ewk_wm_lnu_m50toinf_madgraph",
    id=14301832,
    processes=[procs.ewk_wm_lnu_m50toinf],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4077000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50toinf_madgraph",
    id=14300978,
    processes=[procs.ewk_wp_lnu_m50toinf],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=3595000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50toinf_madgraph",
    id=14301412,
    processes=[procs.ewk_z_ll_m50toinf],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=579000,
)


#
# Di-boson
#

# ZZ
cpn.add_dataset(
    name="zz_pythia",
    id=14227451,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2706000,
)

cpn.add_dataset(
    name="zz_zqq_zll_m4toinf_amcatnlo",
    id=14298864,
    processes=[procs.zz_zqq_zll_m4toinf],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=29521496,
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_2L2NU_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore the corresponding process is with the "_m4" suffix
cpn.add_dataset(
    name="zz_zll_znunu_m4toinf_powheg",
    id=14237024,
    processes=[procs.zz_zll_znunu_m4toinf],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=40839000,
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_4L_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore the corresponding process is with the "_m4" suffix
cpn.add_dataset(
    name="zz_zll_zll_m4toinf_powheg",
    id=14243658,
    processes=[procs.zz_zll_zll_m4toinf],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=99388000,
)

# WZ
cpn.add_dataset(
    name="wz_pythia",
    id=14230373,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=7889000,
)

# looking at the generator config:
# https://github.com/cms-sw/genproductions/blob/2422e1837f93f875c54f8ace0f02d3dc962eca41/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WZTo3LNu01j_5f_NLO_FXFX/WZTo3LNu01j_5f_NLO_FXFX_run_card.dat  # noqa
# it seems that there is a lepton mass cut of 4 GeV for leptons from Z, like in the ZZTo2Q2L channel
# therefore the corresponding process is with the "_m4" suffix
cpn.add_dataset(
    name="wz_wlnu_zll_m4toinf_amcatnlo",
    id=14253602,
    processes=[procs.wz_wlnu_zll_m4toinf],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=10339582,
)

cpn.add_dataset(
    name="wz_wqq_zll_m4toinf_amcatnlo",
    id=14328000,
    processes=[procs.wz_wqq_zll_m4toinf],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=29091996,
)

# WW
cpn.add_dataset(
    name="ww_pythia",
    id=14229298,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=15634000,
)

cpn.add_dataset(
    name="ww_dl_powheg",
    id=14241651,
    processes=[procs.ww_dl],
    keys=[
        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7098000,
)

#
# Triple-boson
#

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14231380,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=15 + 31,
    n_events=178000 + 9524000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14247843,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 23,
    n_events=298000 + 9898000,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14231348,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5 + 41,
    n_events=178000 + 9938400,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id=14231501,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16 + 43,
    n_events=171000 + 9854000,
)
