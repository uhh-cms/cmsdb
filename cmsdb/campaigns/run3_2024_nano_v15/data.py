# coding: utf-8

"""
Recorded datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# Muon
#

cpn.add_dataset(
    name="data_mu_c",
    id=15288695,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=103 + 94,
    n_events=97_505_587 + 97_531_998,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=15291308,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=180 + 168,
    n_events=120_787_065 + 120_467_371,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=15297256,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=255 + 171,
    n_events=169_640_946 + 172_848_674,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=15291901,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=594 + 538,
    n_events=442_432_787 + 442_360_423,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=15291960,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=948 + 565,
    n_events=642_028_803 + 641_959_643,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_mu_h",
    id=15291794,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=152 + 93,
    n_events=93_983_627 + 93_981_102,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_mu_i",
    id=15291900,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
        "/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=173 + 94 + 174 + 133,
    n_events=97_634_104 + 97_630_010 + 105_194_627 + 105_189_040,
    aux={
        "prompt": True,
        "era": "I",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c",
    id=15288975,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=35,
    n_events=18_312_408,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=15291188,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=47,
    n_events=18_827_708,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=15290662,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=63,
    n_events=26_319_233,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=15299473,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024F-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=106,
    n_events=67_341_687,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=15297392,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024G-MINIv6NANOv15-v3/NANOAOD",
    ],
    n_files=150,
    n_events=97_985_222,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=15299540,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=25,
    n_events=14_323_522,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_muoneg_i",
    id=15299590,
    is_data=True,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024I-MINIv6NANOv15-v2/NANOAOD",
        "/MuonEG/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD",
    ],
    n_files=23 + 22,
    n_events=14_579_063 + 14_674_636,
    aux={
        "prompt": True,
        "era": "I",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_e_c",
    id=15289158,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=167 + 247,
    n_events=157_351_226 + 157_860_731,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=15291573,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=173 + 279,
    n_events=156_558_757 + 156_275_778,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=15291143,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=267 + 335,
    n_events=249_417_634 + 249_489_829,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=15290277,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=719 + 747,
    n_events=638_196_622 + 631_079_889,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_e_g",
    id=15299541,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD",
        "/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=850 + 888,
    n_events=903_520_258 + 903_441_926,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_e_h",
    id=15299592,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD",
        "/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=138 + 191,
    n_events=134_680_448 + 134_835_799,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_e_i",
    id=15291530,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
        "/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=211 + 176 + 198 + 179,
    n_events=132_904_290 + 132_903_874 + 150_687_674 + 150_687_112,
    aux={
        "prompt": True,
        "era": "I",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c",
    id=15289011,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=69,
    n_events=50_839_148,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=15290642,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=102,
    n_events=58_755_163,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=15290619,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=142,
    n_events=85_422_487,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=15291997,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024F-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=466,
    n_events=233_974_175,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_tau_g",
    id=15291813,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024G-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=624,
    n_events=326_893_418,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_tau_h",
    id=15292908,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024H-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=125,
    n_events=49_147_037,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_tau_i",
    id=15292932,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/Tau/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
    ],
    n_files=126 + 86,
    n_events=47_197_378 + 47_460_687,
    aux={
        "prompt": True,
        "era": "I",
    },
)

#
# Jet/MET
#

cpn.add_dataset(
    name="data_met_c",
    id=15289012,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024C-MINIv6NANOv15-v1/NANOAOD",
        "/JetMET1/Run2024C-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=161 + 110,
    n_events=69_348_871 + 69_648_563,
    aux={
        "prompt": False,
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=15290632,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024D-MINIv6NANOv15-v1/NANOAOD",
        "/JetMET1/Run2024D-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=151 + 155,
    n_events=75_958_774 + 75_810_110,
    aux={
        "prompt": False,
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_e",
    id=15291243,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024E-MINIv6NANOv15-v1/NANOAOD",
        "/JetMET1/Run2024E-MINIv6NANOv15-v1/NANOAOD",
    ],
    n_files=231 + 228,
    n_events=123_673_375 + 123_602_626,
    aux={
        "prompt": False,
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=15299554,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024F-MINIv6NANOv15-v2/NANOAOD",
        "/JetMET1/Run2024F-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=381 + 381,
    n_events=309_079_689 + 309_604_079,
    aux={
        "prompt": True,
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_met_g",
    id=15299588,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024G-MINIv6NANOv15-v2/NANOAOD",
        "/JetMET1/Run2024G-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=443 + 451,
    n_events=401_015_801 + 397_200_034,
    aux={
        "prompt": True,
        "era": "G",
    },
)

cpn.add_dataset(
    name="data_met_h",
    id=15299537,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024H-MINIv6NANOv15-v2/NANOAOD",
        "/JetMET1/Run2024H-MINIv6NANOv15-v2/NANOAOD",
    ],
    n_files=82 + 76,
    n_events=55_794_457 + 55_790_857,
    aux={
        "prompt": True,
        "era": "H",
    },
)

cpn.add_dataset(
    name="data_met_i",
    id=15293121,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2024I-MINIv6NANOv15-v2/NANOAOD",
        "/JetMET1/Run2024I-MINIv6NANOv15-v1/NANOAOD",
        "/JetMET0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",
        "/JetMET1/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD",
    ],
    n_files=149 + 82 + 179 + 116,
    n_events=59_259_348 + 59_255_632 + 116_134_795 + 116_127_561,
    aux={
        "prompt": True,
        "era": "I",
    },
)

