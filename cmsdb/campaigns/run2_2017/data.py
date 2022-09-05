# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017 import campaign_run2_2017


#
# SingleElectron
#

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunB",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunC",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunD",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunE",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunF",
    },
)


#
# SingleMuon
#

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunB",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunC",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunD",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunE",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunF",
    },
)


#
# Tau
#

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunB",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunC",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunD",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunE",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunF",
    },
)


#
# MET
#

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunB",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunC",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunD",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunE",
    },
)

campaign_run2_2017.add_dataset(
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
        "jec_era": "RunF",
    },
)
