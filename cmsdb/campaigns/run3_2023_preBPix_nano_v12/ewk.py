# coding: utf-8

"""
Electroweak datasets for the 2023 pre-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################


#
# LO
#

cpn.add_dataset(
    name="dy_m10to50_madgraph",
    id=14889650,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-10to50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=775,
            n_events=285999749,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14841286,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=154,
            n_events=128629893,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_madgraph",
    id=14895190,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=189,
            n_events=29092286,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_madgraph",
    id=14892625,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=190,
            n_events=29188837,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_3j_madgraph",
    id=14894781,
    processes=[procs.dy_m50toinf_3j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=145,
            n_events=16988034,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_4j_madgraph",
    id=14895189,
    processes=[procs.dy_m50toinf_4j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50_4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=123,
            n_events=5622082,
        ),
    ),
)

# TODO: implement processes
# cpn.add_dataset(
#     name="dy_m50toinf_pt40to100_madgraph",
#     id=14948656,
#     processes=[procs.dy_m50toinf_pt40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=334,
#             n_events=100005339,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_pt100to200_madgraph",
#     id=14948644,
#     processes=[procs.dy_m50toinf_pt100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=194,
#             n_events=38700590,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_pt200to400_madgraph",
#     id=14948738,
#     processes=[procs.dy_m50toinf_pt200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=46,
#             n_events=4023259,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_pt400to600_madgraph",
#     id=14948643,
#     processes=[procs.dy_m50toinf_pt400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=41,
#             n_events=2105393,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_pt600toinf_madgraph",
#     id=14948664,
#     processes=[procs.dy_m50toinf_pt600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50_PTLL-600_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=60,
#             n_events=2241010,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht40to70_madgraph",
#     id=14929613,
#     processes=[procs.dy_m4to50_ht40to70],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=773,
#             n_events=195280048,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht70to100_madgraph",
#     id=14931761,
#     processes=[procs.dy_m4to50_ht70to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=585,
#             n_events=118075999,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht100to400_madgraph",
#     id=14931178,
#     processes=[procs.dy_m4to50_ht100to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=623,
#             n_events=121290191,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht400to800_madgraph",
#     id=14931220,
#     processes=[procs.dy_m4to50_ht400to800],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=74,
#             n_events=2656934,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht800to1500_madgraph",
#     id=14930911,
#     processes=[procs.dy_m4to50_ht800to1500],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
#             ],
#             n_files=72,
#             n_events=1830752,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht1500to2500_madgraph",
#     id=14930347,
#     processes=[procs.dy_m4to50_ht1500to2500],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=61,
#             n_events=1891503,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m4to50_ht2500toinf_madgraph",
#     id=14930962,
#     processes=[procs.dy_m4to50_ht2500toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-4to50_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=233,
#             n_events=2160355,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht40to70_madgraph",
#     id=14909146,
#     processes=[procs.dy_m50to120_ht40to70],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=368,
#             n_events=82469227,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht70to100_madgraph",
#     id=14885235,
#     processes=[procs.dy_m50to120_ht70to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=381,
#             n_events=57582531,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht100to400_madgraph",
#     id=14909012,
#     processes=[procs.dy_m50to120_ht100to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=437,
#             n_events=74271754,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50to120_ht400to800_madgraph",
#     id=14895172,
#     processes=[procs.dy_m50to120_ht400to800],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-4Jets_MLL-50to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=84,
#             n_events=2285923,
#         ),
#     ),
# )

#
# NLO
#

cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14930974,
    processes=[procs.dy_m4to10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=579,
            n_events=193884080,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14905259,
    processes=[procs.dy_m10to50],
    info=dict(
        # NOTE: this is an extension, but there was no "non-extension" dataset to be found in DAS
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=658,
            n_events=200200891,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14837024,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=181,
            n_events=154485208,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14895741,
    processes=[procs.dy_m50toinf_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=632,
            n_events=195345826,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14890414,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=679,
            n_events=154506477,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14891860,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=812,
            n_events=192409561,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14826625,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=332,
            n_events=92974565,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14826648,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=3577765,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14826162,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=191,
            n_events=36811062,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14826639,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=989929,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14825808,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=975787,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14827200,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=183,
            n_events=40037710,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14826665,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=224,
            n_events=39173887,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14826694,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=8048986,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14825065,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=960577,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14825780,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v1/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=1001323,
        ),
    ),
)

# DY m_ll 4-50 GeV, HT-binned,

cpn.add_dataset(
    name="dy_m4to50_ht40to70_madgraph",
    id=14929613,
    processes=[procs.dy_m4to50_ht40to70],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=773,
    n_events=195280048,
)

cpn.add_dataset(
    name="dy_m4to50_ht70to100_madgraph",
    id=14931761,
    processes=[procs.dy_m4to50_ht70to100],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=585,
    n_events=118075999,
)

cpn.add_dataset(
    name="dy_m4to50_ht100to400_madgraph",
    id=14931178,
    processes=[procs.dy_m4to50_ht100to400],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=623,
    n_events=121290191,
)

cpn.add_dataset(
    name="dy_m4to50_ht400to800_madgraph",
    id=14931220,
    processes=[procs.dy_m4to50_ht400to800],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=74,
    n_events=2656934,
)

cpn.add_dataset(
    name="dy_m4to50_ht800to1500_madgraph",
    id=14930911,
    processes=[procs.dy_m4to50_ht800to1500],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=1830752,
)

cpn.add_dataset(
    name="dy_m4to50_ht1500to2500_madgraph",
    id=14930347,
    processes=[procs.dy_m4to50_ht1500to2500],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=1891503,
)

cpn.add_dataset(
    name="dy_m4to50_ht2500toinf_madgraph",
    id=14930962,
    processes=[procs.dy_m4to50_ht2500toinf],
    keys=[
        "/DYto2L-4Jets_MLL-4to50_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=233,
    n_events=2160355,
)

# DY m_ll 50-120 GeV, HT-binned

cpn.add_dataset(
    name="dy_m50to120_ht40to70_madgraph",
    id=14909146,
    processes=[procs.dy_m50to120_ht40to70],
    keys=[
        "/DYto2L-4Jets_MLL-50to120_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=368,
    n_events=82469227,
)

cpn.add_dataset(
    name="dy_m50to120_ht70to100_madgraph",
    id=14885235,
    processes=[procs.dy_m50to120_ht70to100],
    keys=[
        "/DYto2L-4Jets_MLL-50to120_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=381,
    n_events=57582531,
)

cpn.add_dataset(
    name="dy_m50to120_ht100to400_madgraph",
    id=14909012,
    processes=[procs.dy_m50to120_ht100to400],
    keys=[
        "/DYto2L-4Jets_MLL-50to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=437,
    n_events=74271754,
)

cpn.add_dataset(
    name="dy_m50to120_ht400to800_madgraph",
    id=14895172,
    processes=[procs.dy_m50to120_ht400to800],
    keys=[
        "/DYto2L-4Jets_MLL-50to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=2285923,
)

####################################################################################################
#
# W boson production
#
####################################################################################################

#
# NLO
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14979374,
    processes=[procs.w_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
            ],
            n_files=438,
            n_events=192893909,
        ),
    ),
)
# TODO: add processes
# cpn.add_dataset(
#     name="w_lnu_0j_amcatnlo",
#     id=14894802,
#     processes=[procs.w_lnu_0j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=1360,
#             n_events=400648969,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_amcatnlo",
#     id=14912447,
#     processes=[procs.w_lnu_1j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=1151,
#             n_events=308622412,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_amcatnlo",
#     id=14911346,
#     processes=[procs.w_lnu_2j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=848,
#             n_events=193796359,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu40to100_amcatnlo",
#     id=14895723,
#     processes=[procs.w_lnu_1j_ptlnu40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=888,
#             n_events=193901377,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu100to200_amcatnlo",
#     id=14890740,
#     processes=[procs.w_lnu_1j_ptlnu100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=350,
#             n_events=83350855,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu200to400_amcatnlo",
#     id=14892269,
#     processes=[procs.w_lnu_1j_ptlnu200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=69,
#             n_events=5900365,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu400to600_amcatnlo",
#     id=14895155,
#     processes=[procs.w_lnu_1j_ptlnu400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=24,
#             n_events=996510,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu600toinf_amcatnlo",
#     id=14892680,
#     processes=[procs.w_lnu_1j_ptlnu600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=29,
#             n_events=939173,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu40to100_amcatnlo",
#     id=14892355,
#     processes=[procs.w_lnu_2j_ptlnu40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=932,
#             n_events=191631092,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu100to200_amcatnlo",
#     id=14892380,
#     processes=[procs.w_lnu_2j_ptlnu100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=424,
#             n_events=93835137,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu200to400_amcatnlo",
#     id=14894034,
#     processes=[procs.w_lnu_2j_ptlnu200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=76,
#             n_events=10381377,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu400to600_amcatnlo",
#     id=14890396,
#     processes=[procs.w_lnu_2j_ptlnu400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=28,
#             n_events=991432,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu600toinf_amcatnlo",
#     id=14898216,
#     processes=[procs.w_lnu_2j_ptlnu600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=39,
#             n_events=971987,
#         ),
#     ),
# )

# m_lnu 0-120 GeV, Ht binned

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht40to100_madgraph",
    id=14878169,
    processes=[procs.w_lnu_mlnu0to120_ht40to100],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1675,
    n_events=274494348,
)

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht100to400_madgraph",
    id=14880649,
    processes=[procs.w_lnu_mlnu0to120_ht100to400],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=1134,
    n_events=185590464,
)

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht400to800_madgraph",
    id=14885056,
    processes=[procs.w_lnu_mlnu0to120_ht400to800],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=367,
    n_events=26674759,
)

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht800to1500_madgraph",
    id=14959801,
    processes=[procs.w_lnu_mlnu0to120_ht800to1500],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v5/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=2874681,
)

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht1500to2500_madgraph",
    id=14930587,
    processes=[procs.w_lnu_mlnu0to120_ht1500to2500],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=1031962,
)

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht2500toinf_madgraph",
    id=14930797,
    processes=[procs.w_lnu_mlnu0to120_ht2500toinf],
    keys=[
        "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=920162,
)

####################################################################################################
#
# Diboson
#
####################################################################################################

#
# WW
#

cpn.add_dataset(
    name="ww_pythia",
    id=14784470,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=125,
            n_events=33504000,
        ),
    ),
)
cpn.add_dataset(
    name="ww_fh_powheg",
    id=14888427,
    processes=[procs.ww_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM",  # noqa
            ],
            n_files=258,
            n_events=55526000,
        ),
    ),
)
cpn.add_dataset(
    name="ww_dl_powheg",
    id=14888370,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v4/NANOAODSIM",  # noqa
            ],
            n_files=82,
            n_events=12951000,
        ),
    ),
)
cpn.add_dataset(
    name="ww_sl_powheg",
    id=14836299,
    processes=[procs.ww_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
            ],
            n_files=267,
            n_events=53764000,
        ),
    ),
)

#
# WZ
#

cpn.add_dataset(
    name="wz_pythia",
    id=14789850,
    processes=[procs.wz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=16770000,
        ),
    ),
)

#
# ZZ
#

cpn.add_dataset(
    name="zz_pythia",
    id=14788275,
    processes=[procs.zz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=2517000,
        ),
    ),
)

####################################################################################################
#
# Triboson
#
####################################################################################################

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14808800,
    processes=[procs.wwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=3600000,
        ),
    ),
)
cpn.add_dataset(
    name="www_amcatnlo",
    id=14808797,
    processes=[procs.www],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=936000,
        ),
    ),
)
