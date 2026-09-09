# coding: utf-8

"""
Recorded datasets for the 2026 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2026_nano_v15 import campaign_run3_2026_nano_v15 as cpn


#
# JetMET datasets
#

cpn.add_dataset(
    name="data_met_a",
    id=15552525,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2026A-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2026A-PromptReco-v1/NANOAOD",
    ],
    n_files=72 + 76,
    n_events=16602265 + 16588421,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=15591506,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2026D-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=405 + 399,
    n_events=151375589 + 151355297,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=15569003,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2026C-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2026C-PromptReco-v1/NANOAOD",
        "/JetMET2/Run2026C-PromptReco-v1/NANOAOD",
        "/JetMET3/Run2026C-PromptReco-v1/NANOAOD",
        "/JetMET4/Run2026C-PromptReco-v1/NANOAOD",
        "/JetMET5/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=1393 + 1383 + 1371 + 1362 + 1360 + 1354,
    n_events=1756939928 + 1756363080 + 1755211834 + 1755216678 + 1755215414 + 1755211453,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_b",
    id=15558208,
    processes=[procs.data_met],
    keys=[
        "/JetMET0/Run2026B-PromptReco-v1/NANOAOD",
        "/JetMET1/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=612 + 621,
    n_events=245424748 + 245406692,
    is_data=True,
    aux={
        "era": "B",
    },
)

#
# muon datasets
#

# muon egamma
cpn.add_dataset(
    name="data_muoneg_a",
    id=15552736,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2026A-PromptReco-v1/NANOAOD",
    ],
    n_files=38,
    n_events=2699844,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=15557575,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=193,
    n_events=50921430,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=15568792,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=65,
    n_events=5291221,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=15591468,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=120,
    n_events=32379047,
    is_data=True,
    aux={
        "era": "D",
    },
)

# muon
cpn.add_dataset(
    name="data_mu_a",
    id=15552450,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2026A-PromptReco-v1/NANOAOD",
        "/Muon1/Run2026A-PromptReco-v1/NANOAOD",
        "/Muon2/Run2026A-PromptReco-v1/NANOAOD",
        "/Muon3/Run2026A-PromptReco-v1/NANOAOD",
    ],
    n_files=52 + 56 + 54 + 51,
    n_events=7347312 + 7347779 + 7344116 + 7345253,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_mu_b",
    id=15558192,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2026B-PromptReco-v1/NANOAOD",
        "/Muon1/Run2026B-PromptReco-v1/NANOAOD",
        "/Muon2/Run2026B-PromptReco-v1/NANOAOD",
        "/Muon3/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=448 + 443 + 448 + 443,
    n_events=155034715 + 155028140 + 155029788 + 155025135,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=15569405,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2026C-PromptReco-v1/NANOAOD",
        "/Muon1/Run2026C-PromptReco-v1/NANOAOD",
        "/Muon2/Run2026C-PromptReco-v1/NANOAOD",
        "/Muon3/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=813 + 778 + 784 + 777,
    n_events=779902163 + 779231920 + 779164947 + 779192881,
    is_data=True,
    aux={
        "era": "C",
    },
)
cpn.add_dataset(
    name="data_mu_d",
    id=15592049,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2026D-PromptReco-v1/NANOAOD",
        "/Muon1/Run2026D-PromptReco-v1/NANOAOD",
        "/Muon2/Run2026D-PromptReco-v1/NANOAOD",
        "/Muon3/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=321 + 317 + 313 + 321,
    n_events=112288744 + 112284014 + 112290907 + 112282726,
    is_data=True,
    aux={
        "era": "D",
    },
)

# muon shower
cpn.add_dataset(
    name="data_muonshower_a",
    id=15552147,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2026A-PromptReco-v1/NANOAOD",
    ],
    n_files=58,
    n_events=22284,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_muonshower_b",
    id=15557263,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=259,
    n_events=230562,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_muonshower_c",
    id=15568686,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=319,
    n_events=667697,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_muonshower_d",
    id=15590836,
    processes=[procs.data_muonshower],
    keys=[
        "/MuonShower/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=199,
    n_events=414608,
    is_data=True,
    aux={
        "era": "D",
    },
)

#
# E Gamma datasets
#
cpn.add_dataset(
    name="data_e_a",
    id=15552635,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2026A-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2026A-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2026A-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2026A-PromptReco-v1/NANOAOD",
        "/EGamma4/Run2026A-PromptReco-v1/NANOAOD",
        "/EGamma5/Run2026A-PromptReco-v1/NANOAOD",
    ],
    n_files=62 + 61 + 66 + 65 + 60 + 60,
    n_events=11733359 + 11731043 + 11732795 + 11731165 + 11733095 + 11731599,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_e_b",
    id=15557176,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2026B-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2026B-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2026B-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2026B-PromptReco-v1/NANOAOD",
        "/EGamma4/Run2026B-PromptReco-v1/NANOAOD",
        "/EGamma5/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=536 + 532 + 534 + 529 + 533 + 535,
    n_events=205275441 + 205266455 + 205274221 + 205271520 + 205273231 + 205265468,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=15568826,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2026C-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2026C-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2026C-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2026C-PromptReco-v1/NANOAOD",
        "/EGamma4/Run2026C-PromptReco-v1/NANOAOD",
        "/EGamma5/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=603 + 611 + 594 + 590 + 592 + 589,
    n_events=375030929 + 374809724 + 374832870 + 374811337 + 374793369 + 374804007,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=15591574,
    processes=[procs.data_e],
    keys=[
        "/EGamma0/Run2026D-PromptReco-v1/NANOAOD",
        "/EGamma1/Run2026D-PromptReco-v1/NANOAOD",
        "/EGamma2/Run2026D-PromptReco-v1/NANOAOD",
        "/EGamma3/Run2026D-PromptReco-v1/NANOAOD",
        "/EGamma4/Run2026D-PromptReco-v1/NANOAOD",
        "/EGamma5/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=334 + 325 + 335 + 327 + 332 + 327,
    n_events=125742096 + 125740549 + 125741242 + 125739959 + 125741715 + 125738632,
    is_data=True,
    aux={
        "era": "D",
    },
)

# Tau

cpn.add_dataset(
    name="data_tau_b",
    id=15557609,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=453,
    n_events=144_513_582,
    aux={
        "prompt": True,
        "era": "B",
    },
)
cpn.add_dataset(
    name="data_tau_c",
    id=15568796,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=92,
    n_events=15_120_082,
    aux={
        "prompt": True,
        "era": "C",
    },
)
cpn.add_dataset(
    name="data_tau_d",
    id=15591451,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=324,
    n_events=114_250_021,
    aux={
        "prompt": True,
        "era": "D",
    },
)


# Parking dataset (HH/VBF)

# HH parking

cpn.add_dataset(
    name="data_parking_hh_b",
    id=15557438,
    is_data=True,
    processes=[procs.data_hh],
    keys=[
        "/ParkingHH0/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingHH1/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=473 + 463,
    n_events=129_014_771 + 129_007_618,
    aux={
        "prompt": True,
        "era": "B",
    },
)
cpn.add_dataset(
    name="data_parking_hh_c",
    id=15569248,
    is_data=True,
    processes=[procs.data_hh],
    keys=[
        "/ParkingHH0/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingHH1/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=85 + 80,
    n_events=11_246_253 + 11_289_404,
    aux={
        "prompt": True,
        "era": "C",
    },
)
cpn.add_dataset(
    name="data_parking_hh_d",
    id=15591927,
    is_data=True,
    processes=[procs.data_hh],
    keys=[
        "/ParkingHH0/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingHH1/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=307 + 313,
    n_events=86_830_065 + 86_825_827,
    aux={
        "prompt": True,
        "era": "D",
    },
)


# VBF parking

cpn.add_dataset(
    name="data_parking_vbf_b",
    id=15557569,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF1/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF2/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF3/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF4/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF5/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF6/Run2026B-PromptReco-v1/NANOAOD",
        "/ParkingVBF7/Run2026B-PromptReco-v1/NANOAOD",
    ],
    n_files=362 + 356 + 365 + 362 + 359 + 355 + 361 + 363,
    n_events=97_446_800 + 97_445_187 + 97_446_832 + 97_448_260 + 97_448_666 + 97_449_045 + 97_442_546 + 97_440_256,
    aux={
        "prompt": True,
        "era": "B",
    },
)
cpn.add_dataset(
    name="data_parking_vbf_c",
    id=15569253,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF1/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF2/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF3/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF4/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF5/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF6/Run2026C-PromptReco-v1/NANOAOD",
        "/ParkingVBF7/Run2026C-PromptReco-v1/NANOAOD",
    ],
    n_files=71 + 65 + 67 + 65 + 68 + 66 + 65 + 64,
    n_events=10_005_016 + 10_004_293 + 10_012_802 + 10_006_339 + 10_013_372 + 10_000_594 + 10_013_728 + 10_008_466,
    aux={
        "prompt": True,
        "era": "C",
    },
)
cpn.add_dataset(
    name="data_parking_vbf_d",
    id=15591915,
    is_data=True,
    processes=[procs.data_vbf],
    keys=[
        "/ParkingVBF0/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF1/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF2/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF3/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF4/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF5/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF6/Run2026D-PromptReco-v1/NANOAOD",
        "/ParkingVBF7/Run2026D-PromptReco-v1/NANOAOD",
    ],
    n_files=204 + 205 + 205 + 206 + 201 + 205 + 203 + 209,
    n_events=61_868_372 + 61_867_304 + 61_868_622 + 61_868_878 + 61_869_027 + 61_868_922 + 61_869_141 + 61_868_337,
    aux={
        "prompt": True,
        "era": "D",
    },
)
