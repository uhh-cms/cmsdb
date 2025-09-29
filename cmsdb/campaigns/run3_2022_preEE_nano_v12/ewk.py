# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################

# inclusive, LO, forPog
cpn.add_dataset(
    name="dy_m50toinf_for_pog_madgraph",
    id=14802794,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv12-forPOG_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=27096229,
)

#
# NLO
#
cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14950158,
    processes=[procs.dy_m4to10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=624,
            n_events=99285491,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14803891,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=141,
            n_events=67681922,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
            ],
            n_files=73,
            n_events=47494002,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14796042,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=115,
            n_events=65997137,
        ),
        extension=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
            ],
            n_files=259,
            n_events=97500666,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14791297,
    processes=[procs.dy_m50toinf_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=173,
            n_events=105230672,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14791387,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=99076102,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14790870,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=177,
            n_events=75705368,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14826040,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=215,
            n_events=47125505,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14825639,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=168,
            n_events=18503737,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14826712,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=1939721,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14823834,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=503786,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14831319,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=508646,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14826102,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=81,
            n_events=18752305,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14826076,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=174,
            n_events=18592664,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14825454,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=3549847,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14824816,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=488707,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14826080,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=474576,
        ),
    ),
)

# DY m_ll 4-50 GeV, HT-binned,

cpn.add_dataset(
    name="dy_m4to50_ht40to70_madgraph",
    id=14949230,
    processes=[procs.dy_m4to50_ht40to70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=624,
            n_events=94731405,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht70to100_madgraph",
    id=14952860,
    processes=[procs.dy_m4to50_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=583,
            n_events=59168456,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht100to400_madgraph",
    id=14950528,
    processes=[procs.dy_m4to50_ht100to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=459,
            n_events=61642038,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht400to800_madgraph",
    id=14950277,
    processes=[procs.dy_m4to50_ht400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=1245442,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht800to1500_madgraph",
    id=14949446,
    processes=[procs.dy_m4to50_ht800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=67,
            n_events=994723,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht1500to2500_madgraph",
    id=14947931,
    processes=[procs.dy_m4to50_ht1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=966928,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m4to50_ht2500toinf_madgraph",
    id=14953120,
    processes=[procs.dy_m4to50_ht2500toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-4to50_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=74,
            n_events=1078931,
        ),
    ),
)

# DY m_ll 50-120 GeV, HT-binned,

cpn.add_dataset(
    name="dy_m50to120_ht40to70_madgraph",
    id=14815946,
    processes=[procs.dy_m50to120_ht40to70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50to120_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=40420484,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50to120_ht70to100_madgraph",
    id=14813985,
    processes=[procs.dy_m50to120_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50to120_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=72,
            n_events=29650452,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50to120_ht100to400_madgraph",
    id=14821740,
    processes=[procs.dy_m50to120_ht100to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=127,
            n_events=35470534,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50to120_ht400to800_madgraph",
    id=14815864,
    processes=[procs.dy_m50to120_ht400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-4Jets_MLL-50to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=1089838,
        ),
    ),
)

# TODO: implement corresponding processes + xsecs
# # ptll and jet-binned, NLO
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll40to100_amcatnlo",
#     id=14825993,
#     processes=[procs.dy_m50toinf_1j_ptll40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=287,
#             n_events=163904854,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll100to200_amcatnlo",
#     id=14826169,
#     processes=[procs.dy_m50toinf_1j_ptll100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=183,
#             n_events=64510280,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll200to400_amcatnlo",
#     id=14824736,
#     processes=[procs.dy_m50toinf_1j_ptll200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=61,
#             n_events=6583092,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll400to600_amcatnlo",
#     id=14826052,
#     processes=[procs.dy_m50toinf_1j_ptll400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=38,
#             n_events=1722633,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_1j_ptll600toinf_amcatnlo",
#     id=14870369,
#     processes=[procs.dy_m50toinf_1j_ptll600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=33,
#             n_events=1862921,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll40to100_amcatnlo",
#     id=14868304,
#     processes=[procs.dy_m50toinf_2j_ptll40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=406,
#             n_events=66554879,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll100to200_amcatnlo",
#     id=14870830,
#     processes=[procs.dy_m50toinf_2j_ptll100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=356,
#             n_events=70249250,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll200to400_amcatnlo",
#     id=14853119,
#     processes=[procs.dy_m50toinf_2j_ptll200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=93,
#             n_events=12661552,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll400to600_amcatnlo",
#     id=14827368,
#     processes=[procs.dy_m50toinf_2j_ptll400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=48,
#             n_events=1739647,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="dy_m50toinf_2j_ptll600toinf_amcatnlo",
#     id=14824689,
#     processes=[procs.dy_m50toinf_2j_ptll600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#             ],
#             n_files=25,
#             n_events=1682240,
#         ),
#     ),
# )


####################################################################################################
#
# W boson production
#
####################################################################################################

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803995,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=148,
    n_events=84739011,
)

# m_lnu 0-120 GeV, Ht binned

cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht40to100_madgraph",
    id=14848710,
    processes=[procs.w_lnu_mlnu0to120_ht40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=1429,
            n_events=146630714,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht100to400_madgraph",
    id=14846457,
    processes=[procs.w_lnu_mlnu0to120_ht100to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=606,
            n_events=100572216,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht400to800_madgraph",
    id=14814846,
    processes=[procs.w_lnu_mlnu0to120_ht400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=111,
            n_events=13533118,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht800to1500_madgraph",
    id=14892501,
    processes=[procs.w_lnu_mlnu0to120_ht800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=1432995,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht1500to2500_madgraph",
    id=14892061,
    processes=[procs.w_lnu_mlnu0to120_ht1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=477881,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu0to120_ht2500toinf_madgraph",
    id=14892471,
    processes=[procs.w_lnu_mlnu0to120_ht2500toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-0to120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=514983,
        ),
    ),
)

# m_lnu 120 GeV, Ht binned

cpn.add_dataset(
    name="w_lnu_mlnu120_ht40to100_madgraph",
    id=14881688,
    processes=[procs.w_lnu_mlnu120_ht40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-40to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=4532184,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu120_ht100to400_madgraph",
    id=14881523,
    processes=[procs.w_lnu_mlnu120_ht100to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=2132100,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu120_ht400to800_madgraph",
    id=14881746,
    processes=[procs.w_lnu_mlnu120_ht400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=506334,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu120_ht800to1500_madgraph",
    id=14881792,
    processes=[procs.w_lnu_mlnu120_ht800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=483978,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu120_ht1500to2500_madgraph",
    id=14881353,
    processes=[procs.w_lnu_mlnu120_ht1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=486619,
        ),
    ),
)
cpn.add_dataset(
    name="w_lnu_mlnu120_ht2500toinf_madgraph",
    id=14881829,
    processes=[procs.w_lnu_mlnu120_ht2500toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_MLNu-120_HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=489635,
        ),
    ),
)

#
# Diboson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800098,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=15357390,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14803901,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=46 - 1,  # 1 file missing 07.08.25
    n_events=7527043,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14808010,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=1181750,
)
