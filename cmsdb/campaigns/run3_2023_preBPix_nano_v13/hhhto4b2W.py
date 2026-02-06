# coding: utf-8

"""
HHH -> bbbbWW datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 13, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v13 import campaign_run3_2023_preBPix_nano_v13 as cpn


#
# HHH
#


cpn.add_dataset(
    name="hhh_4b2w_c30_d40_amcatnlo",
    id=15263718,
    processes=[procs.hhh_4b2w_c30_d40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=56,  # 56-0
            n_events=1585922,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c30_d499_amcatnlo",
    id=15264113,
    processes=[procs.hhh_4b2w_c30_d499],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=599982,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c30_d4m1_amcatnlo",
    id=15266196,
    processes=[procs.hhh_4b2w_c30_d4m1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=599969,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c319_d419_amcatnlo",
    id=15271703,
    processes=[procs.hhh_4b2w_c319_d419],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=596969,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c31_d40_amcatnlo",
    id=15271704,
    processes=[procs.hhh_4b2w_c31_d40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,  # 36-0
            n_events=590970,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c31_d42_amcatnlo",
    id=15268265,
    processes=[procs.hhh_4b2w_c31_d42],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,  # 26-0
            n_events=585970,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c32_d4m1_amcatnlo",
    id=15265114,
    processes=[procs.hhh_4b2w_c32_d4m1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,  # 21-0
            n_events=599964,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c34_d49_amcatnlo",
    id=15263890,
    processes=[procs.hhh_4b2w_c34_d49],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,  # 9-0
            n_events=599968,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c3m1_d40_amcatnlo",
    id=15264872,
    processes=[procs.hhh_4b2w_c3m1_d40],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=32,  # 32-0
            n_events=575959,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c3m1_d4m1_amcatnlo",
    id=15268183,
    processes=[procs.hhh_4b2w_c3m1_d4m1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-minus1_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=593964,
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_c3m1p5_d4m0p5_amcatnlo",
    id=15266333,
    processes=[procs.hhh_4b2w_c3m1p5_d4m0p5],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/HHHto4B2Wto2L2Nu_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,  # 24-0
            n_events=599965,
        ),
    ),
)
