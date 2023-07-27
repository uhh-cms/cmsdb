# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_JMEnano_v9 import campaign_run2_2017_JMEnano_v9 as cpn


#
# DiJet
#

cpn.add_dataset(
    name="data_jetht_b",
    id=14260759,  # from das
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017B-UL2017_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=96,
    n_events=63043590,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14260769,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017C-UL2017_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=158,
    n_events=96264601,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetht_d",
    id=14260518,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017D-UL2017_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=89,
    n_events=46145204,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_jetht_e",
    id=14260363,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017E-UL2017_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=148,
    n_events=89630771,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_jetht_f",
    id=14260621,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2017F-UL2017_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=228,
    n_events=115429972,
    aux={
        "era": "F",
    },
)
