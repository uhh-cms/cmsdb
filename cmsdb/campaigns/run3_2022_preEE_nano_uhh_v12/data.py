# coding: utf-8

"""
Recorded datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn  # noqa


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=14784126,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022C-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=94,
    n_events=138_329_693,
    aux={
        "merging_factors": {
            "nominal": 19,
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
        "/Muon/Run2022D-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=51,
    n_events=75_440_027,
    aux={
        "merging_factors": {
            "nominal": 20,
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
        "/EGamma/Run2022C-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=198,
    n_events=263_549_470,
    aux={
        "merging_factors": {
            "nominal": 17,
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
        "/EGamma/Run2022D-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=72,
    n_events=89_134_996,
    aux={
        "merging_factors": {
            "nominal": 17,
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
        "/Tau/Run2022C-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=23,
    n_events=25_903_135,
    aux={
        "merging_factors": {
            "nominal": 16,
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
        "/Tau/Run2022D-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=16,
    n_events=16_686_692,
    aux={
        "merging_factors": {
            "nominal": 16,
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
    id=14853683,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022C-19Dec2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=193,
    n_events=169_968_073,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "C",
        "jec_era": "RunCD",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14853651,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET/Run2022D-19Dec2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=121,
    n_events=101_270_969,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "D",
        "jec_era": "RunCD",
    },
)
