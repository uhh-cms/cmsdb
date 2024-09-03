# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
CMS datasets from the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

# Add eras A and B also?

#
# Muon
#

cpn.add_dataset(
    name="data_mu_c_1",
    id=14786982,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=165,
    n_events=138943783,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_2",
    id=14787027,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=131,
    n_events=101615754,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_2_v2",
    id=14953406,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD",  # noqa
    ],
    n_files=108,
    n_events=138912262,
    aux={
        "era": "C",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_c_1",
    id=14786977,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=168,
    n_events=160108119,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_c_2",
    id=14786782,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=177,
    n_events=160049621,
    aux={
        "era": "C",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c",
    id=14786972,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=70,
    n_events=45176805,
    aux={
        "era": "C",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784848,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=41,
    n_events=24205121,
    aux={
        "era": "C",
    },
)

