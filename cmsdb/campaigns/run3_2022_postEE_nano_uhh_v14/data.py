# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_e",
    id=14783091,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022E-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=136,
    n_events=148_661_479,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=14783516,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022F-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=452,
    n_events=464_077_454,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_e_reproc_f",
    id=14853821,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022F-19Dec2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=479,
    n_events=463_294_611,
    aux={
        "merging_factors": {
            "nominal": 15,
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
        "/EGamma/Run2022G-22Sep2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=78,
    n_events=76_724_231,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_e_reproc_g",
    id=14853933,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022G-19Dec2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=83,
    n_events=76_638_647,
    aux={
        "merging_factors": {
            "nominal": 16,
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
        "/Muon/Run2022E-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=113,
    n_events=141_480_973,
    aux={
        "merging_factors": {
            "nominal": 17,
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
        "/Muon/Run2022F-22Sep2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=372,
    n_events=449_185_088,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_reproc_f",
    id=14853509,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022F-19Dec2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=410,
    n_events=449_047_272,
    aux={
        "merging_factors": {
            "nominal": 17,
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
        "/Muon/Run2022G-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=66,
    n_events=76_689_396,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_mu_reproc_g",
    id=14853828,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022G-19Dec2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=71,
    n_events=76_499_845,
    aux={
        "merging_factors": {
            "nominal": 18,
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
        "/Tau/Run2022E-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=34,
    n_events=30_520_481,
    aux={
        "merging_factors": {
            "nominal": 13,
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
        "/Tau/Run2022F-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=127,
    n_events=115_472_800,
    aux={
        "merging_factors": {
            "nominal": 16,
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
        "/Tau/Run2022G-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=21,
    n_events=17_838_713,
    aux={
        "merging_factors": {
            "nominal": 16,
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
        "/JetMET/Run2022E-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=173,
    n_events=138_964_668,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_reproc_e",
    id=14853613,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022E-19Dec2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=184,
    n_events=140_001_854,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=14825994,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022F-22Sep2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=644,
    n_events=514_319_264,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_met_reproc_f",
    id=14853289,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022F-19Dec2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=704,
    n_events=514_498_319,
    aux={
        "merging_factors": {
            "nominal": 13,
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
        "/JetMET/Run2022G-22Sep2023_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=109,
    n_events=84_696_790,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_met_reproc_g",
    id=14853288,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022G-19Dec2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=114,
    n_events=84_795_124,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "G",
    },
)
