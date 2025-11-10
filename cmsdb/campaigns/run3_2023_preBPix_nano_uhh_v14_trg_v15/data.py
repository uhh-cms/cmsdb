# coding: utf-8

"""
Recorded datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15 import campaign_run3_2023_preBPix_nano_uhh_v14_trg_v15 as cpn  # noqa: E501


#
# Muon
#

cpn.add_dataset(
    name="data_mu_c1",
    id=14787007,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=53 + 52,
    n_events=54_715_896 + 54_621_922,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 16,
        },
        "era": "MU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c2",
    id=14786981,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=17 + 17,
    n_events=17_063_451 + 17_059_895,
    aux={
        "merging_factors": {
            "nominal": 16,
            "nominal_ext1": 16,
        },
        "era": "MU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c3",
    id=14787042,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=20 + 20,
    n_events=20_015_377 + 20_010_429,
    aux={
        "merging_factors": {
            "nominal": 17,
            "nominal_ext1": 17,
        },
        "era": "MU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c4",
    id=14786114,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=130 + 127,  # 0 + 1 skipped
    n_events=138_943_783 + 138_834_244,  # 0 + 78_018 skipped
    aux={
        "merging_factors": {
            "nominal": 17,
            "nominal_ext1": 17,
        },
        "era": "MU",
        "jec_era": "RunCv4",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_c1",
    id=14786979,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=76 + 75,
    n_events=67_598_081 + 67_530_273,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "E",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_e_c2",
    id=14787632,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=20 + 20,
    n_events=17_233_307 + 17_230_822,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "E",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_e_c3",
    id=14787547,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=25 + 26,
    n_events=21_993_048 + 21_987_586,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 13,
        },
        "era": "E",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_e_c4",
    id=14786976,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=175 + 174,
    n_events=160_108_119 + 159_997_174,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "E",
        "jec_era": "RunCv4",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c1",
    id=14826260,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v1_NanoAODv14UHH-v2/NANOAOD",
    ],
    n_files=21,
    n_events=14_484_171,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
        "era": "TAU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_tau_c2",
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
        "era": "TAU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_tau_c3",
    id=14787784,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=9,
    n_events=6_470_602,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "TAU",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_tau_c4",
    id=14786973,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=61,
    n_events=45_176_805,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "TAU",
        "jec_era": "RunCv4",
    },
)

#
# VBF parking
#

cpn.add_dataset(
    name="data_parking_vbf_c3",
    id=14826159,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF1/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF2/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF3/Run2023C-22Sep2023_v3_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=42 + 43 + 41 + 41,
    n_events=35_190_486 + 35_190_430 + 35_131_412 + 35_139_018,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
            "nominal_ext2": 14,
            "nominal_ext3": 14,
        },
        "era": "VBF",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_parking_vbf_c4",
    id=14825784,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF1/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF2/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF3/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF4/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF5/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF6/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF7/Run2023C-22Sep2023_v4_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=127 + 127 + 126 + 126 + 103 + 104 + 104 + 104,  # 1 + 0 + 0 + 0 + 1 + 0 + 0 + 1 skipped
    n_events=104_064_197 + 104_013_699 + 103_990_476 + 104_062_923 + 85_296_160 + 85_355_409 + 85_382_472 + 85_336_039,  # 84_682 + 0 + 0 + 0 + 55_130 + 0 + 0 + 70_738 skipped # noqa
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
            "nominal_ext2": 14,
            "nominal_ext3": 14,
            "nominal_ext4": 14,
            "nominal_ext5": 14,
            "nominal_ext6": 14,
            "nominal_ext7": 14,
        },
        "era": "VBF",
        "jec_era": "RunCv4",
    },
)
