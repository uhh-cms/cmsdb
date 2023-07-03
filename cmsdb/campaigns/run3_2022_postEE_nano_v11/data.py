# coding: utf-8

"""
CMS datasets from the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v11 import campaign_run3_2022_postEE_nano_v11 as cpn



#
# Muon
#

cpn.add_dataset(
    name="data_mu_e",
    id=14665058,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022E-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=98,
    n_events=142785268,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_mu_f",
    id=14578756,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022F-PromptNanoAODv11_v1-v2/NANOAOD",
    ],
    n_files=290,
    n_events=449906805,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_mu_g",
    id=14578734,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/Muon/Run2022G-PromptNanoAODv11_v1-v2/NANOAOD",
    ],
    n_files=51,
    n_events=76689396,
    aux={
        "era": "G",
    },
)

#
# E/Gamma
#

cpn.add_dataset(
    name="data_egamma_e",
    id=14670601,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022E-ReRecoNanoAODv11-v1/NANOAOD",
    ],
    n_files=99,
    n_events=149463867,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_egamma_f",
    id=14579815,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022F-PromptNanoAODv11_v1-v2/NANOAOD",
    ],
    n_files=343,
    n_events=464472966,
    aux={
        "era": "F",
    },
)

cpn.add_dataset(
    name="data_egamma_g",
    id=14579488,
    is_data=True,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma/Run2022G-PromptNanoAODv11_v1-v2/NANOAOD",
    ],
    n_files=60,
    n_events=76828141,
    aux={
        "era": "G",
    },
)
