# coding: utf-8

"""
Higgs datasets for the 2018 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v11 import campaign_run2_2018_nano_v11 as cpn

cpn.add_dataset(
    name="zz_llll_powheg",
    id=14058483,
    processes=[procs.zz_llll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=6689900,
)
