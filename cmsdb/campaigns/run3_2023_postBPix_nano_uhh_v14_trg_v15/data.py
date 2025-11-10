# coding: utf-8

"""
Recorded datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14_trg_v15 import campaign_run3_2023_postBPix_nano_uhh_v14_trg_v15 as cpn  # noqa: E501


#
# Muon
#

cpn.add_dataset(
    name="data_mu_d1",
    id=14787753,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=92 + 94,
    n_events=100_211_533 + 100_281_976,
    aux={
        "merging_factors": {
            "nominal": 17,
            "nominal_ext1": 16,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_d2",
    id=14787624,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/Muon1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=21 + 20,
    n_events=21_462_916 + 21_463_645,
    aux={
        "merging_factors": {
            "nominal": 18,
            "nominal_ext1": 18,
        },
        "era": "D",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_d1",
    id=14787218,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=23,
    n_events=17_530_531,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muoneg_d2",
    id=14787199,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=6,
    n_events=3_751_587,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
        "era": "D",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_d1",
    id=14786983,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=122 + 121,
    n_events=105_892_646 + 105_850_543,
    aux={
        "merging_factors": {
            "nominal": 14,
            "nominal_ext1": 14,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_d2",
    id=14787826,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/EGamma1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=27 + 27,
    n_events=22_657_211 + 22_653_287,
    aux={
        "merging_factors": {
            "nominal": 15,
            "nominal_ext1": 15,
        },
        "era": "D",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_d1",
    id=14787583,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=42,
    n_events=32_092_659,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_d2",
    id=14786909,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=10,
    n_events=7_246_202,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
        "era": "D",
    },
)

#
# VBF parking
#

cpn.add_dataset(
    name="data_parking_vbf_d1",
    id=14826079,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF1/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF2/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF3/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF4/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF5/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF6/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF7/Run2023D-22Sep2023_v1_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=78 + 79 + 77 + 77 + 77 + 78 + 77 + 78,  # 0 + 1 + 0 + 0 + 0 + 0 + 0 + 0 skipped
    n_events=65_139_138 + 65_244_498 + 65_300_193 + 65_137_849 + 65_139_877 + 65_275_863 + 65_248_479 + 65_244_286,  # 0 + 56_714 + 0 + 0 + 0 + 0 + 0 + 0 skipped # noqa
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
    },
)

cpn.add_dataset(
    name="data_parking_vbf_d2",
    id=14826114,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF1/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF2/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF3/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF4/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF5/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF6/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
        "/ParkingVBF7/Run2023D-22Sep2023_v2_NanoAODv14UHH-v1/NANOAOD",
    ],
    n_files=18 + 18 + 18 + 18 + 18 + 18 + 18 + 18,
    n_events=13_845_112 + 13_874_062 + 13_872_438 + 13_871_931 + 13_872_999 + 13_873_320 + 13_872_756 + 13_873_107,
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
    },
)
