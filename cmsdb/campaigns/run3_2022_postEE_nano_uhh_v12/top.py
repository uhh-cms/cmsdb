# coding: utf-8

"""
Top quark related datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn  # noqa


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14797557,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=512 + 518,
            n_events=268_023_449 + 275_487_429,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=191,
            n_events=105_851_436,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=197,
            n_events=109_097_160,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=204,
            n_events=106_511_300,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=213,
            n_events=109_246_944,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=199,
            n_events=108_074_523,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=215,
            n_events=108_290_720,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 9,
            "nominal_ext1": 17,
            "hdamp_down": 10,
            "hdamp_up": 10,
            "mtop_down": 9,
            "mtop_up": 9,
            "tune_down": 10,
            "tune_up": 12,
        },
    },
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14790677,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=158 + 154,
            n_events=84_809_345 + 84_925_614,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=33_491_099,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=33_747_584,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=34_555_001,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=64,
            n_events=34_985_006,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=33_074_645,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=34_184_038,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 10,
            "nominal_ext1": 19,
            "hdamp_down": 11,
            "hdamp_up": 10,
            "mtop_down": 10,
            "mtop_up": 13,
            "tune_down": 12,
            "tune_up": 10,
        },
    },
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14802625,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=333 + 369,
            n_events=179_665_017 + 187_547_263,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=161,
            n_events=79_769_032,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=143,
            n_events=73_609_756,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=143,
            n_events=73_856_893,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=146,
            n_events=76_754_456,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=152,
            n_events=75_122_008,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=146,
            n_events=74_691_568,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 9,
            "nominal_ext1": 17,
            "hdamp_down": 12,
            "hdamp_up": 12,
            "mtop_down": 9,
            "mtop_up": 9,
            "tune_down": 9,
            "tune_up": 9,
        },
    },
)

# #
# # ttbar + 1 vector boson
# #

# cpn.add_dataset(
#     name="ttw_wlnu_amcatnlo",
#     id=14836091,
#     processes=[procs.ttw_wlnu],
#     keys=[
#         "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=111_308,
#     aux={
#         "merging_factors": {
#             "nominal": 3,
#         },
#     },
# )

# cpn.add_dataset(
#     name="ttz_zqq_amcatnlo",
#     id=14796231,
#     processes=[procs.ttz_zqq],
#     keys=[
#         "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=376_687,
#     aux={
#         "merging_factors": {
#             "nominal": 26,
#         },
#     },
# )

# cpn.add_dataset(
#     name="ttz_zll_m4to50_amcatnlo",
#     id=14790832,
#     processes=[procs.ttz_zll_m4to50],
#     keys=[
#         "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=300_000,
#     aux={
#         "merging_factors": {
#             "nominal": 25,
#         },
#     },
# )

# cpn.add_dataset(
#     name="ttz_zll_m50toinf_amcatnlo",
#     id=14791117,
#     processes=[procs.ttz_zll_m50toinf],
#     keys=[
#         "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=400_000,
#     aux={
#         "merging_factors": {
#             "nominal": 30,
#         },
#     },
# )

# cpn.add_dataset(
#     name="ttz_znunu_amcatnlo",
#     id=14881328,
#     processes=[procs.ttz_znunu],
#     keys=[
#         "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=498_544,
#     aux={
#         "merging_factors": {
#             "nominal": 36,
#         },
#     },
# )

# #
# # ttbar + 2 vector boson
# #

# cpn.add_dataset(
#     name="ttww_madgraph",
#     id=14792013,
#     processes=[procs.ttww],
#     keys=[
#         "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=450_000,
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="ttzz_madgraph",
#     id=14796051,
#     processes=[procs.ttzz],
#     keys=[
#         "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=443_238,
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#         },
#     },
# )

# #
# # single top
# #

# cpn.add_dataset(
#     name="st_tchannel_tbar_4f_powheg",
#     id=14803988,
#     processes=[procs.st_tchannel_tbar],
#     keys=[
#         "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1_433_215,
#     aux={
#         "merging_factors": {
#             "nominal": 23,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_tchannel_t_4f_powheg",
#     id=14801389,
#     processes=[procs.st_tchannel_t],
#     keys=[
#         "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=2_973_675,
#     aux={
#         "merging_factors": {
#             "nominal": 16,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_tbar_dl_powheg",
#     id=14791318,
#     processes=[procs.st_twchannel_tbar_dl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#                 "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4 + 4,
#             n_events=2_465_972 + 2_435_737,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_499_291,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_436_721,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_524_255,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_497_188,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_363_085,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_536_835,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#             "nominal_ext1": 32,
#             "hdamp_down": 18,
#             "hdamp_up": 16,
#             "mtop_down": 19,
#             "mtop_up": 17,
#             "tune_down": 14,
#             "tune_up": 17,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_tbar_fh_powheg",
#     id=14790862,
#     processes=[procs.st_twchannel_tbar_fh],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#                 "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7 + 8,
#             n_events=3_762_952 + 4_000_000,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_963_854,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_895_220,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_938_484,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_898_600,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_971_608,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_920_656,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 11,
#             "nominal_ext1": 22,
#             "hdamp_down": 12,
#             "hdamp_up": 13,
#             "mtop_down": 15,
#             "mtop_up": 13,
#             "tune_down": 14,
#             "tune_up": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_tbar_sl_powheg",
#     id=14791094,
#     processes=[procs.st_twchannel_tbar_sl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=8,
#             n_events=4_407_845,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_930_632,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_865_573,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=5_133_770,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_995_477,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=8,
#             n_events=4_659_748,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=8,
#             n_events=4_661_358,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#             "hdamp_down": 15,
#             "hdamp_up": 15,
#             "mtop_down": 15,
#             "mtop_up": 13,
#             "tune_down": 19,
#             "tune_up": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_t_dl_powheg",
#     id=14805970,
#     processes=[procs.st_twchannel_t_dl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#                 "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4 + 4,
#             n_events=2_387_056 + 2_500_000,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_501_382,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=5,
#             n_events=2_538_826,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_513_281,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_497_924,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_361_903,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=4,
#             n_events=2_375_416,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#             "nominal_ext1": 31,
#             "hdamp_down": 21,
#             "hdamp_up": 15,
#             "mtop_down": 24,
#             "mtop_up": 25,
#             "tune_down": 15,
#             "tune_up": 20,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_t_fh_powheg",
#     id=14791162,
#     processes=[procs.st_twchannel_t_fh],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#                 "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7 + 7,
#             n_events=3_862_005 + 3_909_550,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_976_914,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_916_606,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=8,
#             n_events=4_020_863,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_870_500,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_793_280,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=3_853_959,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#             "nominal_ext1": 22,
#             "hdamp_down": 13,
#             "hdamp_up": 12,
#             "mtop_down": 11,
#             "mtop_up": 17,
#             "tune_down": 16,
#             "tune_up": 13,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_twchannel_t_sl_powheg",
#     id=14798336,
#     processes=[procs.st_twchannel_t_sl],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#                 "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9 + 9,
#             n_events=4_743_971 + 4_900_350,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_903_597,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_801_624,
#         ),
#         mtop_down=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_904_011,
#         ),
#         mtop_up=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=8,
#             n_events=4_522_843,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=5_090_154,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=9,
#             n_events=4_902_158,
#         ),
#     ),
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#             "nominal_ext1": 26,
#             "hdamp_down": 15,
#             "hdamp_up": 15,
#             "mtop_down": 12,
#             "mtop_up": 15,
#             "tune_down": 13,
#             "tune_up": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_schannel_t_lep_4f_amcatnlo",
#     id=14791065,
#     processes=[procs.st_schannel_t_lep],
#     keys=[
#         "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1_271_280,
#     aux={
#         "merging_factors": {
#             "nominal": 20,
#         },
#     },
# )

# cpn.add_dataset(
#     name="st_schannel_tbar_lep_4f_amcatnlo",
#     id=14791008,
#     processes=[procs.st_schannel_tbar_lep],
#     keys=[
#         "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=785_520,
#     aux={
#         "merging_factors": {
#             "nominal": 34,
#         },
#     },
# )
