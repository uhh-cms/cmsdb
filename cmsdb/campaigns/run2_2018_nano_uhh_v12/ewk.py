# # coding: utf-8

# """
# Electroweak datasets for the 2018 data-taking campaign with datasets at NanoAOD tier in
# version 12, created with custom content at UHH.
# """

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_uhh_v12 import campaign_run2_2018_nano_uhh_v12 as cpn


# DY
cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14196228,
    processes=[procs.dy_m10to50],
    keys=[
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=99288125,
)

cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14205668,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=96233328,
)

cpn.add_dataset(
    name="dy_m50toinf_ext1_madgraph",
    id=14179545,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=101415750,
)

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14260218,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=113,
    n_events=196626007,
)

# jet binned
cpn.add_dataset(
    name="dy_m50toinf_1j_madgraph",
    id=14212255,
    processes=[procs.dy_m50toinf_1j],
    keys=[
        "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=60368985,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_madgraph",
    id=14209983,
    processes=[procs.dy_m50toinf_2j],
    keys=[
        "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=27494377,
)

cpn.add_dataset(
    name="dy_m50toinf_3j_madgraph",
    id=14284866,
    processes=[procs.dy_m50toinf_3j],
    keys=[
        "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=20466041,
)

cpn.add_dataset(
    name="dy_m50toinf_4j_madgraph",
    id=14214881,
    processes=[procs.dy_m50toinf_4j],
    keys=[
        "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=8885353,
)

cpn.add_dataset(
    name="dy_0j_amcatnlo",
    id=14196360,
    processes=[procs.dy_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=86443196,
)

cpn.add_dataset(
    name="dy_1j_amcatnlo",
    id=14198526,
    processes=[procs.dy_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=92267238,
)

cpn.add_dataset(
    name="dy_2j_amcatnlo",
    id=14198570,
    processes=[procs.dy_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=44735479,
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

# pt binned
cpn.add_dataset(
    name="dy_pt0to50_amcatnlo",
    id=14349198,
    processes=[procs.dy_pt0to50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=122,
    n_events=198329754,
)

cpn.add_dataset(
    name="dy_pt50to100_amcatnlo",
    id=14349041,
    processes=[procs.dy_pt50to100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=123100779,
)

cpn.add_dataset(
    name="dy_pt100to250_amcatnlo",
    id=14348756,
    processes=[procs.dy_pt100to250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=79621344,
)

cpn.add_dataset(
    name="dy_pt250to400_amcatnlo",
    id=14349402,
    processes=[procs.dy_pt250to400],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=24195330,
)

cpn.add_dataset(
    name="dy_pt400to650_amcatnlo",
    id=14355832,
    processes=[procs.dy_pt400to650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3954087,
)

cpn.add_dataset(
    name="dy_pt650toinf_amcatnlo",
    id=14353254,
    processes=[procs.dy_pt650toinf],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3994997,
)

# Z boson production
cpn.add_dataset(
    name="z_nunu_ht2500toinf_madgraph",
    id=14202078,
    processes=[procs.z_nunu_ht2500toinf],
    keys=[
        "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=268224,
)

cpn.add_dataset(
    name="z_nunu_ht1200to2500_madgraph",
    id=14238202,
    processes=[procs.z_nunu_ht1200to2500],
    keys=[
        "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=381695,
)

cpn.add_dataset(
    name="z_nunu_ht800to1200_madgraph",
    id=14202929,
    processes=[procs.z_nunu_ht800to1200],
    keys=[
        "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2129122,
)

cpn.add_dataset(
    name="z_nunu_ht600to800_madgraph",
    id=14208190,
    processes=[procs.z_nunu_ht600to800],
    keys=[
        "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=5968910,
)

cpn.add_dataset(
    name="z_nunu_ht400to600_madgraph",
    id=14206085,
    processes=[procs.z_nunu_ht400to600],
    keys=[
        "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=19810491,
)

cpn.add_dataset(
    name="z_nunu_ht200to400_madgraph",
    id=14222577,
    processes=[procs.z_nunu_ht200to400],
    keys=[
        "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=22749608,
)

cpn.add_dataset(
    name="z_nunu_ht100to200_madgraph",
    id=14196293,
    processes=[procs.z_nunu_ht100to200],
    keys=[
        "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=28876062,
)


#
# W boson production
#

# inclusive
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14196327,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=82442496,
)

# ht binned
cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    id=14196361,
    processes=[procs.w_lnu_ht70to100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=66189554,
)

cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    id=14222479,
    processes=[procs.w_lnu_ht100to200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=51541593,
)

cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    id=14196351,
    processes=[procs.w_lnu_ht200to400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=58331446,
)

cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    id=14196599,
    processes=[procs.w_lnu_ht400to600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=7444030,
)

cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    id=14196615,
    processes=[procs.w_lnu_ht600to800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=7718765,
)

cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    id=14195662,
    processes=[procs.w_lnu_ht800to1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=7306187,
)

cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    id=14241552,
    processes=[procs.w_lnu_ht1200to2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=6481518,
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    id=14278023,
    processes=[procs.w_lnu_ht2500toinf],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2097648,
)

cpn.add_dataset(
    name="w_taunu_pythia",
    id=14201993,
    processes=[procs.w_taunu],
    keys=[
        "/WToTauNu_M-200_TuneCP5_13TeV-pythia8-tauola/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1949000,
)

cpn.add_dataset(
    name="w_munu_pythia",
    id=14211588,
    processes=[procs.w_munu],
    keys=[
        "/WToMuNu_M-200_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1952000,
)


#
# EWK
# (vector boson emissions)
#

cpn.add_dataset(
    name="ewk_wm_lnu_m50toinf_madgraph",
    id=14241011,
    processes=[procs.ewk_wm_lnu_m50toinf],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=4479000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50toinf_madgraph",
    id=14266666,
    processes=[procs.ewk_wp_lnu_m50toinf],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=4488000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50toinf_madgraph",
    id=14241555,
    processes=[procs.ewk_z_ll_m50toinf],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1000000,
)

#
# Di-boson
#

# ZZ
# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_pythia",
    id=14241945,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=3526000,
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zqq_zll_pythia",
    id=14284213,
    processes=[procs.zz_zqq_zll],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=29357938,
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zll_znunu_pythia",
    id=14196326,
    processes=[procs.zz_zll_znunu],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=56886000,
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_znunu_zqq_pythia",
    id=14245915,
    processes=[procs.zz_znunu_zqq],
    keys=[
        "/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=19813764,
)

# there is a 4 GeV mZ cut, which has no effect on the cross section though
cpn.add_dataset(
    name="zz_zqq_zqq_pythia",
    id=14373150,
    processes=[procs.zz_zqq_zqq],
    keys=[
        "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2535895,
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=14241106,
    processes=[procs.zz_zll_zll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=99191000,
)

# WZ
cpn.add_dataset(
    name="wz_pythia",
    id=14196374,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=7940000,
)

cpn.add_dataset(
    name="wz_wlnu_zll_pythia",
    id=14253723,
    processes=[procs.wz_wlnu_zll],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=9821283,
)

cpn.add_dataset(
    name="wz_wqq_zll_pythia",
    id=14284121,
    processes=[procs.wz_wqq_zll],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=28576996,
)

cpn.add_dataset(
    name="wz_wlnu_zqq_4f_amcatnlo",
    id=14373352,
    processes=[procs.wz_wlnu_zqq],
    keys=[
        "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=7395487,
)

# WW
cpn.add_dataset(
    name="ww_pythia",
    id=14196344,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=15679000,
)

cpn.add_dataset(
    name="ww_sl_4f_pythia",
    id=14372963,
    processes=[procs.ww_sl],
    keys=[
        "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=40272013,
)

cpn.add_dataset(
    name="ww_dl_powheg",
    id=14241325,
    processes=[procs.ww_dl],
    keys=[
        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=9994000,
)

cpn.add_dataset(
    name="ww_fh_4f_amcatnlo",
    id=14373134,
    processes=[procs.ww_fh],
    keys=[
        "/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=39674916,
)

#
# Triple-boson
#

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14195605,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=250000,
)

cpn.add_dataset(
    name="zzz_ext_amcatnlo",
    id=14241156,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=9889000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14210398,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="wzz_ext_amcatnlo",
    id=14241005,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=9994000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14195619,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=248000,
)

cpn.add_dataset(
    name="wwz_4f_ext_amcatnlo",
    id=14266674,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=9961999,
)

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14195624,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=240000,
)

cpn.add_dataset(
    name="www_4f_ext_amcatnlo",
    id=14266489,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=9894000,
)
