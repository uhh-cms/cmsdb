# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

# Z'->ttbar samples generated with MadGraph

cpn.add_dataset(
    name="zprime_tt_m1000_w100_madgraph",
    id=15537046,
    processes=[procs.zprime_tt_m1000_w100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w10_madgraph",
    id=15537552,
    processes=[procs.zprime_tt_m1000_w10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-10_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w300_madgraph",
    id=15541577,
    processes=[procs.zprime_tt_m1000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=30,  # 30-0
            n_events=121000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w120_madgraph",
    id=15620592,
    processes=[procs.zprime_tt_m1200_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w12_madgraph",
    id=15581507,
    processes=[procs.zprime_tt_m1200_w12],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-12_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w360_madgraph",
    id=15629043,
    processes=[procs.zprime_tt_m1200_w360],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-360_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w140_madgraph",
    id=15628315,
    processes=[procs.zprime_tt_m1400_w140],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-140_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w14_madgraph",
    id=15578437,
    processes=[procs.zprime_tt_m1400_w14],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-14_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w420_madgraph",
    id=15595117,
    processes=[procs.zprime_tt_m1400_w420],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-420_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=121000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w160_madgraph",
    id=15578275,
    processes=[procs.zprime_tt_m1600_w160],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-160_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w16_madgraph",
    id=15627646,
    processes=[procs.zprime_tt_m1600_w16],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-16_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w480_madgraph",
    id=15588611,
    processes=[procs.zprime_tt_m1600_w480],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-480_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w180_madgraph",
    id=15581559,
    processes=[procs.zprime_tt_m1800_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-180_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=123000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w18_madgraph",
    id=15620832,
    processes=[procs.zprime_tt_m1800_w18],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-18_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w540_madgraph",
    id=15447886,
    processes=[procs.zprime_tt_m1800_w540],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-540_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w200_madgraph",
    id=15627693,
    processes=[procs.zprime_tt_m2000_w200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w20_madgraph",
    id=15580614,
    processes=[procs.zprime_tt_m2000_w20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-20_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2,  # 2-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w600_madgraph",
    id=15597481,
    processes=[procs.zprime_tt_m2000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=119000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w250_madgraph",
    id=15480326,
    processes=[procs.zprime_tt_m2500_w250],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-250_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w25_madgraph",
    id=15618472,
    processes=[procs.zprime_tt_m2500_w25],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-25_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w750_madgraph",
    id=15599088,
    processes=[procs.zprime_tt_m2500_w750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-750_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w300_madgraph",
    id=15596784,
    processes=[procs.zprime_tt_m3000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w30_madgraph",
    id=15620371,
    processes=[procs.zprime_tt_m3000_w30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-30_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w900_madgraph",
    id=15592227,
    processes=[procs.zprime_tt_m3000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w1050_madgraph",
    id=15594353,
    processes=[procs.zprime_tt_m3500_w1050],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-1050_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w350_madgraph",
    id=15571829,
    processes=[procs.zprime_tt_m3500_w350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-350_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w35_madgraph",
    id=15572483,
    processes=[procs.zprime_tt_m3500_w35],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-35_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w120_madgraph",
    id=15469519,
    processes=[procs.zprime_tt_m400_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w40_madgraph",
    id=15594070,
    processes=[procs.zprime_tt_m400_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-40_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w4_madgraph",
    id=15594701,
    processes=[procs.zprime_tt_m400_w4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w1200_madgraph",
    id=15620796,
    processes=[procs.zprime_tt_m4000_w1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w400_madgraph",
    id=15571673,
    processes=[procs.zprime_tt_m4000_w400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w40_madgraph",
    id=15613781,
    processes=[procs.zprime_tt_m4000_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-40_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w1350_madgraph",
    id=15458969,
    processes=[procs.zprime_tt_m4500_w1350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-1350_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w450_madgraph",
    id=15628327,
    processes=[procs.zprime_tt_m4500_w450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-450_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w45_madgraph",
    id=15613706,
    processes=[procs.zprime_tt_m4500_w45],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-45_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w150_madgraph",
    id=15539928,
    processes=[procs.zprime_tt_m500_w150],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-150_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w50_madgraph",
    id=15447984,
    processes=[procs.zprime_tt_m500_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w5_madgraph",
    id=15549379,
    processes=[procs.zprime_tt_m500_w5],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-5_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w1500_madgraph",
    id=15537012,
    processes=[procs.zprime_tt_m5000_w1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w500_madgraph",
    id=15537753,
    processes=[procs.zprime_tt_m5000_w500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w50_madgraph",
    id=15537656,
    processes=[procs.zprime_tt_m5000_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w180_madgraph",
    id=15626569,
    processes=[procs.zprime_tt_m600_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-180_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w60_madgraph",
    id=15584376,
    processes=[procs.zprime_tt_m600_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-60_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w6_madgraph",
    id=15585717,
    processes=[procs.zprime_tt_m600_w6],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-6_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w1800_madgraph",
    id=15620885,
    processes=[procs.zprime_tt_m6000_w1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w600_madgraph",
    id=15627785,
    processes=[procs.zprime_tt_m6000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w60_madgraph",
    id=15629282,
    processes=[procs.zprime_tt_m6000_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-60_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w210_madgraph",
    id=15578271,
    processes=[procs.zprime_tt_m700_w210],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-210_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w70_madgraph",
    id=15594781,
    processes=[procs.zprime_tt_m700_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-70_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w7_madgraph",
    id=15628411,
    processes=[procs.zprime_tt_m700_w7],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-7_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w2100_madgraph",
    id=15588978,
    processes=[procs.zprime_tt_m7000_w2100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-2100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w700_madgraph",
    id=15613687,
    processes=[procs.zprime_tt_m7000_w700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w70_madgraph",
    id=15587444,
    processes=[procs.zprime_tt_m7000_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-70_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=123000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w240_madgraph",
    id=15620352,
    processes=[procs.zprime_tt_m800_w240],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-240_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w80_madgraph",
    id=15614446,
    processes=[procs.zprime_tt_m800_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-80_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w8_madgraph",
    id=15620976,
    processes=[procs.zprime_tt_m800_w8],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-8_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w2400_madgraph",
    id=15591197,
    processes=[procs.zprime_tt_m8000_w2400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w800_madgraph",
    id=15628931,
    processes=[procs.zprime_tt_m8000_w800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w80_madgraph",
    id=15615060,
    processes=[procs.zprime_tt_m8000_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-80_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,  # 8-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w270_madgraph",
    id=15627128,
    processes=[procs.zprime_tt_m900_w270],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-270_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w90_madgraph",
    id=15628485,
    processes=[procs.zprime_tt_m900_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-90_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w9_madgraph",
    id=15586240,
    processes=[procs.zprime_tt_m900_w9],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-9_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=124000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w2700_madgraph",
    id=15469642,
    processes=[procs.zprime_tt_m9000_w2700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-2700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w900_madgraph",
    id=15583405,
    processes=[procs.zprime_tt_m9000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=125000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w90_madgraph",
    id=15591309,
    processes=[procs.zprime_tt_m9000_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-90_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=124000,
        ),
    ),
)

