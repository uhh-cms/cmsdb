
# coding: utf-8

""""
Data datasets for the run3_2024_nano_v15 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


cpn.add_dataset(
    name="data_jetmet_c",
    id=15289012,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/JetMET1/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=161 + 110,
    n_events=69_348_871 + 69_648_563,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=15290632,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/JetMET1/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=151 + 155,
    n_events=75_958_774 + 75_810_110,
    is_data=True,
    aux={
        "era": "D",
    }
)

cpn.add_dataset(
    name="data_jetmet_e",
    id=15291243,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/JetMET1/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=231 + 228,
    n_events=123_673_375 + 123_602_626,
    is_data=True,
    aux={
        "era": "E",
    }
)

cpn.add_dataset(
    name="data_jetmet_f",
    id=15299554,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024F-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/JetMET1/Run2024F-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=381 + 381,
    n_events=309_079_689 + 309_604_079,
    is_data=True,
    aux={
        "era": "F",
    }
)

cpn.add_dataset(
    name="data_jetmet_g",
    id=15299588,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024G-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/JetMET1/Run2024G-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=443 + 451,
    n_events=401_015_801 + 397_200_034,
    is_data=True,
    aux={
        "era": "G",
    }
)

cpn.add_dataset(
    name="data_jetmet_h",
    id=15299537,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024H-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/JetMET1/Run2024H-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=82 + 76,
    n_events=55_794_457 + 55_790_857,
    is_data=True,
    aux={
        "era": "H",
    }
)

cpn.add_dataset(
    name="data_jetmet_i",
    id=15293121,
    processes=[procs.data_jetmet],
    keys=[
        "/JetMET0/Run2024I-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/JetMET0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",  # noqa; FIXME why v2-v1 in this era?
        "/JetMET1/Run2024I-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/JetMET1/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD",  # noqa; FIXME why v2-v2 in this era?
    ],
    n_files=149 + 179 + 82 + 116,
    n_events=59_259_348 + 116_134_795 + 59_255_632 + 116_127_561,
    is_data=True,
    aux={
        "era": "I",
    }
)

cpn.add_dataset(
    name="data_muon_c",
    id=15288695,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=103 + 94,
    n_events=97_505_587 + 97_531_998,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_muon_d",
    id=15291308,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=180 + 168,
    n_events=120_787_065 + 120_467_371,
    is_data=True,
    aux={
        "era": "D",
    }
)

cpn.add_dataset(
    name="data_muon_e",
    id=15297256,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=255 + 171,
    n_events=169_640_946 + 172_848_674,
    is_data=True,
    aux={
        "era": "E",
    }
)

cpn.add_dataset(
    name="data_muon_f",
    id=15291901,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024F-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024F-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=594 + 538,
    n_events=442_432_787 + 442_360_423,
    is_data=True,
    aux={
        "era": "F",
    }
)

cpn.add_dataset(
    name="data_muon_g",
    id=15291960,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024G-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024G-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=948 + 565,
    n_events=642_028_803 + 641_959_643,
    is_data=True,
    aux={
        "era": "G",
    }
)

cpn.add_dataset(
    name="data_muon_h",
    id=15291794,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024H-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024H-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=152 + 93,
    n_events=93_983_627 + 93_981_102,
    is_data=True,
    aux={
        "era": "H",
    }
)

cpn.add_dataset(
    name="data_muon_i",
    id=15291900,
    processes=[procs.data_muon],
    keys=[
        "/Muon0/Run2024I-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",  # noqa; FIXME why v2-v1 in this era?
        "/Muon1/Run2024I-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/Muon1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",  # noqa FIXME why v2-v1 in this era?
    ],
    n_files=173 + 174 + 94 + 133,
    n_events=97_634_104 + 105_194_627 + 97_630_010 + 105_189_040,
    is_data=True,
    aux={
        "era": "I",
    }
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=15288975,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=35,
    n_events=18_312_408,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=15291188,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=47,
    n_events=18_827_708,
    is_data=True,
    aux={
        "era": "D",
    }
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=15290662,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=63,
    n_events=26_319_233,
    is_data=True,
    aux={
        "era": "E",
    }
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=15299473,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024F-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=106,
    n_events=67_341_687,
    is_data=True,
    aux={
        "era": "F",
    }
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=15297392,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024G-MINIv6NANOv15-v3/NANOAOD",  # noqa
    ],
    n_files=150,
    n_events=97_985_222,
    is_data=True,
    aux={
        "era": "G",
    }
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=15299540,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024H-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=14_323_522,
    is_data=True,
    aux={
        "era": "H",
    }
)

cpn.add_dataset(
    name="data_muoneg_i",
    id=15299590,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2024I-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/MuonEG/Run2024I-MINIv6NANOv15_v2-v2/NANOAOD",  # noqa; FIXME why v2-v2 in this era?
    ],
    n_files=23 + 22,
    n_events=14_579_063 + 14_674_636,
    is_data=True,
    aux={
        "era": "I",
    }
)

cpn.add_dataset(
    name="data_egamma_c",
    id=15289158,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma1/Run2024C-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=167 + 247,
    n_events=157_351_226 + 157_860_731,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_egamma_d",
    id=15291573,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma1/Run2024D-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=173 + 279,
    n_events=156_558_757 + 156_275_778,
    is_data=True,
    aux={
        "era": "D",
    }
)

cpn.add_dataset(
    name="data_egamma_e",
    id=15291143,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma1/Run2024E-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=267 + 335,
    n_events=249_417_634 + 249_489_829,
    is_data=True,
    aux={
        "era": "E",
    }
)

cpn.add_dataset(
    name="data_egamma_f",
    id=15290277,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024F-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma1/Run2024F-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=719 + 747,
    n_events=638_196_622 + 631_079_889,
    is_data=True,
    aux={
        "era": "F",
    }
)

cpn.add_dataset(
    name="data_egamma_g",
    id=15299541,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024G-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/EGamma1/Run2024G-MINIv6NANOv15-v2/NANOAOD",  # noqa
    ],
    n_files=850 + 888,
    n_events=903_520_258 + 903_441_926,
    is_data=True,
    aux={
        "era": "G",
    }
)

cpn.add_dataset(
    name="data_egamma_h",
    id=15299592,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024H-MINIv6NANOv15-v2/NANOAOD",  # noqa
        "/EGamma1/Run2024H-MINIv6NANOv15-v1/NANOAOD",  # noqa
    ],
    n_files=138 + 191,
    n_events=134_680_448 + 134_835_799,
    is_data=True,
    aux={
        "era": "H",
    }
)

cpn.add_dataset(
    name="data_egamma_i",
    id=15291530,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2024I-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma0/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",  # noqa FIXME why v2-v1 in this era?
        "/EGamma1/Run2024I-MINIv6NANOv15-v1/NANOAOD",  # noqa
        "/EGamma1/Run2024I-MINIv6NANOv15_v2-v1/NANOAOD",  # noqa FIXME why v2-v1 in this era?
    ],
    n_files=211 + 198 + 176 + 179,
    n_events=132_904_290 + 150_687_674 + 132_903_874 + 150_687_112,
    is_data=True,
    aux={
        "era": "I",
    }
)
