# coding: utf-8

"""
Recorded datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14 import campaign_run3_2022_preEE_nano_uhh_v14 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14784103,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
        "/Muon/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=16 + 89,
    n_events=20_162_441 + 138_329_693,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 20,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14783356,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022D-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=56,
    n_events=75_440_027,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c",
    id=14784124,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=16,
    n_events=15_768_439,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14784162,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2022D-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=9,
    n_events=8_007_031,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)


#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_c",
    id=14784139,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=187,
    n_events=263_549_470,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=14783296,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2022D-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=82,
    n_events=89_134_996,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c",
    id=14784152,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=25,
    n_events=25_903_135,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14783293,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022D-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=17,
    n_events=16_686_692,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)

#
# Jet/MET
#

cpn.add_dataset(
    name="data_met_c",
    id=14784128,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022C-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=162,
    n_events=169_113_266,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14809044,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022D-22Sep2023_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=122,
    n_events=100_853_361,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)
