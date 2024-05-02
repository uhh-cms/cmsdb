# coding: utf-8

"""
A->ZH->Ztt datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# AZH->Ztt->lltt
#

cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-330",
    id=14640747,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-350",
    id=14640749,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-400",
    id=14644922,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-450",
    id=14644445,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-500",
    id=14644631,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-550",
    id=14637796,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-600",
    id=14548924,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-650",
    id=14643976,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-700",
    id=14536925,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-750",
    id=14636760,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-800",
    id=14548527,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-850",
    id=14644480,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1000_MH-900",
    id=14641365,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-330",
    id=14644650,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-350",
    id=14636601,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-400",
    id=14637383,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-450",
    id=14643202,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-500",
    id=14645580,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-550",
    id=14637742,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-600",
    id=14637456,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-700",
    id=14638692,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-750",
    id=14637603,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-800",
    id=14639246,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-850",
    id=14641223,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-900",
    id=14645437,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1050_MH-950",
    id=14644029,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-1000",
    id=14638003,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-330",
    id=14643995,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-350",
    id=14643757,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-400",
    id=14644862,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-450",
    id=14641209,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-500",
    id=14643951,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-550",
    id=14640899,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-600",
    id=14640946,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-650",
    id=14640680,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-700",
    id=14645549,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-750",
    id=14637895,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-800",
    id=14636438,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-850",
    id=14643264,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-900",
    id=14641361,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1100_MH-950",
    id=14641067,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-1050",
    id=14637047,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1050_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-330",
    id=14645065,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-350",
    id=14641502,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-450",
    id=14638090,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-550",
    id=14645380,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-650",
    id=14637436,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-750",
    id=14644493,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-850",
    id=14645060,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1150_MH-950",
    id=14644915,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-1000",
    id=14543193,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-1100",
    id=14644025,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-330",
    id=14637970,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-350",
    id=14644005,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-400",
    id=14647612,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-500",
    id=14644884,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-600",
    id=14644415,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-700",
    id=14641569,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-800",
    id=14639844,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-850",
    id=14549534,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1200_MH-900",
    id=14641099,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-1000",
    id=14640819,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-1100",
    id=14641489,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-1200",
    id=14644883,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-350",
    id=14645154,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-400",
    id=14639378,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-500",
    id=14640835,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-600",
    id=14645563,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-700",
    id=14637957,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-800",
    id=14644759,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1300_MH-900",
    id=14636843,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-1000",
    id=14641266,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-1100",
    id=14643808,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-1200",
    id=14645021,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-1300",
    id=14640339,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-350",
    id=14636494,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-400",
    id=14644419,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-500",
    id=14640681,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-600",
    id=14643451,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-700",
    id=14641327,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-800",
    id=14644989,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1400_MH-900",
    id=14645622,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-1000",
    id=14647495,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-1100",
    id=14641077,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-1200",
    id=14644354,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-1300",
    id=14638120,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-1400",
    id=14647514,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-350",
    id=14645022,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-400",
    id=14548215,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-500",
    id=14641173,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-600",
    id=14637940,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-700",
    id=14640888,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1500_MH-900",
    id=14643452,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1000",
    id=14641468,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1100",
    id=14637407,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1200",
    id=14638121,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1300",
    id=14641294,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1400",
    id=14636598,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-1500",
    id=14641495,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-350",
    id=14637598,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-400",
    id=14644182,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-500",
    id=14641368,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-600",
    id=14644439,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1600_MH-900",
    id=14640009,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1000",
    id=14640900,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1100",
    id=14645008,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1200",
    id=14644904,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1300",
    id=14636430,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1400",
    id=14636571,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1500",
    id=14638199,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-1600",
    id=14641481,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-350",
    id=14645023,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-400",
    id=14645452,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-500",
    id=14636536,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-600",
    id=14644424,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-700",
    id=14636781,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-800",
    id=14644001,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1700_MH-900",
    id=14637536,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1000",
    id=14636446,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1100",
    id=14645028,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1200",
    id=14644991,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1300",
    id=14643136,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1400",
    id=14644377,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1500",
    id=14641545,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1600",
    id=14536346,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-1700",
    id=14638264,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-350",
    id=14645239,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-400",
    id=14647680,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-500",
    id=14636041,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-600",
    id=14638191,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-700",
    id=14641337,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-800",
    id=14641404,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1800_MH-900",
    id=14644425,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1000",
    id=14645483,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1100",
    id=14641381,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1200",
    id=14644032,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1300",
    id=14640668,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1400",
    id=14638513,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1500",
    id=14641448,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1600",
    id=14644761,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1700",
    id=14644521,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-1800",
    id=14639947,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-350",
    id=14645606,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-400",
    id=14640620,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-500",
    id=14644122,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-600",
    id=14638778,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-700",
    id=14643966,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-800",
    id=14644992,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-1900_MH-900",
    id=14636485,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1000",
    id=14640348,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1100",
    id=14644809,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1200",
    id=14637610,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1300",
    id=14636407,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1400",
    id=14641386,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1600",
    id=14636572,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1700",
    id=14645641,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1800",
    id=14638745,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-1900",
    id=14640887,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-350",
    id=14645372,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-400",
    id=14640824,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-500",
    id=14641466,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-600",
    id=14644380,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-700",
    id=14641216,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-800",
    id=14636495,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2000_MH-900",
    id=14643988,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1000",
    id=14536369,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1100",
    id=14637855,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1200",
    id=14640710,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1300",
    id=14636479,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1400",
    id=14637248,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1500",
    id=14645029,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1700",
    id=14637551,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1800",
    id=14638095,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-1900",
    id=14643999,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-2000",
    id=14536433,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-350",
    id=14640847,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-400",
    id=14549535,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-500",
    id=14641088,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-600",
    id=14645539,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-700",
    id=14636576,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-800",
    id=14644946,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-2100_MH-900",
    id=14641004,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-430_MH-330",
    id=14640871,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-430_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-450_MH-330",
    id=14641217,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-450_MH-350",
    id=14637724,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-500_MH-330",
    id=14645669,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-500_MH-350",
    id=14548216,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-500_MH-370",
    id=14648537,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-500_MH-400",
    id=14537163,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-550_MH-330",
    id=14640737,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-550_MH-350",
    id=14641310,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-550_MH-400",
    id=14641298,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-550_MH-450",
    id=14644728,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-600_MH-330",
    id=14643492,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-600_MH-350",
    id=14644865,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-600_MH-400",
    id=14640637,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-600_MH-450",
    id=14644417,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-600_MH-500",
    id=14641414,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-330",
    id=14644791,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-350",
    id=14636505,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-400",
    id=14643912,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-450",
    id=14641233,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-500",
    id=14637773,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-650_MH-550",
    id=14637782,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-330",
    id=14637877,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-350",
    id=14549119,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-370",
    id=14548653,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-400",
    id=14550258,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-450",
    id=14644343,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-500",
    id=14645288,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-700_MH-550",
    id=14644477,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-330",
    id=14641059,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-350",
    id=14644713,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-400",
    id=14637708,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-450",
    id=14640716,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-500",
    id=14636467,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-550",
    id=14644222,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-600",
    id=14644813,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-750_MH-650",
    id=14644183,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-330",
    id=14643977,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-350",
    id=14638955,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-400",
    id=14643987,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-450",
    id=14637537,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-500",
    id=14636808,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-550",
    id=14640965,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-600",
    id=14548217,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-650",
    id=14647537,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-800_MH-700",
    id=14637545,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-330",
    id=14636408,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-350",
    id=14640072,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-400",
    id=14641161,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-450",
    id=14644205,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-500",
    id=14636506,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-550",
    id=14640940,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-600",
    id=14637903,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-650",
    id=14644591,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-700",
    id=14645081,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-850_MH-750",
    id=14640939,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-330",
    id=14641018,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-350",
    id=14647696,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-370",
    id=14548218,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-400",
    id=14544289,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-450",
    id=14637509,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-550",
    id=14640075,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-500",
    id=14640067,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-600",
    id=14641600,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-650",
    id=14645044,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-700",
    id=14644427,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-750",
    id=14641142,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-900_MH-800",
    id=14636409,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-330",
    id=14636607,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-350",
    id=14638010,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-400",
    id=14638017,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-450",
    id=14642920,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-500",
    id=14637960,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-550",
    id=14641687,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-600",
    id=14637720,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-650",
    id=14637077,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-700",
    id=14636448,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-750",
    id=14644979,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-800",
    id=14645411,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)
cpn.add_dataset(
    name="AToZHToLLTTbar_MA-950_MH-850",
    id=14636342,
    processes=[procs.AToZHToLLTTbar],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

#
# AZH->Ztt->nunutt
#