# coding: utf-8

"""
CMS datasets from the 2018 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_uhh_v12 import campaign_run2_2018_nano_uhh_v12 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_a",
    id=14369804,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2018A-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=157,
    n_events=339013231,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_e_b",
    id=14425116,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2018B-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=71,
    n_events=153822427,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=14400993,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2018C-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=70,
    n_events=147827904,
    aux={
        "era": "C",
    },
)


cpn.add_dataset(
    name="data_e_d",
    id=14173006,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/EGamma/Run2018D-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=348,
    n_events=734264684,
    aux={
        "era": "D",
    },
)


#
# SingleMuon
#
cpn.add_dataset(
    name="data_mu_a",
    id=14668759,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018A-UL2018_NanoAODv12_GT36-v2/NANOAOD",  # noqa
    ],
    n_files=88,
    n_events=241605557,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_mu_b",
    id=14668968,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018B-UL2018_NanoAODv12_GT36-v2/NANOAOD",  # noqa
    ],
    n_files=43,
    n_events=119918017,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14668849,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018C-UL2018_NanoAODv12_GT36-v3/NANOAOD",  # noqa
    ],
    n_files=41,
    n_events=110032072,
    aux={
        "era": "C",
    },
)


cpn.add_dataset(
    name="data_mu_d",
    id=14668961,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018D-UL2018_NanoAODv12_GT36-v2/NANOAOD",  # noqa
    ],
    n_files=181,
    n_events=513884680,
    aux={
        "era": "D",
    },
)



#
# Tau
#

cpn.add_dataset(
    name="data_tau_a",
    id=14501798,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2018A-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=32,
    n_events=63214407,
    aux={
        "era": "A",
    },
)


cpn.add_dataset(
    name="data_tau_b",
    id=14386351,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2018B-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=17,
    n_events=32678961,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14380679,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2018C-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=16,
    n_events=31974422,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14443704,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2018D-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=80,
    n_events=167852084,
    aux={
        "era": "D",
    },
)


#
# MET
#

cpn.add_dataset(
    name="data_met_a",
    id=14351169,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2018A-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=24,
    n_events=52759851,
    aux={
        "era": "A",
    },
)

cpn.add_dataset(
    name="data_met_b",
    id=14175345,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017B-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=15,
    n_events=51623474,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_met_c",
    id=14364332,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2018C-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=15,
    n_events=31144738,
    aux={
        "era": "C",
    },
)


cpn.add_dataset(
    name="data_met_d",
    id=14380811,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2018D-UL2018_NanoAODv12_GT36-v1/NANOAOD",  # noqa
    ],
    n_files=93,
    n_events=160411782,
    aux={
        "era": "D",
    },
)

