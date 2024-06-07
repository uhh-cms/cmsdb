# coding: utf-8

"""
Higgs datasets for the 2022postEE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# Single Higgs
#

####################################################################################################
#
# ggH
#
####################################################################################################

# cpn.add_dataset(
#     name="h_ggf_hbb_pt200toinf_powheg",
#     id=14805810,
#     processes=[procs.h_ggf_hbb_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=32,
#             n_events=207945,
#         ),
#         extension=DatasetInfo(
#             keys=[
#                 "/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=355,
#             n_events=15058774,
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hcc_pt200toinf_powheg",
#     id=14798441,
#     processes=[procs.h_ggf_hcc_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHtoCC_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=36,
#             n_events=359490,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hgg_amcatnlo",
    id=14796528,
    processes=[procs.h_ggf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=3174151,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=14793399,
    processes=[procs.h_ggf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=1666666,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzg_zll_powheg",
    id=14796430,
    processes=[procs.h_ggf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=199278,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=196495,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=199301,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14876616,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=135,
            n_events=15489920,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=14849369,
    processes=[procs.h_ggf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=93,
            n_events=4980263,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=95,
            n_events=4987292,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=4982312,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4nu_pt150toinf_powheg",
    id=14849364,
    processes=[procs.h_ggf_hzz4nu_pt150toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Zto4Nu_PT-150_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=3734036,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hcc_powheg",
    id=14872560,
    processes=[procs.h_ggf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2C_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=134,
            n_events=15481839,
        ),
    ),
)
# NOTE: there are also htt samples with *UncorrelatedDecay* in the DAS name. They are not considered here.
cpn.add_dataset(
    name="h_ggf_htt_amcatnlo",
    id=14849353,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=3533459,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_hcc_pt200toinf_powheg",
#     id=14851872,
#     processes=[procs.h_ggf_hcc_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2C_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=696,
#             n_events=15117536,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hee_amcatnlo",
#     id=14948781,
#     processes=[procs.h_ggf_hee],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2E_M-125_TuneCP5_13p6TeV_amcatnloFxFx-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=115,
#             n_events=3055389,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hmm_powheg",
    id=14850119,
    processes=[procs.h_ggf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Mu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=1,
            n_events=691000,
        ),
    ),
)

####################################################################################################
#
# qqH
#
####################################################################################################

# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14927452,
    processes=[procs.h_vbf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=397268,
        ),
    ),
)

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14857769,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=131,
            n_events=12246336,
        ),
        dipole_recoil_on=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_dipoleRecoilOn_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=3180348,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hcc_powheg",
    id=14870678,
    processes=[procs.h_vbf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=140,
            n_events=15542540,
        ),
    ),
)

cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14849309,
    processes=[procs.h_vbf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=4987403,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=4984705,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=4978912,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4nu_powheg",
    id=14849347,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=1743925,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hgg_amcatnlo",
    id=14802334,
    processes=[procs.h_vbf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoGG_M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=1799500,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneDown_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=350000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneUp_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=349296,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzg_zll_powheg",
    id=14800564,
    processes=[procs.h_vbf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=50000,
        ),
        with_dipole_recoil=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=345734,
        ),
    ),
)

####################################################################################################
#
# ZH
#
####################################################################################################

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14790777,
    processes=[procs.zh_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=4090842,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=136,
            n_events=11353020,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_powheg",
    id=14796033,
    processes=[procs.zh_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_HtoZG_ZtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=424143,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14802579,
    processes=[procs.zh_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=2062940,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=236,
            n_events=12923375,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hcc_powheg",
    id=14792528,
    processes=[procs.zh_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=2955696,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hll4nu_powheg",
    id=14849385,
    processes=[procs.zh_zqq_hll4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2Zto4Nu_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=1746525,
        ),
    ),
)

cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14918165,
    processes=[procs.zh_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=3499224,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_zll_powheg",
    id=14885107,
    processes=[procs.zh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=424006,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=134,
            n_events=422599,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=142,
            n_events=420688,
        ),
    ),
)

cpn.add_dataset(
    name="zh_zqq_hcc_powheg",
    id=14868436,
    processes=[procs.zh_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=15467517,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=248,
            n_events=11811488,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hmm_powheg",
    id=14861719,
    processes=[procs.zh_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2Mu_ZtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=110,
            n_events=690584,
        ),
    ),
)
# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927555,
    processes=[procs.zh_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=69650,
        ),
    ),
)

####################################################################################################
#
# zh_gg
#
####################################################################################################

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14800335,
    processes=[procs.zh_gg_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=2068050,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=153,
            n_events=13417872,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14805763,
    processes=[procs.zh_gg_znunu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=2012538,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=144,
            n_events=13450930,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14798128,
    processes=[procs.zh_gg_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=1995576,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=251,
            n_events=13393120,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hcc_powheg",
    id=14793916,
    processes=[procs.zh_gg_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=2901759,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=12308985,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hcc_powheg",
    id=14802049,
    processes=[procs.zh_gg_znunu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=70,
            n_events=2934525,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=93,
            n_events=12576235,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zqq_hcc_powheg",
    id=14870624,
    processes=[procs.zh_gg_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=135,
            n_events=15549976,
        ),
    ),
)

####################################################################################################
#
# WplusH
#
####################################################################################################

# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="wph_htt_powheg",
    id=14925742,
    processes=[procs.wph_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=70000,
        ),
    ),
)
cpn.add_dataset(
    name="wph_zqq_hbb_powheg",
    id=14810685,
    processes=[procs.wph_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=4085059,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=481,
            n_events=11334593,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14805180,
    processes=[procs.wph_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=2120400,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=306,
            n_events=12788758,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hcc_powheg",
    id=14852306,
    processes=[procs.wph_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=531,
            n_events=15514030,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hcc_powheg",
    id=14792459,
    processes=[procs.wph_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=2926870,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=365,
            n_events=11934720,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hmm_powheg",
    id=14872544,
    processes=[procs.wph_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2Mu_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=417345,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzz4l_powheg",
    id=14793772,
    processes=[procs.wph_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2Zto4L_M-125_TuneCP5_13p6TeV_powheg2-minlo-HWJ-JHUGenV752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=1691511,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_powheg",
    id=14802027,
    processes=[procs.wph_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=138428,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_zll_powheg",
    id=14844999,
    processes=[procs.wph_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=537606,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=139061,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=139225,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hzz4nu_powheg",
    id=14849411,
    processes=[procs.wph_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=1742996,
        ),
    ),
)

####################################################################################################
#
# WminusH
#
####################################################################################################

cpn.add_dataset(
    name="wmh_hzz4l_powheg",
    id=14796284,
    processes=[procs.wmh_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Zto4L_M-125_TuneCP5_13p6TeV_powheg2-minlo-HWJ-JHUGenV752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=1688428,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnhbb_u_powheg",
    id=14799662,
    processes=[procs.wmh_wlnhbb_u],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=2027956,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=340,
            n_events=12999904,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14801501,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=4003343,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=309,
            n_events=11304506,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hzz4l_powheg",
    id=14799041,
    processes=[procs.wmh_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Zto4L_M-125p5_TuneCP5_13p6TeV_powheg2-minlo-HWJ-JHUGenV752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=1730541,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hzg_zll_powheg",
    id=14793565,
    processes=[procs.wmh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=235813,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=238880,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=91,
            n_events=238177,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=14798000,
    processes=[procs.wmh_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=121,
            n_events=2993794,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=557,
            n_events=11901295,
        ),
    ),
)
# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="wmh_htt_powheg",
    id=14925240,
    processes=[procs.wmh_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=67580,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=14852324,
    processes=[procs.wmh_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=529,
            n_events=15485820,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_powheg",
    id=14958828,
    processes=[procs.wmh_wqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=1746566,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hmm_powheg",
    id=14868377,
    processes=[procs.wmh_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Mu_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=420000,
        ),
    ),
)


####################################################################################################
#
# ttH
#
####################################################################################################

# cpn.add_dataset(
#     name="tth_hbb_powheg",
#     id=14870747,
#     processes=[procs.tth_hbb],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=85,
#             n_events=10478951,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14868530,
    processes=[procs.tth_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=134,
            n_events=11099294,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hmm_powheg",
    id=14867977,
    processes=[procs.tth_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Mu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=699316,
        ),
    ),
)
# cpn.add_dataset(
#     name="tth_hzz_powheg",
#     id=14951667,
#     processes=[procs.tth_hzz],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=30,
#             n_events=298293,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hzz_powheg",
    id=14793353,
    processes=[procs.tth_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Z_M-125_4LFilter_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=341864,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hcc_powheg",
    id=14870594,
    processes=[procs.tth_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=11355120,
        ),
    ),
)
# cpn.add_dataset(
#     name="tth_hnonbb_1j_amcatnlo",
#     id=14852415,
#     processes=[procs.tth_hnonbb_1j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=320,
#             n_events=22107915,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14845759,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=122,
            n_events=13955780,
        ),
    ),
)

####################################################################################################
#
# ttVH
#
####################################################################################################

cpn.add_dataset(
    name="ttzh_madgraph",
    id=14861698,
    processes=[procs.ttzh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=2785771,
        ),
    ),
)
cpn.add_dataset(
    name="ttwh_madgraph",
    id=14855650,
    processes=[procs.ttwh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=2800000,
        ),
    ),
)
