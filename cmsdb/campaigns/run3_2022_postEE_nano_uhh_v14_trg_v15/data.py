# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14_trg_v15 import campaign_run3_2022_postEE_nano_uhh_v14_trg_v15 as cpn

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
    n_files=157,
    n_events=148_661_479,
    aux={
        "merging_factors": {
            "nominal": 13,
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
    n_files=516,
    n_events=464_077_454,
    aux={
        "merging_factors": {
            "nominal": 14,
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
    n_files=83,
    n_events=76_724_231,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "G",
    },
)

#
# MuonEG
#


cpn.add_dataset(
    name="data_muoneg_e",
    id=14783434,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022E-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=16,
    n_events=12_868_267,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "E",
    },
)

# NOTE: we had to veto rougly 900 events from this dataset due to one broken basket.
cpn.add_dataset(
    name="data_muoneg_f",
    id=14784358,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022F-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=48,
    n_events=38_215_918,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "F",
    },
)


cpn.add_dataset(
    name="data_muoneg_g",
    id=14784382,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022G-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=9,
    n_events=6_238_527,
    aux={
        "merging_factors": {
            "nominal": 14,
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
    n_files=120,
    n_events=141_480_973,
    aux={
        "merging_factors": {
            "nominal": 16,
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
    n_files=419,
    n_events=449_185_088,
    aux={
        "merging_factors": {
            "nominal": 16,
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
    n_files=74,
    n_events=76_689_396,
    aux={
        "merging_factors": {
            "nominal": 17,
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
    n_files=37,
    n_events=30_520_481,
    aux={
        "merging_factors": {
            "nominal": 12,
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
    n_files=145,
    n_events=115_472_800,
    aux={
        "merging_factors": {
            "nominal": 14,
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
    n_files=23,
    n_events=17_838_713,
    aux={
        "merging_factors": {
            "nominal": 14,
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
