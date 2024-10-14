# coding: utf-8

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

# SM sample
cpn.add_dataset(
    name="hhh_4b2tau_c30_d40_amcatnlo",
    id=14846243,
    processes=[procs.hhh_4b2tau_c30_d40],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=74,
    n_events=9680000,
)
