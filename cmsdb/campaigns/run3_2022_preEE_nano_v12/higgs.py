# coding: utf-8

"""
Higgs datasets for the 2022preEE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Single Higgs
#

####################################################################################################
#
# h_ggf
#
####################################################################################################

# cpn.add_dataset(
#     name="h_ggf_hbb_pt200toinf_powheg",
#     id=14801316,
#     processes=[procs.h_ggf_hbb_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=29,
#             n_events=59480,
#         ),
#         extension=DatasetInfo(
#             keys=[
#                 "/GluGluHto2B_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=291,
#             n_events=4324232,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hcc_pt200toinf_powheg",
#     id=14797543,
#     processes=[procs.h_ggf_hcc_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHtoCC_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=20,
#             n_events=122144,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hgg_amcatnlo",
    id=14805985,
    processes=[procs.h_ggf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=933797,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=14796087,
    processes=[procs.h_ggf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=486643,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzg_zll_powheg",
    id=14797462,
    processes=[procs.h_ggf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=55000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=55000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHtoZG_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=54999,
        ),
    ),
)
# NOTE: there are also htt samples with *UncorrelatedDecay* in the DAS name. They are not considered here.
cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=14805667,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=295722,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=14876200,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=4353624,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=14849365,
    processes=[procs.h_ggf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=1494981,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=1494981,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=1497196,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hzz4nu_powheg",
    id=14849342,
    processes=[procs.h_ggf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Zto4Nu_PT-150_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=1014208,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_hcc_powheg",
    id=14877479,
    processes=[procs.h_ggf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2C_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=4371062,
        ),
    ),
)
cpn.add_dataset(
    name="h_ggf_htt_amcatnlo",
    id=14849328,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Tau_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=1038456,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_ggf_hcc_pt200toinf_powheg",
#     id=14852276,
#     processes=[procs.h_ggf_hcc_pt200toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2C_PT-200_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=319,
#             n_events=4322480,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hee_amcatnlo",
#     id=14947996,
#     processes=[procs.h_ggf_hee],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHto2E_M-125_TuneCP5_13p6TeV_amcatnloFxFx-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=65,
#             n_events=881432,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="h_ggf_hzz4l_ew0_powheg",
#     id=14950668,
#     processes=[procs.h_ggf_hzz4l_ew0],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/GluGluHtoZZto4L_ew0_M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=20,
#             n_events=100000,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_ggf_hmm_powheg",
    id=14868421,
    processes=[procs.h_ggf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Mu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=200000,
        ),
    ),
)

####################################################################################################
#
# h_vbf
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_hzg_zll_powheg",
    id=14798046,
    processes=[procs.h_vbf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=12000,
        ),
        with_dipole_recoil=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_TuneCP5_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=4,
            n_events=96465,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneUp_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=98582,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHtoZG_Zto2L_M-125_CP5TuneDown_withDipoleRecoil_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=96480,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=14849334,
    processes=[procs.h_vbf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=1497840,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Up_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=1498588,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_M-125_TuneCP5Down_13p6TeV_powheg-jhugen752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=1497840,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hzz4nu_powheg",
    id=14849329,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=500000,
        ),
    ),
)
# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=14926213,
    processes=[procs.h_vbf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=100000,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hgg_amcatnlo",
    id=14885189,
    processes=[procs.h_vbf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHtoGG_M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=314360,
        ),
    ),
)
cpn.add_dataset(
    name="h_vbf_hcc_powheg",
    id=14853086,
    processes=[procs.h_vbf_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=119,
            n_events=4348092,
        ),
    ),
)
# cpn.add_dataset(
#     name="h_vbf_hcc_powheg",
#     id=14788422,
#     processes=[procs.h_vbf_hcc],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/VBFHToCC_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-FlatPU0to70_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=1,
#             n_events=300000,
#         ),
#     ),
# )
cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=14870810,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=3330700,
        ),
        dipole_recoil_on=DatasetInfo(
            keys=[
                "/VBFHto2B_M-125_dipoleRecoilOn_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=948700,
        ),
    ),
)

####################################################################################################
#
# zh
#
####################################################################################################

cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=14805167,
    processes=[procs.zh_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=1144560,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=3177722,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_powheg",
    id=14794187,
    processes=[procs.zh_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_HtoZG_ZtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=124384,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=14805378,
    processes=[procs.zh_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=599100,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=4339792,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zll_hcc_powheg",
    id=14800392,
    processes=[procs.zh_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=799380,
        ),
        extension=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=4153800,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_powheg",
    id=14849422,
    processes=[procs.zh_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2Zto4Nu_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=70,
            n_events=497369,
        ),
    ),
)
# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="zh_htt_powheg",
    id=14927154,
    processes=[procs.zh_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZHto2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=28752,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hww2l2nu_powheg",
    id=14918311,
    processes=[procs.zh_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_Hto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-minlo-HZJ-jhugenv752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=963869,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hzg_zll_powheg",
    id=14885110,
    processes=[procs.zh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=124660,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=124656,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ZH_ZtoAll_HtoZGto2LG_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=124659,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hcc_powheg",
    id=14868489,
    processes=[procs.zh_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=64,
            n_events=3101694,
        ),
    ),
)
cpn.add_dataset(
    name="zh_hmm_powheg",
    id=14863423,
    processes=[procs.zh_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH_Hto2Mu_ZtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=196974,
        ),
    ),
)

####################################################################################################
#
# zh_gg
#
####################################################################################################

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=14804331,
    processes=[procs.zh_gg_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=578672,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=3782022,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=14803231,
    processes=[procs.zh_gg_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=582250,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=3780820,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=14805533,
    processes=[procs.zh_gg_znunu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=581016,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2B_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=3784521,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zll_hcc_powheg",
    id=14803676,
    processes=[procs.zh_gg_zll_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=773402,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=3588800,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_znunu_hcc_powheg",
    id=14846449,
    processes=[procs.zh_gg_znunu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Nu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=797924,
        ),
        extension=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=3593320,
        ),
    ),
)
cpn.add_dataset(
    name="zh_gg_zqq_hcc_powheg",
    id=14853067,
    processes=[procs.zh_gg_zqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ggZH_Hto2C_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=4391804,
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
    id=14793663,
    processes=[procs.wmh_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Zto4L_M-125_TuneCP5_13p6TeV_powheg2-minlo-HWJ-JHUGenV752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=491969,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=14805882,
    processes=[procs.wmh_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=590044,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=169,
            n_events=4399854,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=14801338,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=1147965,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=223,
            n_events=3153199,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hcc_powheg",
    id=14804815,
    processes=[procs.wmh_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=732400,
        ),
    ),
)
# NOTE: this sample includes the *UncorrelatedDecay* tag. No htt dataset without this tag has been found on 07.06.2024
cpn.add_dataset(
    name="wmh_powheg",
    id=14926126,
    processes=[procs.wmh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=30000,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hcc_powheg",
    id=14852474,
    processes=[procs.wmh_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=321,
            n_events=4357249,
        ),
        extension=DatasetInfo(
            keys=[
                "/WminusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=147,
            n_events=4200000,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hzz4nu_powheg",
    id=14849469,
    processes=[procs.wmh_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=497364,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hzg_zll_powheg",
    id=14826664,
    processes=[procs.wmh_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=53961,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=70000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WminusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=69801,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hmm_powheg",
    id=14856644,
    processes=[procs.wmh_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH_Hto2Mu_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=120000,
        ),
    ),
)

####################################################################################################
#
# WplusH
#
####################################################################################################

cpn.add_dataset(
    name="wph_htt_powheg",
    id=14925460,
    processes=[procs.wph_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-minnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=30000,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=14810156,
    processes=[procs.wph_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=1199214,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=147,
            n_events=3179822,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=14804043,
    processes=[procs.wph_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=565746,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=159,
            n_events=4206261,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hcc_powheg",
    id=14852349,
    processes=[procs.wph_wqq_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=271,
            n_events=4369883,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wlnu_hcc_powheg",
    id=14795238,
    processes=[procs.wph_wlnu_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=754430,
        ),
        extension=DatasetInfo(
            keys=[
                "/WplusH_Hto2C_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=4200000,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hmm_powheg",
    id=14868497,
    processes=[procs.wph_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2Mu_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=118804,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzz4l_powheg",
    id=14810120,
    processes=[procs.wph_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_Hto2Zto4L_M-125_TuneCP5_13p6TeV_powheg2-minlo-HWJ-JHUGenV752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=492605,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_powheg",
    id=14798660,
    processes=[procs.wph_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=38162,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneDown_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=39616,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_CP5TuneUp_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=39997,
        ),
    ),
)
cpn.add_dataset(
    name="wph_hzg_zll_powheg",
    id=14792521,
    processes=[procs.wph_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH_HtoZG_WtoAll_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=156824,
        ),
    ),
)
cpn.add_dataset(
    name="wph_wqq_hzz4nu_powheg",
    id=14849415,
    processes=[procs.wph_wqq_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusHto2Zto4Nu_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=495938,
        ),
    ),
)


####################################################################################################
#
# ttH
#
####################################################################################################

# cpn.add_dataset(
#     name="tth_hzz_powheg",
#     id=14793299,
#     processes=[procs.tth_hzz],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTH_Hto2Z_M-125_4LFilter_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=20,
#             n_events=96720,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hzz_powheg",
    id=14952169,
    processes=[procs.tth_hzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Z_4LFilter_M-125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=95869,
        ),
    ),
)
# cpn.add_dataset(
#     name="tth_hnonbb_1j_amcatnlo",
#     id=14852673,
#     processes=[procs.tth_hnonbb_1j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTHtoNon2B-1Jets_M-125_TuneCP5_13p6TeV_amcatnloFXFX-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=165,
#             n_events=6303497,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=14849153,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=3846525,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hcc_powheg",
    id=14870558,
    processes=[procs.tth_hcc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2C_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=3184328,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hbb_powheg",
    id=14857767,
    processes=[procs.tth_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=3177628,
        ),
    ),
)
# cpn.add_dataset(
#     name="tth_hbb_powheg",
#     id=14870504,
#     processes=[procs.tth_hbb],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=43,
#             n_events=2989710,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tth_hmm_powheg",
    id=14868415,
    processes=[procs.tth_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH_Hto2Mu_M-125_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=197248,
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
    id=14861662,
    processes=[procs.ttz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=798996,
        ),
    ),
)

cpn.add_dataset(
    name="ttwh_madgraph",
    id=14860507,
    processes=[procs.ttwh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=790196,
        ),
    ),
)
