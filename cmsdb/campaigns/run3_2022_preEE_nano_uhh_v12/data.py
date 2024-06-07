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
    n_files=177,
    n_events=138_329_693,
    aux={
        "nominal_merging_factor": 10,
        "era": "C",
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
    n_files=101,
    n_events=75_440_027,
    aux={
        "nominal_merging_factor": 10,
        "era": "D",
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
    n_files=373,
    n_events=263_549_470,
    aux={
        "nominal_merging_factor": 9,
        "era": "C",
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
    n_files=136,
    n_events=89_134_996,
    aux={
        "nominal_merging_factor": 9,
        "era": "D",
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
    n_files=46,
    n_events=25_903_135,
    aux={
        "nominal_merging_factor": 8,
        "era": "C",
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
    n_files=28,
    n_events=16_686_692,
    aux={
        "nominal_merging_factor": 9,
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
    n_files=359,
    n_events=169_968_073,
    aux={
        "nominal_merging_factor": 7,
        "era": "C",
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
    n_files=224,
    n_events=101_270_969,
    aux={
        "nominal_merging_factor": 7,
        "era": "D",
    },
)
