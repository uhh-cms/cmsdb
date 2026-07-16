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
    name="data_jethtmet_a",
    id=15552525,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET1/Run2026A-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=72 + 76,
    n_events=16602265 + 16588421,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_jethtmet_d",
    id=15591506,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET1/Run2026D-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=405 + 399,
    n_events=151375589 + 151355297,
    is_data=True,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_jethtmet_c",
    id=15569003,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET1/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET2/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET3/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET4/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET5/Run2026C-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=1393 + 1383 + 1371 + 1362 + 1360 + 1354,
    n_events=1756939928 + 1756363080 + 1755211834 + 1755216678 + 1755215414 + 1755211453,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jethtmet_b",
    id=15558208,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/JetMET1/Run2026B-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonEG/Run2026A-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonEG/Run2026B-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonEG/Run2026C-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonEG/Run2026D-PromptReco-v1/NANOAOD",  # noqa
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
        "/Muon0/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/Muon1/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/Muon2/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/Muon3/Run2026A-PromptReco-v1/NANOAOD",  # noqa
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
        "/Muon0/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/Muon1/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/Muon2/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/Muon3/Run2026B-PromptReco-v1/NANOAOD",  # noqa
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
        "/Muon0/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/Muon1/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/Muon2/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/Muon3/Run2026C-PromptReco-v1/NANOAOD",  # noqa
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
        "/Muon0/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/Muon1/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/Muon2/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/Muon3/Run2026D-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonShower/Run2026A-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonShower/Run2026B-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonShower/Run2026C-PromptReco-v1/NANOAOD",  # noqa
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
        "/MuonShower/Run2026D-PromptReco-v1/NANOAOD",  # noqa
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
    name="data_egamma_a",
    id=15552635,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma1/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma2/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma3/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma4/Run2026A-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma5/Run2026A-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=62 + 61 + 66 + 65 + 60 + 60,
    n_events=11733359 + 11731043 + 11732795 + 11731165 + 11733095 + 11731599,
    is_data=True,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_egamma_b",
    id=15557176,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma1/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma2/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma3/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma4/Run2026B-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma5/Run2026B-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=536 + 532 + 534 + 529 + 533 + 535,
    n_events=205275441 + 205266455 + 205274221 + 205271520 + 205273231 + 205265468,
    is_data=True,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_egamma_c",
    id=15568826,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma1/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma2/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma3/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma4/Run2026C-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma5/Run2026C-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=603 + 611 + 594 + 590 + 592 + 589,
    n_events=375030929 + 374809724 + 374832870 + 374811337 + 374793369 + 374804007,
    is_data=True,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_egamma_d",
    id=15591574,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma1/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma2/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma3/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma4/Run2026D-PromptReco-v1/NANOAOD",  # noqa
        "/EGamma5/Run2026D-PromptReco-v1/NANOAOD",  # noqa
    ],
    n_files=334 + 325 + 335 + 327 + 332 + 327,
    n_events=125742096 + 125740549 + 125741242 + 125739959 + 125741715 + 125738632,
    is_data=True,
    aux={
        "era": "D",
    },
)
