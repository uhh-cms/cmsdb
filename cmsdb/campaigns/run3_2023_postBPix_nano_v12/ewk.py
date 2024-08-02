# coding: utf-8

"""
Electroweak datasets for the 2023 postBPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

#
# Drell-Yan
#


# inclusive (madgraph)
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14770995,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-Pilot_130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=18713,
)

cpn.add_dataset(
    name="dy_lep_m50_muonhits_madgraph",
    id=14845388,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer23BPixNanoAODv12-PilotMuonHits_130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=19244,
)


#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14978436,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=352,
    n_events=95759797,
)

#
# Diboson
#
cpn.add_dataset(
    name="ww_pythia",
    id=14783236,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=16734000,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14784070,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=8379000,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14784123,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1254000,
)
