# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_e",
    id=14783091,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022E-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=120,
    n_events=148_661_479,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
        "era": "E",
    },
)

# TODO: might need re-merging as one lfn was broken
cpn.add_dataset(
    name="data_e_f",
    id=14783516,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022F-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=380,
    n_events=464_077_454,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_e_g",
    id=14826524,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022G-22Sep2023_NanoAODv12UHH-v2/NANOAOD",
    ],
    n_files=63,
    n_events=76_724_231,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
        "era": "G",
    },
)

#
# Muon
#

cpn.add_dataset(
    name="data_mu_e",
    id=14784108,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022E-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=96,
    n_events=141_480_973,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14826010,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022F-22Sep2023_NanoAODv12UHH-v2/NANOAOD",
    ],
    n_files=305,
    n_events=449_185_088,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14784261,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022G-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=52,
    n_events=76_689_396,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
        "era": "G",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_e",
    id=14784143,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022E-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=28,
    n_events=30_520_481,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14784499,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022F-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=107,
    n_events=115_472_800,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_tau_g",
    id=14784346,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022G-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=17,
    n_events=17_838_713,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
        "era": "G",
    },
)

#
# MET
#

cpn.add_dataset(
    name="data_met_e",
    id=14783096,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022E-22Sep2023_NanoAODv12UHH-v1/NANOAOD",
    ],
    n_files=160,
    n_events=138_964_668,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "E",
    },
)

# TODO: might need re-merging as five lfns were broken
cpn.add_dataset(
    name="data_met_f",
    id=14825994,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022F-22Sep2023_NanoAODv12UHH-v2/NANOAOD",
    ],
    n_files=601,
    n_events=514_319_264,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_met_g",
    id=14826192,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022G-22Sep2023_NanoAODv12UHH-v2/NANOAOD",
    ],
    n_files=102,
    n_events=84_696_790,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "G",
    },
)
