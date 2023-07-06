# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_b",
    id=14226251,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=60537490,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=14226092,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=136637888,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_e_d",
    id=14227611,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=37,
    n_events=51512837,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_e_e",
    id=14226090,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=51,
    n_events=102122055,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_e_f",
    id=14226476,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=66,
    n_events=128467223,
    aux={
        "era": "F",
    },
)


#
# SingleMuon
#

cpn.add_dataset(
    name="data_mu_b",
    id=14226191,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=79,
    n_events=136300266,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14226140,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=117,
    n_events=165652756,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14226234,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=47,
    n_events=70361660,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=14235644,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=78,
    n_events=154618774,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14226183,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=115,
    n_events=242140980,
    aux={
        "era": "F",
    },
)


#
# Tau
#

cpn.add_dataset(
    name="data_tau_b",
    id=14233603,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=38158216,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14233706,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=45,
    n_events=55416425,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14233103,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=13,
    n_events=20530776,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=14233325,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017E-UL2017_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=36,
    n_events=44316628,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14232807,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=88502118,
    aux={
        "era": "F",
    },
)


#
# MET
#

cpn.add_dataset(
    name="data_met_b",
    id=14225468,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=43,
    n_events=51623474,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=14226051,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=53,
    n_events=115906496,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14230935,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=15,
    n_events=20075033,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_e",
    id=14225819,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=48,
    n_events=71418865,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_met_f",
    id=14224849,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=133,
    n_events=177521562,
    aux={
        "era": "F",
    },
)


#
# SinglePhoton
#

cpn.add_dataset(
    name="data_gamma_b",
    id=14226103,
    is_data=True,
    processes=[procs.data_gamma],
    keys=[
        "/SinglePhoton/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=10,
    n_events=15950935,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_gamma_c",
    id=14226292,
    is_data=True,
    processes=[procs.data_gamma],
    keys=[
        "/SinglePhoton/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=34,
    n_events=42182948,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_gamma_d",
    id=14226047,
    is_data=True,
    processes=[procs.data_gamma],
    keys=[
        "/SinglePhoton/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=7,
    n_events=9753462,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_gamma_e",
    id=14226326,
    is_data=True,
    processes=[procs.data_gamma],
    keys=[
        "/SinglePhoton/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=22,
    n_events=19011446,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_gamma_f",
    id=14226332,
    is_data=True,
    processes=[procs.data_gamma],
    keys=[
        "/SinglePhoton/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=31,
    n_events=29783015,
    aux={
        "era": "F",
    },
)
