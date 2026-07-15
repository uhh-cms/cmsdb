# coding: utf-8

"""
Recorded datasets for the 2024 data-taking campaign with datasets at JMENanoAOD tier in version 15.
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_JMEnano_v15 import campaign_run3_2024_JMEnano_v15 as cpn

#
# Jet/MET
#

cpn.add_dataset(
    name="data_jetmet_c",
    id=15321032,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024C-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024C-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "C",
            },
            n_files=161 + 155,  # 161-0
            n_events=67828208 + 69648563,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=15321043,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024D-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024D-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "D",
            },
            n_files=198 + 167,  # 198-0
            n_events=75982398 + 75810110,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_e",
    id=15320996,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024E-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024E-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "E",
            },
            n_files=262 + 250,  # 262-0
            n_events=123673375 + 123602626,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_f",
    id=15320962,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024F-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024F-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "F",
            },
            n_files=634 + 625,  # 634-0
            n_events=308383420 + 308812258,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_g",
    id=15320916,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024G-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024G-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "G",
            },
            n_files=751 + 817,  # 751-0
            n_events=396556815 + 396333090,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_h",
    id=15321388,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024H-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024H-JMENANOv15-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "H",
            },
            n_files=117 + 106,  # 117-0
            n_events=55794457 + 55790857,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_i",
    id=15329863,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024I-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-JMENANOv15-v1/NANOAOD",  # noqa: E501
                "/JetMET0/Run2024I-JMENANOv15_v2-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-JMENANOv15_v2-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "era": "I",
            },
            n_files=129 + 124 + 229 + 177,  # 129-0
            n_events=59259348 + 59255632 + 116046182 + 115844607,
        ),
    ),
)
