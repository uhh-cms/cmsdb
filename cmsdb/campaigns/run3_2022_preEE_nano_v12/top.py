# coding: utf-8

"""
top quark datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# ttbar
#


cpn.add_dataset(
    name="tt_sl_powheg",
    id=14791322,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=125,
            n_events=49771670,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=716,
            n_events=76955324,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=101,
            n_events=32029996,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=160,
            n_events=31572504,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=85,
        #     n_events=30007707,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=77,
        #     n_events=32108628,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=112,
            n_events=32724200,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=31188404,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=99,
        #     n_events=31416065,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=70,
        #     n_events=31349400,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=32314035,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=31008419,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=70,
            n_events=32337000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=76,
            n_events=31582784,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3_ext1-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=116,
        #     n_events=77002090,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTtoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=74,
        #     n_events=32388034,
        # ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14803719,
    is_data=False,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=23778148,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=319,
            n_events=24047488,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=9858113,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=63,
            n_events=9795550,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=32,
        #     n_events=9822000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=89,
        #     n_events=9638631,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=9728780,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=111,
            n_events=9445459,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=143,
        #     n_events=9539336,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=127,
        #     n_events=9494040,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=9784596,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=9752000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=9765000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=109,
            n_events=9669120,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=33,
        #     n_events=23802613,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3_ext1-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=37,
        #     n_events=24084800,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=41,
        #     n_events=9829000,
        # ),
    ),
)


cpn.add_dataset(
    name="tt_fh_powheg",
    id=14808372,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=53605620,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=498,
            n_events=51819730,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=23228415,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=21600896,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=114,
        #     n_events=22800215,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=122,
        #     n_events=21834464,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=107,
            n_events=23222000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=129,
            n_events=22750854,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=146,
        #     n_events=21718270,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=55,
        #     n_events=21696467,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=22590056,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=23285645,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=22201488,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=22435778,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=83,
        #     n_events=53475524,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-JMENano12p5_132X_mcRun3_2022_realistic_v3_ext1-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=88,
        #     n_events=52573597,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=63,
        #     n_events=21791429,
        # ),
    ),
)


#
# single top (t-channel)
#


cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=14803181,
    processes=[procs.st_tchannel_t],
    keys=[
        "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=2973675,
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=14808106,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=1433215,
)


#
# single-top (tW-channel)
#


cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14799262,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa

            ],
            n_files=64,
            n_events=4643600,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa

            ],
            n_files=119,
            n_events=4899672,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=63,
        #     n_events=4681299,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=4903597,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=73,
            n_events=4837983,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=54,
        #     n_events=4854094,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=4904011,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=4512526,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=62,
        #     n_events=4825550,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=83,
            n_events=4524604,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=4548795,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=5090154,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=4902158,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=37,
        #     n_events=4635831,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14793356,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa

            ],
            n_files=49,
            n_events=4366467,
        ),
        extension=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa

            ],
            n_files=116,
            n_events=4850663,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=62,
        #     n_events=5283169,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=4676784,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=68,
            n_events=4844713,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=69,
        #     n_events=5023981,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=5085865,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=4995477,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=55,
        #     n_events=5034432,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=4667072,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=4633416,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=98,
            n_events=4554541,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=4623327,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=41,
        #     n_events=4612907,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14805980,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=2369680,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=2499302,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=46,
        #     n_events=2500000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=2501382,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=2538826,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=20,
        #     n_events=2489305,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=2513281,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=2497924,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=64,
        #     n_events=2428448,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCH3_13p6TeV_powheg-herwig7/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=23,
        #     n_events=2392986,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=2490270,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=2455584,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=2365408,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=2375416,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=27,
        #     n_events=2387360,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14794142,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=2327688,
        ),
        extension=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=73,
            n_events=2461995,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=39,
        #     n_events=2500000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=2499291,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=2458051,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=23,
        #     n_events=2377870,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=2524255,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=2491432,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=72,
        #     n_events=2488253,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCH3_13p6TeV_powheg-herwig7/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
        #     ],
        #     n_files=24,
        #     n_events=2462984,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=2350270,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=2445712,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=2363085,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=2536835,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=55,
        #     n_events=2437522,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14793291,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=3883455,
        ),
        extension=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=3880525,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=64,
        #     n_events=3956724,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=3976914,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=3916606,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=17,
        #     n_events=3950320,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=4020863,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=80,
            n_events=3883800,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=29,
        #     n_events=3981640,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=3784408,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=82,
            n_events=3786106,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=3814360,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=3853959,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=58,
        #     n_events=3717175,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14791411,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=3762952,
        ),
        extension=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=71,
            n_events=4000000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_DS_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=28,
        #     n_events=3871291,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=3963854,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=3897924,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=44,
        #     n_events=3960966,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=3938484,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=3919556,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=76,
        #     n_events=3995968,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=88,
            n_events=3779571,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=3842472,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=34,
            n_events=3971608,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=3920656,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_TuneCP5_ERDOn_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        #     ],
        #     n_files=51,
        #     n_events=3896725,
        # ),
    ),
)


####################################################################################################
#
# ttV, ttVV
#
####################################################################################################

# TODO: add corresponding process
# cpn.add_dataset(
#     name="ttz_amcatnlo",
#     id=14796050,
#     processes=[procs.ttz],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=24,
#             n_events=376687,
#         ),
#     ),
# )

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=14793929,
    processes=[procs.ttz_zll_m4to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=300000,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=14793589,
    processes=[procs.ttz_zll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=400000,
        ),
    ),
)

cpn.add_dataset(
    name="ttw_amcatnlo",
    id=14836097,
    processes=[procs.ttw],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=1,
            n_events=111308,
        ),
    ),
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14800072,
    processes=[procs.ttzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=443238,
        ),
    ),
)

cpn.add_dataset(
    name="ttww_madgraph",
    id=14797430,
    processes=[procs.ttww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=448443,
        ),
    ),
)
cpn.add_dataset(
    name="ttwz_madgraph",
    id=15006953,
    processes=[procs.ttwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=272400,
        ),
    ),
)

#
# tttt
#

cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14795232,
    processes=[procs.tttt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=2396925,
        ),
    ),
)

#
# ttg, tg
#

cpn.add_dataset(
    name="ttg_pt10to100_amcatnlo",
    id=14837199,
    processes=[procs.ttg_pt10to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=986777,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt200toinf_amcatnlo",
    id=14845249,
    processes=[procs.ttg_pt200toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=286306,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt100to200_amcatnlo",
    id=14845482,
    processes=[procs.ttg_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,  # 26-0
            n_events=317194,
        ),
    ),
)

cpn.add_dataset(
    name="tgqb_amcatnlo",
    id=14793135,
    processes=[procs.tgqb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=2160840,
        ),
    ),
)
