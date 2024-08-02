# coding: utf-8

"""
Electroweak datasets for the 2023 preBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

#
# Drell-Yan
#


# inclusive (madgraph)
cpn.add_dataset(
    name="dy_lep_m50_muonhits_madgraph",
    id=14845599,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer23NanoAODv12-PilotMuonHits_130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=19967,
)

cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14770722,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer23NanoAODv12-Pilot_130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=20127,
)


#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14979374,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=439,
    n_events=193207285,
)

#
# Diboson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14784470,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=125,
    n_events=33504000,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14789850,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=16770000,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14788275,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=2517000,
)
