# coding: utf-8


"""HH -> bbtautau datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH."""


import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn

#####
# SM
#####

# ggF -> H -> HH

cpn.add_dataset(
    name="hh_ggf_bbtautau_madgraph",
    id=14335916,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=216_000,
)

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node10_madgraph",
#     id=14355626,
#     processes=[procs.hh_ggf_bbtautau_node10],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_10_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node6_madgraph",
#     id=14347302,
#     processes=[procs.hh_ggf_bbtautau_node6],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_6_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node9_madgraph",
#     id=14359169,
#     processes=[procs.hh_ggf_bbtautau_node9],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_9_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node11_madgraph",
#     id=14351156,
#     processes=[procs.hh_ggf_bbtautau_node11],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_11_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node2_madgraph",
#     id=14342671,
#     processes=[procs.hh_ggf_bbtautau_node2],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_2_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=210000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node8_madgraph",
#     id=14343392,
#     processes=[procs.hh_ggf_bbtautau_node8],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_8_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node4_madgraph",
#     id=14363921,
#     processes=[procs.hh_ggf_bbtautau_node4],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_4_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node5_madgraph",
#     id=14359164,
#     processes=[procs.hh_ggf_bbtautau_node5],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node7_madgraph",
#     id=14358610,
#     processes=[procs.hh_ggf_bbtautau_node7],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_7_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node1_madgraph",
#     id=14349843,
#     processes=[procs.hh_ggf_bbtautau_node1],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_1_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node12_madgraph",
#     id=14332443,
#     processes=[procs.hh_ggf_bbtautau_node12],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_12_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="hh_ggf_bbtautau_node3_madgraph",
#     id=14351327,
#     processes=[procs.hh_ggf_bbtautau_node3],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_3_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

################
# BSM scenarios
################

