# coding: utf-8


"""Electroweak datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH."""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn

# EWK

cpn.add_dataset(
    name="ewk_wm_lnu_m50toinf_madgraph",
    id=14217420,
    processes=[procs.ewk_wm_lnu_m50toinf],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=2_248_000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50toinf_madgraph",
    id=14216470,
    processes=[procs.ewk_wp_lnu_m50toinf],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=2_185_000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50toinf_madgraph",
    id=14214791,
    processes=[procs.ewk_z_ll_m50toinf],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=500_000,
)

# DY

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14212297,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=980,
    n_events=90_947_213,
)

cpn.add_dataset(
    name="dy_0j_amcatnlo",
    id=14212804,
    processes=[procs.dy_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=882,
    n_events=79_751_592,
)

cpn.add_dataset(
    name="dy_1j_amcatnlo",
    id=14238480,
    processes=[procs.dy_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=907,
    n_events=88_364_975,
)

cpn.add_dataset(
    name="dy_2j_amcatnlo",
    id=14212211,
    processes=[procs.dy_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=669,
    n_events=42_948_118,
)

cpn.add_dataset(
    name="dy_pt0to50_amcatnlo",
    id=14339864,
    processes=[procs.dy_pt0to50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=2_335,
    n_events=101_338_633,
)

cpn.add_dataset(
    name="dy_pt50to100_amcatnlo",
    id=14335914,
    processes=[procs.dy_pt50to100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1_762,
    n_events=60_848_787,
)

cpn.add_dataset(
    name="dy_pt100to250_amcatnlo",
    id=14342843,
    processes=[procs.dy_pt100to250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1_273,
    n_events=40_115_413,
)

cpn.add_dataset(
    name="dy_pt250to400_amcatnlo",
    id=14346965,
    processes=[procs.dy_pt250to400],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=356,
    n_events=12_085_183,
)

cpn.add_dataset(
    name="dy_pt400to650_amcatnlo",
    id=14350490,
    processes=[procs.dy_pt400to650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=79,
    n_events=1_993_002,
)

cpn.add_dataset(
    name="dy_pt650toinf_amcatnlo",
    id=14349654,
    processes=[procs.dy_pt650toinf],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=1_999_583,
)


# multi boson

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14215019,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=98,
    n_events=5_302_000,
)

# cpn.add_dataset(
#     name="zzz_ext_amcatnlo",
#     id=14215019,
#     processes=[procs.zzz],
#     keys=[
#         "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=5302000,
# )

cpn.add_dataset(
    name="ww_pythia",
    id=14214902,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=185,
    n_events=15_859_000,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14214976,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=103,
    n_events=7_934_000,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14214813,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=1_282_000,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id=14215136,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=5_190_000,
)

# cpn.add_dataset(
#     name="www_ext_amcatnlo",
#     id=14215136,
#     processes=[procs.www],
#     keys=[
#         "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=5190000,
# )


cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14214901,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=85,
    n_events=5_394_000,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14214960,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=83,
    n_events=5_072_000,
)

# W

cpn.add_dataset(
    name="w_lnu_madgraph",
    id=14270880,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=859,
    n_events=74_676_454,
)


cpn.add_dataset(
    name="w_lnu_ht70to100_madgraph",
    id=14300594,
    processes=[procs.w_lnu_ht70to100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=225,
    n_events=16_931_765,
)

cpn.add_dataset(
    name="w_lnu_ht100to200_madgraph",
    id=14221276,
    processes=[procs.w_lnu_ht100to200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=328,
    n_events=21_734_530,
)

cpn.add_dataset(
    name="w_lnu_ht200to400_madgraph",
    id=14212310,
    processes=[procs.w_lnu_ht200to400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=283,
    n_events=17_870_845,
)

cpn.add_dataset(
    name="w_lnu_ht400to600_madgraph",
    id=14213493,
    processes=[procs.w_lnu_ht400to600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=2_467_498,
)

cpn.add_dataset(
    name="w_lnu_ht600to800_madgraph",
    id=14227116,
    processes=[procs.w_lnu_ht600to800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=2_344_130,
)

cpn.add_dataset(
    name="w_lnu_ht800to1200_madgraph",
    id=14212489,
    processes=[procs.w_lnu_ht800to1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=96,
    n_events=2_510_487,
)


cpn.add_dataset(
    name="w_lnu_ht1200to2500_madgraph",
    id=14226935,
    processes=[procs.w_lnu_ht1200to2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=2_119_975,
)

cpn.add_dataset(
    name="w_lnu_ht2500toinf_madgraph",
    id=14266888,
    processes=[procs.w_lnu_ht2500toinf],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=808_649,
)

# Z

# cpn.add_dataset(
#     name="z_nunu_ht100to200_madgraph",
#     id=14212946,
#     processes=[procs.z_nunu_ht100to200],
#     keys=[
#         "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=7784090,
# )

# cpn.add_dataset(
#     name="z_nunu_ht200to400_madgraph",
#     id=14216548,
#     processes=[procs.z_nunu_ht200to400],
#     keys=[
#         "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=7531529,
# )

# cpn.add_dataset(
#     name="z_nunu_ht400to600_madgraph",
#     id=14238470,
#     processes=[procs.z_nunu_ht400to600],
#     keys=[
#         "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=6632524,
# )

# cpn.add_dataset(
#     name="z_nunu_ht600to800_madgraph",
#     id=14238483,
#     processes=[procs.z_nunu_ht600to800],
#     keys=[
#         "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=2030858,
# )

# cpn.add_dataset(
#     name="z_nunu_ht800to1200_madgraph",
#     id=14285553,
#     processes=[procs.z_nunu_ht800to1200],
#     keys=[
#         "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=703970,
# )

# cpn.add_dataset(
#     name="z_nunu_ht1200to2500_madgraph",
#     id=14240780,
#     processes=[procs.z_nunu_ht1200to2500],
#     keys=[
#         "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=136393,
# )

# cpn.add_dataset(
#     name="z_nunu_ht2500toinf_madgraph",
#     id=14242842,
#     processes=[procs.z_nunu_ht2500toinf],
#     keys=[
#         "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=111838,
# )

# cpn.add_dataset(
#     name="z_qq_ht200to400_madgraph",
#     id=14303395,
#     processes=[procs.z_qq_ht200to400],
#     keys=[
#         "/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=8753905,
# )

# cpn.add_dataset(
#     name="z_qq_ht400to600_madgraph",
#     id=14284977,
#     processes=[procs.z_qq_ht400to600],
#     keys=[
#         "/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=7709128,
# )

# cpn.add_dataset(
#     name="z_qq_ht600to800_madgraph",
#     id=14275517,
#     processes=[procs.z_qq_ht600to800],
#     keys=[
#         "/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=6116617,
# )

# cpn.add_dataset(
#     name="z_qq_ht800toinf_madgraph",
#     id=14305027,
#     processes=[procs.z_qq_ht800toinf],
#     keys=[
#         "/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=3726992,
# )
