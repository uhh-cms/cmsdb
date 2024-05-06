
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

cpn.add_dataset(
    name="hhh4b2tau_c3_0_d4_0_madgraph",
    id=14791536,
    processes=[procs.hhh_ggf_4b2tau],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=9483880,
)