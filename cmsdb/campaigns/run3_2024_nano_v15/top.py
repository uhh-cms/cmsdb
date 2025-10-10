
# coding: utf-8

""""
top quark datasets for the run3_2024_nano_v15 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ttbar
#

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

#
# single top
#

# s channel - missing? FIXME

# t channel

# # FIXME: what's up with st t channel??
# cpn.add_dataset(
#     name="st_tchannel_t_powheg",
#     id=15370314,
#     processes=[procs.st_tchannel_t],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=778,  # 778-0
#             n_events=87576444,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="st_tchannel_t_4f_powheg",  # FIXME
#     id=15316276,
#     processes=[procs.st_tchannel_t],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=391,  # 391-0
#             n_events=44258039,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TBbarQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=218,  # 218-0
#             n_events=21903026,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TBbarQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=389,  # 389-0
#             n_events=22008628,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="st_tchannel_tbar_4f_powheg",  # FIXME
#     id=15363774,
#     processes=[procs.st_tchannel_tbar],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=825,  # 825-0
#             n_events=43273264,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TbarBQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=188,  # 188-0
#             n_events=10997130,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TbarBQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=166,  # 166-0
#             n_events=11000625,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="PLACEHOLDER_powheg",  # FIXME
#     id=15316115,
#     processes=[procs.PLACEHOLDER],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=249,  # 249-0
#             n_events=22102160,
#         ),
#     ),
# )

# tw channel

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=15377565,
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
    ),
)

# ttv

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=15390973,
    processes=[procs.ttz_zll_m4to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=2965000,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=15390855,
    processes=[procs.ttz_zll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=3952000,
        ),
    ),
)
cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15393690,
    processes=[procs.ttw_wlnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLNu-EWK_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=38,  # 38-0
            n_events=2999000,
        ),
    ),
)

# ttvv

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
    name="ttzz_madgraph",
    id=15292170,
    processes=[procs.ttzz],
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