# ggF -> radion -> HH

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m700_madgraph",
    id=14346431,
    processes=[procs.radion_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m450_madgraph",
    id=14346648,
    processes=[procs.radion_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m300_madgraph",
    id=14346436,
    processes=[procs.radion_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m350_madgraph",
    id=14346867,
    processes=[procs.radion_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m750_madgraph",
    id=14346824,
    processes=[procs.radion_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m800_madgraph",
    id=14346661,
    processes=[procs.radion_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m3000_madgraph",
    id=14346643,
    processes=[procs.radion_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m650_madgraph",
    id=14347450,
    processes=[procs.radion_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m600_madgraph",
    id=14346396,
    processes=[procs.radion_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m400_madgraph",
    id=14346575,
    processes=[procs.radion_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m280_madgraph",
    id=14357712,
    processes=[procs.radion_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=214_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m850_madgraph",
    id=14346515,
    processes=[procs.radion_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m900_madgraph",
    id=14346497,
    processes=[procs.radion_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=96_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m500_madgraph",
    id=14346666,
    processes=[procs.radion_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m320_madgraph",
    id=14346716,
    processes=[procs.radion_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=162_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m550_madgraph",
    id=14346591,
    processes=[procs.radion_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=108_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m270_madgraph",
    id=14346791,
    processes=[procs.radion_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=214_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m260_madgraph",
    id=14346788,
    processes=[procs.radion_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2500_madgraph",
    id=14346427,
    processes=[procs.radion_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m250_madgraph",
    id=14346555,
    processes=[procs.radion_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2000_madgraph",
    id=14346581,
    processes=[procs.radion_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1750_madgraph",
    id=14346610,
    processes=[procs.radion_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1500_madgraph",
    id=14346361,
    processes=[procs.radion_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1250_madgraph",
    id=14646635,
    processes=[procs.radion_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1000_madgraph",
    id=14346516,
    processes=[procs.radion_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=54_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1100_madgraph",
    id=14411934,
    processes=[procs.radion_hh_ggf_bbtautau_m1100],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1100_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1200_madgraph",
    id=14419410,
    processes=[procs.radion_hh_ggf_bbtautau_m1200],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1200_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1300_madgraph",
    id=14412110,
    processes=[procs.radion_hh_ggf_bbtautau_m1300],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1400_madgraph",
    id=14397712,
    processes=[procs.radion_hh_ggf_bbtautau_m1400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1600_madgraph",
    id=14413443,
    processes=[procs.radion_hh_ggf_bbtautau_m1600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=213_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1700_madgraph",
    id=14419235,
    processes=[procs.radion_hh_ggf_bbtautau_m1700],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1800_madgraph",
    id=14391871,
    processes=[procs.radion_hh_ggf_bbtautau_m1800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m1900_madgraph",
    id=14395552,
    processes=[procs.radion_hh_ggf_bbtautau_m1900],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2200_madgraph",
    id=14414886,
    processes=[procs.radion_hh_ggf_bbtautau_m2200],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2200_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=214_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2400_madgraph",
    id=14397821,
    processes=[procs.radion_hh_ggf_bbtautau_m2400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v4/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=216_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2600_madgraph",
    id=14397727,
    processes=[procs.radion_hh_ggf_bbtautau_m2600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=213_000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m2800_madgraph",
    id=14396084,
    processes=[procs.radion_hh_ggf_bbtautau_m2800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v4/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=216_000,
)


# ggF -> graviton -> HH

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m900_madgraph",
    id=14346388,
    processes=[procs.graviton_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=106_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m850_madgraph",
    id=14346601,
    processes=[procs.graviton_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m800_madgraph",
    id=14346568,
    processes=[procs.graviton_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m750_madgraph",
    id=14346412,
    processes=[procs.graviton_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m700_madgraph",
    id=14346469,
    processes=[procs.graviton_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m650_madgraph",
    id=14346723,
    processes=[procs.graviton_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m600_madgraph",
    id=14346637,
    processes=[procs.graviton_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m550_madgraph",
    id=14346640,
    processes=[procs.graviton_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=108_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m500_madgraph",
    id=14346606,
    processes=[procs.graviton_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=162_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m450_madgraph",
    id=14346556,
    processes=[procs.graviton_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=162_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m400_madgraph",
    id=14346409,
    processes=[procs.graviton_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=152_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m350_madgraph",
    id=14346554,
    processes=[procs.graviton_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=162_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m320_madgraph",
    id=14346528,
    processes=[procs.graviton_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=162_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m3000_madgraph",
    id=14346475,
    processes=[procs.graviton_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=52_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m300_madgraph",
    id=14346580,
    processes=[procs.graviton_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=162_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m280_madgraph",
    id=14346410,
    processes=[procs.graviton_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=216_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m270_madgraph",
    id=14346718,
    processes=[procs.graviton_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=216_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m260_madgraph",
    id=14346710,
    processes=[procs.graviton_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=216_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m250_madgraph",
    id=14346628,
    processes=[procs.graviton_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=216_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2500_madgraph",
    id=14346511,
    processes=[procs.graviton_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=52_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2000_madgraph",
    id=14346848,
    processes=[procs.graviton_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=54_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1750_madgraph",
    id=14347595,
    processes=[procs.graviton_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=54_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1500_madgraph",
    id=14346362,
    processes=[procs.graviton_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=54_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1250_madgraph",
    id=14346454,
    processes=[procs.graviton_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=54_000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1000_madgraph",
    id=14346419,
    processes=[procs.graviton_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=54_000,
)

# VBF -> radion -> HH

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m500_madgraph",
#     id=14311131,
#     processes=[procs.radion_hh_vbf_bbtautau_m500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=160000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m320_madgraph",
#     id=14310796,
#     processes=[procs.radion_hh_vbf_bbtautau_m320],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m400_madgraph",
#     id=14311092,
#     processes=[procs.radion_hh_vbf_bbtautau_m400],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=160000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m450_madgraph",
#     id=14310489,
#     processes=[procs.radion_hh_vbf_bbtautau_m450],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m650_madgraph",
#     id=14310467,
#     processes=[procs.radion_hh_vbf_bbtautau_m650],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m600_madgraph",
#     id=14309147,
#     processes=[procs.radion_hh_vbf_bbtautau_m600],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=104000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m260_madgraph",
#     id=14310633,
#     processes=[procs.radion_hh_vbf_bbtautau_m260],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m3000_madgraph",
#     id=14311354,
#     processes=[procs.radion_hh_vbf_bbtautau_m3000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=52000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m550_madgraph",
#     id=14310820,
#     processes=[procs.radion_hh_vbf_bbtautau_m550],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1500_madgraph",
#     id=14310564,
#     processes=[procs.radion_hh_vbf_bbtautau_m1500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m250_madgraph",
#     id=14311026,
#     processes=[procs.radion_hh_vbf_bbtautau_m250],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=210000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m800_madgraph",
#     id=14310585,
#     processes=[procs.radion_hh_vbf_bbtautau_m800],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m300_madgraph",
#     id=14309129,
#     processes=[procs.radion_hh_vbf_bbtautau_m300],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m350_madgraph",
#     id=14310922,
#     processes=[procs.radion_hh_vbf_bbtautau_m350],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m850_madgraph",
#     id=14311176,
#     processes=[procs.radion_hh_vbf_bbtautau_m850],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=106000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m280_madgraph",
#     id=14310610,
#     processes=[procs.radion_hh_vbf_bbtautau_m280],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1000_madgraph",
#     id=14311373,
#     processes=[procs.radion_hh_vbf_bbtautau_m1000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=52000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1750_madgraph",
#     id=14311180,
#     processes=[procs.radion_hh_vbf_bbtautau_m1750],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m2500_madgraph",
#     id=14309857,
#     processes=[procs.radion_hh_vbf_bbtautau_m2500],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=52000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m270_madgraph",
#     id=14311009,
#     processes=[procs.radion_hh_vbf_bbtautau_m270],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=214000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m900_madgraph",
#     id=14309240,
#     processes=[procs.radion_hh_vbf_bbtautau_m900],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=106000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m750_madgraph",
#     id=14309178,
#     processes=[procs.radion_hh_vbf_bbtautau_m750],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=106000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m2000_madgraph",
#     id=14310672,
#     processes=[procs.radion_hh_vbf_bbtautau_m2000],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m700_madgraph",
#     id=14311299,
#     processes=[procs.radion_hh_vbf_bbtautau_m700],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=106000,
# )

# cpn.add_dataset(
#     name="radion_hh_vbf_bbtautau_m1250_madgraph",
#     id=14309599,
#     processes=[procs.radion_hh_vbf_bbtautau_m1250],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )


# # VBF -> graviton -> HH

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m900_madgraph",
#     id=14309476,
#     processes=[procs.graviton_hh_vbf_bbtautau_m900],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m850_madgraph",
#     id=14309603,
#     processes=[procs.graviton_hh_vbf_bbtautau_m850],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m800_madgraph",
#     id=14311096,
#     processes=[procs.graviton_hh_vbf_bbtautau_m800],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=104000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m750_madgraph",
#     id=14310181,
#     processes=[procs.graviton_hh_vbf_bbtautau_m750],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=106000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m700_madgraph",
#     id=14309734,
#     processes=[procs.graviton_hh_vbf_bbtautau_m700],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m650_madgraph",
#     id=14309837,
#     processes=[procs.graviton_hh_vbf_bbtautau_m650],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m600_madgraph",
#     id=14310214,
#     processes=[procs.graviton_hh_vbf_bbtautau_m600],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m550_madgraph",
#     id=14309850,
#     processes=[procs.graviton_hh_vbf_bbtautau_m550],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=108000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m500_madgraph",
#     id=14309834,
#     processes=[procs.graviton_hh_vbf_bbtautau_m500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m450_madgraph",
#     id=14310948,
#     processes=[procs.graviton_hh_vbf_bbtautau_m450],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=160000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m400_madgraph",
#     id=14311043,
#     processes=[procs.graviton_hh_vbf_bbtautau_m400],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=158000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m350_madgraph",
#     id=14310464,
#     processes=[procs.graviton_hh_vbf_bbtautau_m350],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m320_madgraph",
#     id=14309870,
#     processes=[procs.graviton_hh_vbf_bbtautau_m320],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=160000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m3000_madgraph",
#     id=14309851,
#     processes=[procs.graviton_hh_vbf_bbtautau_m3000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m300_madgraph",
#     id=14310056,
#     processes=[procs.graviton_hh_vbf_bbtautau_m300],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=162000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m280_madgraph",
#     id=14310550,
#     processes=[procs.graviton_hh_vbf_bbtautau_m280],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=214000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m270_madgraph",
#     id=14309919,
#     processes=[procs.graviton_hh_vbf_bbtautau_m270],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=216000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m260_madgraph",
#     id=14311171,
#     processes=[procs.graviton_hh_vbf_bbtautau_m260],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=214000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m2500_madgraph",
#     id=14309744,
#     processes=[procs.graviton_hh_vbf_bbtautau_m2500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m250_madgraph",
#     id=14311070,
#     processes=[procs.graviton_hh_vbf_bbtautau_m250],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=214000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m2000_madgraph",
#     id=14309508,
#     processes=[procs.graviton_hh_vbf_bbtautau_m2000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1750_madgraph",
#     id=14309405,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1750],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1500_madgraph",
#     id=14309566,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1500],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1250_madgraph",
#     id=14309555,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1250],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )

# cpn.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m1000_madgraph",
#     id=14309686,
#     processes=[procs.graviton_hh_vbf_bbtautau_m1000],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=54000,
# )
