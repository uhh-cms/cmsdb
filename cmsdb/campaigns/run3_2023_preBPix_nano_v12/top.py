# coding: utf-8

"""
top quark datasets for the 2023 pre-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


####################################################################################################
#
# ttbar
#
####################################################################################################

#
# ttbar (amcatnlo)
#

# cpn.add_dataset(
#     name="tt_sl_lplus_amcatnlo",
#     id=14898683,
#     processes=[procs.tt_sl_lplus],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTtoLplusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=849,
#             n_events=112810992,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="tt_sl_lminus_amcatnlo",
#     id=14900212,
#     processes=[procs.tt_sl_lminus],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTtoLminusNu2Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=767,
#             n_events=121126936,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tt_dl_amcatnlo",
    id=14836339,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=669,
            n_events=85706556,
        ),
    ),
)
cpn.add_dataset(
    name="tt_fh_amcatnlo",
    id=14890409,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=1012,
            n_events=163529794,
        ),
    ),
)

#
# ttbar (powheg)
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14808378,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=798,
            n_events=152797000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=463,
            n_events=63714000,
        ),
        # _MT-166p5_=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=388,
        #     n_events=64958999,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=462,
            n_events=65514000,
        ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=375,
        #     n_events=65907000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=345,
            n_events=65751000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=359,
            n_events=65766000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=285,
            n_events=63486000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=425,
            n_events=64152000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=267,
        #     n_events=62063999,
        # ),
        # _MT-178p5_=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=435,
        #     n_events=65694000,
        # ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=365,
        #     n_events=64026000,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=333,
            n_events=65670000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=536,
            n_events=65655000,
        ),
    ),
)


cpn.add_dataset(
    name="tt_dl_powheg",
    id=14821827,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=198,
            n_events=48203000,
        ),
        # _MT-178p5_=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=98,
        #     n_events=19616000,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=19661000,
        ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=134,
        #     n_events=19973000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=95,
            n_events=19736000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=110,
        #     n_events=19802000,
        # ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=112,
            n_events=19682000,
        ),
        # _MT-166p5_=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=87,
        #     n_events=19517000,
        # ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=97,
            n_events=19511000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=100,
            n_events=19745000,
        ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=136,
        #     n_events=19940000,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=97,
            n_events=19423999,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=19832000,
        ),
    ),
)


cpn.add_dataset(
    name="tt_fh_powheg",
    id=14809569,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=467,
            n_events=104393000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=303,
            n_events=44806000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=223,
            n_events=45873999,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=255,
            n_events=45748000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=418,
            n_events=45811000,
        ),
        # _MT-178p5_=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=350,
        #     n_events=44551000,
        # ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=411,
        #     n_events=45808000,
        # ),
        # _MT-166p5_=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=220,
        #     n_events=45904000,
        # ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=259,
            n_events=45022000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=181,
            n_events=44800000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=230,
            n_events=45262000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=236,
        #     n_events=45565000,
        # ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=239,
        #     n_events=45928000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=429,
            n_events=44557000,
        ),
    ),
)

####################################################################################################
#
# single top (s-channel)
#
####################################################################################################

# TODO: not yet found in DAS

####################################################################################################
#
# single top (t-channel)
#
####################################################################################################
cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=15017347,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=92,  # 92-0
            n_events=5786000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=15017262,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=2878000,
        ),
    ),
)

####################################################################################################
#
# single top (tW-channel)
#
####################################################################################################

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14820989,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=9650268,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=9703429,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=74,
            n_events=9758668,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=99,
        #     n_events=9477005,
        # ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=90,
        #     n_events=9953467,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=9878214,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=97,
            n_events=9629035,
        ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=126,
        #     n_events=9786266,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=93,
            n_events=9651040,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=9734131,
        ),
        # _DS_TuneCP5_=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=108,
        #     n_events=9857973,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=96,
            n_events=9821540,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=111,
            n_events=9835242,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14834106,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=4985000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=4956000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=49,
        #     n_events=4943000,
        # ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=30,
        #     n_events=4970000,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=4874000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=4961000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=64,
            n_events=4970000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=4982000,
        ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=62,
        #     n_events=4961000,
        # ),
        # _DS_TuneCP5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=54,
        #     n_events=4940000,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=4937000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=4982000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=4853000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14825872,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=7922000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=49,
            n_events=7832000,
        ),
        # _DS_TuneCP5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=81,
        #     n_events=7973000,
        # ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=7991000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=7793000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=7838000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=7940000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=83,
        #     n_events=7991000,
        # ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=7670000,
        ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=91,
        #     n_events=7928000,
        # ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=7934000,
        ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=66,
        #     n_events=7964000,
        # ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=7910000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=15202170,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v6/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=9550671,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=10046550,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=9606924,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=9592802,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=9832735,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=9914851,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=9646157,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=9982124,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v5/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=9876854,
        ),
    ),
)


cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14929076,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=4931000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=4908000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=4964000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=4910000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=4937000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=4920000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=4676000,
        ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
        #     ],
        #     n_files=57,
        #     n_events=4864000,
        # ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
        #     ],
        #     n_files=43,
        #     n_events=4958000,
        # ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=4985000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=4952000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14929408,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=7841000,
        ),
        # _DS_TuneCP5_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
        #     ],
        #     n_files=44,
        #     n_events=7976000,
        # ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=7718000,
        ),
        # _MT-169p5_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
        #     ],
        #     n_files=50,
        #     n_events=7898000,
        # ),
        # _MT-175p5_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
        #     ],
        #     n_files=60,
        #     n_events=7895000,
        # ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=7931000,
        ),
        # _TuneCP5_ERDOn_=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
        #     ],
        #     n_files=60,
        #     n_events=7832000,
        # ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=7886000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=7868000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=87,
            n_events=7997000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=7724000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=7853000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=7835000,
        ),
    ),
)

####################################################################################################
#
# ttV, ttVV
#
####################################################################################################

#
# ttW
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15138234,
    processes=[procs.ttw_wlnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=460305,
        ),
    ),
)

#
# ttZ
#

cpn.add_dataset(
    name="ttz_zqq_amcatnlo",
    id=15200215,
    processes=[procs.ttz_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=803622,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=14995483,
    processes=[procs.ttz_zll_m4to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=591000,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=14998321,
    processes=[procs.ttz_zll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=794000,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=7850000,
        ),
    ),
)

cpn.add_dataset(
    name="ttz_znunu_amcatnlo",
    id=14930815,
    processes=[procs.ttz_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=976000,
        ),
    ),
)

#
# ttVV
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14942216,
    processes=[procs.ttww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=151,
            n_events=14912000,
        ),
    ),
)
cpn.add_dataset(
    name="ttwz_madgraph",
    id=14969092,
    processes=[procs.ttw],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=1000000,
        ),
    ),
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14942834,
    processes=[procs.ttzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=1994000,
        ),
    ),
)

#
# tttt
#

cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14986966,
    processes=[procs.tttt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=113,  # 113-0
            n_events=4994204,
        ),
    ),
)

#
# ttg, tg
#

cpn.add_dataset(
    name="ttg_pt10to100_amcatnlo",
    id=14987262,
    processes=[procs.ttg_pt10to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=1976537,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt200toinf_amcatnlo",
    id=14995480,
    processes=[procs.ttg_pt200toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=606104,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt100to200_amcatnlo",
    id=14998312,
    processes=[procs.ttg_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=605263,
        ),
    ),
)

cpn.add_dataset(
    name="tgqb_amcatnlo",
    id=15200779,
    processes=[procs.tgqb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=59,  # 59-0
            n_events=4419000,
        ),
    ),
)
