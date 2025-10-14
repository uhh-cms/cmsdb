# coding: utf-8

"""
CMS datasets from the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# Muon
#

cpn.add_dataset(
    name="data_mu_c1",
    id=14787055,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/Muon1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=90 + 73,
    n_events=54715896 + 54698315,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c2",
    id=14787019,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/Muon1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=31 + 33,
    n_events=17063451 + 17059895,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c3",
    id=14787140,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
        "/Muon1/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=42 + 30,
    n_events=20015377 + 20010429,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_mu_c4",
    id=14786982,
    processes=[procs.data_mu],
    keys=[
        "/Muon0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
        "/Muon1/Run2023C-22Sep2023_v4-v2/NANOAOD",  # noqa
    ],
    n_files=165 + 108,
    n_events=138943783 + 138912262,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)
#
# E/Gamma
#
cpn.add_dataset(
    name="data_egamma_c1",
    id=14786980,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=90 + 71,
    n_events=67598081 + 67582665,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma_c2",
    id=14787633,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=22 + 24,
    n_events=17233307 + 17230822,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma_c3",
    id=14787548,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=26 + 25,
    n_events=21993048 + 21987586,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_egamma_c4",
    id=14786977,
    processes=[procs.data_egamma],
    keys=[
        "/EGamma0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
        "/EGamma1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=168 + 177,
    n_events=160108119 + 160049621,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

#
# Tau
#

cpn.add_dataset(
    name="data_tau_c1",
    id=14826261,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v1-v2/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=14484171,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_tau_c2",
    id=14787195,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=12,
    n_events=5178955,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_tau_c3",
    id=14787785,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=12,
    n_events=6470602,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)


cpn.add_dataset(
    name="data_tau_c4",
    id=14786972,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=70,
    n_events=45176805,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

#
# MuonEG
#

cpn.add_dataset(
    name="data_muoneg_c1",
    id=14784883,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=11,
    n_events=3502967,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c2",
    id=14784846,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=25,
    n_events=9772655,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c3",
    id=14787041,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=8,
    n_events=2735170,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv123",
    },
)

cpn.add_dataset(
    name="data_muoneg_c4",
    id=14784848,
    processes=[procs.data_muoneg],
    keys=[
        "/MuonEG/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=41,
    n_events=24205121,
    is_data=True,
    aux={
        "era": "C",
        "jec_era": "RunCv4",
    },
)

#
# JetMET
#

cpn.add_dataset(
    name="data_jethtmet_c1",
    id=14784875,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023C-22Sep2023_v1-v1/NANOAOD",  # noqa
    ],
    n_files=69 + 73,
    n_events=56089464 + 56071751,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_jethtmet_c2",
    id=14784867,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023C-22Sep2023_v2-v1/NANOAOD",  # noqa
    ],
    n_files=34 + 30,
    n_events=17154040 + 17149627,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_jethtmet_c3",
    id=14784909,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023C-22Sep2023_v3-v1/NANOAOD",  # noqa
    ],
    n_files=28 + 27,
    n_events=14859886 + 14852598,
    is_data=True,
    aux={
        "era": "C",
    }
)

cpn.add_dataset(
    name="data_jethtmet_c4",
    id=14785390,
    processes=[procs.data_jethtmet],
    keys=[
        "/JetMET0/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
        "/JetMET1/Run2023C-22Sep2023_v4-v1/NANOAOD",  # noqa
    ],
    n_files=125 + 124,
    n_events=105910300 + 105874180,
    is_data=True,
    aux={
        "era": "C",
    }
)
