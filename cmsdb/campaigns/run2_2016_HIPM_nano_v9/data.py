# coding: utf-8

"""
CMS datasets from the 2016 data-taking campaign (HIPM)
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_v9 import campaign_run2_2016_HIPM_nano_v9 as cpn

#
# JetHT
#


cpn.add_dataset(
    name="data_jetht_b",
    id=14345758,  # other id of second dataset 14345191
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
        "/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=85,  # 11 + 74
    n_events=143478756,  # 9726665 + 133752091
    aux={
        "era": "B",
    },
)

cpn.add_dataset(
    name="data_jetht_c",
    id=14345718,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=45,
    n_events=46495988,
    aux={
        "era": "C",
    },
)

cpn.add_dataset(
    name="data_jetht_d",
    id=14345368,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=65,
    n_events=73330042,
    aux={
        "era": "D",
    },
)

cpn.add_dataset(
    name="data_jetht_e",
    id=14345688,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=49,
    n_events=69219288,
    aux={
        "era": "E",
    },
)

cpn.add_dataset(
    name="data_jetht_f",
    id=14345749,
    is_data=True,
    processes=[procs.data_jetht],
    keys=[
        "/JetHT/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD",
    ],
    n_files=52,
    n_events=41564915,
    aux={
        "era": "F",
    },
)
