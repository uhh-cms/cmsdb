# coding: utf-8

"""
HHH -> bbbbWW datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 13, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_custom_v15 import campaign_run3_2024_nano_custom_v15 as cpn


#
# HHH
#

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c30_d4_custom",
    id=999001,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c30_d40],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=11,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c30_d499_custom",
    id=999002,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c30_d499],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_c3_0_d4_99_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c319_d419_custom",
    id=999003,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c319_d419],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_c3_19_d4_19_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c31_d40_custom",
    id=999004,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c31_d40],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c31_d42_custom",
    id=999005,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c31_d42],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c32_d4m1_custom",
    id=999006,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c32_d4m1],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c34_d49_custom",
    id=999007,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c34_d49],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c3m1_d40_custom",
    id=999008,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c3m1_d40],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=2,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c3m1_d4m1_custom",
    id=999009,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c3m1_d4m1],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)

cpn.add_dataset(
    name="hhh_4b2w_2l2nu_c3m1p5_d4m0p5_custom",
    id=999010,  # any unused ID
    processes=[procs.hhh_4b2w_2l2nu_c3m1p5_d4m0p5],  # adapt to your process
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "GF_HHH_Run3Summer24_merged.root",
            ],
            n_files=4,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)
