
# coding: utf-8

""""
Higgs boson datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import run3_2023_postBPix_nano_v12 as cpn

#
# h_ggf
#

cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14920370,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=5549000,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hcc_powheg",
    id=14919069,
    processes=[procs.h_ggf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2C_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=5600000,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_htt_amcatnlo",
#     id=14920389,
#     processes=[procs.h_ggf_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=28,
#             n_events=984768,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_htt_amcatnlo",
    id=15022151,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=3381015,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hgg_powheg",
    id=14929730,
    processes=[procs.h_ggf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToGG_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=976000,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=14945935,
    processes=[procs.h_ggf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=121000,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=14997436,
    processes=[procs.h_ggf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=1697000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=1697000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=1673000,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzg_zll_powheg",
    id=14937484,
    processes=[procs.h_ggf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=329999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=82499,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=82500,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hmm_powheg",
    id=15023297,
    processes=[procs.h_ggf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Mu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=300000,
        ),
    ),
)

#
# h_vbf
#

# cpn.add_dataset(
#     name="h_vbf_htt_powheg",
#     id=14927460,
#     processes=[procs.h_vbf_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=21,
#             n_events=200000,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_vbf_htt_powheg",
#     id=14927786,
#     processes=[procs.h_vbf_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=71,
#             n_events=7065031,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_vbf_hcc_powheg",
    id=14900368,
    processes=[procs.h_vbf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=5585000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14900357,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=5582000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzg_zll_powheg",
    id=14930806,
    processes=[procs.h_vbf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=300000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneUp_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=300000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneDown_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=294000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14998527,
    processes=[procs.h_vbf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=1688000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=1628000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=1697000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4nu_powheg",
    id=14972564,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=497000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4l_powheg",
    id=14942227,
    processes=[procs.h_vbf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4L_M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=125000,
        ),
    ),
)

#
# zh
#

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14902790,
    processes=[procs.zh_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=5556305,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14836898,
    processes=[procs.zh_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=66,
            n_events=5556000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hcc_powheg",
    id=14903170,
    processes=[procs.zh_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=5532000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hcc_powheg",
    id=14904931,
    processes=[procs.zh_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=5592000,
        ),
    ),
)
# cpn.add_dataset(
#     name="zh_htt_powheg",
#     id=14927596,
#     processes=[procs.zh_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=26,
#             n_events=29949,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="zh_htt_powheg",
#     id=14927498,
#     processes=[procs.zh_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/ZHto2TauUncorrelatedDecay_Filtered_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=230,
#             n_events=1009433,
#         ),
#     ),
# )
cpn.add_dataset(
    name="zh_hzz4nu_powheg",
    id=14977774,
    processes=[procs.zh_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2Zto4Nu_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=498838,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14944555,
    processes=[procs.zh_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=1244427,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_powheg",
    id=14932839,
    processes=[procs.zh_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=185745,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=186400,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=187112,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzz_powheg",
    id=14932642,
    processes=[procs.zh_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=153033,
        ),
    ),
)
cpn.add_dataset(
    name="zh_znunu_hbb_powheg",
    id=15023028,
    processes=[procs.zh_znunu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=5508000,
        ),
    ),
)

#
# zh_gg
#

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14900172,
    processes=[procs.zh_gg_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=5568000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14900235,
    processes=[procs.zh_gg_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=5570000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14900310,
    processes=[procs.zh_gg_znunu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=64,
            n_events=5564000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hcc_powheg",
    id=14900000,
    processes=[procs.zh_gg_znunu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=5570000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hcc_powheg",
    id=14900354,
    processes=[procs.zh_gg_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=5585000,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zqq_hcc_powheg",
    id=14900211,
    processes=[procs.zh_gg_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=5582000,
        ),
    ),
)

#
# wph
#

cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14900907,
    processes=[procs.wph_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=253,
            n_events=5536721,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hcc_powheg",
    id=14900903,
    processes=[procs.wph_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=206,
            n_events=5551318,
        ),
    ),
)
# cpn.add_dataset(
#     name="wph_htt_powheg",
#     id=14927431,
#     processes=[procs.wph_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=2,
#             n_events=30000,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="wph_htt_powheg",
#     id=14926515,
#     processes=[procs.wph_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WplusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=28,
#             n_events=1015644,
#         ),
#     ),
# )
cpn.add_dataset(
    name="wph_wqq_hcc_powheg",
    id=14901084,
    processes=[procs.wph_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=211,
            n_events=5538310,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14915195,
    processes=[procs.wph_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=5497144,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_zll_powheg",
    id=14940743,
    processes=[procs.wph_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=239513,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=59997,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=58162,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hzz4nu_powheg",
    id=14973544,
    processes=[procs.wph_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=499988,
        ),
    ),
)

#
# wmh
#

cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14904895,
    processes=[procs.wmh_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=174,
            n_events=5398979,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hbb_powheg",
    id=14901030,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=156,
            n_events=5547273,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=14838225,
    processes=[procs.wmh_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=250,
            n_events=5568160,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=14904999,
    processes=[procs.wmh_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=228,
            n_events=5542812,
        ),
    ),
)
# cpn.add_dataset(
#     name="wmh_htt_powheg",
#     id=14927422,
#     processes=[procs.wmh_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=1,
#             n_events=30000,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="wmh_htt_powheg",
#     id=14927570,
#     processes=[procs.wmh_htt],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WminusHTo2TauUncorrelatedDecay_Filtered_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=20,
#             n_events=753115,
#         ),
#     ),
# )
cpn.add_dataset(
    name="wmh_wqq_hzz4nu_powheg",
    id=14973628,
    processes=[procs.wmh_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=499986,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hzg_zll_powheg",
    id=14932830,
    processes=[procs.wmh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=418162,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=103015,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=104999,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hmm_powheg",
    id=15023009,
    processes=[procs.wmh_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Mu_WtoAll_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=116000,
        ),
    ),
)

#
# tth
#

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14920188,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=138,
            n_events=5887987,
        ),
    ),
)
# cpn.add_dataset(
#     name="tth_hnonbb_1j_amcatnlo",
#     id=14918806,
#     processes=[procs.tth_hnonbb_1j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=140,
#             n_events=5595534,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hcc_powheg",
    id=14900092,
    processes=[procs.tth_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=5537000,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14900362,
    processes=[procs.tth_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=5576000,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hzz_powheg",
    id=14943407,
    processes=[procs.tth_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=116569,
        ),
    ),
)
