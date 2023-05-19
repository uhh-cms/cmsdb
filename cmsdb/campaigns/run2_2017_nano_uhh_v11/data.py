# coding: utf-8

"""
CMS datasets from the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# SingleElectron
#

cpn.add_dataset(
    name="data_e_b",
    id=14172939,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017B-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=21,
    n_events=60537490,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_e_c",
    id=14172612,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017C-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=56,
    n_events=136637888,
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
        "/SingleElectron/Run2017D-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=22,
    n_events=51526521,
    aux={
        "era": "D",
    },
)

# cpn.add_dataset(
#     name="data_e_e",
#     id=14226090,
#     is_data=True,
#     processes=[procs.data_e],
#     keys=[
#         "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
#     ],
#     n_files=51,
#     n_events=102122055,
#     aux={
#         "era": "E",
#     },
# )

cpn.add_dataset(
    name="data_e_f",
    id=14173745,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017F-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=57,
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
    id=14175335,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017B-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=51,
    n_events=136300266,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_mu_c",
    id=14175349,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017C-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=65,
    n_events=165652756,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_mu_d",
    id=14173875,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017D-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=28,
    n_events=70361660,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_mu_e",
    id=14172567,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017E-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=62,
    n_events=154618774,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14172671,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017F-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=101,
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
    id=14173749,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
    "/Tau/Run2017B-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=21,
    n_events=38158216,
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_tau_c",
    id=14173679,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017C-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=29,
    n_events=55416425,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_tau_d",
    id=14173084,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017D-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=10,
    n_events=20530776,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_tau_e",
    id=14173632,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017E-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=22,
    n_events=44316628,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_tau_f",
    id=14173624,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017F-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=46,
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
    id=14173597,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017C-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=36,
    n_events=115906496,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_met_d",
    id=14173623,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017D-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=9,
    n_events=20075033,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_met_e",
    id=14173654,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017E-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=38,
    n_events=71418865,
    aux={
        "era": "E",
    },
)


cpn.add_dataset(
    name="data_met_f",
    id=14174316,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017F-UL2017_NanoAODv11-v1/NANOAOD",  # noqa
    ],
    n_files=88,
    n_events=177521562,
    aux={
        "era": "F",
    },
)
