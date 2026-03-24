# coding: utf-8

"""
Recorded datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15 import campaign_run3_2022_preEE_nano_uhh_v14_trg_v15 as cpn


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
    n_files=18 + 99,
    n_events=20_162_441 + 138_329_693,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 18,
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
    n_files=63,
    n_events=75_440_027,
    aux={
        "merging_factors": {
            "nominal": 16,
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
    n_files=210,
    n_events=263_549_470,
    aux={
        "merging_factors": {
            "nominal": 16,
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
    n_files=87,
    n_events=89_134_996,
    aux={
        "merging_factors": {
            "nominal": 14,
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
    n_files=27,
    n_events=25_903_135,
    aux={
        "merging_factors": {
            "nominal": 14,
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
    n_files=18,
    n_events=16_686_692,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)
