# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

from order import DatasetInfo

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
    is_data=True,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2022E-22Sep2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,  # 29-0
            n_events=12873327,
        ),
    ),
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=14784482,
    is_data=True,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2022F-22Sep2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2022F/MuonEG/NANOAOD/22Sep2023-v1/50000/4d76213a-ef14-411a-9558-559a6df3f978.root",  # empty  # noqa: E501
                    "/store/data/Run2022F/MuonEG/NANOAOD/22Sep2023-v1/50000/4fb72196-3b02-4499-8f6c-a54e15692b32.root",  # empty  # noqa: E501
                ],
            },
            n_files=93,  # 95-2
            n_events=38219969,
        ),
    ),
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=14784485,
    is_data=True,
    processes=[procs.data_muoneg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2022G-22Sep2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2022G/MuonEG/NANOAOD/22Sep2023-v1/2520000/cd404eb6-8218-4787-b5ed-af6cd9fe3750.root",  # empty  # noqa: E501
                ],
            },
            n_files=26,  # 27-1
            n_events=6238527,
        ),
    ),
    aux={
        "era": "G",
    },
)


#
# MET
#


cpn.add_dataset(
    name="data_jethtmet_e",
    id=14853647,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET/Run2022E-19Dec2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=185,  # 185-0
            n_events=140001854,
        ),
    ),
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_jethtmet_f",
    id=14853355,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET/Run2022F-19Dec2023-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=722,  # 722-0
            n_events=514342877,
        ),
    ),
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_jethtmet_g",
    id=14853371,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET/Run2022G-19Dec2023-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=139,  # 139-0
            n_events=84795124,
        ),
    ),
    aux={
        "era": "G",
    },
)
