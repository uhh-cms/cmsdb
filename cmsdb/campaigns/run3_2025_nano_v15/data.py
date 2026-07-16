# coding: utf-8

"""
Recorded datasets for the 2025 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2025_nano_v15 import campaign_run3_2025_nano_v15 as cpn


#
# JetMET datasets
#

cpn.add_dataset(
    name="data_met_b",
    id=15310763,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025B-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025B-PromptReco-v1/NANOAOD",
    ],
    n_files=91 + 92,
    n_events=13561943 + 13551058,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=15337395,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025C-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025C-PromptReco-v1/NANOAOD",
        "/JetMET0/Run2025C-PromptReco-v2/NANOAOD",
        "/JetMET1/Run2025C-PromptReco-v2/NANOAOD",
    ],
    n_files=524 + 530 + 290 + 282,
    n_events=155327920 + 155309595 + 81725663 + 81736350,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=15369835,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025D-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025D-PromptReco-v1/NANOAOD",
    ],
    n_files=944 + 930,
    n_events=257411297 + 257342455,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_e",
    id=15396830,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025E-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025E-PromptReco-v1/NANOAOD",
    ],
    n_files=484 + 492,
    n_events=145280947 + 145256476,
    is_data=True,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=15419644,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025F-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025F-PromptReco-v1/NANOAOD",
        "/JetMET0/Run2025F-PromptReco-v2/NANOAOD",
        "/JetMET1/Run2025F-PromptReco-v2/NANOAOD",
    ],
    n_files=723 + 715 + 290 + 287,
    n_events=200915960 + 200859929 + 76494690 + 76479375,
    is_data=True,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_met_g",
    id=15426626,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2025G-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2025G-PromptReco-v1/NANOAOD",
    ],
    n_files=824 + 836,
    n_events=259840950 + 259876805,
    is_data=True,
    aux={
        "era": "G",
    },
)

#
# Muon datasets
#

# muonEG
cpn.add_dataset(
    name="data_muoneg_b",
    id=15312837,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025B-PromptReco-v1/NANOAOD",
    ],
    n_files=47,
    n_events=910971,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=15337052,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025C-PromptReco-v1/NANOAOD",
        "/MuonEG/Run2025C-PromptReco-v2/NANOAOD",
    ],
    n_files=172 + 92,
    n_events=41994774 + 23203653,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=15374208,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025D-PromptReco-v1/NANOAOD",
    ],
    n_files=329,
    n_events=72820407,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muoneg_e",
    id=15396290,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025E-PromptReco-v1/NANOAOD",
    ],
    n_files=165,
    n_events=40691496,
    is_data=True,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=15419217,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025F-PromptReco-v1/NANOAOD",
        "/MuonEG/Run2025F-PromptReco-v2/NANOAOD",
    ],
    n_files=270 + 105,
    n_events=58301670 + 22447339,
    is_data=True,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=15427226,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2025G-PromptReco-v1/NANOAOD",
    ],
    n_files=282,
    n_events=67268221,
    is_data=True,
    aux={
        "era": "G",
    },
)

# muon
cpn.add_dataset(
    name="data_mu_b",
    id=15312746,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025B-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025B-PromptReco-v1/NANOAOD",
    ],
    n_files=77 + 77,
    n_events=5602078 + 5598676,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=15337600,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025C-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025C-PromptReco-v1/NANOAOD",
        "/Muon0/Run2025C-PromptReco-v2/NANOAOD",
        "/Muon1/Run2025C-PromptReco-v2/NANOAOD",
    ],
    n_files=638 + 644 + 356 + 350,
    n_events=250835953 + 250819768 + 148575745 + 148565659,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=15369850,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025D-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025D-PromptReco-v1/NANOAOD",
    ],
    n_files=1160 + 1159,
    n_events=479676562 + 479642866,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=15396848,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025E-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025E-PromptReco-v1/NANOAOD",
    ],
    n_files=606 + 611,
    n_events=265645863 + 265630211,
    is_data=True,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=15419721,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025F-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025F-PromptReco-v1/NANOAOD",
        "/Muon0/Run2025F-PromptReco-v2/NANOAOD",
        "/Muon1/Run2025F-PromptReco-v2/NANOAOD",
    ],
    n_files=884 + 891 + 344 + 345,
    n_events=377119912 + 377092035 + 143519758 + 143511119,
    is_data=True,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=15427408,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2025G-PromptReco-v1/NANOAOD",
        "/Muon1/Run2025G-PromptReco-v1/NANOAOD",
    ],
    n_files=1009 + 1003,
    n_events=442329683 + 442232031,
    is_data=True,
    aux={
        "era": "G",
    },
)

# muon shower
cpn.add_dataset(
    name="data_muonshower_a",
    id=15300570,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025A-PromptReco-v1/NANOAOD",
        "/MuonShower/Run2025A-PromptReco-v2/NANOAOD",
    ],
    n_files=54 + 127,
    n_events=195375 + 70611,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muonshower_b",
    id=15310631,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025B-PromptReco-v1/NANOAOD",
    ],
    n_files=201,
    n_events=154746,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muonshower_c",
    id=15336187,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025C-PromptReco-v1/NANOAOD",
        "/MuonShower/Run2025C-PromptReco-v2/NANOAOD",
    ],
    n_files=314 + 143,
    n_events=717306 + 377874,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muonshower_d",
    id=15369146,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025D-PromptReco-v1/NANOAOD",
    ],
    n_files=521,
    n_events=1100421,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_muonshower_e",
    id=15395625,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025E-PromptReco-v1/NANOAOD",
    ],
    n_files=191,
    n_events=186730,
    is_data=True,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_muonshower_f",
    id=15416847,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025F-PromptReco-v1/NANOAOD",
        "/MuonShower/Run2025F-PromptReco-v2/NANOAOD",
    ],
    n_files=71 + 360,
    n_events=74780 + 512079,
    is_data=True,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_muonshower_g",
    id=15422929,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2025G-PromptReco-v1/NANOAOD",
    ],
    n_files=288,
    n_events=647388,
    is_data=True,
    aux={
        "era": "G",
    },
)

#
# EGamma datasets
#
cpn.add_dataset(
    name="data_e_b",
    id=15312679,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025B-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025B-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025B-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025B-PromptReco-v1/NANOAOD",
    ],
    n_files=75 + 75 + 75 + 75,
    n_events=5256904 + 5253103 + 5254123 + 5253489,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=15336258,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025C-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025C-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025C-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025C-PromptReco-v1/NANOAOD",
        "/EGamma0/Run2025C-PromptReco-v2/NANOAOD",
        "/EGamma1/Run2025C-PromptReco-v2/NANOAOD",
        "/EGamma2/Run2025C-PromptReco-v2/NANOAOD",
        "/EGamma3/Run2025C-PromptReco-v2/NANOAOD",
    ],
    n_files=655 + 652 + 656 + 660 + 342 + 347 + 351 + 343,
    n_events=243682359 + 243674671 + 133952379 + 243679348 + 133951067 + 133950574 + 133949781,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=15369930,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025D-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025D-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025D-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025D-PromptReco-v1/NANOAOD",
    ],
    n_files=1105 + 1095 + 1121 + 1090,
    n_events=414017171 + 413556254 + 414008481 + 414010046,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=15396831,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025E-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025E-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025E-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025E-PromptReco-v1/NANOAOD",
    ],
    n_files=595 + 596 + 593 + 598,
    n_events=240927385 + 240921314 + 240923259 + 240923335,
    is_data=True,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=15419718,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025F-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025F-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025F-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025F-PromptReco-v1/NANOAOD",
        "/EGamma0/Run2025F-PromptReco-v2/NANOAOD",
        "/EGamma1/Run2025F-PromptReco-v2/NANOAOD",
        "/EGamma2/Run2025F-PromptReco-v2/NANOAOD",
        "/EGamma3/Run2025F-PromptReco-v2/NANOAOD",
    ],
    n_files=875 + 888 + 876 + 889 + 351 + 350 + 358 + 340,
    n_events=346000262 + 346019505 + 139317024 + 346009210 + 346008679 + 139310909 + 139313488 + 139314438 + 139314438,
    is_data=True,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_e_g",
    id=15426128,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2025G-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2025G-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2025G-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2025G-PromptReco-v1/NANOAOD",
    ],
    n_files=1012 + 1010 + 1016 + 1012,
    n_events=421398444 + 421102377 + 421453068 + 421124471,
    is_data=True,
    aux={
        "era": "G",
    },
)
