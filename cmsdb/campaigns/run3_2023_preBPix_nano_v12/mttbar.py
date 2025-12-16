# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


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
