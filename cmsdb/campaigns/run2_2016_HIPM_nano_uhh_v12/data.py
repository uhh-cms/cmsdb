# coding: utf-8


"""CMS datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH."""


import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn

# SingleElectron

cpn.add_dataset(
    name="data_e_b",
    id=14215862,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=1_921,
    n_events=246_440_440,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=14215473,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=817,
    n_events=97_259_854,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=14215730,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=1_135,
    n_events=148_167_727,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=14245922,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v5/NANOAOD",  # noqa
    ],
    n_files=1_024,
    n_events=117_269_446,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=14215954,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=549,
    n_events=61_735_326,
    aux={
        "era": "F",
    },
)

# SingleMuon

cpn.add_dataset(
    name="data_mu_b",
    id=14218988,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=986,
    n_events=158_145_722,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14218866,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=448,
    n_events=67_441_308,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14215508,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=630,
    n_events=98_017_996,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=14219720,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=640,
    n_events=90_984_718,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14218111,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=433,
    n_events=57_465_359,
    aux={
        "era": "F",
    },
)


# Tau

cpn.add_dataset(
    name="data_tau_b",
    id=14216759,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=512,
    n_events=68_736_788,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14216795,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=301,
    n_events=36_931_473,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14216809,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=510,
    n_events=56_827_771,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=14217195,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=507,
    n_events=58_343_324,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14216534,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=315,
    n_events=36_189_610,
    aux={
        "era": "F",
    },
)


# MET

cpn.add_dataset(
    name="data_met_b",
    id=14216190,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=274,
    n_events=35987712,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=14216283,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=142,
    n_events=17381222,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14223521,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=187,
    n_events=20947429,
    aux={
        "era": "D",
    },
)


cpn.add_dataset(
    name="data_met_e",
    id=14216335,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=215,
    n_events=22348402,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=14216275,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv12UHH-v2/NANOAOD",  # noqa
    ],
    n_files=114,
    n_events=11936579,
    aux={
        "era": "F",
    },
)
