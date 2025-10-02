# coding: utf-8

"""
A->ZH->llttbar MC Datasets
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn

# MA 1000, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1000_h330_amcatnlo",
    id=15109555,
    processes=[procs.azh_htt_zll_a1000_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1000, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1000_h350_amcatnlo",
    id=15111270,
    processes=[procs.azh_htt_zll_a1000_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1000, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1000_h400_amcatnlo",
    id=15111326,
    processes=[procs.azh_htt_zll_a1000_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1000, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1000_h450_amcatnlo",
    id=15111404,
    processes=[procs.azh_htt_zll_a1000_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1000, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1000_h500_amcatnlo",
    id=15109580,
    processes=[procs.azh_htt_zll_a1000_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1000, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1000_h550_amcatnlo",
    id=15109652,
    processes=[procs.azh_htt_zll_a1000_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1000, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1000_h600_amcatnlo",
    id=15110447,
    processes=[procs.azh_htt_zll_a1000_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1000, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1000_h650_amcatnlo",
    id=15104168,
    processes=[procs.azh_htt_zll_a1000_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1000, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1000_h700_amcatnlo",
    id=15111521,
    processes=[procs.azh_htt_zll_a1000_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1000, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1000_h750_amcatnlo",
    id=15098967,
    processes=[procs.azh_htt_zll_a1000_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1000, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1000_h800_amcatnlo",
    id=15109768,
    processes=[procs.azh_htt_zll_a1000_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1000, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1000_h850_amcatnlo",
    id=15103969,
    processes=[procs.azh_htt_zll_a1000_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 1000, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1000_h900_amcatnlo",
    id=15109775,
    processes=[procs.azh_htt_zll_a1000_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1050, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1050_h330_amcatnlo",
    id=15109804,
    processes=[procs.azh_htt_zll_a1050_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1050_h350_amcatnlo",
    id=15111368,
    processes=[procs.azh_htt_zll_a1050_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1050_h400_amcatnlo",
    id=15110247,
    processes=[procs.azh_htt_zll_a1050_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1050_h450_amcatnlo",
    id=15110696,
    processes=[procs.azh_htt_zll_a1050_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1050, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1050_h500_amcatnlo",
    id=15109167,
    processes=[procs.azh_htt_zll_a1050_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1050, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1050_h550_amcatnlo",
    id=15109235,
    processes=[procs.azh_htt_zll_a1050_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1050, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1050_h600_amcatnlo",
    id=15110471,
    processes=[procs.azh_htt_zll_a1050_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1050_h650_amcatnlo",
    id=15111514,
    processes=[procs.azh_htt_zll_a1050_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1050_h700_amcatnlo",
    id=15109559,
    processes=[procs.azh_htt_zll_a1050_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1050, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1050_h750_amcatnlo",
    id=15110749,
    processes=[procs.azh_htt_zll_a1050_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1050, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1050_h800_amcatnlo",
    id=15111671,
    processes=[procs.azh_htt_zll_a1050_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1050, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1050_h850_amcatnlo",
    id=15110940,
    processes=[procs.azh_htt_zll_a1050_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1050, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1050_h900_amcatnlo",
    id=15110949,
    processes=[procs.azh_htt_zll_a1050_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1050, MH: 950
cpn.add_dataset(
    name="azh_htt_zll_a1050_h950_amcatnlo",
    id=15111135,
    processes=[procs.azh_htt_zll_a1050_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1100, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1100_h1000_amcatnlo",
    id=15103971,
    processes=[procs.azh_htt_zll_a1100_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 1100, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1100_h330_amcatnlo",
    id=15109728,
    processes=[procs.azh_htt_zll_a1100_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1100, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1100_h350_amcatnlo",
    id=15110870,
    processes=[procs.azh_htt_zll_a1100_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1100, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1100_h400_amcatnlo",
    id=15110490,
    processes=[procs.azh_htt_zll_a1100_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 1100, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1100_h450_amcatnlo",
    id=15111811,
    processes=[procs.azh_htt_zll_a1100_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1100, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1100_h500_amcatnlo",
    id=15111084,
    processes=[procs.azh_htt_zll_a1100_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1100, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1100_h550_amcatnlo",
    id=15111657,
    processes=[procs.azh_htt_zll_a1100_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1100, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1100_h600_amcatnlo",
    id=15110119,
    processes=[procs.azh_htt_zll_a1100_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1100, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1100_h650_amcatnlo",
    id=15111211,
    processes=[procs.azh_htt_zll_a1100_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1100, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1100_h700_amcatnlo",
    id=15103973,
    processes=[procs.azh_htt_zll_a1100_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 1100, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1100_h750_amcatnlo",
    id=15109617,
    processes=[procs.azh_htt_zll_a1100_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1100, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1100_h800_amcatnlo",
    id=15111905,
    processes=[procs.azh_htt_zll_a1100_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1100, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1100_h850_amcatnlo",
    id=15111872,
    processes=[procs.azh_htt_zll_a1100_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1100, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1100_h900_amcatnlo",
    id=15109606,
    processes=[procs.azh_htt_zll_a1100_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1100, MH: 950
cpn.add_dataset(
    name="azh_htt_zll_a1100_h950_amcatnlo",
    id=15109894,
    processes=[procs.azh_htt_zll_a1100_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1150_h1000_amcatnlo",
    id=15110349,
    processes=[procs.azh_htt_zll_a1150_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 1050
cpn.add_dataset(
    name="azh_htt_zll_a1150_h1050_amcatnlo",
    id=15110267,
    processes=[procs.azh_htt_zll_a1150_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1150_h330_amcatnlo",
    id=15110817,
    processes=[procs.azh_htt_zll_a1150_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1150, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1150_h350_amcatnlo",
    id=15103975,
    processes=[procs.azh_htt_zll_a1150_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1150_h400_amcatnlo",
    id=15110663,
    processes=[procs.azh_htt_zll_a1150_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1150, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1150_h450_amcatnlo",
    id=15110408,
    processes=[procs.azh_htt_zll_a1150_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1150, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1150_h500_amcatnlo",
    id=15104106,
    processes=[procs.azh_htt_zll_a1150_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1150, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1150_h550_amcatnlo",
    id=15109766,
    processes=[procs.azh_htt_zll_a1150_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 1150, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1150_h600_amcatnlo",
    id=15109510,
    processes=[procs.azh_htt_zll_a1150_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1150, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1150_h650_amcatnlo",
    id=15110893,
    processes=[procs.azh_htt_zll_a1150_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1150_h700_amcatnlo",
    id=15110981,
    processes=[procs.azh_htt_zll_a1150_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1150, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1150_h750_amcatnlo",
    id=15112269,
    processes=[procs.azh_htt_zll_a1150_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1150, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1150_h800_amcatnlo",
    id=15109798,
    processes=[procs.azh_htt_zll_a1150_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1150, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1150_h850_amcatnlo",
    id=15110282,
    processes=[procs.azh_htt_zll_a1150_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1150, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1150_h900_amcatnlo",
    id=15109933,
    processes=[procs.azh_htt_zll_a1150_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1150, MH: 950
cpn.add_dataset(
    name="azh_htt_zll_a1150_h950_amcatnlo",
    id=15110542,
    processes=[procs.azh_htt_zll_a1150_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1200, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1200_h1000_amcatnlo",
    id=15109646,
    processes=[procs.azh_htt_zll_a1200_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 1050
cpn.add_dataset(
    name="azh_htt_zll_a1200_h1050_amcatnlo",
    id=15110271,
    processes=[procs.azh_htt_zll_a1200_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1200_h1100_amcatnlo",
    id=15111932,
    processes=[procs.azh_htt_zll_a1200_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1200, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1200_h330_amcatnlo",
    id=15109520,
    processes=[procs.azh_htt_zll_a1200_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1200, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1200_h350_amcatnlo",
    id=15109751,
    processes=[procs.azh_htt_zll_a1200_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1200, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1200_h400_amcatnlo",
    id=15111399,
    processes=[procs.azh_htt_zll_a1200_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1200, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1200_h450_amcatnlo",
    id=15110620,
    processes=[procs.azh_htt_zll_a1200_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1200, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1200_h500_amcatnlo",
    id=15110634,
    processes=[procs.azh_htt_zll_a1200_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1200_h550_amcatnlo",
    id=15110760,
    processes=[procs.azh_htt_zll_a1200_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1200_h600_amcatnlo",
    id=15111359,
    processes=[procs.azh_htt_zll_a1200_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1200, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1200_h650_amcatnlo",
    id=15109440,
    processes=[procs.azh_htt_zll_a1200_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1200_h700_amcatnlo",
    id=15111848,
    processes=[procs.azh_htt_zll_a1200_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1200_h750_amcatnlo",
    id=15111620,
    processes=[procs.azh_htt_zll_a1200_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1200, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1200_h800_amcatnlo",
    id=15110414,
    processes=[procs.azh_htt_zll_a1200_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1200, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1200_h850_amcatnlo",
    id=15104974,
    processes=[procs.azh_htt_zll_a1200_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 1200, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1200_h900_amcatnlo",
    id=15110102,
    processes=[procs.azh_htt_zll_a1200_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1200, MH: 950
cpn.add_dataset(
    name="azh_htt_zll_a1200_h950_amcatnlo",
    id=15109934,
    processes=[procs.azh_htt_zll_a1200_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1250, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1250_h1000_amcatnlo",
    id=15111827,
    processes=[procs.azh_htt_zll_a1250_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 1050
cpn.add_dataset(
    name="azh_htt_zll_a1250_h1050_amcatnlo",
    id=15110444,
    processes=[procs.azh_htt_zll_a1250_h1050],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1050_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1250_h1100_amcatnlo",
    id=15111055,
    processes=[procs.azh_htt_zll_a1250_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1250, MH: 1150
cpn.add_dataset(
    name="azh_htt_zll_a1250_h1150_amcatnlo",
    id=15109419,
    processes=[procs.azh_htt_zll_a1250_h1150],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-1150_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a1250_h330_amcatnlo",
    id=15110171,
    processes=[procs.azh_htt_zll_a1250_h330],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1250, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1250_h350_amcatnlo",
    id=15110710,
    processes=[procs.azh_htt_zll_a1250_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1250_h400_amcatnlo",
    id=15110062,
    processes=[procs.azh_htt_zll_a1250_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a1250_h450_amcatnlo",
    id=15110565,
    processes=[procs.azh_htt_zll_a1250_h450],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1250_h500_amcatnlo",
    id=15111707,
    processes=[procs.azh_htt_zll_a1250_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a1250_h550_amcatnlo",
    id=15109203,
    processes=[procs.azh_htt_zll_a1250_h550],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1250_h600_amcatnlo",
    id=15104328,
    processes=[procs.azh_htt_zll_a1250_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a1250_h650_amcatnlo",
    id=15109820,
    processes=[procs.azh_htt_zll_a1250_h650],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1250, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1250_h700_amcatnlo",
    id=15109486,
    processes=[procs.azh_htt_zll_a1250_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a1250_h750_amcatnlo",
    id=15111822,
    processes=[procs.azh_htt_zll_a1250_h750],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1250, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1250_h800_amcatnlo",
    id=15109712,
    processes=[procs.azh_htt_zll_a1250_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1250, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a1250_h850_amcatnlo",
    id=15109973,
    processes=[procs.azh_htt_zll_a1250_h850],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1250, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1250_h900_amcatnlo",
    id=15109174,
    processes=[procs.azh_htt_zll_a1250_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1250, MH: 950
cpn.add_dataset(
    name="azh_htt_zll_a1250_h950_amcatnlo",
    id=15111153,
    processes=[procs.azh_htt_zll_a1250_h950],
    keys=[
        "/AToZHToLLTTbar_MA-1250_MH-950_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1300, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1300_h1000_amcatnlo",
    id=15111470,
    processes=[procs.azh_htt_zll_a1300_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1300, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1300_h1100_amcatnlo",
    id=15110388,
    processes=[procs.azh_htt_zll_a1300_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1300, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1300_h1200_amcatnlo",
    id=15110045,
    processes=[procs.azh_htt_zll_a1300_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1300, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1300_h350_amcatnlo",
    id=15109236,
    processes=[procs.azh_htt_zll_a1300_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1300, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1300_h400_amcatnlo",
    id=15110640,
    processes=[procs.azh_htt_zll_a1300_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1300, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1300_h500_amcatnlo",
    id=15111522,
    processes=[procs.azh_htt_zll_a1300_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1300, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1300_h600_amcatnlo",
    id=15110006,
    processes=[procs.azh_htt_zll_a1300_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1300, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1300_h700_amcatnlo",
    id=15111406,
    processes=[procs.azh_htt_zll_a1300_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1300, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1300_h800_amcatnlo",
    id=15110739,
    processes=[procs.azh_htt_zll_a1300_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1300, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1300_h900_amcatnlo",
    id=15111865,
    processes=[procs.azh_htt_zll_a1300_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1400, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1400_h1000_amcatnlo",
    id=15104694,
    processes=[procs.azh_htt_zll_a1400_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1400, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1400_h1100_amcatnlo",
    id=15110873,
    processes=[procs.azh_htt_zll_a1400_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1400, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1400_h1200_amcatnlo",
    id=15109434,
    processes=[procs.azh_htt_zll_a1400_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1400, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1400_h1300_amcatnlo",
    id=15110175,
    processes=[procs.azh_htt_zll_a1400_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1400, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1400_h350_amcatnlo",
    id=15111645,
    processes=[procs.azh_htt_zll_a1400_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1400, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1400_h400_amcatnlo",
    id=15104566,
    processes=[procs.azh_htt_zll_a1400_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 1400, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1400_h500_amcatnlo",
    id=15103902,
    processes=[procs.azh_htt_zll_a1400_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=11500,
)

# MA 1400, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1400_h600_amcatnlo",
    id=15109408,
    processes=[procs.azh_htt_zll_a1400_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1400, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1400_h700_amcatnlo",
    id=15109888,
    processes=[procs.azh_htt_zll_a1400_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1400, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1400_h800_amcatnlo",
    id=15109531,
    processes=[procs.azh_htt_zll_a1400_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 1400, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1400_h900_amcatnlo",
    id=15111213,
    processes=[procs.azh_htt_zll_a1400_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1500, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1500_h1000_amcatnlo",
    id=15109729,
    processes=[procs.azh_htt_zll_a1500_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1500, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1500_h1100_amcatnlo",
    id=15109900,
    processes=[procs.azh_htt_zll_a1500_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1500, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1500_h1200_amcatnlo",
    id=15109995,
    processes=[procs.azh_htt_zll_a1500_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1500, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1500_h1300_amcatnlo",
    id=15111516,
    processes=[procs.azh_htt_zll_a1500_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1500, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a1500_h1400_amcatnlo",
    id=15104493,
    processes=[procs.azh_htt_zll_a1500_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1500, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1500_h350_amcatnlo",
    id=15109625,
    processes=[procs.azh_htt_zll_a1500_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1500, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1500_h400_amcatnlo",
    id=15109577,
    processes=[procs.azh_htt_zll_a1500_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1500, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1500_h500_amcatnlo",
    id=15110586,
    processes=[procs.azh_htt_zll_a1500_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1500, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1500_h600_amcatnlo",
    id=15104397,
    processes=[procs.azh_htt_zll_a1500_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1500, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1500_h700_amcatnlo",
    id=15111328,
    processes=[procs.azh_htt_zll_a1500_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1500, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1500_h800_amcatnlo",
    id=15109594,
    processes=[procs.azh_htt_zll_a1500_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1500, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1500_h900_amcatnlo",
    id=15111617,
    processes=[procs.azh_htt_zll_a1500_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1600, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1000_amcatnlo",
    id=15104578,
    processes=[procs.azh_htt_zll_a1600_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 1600, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1100_amcatnlo",
    id=15110476,
    processes=[procs.azh_htt_zll_a1600_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1600, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1200_amcatnlo",
    id=15111615,
    processes=[procs.azh_htt_zll_a1600_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1600, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1300_amcatnlo",
    id=15103978,
    processes=[procs.azh_htt_zll_a1600_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 1600, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1400_amcatnlo",
    id=15110383,
    processes=[procs.azh_htt_zll_a1600_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1600, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a1600_h1500_amcatnlo",
    id=15109613,
    processes=[procs.azh_htt_zll_a1600_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1600, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1600_h350_amcatnlo",
    id=15103981,
    processes=[procs.azh_htt_zll_a1600_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1600, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1600_h400_amcatnlo",
    id=15109971,
    processes=[procs.azh_htt_zll_a1600_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1600, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1600_h500_amcatnlo",
    id=15111172,
    processes=[procs.azh_htt_zll_a1600_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1600, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1600_h600_amcatnlo",
    id=15110991,
    processes=[procs.azh_htt_zll_a1600_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1600, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1600_h700_amcatnlo",
    id=15110866,
    processes=[procs.azh_htt_zll_a1600_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1600, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1600_h800_amcatnlo",
    id=15111096,
    processes=[procs.azh_htt_zll_a1600_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1600, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1600_h900_amcatnlo",
    id=15111136,
    processes=[procs.azh_htt_zll_a1600_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1700, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1000_amcatnlo",
    id=15111784,
    processes=[procs.azh_htt_zll_a1700_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1700, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1100_amcatnlo",
    id=15109609,
    processes=[procs.azh_htt_zll_a1700_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1700, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1200_amcatnlo",
    id=15111074,
    processes=[procs.azh_htt_zll_a1700_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1700, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1300_amcatnlo",
    id=15110683,
    processes=[procs.azh_htt_zll_a1700_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1700, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1400_amcatnlo",
    id=15111833,
    processes=[procs.azh_htt_zll_a1700_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1700, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1500_amcatnlo",
    id=15110783,
    processes=[procs.azh_htt_zll_a1700_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1700, MH: 1600
cpn.add_dataset(
    name="azh_htt_zll_a1700_h1600_amcatnlo",
    id=15110910,
    processes=[procs.azh_htt_zll_a1700_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1700, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1700_h350_amcatnlo",
    id=15104409,
    processes=[procs.azh_htt_zll_a1700_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 1700, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1700_h400_amcatnlo",
    id=15111420,
    processes=[procs.azh_htt_zll_a1700_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1700, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1700_h500_amcatnlo",
    id=15110128,
    processes=[procs.azh_htt_zll_a1700_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1700, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1700_h600_amcatnlo",
    id=15109539,
    processes=[procs.azh_htt_zll_a1700_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1700, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1700_h700_amcatnlo",
    id=15110658,
    processes=[procs.azh_htt_zll_a1700_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1700, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1700_h800_amcatnlo",
    id=15111300,
    processes=[procs.azh_htt_zll_a1700_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1700, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1700_h900_amcatnlo",
    id=15110016,
    processes=[procs.azh_htt_zll_a1700_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1800, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1000_amcatnlo",
    id=15109201,
    processes=[procs.azh_htt_zll_a1800_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1800, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1100_amcatnlo",
    id=15109727,
    processes=[procs.azh_htt_zll_a1800_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1800, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1200_amcatnlo",
    id=15110215,
    processes=[procs.azh_htt_zll_a1800_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1800, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1300_amcatnlo",
    id=15109664,
    processes=[procs.azh_htt_zll_a1800_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1800, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1400_amcatnlo",
    id=15110774,
    processes=[procs.azh_htt_zll_a1800_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1800, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1500_amcatnlo",
    id=15110106,
    processes=[procs.azh_htt_zll_a1800_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1800, MH: 1600
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1600_amcatnlo",
    id=15109656,
    processes=[procs.azh_htt_zll_a1800_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1800, MH: 1700
cpn.add_dataset(
    name="azh_htt_zll_a1800_h1700_amcatnlo",
    id=15112002,
    processes=[procs.azh_htt_zll_a1800_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1800, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1800_h350_amcatnlo",
    id=15111257,
    processes=[procs.azh_htt_zll_a1800_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1800, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1800_h400_amcatnlo",
    id=15111489,
    processes=[procs.azh_htt_zll_a1800_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1800, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1800_h500_amcatnlo",
    id=15111372,
    processes=[procs.azh_htt_zll_a1800_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1800, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1800_h600_amcatnlo",
    id=15103985,
    processes=[procs.azh_htt_zll_a1800_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1800, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1800_h700_amcatnlo",
    id=15111818,
    processes=[procs.azh_htt_zll_a1800_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1800, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1800_h800_amcatnlo",
    id=15109280,
    processes=[procs.azh_htt_zll_a1800_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1800, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1800_h900_amcatnlo",
    id=15111990,
    processes=[procs.azh_htt_zll_a1800_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 1900, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1000_amcatnlo",
    id=15103987,
    processes=[procs.azh_htt_zll_a1900_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1900, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1100_amcatnlo",
    id=15111376,
    processes=[procs.azh_htt_zll_a1900_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1900, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1200_amcatnlo",
    id=15110220,
    processes=[procs.azh_htt_zll_a1900_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1900, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1300_amcatnlo",
    id=15111432,
    processes=[procs.azh_htt_zll_a1900_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1900, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1400_amcatnlo",
    id=15111895,
    processes=[procs.azh_htt_zll_a1900_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1900, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1500_amcatnlo",
    id=15104733,
    processes=[procs.azh_htt_zll_a1900_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 1900, MH: 1600
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1600_amcatnlo",
    id=15109497,
    processes=[procs.azh_htt_zll_a1900_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1900, MH: 1700
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1700_amcatnlo",
    id=15109550,
    processes=[procs.azh_htt_zll_a1900_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1900, MH: 1800
cpn.add_dataset(
    name="azh_htt_zll_a1900_h1800_amcatnlo",
    id=15111133,
    processes=[procs.azh_htt_zll_a1900_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1900, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a1900_h350_amcatnlo",
    id=15111151,
    processes=[procs.azh_htt_zll_a1900_h350],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 1900, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a1900_h400_amcatnlo",
    id=15113436,
    processes=[procs.azh_htt_zll_a1900_h400],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 1900, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a1900_h500_amcatnlo",
    id=15110793,
    processes=[procs.azh_htt_zll_a1900_h500],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 1900, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a1900_h600_amcatnlo",
    id=15110625,
    processes=[procs.azh_htt_zll_a1900_h600],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 1900, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a1900_h700_amcatnlo",
    id=15110270,
    processes=[procs.azh_htt_zll_a1900_h700],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 1900, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a1900_h800_amcatnlo",
    id=15111077,
    processes=[procs.azh_htt_zll_a1900_h800],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 1900, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a1900_h900_amcatnlo",
    id=15110888,
    processes=[procs.azh_htt_zll_a1900_h900],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2000, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1000_amcatnlo",
    id=15111742,
    processes=[procs.azh_htt_zll_a2000_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2000, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1100_amcatnlo",
    id=15110177,
    processes=[procs.azh_htt_zll_a2000_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2000, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1200_amcatnlo",
    id=15109793,
    processes=[procs.azh_htt_zll_a2000_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=11500,
)

# MA 2000, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1300_amcatnlo",
    id=15111240,
    processes=[procs.azh_htt_zll_a2000_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 2000, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1400_amcatnlo",
    id=15111864,
    processes=[procs.azh_htt_zll_a2000_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2000, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1500_amcatnlo",
    id=15110258,
    processes=[procs.azh_htt_zll_a2000_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2000, MH: 1600
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1600_amcatnlo",
    id=15111972,
    processes=[procs.azh_htt_zll_a2000_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2000, MH: 1700
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1700_amcatnlo",
    id=15109905,
    processes=[procs.azh_htt_zll_a2000_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 2000, MH: 1800
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1800_amcatnlo",
    id=15104110,
    processes=[procs.azh_htt_zll_a2000_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 2000, MH: 1900
cpn.add_dataset(
    name="azh_htt_zll_a2000_h1900_amcatnlo",
    id=15111000,
    processes=[procs.azh_htt_zll_a2000_h1900],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 2000, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a2000_h350_amcatnlo",
    id=15110558,
    processes=[procs.azh_htt_zll_a2000_h350],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2000, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a2000_h400_amcatnlo",
    id=15111169,
    processes=[procs.azh_htt_zll_a2000_h400],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 2000, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a2000_h500_amcatnlo",
    id=15110436,
    processes=[procs.azh_htt_zll_a2000_h500],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2000, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a2000_h600_amcatnlo",
    id=15111215,
    processes=[procs.azh_htt_zll_a2000_h600],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 2000, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a2000_h700_amcatnlo",
    id=15111633,
    processes=[procs.azh_htt_zll_a2000_h700],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2000, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a2000_h800_amcatnlo",
    id=15110784,
    processes=[procs.azh_htt_zll_a2000_h800],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2000, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a2000_h900_amcatnlo",
    id=15104314,
    processes=[procs.azh_htt_zll_a2000_h900],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2100, MH: 1000
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1000_amcatnlo",
    id=15110927,
    processes=[procs.azh_htt_zll_a2100_h1000],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2100, MH: 1100
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1100_amcatnlo",
    id=15109931,
    processes=[procs.azh_htt_zll_a2100_h1100],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1100_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2100, MH: 1200
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1200_amcatnlo",
    id=15111536,
    processes=[procs.azh_htt_zll_a2100_h1200],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1200_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 2100, MH: 1300
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1300_amcatnlo",
    id=15126018,
    processes=[procs.azh_htt_zll_a2100_h1300],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1300_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=11500,
)

# MA 2100, MH: 1400
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1400_amcatnlo",
    id=15104502,
    processes=[procs.azh_htt_zll_a2100_h1400],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 2100, MH: 1500
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1500_amcatnlo",
    id=15111867,
    processes=[procs.azh_htt_zll_a2100_h1500],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2100, MH: 1600
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1600_amcatnlo",
    id=15110225,
    processes=[procs.azh_htt_zll_a2100_h1600],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2100, MH: 1700
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1700_amcatnlo",
    id=15110221,
    processes=[procs.azh_htt_zll_a2100_h1700],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2100, MH: 1800
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1800_amcatnlo",
    id=15111191,
    processes=[procs.azh_htt_zll_a2100_h1800],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2100, MH: 1900
cpn.add_dataset(
    name="azh_htt_zll_a2100_h1900_amcatnlo",
    id=15110830,
    processes=[procs.azh_htt_zll_a2100_h1900],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2100, MH: 2000
cpn.add_dataset(
    name="azh_htt_zll_a2100_h2000_amcatnlo",
    id=15111519,
    processes=[procs.azh_htt_zll_a2100_h2000],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 2100, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a2100_h350_amcatnlo",
    id=15103904,
    processes=[procs.azh_htt_zll_a2100_h350],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 2100, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a2100_h400_amcatnlo",
    id=15111844,
    processes=[procs.azh_htt_zll_a2100_h400],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 2100, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a2100_h500_amcatnlo",
    id=15111218,
    processes=[procs.azh_htt_zll_a2100_h500],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 2100, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a2100_h600_amcatnlo",
    id=15104316,
    processes=[procs.azh_htt_zll_a2100_h600],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 2100, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a2100_h700_amcatnlo",
    id=15111067,
    processes=[procs.azh_htt_zll_a2100_h700],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 2100, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a2100_h800_amcatnlo",
    id=15111871,
    processes=[procs.azh_htt_zll_a2100_h800],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 2100, MH: 900
cpn.add_dataset(
    name="azh_htt_zll_a2100_h900_amcatnlo",
    id=15111788,
    processes=[procs.azh_htt_zll_a2100_h900],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-900_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 430, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a430_h330_amcatnlo",
    id=15104176,
    processes=[procs.azh_htt_zll_a430_h330],
    keys=[
        "/AToZHToLLTTbar_MA-430_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 450, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a450_h330_amcatnlo",
    id=15111843,
    processes=[procs.azh_htt_zll_a450_h330],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 450, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a450_h350_amcatnlo",
    id=15109772,
    processes=[procs.azh_htt_zll_a450_h350],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 500, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a500_h330_amcatnlo",
    id=15110023,
    processes=[procs.azh_htt_zll_a500_h330],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 500, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a500_h350_amcatnlo",
    id=15109573,
    processes=[procs.azh_htt_zll_a500_h350],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 500, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a500_h400_amcatnlo",
    id=15110534,
    processes=[procs.azh_htt_zll_a500_h400],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 550, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a550_h330_amcatnlo",
    id=15111178,
    processes=[procs.azh_htt_zll_a550_h330],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 550, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a550_h350_amcatnlo",
    id=15109724,
    processes=[procs.azh_htt_zll_a550_h350],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 550, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a550_h400_amcatnlo",
    id=15110638,
    processes=[procs.azh_htt_zll_a550_h400],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 550, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a550_h450_amcatnlo",
    id=15109685,
    processes=[procs.azh_htt_zll_a550_h450],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 600, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a600_h330_amcatnlo",
    id=15111592,
    processes=[procs.azh_htt_zll_a600_h330],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 600, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a600_h350_amcatnlo",
    id=15109441,
    processes=[procs.azh_htt_zll_a600_h350],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 600, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a600_h400_amcatnlo",
    id=15110209,
    processes=[procs.azh_htt_zll_a600_h400],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 600, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a600_h450_amcatnlo",
    id=15111739,
    processes=[procs.azh_htt_zll_a600_h450],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 600, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a600_h500_amcatnlo",
    id=15109138,
    processes=[procs.azh_htt_zll_a600_h500],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 650, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a650_h330_amcatnlo",
    id=15111756,
    processes=[procs.azh_htt_zll_a650_h330],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 650, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a650_h350_amcatnlo",
    id=15110420,
    processes=[procs.azh_htt_zll_a650_h350],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 650, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a650_h400_amcatnlo",
    id=15104039,
    processes=[procs.azh_htt_zll_a650_h400],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 650, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a650_h450_amcatnlo",
    id=15109298,
    processes=[procs.azh_htt_zll_a650_h450],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 650, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a650_h500_amcatnlo",
    id=15109316,
    processes=[procs.azh_htt_zll_a650_h500],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 650, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a650_h550_amcatnlo",
    id=15103962,
    processes=[procs.azh_htt_zll_a650_h550],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 700, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a700_h330_amcatnlo",
    id=15110687,
    processes=[procs.azh_htt_zll_a700_h330],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 700, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a700_h350_amcatnlo",
    id=15110085,
    processes=[procs.azh_htt_zll_a700_h350],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 700, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a700_h400_amcatnlo",
    id=15111157,
    processes=[procs.azh_htt_zll_a700_h400],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 700, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a700_h450_amcatnlo",
    id=15110904,
    processes=[procs.azh_htt_zll_a700_h450],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 700, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a700_h500_amcatnlo",
    id=15110411,
    processes=[procs.azh_htt_zll_a700_h500],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 700, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a700_h550_amcatnlo",
    id=15110771,
    processes=[procs.azh_htt_zll_a700_h550],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 700, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a700_h600_amcatnlo",
    id=15109787,
    processes=[procs.azh_htt_zll_a700_h600],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 750, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a750_h330_amcatnlo",
    id=15111245,
    processes=[procs.azh_htt_zll_a750_h330],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 750, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a750_h350_amcatnlo",
    id=15111206,
    processes=[procs.azh_htt_zll_a750_h350],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 750, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a750_h400_amcatnlo",
    id=15110325,
    processes=[procs.azh_htt_zll_a750_h400],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 750, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a750_h450_amcatnlo",
    id=15111718,
    processes=[procs.azh_htt_zll_a750_h450],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 750, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a750_h500_amcatnlo",
    id=15110091,
    processes=[procs.azh_htt_zll_a750_h500],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 750, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a750_h550_amcatnlo",
    id=15111224,
    processes=[procs.azh_htt_zll_a750_h550],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 750, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a750_h600_amcatnlo",
    id=15104179,
    processes=[procs.azh_htt_zll_a750_h600],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 750, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a750_h650_amcatnlo",
    id=15110610,
    processes=[procs.azh_htt_zll_a750_h650],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 800, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a800_h330_amcatnlo",
    id=15111967,
    processes=[procs.azh_htt_zll_a800_h330],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 800, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a800_h350_amcatnlo",
    id=15110720,
    processes=[procs.azh_htt_zll_a800_h350],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 800, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a800_h400_amcatnlo",
    id=15110794,
    processes=[procs.azh_htt_zll_a800_h400],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 800, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a800_h450_amcatnlo",
    id=15110956,
    processes=[procs.azh_htt_zll_a800_h450],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=11500,
)

# MA 800, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a800_h500_amcatnlo",
    id=15110583,
    processes=[procs.azh_htt_zll_a800_h500],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 800, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a800_h550_amcatnlo",
    id=15110606,
    processes=[procs.azh_htt_zll_a800_h550],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 800, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a800_h600_amcatnlo",
    id=15110887,
    processes=[procs.azh_htt_zll_a800_h600],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 800, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a800_h650_amcatnlo",
    id=15110363,
    processes=[procs.azh_htt_zll_a800_h650],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 800, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a800_h700_amcatnlo",
    id=15110004,
    processes=[procs.azh_htt_zll_a800_h700],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 850, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a850_h330_amcatnlo",
    id=15110999,
    processes=[procs.azh_htt_zll_a850_h330],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 850, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a850_h350_amcatnlo",
    id=15110918,
    processes=[procs.azh_htt_zll_a850_h350],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 850, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a850_h400_amcatnlo",
    id=15110921,
    processes=[procs.azh_htt_zll_a850_h400],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 850, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a850_h450_amcatnlo",
    id=15110230,
    processes=[procs.azh_htt_zll_a850_h450],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 850, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a850_h500_amcatnlo",
    id=15109415,
    processes=[procs.azh_htt_zll_a850_h500],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 850, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a850_h550_amcatnlo",
    id=15110895,
    processes=[procs.azh_htt_zll_a850_h550],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 850, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a850_h600_amcatnlo",
    id=15111126,
    processes=[procs.azh_htt_zll_a850_h600],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=11500,
)

# MA 850, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a850_h650_amcatnlo",
    id=15111080,
    processes=[procs.azh_htt_zll_a850_h650],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 850, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a850_h700_amcatnlo",
    id=15111038,
    processes=[procs.azh_htt_zll_a850_h700],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 850, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a850_h750_amcatnlo",
    id=15110136,
    processes=[procs.azh_htt_zll_a850_h750],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=11500,
)

# MA 900, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a900_h330_amcatnlo",
    id=15110236,
    processes=[procs.azh_htt_zll_a900_h330],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 900, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a900_h350_amcatnlo",
    id=15110513,
    processes=[procs.azh_htt_zll_a900_h350],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 900, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a900_h400_amcatnlo",
    id=15110979,
    processes=[procs.azh_htt_zll_a900_h400],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=11500,
)

# MA 900, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a900_h450_amcatnlo",
    id=15110352,
    processes=[procs.azh_htt_zll_a900_h450],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 900, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a900_h500_amcatnlo",
    id=15110732,
    processes=[procs.azh_htt_zll_a900_h500],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 900, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a900_h550_amcatnlo",
    id=15110777,
    processes=[procs.azh_htt_zll_a900_h550],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 900, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a900_h600_amcatnlo",
    id=15110168,
    processes=[procs.azh_htt_zll_a900_h600],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 900, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a900_h650_amcatnlo",
    id=15111729,
    processes=[procs.azh_htt_zll_a900_h650],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=11500,
)

# MA 900, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a900_h700_amcatnlo",
    id=15111681,
    processes=[procs.azh_htt_zll_a900_h700],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 900, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a900_h750_amcatnlo",
    id=15109312,
    processes=[procs.azh_htt_zll_a900_h750],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 900, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a900_h800_amcatnlo",
    id=15109549,
    processes=[procs.azh_htt_zll_a900_h800],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 330
cpn.add_dataset(
    name="azh_htt_zll_a950_h330_amcatnlo",
    id=15111878,
    processes=[procs.azh_htt_zll_a950_h330],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-330_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=11500,
)

# MA 950, MH: 350
cpn.add_dataset(
    name="azh_htt_zll_a950_h350_amcatnlo",
    id=15111460,
    processes=[procs.azh_htt_zll_a950_h350],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-350_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=11500,
)

# MA 950, MH: 400
cpn.add_dataset(
    name="azh_htt_zll_a950_h400_amcatnlo",
    id=15109901,
    processes=[procs.azh_htt_zll_a950_h400],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-400_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 450
cpn.add_dataset(
    name="azh_htt_zll_a950_h450_amcatnlo",
    id=15111483,
    processes=[procs.azh_htt_zll_a950_h450],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-450_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 950, MH: 500
cpn.add_dataset(
    name="azh_htt_zll_a950_h500_amcatnlo",
    id=15110298,
    processes=[procs.azh_htt_zll_a950_h500],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-500_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 950, MH: 550
cpn.add_dataset(
    name="azh_htt_zll_a950_h550_amcatnlo",
    id=15111860,
    processes=[procs.azh_htt_zll_a950_h550],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-550_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 600
cpn.add_dataset(
    name="azh_htt_zll_a950_h600_amcatnlo",
    id=15109869,
    processes=[procs.azh_htt_zll_a950_h600],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-600_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 650
cpn.add_dataset(
    name="azh_htt_zll_a950_h650_amcatnlo",
    id=15103907,
    processes=[procs.azh_htt_zll_a950_h650],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-650_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=11500,
)

# MA 950, MH: 700
cpn.add_dataset(
    name="azh_htt_zll_a950_h700_amcatnlo",
    id=15104044,
    processes=[procs.azh_htt_zll_a950_h700],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-700_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=11500,
)

# MA 950, MH: 750
cpn.add_dataset(
    name="azh_htt_zll_a950_h750_amcatnlo",
    id=15109958,
    processes=[procs.azh_htt_zll_a950_h750],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-750_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 800
cpn.add_dataset(
    name="azh_htt_zll_a950_h800_amcatnlo",
    id=15109761,
    processes=[procs.azh_htt_zll_a950_h800],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-800_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)

# MA 950, MH: 850
cpn.add_dataset(
    name="azh_htt_zll_a950_h850_amcatnlo",
    id=15111208,
    processes=[procs.azh_htt_zll_a950_h850],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-850_TuneCP5_13p6TeV-amcatnlo-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=11500,
)
