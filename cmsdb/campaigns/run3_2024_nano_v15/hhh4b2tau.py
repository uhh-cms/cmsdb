
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

# SM sample
cpn.add_dataset(
    name="hhh_4b2tau_c30_d40_amcatnlo",
    id=14791536,
    processes=[procs.hhh_4b2tau_c30_d40],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=9483880,
)

cpn.add_dataset(
    name="hhh_4b2tau_c30_d499_amcatnlo",
    id=14804364,
    processes=[procs.hhh_4b2tau_c30_d499],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=387652,
)

cpn.add_dataset(
    name="hhh_4b2tau_c30_d4m1_amcatnlo",
    id=14796291,
    processes=[procs.hhh_4b2tau_c30_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=393610,
)

cpn.add_dataset(
    name="hhh_4b2tau_c319_d419_amcatnlo",
    id=14805829,
    processes=[procs.hhh_4b2tau_c319_d419],
    keys=[
        "/HHHto4B2Tau_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=393190,
)

cpn.add_dataset(
    name="hhh_4b2tau_c31_d40_amcatnlo",
    id=14805285,
    processes=[procs.hhh_4b2tau_c31_d40],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=395878,
)

cpn.add_dataset(
    name="hhh_4b2tau_c31_d42_amcatnlo",
    id=14797470,
    processes=[procs.hhh_4b2tau_c31_d42],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=407634,
)

cpn.add_dataset(
    name="hhh_4b2tau_c32_d4m1_amcatnlo",
    id=14798802,
    processes=[procs.hhh_4b2tau_c32_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=396595,
)

cpn.add_dataset(
    name="hhh_4b2tau_c34_d49_amcatnlo",
    id=14885952,
    processes=[procs.hhh_4b2tau_c34_d49],
    keys=[
        "/HHHto4B2Tau_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=262292,
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1_d40_amcatnlo",
    id=14797875,
    processes=[procs.hhh_4b2tau_c3m1_d40],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=372600,
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1_d4m1_amcatnlo",
    id=14794127,
    processes=[procs.hhh_4b2tau_c3m1_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=398634,
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1p5_d4m0p5_amcatnlo",
    id=14796572,
    processes=[procs.hhh_4b2tau_c3m1p5_d4m0p5],
    keys=[
        "/HHHto4B2Tau_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=406138,
)
