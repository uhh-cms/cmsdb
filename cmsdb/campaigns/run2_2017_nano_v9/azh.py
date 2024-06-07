# coding: utf-8

"""
A->ZH->Ztt datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# A->ZH->lltt
#

cpn.add_dataset(
    name="azh_htt_zll_a1000_h330_amcatnlo",
    id=14640747,
    processes=[procs.azh_htt_zll_a1000_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h350_amcatnlo",
    id=14640749,
    processes=[procs.azh_htt_zll_a1000_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h400_amcatnlo",
    id=14644922,
    processes=[procs.azh_htt_zll_a1000_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h450_amcatnlo",
    id=14644445,
    processes=[procs.azh_htt_zll_a1000_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h500_amcatnlo",
    id=14644631,
    processes=[procs.azh_htt_zll_a1000_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h550_amcatnlo",
    id=14637796,
    processes=[procs.azh_htt_zll_a1000_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h600_amcatnlo",
    id=14548924,
    processes=[procs.azh_htt_zll_a1000_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h650_amcatnlo",
    id=14643976,
    processes=[procs.azh_htt_zll_a1000_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h700_amcatnlo",
    id=14536925,
    processes=[procs.azh_htt_zll_a1000_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h750_amcatnlo",
    id=14636760,
    processes=[procs.azh_htt_zll_a1000_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h800_amcatnlo",
    id=14548527,
    processes=[procs.azh_htt_zll_a1000_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h850_amcatnlo",
    id=14644480,
    processes=[procs.azh_htt_zll_a1000_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1000_h900_amcatnlo",
    id=14641365,
    processes=[procs.azh_htt_zll_a1000_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1000_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h330_amcatnlo",
    id=14644650,
    processes=[procs.azh_htt_zll_a1050_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h350_amcatnlo",
    id=14636601,
    processes=[procs.azh_htt_zll_a1050_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h400_amcatnlo",
    id=14637383,
    processes=[procs.azh_htt_zll_a1050_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h450_amcatnlo",
    id=14643202,
    processes=[procs.azh_htt_zll_a1050_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h500_amcatnlo",
    id=14645580,
    processes=[procs.azh_htt_zll_a1050_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h550_amcatnlo",
    id=14637742,
    processes=[procs.azh_htt_zll_a1050_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h600_amcatnlo",
    id=14637456,
    processes=[procs.azh_htt_zll_a1050_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h700_amcatnlo",
    id=14638692,
    processes=[procs.azh_htt_zll_a1050_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h750_amcatnlo",
    id=14637603,
    processes=[procs.azh_htt_zll_a1050_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h800_amcatnlo",
    id=14639246,
    processes=[procs.azh_htt_zll_a1050_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h850_amcatnlo",
    id=14641223,
    processes=[procs.azh_htt_zll_a1050_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h900_amcatnlo",
    id=14645437,
    processes=[procs.azh_htt_zll_a1050_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1050_h950_amcatnlo",
    id=14644029,
    processes=[procs.azh_htt_zll_a1050_h950_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1050_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h1000_amcatnlo",
    id=14638003,
    processes=[procs.azh_htt_zll_a1100_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h330_amcatnlo",
    id=14643995,
    processes=[procs.azh_htt_zll_a1100_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h350_amcatnlo",
    id=14643757,
    processes=[procs.azh_htt_zll_a1100_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h400_amcatnlo",
    id=14644862,
    processes=[procs.azh_htt_zll_a1100_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h450_amcatnlo",
    id=14641209,
    processes=[procs.azh_htt_zll_a1100_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h500_amcatnlo",
    id=14643951,
    processes=[procs.azh_htt_zll_a1100_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h550_amcatnlo",
    id=14640899,
    processes=[procs.azh_htt_zll_a1100_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h600_amcatnlo",
    id=14640946,
    processes=[procs.azh_htt_zll_a1100_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h650_amcatnlo",
    id=14640680,
    processes=[procs.azh_htt_zll_a1100_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h700_amcatnlo",
    id=14645549,
    processes=[procs.azh_htt_zll_a1100_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h750_amcatnlo",
    id=14637895,
    processes=[procs.azh_htt_zll_a1100_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h800_amcatnlo",
    id=14636438,
    processes=[procs.azh_htt_zll_a1100_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h850_amcatnlo",
    id=14643264,
    processes=[procs.azh_htt_zll_a1100_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h900_amcatnlo",
    id=14641361,
    processes=[procs.azh_htt_zll_a1100_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1100_h950_amcatnlo",
    id=14641067,
    processes=[procs.azh_htt_zll_a1100_h950_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1100_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h1050_amcatnlo",
    id=14637047,
    processes=[procs.azh_htt_zll_a1150_h1050_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-1050_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h330_amcatnlo",
    id=14645065,
    processes=[procs.azh_htt_zll_a1150_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h350_amcatnlo",
    id=14641502,
    processes=[procs.azh_htt_zll_a1150_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h450_amcatnlo",
    id=14638090,
    processes=[procs.azh_htt_zll_a1150_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h550_amcatnlo",
    id=14645380,
    processes=[procs.azh_htt_zll_a1150_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h650_amcatnlo",
    id=14637436,
    processes=[procs.azh_htt_zll_a1150_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h750_amcatnlo",
    id=14644493,
    processes=[procs.azh_htt_zll_a1150_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h850_amcatnlo",
    id=14645060,
    processes=[procs.azh_htt_zll_a1150_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1150_h950_amcatnlo",
    id=14644915,
    processes=[procs.azh_htt_zll_a1150_h950_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1150_MH-950_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1000_amcatnlo",
    id=14543193,
    processes=[procs.azh_htt_zll_a1200_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h1100_amcatnlo",
    id=14644025,
    processes=[procs.azh_htt_zll_a1200_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h330_amcatnlo",
    id=14637970,
    processes=[procs.azh_htt_zll_a1200_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h350_amcatnlo",
    id=14644005,
    processes=[procs.azh_htt_zll_a1200_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h400_amcatnlo",
    id=14647612,
    processes=[procs.azh_htt_zll_a1200_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h500_amcatnlo",
    id=14644884,
    processes=[procs.azh_htt_zll_a1200_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h600_amcatnlo",
    id=14644415,
    processes=[procs.azh_htt_zll_a1200_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h700_amcatnlo",
    id=14641569,
    processes=[procs.azh_htt_zll_a1200_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h800_amcatnlo",
    id=14639844,
    processes=[procs.azh_htt_zll_a1200_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h850_amcatnlo",
    id=14549534,
    processes=[procs.azh_htt_zll_a1200_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1200_h900_amcatnlo",
    id=14641099,
    processes=[procs.azh_htt_zll_a1200_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1200_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1000_amcatnlo",
    id=14640819,
    processes=[procs.azh_htt_zll_a1300_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1100_amcatnlo",
    id=14641489,
    processes=[procs.azh_htt_zll_a1300_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h1200_amcatnlo",
    id=14644883,
    processes=[procs.azh_htt_zll_a1300_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h350_amcatnlo",
    id=14645154,
    processes=[procs.azh_htt_zll_a1300_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h400_amcatnlo",
    id=14639378,
    processes=[procs.azh_htt_zll_a1300_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h500_amcatnlo",
    id=14640835,
    processes=[procs.azh_htt_zll_a1300_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h600_amcatnlo",
    id=14645563,
    processes=[procs.azh_htt_zll_a1300_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h700_amcatnlo",
    id=14637957,
    processes=[procs.azh_htt_zll_a1300_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h800_amcatnlo",
    id=14644759,
    processes=[procs.azh_htt_zll_a1300_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1300_h900_amcatnlo",
    id=14636843,
    processes=[procs.azh_htt_zll_a1300_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1300_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1000_amcatnlo",
    id=14641266,
    processes=[procs.azh_htt_zll_a1400_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1100_amcatnlo",
    id=14643808,
    processes=[procs.azh_htt_zll_a1400_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1200_amcatnlo",
    id=14645021,
    processes=[procs.azh_htt_zll_a1400_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h1300_amcatnlo",
    id=14640339,
    processes=[procs.azh_htt_zll_a1400_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h350_amcatnlo",
    id=14636494,
    processes=[procs.azh_htt_zll_a1400_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h400_amcatnlo",
    id=14644419,
    processes=[procs.azh_htt_zll_a1400_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h500_amcatnlo",
    id=14640681,
    processes=[procs.azh_htt_zll_a1400_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h600_amcatnlo",
    id=14643451,
    processes=[procs.azh_htt_zll_a1400_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h700_amcatnlo",
    id=14641327,
    processes=[procs.azh_htt_zll_a1400_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h800_amcatnlo",
    id=14644989,
    processes=[procs.azh_htt_zll_a1400_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1400_h900_amcatnlo",
    id=14645622,
    processes=[procs.azh_htt_zll_a1400_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1400_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1000_amcatnlo",
    id=14647495,
    processes=[procs.azh_htt_zll_a1500_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1100_amcatnlo",
    id=14641077,
    processes=[procs.azh_htt_zll_a1500_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1200_amcatnlo",
    id=14644354,
    processes=[procs.azh_htt_zll_a1500_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1300_amcatnlo",
    id=14638120,
    processes=[procs.azh_htt_zll_a1500_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h1400_amcatnlo",
    id=14647514,
    processes=[procs.azh_htt_zll_a1500_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h350_amcatnlo",
    id=14645022,
    processes=[procs.azh_htt_zll_a1500_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h400_amcatnlo",
    id=14548215,
    processes=[procs.azh_htt_zll_a1500_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h500_amcatnlo",
    id=14641173,
    processes=[procs.azh_htt_zll_a1500_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h600_amcatnlo",
    id=14637940,
    processes=[procs.azh_htt_zll_a1500_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h700_amcatnlo",
    id=14640888,
    processes=[procs.azh_htt_zll_a1500_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1500_h900_amcatnlo",
    id=14643452,
    processes=[procs.azh_htt_zll_a1500_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1500_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1000_amcatnlo",
    id=14641468,
    processes=[procs.azh_htt_zll_a1600_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1100_amcatnlo",
    id=14637407,
    processes=[procs.azh_htt_zll_a1600_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1200_amcatnlo",
    id=14638121,
    processes=[procs.azh_htt_zll_a1600_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1300_amcatnlo",
    id=14641294,
    processes=[procs.azh_htt_zll_a1600_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1400_amcatnlo",
    id=14636598,
    processes=[procs.azh_htt_zll_a1600_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h1500_amcatnlo",
    id=14641495,
    processes=[procs.azh_htt_zll_a1600_h1500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h350_amcatnlo",
    id=14637598,
    processes=[procs.azh_htt_zll_a1600_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h400_amcatnlo",
    id=14644182,
    processes=[procs.azh_htt_zll_a1600_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h500_amcatnlo",
    id=14641368,
    processes=[procs.azh_htt_zll_a1600_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h600_amcatnlo",
    id=14644439,
    processes=[procs.azh_htt_zll_a1600_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1600_h900_amcatnlo",
    id=14640009,
    processes=[procs.azh_htt_zll_a1600_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1600_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1000_amcatnlo",
    id=14640900,
    processes=[procs.azh_htt_zll_a1700_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1100_amcatnlo",
    id=14645008,
    processes=[procs.azh_htt_zll_a1700_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1200_amcatnlo",
    id=14644904,
    processes=[procs.azh_htt_zll_a1700_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1300_amcatnlo",
    id=14636430,
    processes=[procs.azh_htt_zll_a1700_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1400_amcatnlo",
    id=14636571,
    processes=[procs.azh_htt_zll_a1700_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1500_amcatnlo",
    id=14638199,
    processes=[procs.azh_htt_zll_a1700_h1500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h1600_amcatnlo",
    id=14641481,
    processes=[procs.azh_htt_zll_a1700_h1600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h350_amcatnlo",
    id=14645023,
    processes=[procs.azh_htt_zll_a1700_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h400_amcatnlo",
    id=14645452,
    processes=[procs.azh_htt_zll_a1700_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h500_amcatnlo",
    id=14636536,
    processes=[procs.azh_htt_zll_a1700_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h600_amcatnlo",
    id=14644424,
    processes=[procs.azh_htt_zll_a1700_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h700_amcatnlo",
    id=14636781,
    processes=[procs.azh_htt_zll_a1700_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h800_amcatnlo",
    id=14644001,
    processes=[procs.azh_htt_zll_a1700_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1700_h900_amcatnlo",
    id=14637536,
    processes=[procs.azh_htt_zll_a1700_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1700_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1000_amcatnlo",
    id=14636446,
    processes=[procs.azh_htt_zll_a1800_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1100_amcatnlo",
    id=14645028,
    processes=[procs.azh_htt_zll_a1800_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1200_amcatnlo",
    id=14644991,
    processes=[procs.azh_htt_zll_a1800_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1300_amcatnlo",
    id=14643136,
    processes=[procs.azh_htt_zll_a1800_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1400_amcatnlo",
    id=14644377,
    processes=[procs.azh_htt_zll_a1800_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1500_amcatnlo",
    id=14641545,
    processes=[procs.azh_htt_zll_a1800_h1500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1600_amcatnlo",
    id=14536346,
    processes=[procs.azh_htt_zll_a1800_h1600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h1700_amcatnlo",
    id=14638264,
    processes=[procs.azh_htt_zll_a1800_h1700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h350_amcatnlo",
    id=14645239,
    processes=[procs.azh_htt_zll_a1800_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h400_amcatnlo",
    id=14647680,
    processes=[procs.azh_htt_zll_a1800_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h500_amcatnlo",
    id=14636041,
    processes=[procs.azh_htt_zll_a1800_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h600_amcatnlo",
    id=14638191,
    processes=[procs.azh_htt_zll_a1800_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h700_amcatnlo",
    id=14641337,
    processes=[procs.azh_htt_zll_a1800_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h800_amcatnlo",
    id=14641404,
    processes=[procs.azh_htt_zll_a1800_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1800_h900_amcatnlo",
    id=14644425,
    processes=[procs.azh_htt_zll_a1800_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1800_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1000_amcatnlo",
    id=14645483,
    processes=[procs.azh_htt_zll_a1900_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1100_amcatnlo",
    id=14641381,
    processes=[procs.azh_htt_zll_a1900_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1200_amcatnlo",
    id=14644032,
    processes=[procs.azh_htt_zll_a1900_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1300_amcatnlo",
    id=14640668,
    processes=[procs.azh_htt_zll_a1900_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1400_amcatnlo",
    id=14638513,
    processes=[procs.azh_htt_zll_a1900_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1500_amcatnlo",
    id=14641448,
    processes=[procs.azh_htt_zll_a1900_h1500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1600_amcatnlo",
    id=14644761,
    processes=[procs.azh_htt_zll_a1900_h1600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1700_amcatnlo",
    id=14644521,
    processes=[procs.azh_htt_zll_a1900_h1700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h1800_amcatnlo",
    id=14639947,
    processes=[procs.azh_htt_zll_a1900_h1800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h350_amcatnlo",
    id=14645606,
    processes=[procs.azh_htt_zll_a1900_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h400_amcatnlo",
    id=14640620,
    processes=[procs.azh_htt_zll_a1900_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h500_amcatnlo",
    id=14644122,
    processes=[procs.azh_htt_zll_a1900_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h600_amcatnlo",
    id=14638778,
    processes=[procs.azh_htt_zll_a1900_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h700_amcatnlo",
    id=14643966,
    processes=[procs.azh_htt_zll_a1900_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h800_amcatnlo",
    id=14644992,
    processes=[procs.azh_htt_zll_a1900_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a1900_h900_amcatnlo",
    id=14636485,
    processes=[procs.azh_htt_zll_a1900_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-1900_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1000_amcatnlo",
    id=14640348,
    processes=[procs.azh_htt_zll_a2000_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1100_amcatnlo",
    id=14644809,
    processes=[procs.azh_htt_zll_a2000_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1200_amcatnlo",
    id=14637610,
    processes=[procs.azh_htt_zll_a2000_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1300_amcatnlo",
    id=14636407,
    processes=[procs.azh_htt_zll_a2000_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1400_amcatnlo",
    id=14641386,
    processes=[procs.azh_htt_zll_a2000_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1600_amcatnlo",
    id=14636572,
    processes=[procs.azh_htt_zll_a2000_h1600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1700_amcatnlo",
    id=14645641,
    processes=[procs.azh_htt_zll_a2000_h1700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1800_amcatnlo",
    id=14638745,
    processes=[procs.azh_htt_zll_a2000_h1800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h1900_amcatnlo",
    id=14640887,
    processes=[procs.azh_htt_zll_a2000_h1900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-1900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h350_amcatnlo",
    id=14645372,
    processes=[procs.azh_htt_zll_a2000_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h400_amcatnlo",
    id=14640824,
    processes=[procs.azh_htt_zll_a2000_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h500_amcatnlo",
    id=14641466,
    processes=[procs.azh_htt_zll_a2000_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h600_amcatnlo",
    id=14644380,
    processes=[procs.azh_htt_zll_a2000_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h700_amcatnlo",
    id=14641216,
    processes=[procs.azh_htt_zll_a2000_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h800_amcatnlo",
    id=14636495,
    processes=[procs.azh_htt_zll_a2000_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2000_h900_amcatnlo",
    id=14643988,
    processes=[procs.azh_htt_zll_a2000_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2000_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1000_amcatnlo",
    id=14536369,
    processes=[procs.azh_htt_zll_a2100_h1000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1100_amcatnlo",
    id=14637855,
    processes=[procs.azh_htt_zll_a2100_h1100_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1100_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1200_amcatnlo",
    id=14640710,
    processes=[procs.azh_htt_zll_a2100_h1200_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1200_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1300_amcatnlo",
    id=14636479,
    processes=[procs.azh_htt_zll_a2100_h1300_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1300_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1400_amcatnlo",
    id=14637248,
    processes=[procs.azh_htt_zll_a2100_h1400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1500_amcatnlo",
    id=14645029,
    processes=[procs.azh_htt_zll_a2100_h1500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1700_amcatnlo",
    id=14637551,
    processes=[procs.azh_htt_zll_a2100_h1700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1800_amcatnlo",
    id=14638095,
    processes=[procs.azh_htt_zll_a2100_h1800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h1900_amcatnlo",
    id=14643999,
    processes=[procs.azh_htt_zll_a2100_h1900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-1900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h2000_amcatnlo",
    id=14536433,
    processes=[procs.azh_htt_zll_a2100_h2000_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-2000_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h350_amcatnlo",
    id=14640847,
    processes=[procs.azh_htt_zll_a2100_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h400_amcatnlo",
    id=14549535,
    processes=[procs.azh_htt_zll_a2100_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h500_amcatnlo",
    id=14641088,
    processes=[procs.azh_htt_zll_a2100_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h600_amcatnlo",
    id=14645539,
    processes=[procs.azh_htt_zll_a2100_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h700_amcatnlo",
    id=14636576,
    processes=[procs.azh_htt_zll_a2100_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h800_amcatnlo",
    id=14644946,
    processes=[procs.azh_htt_zll_a2100_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a2100_h900_amcatnlo",
    id=14641004,
    processes=[procs.azh_htt_zll_a2100_h900_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-2100_MH-900_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a430_h330_amcatnlo",
    id=14640871,
    processes=[procs.azh_htt_zll_a430_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-430_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h330_amcatnlo",
    id=14641217,
    processes=[procs.azh_htt_zll_a450_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a450_h350_amcatnlo",
    id=14637724,
    processes=[procs.azh_htt_zll_a450_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-450_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h330_amcatnlo",
    id=14645669,
    processes=[procs.azh_htt_zll_a500_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h350_amcatnlo",
    id=14548216,
    processes=[procs.azh_htt_zll_a500_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h370_amcatnlo",
    id=14648537,
    processes=[procs.azh_htt_zll_a500_h370_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a500_h400_amcatnlo",
    id=14537163,
    processes=[procs.azh_htt_zll_a500_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-500_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h330_amcatnlo",
    id=14640737,
    processes=[procs.azh_htt_zll_a550_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h350_amcatnlo",
    id=14641310,
    processes=[procs.azh_htt_zll_a550_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h400_amcatnlo",
    id=14641298,
    processes=[procs.azh_htt_zll_a550_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a550_h450_amcatnlo",
    id=14644728,
    processes=[procs.azh_htt_zll_a550_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-550_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h330_amcatnlo",
    id=14643492,
    processes=[procs.azh_htt_zll_a600_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h350_amcatnlo",
    id=14644865,
    processes=[procs.azh_htt_zll_a600_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h400_amcatnlo",
    id=14640637,
    processes=[procs.azh_htt_zll_a600_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h450_amcatnlo",
    id=14644417,
    processes=[procs.azh_htt_zll_a600_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a600_h500_amcatnlo",
    id=14641414,
    processes=[procs.azh_htt_zll_a600_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-600_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h330_amcatnlo",
    id=14644791,
    processes=[procs.azh_htt_zll_a650_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h350_amcatnlo",
    id=14636505,
    processes=[procs.azh_htt_zll_a650_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h400_amcatnlo",
    id=14643912,
    processes=[procs.azh_htt_zll_a650_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h450_amcatnlo",
    id=14641233,
    processes=[procs.azh_htt_zll_a650_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h500_amcatnlo",
    id=14637773,
    processes=[procs.azh_htt_zll_a650_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a650_h550_amcatnlo",
    id=14637782,
    processes=[procs.azh_htt_zll_a650_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-650_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h330_amcatnlo",
    id=14637877,
    processes=[procs.azh_htt_zll_a700_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h350_amcatnlo",
    id=14549119,
    processes=[procs.azh_htt_zll_a700_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h370_amcatnlo",
    id=14548653,
    processes=[procs.azh_htt_zll_a700_h370_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h400_amcatnlo",
    id=14550258,
    processes=[procs.azh_htt_zll_a700_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h450_amcatnlo",
    id=14644343,
    processes=[procs.azh_htt_zll_a700_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h500_amcatnlo",
    id=14645288,
    processes=[procs.azh_htt_zll_a700_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a700_h550_amcatnlo",
    id=14644477,
    processes=[procs.azh_htt_zll_a700_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-700_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h330_amcatnlo",
    id=14641059,
    processes=[procs.azh_htt_zll_a750_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h350_amcatnlo",
    id=14644713,
    processes=[procs.azh_htt_zll_a750_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h400_amcatnlo",
    id=14637708,
    processes=[procs.azh_htt_zll_a750_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h450_amcatnlo",
    id=14640716,
    processes=[procs.azh_htt_zll_a750_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h500_amcatnlo",
    id=14636467,
    processes=[procs.azh_htt_zll_a750_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h550_amcatnlo",
    id=14644222,
    processes=[procs.azh_htt_zll_a750_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h600_amcatnlo",
    id=14644813,
    processes=[procs.azh_htt_zll_a750_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a750_h650_amcatnlo",
    id=14644183,
    processes=[procs.azh_htt_zll_a750_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-750_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h330_amcatnlo",
    id=14643977,
    processes=[procs.azh_htt_zll_a800_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h350_amcatnlo",
    id=14638955,
    processes=[procs.azh_htt_zll_a800_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h400_amcatnlo",
    id=14643987,
    processes=[procs.azh_htt_zll_a800_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h450_amcatnlo",
    id=14637537,
    processes=[procs.azh_htt_zll_a800_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h500_amcatnlo",
    id=14636808,
    processes=[procs.azh_htt_zll_a800_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h550_amcatnlo",
    id=14640965,
    processes=[procs.azh_htt_zll_a800_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h600_amcatnlo",
    id=14548217,
    processes=[procs.azh_htt_zll_a800_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h650_amcatnlo",
    id=14647537,
    processes=[procs.azh_htt_zll_a800_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a800_h700_amcatnlo",
    id=14637545,
    processes=[procs.azh_htt_zll_a800_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-800_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h330_amcatnlo",
    id=14636408,
    processes=[procs.azh_htt_zll_a850_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h350_amcatnlo",
    id=14640072,
    processes=[procs.azh_htt_zll_a850_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h400_amcatnlo",
    id=14641161,
    processes=[procs.azh_htt_zll_a850_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h450_amcatnlo",
    id=14644205,
    processes=[procs.azh_htt_zll_a850_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h500_amcatnlo",
    id=14636506,
    processes=[procs.azh_htt_zll_a850_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h550_amcatnlo",
    id=14640940,
    processes=[procs.azh_htt_zll_a850_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h600_amcatnlo",
    id=14637903,
    processes=[procs.azh_htt_zll_a850_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h650_amcatnlo",
    id=14644591,
    processes=[procs.azh_htt_zll_a850_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h700_amcatnlo",
    id=14645081,
    processes=[procs.azh_htt_zll_a850_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a850_h750_amcatnlo",
    id=14640939,
    processes=[procs.azh_htt_zll_a850_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-850_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h330_amcatnlo",
    id=14641018,
    processes=[procs.azh_htt_zll_a900_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h350_amcatnlo",
    id=14647696,
    processes=[procs.azh_htt_zll_a900_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h370_amcatnlo",
    id=14548218,
    processes=[procs.azh_htt_zll_a900_h370_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-370_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h400_amcatnlo",
    id=14544289,
    processes=[procs.azh_htt_zll_a900_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h450_amcatnlo",
    id=14637509,
    processes=[procs.azh_htt_zll_a900_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h550_amcatnlo",
    id=14640075,
    processes=[procs.azh_htt_zll_a900_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h500_amcatnlo",
    id=14640067,
    processes=[procs.azh_htt_zll_a900_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h600_amcatnlo",
    id=14641600,
    processes=[procs.azh_htt_zll_a900_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h650_amcatnlo",
    id=14645044,
    processes=[procs.azh_htt_zll_a900_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h700_amcatnlo",
    id=14644427,
    processes=[procs.azh_htt_zll_a900_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h750_amcatnlo",
    id=14641142,
    processes=[procs.azh_htt_zll_a900_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a900_h800_amcatnlo",
    id=14636409,
    processes=[procs.azh_htt_zll_a900_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-900_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h330_amcatnlo",
    id=14636607,
    processes=[procs.azh_htt_zll_a950_h330_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-330_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h350_amcatnlo",
    id=14638010,
    processes=[procs.azh_htt_zll_a950_h350_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-350_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h400_amcatnlo",
    id=14638017,
    processes=[procs.azh_htt_zll_a950_h400_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-400_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h450_amcatnlo",
    id=14642920,
    processes=[procs.azh_htt_zll_a950_h450_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-450_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h500_amcatnlo",
    id=14637960,
    processes=[procs.azh_htt_zll_a950_h500_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-500_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=49000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h550_amcatnlo",
    id=14641687,
    processes=[procs.azh_htt_zll_a950_h550_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-550_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h600_amcatnlo",
    id=14637720,
    processes=[procs.azh_htt_zll_a950_h600_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-600_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h650_amcatnlo",
    id=14637077,
    processes=[procs.azh_htt_zll_a950_h650_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-650_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h700_amcatnlo",
    id=14636448,
    processes=[procs.azh_htt_zll_a950_h700_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-700_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h750_amcatnlo",
    id=14644979,
    processes=[procs.azh_htt_zll_a950_h750_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-750_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h800_amcatnlo",
    id=14645411,
    processes=[procs.azh_htt_zll_a950_h800_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-800_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=50000,
)

cpn.add_dataset(
    name="azh_htt_zll_a950_h850_amcatnlo",
    id=14636342,
    processes=[procs.azh_htt_zll_a950_h850_amcatnlo],
    keys=[
        "/AToZHToLLTTbar_MA-950_MH-850_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=48000,
)
