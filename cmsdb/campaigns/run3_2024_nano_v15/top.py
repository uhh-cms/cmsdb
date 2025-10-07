# coding: utf-8

"""
top quark datasets for the 2024 data-taking campaign (Nano v15)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import run3_2024_nano_v15 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_dl_powheg",
    id=15304231,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=780,  # 780-0
            n_events=470123263,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=406,  # 406-0
            n_events=59915000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=368,  # 368-0
            n_events=59985000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_Par-MT-166p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=378,  # 378-0
        #     n_events=59989000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=373,  # 373-0
        #     n_events=59953000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=372,  # 372-0
            n_events=59987000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=373,  # 373-0
            n_events=59982000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=390,  # 390-0
        #     n_events=59980000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_Par-MT-178p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=363,  # 363-0
        #     n_events=59943000,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=378,  # 378-0
            n_events=59983000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=365,  # 365-0
            n_events=59977000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=379,  # 379-0
            n_events=59967000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=383,  # 383-0
            n_events=59987000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TTto2L2Nu_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=389,  # 389-0
        #     n_events=59876000,
        # ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=15296265,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=773,  # 773-0
            n_events=472535695,
        ),
    ),
)

cpn.add_dataset(
    name="tt_sl_powheg",
    id=15292847,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=790,  # 790-0
            n_events=484475057,
        ),
    ),
)

#
# single top (t-channel)
#

cpn.add_dataset(
    name="st_tchannel_t_4f_qq_powheg",
    id=15370314,
    processes=[procs.st_tchannel_t_qq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=778,  # 778-0
            n_events=87576444,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_t_4f_lnu_powheg",
    id=15316276,
    processes=[procs.st_tchannel_t_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=391,  # 391-0
            n_events=44258039,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=218,  # 218-0
            n_events=21903026,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=389,  # 389-0
            n_events=22008628,
        ),
    ),
)


cpn.add_dataset(
    name="st_tchannel_tbar_4f_qq_powheg",
    id=15363774,
    processes=[procs.st_tchannel_tbar_qq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=825,  # 825-0
            n_events=43273264,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_lnu_powheg",
    id=15316115,
    processes=[procs.st_tchannel_t_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=249,  # 249-0
            n_events=22102160,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=188,  # 188-0
            n_events=10997130,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=166,  # 166-0
            n_events=11000625,
        ),
    ),
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
    id=15349111,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=252,  # 252-0
            n_events=28763293,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=281,  # 281-0
        #     n_events=28872518,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=233,  # 233-0
            n_events=29787089,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=254,  # 254-0
            n_events=29889675,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=197,  # 197-0
        #     n_events=29796106,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=238,  # 238-0
            n_events=31799777,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=236,  # 236-0
            n_events=29671243,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=249,  # 249-0
        #     n_events=29577721,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=198,  # 198-0
            n_events=28508686,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=235,  # 235-0
            n_events=30991856,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=209,  # 209-0
            n_events=30179634,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=247,  # 247-0
            n_events=28506776,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminustoLNu2Q_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=230,  # 230-0
        #     n_events=28738391,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=15376087,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=252,  # 252-0
            n_events=29395659,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=294,  # 294-0
        #     n_events=31473868,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=251,  # 251-0
            n_events=32748146,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=218,  # 218-0
            n_events=27886841,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=244,  # 244-0
        #     n_events=30337245,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=234,  # 234-0
            n_events=31313302,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=251,  # 251-0
            n_events=28932755,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=216,  # 216-0
        #     n_events=28334685,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplustoLNu2Q_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=258,  # 258-0
        #     n_events=29648440,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=15376104,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=176,  # 176-0
            n_events=14998000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=178,  # 178-0
        #     n_events=14994000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=150,  # 150-0
            n_events=14980000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=172,  # 172-0
            n_events=14998000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=103,  # 103-0
        #     n_events=14980000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=99,  # 99-0
            n_events=14986000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=226,  # 226-0
            n_events=14861000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=199,  # 199-0
        #     n_events=14988000,
        # ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=171,  # 171-0
            n_events=14989000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=248,  # 248-0
            n_events=14820000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=111,  # 111-0
            n_events=15000000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=206,  # 206-0
            n_events=14972000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto2L2Nu_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=108,  # 108-0
        #     n_events=14795000,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=15376044,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=90,  # 90-0
            n_events=15000000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=172,  # 172-0
        #     n_events=15000000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=167,  # 167-0
            n_events=15000000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=145,  # 145-0
            n_events=15000000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=185,  # 185-0
        #     n_events=14999000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=163,  # 163-0
            n_events=14998000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=186,  # 186-0
            n_events=15000000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=147,  # 147-0
        #     n_events=15000000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto2L2Nu_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=162,  # 162-0
        #     n_events=15000000,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=15375712,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=154,  # 154-0
            n_events=23999000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=185,  # 185-0
        #     n_events=23968000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=203,  # 203-0
            n_events=23991000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=216,  # 216-0
            n_events=23992000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=222,  # 222-0
        #     n_events=23997000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=182,  # 182-0
            n_events=23991000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=160,  # 160-0
            n_events=23948000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=179,  # 179-0
        #     n_events=23983000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TWminusto4Q_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=209,  # 209-0
        #     n_events=23902000,
        # ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=15375023,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=195,  # 195-0
            n_events=24000000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q-DS_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=194,  # 194-0
        #     n_events=24000000,
        # ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=203,  # 203-0
            n_events=24000000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=223,  # 223-0
            n_events=23997000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_Par-MT-169p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=243,  # 243-0
        #     n_events=23999000,
        # ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=180,  # 180-0
            n_events=23999000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=222,  # 222-0
            n_events=23996000,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_Par-MT-175p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=183,  # 183-0
        #     n_events=23999000,
        # ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/TbarWplusto4Q_Par-ERD-On_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=209,  # 209-0
        #     n_events=24000000,
        # ),
    ),
)

####################################################################################################
#
# ttV, ttVV
#
####################################################################################################

# Missing: ttZ, ttW, TTg, TgJets, TTTT, TZq

"""
# ttgg?
cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=15382584,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTGG_TuneCP5_13p6TeV_madgraph-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=2053000,
        ),
    ),
)
"""

cpn.add_dataset(
    name="ttww_madgraph",
    id=15393150,
    processes=[procs.ttww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=5801000,
        ),
    ),
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=15393070,
    processes=[procs.ttwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=51,  # 51-0
            n_events=5529000,
        ),
    ),
)

cpn.add_dataset(
    name="ttzz_zz4b_madgraph",
    id=15292170,
    processes=[procs.ttzz_zz4b],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZZ-ZZto4B_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=9911305,
        ),
    ),
)

# inclusive TTZZ misisng!
