# coding: utf-8

"""
HH -> bbtautau datasets for the 2018 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_uhh_v12 import campaign_run2_2018_nano_uhh_v12 as cpn


# ggF -> H -> HH


# SM

cpn.add_dataset(
    name="hh_ggf_bbtautau_madgraph",
    id=14356126,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

# BSM scenarios

cpn.add_dataset(
    name="hh_ggf_bbtautau_node1_madgraph",
    id=14347001,
    processes=[procs.hh_ggf_bbtautau_node1],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_1_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node2_madgraph",
    id=14356588,
    processes=[procs.hh_ggf_bbtautau_node2],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_2_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node3_madgraph",
    id=14356108,
    processes=[procs.hh_ggf_bbtautau_node3],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_3_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


cpn.add_dataset(
    name="hh_ggf_bbtautau_node4_madgraph",
    id=14361307,
    processes=[procs.hh_ggf_bbtautau_node4],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_4_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


cpn.add_dataset(
    name="hh_ggf_bbtautau_node5_madgraph",
    id=14356161,
    processes=[procs.hh_ggf_bbtautau_node5],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node6_madgraph",
    id=14355979,
    processes=[procs.hh_ggf_bbtautau_node6],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_6_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node7_madgraph",
    id=14332092,
    processes=[procs.hh_ggf_bbtautau_node7],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_7_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


cpn.add_dataset(
    name="hh_ggf_bbtautau_node8_madgraph",
    id=14346840,
    processes=[procs.hh_ggf_bbtautau_node8],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_8_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node9_madgraph",
    id=14366101,
    processes=[procs.hh_ggf_bbtautau_node9],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_9_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node10_madgraph",
    id=14330790,
    processes=[procs.hh_ggf_bbtautau_node10],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_10_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397000,
)

cpn.add_dataset(
    name="hh_ggf_bbtautau_node11_madgraph",
    id=14332902,
    processes=[procs.hh_ggf_bbtautau_node11],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_11_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


cpn.add_dataset(
    name="hh_ggf_bbtautau_node12_madgraph",
    id=14349211,
    processes=[procs.hh_ggf_bbtautau_node12],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_12_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


# ggF -> radion -> HH


cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m250_madgraph",
    id=14304477,
    processes=[procs.radion_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m260_madgraph",
    id=14331329,
    processes=[procs.radion_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)
cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m270_madgraph",
    id=14304157,
    processes=[procs.radion_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m280_madgraph",
    id=14336941,
    processes=[procs.radion_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m300_madgraph",
    id=14346478,
    processes=[procs.radion_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m320_madgraph",
    id=14327224,
    processes=[procs.radion_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=289000,
)


cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m350_madgraph",
    id=14336895,
    processes=[procs.radion_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=289000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m400_madgraph",
    id=14346467,
    processes=[procs.radion_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m450_madgraph",
    id=14304159,
    processes=[procs.radion_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m500_madgraph",
    id=14307144,
    processes=[procs.radion_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=289000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m550_madgraph",
    id=14306515,
    processes=[procs.radion_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=196000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m600_madgraph",
    id=14346429,
    processes=[procs.radion_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m650_madgraph",
    id=14305052,
    processes=[procs.radion_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m700_madgraph",
    id=14346381,
    processes=[procs.radion_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m750_madgraph",
    id=14304450,
    processes=[procs.radion_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m800_madgraph",
    id=14304421,
    processes=[procs.radion_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m850_madgraph",
    id=14304905,
    processes=[procs.radion_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m900_madgraph",
    id=14313896,
    processes=[procs.radion_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1000_madgraph",
    id=14346481,
    processes=[procs.radion_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1250_madgraph",
    id=14308354,
    processes=[procs.radion_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1500_madgraph",
    id=14302066,
    processes=[procs.radion_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1750_madgraph",
    id=14346572,
    processes=[procs.radion_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2000_madgraph",
    id=14318236,
    processes=[procs.radion_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2500_madgraph",
    id=14307129,
    processes=[procs.radion_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m3000_madgraph",
    id=14317809,
    processes=[procs.radion_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


# ggF -> bulk graviton -> HH


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m250_madgraph",
    id=14315749,
    processes=[procs.graviton_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=384000,
)


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m260_madgraph",
    id=14302683,
    processes=[procs.graviton_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m270_madgraph",
    id=14346693,
    processes=[procs.graviton_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m280_madgraph",
    id=14346579,
    processes=[procs.graviton_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m300",
    id=14346590,
    processes=[procs.graviton_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m320_madgraph",
    id=14346358,
    processes=[procs.graviton_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=297000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m350_madgraph",
    id=14317919,
    processes=[procs.graviton_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=295000,
)


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m400_madgraph",
    id=14346578,
    processes=[procs.graviton_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m450_madgraph",
    id=14307091,
    processes=[procs.graviton_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m500_madgraph",
    id=14346448,
    processes=[procs.graviton_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=297000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m550_madgraph",
    id=14307153,
    processes=[procs.graviton_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m600_madgraph",
    id=14346863,
    processes=[procs.graviton_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m650_madgraph",
    id=14346653,
    processes=[procs.graviton_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m700_madgraph",
    id=14307198,
    processes=[procs.graviton_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m750_madgraph",
    id=14305701,
    processes=[procs.graviton_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=191000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m800_madgraph",
    id=14311885,
    processes=[procs.graviton_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m850_madgraph",
    id=14315810,
    processes=[procs.graviton_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m900_madgraph",
    id=14327388,
    processes=[procs.graviton_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=197000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1000_madgraph",
    id=14346486,
    processes=[procs.graviton_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1250_madgraph",
    id=14304903,
    processes=[procs.graviton_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1500_madgraph",
    id=14305049,
    processes=[procs.graviton_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1750_madgraph",
    id=14307150,
    processes=[procs.graviton_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2000_madgraph",
    id=14304447,
    processes=[procs.graviton_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2500_madgraph",
    id=14327217,
    processes=[procs.graviton_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m3000_madgraph",
    id=14305056,
    processes=[procs.graviton_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


# vbf -> radion -> HH

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m250_madgraph",
    id=14311235,
    processes=[procs.radion_hh_vbf_bbtautau_m250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=394000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m260_madgraph",
    id=14310812,
    processes=[procs.radion_hh_vbf_bbtautau_m260],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m270_madgraph",
    id=14310100,
    processes=[procs.radion_hh_vbf_bbtautau_m270],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m280_madgraph",
    id=14310981,
    processes=[procs.radion_hh_vbf_bbtautau_m280],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m300_madgraph",
    id=14311409,
    processes=[procs.radion_hh_vbf_bbtautau_m300],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=291000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m320_madgraph",
    id=14309931,
    processes=[procs.radion_hh_vbf_bbtautau_m320],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m350_madgraph",
    id=14310420,
    processes=[procs.radion_hh_vbf_bbtautau_m350],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m400_madgraph",
    id=14310226,
    processes=[procs.radion_hh_vbf_bbtautau_m400],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=288000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m450_madgraph",
    id=14310924,
    processes=[procs.radion_hh_vbf_bbtautau_m450],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=285000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m500_madgraph",
    id=14311215,
    processes=[procs.radion_hh_vbf_bbtautau_m500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=294000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m550_madgraph",
    id=14310983,
    processes=[procs.radion_hh_vbf_bbtautau_m550],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=191000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m600_madgraph",
    id=14310965,
    processes=[procs.radion_hh_vbf_bbtautau_m600],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=194000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m650_madgraph",
    id=14310036,
    processes=[procs.radion_hh_vbf_bbtautau_m650],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m700_madgraph",
    id=14310380,
    processes=[procs.radion_hh_vbf_bbtautau_m700],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m750_madgraph",
    id=14310859,
    processes=[procs.radion_hh_vbf_bbtautau_m750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=194000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m800_madgraph",
    id=14310297,
    processes=[procs.radion_hh_vbf_bbtautau_m800],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m850_madgraph",
    id=14310949,
    processes=[procs.radion_hh_vbf_bbtautau_m850],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m900_madgraph",
    id=14310341,
    processes=[procs.radion_hh_vbf_bbtautau_m900],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m1000_madgraph",
    id=14311345,
    processes=[procs.radion_hh_vbf_bbtautau_m1000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m1250_madgraph",
    id=14310805,
    processes=[procs.radion_hh_vbf_bbtautau_m1250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m1500_madgraph",
    id=14311124,
    processes=[procs.radion_hh_vbf_bbtautau_m1500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m1750_madgraph",
    id=14310945,
    processes=[procs.radion_hh_vbf_bbtautau_m1750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m2000_madgraph",
    id=14310579,
    processes=[procs.radion_hh_vbf_bbtautau_m2000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)


cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m2500_madgraph",
    id=14311168,
    processes=[procs.radion_hh_vbf_bbtautau_m2500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_vbf_bbtautau_m3000_madgraph",
    id=14311447,
    processes=[procs.radion_hh_vbf_bbtautau_m3000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)


# vbf -> bulk graviton -> HH


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m250_madgraph",
    id=14310533,
    processes=[procs.graviton_hh_vbf_bbtautau_m250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m260_madgraph",
    id=14311370,
    processes=[procs.graviton_hh_vbf_bbtautau_m260],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m270_madgraph",
    id=14310664,
    processes=[procs.graviton_hh_vbf_bbtautau_m270],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m280_madgraph",
    id=14311242,
    processes=[procs.graviton_hh_vbf_bbtautau_m280],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m300_madgraph",
    id=14309982,
    processes=[procs.graviton_hh_vbf_bbtautau_m300],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m320_madgraph",
    id=14311297,
    processes=[procs.graviton_hh_vbf_bbtautau_m320],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=297000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m350_madgraph",
    id=14310572,
    processes=[procs.graviton_hh_vbf_bbtautau_m350],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m400_madgraph",
    id=14311230,
    processes=[procs.graviton_hh_vbf_bbtautau_m400],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m450_madgraph",
    id=14311274,
    processes=[procs.graviton_hh_vbf_bbtautau_m450],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m500_madgraph",
    id=14310249,
    processes=[procs.graviton_hh_vbf_bbtautau_m500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m550_madgraph",
    id=14311264,
    processes=[procs.graviton_hh_vbf_bbtautau_m550],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m600_madgraph",
    id=14311268,
    processes=[procs.graviton_hh_vbf_bbtautau_m600],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=197000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m650_madgraph",
    id=14309787,
    processes=[procs.graviton_hh_vbf_bbtautau_m650],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m700_madgraph",
    id=14311344,
    processes=[procs.graviton_hh_vbf_bbtautau_m700],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=197000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m750_madgraph",
    id=14309923,
    processes=[procs.graviton_hh_vbf_bbtautau_m750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m800_madgraph",
    id=14310500,
    processes=[procs.graviton_hh_vbf_bbtautau_m800],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m850_madgraph",
    id=14310560,
    processes=[procs.graviton_hh_vbf_bbtautau_m850],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)


cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m900_madgraph",
    id=14309934,
    processes=[procs.graviton_hh_vbf_bbtautau_m900],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1000_madgraph",
    id=14310535,
    processes=[procs.graviton_hh_vbf_bbtautau_m1000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1250_madgraph",
    id=14310728,
    processes=[procs.graviton_hh_vbf_bbtautau_m1250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1500_madgraph",
    id=14310657,
    processes=[procs.graviton_hh_vbf_bbtautau_m1500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1750_madgraph",
    id=14310681,
    processes=[procs.graviton_hh_vbf_bbtautau_m1750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m2000_madgraph",
    id=14311423,
    processes=[procs.graviton_hh_vbf_bbtautau_m2000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m2500_madgraph",
    id=14310911,
    processes=[procs.graviton_hh_vbf_bbtautau_m2500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m3000_madgraph",
    id=14311366,
    processes=[procs.graviton_hh_vbf_bbtautau_m3000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=97000,
)
