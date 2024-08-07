# coding: utf-8

"""
Higgs datasets for the 2023preBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

####################################################################################################
#
# ggH
#
####################################################################################################

cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14920360,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=10974000,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_hbb_pt200toinf_powheg",
#     id=14908055,
#     processes=[procs.h_ggf_hbb_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=413,
#             n_events=10731692,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hinv_pt150toinf_powheg",
#     id=14920411,
#     processes=[procs.h_ggf_hinv_pt150toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHtoInv_PT-150_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=44,
#             n_events=1876392,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hcc_powheg",
    id=14920368,
    processes=[procs.h_ggf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2C_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=78,
            n_events=10938000,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_hcc_pt200toinf_powheg",
#     id=14909953,
#     processes=[procs.h_ggf_hcc_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2C_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=383,
#             n_events=10654050,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_htt_amcatnlo",
    id=14920472,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=1975609,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=14932450,
    processes=[procs.h_ggf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=250000,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_hzz4nu_pt150toinf_powheg",
#     id=14972533,
#     processes=[procs.h_ggf_hzz4nu_pt150toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2Zto4Nu_PT-150_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=54,
#             n_events=1997461,
#         ),
#     ),
# )

# # TODO: nominal dataset missing in DAS
# cpn.add_dataset(
#     name="h_ggf_hww2l2nu_powheg",
#     id=-1,
#     processes=[procs.h_ggf_hww2l2nu],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=-1,
#             n_events=-1,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=68,
#             n_events=3500000,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=59,
#             n_events=3449000,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hzg_zll_powheg",
    id=14932639,
    processes=[procs.h_ggf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=655998,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=165000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=165000,
        ),
    ),
)

####################################################################################################
#
# qqH
#
####################################################################################################


cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14900094,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=121,
            n_events=11049000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hcc_powheg",
    id=14915170,
    processes=[procs.h_vbf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=125,
            n_events=10956000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4l_powheg",
    id=14942235,
    processes=[procs.h_vbf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4L_M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=250000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4nu_powheg",
    id=14972668,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=1000000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14998531,
    processes=[procs.h_vbf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=3491000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=3476000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=3455000,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_vbf_hinv_powheg",
#     id=14920337,
#     processes=[procs.h_vbf_hinv],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHtoInv_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=34,
#             n_events=994000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="h_vbf_hzg_zll_powheg",
    id=14930292,
    processes=[procs.h_vbf_hzg_zll],
    info=dict(
        # NOTE: datasets contain *withDiopoleRecoil* tag
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=141000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneUp_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=144000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneDown_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=150000,
        ),
    ),
)

####################################################################################################
#
# ZH
#
####################################################################################################

cpn.add_dataset(
    name="zh_zqq_hzz4nu_powheg",
    id=14976992,
    processes=[procs.zh_zqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2Zto4Nu_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=995967,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14900724,
    processes=[procs.zh_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=216,
            n_events=11060000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14838001,
    processes=[procs.zh_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=202,
            n_events=10925000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hcc_powheg",
    id=14904027,
    processes=[procs.zh_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=120,
            n_events=10776000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hcc_powheg",
    id=14900900,
    processes=[procs.zh_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=199,
            n_events=10984000,
        ),
    ),
)

# TODO: what does the 4l filter mean?
cpn.add_dataset(
    name="zh_hzz_powheg",
    id=14931626,
    processes=[procs.zh_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=289848,
        ),
    ),
)

# NOTE: contains the *UncorrelatedDecay* tag, no datasets without it available
cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927610,
    processes=[procs.zh_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=67552,
        ),
    ),
)
# cpn.add_dataset(
#     name="zh_htt_powheg",
#     id=14927389,
#     processes=[procs.zh_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/ZHto2TauUncorrelatedDecay_Filtered_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=268,
#             n_events=1789875,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="zh_hinv_zqq_powheg",
#     id=14919537,
#     processes=[procs.zh_hinv_zqq],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/ZHtoInv_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=266,
#             n_events=989610,
#         ),
#     ),
# )
cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14939880,
    processes=[procs.zh_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=2486319,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_powheg",
    id=14932785,
    processes=[procs.zh_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=85,
            n_events=374457,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=95,
            n_events=371157,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=374136,
        ),
    ),
)

####################################################################################################
#
# ggZH
#
####################################################################################################


cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14900023,
    processes=[procs.zh_gg_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=106,
            n_events=11056000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14900026,
    processes=[procs.zh_gg_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=143,
            n_events=11066000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14845360,
    processes=[procs.zh_gg_znunu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=10848000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hcc_powheg",
    id=14917018,
    processes=[procs.zh_gg_znunu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=10692000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hcc_powheg",
    id=14915168,
    processes=[procs.zh_gg_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=11030000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zqq_hcc_powheg",
    id=14900318,
    processes=[procs.zh_gg_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=11056000,
        ),
    ),
)

####################################################################################################
#
# WplusH
#
####################################################################################################


cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14845624,
    processes=[procs.wph_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=369,
            n_events=10997744,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14900236,
    processes=[procs.wph_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=381,
            n_events=11031056,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hcc_powheg",
    id=14903434,
    processes=[procs.wph_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=369,
            n_events=10874444,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hcc_powheg",
    id=14904332,
    processes=[procs.wph_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=666,
            n_events=11008206,
        ),
    ),
)
# cpn.add_dataset(
#     name="wph_hinv_wqq_powheg",
#     id=14919241,
#     processes=[procs.wph_hinv_wqq],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WplusHtoInv_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=44,
#             n_events=997978,
#         ),
#     ),
# )
# NOTE: contains the *UncorrelatedDecay* tag, no datasets without it available
cpn.add_dataset(
    name="wph_htt_powheg",
    id=14927461,
    processes=[procs.wph_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=68000,
        ),
    ),
)
# cpn.add_dataset(
#     name="wph_htt_powheg",
#     id=14927100,
#     processes=[procs.wph_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WplusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=25,
#             n_events=1887577,
#         ),
#     ),
# )
cpn.add_dataset(
    name="wph_wqq_hzz4nu_powheg",
    id=14973548,
    processes=[procs.wph_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=999977,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_zll_powheg",
    id=14932801,
    processes=[procs.wph_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=470720,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=119995,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=119996,
        ),
    ),
)

####################################################################################################
#
# WminusH
#
####################################################################################################


cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14905191,
    processes=[procs.wmh_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=349,
            n_events=10890938,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14900874,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=404,
            n_events=11040960,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=14901004,
    processes=[procs.wmh_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=321,
            n_events=11011056,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=14900875,
    processes=[procs.wmh_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=326,
            n_events=11046549,
        ),
    ),
)
# cpn.add_dataset(
#     name="wmh_hinv_wqq_powheg",
#     id=14922048,
#     processes=[procs.wmh_hinv_wqq],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WminusHtoInv_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=27,
#             n_events=987977,
#         ),
#     ),
# )
# NOTE: contains the *UncorrelatedDecay* tag, no datasets without it available
cpn.add_dataset(
    name="wmh_powheg",
    id=14927427,
    processes=[procs.wmh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=1,
            n_events=70000,
        ),
    ),
)
# cpn.add_dataset(
#     name="wmh_powheg",
#     id=14927577,
#     processes=[procs.wmh],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WminusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=38,
#             n_events=1290200,
#         ),
#     ),
# )
cpn.add_dataset(
    name="wmh_wqq_hzz4nu_powheg",
    id=14972839,
    processes=[procs.wmh_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=999978,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hzg_zll_powheg",
    id=14932805,
    processes=[procs.wmh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=837298,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=202843,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=208636,
        ),
    ),
)

####################################################################################################
#
# TTH
#
####################################################################################################

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14901069,
    processes=[procs.tth_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=131,
            n_events=10846000,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hcc_powheg",
    id=14913830,
    processes=[procs.tth_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=10884000,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14919222,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=236,
            n_events=11901980,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hnonbb_amcatnlo",
    id=14920051,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=161,
            n_events=11083178,
        ),
    ),
)
# TODO: what does the 4l filter mean?
cpn.add_dataset(
    name="tth_hzz_powheg",
    id=14931825,
    processes=[procs.tth_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=239674,
        ),
    ),
)

####################################################################################################
#
# TTWH, TTZH
#
####################################################################################################


cpn.add_dataset(
    name="ttwh_madgraph",
    id=14940785,
    processes=[procs.ttwh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=1960000,
        ),
    ),
)
cpn.add_dataset(
    name="ttzh_madgraph",
    id=14937478,
    processes=[procs.ttzh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=1993000,
        ),
    ),
)
