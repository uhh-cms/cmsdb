# coding: utf-8

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

# SM sample

cpn.add_dataset(
    name="hhh4b2tau_c3_0_d4_0_madgraph",
    id=14846187,
    processes=[procs.hhh_ggf_4b2tau],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=4968000,
)
