# coding: utf-8

"""
HH -> bbtautau datasets for the 2017 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn


#
# ggF -> H -> HH
#

# # SM
cpn.add_dataset(
    name="hh_ggf_bbtautau_madgraph",
    id=14336680,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=400000,
)
#
# # BSM scenarios
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node1_madgraph",
#     id=14366362,
#     processes=[procs.hh_ggf_bbtautau_node1],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_1_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=400000,
# )
#
# # missing
# # cpn.add_dataset(
# #     name="hh_ggf_bbtautau_node2_madgraph",
# #     id=,
# #     processes=[procs.hh_ggf_bbtautau_node2],
# #     keys=[
# #         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=,
# #     n_events=,
# # )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node3_madgraph",
#     id=14369747,
#     processes=[procs.hh_ggf_bbtautau_node3],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_3_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node4_madgraph",
#     id=14368375,
#     processes=[procs.hh_ggf_bbtautau_node4],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_4_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node5_madgraph",
#     id=14364195,
#     processes=[procs.hh_ggf_bbtautau_node5],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node6_madgraph",
#     id=14368376,
#     processes=[procs.hh_ggf_bbtautau_node6],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_6_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node7_madgraph",
#     id=14369764,
#     processes=[procs.hh_ggf_bbtautau_node7],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_7_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node8_madgraph",
#     id=14370426,
#     processes=[procs.hh_ggf_bbtautau_node8],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_8_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node9_madgraph",
#     id=14366977,
#     processes=[procs.hh_ggf_bbtautau_node9],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_9_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node10_madgraph",
#     id=14369844,
#     processes=[procs.hh_ggf_bbtautau_node10],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_10_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node11_madgraph",
#     id=14368408,
#     processes=[procs.hh_ggf_bbtautau_node11],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_11_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node12_madgraph",
#     id=14368374,
#     processes=[procs.hh_ggf_bbtautau_node12],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_12_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=400000,
# )
#
#
# #
# # ggF -> radion -> HH
# #
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m250_madgraph",
#     id=14302777,
#     processes=[procs.radion_hh_ggf_bbtautau_m250],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m260_madgraph",
#     id=14346707,
#     processes=[procs.radion_hh_ggf_bbtautau_m260],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=22,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m270_madgraph",
#     id=14308899,
#     processes=[procs.radion_hh_ggf_bbtautau_m270],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=17,
#     n_events=393000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m280_madgraph",
#     id=14346524,
#     processes=[procs.radion_hh_ggf_bbtautau_m280],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=388000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m300_madgraph",
#     id=14305216,
#     processes=[procs.radion_hh_ggf_bbtautau_m300],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=276000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m320_madgraph",
#     id=14317863,
#     processes=[procs.radion_hh_ggf_bbtautau_m320],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=286000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m350_madgraph",
#     id=14305228,
#     processes=[procs.radion_hh_ggf_bbtautau_m350],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=282000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m400_madgraph",
#     id=14304148,
#     processes=[procs.radion_hh_ggf_bbtautau_m400],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=288000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m450_madgraph",
#     id=14327613,
#     processes=[procs.radion_hh_ggf_bbtautau_m450],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=294000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m500_madgraph",
#     id=14305221,
#     processes=[procs.radion_hh_ggf_bbtautau_m500],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=285000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m550_madgraph",
#     id=14302808,
#     processes=[procs.radion_hh_ggf_bbtautau_m550],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m600_madgraph",
#     id=14308469,
#     processes=[procs.radion_hh_ggf_bbtautau_m600],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m650_madgraph",
#     id=14346493,
#     processes=[procs.radion_hh_ggf_bbtautau_m650],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m700_madgraph",
#     id=14346372,
#     processes=[procs.radion_hh_ggf_bbtautau_m700],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m750_madgraph",
#     id=14346507,
#     processes=[procs.radion_hh_ggf_bbtautau_m750],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=191000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m800_madgraph",
#     id=14327247,
#     processes=[procs.radion_hh_ggf_bbtautau_m800],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m850_madgraph",
#     id=14329740,
#     processes=[procs.radion_hh_ggf_bbtautau_m850],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=189000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m900_madgraph",
#     id=14346605,
#     processes=[procs.radion_hh_ggf_bbtautau_m900],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m1000_madgraph",
#     id=14305457,
#     processes=[procs.radion_hh_ggf_bbtautau_m1000],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m1250_madgraph",
#     id=14302759,
#     processes=[procs.radion_hh_ggf_bbtautau_m1250],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m1500_madgraph",
#     id=14304452,
#     processes=[procs.radion_hh_ggf_bbtautau_m1500],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m1750_madgraph",
#     id=14302315,
#     processes=[procs.radion_hh_ggf_bbtautau_m1750],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m2000_madgraph",
#     id=14304853,
#     processes=[procs.radion_hh_ggf_bbtautau_m2000],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=97000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m2500_madgraph",
#     id=14305723,
#     processes=[procs.radion_hh_ggf_bbtautau_m2500],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_ggf_bbtautau_m3000_madgraph",
#     id=14346584,
#     processes=[procs.radion_hh_ggf_bbtautau_m3000],
#     keys=[
#         "/GluGluToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=100000,
# )
#
#
# #
# # ggF -> bulk graviton -> HH
# #
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m250_madgraph",
#     id=14309793,
#     processes=[procs.graviton_hh_ggf_bbtautau_m250],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m260_madgraph",
#     id=14302792,
#     processes=[procs.graviton_hh_ggf_bbtautau_m260],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m270_madgraph",
#     id=14330676,
#     processes=[procs.graviton_hh_ggf_bbtautau_m270],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m280_madgraph",
#     id=14330326,
#     processes=[procs.graviton_hh_ggf_bbtautau_m280],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m300_madgraph",
#     id=14346485,
#     processes=[procs.graviton_hh_ggf_bbtautau_m300],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=300000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m320_madgraph",
#     id=14335123,
#     processes=[procs.graviton_hh_ggf_bbtautau_m320],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=297000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m350_madgraph",
#     id=14346502,
#     processes=[procs.graviton_hh_ggf_bbtautau_m350],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=285000,
# )
#
cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m400_madgraph",
    id=14346355,
    processes=[procs.graviton_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODvv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=300000,
)
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m450_madgraph",
#     id=14311442,
#     processes=[procs.graviton_hh_ggf_bbtautau_m450],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=286000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m500_madgraph",
#     id=14307226,
#     processes=[procs.graviton_hh_ggf_bbtautau_m500],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=300000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m550_madgraph",
#     id=14302414,
#     processes=[procs.graviton_hh_ggf_bbtautau_m550],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m600_madgraph",
#     id=14302378,
#     processes=[procs.graviton_hh_ggf_bbtautau_m600],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m650_madgraph",
#     id=14309720,
#     processes=[procs.graviton_hh_ggf_bbtautau_m650],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m700_madgraph",
#     id=14305200,
#     processes=[procs.graviton_hh_ggf_bbtautau_m700],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=198000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m750_madgraph",
#     id=14346504,
#     processes=[procs.graviton_hh_ggf_bbtautau_m750],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m800_madgraph",
#     id=14346495,
#     processes=[procs.graviton_hh_ggf_bbtautau_m800],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m850_madgraph",
#     id=14346604,
#     processes=[procs.graviton_hh_ggf_bbtautau_m850],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m900_madgraph",
#     id=14330168,
#     processes=[procs.graviton_hh_ggf_bbtautau_m900],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=189000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m1000_madgraph",
#     id=14307192,
#     processes=[procs.graviton_hh_ggf_bbtautau_m1000],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=95000,
# )

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1250_madgraph",
    id=14305051,
    processes=[procs.graviton_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=98000,
)

# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m1500_madgraph",
#     id=14302337,
#     processes=[procs.graviton_hh_ggf_bbtautau_m1500],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=100000,
# )

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1750_madgraph",
    id=14307182,
    processes=[procs.graviton_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100000,
)

# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m2000_madgraph",
#     id=14304912,
#     processes=[procs.graviton_hh_ggf_bbtautau_m2000],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m2500_madgraph",
#     id=14306377,
#     processes=[procs.graviton_hh_ggf_bbtautau_m2500],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_ggf_bbtautau_m3000_madgraph",
#     id=14305674,
#     processes=[procs.graviton_hh_ggf_bbtautau_m3000],
#     keys=[
#         "/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=100000,
# )
#
#
# #
# # vbf -> radion -> HH
# #
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m250_madgraph",
#     id=14313383,
#     processes=[procs.radion_hh_vbf_bbtautau_m250],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=397000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m260_madgraph",
#     id=14312102,
#     processes=[procs.radion_hh_vbf_bbtautau_m260],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=15,
#     n_events=394000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m270_madgraph",
#     id=14315423,
#     processes=[procs.radion_hh_vbf_bbtautau_m270],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=8,
#     n_events=379000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m280_madgraph",
#     id=14315394,
#     processes=[procs.radion_hh_vbf_bbtautau_m280],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=394000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m300_madgraph",
#     id=14312259,
#     processes=[procs.radion_hh_vbf_bbtautau_m300],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=294000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m320_madgraph",
#     id=14315335,
#     processes=[procs.radion_hh_vbf_bbtautau_m320],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=276000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m350_madgraph",
#     id=14315249,
#     processes=[procs.radion_hh_vbf_bbtautau_m350],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=297000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m400_madgraph",
#     id=14315364,
#     processes=[procs.radion_hh_vbf_bbtautau_m400],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=297000,
# )
#
# # missing
# # cpn.add_dataset(
# #     name="radion_hh_vbf_bbtautau_m450_madgraph",
# #     id=,
# #     processes=[procs.radion_hh_vbf_bbtautau_m450],
# #     keys=[
# #         "/VBFToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=,
# #     n_events=,
# # )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m500_madgraph",
#     id=14315911,
#     processes=[procs.radion_hh_vbf_bbtautau_m500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=300000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m550_madgraph",
#     id=14313492,
#     processes=[procs.radion_hh_vbf_bbtautau_m550],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m600_madgraph",
#     id=14313271,
#     processes=[procs.radion_hh_vbf_bbtautau_m600],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m650_madgraph",
#     id=14313413,
#     processes=[procs.radion_hh_vbf_bbtautau_m650],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m700_madgraph",
#     id=14312044,
#     processes=[procs.radion_hh_vbf_bbtautau_m700],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=194000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m750_madgraph",
#     id=14313296,
#     processes=[procs.radion_hh_vbf_bbtautau_m750],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m800_madgraph",
#     id=14311221,
#     processes=[procs.radion_hh_vbf_bbtautau_m800],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=194000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m850_madgraph",
#     id=14312594,
#     processes=[procs.radion_hh_vbf_bbtautau_m850],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=12,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m900_madgraph",
#     id=14312083,
#     processes=[procs.radion_hh_vbf_bbtautau_m900],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=197000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1000_madgraph",
#     id=14311676,
#     processes=[procs.radion_hh_vbf_bbtautau_m1000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=97000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1250_madgraph",
#     id=14313782,
#     processes=[procs.radion_hh_vbf_bbtautau_m1250],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1500_madgraph",
#     id=14315286,
#     processes=[procs.radion_hh_vbf_bbtautau_m1500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=97000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1750_madgraph",
#     id=14314144,
#     processes=[procs.radion_hh_vbf_bbtautau_m1750],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m2000_madgraph",
#     id=14319538,
#     processes=[procs.radion_hh_vbf_bbtautau_m2000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=94000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m2500_madgraph",
#     id=14316124,
#     processes=[procs.radion_hh_vbf_bbtautau_m2500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=97000,
# )
#
# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m3000_madgraph",
#     id=14316141,
#     processes=[procs.radion_hh_vbf_bbtautau_m3000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=100000,
# )
#
#
# #
# # vbf -> bulk graviton -> HH
# #
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m250_madgraph",
#     id=14313377,
#     processes=[procs.graviton_hh_vbf_bbtautau_m250],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=399000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m260_madgraph",
#     id=14312620,
#     processes=[procs.graviton_hh_vbf_bbtautau_m260],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=394000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m270_madgraph",
#     id=14311771,
#     processes=[procs.graviton_hh_vbf_bbtautau_m270],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=5,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m280_madgraph",
#     id=14313366,
#     processes=[procs.graviton_hh_vbf_bbtautau_m280],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=400000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m300_madgraph",
#     id=14312031,
#     processes=[procs.graviton_hh_vbf_bbtautau_m300],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=16,
#     n_events=291000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m320_madgraph",
#     id=14312181,
#     processes=[procs.graviton_hh_vbf_bbtautau_m320],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=300000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m350_madgraph",
#     id=14312121,
#     processes=[procs.graviton_hh_vbf_bbtautau_m350],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=297000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m400_madgraph",
#     id=14312057,
#     processes=[procs.graviton_hh_vbf_bbtautau_m400],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=300000,
# )
#
# # missing
# # cpn.add_dataset(
# #     name="graviton_hh_vbf_bbtautau_m450_madgraph",
# #     id=,
# #     processes=[procs.graviton_hh_vbf_bbtautau_m450],
# #     keys=[
# #         "/VBFToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=,
# #     n_events=,
# # )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m500_madgraph",
#     id=14312369,
#     processes=[procs.graviton_hh_vbf_bbtautau_m500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=297000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m550_madgraph",
#     id=14312211,
#     processes=[procs.graviton_hh_vbf_bbtautau_m550],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m600_madgraph",
#     id=14312266,
#     processes=[procs.graviton_hh_vbf_bbtautau_m600],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=13,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m650_madgraph",
#     id=14312370,
#     processes=[procs.graviton_hh_vbf_bbtautau_m650],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=14,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m700_madgraph",
#     id=14313347,
#     processes=[procs.graviton_hh_vbf_bbtautau_m700],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=198000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m750_madgraph",
#     id=14312212,
#     processes=[procs.graviton_hh_vbf_bbtautau_m750],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=12,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m800_madgraph",
#     id=14312060,
#     processes=[procs.graviton_hh_vbf_bbtautau_m800],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=18,
#     n_events=200000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m850_madgraph",
#     id=14312295,
#     processes=[procs.graviton_hh_vbf_bbtautau_m850],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=200000,
# )
#
# # missing
# # cpn.add_dataset(
# #     name="graviton_hh_vbf_bbtautau_m900_madgraph",
# #     id=,
# #     processes=[procs.graviton_hh_vbf_bbtautau_m900],
# #     keys=[
# #         "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
# #     ],
# #     n_files=,
# #     n_events=,
# # )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1000_madgraph",
#     id=14312631,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1250_madgraph",
#     id=14311308,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1250],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1500_madgraph",
#     id=14311279,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1750_madgraph",
#     id=14312650,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1750],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=11,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m2000_madgraph",
#     id=14312081,
#     processes=[procs.graviton_hh_vbf_bbtautau_m2000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m2500_madgraph",
#     id=14312147,
#     processes=[procs.graviton_hh_vbf_bbtautau_m2500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=10,
#     n_events=100000,
# )
#
# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m3000_madgraph",
#     id=14313382,
#     processes=[procs.graviton_hh_vbf_bbtautau_m3000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=9,
#     n_events=100000,
# )
