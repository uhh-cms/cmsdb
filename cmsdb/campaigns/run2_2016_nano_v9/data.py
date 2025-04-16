# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#
# JetHT
#

cpn.add_dataset(
    name="data_jetht_f",
    id=14233419,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=5,
    n_events=6613811,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_jetht_g",
    id=14240214,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=70,
    n_events=120688407,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_jetht_h",
    id=14233810,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=72,
    n_events=124050331,
    aux={
        "era": "H",
    },
)
