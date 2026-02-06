# coding: utf-8

"""
Recorded datasets for the 2024 data-taking campaign with datasets at JMENanoAOD tier in version 14.
"""
from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_JMEnano_v14 import campaign_run3_2024_JMEnano_v14 as cpn

#
# Jet/MET
#

cpn.add_dataset(
    name="data_jetmet_b",
    id=14951623,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024B-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024B-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "B",
            },
            n_files=18 + 19,
            n_events=8646489 + 8637923,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_c",
    id=14952316,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024C-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024C-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "C",
            },
            n_files=151 + 140,
            n_events=71225117 + 71237941,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_d",
    id=14960754,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024D-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024D-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "D",
            },
            n_files=175 + 167,
            n_events=77429100 + 77411275,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_e",
    id=14966398,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024E-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024E-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET0/Run2024E-PromptJMENano_v2-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024E-PromptJMENano_v2-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "E",
            },
            n_files=140 + 144 + 101 + 110,
            n_events=69338632 + 69326400 + 57056487 + 57052071,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_f",
    id=15036754,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024F-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024F-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "F",
            },
            n_files=435 + 455,
            n_events=312020081 + 311961806,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_g",
    id=15059613,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024G-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024G-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "G",
            },
            n_files=621 + 609,  # 621-0
            n_events=401169857 + 400821545,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_h",
    id=15084796,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024H-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024H-PromptJMENano-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "H",
            },
            n_files=91 + 88,
            n_events=56068074 + 56056824,
        ),
    ),
)

cpn.add_dataset(
    name="data_jetmet_i",
    id=15195641,
    is_data=True,
    processes=[procs.data_jethtmet],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024I-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-PromptJMENano-v1/NANOAOD",  # noqa: E501
                "/JetMET0/Run2024I-PromptJMENano_v2-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-PromptJMENano_v2-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [],
                "prompt": True,
                "era": "I",
            },
            n_files=76 + 76 + 141 + 128,
            n_events=60691186 + 60729426 + 116871063 + 116855237,
        ),
    ),
)
