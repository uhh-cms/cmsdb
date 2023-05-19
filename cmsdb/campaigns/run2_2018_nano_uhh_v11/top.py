# coding: utf-8

"""
Top quark datasets for the 2018 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14197224,
    processes=[procs.tt_dl],
    keys=[
        "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv11-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=146010000,
)
