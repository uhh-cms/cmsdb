# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


cpn.add_dataset(
    name="zprime_tt_m1000_w100_madgraph",
    id=15426440,
    processes=[procs.zprime_tt_m1000_w100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w10_madgraph",
    id=15447382,
    processes=[procs.zprime_tt_m1000_w10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-10_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1000_w300_madgraph",
    id=15426384,
    processes=[procs.zprime_tt_m1000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=328000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w120_madgraph",
    id=15638721,
    processes=[procs.zprime_tt_m1200_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w12_madgraph",
    id=15644849,
    processes=[procs.zprime_tt_m1200_w12],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-12_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1200_w360_madgraph",
    id=15484100,
    processes=[procs.zprime_tt_m1200_w360],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1200-W-360_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w140_madgraph",
    id=15639860,
    processes=[procs.zprime_tt_m1400_w140],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-140_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w14_madgraph",
    id=15597042,
    processes=[procs.zprime_tt_m1400_w14],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-14_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1400_w420_madgraph",
    id=15645374,
    processes=[procs.zprime_tt_m1400_w420],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1400-W-420_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=332000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w160_madgraph",
    id=15598434,
    processes=[procs.zprime_tt_m1600_w160],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-160_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w16_madgraph",
    id=15441749,
    processes=[procs.zprime_tt_m1600_w16],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-16_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=329000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1600_w480_madgraph",
    id=15649603,
    processes=[procs.zprime_tt_m1600_w480],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1600-W-480_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=332000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w180_madgraph",
    id=15448126,
    processes=[procs.zprime_tt_m1800_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-180_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w18_madgraph",
    id=15634092,
    processes=[procs.zprime_tt_m1800_w18],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-18_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=331000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m1800_w540_madgraph",
    id=15638295,
    processes=[procs.zprime_tt_m1800_w540],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-1800-W-540_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w200_madgraph",
    id=15632899,
    processes=[procs.zprime_tt_m2000_w200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,  # 33-0
            n_events=331000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w20_madgraph",
    id=15645739,
    processes=[procs.zprime_tt_m2000_w20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-20_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=328000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2000_w600_madgraph",
    id=15632069,
    processes=[procs.zprime_tt_m2000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w250_madgraph",
    id=15640872,
    processes=[procs.zprime_tt_m2500_w250],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-250_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w25_madgraph",
    id=15483513,
    processes=[procs.zprime_tt_m2500_w25],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-25_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m2500_w750_madgraph",
    id=15637928,
    processes=[procs.zprime_tt_m2500_w750],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-2500-W-750_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w300_madgraph",
    id=15598701,
    processes=[procs.zprime_tt_m3000_w300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-300_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w30_madgraph",
    id=15649814,
    processes=[procs.zprime_tt_m3000_w30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-30_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3000_w900_madgraph",
    id=15591153,
    processes=[procs.zprime_tt_m3000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w1050_madgraph",
    id=15646922,
    processes=[procs.zprime_tt_m3500_w1050],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-1050_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w350_madgraph",
    id=15646898,
    processes=[procs.zprime_tt_m3500_w350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-350_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m3500_w35_madgraph",
    id=15592578,
    processes=[procs.zprime_tt_m3500_w35],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-3500-W-35_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w120_madgraph",
    id=15640908,
    processes=[procs.zprime_tt_m400_w120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-120_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w40_madgraph",
    id=15629575,
    processes=[procs.zprime_tt_m400_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-40_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=30,  # 30-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m400_w4_madgraph",
    id=15595199,
    processes=[procs.zprime_tt_m400_w4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-400-W-4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w1200_madgraph",
    id=15597755,
    processes=[procs.zprime_tt_m4000_w1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-1200_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w400_madgraph",
    id=15620328,
    processes=[procs.zprime_tt_m4000_w400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4000_w40_madgraph",
    id=15587977,
    processes=[procs.zprime_tt_m4000_w40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4000-W-40_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=16,  # 16-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w1350_madgraph",
    id=15598420,
    processes=[procs.zprime_tt_m4500_w1350],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-1350_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w450_madgraph",
    id=15641088,
    processes=[procs.zprime_tt_m4500_w450],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-450_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m4500_w45_madgraph",
    id=15640796,
    processes=[procs.zprime_tt_m4500_w45],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-4500-W-45_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w150_madgraph",
    id=15447039,
    processes=[procs.zprime_tt_m500_w150],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-150_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w50_madgraph",
    id=15426380,
    processes=[procs.zprime_tt_m500_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=12,  # 12-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m500_w5_madgraph",
    id=15426383,
    processes=[procs.zprime_tt_m500_w5],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-500-W-5_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w1500_madgraph",
    id=15426437,
    processes=[procs.zprime_tt_m5000_w1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-1500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w500_madgraph",
    id=15446253,
    processes=[procs.zprime_tt_m5000_w500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-500_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m5000_w50_madgraph",
    id=15426248,
    processes=[procs.zprime_tt_m5000_w50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-5000-W-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,  # 14-0
            n_events=325000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w180_madgraph",
    id=15598710,
    processes=[procs.zprime_tt_m600_w180],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-180_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w60_madgraph",
    id=15634217,
    processes=[procs.zprime_tt_m600_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-60_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,  # 36-0
            n_events=329000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m600_w6_madgraph",
    id=15645494,
    processes=[procs.zprime_tt_m600_w6],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-600-W-6_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=322000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w1800_madgraph",
    id=15621255,
    processes=[procs.zprime_tt_m6000_w1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-1800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=331000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w600_madgraph",
    id=15436459,
    processes=[procs.zprime_tt_m6000_w600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-600_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m6000_w60_madgraph",
    id=15480342,
    processes=[procs.zprime_tt_m6000_w60],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-6000-W-60_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w210_madgraph",
    id=15599044,
    processes=[procs.zprime_tt_m700_w210],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-210_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w70_madgraph",
    id=15620017,
    processes=[procs.zprime_tt_m700_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-70_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=332000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m700_w7_madgraph",
    id=15646523,
    processes=[procs.zprime_tt_m700_w7],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-700-W-7_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w2100_madgraph",
    id=15641675,
    processes=[procs.zprime_tt_m7000_w2100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-2100_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w700_madgraph",
    id=15594151,
    processes=[procs.zprime_tt_m7000_w700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,  # 7-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m7000_w70_madgraph",
    id=15649852,
    processes=[procs.zprime_tt_m7000_w70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-7000-W-70_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w240_madgraph",
    id=15613759,
    processes=[procs.zprime_tt_m800_w240],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-240_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w80_madgraph",
    id=15509485,
    processes=[procs.zprime_tt_m800_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-80_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=4,  # 4-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m800_w8_madgraph",
    id=15598283,
    processes=[procs.zprime_tt_m800_w8],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-800-W-8_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w2400_madgraph",
    id=15435944,
    processes=[procs.zprime_tt_m8000_w2400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-2400_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w800_madgraph",
    id=15597873,
    processes=[procs.zprime_tt_m8000_w800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-800_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m8000_w80_madgraph",
    id=15618635,
    processes=[procs.zprime_tt_m8000_w80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-8000-W-80_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=332000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w270_madgraph",
    id=15617342,
    processes=[procs.zprime_tt_m900_w270],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-270_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w90_madgraph",
    id=15649952,
    processes=[procs.zprime_tt_m900_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-90_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=333000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m900_w9_madgraph",
    id=15620022,
    processes=[procs.zprime_tt_m900_w9],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-900-W-9_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=332000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w2700_madgraph",
    id=15646975,
    processes=[procs.zprime_tt_m9000_w2700],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-2700_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=330000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w900_madgraph",
    id=15640957,
    processes=[procs.zprime_tt_m9000_w900],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-900_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=331000,
        ),
    ),
)

cpn.add_dataset(
    name="zprime_tt_m9000_w90_madgraph",
    id=15649886,
    processes=[procs.zprime_tt_m9000_w90],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZPrimeToTT_Par-M-9000-W-90_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=333000,
        ),
    ),
)
