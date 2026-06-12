# coding: utf-8

""""
QCD datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# QCD
#

# muon enriched, pt-binned
cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=15316273,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_Bin-PT-15to20_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=859,
    n_events=124_873_343,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=15315886,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_Bin-PT-20to30_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=657,
    n_events=93_246_015,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=15315309,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_Bin-PT-30to50_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=729,
    n_events=95_229_839,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=15316568,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_Bin-PT-50to80_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=714,
    n_events=107_361_868,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=15316584,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=680,
    n_events=94_158_748,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=15316135,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=683,
    n_events=99_977_764,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=15315581,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=695,
    n_events=94_354_003,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=15315699,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=591,
    n_events=79_686_379,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=15316109,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=590,
    n_events=71_842_009,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=15315212,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=764,
    n_events=85_759_452,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=15315633,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=673 - 1,
    n_events=81_633_640,
    aux={
        "broken_files": [
            "/store/mc/RunIII2024Summer24NanoAODv15/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/NANOAODSIM/150X_mcRun3_2024_realistic_v2-v2/2550000/a7d8632e-0a31-4d72-9d55-65df40527939.root",
        ],  # FIXME doesn't work like this..., I deleted the file from the LFN task output.
    },
)

cpn.add_dataset(
    name="qcd_mu_pt1000toinf_pythia",
    id=15316533,
    processes=[procs.qcd_mu_pt1000toinf],
    keys=[
        "/QCD_Bin-PT-1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=703,
    n_events=87_267_908,
)

# double em enriched, pt > 30, 40 < m_gg < 80
cpn.add_dataset(
    name="qcd_doubleem_pt30toinf_mgg40to80_pythia",
    id=15316662,
    processes=[procs.qcd_doubleem_pt30toinf_mgg40to80],
    keys=[
        "/QCD_Bin-MGG-40to80-PT-30_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
    ],
    n_files=169,
    n_events=26_481_058,
)

# double em enriched, pt-binned, m_gg > 80
cpn.add_dataset(
    name="qcd_doubleem_pt30to40_mgg80toinf_pythia",
    id=15315165,
    processes=[procs.qcd_doubleem_pt30to40_mgg80toinf],
    keys=[
        "/QCD_Bin-MGG-80-PT-30to40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
    ],
    n_files=160,
    n_events=13_681_212,
)

cpn.add_dataset(
    name="qcd_doubleem_pt40toinf_mgg80toinf_pythia",
    id=15295980,
    processes=[procs.qcd_doubleem_pt40toinf_mgg80toinf],
    keys=[
        "/QCD_Bin-MGG-80-PT-40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
    ],
    n_files=190,
    n_events=27_404_416,
)

cpn.add_dataset(
    name="qcd_em_pt15to20_pythia",
    id=15533112,
    processes=[procs.qcd_em_pt15to20],
    keys=[
        "/QCD_Bin-PT-15to20_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=193,  # 193-0
    n_events=31078562,
)

cpn.add_dataset(
    name="qcd_em_pt20to30_pythia",
    id=15533221,
    processes=[procs.qcd_em_pt20to30],
    keys=[
        "/QCD_Bin-PT-20to30_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=175,  # 175-0
    n_events=27305022,
)

cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=15533148,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_Bin-PT-30to50_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=198,  # 198-0
    n_events=29008060,
)

cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=15533151,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_Bin-PT-50to80_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=218,  # 218-0
    n_events=29059468,
)

cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=15533309,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_Bin-PT-80to120_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=208,  # 208-0
    n_events=29437751,
)

cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=15533119,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_Bin-PT-120to170_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=213,  # 213-0
    n_events=27584498,
)

cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=15533528,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_Bin-PT-170to300_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=231,  # 231-0
    n_events=29515968,
)

cpn.add_dataset(
    name="qcd_em_pt300to470_pythia",
    id=15533244,
    processes=[procs.qcd_em_pt300to470],
    keys=[
        "/QCD_Bin-PT-300to470_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=181,  # 181-0
    n_events=30174212,
)

cpn.add_dataset(
    name="qcd_em_pt470to600_pythia",
    id=15533253,
    processes=[procs.qcd_em_pt470to600],
    keys=[
        "/QCD_Bin-PT-470to600_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=214,  # 214-0
    n_events=34732273,
)

cpn.add_dataset(
    name="qcd_em_pt600to800_pythia",
    id=15533455,
    processes=[procs.qcd_em_pt600to800],
    keys=[
        "/QCD_Bin-PT-600to800_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=249,  # 249-0
    n_events=32404726,
)

cpn.add_dataset(
    name="qcd_em_pt800to1000_pythia",
    id=15533186,
    processes=[procs.qcd_em_pt800to1000],
    keys=[
        "/QCD_Bin-PT-800to1000_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=243,  # 243-0
    n_events=32040195,
)

cpn.add_dataset(
    name="qcd_em_pt1000toinf_pythia",
    id=15533157,
    processes=[procs.qcd_em_pt1000toinf],
    keys=[
        "/QCD_Bin-PT-1000_Fil-EMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    aux={
        "broken_files": [],
    },
    n_files=182,  # 182-0
    n_events=22920551,
)

# ht-binned
cpn.add_dataset(
    name="qcd_ht40to70_madgraph",
    id=15301246,
    processes=[procs.qcd_ht40to70],
    keys=[
        "/QCD-4Jets_Bin-HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=123,
    n_events=110_777_315,
)

cpn.add_dataset(
    name="qcd_ht70to100_madgraph",
    id=15300355,
    processes=[procs.qcd_ht70to100],
    keys=[
        "/QCD-4Jets_Bin-HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=136,
    n_events=108_584_880,
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=15291916,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=169,
    n_events=120_453_600,
)

cpn.add_dataset(
    name="qcd_ht200to400_madgraph",
    id=15300347,
    processes=[procs.qcd_ht200to400],
    keys=[
        "/QCD-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=163,
    n_events=115_255_250,
)

cpn.add_dataset(
    name="qcd_ht400to600_madgraph",
    id=15300312,
    processes=[procs.qcd_ht400to600],
    keys=[
        "/QCD-4Jets_Bin-HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=173,
    n_events=106_725_734,
)

cpn.add_dataset(
    name="qcd_ht600to800_madgraph",
    id=15300360,
    processes=[procs.qcd_ht600to800],
    keys=[
        "/QCD-4Jets_Bin-HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=229,
    n_events=128_235_651,
)

cpn.add_dataset(
    name="qcd_ht800to1000_madgraph",
    id=15300390,
    processes=[procs.qcd_ht800to1000],
    keys=[
        "/QCD-4Jets_Bin-HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=262,
    n_events=124_956_604,
)

cpn.add_dataset(
    name="qcd_ht1000to1200_madgraph",
    id=15301287,
    processes=[procs.qcd_ht1000to1200],
    keys=[
        "/QCD-4Jets_Bin-HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=224,
    n_events=114_436_708,
)

cpn.add_dataset(
    name="qcd_ht1200to1500_madgraph",
    id=15291917,
    processes=[procs.qcd_ht1200to1500],
    keys=[
        "/QCD-4Jets_Bin-HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=230,
    n_events=107_835_822,
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=15300329,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD-4Jets_Bin-HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=248,
    n_events=113_208_234,
)

cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=15291920,
    processes=[procs.qcd_ht2000toinf],
    keys=[
        "/QCD-4Jets_Bin-HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=221,
    n_events=91_953_615,
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=15315319,
    processes=[procs.qcd_pt600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-600to800_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=690,  # 690-0
            n_events=79708520,
        ),
    ),
)

# cpn.add_dataset(
#     name="qcd_pt15to20_pythia",
#     id=15315874,
#     processes=[procs.qcd_pt15to20],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_Bin-PT-15to20_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=566,  # 566-0
#             n_events=99984691,
#         ),
#     ),
# )

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=15316542,
    processes=[procs.qcd_pt470to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-470to600_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=600,  # 600-0
            n_events=77529080,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=15315188,
    processes=[procs.qcd_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=660,  # 660-0
            n_events=97814968,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt2500to3000_pythia",
    id=15315583,
    processes=[procs.qcd_pt2500to3000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-2500to3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=222,  # 222-0
            n_events=19996725,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=15315306,
    processes=[procs.qcd_pt300to470],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-300to470_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=630,  # 630-0
            n_events=79821382,
        ),
    ),
)

# cpn.add_dataset(
#     name="qcd_pt20to30_pythia",
#     id=15316550,
#     processes=[procs.qcd_pt20to30],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_Bin-PT-20to30_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=578,  # 578-0
#             n_events=99972336,
#         ),
#     ),
# )

cpn.add_dataset(
    name="qcd_pt1000to1500_pythia",
    id=15315846,
    processes=[procs.qcd_pt1000to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-1000to1500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=621,  # 621-0
            n_events=79974618,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1500to2000_pythia",
    id=15315893,
    processes=[procs.qcd_pt1500to2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-1500to2000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=225,  # 225-0
            n_events=19997308,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=15315356,
    processes=[procs.qcd_pt800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-800to1000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=650,  # 650-0
            n_events=79505640,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt3000toinf_pythia",
    id=15315205,
    processes=[procs.qcd_pt3000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=315,  # 315-0
            n_events=19347697,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt30to50_pythia",
    id=15315325,
    processes=[procs.qcd_pt30to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-30to50_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=631,  # 631-0
            n_events=99983302,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=15316666,
    processes=[procs.qcd_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-120to170_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=668,  # 668-0
            n_events=99956202,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=15315195,
    processes=[procs.qcd_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-80to120_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=750,  # 750-0
            n_events=99244066,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt2000to2500_pythia",
    id=15315211,
    processes=[procs.qcd_pt2000to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-2000to2500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=250,  # 250-0
            n_events=19311060,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=15316566,
    processes=[procs.qcd_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-170to300_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=678,  # 678-0
            n_events=99860965,
        ),
    ),
)
