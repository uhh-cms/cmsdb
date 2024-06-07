# coding: utf-8

"""
HH -> bbtautau datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_uhh_v12 import campaign_run2_2016_nano_uhh_v12 as cpn


#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20_madgraph",
    id=14374930,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)


# BSM scenarios
cpn.add_dataset(
    name="hh_ggf_hbb_htt_node1_madgraph",
    id=14375093,
    processes=[procs.hh_ggf_hbb_htt_node1],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_1_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=170000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node2_madgraph",
    id=14370208,
    processes=[procs.hh_ggf_hbb_htt_node2],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_2_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=166000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node3_madgraph",
    id=14369799,
    processes=[procs.hh_ggf_hbb_htt_node3],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_3_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node4_madgraph",
    id=14373535,
    processes=[procs.hh_ggf_hbb_htt_node4],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_4_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node5_madgraph",
    id=14370961,
    processes=[procs.hh_ggf_hbb_htt_node5],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node6_madgraph",
    id=14374877,
    processes=[procs.hh_ggf_hbb_htt_node6],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_6_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node7_madgraph",
    id=14372004,
    processes=[procs.hh_ggf_hbb_htt_node7],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_7_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node8_madgraph",
    id=14373531,
    processes=[procs.hh_ggf_hbb_htt_node8],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_8_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node9_madgraph",
    id=14373753,
    processes=[procs.hh_ggf_hbb_htt_node9],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_9_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node10_madgraph",
    id=14373533,
    processes=[procs.hh_ggf_hbb_htt_node10],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_10_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node11_madgraph",
    id=14374873,
    processes=[procs.hh_ggf_hbb_htt_node11],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_11_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_node12_madgraph",
    id=14374899,
    processes=[procs.hh_ggf_hbb_htt_node12],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_12_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)


#
# ggF -> radion -> HH
#

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m250_madgraph",
    id=14302510,
    processes=[procs.radion_hh_ggf_hbb_htt_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m260_madgraph",
    id=14301575,
    processes=[procs.radion_hh_ggf_hbb_htt_m260],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m270_madgraph",
    id=14300691,
    processes=[procs.radion_hh_ggf_hbb_htt_m270],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m280_madgraph",
    id=14302499,
    processes=[procs.radion_hh_ggf_hbb_htt_m280],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m300_madgraph",
    id=14301597,
    processes=[procs.radion_hh_ggf_hbb_htt_m300],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m320_madgraph",
    id=14328047,
    processes=[procs.radion_hh_ggf_hbb_htt_m320],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m350_madgraph",
    id=14301476,
    processes=[procs.radion_hh_ggf_hbb_htt_m350],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m400_madgraph",
    id=14302314,
    processes=[procs.radion_hh_ggf_hbb_htt_m400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=134000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m450_madgraph",
    id=14327252,
    processes=[procs.radion_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m500_madgraph",
    id=14301598,
    processes=[procs.radion_hh_ggf_hbb_htt_m500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m550_madgraph",
    id=14301122,
    processes=[procs.radion_hh_ggf_hbb_htt_m550],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m600_madgraph",
    id=14301567,
    processes=[procs.radion_hh_ggf_hbb_htt_m600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m650_madgraph",
    id=14301498,
    processes=[procs.radion_hh_ggf_hbb_htt_m650],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m700_madgraph",
    id=14301042,
    processes=[procs.radion_hh_ggf_hbb_htt_m700],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m750_madgraph",
    id=14307116,
    processes=[procs.radion_hh_ggf_hbb_htt_m750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m800_madgraph",
    id=14302586,
    processes=[procs.radion_hh_ggf_hbb_htt_m800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m850_madgraph",
    id=14346438,
    processes=[procs.radion_hh_ggf_hbb_htt_m850],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m900_madgraph",
    id=14302493,
    processes=[procs.radion_hh_ggf_hbb_htt_m900],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1000_madgraph",
    id=14302284,
    processes=[procs.radion_hh_ggf_hbb_htt_m1000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1250_madgraph",
    id=14302774,
    processes=[procs.radion_hh_ggf_hbb_htt_m1250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1500_madgraph",
    id=14346476,
    processes=[procs.radion_hh_ggf_hbb_htt_m1500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1750_madgraph",
    id=14302749,
    processes=[procs.radion_hh_ggf_hbb_htt_m1750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m2000_madgraph",
    id=14302517,
    processes=[procs.radion_hh_ggf_hbb_htt_m2000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m2500_madgraph",
    id=14301151,
    processes=[procs.radion_hh_ggf_hbb_htt_m2500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m3000_madgraph",
    id=14302763,
    processes=[procs.radion_hh_ggf_hbb_htt_m3000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)


#
# ggF -> bulk graviton -> HH
#

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m250_madgraph",
    id=14301503,
    processes=[procs.graviton_hh_ggf_hbb_htt_m250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m260_madgraph",
    id=14302469,
    processes=[procs.graviton_hh_ggf_hbb_htt_m260],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m270_madgraph",
    id=14302682,
    processes=[procs.graviton_hh_ggf_hbb_htt_m270],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m280_madgraph",
    id=14307123,
    processes=[procs.graviton_hh_ggf_hbb_htt_m280],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m300_madgraph",
    id=14302691,
    processes=[procs.graviton_hh_ggf_hbb_htt_m300],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m320_madgraph",
    id=14301964,
    processes=[procs.graviton_hh_ggf_hbb_htt_m320],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=137000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m350_madgraph",
    id=14302701,
    processes=[procs.graviton_hh_ggf_hbb_htt_m350],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m400_madgraph",
    id=14301632,
    processes=[procs.graviton_hh_ggf_hbb_htt_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m450_madgraph",
    id=14327296,
    processes=[procs.graviton_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m500_madgraph",
    id=14302698,
    processes=[procs.graviton_hh_ggf_hbb_htt_m500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m550_madgraph",
    id=14302695,
    processes=[procs.graviton_hh_ggf_hbb_htt_m550],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m600_madgraph",
    id=14301494,
    processes=[procs.graviton_hh_ggf_hbb_htt_m600],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m650_madgraph",
    id=14302697,
    processes=[procs.graviton_hh_ggf_hbb_htt_m650],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m700_madgraph",
    id=14302694,
    processes=[procs.graviton_hh_ggf_hbb_htt_m700],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m750_madgraph",
    id=14302705,
    processes=[procs.graviton_hh_ggf_hbb_htt_m750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m800_madgraph",
    id=14302692,
    processes=[procs.graviton_hh_ggf_hbb_htt_m800],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m850_madgraph",
    id=14302494,
    processes=[procs.graviton_hh_ggf_hbb_htt_m850],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m900_madgraph",
    id=14302790,
    processes=[procs.graviton_hh_ggf_hbb_htt_m900],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1000_madgraph",
    id=14302752,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1250_madgraph",
    id=14302430,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1500_madgraph",
    id=14302608,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1750_madgraph",
    id=14327225,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m2000_madgraph",
    id=14302799,
    processes=[procs.graviton_hh_ggf_hbb_htt_m2000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m2500_madgraph",
    id=14302809,
    processes=[procs.graviton_hh_ggf_hbb_htt_m2500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m3000_madgraph",
    id=14302801,
    processes=[procs.graviton_hh_ggf_hbb_htt_m3000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

# #
# # vbf -> radion -> HH
# #

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m250_madgraph",
    id=14309148,
    processes=[procs.radion_hh_vbf_hbb_htt_m250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=176000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m260_madgraph",
    id=14309020,
    processes=[procs.radion_hh_vbf_hbb_htt_m260],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=178000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m270_madgraph",
    id=14311151,
    processes=[procs.radion_hh_vbf_hbb_htt_m270],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=182000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m280_madgraph",
    id=14309161,
    processes=[procs.radion_hh_vbf_hbb_htt_m280],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=176000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m300_madgraph",
    id=14309100,
    processes=[procs.radion_hh_vbf_hbb_htt_m300],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=132000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m320_madgraph",
    id=14310842,
    processes=[procs.radion_hh_vbf_hbb_htt_m320],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=136000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m350_madgraph",
    id=14309861,
    processes=[procs.radion_hh_vbf_hbb_htt_m350],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m400_madgraph",
    id=14311190,
    processes=[procs.radion_hh_vbf_hbb_htt_m400],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=136000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m450_madgraph",
    id=14310135,
    processes=[procs.radion_hh_vbf_hbb_htt_m450],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m500_madgraph",
    id=14310709,
    processes=[procs.radion_hh_vbf_hbb_htt_m500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m550_madgraph",
    id=14310466,
    processes=[procs.radion_hh_vbf_hbb_htt_m550],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m600_madgraph",
    id=14309160,
    processes=[procs.radion_hh_vbf_hbb_htt_m600],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=90000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m650_madgraph",
    id=14309190,
    processes=[procs.radion_hh_vbf_hbb_htt_m650],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m700_madgraph",
    id=14311152,
    processes=[procs.radion_hh_vbf_hbb_htt_m700],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m750_madgraph",
    id=14309175,
    processes=[procs.radion_hh_vbf_hbb_htt_m750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m800_madgraph",
    id=14310505,
    processes=[procs.radion_hh_vbf_hbb_htt_m800],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m850_madgraph",
    id=14311379,
    processes=[procs.radion_hh_vbf_hbb_htt_m850],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m900_madgraph",
    id=14309625,
    processes=[procs.radion_hh_vbf_hbb_htt_m900],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m1000_madgraph",
    id=14309210,
    processes=[procs.radion_hh_vbf_hbb_htt_m1000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=44000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m1250_madgraph",
    id=14310195,
    processes=[procs.radion_hh_vbf_hbb_htt_m1250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m1500_madgraph",
    id=14310941,
    processes=[procs.radion_hh_vbf_hbb_htt_m1500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=44000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m1750_madgraph",
    id=14310430,
    processes=[procs.radion_hh_vbf_hbb_htt_m1750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m2000_madgraph",
    id=14310892,
    processes=[procs.radion_hh_vbf_hbb_htt_m2000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=44000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m2500_madgraph",
    id=14310517,
    processes=[procs.radion_hh_vbf_hbb_htt_m2500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="radion_hh_vbf_hbb_htt_m3000_madgraph",
    id=14309309,
    processes=[procs.radion_hh_vbf_hbb_htt_m3000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=44000,
)

#
# vbf -> bulk graviton -> HH
#

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m250_madgraph",
    id=14310654,
    processes=[procs.graviton_hh_vbf_hbb_htt_m250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m260_madgraph",
    id=14311003,
    processes=[procs.graviton_hh_vbf_hbb_htt_m260],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=176000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m270_madgraph",
    id=14309629,
    processes=[procs.graviton_hh_vbf_hbb_htt_m270],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=180000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m280_madgraph",
    id=14310656,
    processes=[procs.graviton_hh_vbf_hbb_htt_m280],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m300_madgraph",
    id=14310586,
    processes=[procs.graviton_hh_vbf_hbb_htt_m300],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m320_madgraph",
    id=14310975,
    processes=[procs.graviton_hh_vbf_hbb_htt_m320],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=134000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m350_madgraph",
    id=14311117,
    processes=[procs.graviton_hh_vbf_hbb_htt_m350],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=138000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m400_madgraph",
    id=14311181,
    processes=[procs.graviton_hh_vbf_hbb_htt_m400],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=132000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m450_madgraph",
    id=14309349,
    processes=[procs.graviton_hh_vbf_hbb_htt_m450],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=136000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m500_madgraph",
    id=14309200,
    processes=[procs.graviton_hh_vbf_hbb_htt_m500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=134000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m550_madgraph",
    id=14310115,
    processes=[procs.graviton_hh_vbf_hbb_htt_m550],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m600_madgraph",
    id=14309252,
    processes=[procs.graviton_hh_vbf_hbb_htt_m600],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m650_madgraph",
    id=14310547,
    processes=[procs.graviton_hh_vbf_hbb_htt_m650],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m700_madgraph",
    id=14311093,
    processes=[procs.graviton_hh_vbf_hbb_htt_m700],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m750_madgraph",
    id=14310895,
    processes=[procs.graviton_hh_vbf_hbb_htt_m750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m800_madgraph",
    id=14311153,
    processes=[procs.graviton_hh_vbf_hbb_htt_m800],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m850_madgraph",
    id=14310531,
    processes=[procs.graviton_hh_vbf_hbb_htt_m850],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m900_madgraph",
    id=14310429,
    processes=[procs.graviton_hh_vbf_hbb_htt_m900],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=92000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m1000_madgraph",
    id=14310463,
    processes=[procs.graviton_hh_vbf_hbb_htt_m1000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m1250_madgraph",
    id=14310462,
    processes=[procs.graviton_hh_vbf_hbb_htt_m1250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m1500_madgraph",
    id=14309776,
    processes=[procs.graviton_hh_vbf_hbb_htt_m1500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m1750_madgraph",
    id=14309067,
    processes=[procs.graviton_hh_vbf_hbb_htt_m1750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m2000_madgraph",
    id=14309506,
    processes=[procs.graviton_hh_vbf_hbb_htt_m2000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m2500_madgraph",
    id=14310005,
    processes=[procs.graviton_hh_vbf_hbb_htt_m2500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_hbb_htt_m3000_madgraph",
    id=14310674,
    processes=[procs.graviton_hh_vbf_hbb_htt_m3000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=46000,
)
