# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_uhh_v12 import campaign_run2_2016_nano_uhh_v12 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_f",
    id=14215635,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016F-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=4,
    n_events=8858206,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_e_g",
    id=14215504,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016G-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=64,
    n_events=153363109,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_e_h",
    id=14218981,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016H-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=56,
    n_events=129021893,
    aux={
        "era": "H",
    },
)


#
# SingleMuon
#

cpn.add_dataset(
    name="data_mu_f",
    id=14226884,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016F-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=3,
    n_events=8024195,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14218939,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016G-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=52,
    n_events=149916849,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_mu_h",
    id=14218989,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016H-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=62,
    n_events=174035164,
    aux={
        "era": "H",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_f",
    id=14216825,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016F-UL2016_NanoAODv12-v1/NANOAOD",  # noqa
    ],
    n_files=3,
    n_events=4360106,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_tau_g",
    id=14216980,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016G-UL2016_NanoAODv12-v1/NANOAOD",  # noqa
    ],
    n_files=39,
    n_events=79578661,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_tau_h",
    id=14217207,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016H-UL2016_NanoAODv12-v1/NANOAOD",  # noqa
    ],
    n_files=39,
    n_events=76758754,
    aux={
        "era": "H",
    },
)


#
# MET
#

cpn.add_dataset(
    name="data_met_f",
    id=14215626,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016F-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=1,
    n_events=1383250,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_met_g",
    id=14216287,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016G-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=13,
    n_events=26974131,
    aux={
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_met_h",
    id=14216437,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016H-UL2016_NanoAODv12-v2/NANOAOD",  # noqa
    ],
    n_files=18,
    n_events=39773485,
    aux={
        "era": "H",
    },
)
