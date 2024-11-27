# coding: utf-8

"""
CMS datasets from the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn


#
# JetHT
#

cpn.add_dataset(
    name="data_jetht_a",
    id=14250828,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=146,
    n_events=171484635,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_jetht_b",
    id=14226541,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=45,
    n_events=78255208,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14226773,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=57,
    n_events=70027804,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetht_d",
    id=14324486,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=232,
    n_events=14324486,
    aux={
        "era": "D",
    },
)
