# coding: utf-8

"""
Triple-Higgs datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn


cpn.add_dataset(
    name="hhh_4b2tau_c30_d40_amcatnlo",
    id=14846153,
    processes=[procs.hhh_4b2tau_c30_d40],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=9_682_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)
