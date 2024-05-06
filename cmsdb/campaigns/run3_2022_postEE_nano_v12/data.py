# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


#
# Muon
#


cpn.add_dataset(
    name="data_mu_e",
    id=14784109,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=147,
    n_events=141460608,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14826624,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022F-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=359,
    n_events=449887248,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14784262,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022G-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=88,
    n_events=76689396,
    aux={
        "era": "G",
    },
)


#
# E/Gamma
#


cpn.add_dataset(
    name="data_egamma_e",
    id=14783260,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=188,
    n_events=148654795,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_egamma_f",
    id=14784299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022F-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=490,
    n_events=464373259,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_egamma_g",
    id=14826525,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022G-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=87,
    n_events=76807350,
    aux={
        "era": "G",
    },
)


#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_e",
    id=14783435,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=29,
    n_events=12873327,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=14784482,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=95,
    n_events=38219969,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=14784485,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=27,
    n_events=6238527,
    aux={
        "era": "G",
    },
)
