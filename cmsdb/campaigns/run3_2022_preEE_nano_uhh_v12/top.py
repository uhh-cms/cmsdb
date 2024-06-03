# coding: utf-8

"""
Top quark related datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn  # noqa


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14791247,
    processes=[procs.tt_sl],
    keys=[
        "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=316,
    n_events=89_455_475,
    aux={
        "nominal_merging_factor": 5,
    },
)
