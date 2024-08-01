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
