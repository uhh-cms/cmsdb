# coding: utf-8

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
    name="data_mu_d",
    id=14787686,  # id from Muon0 dataset
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/Muon1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=32 + 30,
    n_events=21462916 + 21463645,
    aux={
        "era": "D",
    },
)

#
# E/Gamma
#
cpn.add_dataset(
    name="data_egamma_d",
    id=14787876,  # id from EGamma0 dataset
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=33 + 30,
    n_events=22657211 + 22653287,
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
