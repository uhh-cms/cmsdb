# coding: utf-8

"""
Recorded datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn


#
# Muon
#

cpn.add_dataset(
    name="data_mu_d_1",
    id=14787753,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=82 + 84,
    n_events=100_211_533 + 100_281_976,
    aux={
        "merging_factors": {
            "nominal": 19,
            "nominal_ext1": 18,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_d_2",
    id=14787624,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=19 + 19,
    n_events=21_462_916 + 21_463_645,
    aux={
        "merging_factors": {
            "nominal": 20,
            "nominal_ext1": 19,
        },
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_d_1",
    id=14786983,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=106 + 113,
    n_events=105_892_646 + 105_850_543,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 15,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_d_2",
    id=14787826,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=25 + 25,
    n_events=22_657_211 + 22_653_287,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 16,
        },
        "era": "D",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_d_1",
    id=14787583,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=39,
    n_events=32_092_659,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_d_2",
    id=14786909,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=9,
    n_events=7_246_202,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "D",
    },
)

#
# Jet/MET
#

cpn.add_dataset(
    name="data_met_d_1",
    id=14787275,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=76 + 77,
    n_events=61_507_467 + 61_491_693,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_d_2",
    id=14787322,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=17 + 17,
    n_events=13_254_510 + 13_252_102,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "D",
    },
)
