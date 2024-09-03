# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
CMS datasets from the 2023 postBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

# Add era E also?

#
# Muon
#

cpn.add_dataset(
    name="data_mu_d_1",
    id=14787686,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=21462916,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_d_2",
    id=14786997,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=21463645,
    aux={
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_d_1",
    id=14787876,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=33,
    n_events=22657211,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_egamma_d_2",
    id=14785166,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=30,
    n_events=22653287,
    aux={
        "era": "D",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_d",
    id=14786907,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=13,
    n_events=7246202,
    aux={
        "era": "D",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_d",
    id=14787200,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=11,
    n_events=3751587,
    aux={
        "era": "D",
    },
)