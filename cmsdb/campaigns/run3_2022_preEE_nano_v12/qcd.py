# coding: utf-8

"""
QCD datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn
from order import DatasetInfo


#
# QCD (pythia, pt-binned, muon enriched)
#


cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14800053,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=4417909,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14809799,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=71,
    n_events=30200859,
)
cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14805426,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=33440507,
)
cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14791064,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=40107069,
)
cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14797620,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=24614026,
)
cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14791498,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=18555616,
)
cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14798613,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=193,
    n_events=36864921,
)
cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14792060,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=30226277,
)
cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14791997,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=18567007,
)
cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14800405,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=107,
    n_events=19723745,
)
cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14808237,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=39316355,
)
cpn.add_dataset(
    name="qcd_mu_pt1000toinf_pythia",
    id=14796004,
    processes=[procs.qcd_mu_pt1000toinf],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=13705539,
)


#
# QCD (pythia, pt-binned, electron enriched)
#


cpn.add_dataset(
    name="qcd_em_pt10to30_pythia",
    id=14805335,
    processes=[procs.qcd_em_pt10to30],
    keys=[
        "/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=986169,
)
cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14808098,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=954720,
)
cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14792371,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=929811,
)
cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14801474,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=951227,
)
cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14801536,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=931334,
)
cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14808219,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=1007981,
)
cpn.add_dataset(
    name="qcd_em_pt300toinf_pythia",
    id=14802354,
    processes=[procs.qcd_em_pt300toinf],
    keys=[
        "/QCD_PT-300toInf_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=908512,
)


#
# QCD (pythia, pt-binned, double electron enriched)
#


cpn.add_dataset(
    name="qcd_doubleem_pt30to40_mgg80toinf_pythia",
    id=14801752,
    processes=[procs.qcd_doubleem_pt30to40_mgg80toinf],
    keys=[
        "/QCD_PT-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1425413,
)
cpn.add_dataset(
    name="qcd_doubleem_pt30toinf_mgg40to80_pythia",
    id=14807962,
    processes=[procs.qcd_doubleem_pt30toinf_mgg40to80],
    keys=[
        "/QCD_PT-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=2875029,
)
cpn.add_dataset(
    name="qcd_doubleem_pt40toinf_mgg80toinf_pythia",
    id=14803826,
    processes=[procs.qcd_doubleem_pt40toinf_mgg80toinf],
    keys=[
        "/QCD_PT-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=2947774,
)


#
# QCD (madgraph, HT-binned, 4 jets)
#

# cpn.add_dataset(
#     name="qcd_ht40to70_madgraph",
#     id=14790741,
#     processes=[procs.qcd_ht40to70],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=36,
#             n_events=19200453,
#         ),
#     ),
# )
cpn.add_dataset(
    name="qcd_ht70to100_madgraph",
    id=14796537,
    processes=[procs.qcd_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=122,
            n_events=18852962,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14791746,
    processes=[procs.qcd_ht100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=84,
            n_events=19039024,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht200to400_madgraph",
    id=14791211,
    processes=[procs.qcd_ht200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=20642715,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht400to600_madgraph",
    id=14791899,
    processes=[procs.qcd_ht400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=19602817,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht600to800_madgraph",
    id=14792475,
    processes=[procs.qcd_ht600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=118,
            n_events=19028458,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht800to1000_madgraph",
    id=14791019,
    processes=[procs.qcd_ht800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=105,
            n_events=21602068,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht1000to1200_madgraph",
    id=14791276,
    processes=[procs.qcd_ht1000to1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=20642169,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht1200to1500_madgraph",
    id=14792140,
    processes=[procs.qcd_ht1200to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=135,
            n_events=21112774,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14791093,
    processes=[procs.qcd_ht1500to2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=88,
            n_events=21191630,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=14792291,
    processes=[procs.qcd_ht2000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=110,
            n_events=18132719,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt15to30_pythia",
    id=14853174,
    processes=[procs.qcd_pt15to30],
    info=dict(
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=1174100,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt30to50_pythia",
    id=14854083,
    processes=[procs.qcd_pt30to50],
    info=dict(
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=1198100,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14793083,
    processes=[procs.qcd_pt800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=4400187,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=108,  # 108-0
            n_events=39198266,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14802394,
    processes=[procs.qcd_pt600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=7839456,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=130,  # 130-0
            n_events=65122631,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14804302,
    processes=[procs.qcd_pt2400to3200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=195024,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=1900172,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14807815,
    processes=[procs.qcd_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=1418925,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=64,  # 64-0
            n_events=29178417,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14799311,
    processes=[procs.qcd_pt300to470],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=967072,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=99,  # 99-0
            n_events=56638371,
        ),
    ),
)

# cpn.add_dataset(
#     name="qcd_pt600toinf_pythia",
#     id=14805830,
#     processes=[procs.qcd_pt600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_PT-600toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=10,  # 10-0
#             n_events=989648,
#         ),
#     ),
# )

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14796376,
    processes=[procs.qcd_pt470to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=976760,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=80,  # 80-0
            n_events=27468864,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14796571,
    processes=[procs.qcd_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=805272,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=94,  # 94-0
            n_events=28570060,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt3200toinf_pythia",
    id=14799246,
    processes=[procs.qcd_pt3200toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=100000,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=699375,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14805715,
    processes=[procs.qcd_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=983532,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=84,  # 84-0
            n_events=29759904,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14802404,
    processes=[procs.qcd_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=1476736,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=64,  # 64-0
            n_events=19617716,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14792773,
    processes=[procs.qcd_pt1000to1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=2432093,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=19615910,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14793089,
    processes=[procs.qcd_pt1800to2400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=693521,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=2961265,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14800404,
    processes=[procs.qcd_pt1400to1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=1488256,
        ),
        extension=DatasetInfo(
            keys=[
                "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=5901990,
        ),
    ),
)
