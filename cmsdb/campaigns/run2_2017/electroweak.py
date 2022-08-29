# coding: utf-8

"""
Electroweak datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs

from cmsdb.campaigns import run2_2017

#
# Drell-Yan
#

# jet binned, madgraph
run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14242968,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=65903452,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14235404,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=27099640,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14235548,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=20165687,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14235551,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=10872554,
)

# jet binned, amcatnlo
run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_0j_amcatnlo",
    id=14302706,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=78288099,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_1j_amcatnlo",
    id=14300055,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=84321311,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_2j_amcatnlo",
    id=14231469,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=46395058,
)

# ht binned
run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht70to100_madgraph",
    id=14235248,
    processes=[procs.dy_lep_m50_ht70to100],
    keys=[
        "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=12205958,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht100to200_madgraph",
    id=14235412,
    processes=[procs.dy_lep_m50_ht100to200],
    keys=[
        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=18648544,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht200to400_madgraph",
    id=14235285,
    processes=[procs.dy_lep_m50_ht200to400],
    keys=[
        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=12451701,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht400to600_madgraph",
    id=14234754,
    processes=[procs.dy_lep_m50_ht400to600],
    keys=[
        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5384252,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht600to800_madgraph",
    id=14234976,
    processes=[procs.dy_lep_m50_ht600to800],
    keys=[
        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=5118706,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht800to1200_madgraph",
    id=14234833,
    processes=[procs.dy_lep_m50_ht800to1200],
    keys=[
        "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4347168,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht1200to2500_madgraph",
    id=14243239,
    processes=[procs.dy_lep_m50_ht1200to2500],
    keys=[
        "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=4725936,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht2500_madgraph",
    id=14244972,
    processes=[procs.dy_lep_m50_ht2500],
    keys=[
        "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=1480047,
)

# pt binned
run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_pt50To100_amcatnlo",
    id=14231159,
    processes=[procs.dy_lep_pt50To100],
    keys=[
        "/DYJetsToLL_Pt-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=107079717,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_pt100To250_amcatnlo",
    id=14300156,
    processes=[procs.dy_lep_pt100To250],
    keys=[
        "/DYJetsToLL_Pt-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=75818801,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_pt250To400_amcatnlo",
    id=14235259,
    processes=[procs.dy_lep_pt250To400],
    keys=[
        "/DYJetsToLL_Pt-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=18739246,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_pt400To650_amcatnlo",
    id=14228178,
    processes=[procs.dy_lep_pt400To650],
    keys=[
        "/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1895259,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="dy_lep_pt650_amcatnlo",
    id=14232153,
    processes=[procs.dy_lep_pt650],
    keys=[
        "/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=1921546,
)


#
# W boson production
#

# inclusive
run2_2017.campaign_run2_2017.add_dataset(
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
run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht70To100_madgraph",
    id=14245091,
    processes=[procs.w_lnu_ht70To100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=44576510,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht100To200_madgraph",
    id=14231627,
    processes=[procs.w_lnu_ht100To200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=47424468,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht200To400_madgraph",
    id=14239255,
    processes=[procs.w_lnu_ht200To400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=42281979,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht400To600_madgraph",
    id=14231356,
    processes=[procs.w_lnu_ht400To600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=5468473,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht600To800_madgraph",
    id=14230638,
    processes=[procs.w_lnu_ht600To800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5545298,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht800To1200_madgraph",
    id=14346984,
    processes=[procs.w_lnu_ht800To1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=5088483,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht1200To2500_madgraph",
    id=14231551,
    processes=[procs.w_lnu_ht1200To2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=4752118,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="w_lnu_ht2500_madgraph",
    id=14267094,
    processes=[procs.w_lnu_ht2500],
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

run2_2017.campaign_run2_2017.add_dataset(
    name="ewk_wm_lnu_madgraph",
    id=14301832,
    processes=[procs.ewk_wm_lnu],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4077000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="ewk_w_lnu_madgraph",
    id=14300978,
    processes=[procs.ewk_wp_lnu],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=3595000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="ewk_z_ll_madgraph",
    id=14301412,
    processes=[procs.ewk_z_ll],
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
run2_2017.campaign_run2_2017.add_dataset(
    name="zz_pythia",
    id=14227451,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2706000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="zz_qqll_m4_amcatnlo",
    id=14298864,
    processes=[procs.zz_qqll_m4],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=29521496,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="zz_llnunu_powheg",
    id=14237024,
    processes=[procs.zz_llnunu],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=40839000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="zz_llll_powheg",
    id=14243658,
    processes=[procs.zz_llll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=99388000,
)

# WZ
run2_2017.campaign_run2_2017.add_dataset(
    name="wz_pythia",
    id=14230373,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=7889000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14253602,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=10339582,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="wz_qqll_m4_amcatnlo",
    id=14328000,
    processes=[procs.wz_qqll_m4],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=29091996,
)

# WW
run2_2017.campaign_run2_2017.add_dataset(
    name="ww_pythia",
    id=14229298,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=15634000,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="ww_lnulnu_powheg",
    id=14241651,
    processes=[procs.ww_lnulnu],
    keys=[
        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7098000,
)


#
# Triple-boson
#

run2_2017.campaign_run2_2017.add_dataset(
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

run2_2017.campaign_run2_2017.add_dataset(
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

run2_2017.campaign_run2_2017.add_dataset(
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

run2_2017.campaign_run2_2017.add_dataset(
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
