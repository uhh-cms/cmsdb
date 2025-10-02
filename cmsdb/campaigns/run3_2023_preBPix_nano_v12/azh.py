# coding: utf-8

"""
A->ZH->llttbar MC Datasets
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn

cpn.add_dataset(
    name="azh_htt_zll_a1000_h330_amcatnlo",
    id=15103081,
    processes=[procs.azh_htt_zll_a1000_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h350_amcatnlo",
    id=15109407,
    processes=[procs.azh_htt_zll_a1000_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h400_amcatnlo",
    id=15102973,
    processes=[procs.azh_htt_zll_a1000_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h450_amcatnlo",
    id=15108485,
    processes=[procs.azh_htt_zll_a1000_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h500_amcatnlo",
    id=15171498,
    processes=[procs.azh_htt_zll_a1000_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h550_amcatnlo",
    id=15108589,
    processes=[procs.azh_htt_zll_a1000_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h600_amcatnlo",
    id=15112009,
    processes=[procs.azh_htt_zll_a1000_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h650_amcatnlo",
    id=15112060,
    processes=[procs.azh_htt_zll_a1000_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h700_amcatnlo",
    id=15176999,
    processes=[procs.azh_htt_zll_a1000_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h750_amcatnlo",
    id=15108787,
    processes=[procs.azh_htt_zll_a1000_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h800_amcatnlo",
    id=15109887,
    processes=[procs.azh_htt_zll_a1000_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h850_amcatnlo",
    id=15109205,
    processes=[procs.azh_htt_zll_a1000_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h900_amcatnlo",
    id=15104488,
    processes=[procs.azh_htt_zll_a1000_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h330_amcatnlo",
    id=15108906,
    processes=[procs.azh_htt_zll_a1050_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h350_amcatnlo",
    id=15104833,
    processes=[procs.azh_htt_zll_a1050_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h400_amcatnlo",
    id=15104551,
    processes=[procs.azh_htt_zll_a1050_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h450_amcatnlo",
    id=15103259,
    processes=[procs.azh_htt_zll_a1050_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h500_amcatnlo",
    id=15108925,
    processes=[procs.azh_htt_zll_a1050_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h550_amcatnlo",
    id=15111087,
    processes=[procs.azh_htt_zll_a1050_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h600_amcatnlo",
    id=15109144,
    processes=[procs.azh_htt_zll_a1050_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h650_amcatnlo",
    id=15109286,
    processes=[procs.azh_htt_zll_a1050_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h700_amcatnlo",
    id=15109885,
    processes=[procs.azh_htt_zll_a1050_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h750_amcatnlo",
    id=15104405,
    processes=[procs.azh_htt_zll_a1050_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h800_amcatnlo",
    id=15104708,
    processes=[procs.azh_htt_zll_a1050_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h850_amcatnlo",
    id=15103426,
    processes=[procs.azh_htt_zll_a1050_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h900_amcatnlo",
    id=15104710,
    processes=[procs.azh_htt_zll_a1050_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h950_amcatnlo",
    id=15109276,
    processes=[procs.azh_htt_zll_a1050_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h1000_amcatnlo",
    id=15108621,
    processes=[procs.azh_htt_zll_a1100_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h330_amcatnlo",
    id=15104727,
    processes=[procs.azh_htt_zll_a1100_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h350_amcatnlo",
    id=15104156,
    processes=[procs.azh_htt_zll_a1100_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h400_amcatnlo",
    id=15102797,
    processes=[procs.azh_htt_zll_a1100_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h450_amcatnlo",
    id=15105636,
    processes=[procs.azh_htt_zll_a1100_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h500_amcatnlo",
    id=15108991,
    processes=[procs.azh_htt_zll_a1100_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h550_amcatnlo",
    id=15104557,
    processes=[procs.azh_htt_zll_a1100_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h600_amcatnlo",
    id=15104712,
    processes=[procs.azh_htt_zll_a1100_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h650_amcatnlo",
    id=15105287,
    processes=[procs.azh_htt_zll_a1100_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h700_amcatnlo",
    id=15104827,
    processes=[procs.azh_htt_zll_a1100_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h750_amcatnlo",
    id=15109215,
    processes=[procs.azh_htt_zll_a1100_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h800_amcatnlo",
    id=15104079,
    processes=[procs.azh_htt_zll_a1100_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h850_amcatnlo",
    id=15109199,
    processes=[procs.azh_htt_zll_a1100_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h900_amcatnlo",
    id=15104729,
    processes=[procs.azh_htt_zll_a1100_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h950_amcatnlo",
    id=15108909,
    processes=[procs.azh_htt_zll_a1100_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h1000_amcatnlo",
    id=15118833,
    processes=[procs.azh_htt_zll_a1150_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h1050_amcatnlo",
    id=15104516,
    processes=[procs.azh_htt_zll_a1150_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h330_amcatnlo",
    id=15104382,
    processes=[procs.azh_htt_zll_a1150_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h350_amcatnlo",
    id=15109498,
    processes=[procs.azh_htt_zll_a1150_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h400_amcatnlo",
    id=15111923,
    processes=[procs.azh_htt_zll_a1150_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h450_amcatnlo",
    id=15108461,
    processes=[procs.azh_htt_zll_a1150_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h500_amcatnlo",
    id=15110033,
    processes=[procs.azh_htt_zll_a1150_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h550_amcatnlo",
    id=15109247,
    processes=[procs.azh_htt_zll_a1150_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h600_amcatnlo",
    id=15119665,
    processes=[procs.azh_htt_zll_a1150_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h650_amcatnlo",
    id=15110501,
    processes=[procs.azh_htt_zll_a1150_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h700_amcatnlo",
    id=15111837,
    processes=[procs.azh_htt_zll_a1150_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h750_amcatnlo",
    id=15109409,
    processes=[procs.azh_htt_zll_a1150_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h800_amcatnlo",
    id=15113644,
    processes=[procs.azh_htt_zll_a1150_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h850_amcatnlo",
    id=15103419,
    processes=[procs.azh_htt_zll_a1150_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h900_amcatnlo",
    id=15119388,
    processes=[procs.azh_htt_zll_a1150_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h950_amcatnlo",
    id=15112048,
    processes=[procs.azh_htt_zll_a1150_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1000_amcatnlo",
    id=15108900,
    processes=[procs.azh_htt_zll_a1200_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1050_amcatnlo",
    id=15103523,
    processes=[procs.azh_htt_zll_a1200_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1100_amcatnlo",
    id=15109136,
    processes=[procs.azh_htt_zll_a1200_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h330_amcatnlo",
    id=15108858,
    processes=[procs.azh_htt_zll_a1200_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h350_amcatnlo",
    id=15103671,
    processes=[procs.azh_htt_zll_a1200_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h400_amcatnlo",
    id=15109865,
    processes=[procs.azh_htt_zll_a1200_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h450_amcatnlo",
    id=15118848,
    processes=[procs.azh_htt_zll_a1200_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h500_amcatnlo",
    id=15104518,
    processes=[procs.azh_htt_zll_a1200_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h550_amcatnlo",
    id=15119603,
    processes=[procs.azh_htt_zll_a1200_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h600_amcatnlo",
    id=15108953,
    processes=[procs.azh_htt_zll_a1200_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h650_amcatnlo",
    id=15119583,
    processes=[procs.azh_htt_zll_a1200_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h700_amcatnlo",
    id=15104170,
    processes=[procs.azh_htt_zll_a1200_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h750_amcatnlo",
    id=15104563,
    processes=[procs.azh_htt_zll_a1200_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h800_amcatnlo",
    id=15103107,
    processes=[procs.azh_htt_zll_a1200_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h850_amcatnlo",
    id=15104757,
    processes=[procs.azh_htt_zll_a1200_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h900_amcatnlo",
    id=15112149,
    processes=[procs.azh_htt_zll_a1200_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h950_amcatnlo",
    id=15108997,
    processes=[procs.azh_htt_zll_a1200_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h1000_amcatnlo",
    id=15109846,
    processes=[procs.azh_htt_zll_a1250_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h1050_amcatnlo",
    id=15112095,
    processes=[procs.azh_htt_zll_a1250_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h1100_amcatnlo",
    id=15108901,
    processes=[procs.azh_htt_zll_a1250_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h1150_amcatnlo",
    id=15110665,
    processes=[procs.azh_htt_zll_a1250_h1150],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1150_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h330_amcatnlo",
    id=15109129,
    processes=[procs.azh_htt_zll_a1250_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h350_amcatnlo",
    id=15105102,
    processes=[procs.azh_htt_zll_a1250_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h400_amcatnlo",
    id=15105104,
    processes=[procs.azh_htt_zll_a1250_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h450_amcatnlo",
    id=15109535,
    processes=[procs.azh_htt_zll_a1250_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h500_amcatnlo",
    id=15109483,
    processes=[procs.azh_htt_zll_a1250_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h550_amcatnlo",
    id=15105802,
    processes=[procs.azh_htt_zll_a1250_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h600_amcatnlo",
    id=15108721,
    processes=[procs.azh_htt_zll_a1250_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h650_amcatnlo",
    id=15110362,
    processes=[procs.azh_htt_zll_a1250_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h700_amcatnlo",
    id=15110275,
    processes=[procs.azh_htt_zll_a1250_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h750_amcatnlo",
    id=15103898,
    processes=[procs.azh_htt_zll_a1250_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h800_amcatnlo",
    id=15104829,
    processes=[procs.azh_htt_zll_a1250_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h850_amcatnlo",
    id=15108823,
    processes=[procs.azh_htt_zll_a1250_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h900_amcatnlo",
    id=15104306,
    processes=[procs.azh_htt_zll_a1250_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1250_h950_amcatnlo",
    id=15109263,
    processes=[procs.azh_htt_zll_a1250_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1000_amcatnlo",
    id=15104564,
    processes=[procs.azh_htt_zll_a1300_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1100_amcatnlo",
    id=15109184,
    processes=[procs.azh_htt_zll_a1300_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1200_amcatnlo",
    id=15111597,
    processes=[procs.azh_htt_zll_a1300_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h350_amcatnlo",
    id=15110155,
    processes=[procs.azh_htt_zll_a1300_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h400_amcatnlo",
    id=15108630,
    processes=[procs.azh_htt_zll_a1300_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h500_amcatnlo",
    id=15109411,
    processes=[procs.azh_htt_zll_a1300_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h600_amcatnlo",
    id=15108939,
    processes=[procs.azh_htt_zll_a1300_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h700_amcatnlo",
    id=15106097,
    processes=[procs.azh_htt_zll_a1300_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h800_amcatnlo",
    id=15108821,
    processes=[procs.azh_htt_zll_a1300_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h900_amcatnlo",
    id=15109432,
    processes=[procs.azh_htt_zll_a1300_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1000_amcatnlo",
    id=15109412,
    processes=[procs.azh_htt_zll_a1400_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1100_amcatnlo",
    id=15108636,
    processes=[procs.azh_htt_zll_a1400_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1200_amcatnlo",
    id=15108395,
    processes=[procs.azh_htt_zll_a1400_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1300_amcatnlo",
    id=15109209,
    processes=[procs.azh_htt_zll_a1400_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h350_amcatnlo",
    id=15104681,
    processes=[procs.azh_htt_zll_a1400_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h400_amcatnlo",
    id=15109399,
    processes=[procs.azh_htt_zll_a1400_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h500_amcatnlo",
    id=15109929,
    processes=[procs.azh_htt_zll_a1400_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h600_amcatnlo",
    id=15109512,
    processes=[procs.azh_htt_zll_a1400_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h700_amcatnlo",
    id=15109163,
    processes=[procs.azh_htt_zll_a1400_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h800_amcatnlo",
    id=15103020,
    processes=[procs.azh_htt_zll_a1400_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h900_amcatnlo",
    id=15103694,
    processes=[procs.azh_htt_zll_a1400_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1000_amcatnlo",
    id=15111353,
    processes=[procs.azh_htt_zll_a1500_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1100_amcatnlo",
    id=15109148,
    processes=[procs.azh_htt_zll_a1500_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1200_amcatnlo",
    id=15109308,
    processes=[procs.azh_htt_zll_a1500_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1300_amcatnlo",
    id=15104308,
    processes=[procs.azh_htt_zll_a1500_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1400_amcatnlo",
    id=15104568,
    processes=[procs.azh_htt_zll_a1500_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h350_amcatnlo",
    id=15112160,
    processes=[procs.azh_htt_zll_a1500_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h400_amcatnlo",
    id=15108638,
    processes=[procs.azh_htt_zll_a1500_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h500_amcatnlo",
    id=15104576,
    processes=[procs.azh_htt_zll_a1500_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h600_amcatnlo",
    id=15103018,
    processes=[procs.azh_htt_zll_a1500_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h700_amcatnlo",
    id=15109817,
    processes=[procs.azh_htt_zll_a1500_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h800_amcatnlo",
    id=15102799,
    processes=[procs.azh_htt_zll_a1500_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h900_amcatnlo",
    id=15103723,
    processes=[procs.azh_htt_zll_a1500_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1000_amcatnlo",
    id=15104695,
    processes=[procs.azh_htt_zll_a1600_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1100_amcatnlo",
    id=15104725,
    processes=[procs.azh_htt_zll_a1600_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=29000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1200_amcatnlo",
    id=15110439,
    processes=[procs.azh_htt_zll_a1600_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1300_amcatnlo",
    id=15108798,
    processes=[procs.azh_htt_zll_a1600_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1400_amcatnlo",
    id=15104099,
    processes=[procs.azh_htt_zll_a1600_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1500_amcatnlo",
    id=15111810,
    processes=[procs.azh_htt_zll_a1600_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h350_amcatnlo",
    id=15112116,
    processes=[procs.azh_htt_zll_a1600_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h400_amcatnlo",
    id=15103952,
    processes=[procs.azh_htt_zll_a1600_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h500_amcatnlo",
    id=15105905,
    processes=[procs.azh_htt_zll_a1600_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h600_amcatnlo",
    id=15109128,
    processes=[procs.azh_htt_zll_a1600_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h700_amcatnlo",
    id=15109328,
    processes=[procs.azh_htt_zll_a1600_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h800_amcatnlo",
    id=15104579,
    processes=[procs.azh_htt_zll_a1600_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h900_amcatnlo",
    id=15108813,
    processes=[procs.azh_htt_zll_a1600_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1000_amcatnlo",
    id=15105638,
    processes=[procs.azh_htt_zll_a1700_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1100_amcatnlo",
    id=15109132,
    processes=[procs.azh_htt_zll_a1700_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1200_amcatnlo",
    id=15111740,
    processes=[procs.azh_htt_zll_a1700_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1300_amcatnlo",
    id=15102958,
    processes=[procs.azh_htt_zll_a1700_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1400_amcatnlo",
    id=15111162,
    processes=[procs.azh_htt_zll_a1700_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1500_amcatnlo",
    id=15104560,
    processes=[procs.azh_htt_zll_a1700_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1600_amcatnlo",
    id=15103513,
    processes=[procs.azh_htt_zll_a1700_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h350_amcatnlo",
    id=15111365,
    processes=[procs.azh_htt_zll_a1700_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h400_amcatnlo",
    id=15103388,
    processes=[procs.azh_htt_zll_a1700_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h500_amcatnlo",
    id=15111606,
    processes=[procs.azh_htt_zll_a1700_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h600_amcatnlo",
    id=15108664,
    processes=[procs.azh_htt_zll_a1700_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h700_amcatnlo",
    id=15104172,
    processes=[procs.azh_htt_zll_a1700_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h800_amcatnlo",
    id=15109307,
    processes=[procs.azh_htt_zll_a1700_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h900_amcatnlo",
    id=15103101,
    processes=[procs.azh_htt_zll_a1700_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1000_amcatnlo",
    id=15104498,
    processes=[procs.azh_htt_zll_a1800_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1100_amcatnlo",
    id=15109017,
    processes=[procs.azh_htt_zll_a1800_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1200_amcatnlo",
    id=15103581,
    processes=[procs.azh_htt_zll_a1800_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1300_amcatnlo",
    id=15109561,
    processes=[procs.azh_htt_zll_a1800_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1400_amcatnlo",
    id=15109288,
    processes=[procs.azh_htt_zll_a1800_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1500_amcatnlo",
    id=15109264,
    processes=[procs.azh_htt_zll_a1800_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1600_amcatnlo",
    id=15101332,
    processes=[procs.azh_htt_zll_a1800_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1700_amcatnlo",
    id=15103688,
    processes=[procs.azh_htt_zll_a1800_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h350_amcatnlo",
    id=15110234,
    processes=[procs.azh_htt_zll_a1800_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h400_amcatnlo",
    id=15104310,
    processes=[procs.azh_htt_zll_a1800_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h500_amcatnlo",
    id=15104706,
    processes=[procs.azh_htt_zll_a1800_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h600_amcatnlo",
    id=15109397,
    processes=[procs.azh_htt_zll_a1800_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h700_amcatnlo",
    id=15109273,
    processes=[procs.azh_htt_zll_a1800_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h800_amcatnlo",
    id=15103001,
    processes=[procs.azh_htt_zll_a1800_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h900_amcatnlo",
    id=15109127,
    processes=[procs.azh_htt_zll_a1800_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1000_amcatnlo",
    id=15109621,
    processes=[procs.azh_htt_zll_a1900_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1100_amcatnlo",
    id=15105770,
    processes=[procs.azh_htt_zll_a1900_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1200_amcatnlo",
    id=15109186,
    processes=[procs.azh_htt_zll_a1900_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1300_amcatnlo",
    id=15110946,
    processes=[procs.azh_htt_zll_a1900_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1400_amcatnlo",
    id=15103529,
    processes=[procs.azh_htt_zll_a1900_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1500_amcatnlo",
    id=15104804,
    processes=[procs.azh_htt_zll_a1900_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1600_amcatnlo",
    id=15105506,
    processes=[procs.azh_htt_zll_a1900_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1700_amcatnlo",
    id=15177069,
    processes=[procs.azh_htt_zll_a1900_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1800_amcatnlo",
    id=15102681,
    processes=[procs.azh_htt_zll_a1900_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h350_amcatnlo",
    id=15110283,
    processes=[procs.azh_htt_zll_a1900_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h400_amcatnlo",
    id=15103596,
    processes=[procs.azh_htt_zll_a1900_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h500_amcatnlo",
    id=15108796,
    processes=[procs.azh_htt_zll_a1900_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h600_amcatnlo",
    id=15109278,
    processes=[procs.azh_htt_zll_a1900_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h700_amcatnlo",
    id=15108824,
    processes=[procs.azh_htt_zll_a1900_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h800_amcatnlo",
    id=15105716,
    processes=[procs.azh_htt_zll_a1900_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h900_amcatnlo",
    id=15103599,
    processes=[procs.azh_htt_zll_a1900_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1000_amcatnlo",
    id=15105581,
    processes=[procs.azh_htt_zll_a2000_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1100_amcatnlo",
    id=15108791,
    processes=[procs.azh_htt_zll_a2000_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1200_amcatnlo",
    id=15104173,
    processes=[procs.azh_htt_zll_a2000_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1300_amcatnlo",
    id=15110441,
    processes=[procs.azh_htt_zll_a2000_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1400_amcatnlo",
    id=15103148,
    processes=[procs.azh_htt_zll_a2000_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1500_amcatnlo",
    id=15104799,
    processes=[procs.azh_htt_zll_a2000_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1600_amcatnlo",
    id=15101838,
    processes=[procs.azh_htt_zll_a2000_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1700_amcatnlo",
    id=15110884,
    processes=[procs.azh_htt_zll_a2000_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1800_amcatnlo",
    id=15109034,
    processes=[procs.azh_htt_zll_a2000_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1900_amcatnlo",
    id=15109176,
    processes=[procs.azh_htt_zll_a2000_h1900],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h350_amcatnlo",
    id=15111768,
    processes=[procs.azh_htt_zll_a2000_h350],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h400_amcatnlo",
    id=15109234,
    processes=[procs.azh_htt_zll_a2000_h400],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h500_amcatnlo",
    id=15111047,
    processes=[procs.azh_htt_zll_a2000_h500],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h600_amcatnlo",
    id=15109815,
    processes=[procs.azh_htt_zll_a2000_h600],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h700_amcatnlo",
    id=15103137,
    processes=[procs.azh_htt_zll_a2000_h700],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h800_amcatnlo",
    id=15104759,
    processes=[procs.azh_htt_zll_a2000_h800],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h900_amcatnlo",
    id=15111468,
    processes=[procs.azh_htt_zll_a2000_h900],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1000_amcatnlo",
    id=15109532,
    processes=[procs.azh_htt_zll_a2100_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1100_amcatnlo",
    id=15112056,
    processes=[procs.azh_htt_zll_a2100_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1200_amcatnlo",
    id=15119457,
    processes=[procs.azh_htt_zll_a2100_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1300_amcatnlo",
    id=15112088,
    processes=[procs.azh_htt_zll_a2100_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1400_amcatnlo",
    id=15111440,
    processes=[procs.azh_htt_zll_a2100_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1500_amcatnlo",
    id=15110595,
    processes=[procs.azh_htt_zll_a2100_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1600_amcatnlo",
    id=15109295,
    processes=[procs.azh_htt_zll_a2100_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1700_amcatnlo",
    id=15119607,
    processes=[procs.azh_htt_zll_a2100_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1800_amcatnlo",
    id=15119398,
    processes=[procs.azh_htt_zll_a2100_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1900_amcatnlo",
    id=15119667,
    processes=[procs.azh_htt_zll_a2100_h1900],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h2000_amcatnlo",
    id=15118922,
    processes=[procs.azh_htt_zll_a2100_h2000],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h350_amcatnlo",
    id=15119632,
    processes=[procs.azh_htt_zll_a2100_h350],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h400_amcatnlo",
    id=15110916,
    processes=[procs.azh_htt_zll_a2100_h400],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h500_amcatnlo",
    id=15106548,
    processes=[procs.azh_htt_zll_a2100_h500],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h600_amcatnlo",
    id=15102565,
    processes=[procs.azh_htt_zll_a2100_h600],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h700_amcatnlo",
    id=15104520,
    processes=[procs.azh_htt_zll_a2100_h700],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h800_amcatnlo",
    id=15105493,
    processes=[procs.azh_htt_zll_a2100_h800],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h900_amcatnlo",
    id=15110955,
    processes=[procs.azh_htt_zll_a2100_h900],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a430_h330_amcatnlo",
    id=15102873,
    processes=[procs.azh_htt_zll_a430_h330],
    keys=[
        "/AToZHToLLTTbar_MA-430_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h330_amcatnlo",
    id=15108457,
    processes=[procs.azh_htt_zll_a450_h330],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h350_amcatnlo",
    id=15103233,
    processes=[procs.azh_htt_zll_a450_h350],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h330_amcatnlo",
    id=15103522,
    processes=[procs.azh_htt_zll_a500_h330],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h350_amcatnlo",
    id=15110197,
    processes=[procs.azh_htt_zll_a500_h350],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h400_amcatnlo",
    id=15109402,
    processes=[procs.azh_htt_zll_a500_h400],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h330_amcatnlo",
    id=15108876,
    processes=[procs.azh_htt_zll_a550_h330],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h350_amcatnlo",
    id=15103884,
    processes=[procs.azh_htt_zll_a550_h350],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h400_amcatnlo",
    id=15103195,
    processes=[procs.azh_htt_zll_a550_h400],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h450_amcatnlo",
    id=15104473,
    processes=[procs.azh_htt_zll_a550_h450],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h330_amcatnlo",
    id=15109015,
    processes=[procs.azh_htt_zll_a600_h330],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h350_amcatnlo",
    id=15104269,
    processes=[procs.azh_htt_zll_a600_h350],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h400_amcatnlo",
    id=15109165,
    processes=[procs.azh_htt_zll_a600_h400],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h450_amcatnlo",
    id=15109097,
    processes=[procs.azh_htt_zll_a600_h450],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h500_amcatnlo",
    id=15103897,
    processes=[procs.azh_htt_zll_a600_h500],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h330_amcatnlo",
    id=15108608,
    processes=[procs.azh_htt_zll_a650_h330],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h350_amcatnlo",
    id=15105050,
    processes=[procs.azh_htt_zll_a650_h350],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h400_amcatnlo",
    id=15104392,
    processes=[procs.azh_htt_zll_a650_h400],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h450_amcatnlo",
    id=15108936,
    processes=[procs.azh_htt_zll_a650_h450],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h500_amcatnlo",
    id=15108624,
    processes=[procs.azh_htt_zll_a650_h500],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h550_amcatnlo",
    id=15103772,
    processes=[procs.azh_htt_zll_a650_h550],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h330_amcatnlo",
    id=15103519,
    processes=[procs.azh_htt_zll_a700_h330],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h350_amcatnlo",
    id=15111409,
    processes=[procs.azh_htt_zll_a700_h350],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h400_amcatnlo",
    id=15110673,
    processes=[procs.azh_htt_zll_a700_h400],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h450_amcatnlo",
    id=15109382,
    processes=[procs.azh_htt_zll_a700_h450],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h500_amcatnlo",
    id=15105289,
    processes=[procs.azh_htt_zll_a700_h500],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h550_amcatnlo",
    id=15109378,
    processes=[procs.azh_htt_zll_a700_h550],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h600_amcatnlo",
    id=15105011,
    processes=[procs.azh_htt_zll_a700_h600],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h330_amcatnlo",
    id=15108926,
    processes=[procs.azh_htt_zll_a750_h330],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h350_amcatnlo",
    id=15109380,
    processes=[procs.azh_htt_zll_a750_h350],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h400_amcatnlo",
    id=15103889,
    processes=[procs.azh_htt_zll_a750_h400],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h450_amcatnlo",
    id=15104292,
    processes=[procs.azh_htt_zll_a750_h450],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h500_amcatnlo",
    id=15103990,
    processes=[procs.azh_htt_zll_a750_h500],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h550_amcatnlo",
    id=15109084,
    processes=[procs.azh_htt_zll_a750_h550],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h600_amcatnlo",
    id=15101947,
    processes=[procs.azh_htt_zll_a750_h600],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h650_amcatnlo",
    id=15105786,
    processes=[procs.azh_htt_zll_a750_h650],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h330_amcatnlo",
    id=15103253,
    processes=[procs.azh_htt_zll_a800_h330],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h350_amcatnlo",
    id=15104583,
    processes=[procs.azh_htt_zll_a800_h350],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h400_amcatnlo",
    id=15104041,
    processes=[procs.azh_htt_zll_a800_h400],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h450_amcatnlo",
    id=15108150,
    processes=[procs.azh_htt_zll_a800_h450],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h500_amcatnlo",
    id=15109099,
    processes=[procs.azh_htt_zll_a800_h500],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h550_amcatnlo",
    id=15103515,
    processes=[procs.azh_htt_zll_a800_h550],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h600_amcatnlo",
    id=15118980,
    processes=[procs.azh_htt_zll_a800_h600],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h650_amcatnlo",
    id=15111275,
    processes=[procs.azh_htt_zll_a800_h650],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h700_amcatnlo",
    id=15104153,
    processes=[procs.azh_htt_zll_a800_h700],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h330_amcatnlo",
    id=15106685,
    processes=[procs.azh_htt_zll_a850_h330],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h350_amcatnlo",
    id=15105815,
    processes=[procs.azh_htt_zll_a850_h350],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h400_amcatnlo",
    id=15105679,
    processes=[procs.azh_htt_zll_a850_h400],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h450_amcatnlo",
    id=15102339,
    processes=[procs.azh_htt_zll_a850_h450],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h500_amcatnlo",
    id=15099761,
    processes=[procs.azh_htt_zll_a850_h500],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h550_amcatnlo",
    id=15100128,
    processes=[procs.azh_htt_zll_a850_h550],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h600_amcatnlo",
    id=15109522,
    processes=[procs.azh_htt_zll_a850_h600],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h650_amcatnlo",
    id=15105640,
    processes=[procs.azh_htt_zll_a850_h650],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h700_amcatnlo",
    id=15104619,
    processes=[procs.azh_htt_zll_a850_h700],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h750_amcatnlo",
    id=15104507,
    processes=[procs.azh_htt_zll_a850_h750],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h330_amcatnlo",
    id=15108706,
    processes=[procs.azh_htt_zll_a900_h330],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h350_amcatnlo",
    id=15111306,
    processes=[procs.azh_htt_zll_a900_h350],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h400_amcatnlo",
    id=15119820,
    processes=[procs.azh_htt_zll_a900_h400],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h450_amcatnlo",
    id=15108752,
    processes=[procs.azh_htt_zll_a900_h450],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h500_amcatnlo",
    id=15106408,
    processes=[procs.azh_htt_zll_a900_h500],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h550_amcatnlo",
    id=15105105,
    processes=[procs.azh_htt_zll_a900_h550],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h600_amcatnlo",
    id=15104508,
    processes=[procs.azh_htt_zll_a900_h600],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h650_amcatnlo",
    id=15104331,
    processes=[procs.azh_htt_zll_a900_h650],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h700_amcatnlo",
    id=15105718,
    processes=[procs.azh_htt_zll_a900_h700],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h750_amcatnlo",
    id=15108690,
    processes=[procs.azh_htt_zll_a900_h750],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h800_amcatnlo",
    id=15104806,
    processes=[procs.azh_htt_zll_a900_h800],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h330_amcatnlo",
    id=15104621,
    processes=[procs.azh_htt_zll_a950_h330],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h350_amcatnlo",
    id=15105633,
    processes=[procs.azh_htt_zll_a950_h350],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h400_amcatnlo",
    id=15109145,
    processes=[procs.azh_htt_zll_a950_h400],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h450_amcatnlo",
    id=15108639,
    processes=[procs.azh_htt_zll_a950_h450],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h500_amcatnlo",
    id=15103721,
    processes=[procs.azh_htt_zll_a950_h500],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h550_amcatnlo",
    id=15108590,
    processes=[procs.azh_htt_zll_a950_h550],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h600_amcatnlo",
    id=15109052,
    processes=[procs.azh_htt_zll_a950_h600],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h650_amcatnlo",
    id=15109809,
    processes=[procs.azh_htt_zll_a950_h650],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h700_amcatnlo",
    id=15104803,
    processes=[procs.azh_htt_zll_a950_h700],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h750_amcatnlo",
    id=15109735,
    processes=[procs.azh_htt_zll_a950_h750],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h800_amcatnlo",
    id=15103278,
    processes=[procs.azh_htt_zll_a950_h800],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h850_amcatnlo",
    id=15104084,
    processes=[procs.azh_htt_zll_a950_h850],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=32000,
)
