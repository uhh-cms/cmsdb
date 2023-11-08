# # coding: utf-8

# """
# Electroweak datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
# version 11, created with custom content at UHH.
# """

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


# #
# # Drell-Yan
# #
# cpn.add_dataset(


cpn.add_dataset(
    name="dy_lep_m10to50_madgraph",
    id=14196228,
    processes=[procs.dy_lep_m10to50],
    keys=[
        "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=99288125,
)

cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14205668,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=96233328,
)

cpn.add_dataset(
    name="dy_lep_m50_ext1_madgraph",
    id=14179545,
    processes=[procs.dy_lep_m50_ext1],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=101415750,
)

# # jet binned, madgraph

cpn.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14284866,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=20466041,
)


cpn.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14209983,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=27494377,
)

cpn.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14212255,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=60368985,
)


# # cpn.add_dataset(
# #     name="dy_lep_m50_4j_madgraph",
# #     id=14235551,
# #     processes=[procs.dy_lep_m50_4j],
# #     keys=[
# #         "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=21,
# #     n_events=10872554,
# # )
# #

cpn.add_dataset(
    name="dy_lep_0j_amcatnlo",
    id=14196360,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=86443196,
)


# cpn.add_dataset(
#     name="dy_lep_1j_amcatnlo",
#     id=14241548,
#     processes=[procs.dy_lep_1j],
#     keys=[
#         "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=67,
#     n_events=84321311,
# )


cpn.add_dataset(
    name="dy_lep_2j_amcatnlo",
    id=14198570,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=44735479,
)



# # ht binned


# # cpn.add_dataset(
# #     name="dy_lep_m50_ht70to100_madgraph",
# #     id=14235248,
# #     processes=[procs.dy_lep_m50_ht70to100],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=18,
# #     n_events=12205958,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht100to200_madgraph",
# #     id=14235412,
# #     processes=[procs.dy_lep_m50_ht100to200],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=22,
# #     n_events=18648544,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht200to400_madgraph",
# #     id=14235285,
# #     processes=[procs.dy_lep_m50_ht200to400],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=37,
# #     n_events=12451701,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht400to600_madgraph",
# #     id=14234754,
# #     processes=[procs.dy_lep_m50_ht400to600],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=17,
# #     n_events=5384252,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht600to800_madgraph",
# #     id=14234976,
# #     processes=[procs.dy_lep_m50_ht600to800],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=14,
# #     n_events=5118706,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht800to1200_madgraph",
# #     id=14234833,
# #     processes=[procs.dy_lep_m50_ht800to1200],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=16,
# #     n_events=4347168,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht1200to2500_madgraph",
# #     id=14243239,
# #     processes=[procs.dy_lep_m50_ht1200to2500],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=14,
# #     n_events=4725936,
# # )
# #
# # cpn.add_dataset(
# #     name="dy_lep_m50_ht2500_madgraph",
# #     id=14244972,
# #     processes=[procs.dy_lep_m50_ht2500],
# #     keys=[
# #         "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=12,
# #     n_events=1480047,
# # )
# #

# # pt binned

