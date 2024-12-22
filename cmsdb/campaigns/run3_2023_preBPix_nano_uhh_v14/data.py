# coding: utf-8

"""
Recorded datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn  # noqa


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c_1",
    id=14787007,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=47 + 46,
    n_events=54_715_896 + 54_621_922,
    aux={
        "merging_factors": {
            "nominal": 18,
            "nominal_ext1": 18,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_2",
    id=14786981,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=15 + 15,
    n_events=17_063_451 + 17_059_895,
    aux={
        "merging_factors": {
            "nominal": 18,
            "nominal_ext1": 18,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_3",
    id=14787042,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=18 + 18,
    n_events=20_015_377 + 20_010_429,
    aux={
        "merging_factors": {
            "nominal": 19,
            "nominal_ext1": 19,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_c_4",
    id=14786114,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v2/NANOAOD",  # misses 258 due to lzma errors
    ],
    n_files=123 + 120,
    n_events=138_943_783 + 138_912_262,
    aux={
        "merging_factors": {
            "nominal": 18,
            "nominal_ext1": 18,
        },
        "era": "C",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_c_1",
    id=14786979,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=71 + 70,
    n_events=67_598_081 + 67_530_273,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_c_2",
    id=14787632,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=19 + 19,
    n_events=17_233_307 + 17_230_822,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_c_3",
    id=14787547,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=23 + 23,
    n_events=21_993_048 + 21_987_586,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_c_4",
    id=14786976,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=164 + 164,
    n_events=160_108_119 + 159_997_174,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 16,
        },
        "era": "C",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c_1",
    id=14826260,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v1_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=19,
    n_events=14_484_171,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_c_2",
    id=14787194,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=7,
    n_events=5_178_955,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_c_3",
    id=14787784,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=8,
    n_events=6_470_602,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_c_4",
    id=14786973,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=56,
    n_events=45_176_805,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "C",
    },
)

#
# Jet/MET
#

cpn.add_dataset(
    name="data_met_c_1",
    id=14784874,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=75 + 76,
    n_events=56_089_464 + 56_071_751,
    aux={
        "merging_factors": {
            "nominal": 13,
            "nominal_ext1": 13,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_c_2",
    id=14784866,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=23 + 24,
    n_events=17_154_040 + 17_149_627,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 13,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_c_3",
    id=14784908,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=20 + 20,
    n_events=14_859_886 + 14_852_598,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_c_4",
    id=14785389,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/JetMET1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=134 + 135,
    n_events=105_910_300 + 105_874_180,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "C",
    },
)
