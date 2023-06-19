# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# DiJet
#

cpn.add_dataset(
    name="data_dijet_a",
    id=14260294, # from das
    is_data=True,
    processes=[procs.data_dijet],
    keys=[
        "/JetHT/Run2018A-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=281,
    n_events=171484635,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_dijet_b",
    id=14260659,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/JetHT/Run2018B-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=128,
    n_events=78255208,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_dijet_c",
    id=14260590,
    is_data=True,
    processes=[procs.data_dijet],
    keys=[
        "/JetHT/Run2018C-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=138,
    n_events=70027804,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_dijet_d",
    id=14324490,
    is_data=True,
    processes=[procs.data_dijet],
    keys=[
        "/JetHT/Run2018D-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD",
    ],
    n_files=538,
    n_events=356967606,
    aux={
        "era": "D",
    },
)
