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
    name="data_mu_d1",
    id=14787767,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/Muon1/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=125 + 100,
    n_events=100291308 + 100281976,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_d2",
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
    name="data_egamma_d1",
    id=14786984,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=124 + 104,
    n_events=105892646 + 105824276,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_egamma_d2",
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
    name="data_tau_d1",
    id=14787584,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=42,
    n_events=32092659,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_d2",
    id=14786907,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=13,
    n_events=7246202,
    is_data=True,
    aux={
        "era": "D",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_d1",
    id=14787219,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=17530531,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muoneg_d2",
    id=14787200,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=11,
    n_events=3751587,
    is_data=True,
    aux={
        "era": "D",
    },
)

#
# JetMET
#

cpn.add_dataset(
    name="data_jethtmet_d1",
    id=14787276,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023D-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=70 + 80,
    n_events=61507467 + 61491693,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_jethtmet_d2",
    id=14787323,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023D-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=22 + 25,
    n_events=13254510 + 13252102,
    is_data=True,
    aux={
        "era": "D",
    },
)
