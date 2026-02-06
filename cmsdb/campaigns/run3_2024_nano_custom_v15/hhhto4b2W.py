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
            n_files=1,
            n_events=1000000,  # can be approximate
            aux={
                "is_local": True,
            },
        ),
    ),
)
