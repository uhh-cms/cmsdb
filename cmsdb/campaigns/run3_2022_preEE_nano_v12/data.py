# coding: utf-8

"""
CMS datasets from the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# Muon
#


cpn.add_dataset(
    name="data_mu_c",
    id=14784127,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=124,
    n_events=138427345,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783357,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=82,
    n_events=75468381,
    aux={
        "era": "D",
    },
)


#
# E/Gamma
#


cpn.add_dataset(
    name="data_egamma_a",
    id=14783268,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022A-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=5,
    n_events=186,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_egamma_b",
    id=14826835,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022B-22Sep2023-v2/NANOAOD",  # noqa
    ],
    n_files=14,
    n_events=11074301,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_egamma_c",
    id=14784140,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=313,
    n_events=263689151,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14783299,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=109,
    n_events=89134996,
    aux={
        "era": "D",
    },
)


#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_a",
    id=14783289,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022A-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=5,
    n_events=12,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=14784076,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022B-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=7,
    n_events=254803,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784125,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022C-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=28,
    n_events=15768439,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14784209,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022D-22Sep2023-v1/NANOAOD",  # noqa
    ],
    n_files=16,
    n_events=8007031,
    aux={
        "era": "D",
    },
)
