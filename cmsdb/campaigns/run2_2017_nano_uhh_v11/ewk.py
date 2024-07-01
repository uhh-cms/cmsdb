# coding: utf-8

"""
Electroweak datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# Drell-Yan
#
cpn.add_dataset(

    name="dy_m50toinf_amcatnlo",
    id=14262131,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=143,
    n_events=196329377,
)

# jet binned, madgraph
# cpn.add_dataset(
#     name="dy_m50toinf_1j_madgraph",
#     id=14242968,
#     processes=[procs.dy_m50toinf_1j],
#     keys=[
#         "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=51,
#     n_events=65903452,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_2j_madgraph",
#     id=14235404,
#     processes=[procs.dy_m50toinf_2j],
#     keys=[
#         "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=19,
#     n_events=27099640,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_3j_madgraph",
#     id=14235548,
#     processes=[procs.dy_m50toinf_3j],
#     keys=[
#         "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=15,
#     n_events=20165687,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_4j_madgraph",
#     id=14235551,
#     processes=[procs.dy_m50toinf_4j],
#     keys=[
#         "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=21,
#     n_events=10872554,
# )
#

# jet binned, amcatnlo
cpn.add_dataset(
    name="dy_0j_amcatnlo",
    id=14222486,
    processes=[procs.dy_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=78448070,
)

cpn.add_dataset(
    name="dy_1j_amcatnlo",
    id=14241548,
    processes=[procs.dy_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=84321311,
)

cpn.add_dataset(
    name="dy_2j_amcatnlo",
    id=14196906,
    processes=[procs.dy_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=47006742,
)

# ht binned
# cpn.add_dataset(
#     name="dy_m50toinf_ht70to100_madgraph",
#     id=14235248,
#     processes=[procs.dy_m50toinf_ht70to100],
#     keys=[
#         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=18,
#     n_events=12205958,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht100to200_madgraph",
#     id=14235412,
#     processes=[procs.dy_m50toinf_ht100to200],
#     keys=[
#         "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=22,
#     n_events=18648544,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht200to400_madgraph",
#     id=14235285,
#     processes=[procs.dy_m50toinf_ht200to400],
#     keys=[
#         "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=37,
#     n_events=12451701,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht400to600_madgraph",
#     id=14234754,
#     processes=[procs.dy_m50toinf_ht400to600],
#     keys=[
#         "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=17,
#     n_events=5384252,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht600to800_madgraph",
#     id=14234976,
#     processes=[procs.dy_m50toinf_ht600to800],
#     keys=[
#         "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=5118706,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht800to1200_madgraph",
#     id=14234833,
#     processes=[procs.dy_m50toinf_ht800to1200],
#     keys=[
#         "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=4347168,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht1200to2500_madgraph",
#     id=14243239,
#     processes=[procs.dy_m50toinf_ht1200to2500],
#     keys=[
#         "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=4725936,
# )
#
# cpn.add_dataset(
#     name="dy_m50toinf_ht2500toinf_madgraph",
#     id=14244972,
#     processes=[procs.dy_m50toinf_ht2500toinf],
#     keys=[
#         "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=12,
#     n_events=1480047,
# )
#

# pt binned
cpn.add_dataset(
    name="dy_pt0to50_amcatnlo",
    id=14349689,
    processes=[procs.dy_pt0to50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=198356238,
)

cpn.add_dataset(
    name="dy_pt50to100_amcatnlo",
    id=14350659,
    processes=[procs.dy_pt50to100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=105,
    n_events=123053065,
)

cpn.add_dataset(
    name="dy_pt100to250_amcatnlo",
    id=14353573,
    processes=[procs.dy_pt100to250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=80740184,
)

cpn.add_dataset(
    name="dy_pt250to400_amcatnlo",
    id=14353503,
    processes=[procs.dy_pt250to400],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=24283448,
)

cpn.add_dataset(
    name="dy_pt400to650_amcatnlo",
    id=14335843,
    processes=[procs.dy_pt400to650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v4/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4042549,
)

cpn.add_dataset(
    name="dy_pt650toinf_amcatnlo",
    id=14349880,
    processes=[procs.dy_pt650toinf],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=4034670,
)


#
# W boson production
#

# inclusive
cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14196281,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=78981243,
)

# ht binned
cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    id=14240461,
    processes=[procs.w_lnu_ht70to100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=44736228,
)

cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    id=14196336,
    processes=[procs.w_lnu_ht100to200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=47424468,
)

cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    id=14195523,
    processes=[procs.w_lnu_ht200to400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=42602407,
)

cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    id=14196379,
    processes=[procs.w_lnu_ht400to600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=5468473,
)

cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    id=14196381,
    processes=[procs.w_lnu_ht600to800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=5545298,
)

cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    id=14222533,
    processes=[procs.w_lnu_ht800to1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=5088483,
)

cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    id=14197191,
    processes=[procs.w_lnu_ht1200to2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=4955636,
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    id=14267026,
    processes=[procs.w_lnu_ht2500toinf],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1185699,
)


#
# EWK
# (vector boson emissions)
#

cpn.add_dataset(
    name="ewk_wm_lnu_m50toinf_madgraph",
    id=14301802,
    processes=[procs.ewk_wm_lnu_m50toinf],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=4077000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50toinf_madgraph",
    id=14300809,
    processes=[procs.ewk_wp_lnu_m50toinf],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=3595000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50toinf_madgraph",
    id=14300868,
    processes=[procs.ewk_z_ll_m50toinf],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=579000,
)


#
# Di-boson
#

# ZZ
cpn.add_dataset(
    name="zz_pythia",
    id=14197074,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2706000,
)

# cpn.add_dataset(
#     name="zz_zqq_zll_m4toinf_amcatnlo",
#     id=14298864,
#     processes=[procs.zz_zqq_zll_m4toinf],
#     keys=[
#         "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=24,
#     n_events=29521496,
# )

# # looking at the generator config:
# # https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_2L2NU_NNPDF31_13TeV.input  # noqa
# # it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# # therefore the corresponding process is with the "_m4" suffix
# cpn.add_dataset(
#     name="zz_zll_znunu_m4toinf_powheg",
#     id=14237024,
#     processes=[procs.zz_zll_znunu_m4toinf],
#     keys=[
#         "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=29,
#     n_events=40839000,
# )

# # looking at the generator config:
# # https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_4L_NNPDF31_13TeV.input  # noqa
# # it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# # therefore the corresponding process is with the "_m4" suffix
# cpn.add_dataset(
#     name="zz_zll_zll_m4toinf_powheg",
#     id=14243658,
#     processes=[procs.zz_zll_zll_m4toinf],
#     keys=[
#         "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=109,
#     n_events=99388000,
# )

# WZ
cpn.add_dataset(
    name="wz_pythia",
    id=14173898,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=7889000,
)

# # looking at the generator config:
# # https://github.com/cms-sw/genproductions/blob/2422e1837f93f875c54f8ace0f02d3dc962eca41/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WZTo3LNu01j_5f_NLO_FXFX/WZTo3LNu01j_5f_NLO_FXFX_run_card.dat  # noqa
# # it seems that there is a lepton mass cut of 4 GeV for leptons from Z, like in the ZZTo2Q2L channel
# # therefore the corresponding process is with the "_m4" suffix
# cpn.add_dataset(
#     name="wz_wlnu_zll_m4toinf_amcatnlo",
#     id=14253602,
#     processes=[procs.wz_wlnu_zll_m4toinf],
#     keys=[
#         "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=31,
#     n_events=10339582,
# )

# cpn.add_dataset(
#     name="wz_wqq_zll_m4toinf_amcatnlo",
#     id=14328000,
#     processes=[procs.wz_wqq_zll_m4toinf],
#     keys=[
#         "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=30,
#     n_events=29091996,
# )

# WW
cpn.add_dataset(
    name="ww_pythia",
    id=14175175,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=15634000,
)

# cpn.add_dataset(
#     name="ww_dl_powheg",
#     id=14241651,
#     processes=[procs.ww_dl],
#     keys=[
#         "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=46,
#     n_events=7098000,
# )


#
# Triple-boson
#

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14269622,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=9524000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14240923,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=9898000,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14195642,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=178000,
)

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14241535,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=9854000,
)