cpn.add_dataset(
    name="dy_lep_pt0To50_amcatnlo",
    id=14349198,
    processes=[procs.dy_lep_pt0To50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=122,
    n_events=198329754,
)

cpn.add_dataset(
    name="dy_lep_pt50To100_amcatnlo",
    id=14349041,
    processes=[procs.dy_lep_pt50To100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=123100779,
)

cpn.add_dataset(
    name="dy_lep_pt100To250_amcatnlo",
    id=14348756,
    processes=[procs.dy_lep_pt100To250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=79621344,
)

# cpn.add_dataset(
#     name="dy_lep_pt250To400_amcatnlo",
#     id=14353503,
#     processes=[procs.dy_lep_pt250To400],
#     keys=[
#         "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=34,
#     n_events=24283448,
# )

cpn.add_dataset(
    name="dy_lep_pt400To650_amcatnlo",
    id=14355832,
    processes=[procs.dy_lep_pt400To650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3954087,
)

cpn.add_dataset(
    name="dy_lep_pt650ToInf_amcatnlo",
    id=14353254,
    processes=[procs.dy_lep_pt650ToInf],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3994997,
)


# Z boson production

cpn.add_dataset(
    name="z_2nu_ht2500toinf_madgraph",
    id=14202078,
    processes=[procs.z_2nu_ht2500toinf],
    keys=[
        "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=268224,
)

cpn.add_dataset(
    name="z_2nu_ht1200to2500_madgraph",
    id=14238202,
    processes=[procs.z_2nu_ht1200to2500],
    keys=[
        "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=381695,
)

cpn.add_dataset(
    name="z_2nu_ht800to1200_madgraph",
    id=14202929,
    processes=[procs.z_2nu_ht800to1200],
    keys=[
        "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2129122,
)


cpn.add_dataset(
    name="z_2nu_ht600to800_madgraph",
    id=14208190,
    processes=[procs.z_2nu_ht600to800],
    keys=[
        "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=5968910,
)


cpn.add_dataset(
    name="z_2nu_ht400to600",
    id=14206085,
    processes=[procs.z_2nu_ht400to600],
    keys=[
        "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=19810491,
)


cpn.add_dataset(
    name="z_2nu_ht200to400",
    id=14222577,
    processes=[procs.z_2nu_ht200to400],
    keys=[
        "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=22749608,
)

# #
# # W boson production
# #

# # inclusive





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


# cpn.add_dataset(
#     name="w_lnu_madgraph",
#     id=14196281,
#     processes=[procs.w_lnu],
#     keys=[
#         "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=45,
#     n_events=78981243,
# )

# # ht binned
# cpn.add_dataset(
#     name="w_lnu_ht70To100_madgraph",
#     id=14240461,
#     processes=[procs.w_lnu_ht70To100],
#     keys=[
#         "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=33,
#     n_events=44736228,
# )


cpn.add_dataset(
    name="w_lnu_ht100To200_madgraph",
    id=14222479,
    processes=[procs.w_lnu_ht100To200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=51541593,
)

cpn.add_dataset(
    name="w_lnu_ht200To400_madgraph",
    id=14196351,
    processes=[procs.w_lnu_ht200To400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=58331446,
)

cpn.add_dataset(
    name="w_lnu_ht400To600_madgraph",
    id=14196599,
    processes=[procs.w_lnu_ht400To600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=7444030,
)


# cpn.add_dataset(
#     name="w_lnu_ht600To800_madgraph",
#     id=14196381,
#     processes=[procs.w_lnu_ht600To800],
#     keys=[
#         "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=5545298,
# )

cpn.add_dataset(
    name="w_lnu_ht800To1200_madgraph",
    id=14195662,
    processes=[procs.w_lnu_ht800To1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=7306187,
)

cpn.add_dataset(
    name="w_lnu_ht1200To2500_madgraph",
    id=14241552,
    processes=[procs.w_lnu_ht1200To2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=6481518,
)


cpn.add_dataset(
    name="w_lnu_ht2500ToInf_madgraph",
    id=14278023,
    processes=[procs.w_lnu_ht2500ToInf],
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

# #
# # EWK
# # (vector boson emissions)
# #

# cpn.add_dataset(
#     name="ewk_wm_lnu_m50_madgraph",
#     id=14301802,
#     processes=[procs.ewk_wm_lnu_m50],
#     keys=[
#         "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=4077000,
# )

# cpn.add_dataset(
#     name="ewk_w_lnu_m50_madgraph",
#     id=14300809,
#     processes=[procs.ewk_wp_lnu_m50],
#     keys=[
#         "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=3595000,
# )

# cpn.add_dataset(
#     name="ewk_z_ll_m50_madgraph",
#     id=14300868,
#     processes=[procs.ewk_z_ll_m50],
#     keys=[
#         "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=579000,
# )


# #
# # Di-boson
# #

# # ZZ

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


cpn.add_dataset(
    name="zz_2q2l_pythia",
    id=14284213,
    processes=[procs.zz_2q2l],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=29357938,
)


cpn.add_dataset(
    name="zz_2l2nu_pythia",
    id=14196326,
    processes=[procs.zz_2l2nu],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=56886000,
)

cpn.add_dataset(
    name="zz_2q2nu_pythia",
    id=14245915,
    processes=[procs.zz_2q2nu],
    keys=[
        "/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=19813764,
)

cpn.add_dataset(
    name="zz_4q_pythia",
    id=14373150,
    processes=[procs.zz_4q],
    keys=[
        "/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2535895,
)

# # cpn.add_dataset(
# #     name="zz_llll_powheg",
# #     id=14243658,
# #     processes=[procs.zz_llll],
# #     keys=[
# #         "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
# #     ],
# #     n_files=109,
# #     n_events=99388000,
# # )

# # WZ


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
    name="wz_3lnu_pythia",
    id=14253723,
    processes=[procs.wz_3lnu],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=9821283,
)


cpn.add_dataset(
    name="wz_2q2l_pythia",
    id=14284121,
    processes=[procs.THE_PROCESS],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=28576996,
)

# # WW
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
    name="ww_1l1nu2q_pythia",
    id=14372963,
    processes=[procs.ww_1l1nu2q],
    keys=[
        "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=40272013,
)

# # cpn.add_dataset(
# #     name="ww_lnulnu_powheg",
# #     id=14241651,
# #     processes=[procs.ww_lnulnu],
# #     keys=[
# #         "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
# #     ],
# #     n_files=46,
# #     n_events=7098000,
# # )


# #
# # Triple-boson
# #

# cpn.add_dataset(
#     name="zzz_amcatnlo",
#     id=14269622,
#     processes=[procs.zzz],
#     keys=[
#         "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=9524000,
# )

# cpn.add_dataset(
#     name="wzz_amcatnlo",
#     id=14240923,
#     processes=[procs.wzz],
#     keys=[
#         "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=9898000,
# )

# cpn.add_dataset(
#     name="wwz_amcatnlo",
#     id=14195642,
#     processes=[procs.wwz],
#     keys=[
#         "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=178000,
# )

# cpn.add_dataset(
#     name="www_amcatnlo",
#     id=14241535,
#     processes=[procs.www],
#     keys=[
#         "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=12,
#     n_events=9854000,
# )
