# coding: utf-8

"""
CMS datasets from the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# Muon
#
cpn.add_dataset(
    name="data_mu_c",
    id=14786982,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
        "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD",  # noqa
    ],
    n_files=165 + 108,
    n_events=138943783 + 138912262,
    aux={
        "era": "Cv4",
    },
)

#
# E/Gamma
#
cpn.add_dataset(
    name="data_egamma_c",
    id=14786977,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=168 + 177,
    n_events=160108119 + 160049621,
    aux={
        "era": "Cv4",
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
        "era": "Cv4",
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
        "era": "Cv4",
    },
)
