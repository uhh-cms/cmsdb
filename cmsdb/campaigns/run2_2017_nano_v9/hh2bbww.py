# coding: utf-8

"""
HH -> bbWW datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn

#
# ggf, single lepton
#

cpn.add_dataset(
    name="ggHH_kl_0_kt_1_sl_hbbhvv_powheg",
    id=14057341,
    processes=[procs.ggHH_kl_0_kt_1_sl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=392598,
)

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_sl_hbbhvv_powheg",
    id=14065482,
    processes=[procs.ggHH_kl_1_kt_1_sl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", # noqa
    ],
    n_files=24,
    n_events=399994,
)

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_sl_hbbhvv_powheg",
    id=14066581,
    processes=[procs.ggHH_kl_2p45_kt_1_sl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=399996,
)

cpn.add_dataset(
    name="ggHH_kl_5_kt_1_sl_hbbhvv_powheg",
    id=14058363,
    processes=[procs.ggHH_kl_5_kt_1_sl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=395996,
)

#
# ggf, dilepton
#

cpn.add_dataset(
    name="ggHH_kl_0_kt_1_dl_hbbhvv_powheg",
    id=14062942,
    processes=[procs.ggHH_kl_0_kt_1_dl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VTo2L2Nu_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=400000,
)

cpn.add_dataset(
    name="ggHH_kl_1_kt_1_dl_hbbhvv_powheg",
    id=14057872,
    processes=[procs.ggHH_kl_1_kt_1_dl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VTo2L2Nu_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=395000,
)

cpn.add_dataset(
    name="ggHH_kl_2p45_kt_1_dl_hbbhvv_powheg",
    id=14057488,
    processes=[procs.ggHH_kl_2p45_kt_1_dl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VTo2L2Nu_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=397398,
)

cpn.add_dataset(
    name="ggHH_kl_5_kt_1_dl_hbbhvv_powheg",
    id=14067172,
    processes=[procs.ggHH_kl_5_kt_1_dl_hbbhvv],
    keys=[
        "/GluGluToHHTo2B2VTo2L2Nu_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=399999,
)

#
# VBF (dipoleRecoilOff), single lepton
#

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_1_sl_hbbhvv_madgraph",
    id=14152276,
    processes=[procs.qqHH_CV_1_C2V_1_kl_1_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=396993,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_0_sl_hbbhvv_madgraph",
    id=14153107,
    processes=[procs.qqHH_CV_1_C2V_1_kl_0_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=389995,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_2_sl_hbbhvv_madgraph",
    id=14152113,
    processes=[procs.qqHH_CV_1_C2V_1_kl_2_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=399997,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_0_kl_1_sl_hbbhvv_madgraph",
    id=14154259,
    processes=[procs.qqHH_CV_1_C2V_0_kl_1_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=399993,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_2_kl_1_sl_hbbhvv_madgraph",
    id=14149758,
    processes=[procs.qqHH_CV_1_C2V_2_kl_1_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=399997,
)

cpn.add_dataset(
    name="qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhvv_madgraph",
    id=14151042,
    processes=[procs.qqHH_CV_0p5_C2V_1_kl_1_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=399998,
)

cpn.add_dataset(
    name="qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhvv_madgraph",
    id=14149171,
    processes=[procs.qqHH_CV_1p5_C2V_1_kl_1_sl_hbbhvv],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399998,
)

#
# VBF (dipoleRecoilOff), dilepton
#

cpn.add_dataset(
    name="qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv_madgraph",
    id=14154110,
    processes=[procs.qqHH_CV_0p5_C2V_1_kl_1_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=396000,
)

cpn.add_dataset(
    name="qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv_madgraph",
    id=14151539,
    processes=[procs.qqHH_CV_1p5_C2V_1_kl_1_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=399999,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv_madgraph",
    id=14153811,
    processes=[procs.qqHH_CV_1_C2V_0_kl_1_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=395998,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv_madgraph",
    id=14151850,
    processes=[procs.qqHH_CV_1_C2V_1_kl_0_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=400000,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv_madgraph",
    id=14159390,
    processes=[procs.qqHH_CV_1_C2V_1_kl_1_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=395998,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv_madgraph",
    id=14149920,
    processes=[procs.qqHH_CV_1_C2V_1_kl_2_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)

cpn.add_dataset(
    name="qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv_madgraph",
    id=14153964,
    processes=[procs.qqHH_CV_1_C2V_2_kl_1_dl_hbbhvv],
    keys=[
        "/VBFHHTo2B2VTo2L2Nu_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=397998,
)

#
# Resonant samples
#

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m400_madgraph",
    id=14141149,
    processes=[procs.graviton_hh_ggf_bbww_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=299996,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m800_madgraph",
    id=14146771,
    processes=[procs.graviton_hh_ggf_bbww_m800],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=199999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m600_madgraph",
    id=14140368,
    processes=[procs.graviton_hh_ggf_bbww_m600],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=192000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m500_madgraph",
    id=14140884,
    processes=[procs.graviton_hh_ggf_bbww_m500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=300000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m250_madgraph",
    id=14144191,
    processes=[procs.graviton_hh_ggf_bbww_m250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=399998,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m320_madgraph",
    id=14140657,
    processes=[procs.graviton_hh_ggf_bbww_m320],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=289997,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m2500_madgraph",
    id=14140814,
    processes=[procs.graviton_hh_ggf_bbww_m2500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=99999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m260_madgraph",
    id=14141489,
    processes=[procs.graviton_hh_ggf_bbww_m260],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=384999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m700_madgraph",
    id=14140370,
    processes=[procs.graviton_hh_ggf_bbww_m700],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=199999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m550_madgraph",
    id=14140970,
    processes=[procs.graviton_hh_ggf_bbww_m550],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=299996,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m900_madgraph",
    id=14145330,
    processes=[procs.graviton_hh_ggf_bbww_m900],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=199999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m1500_madgraph",
    id=14140770,
    processes=[procs.graviton_hh_ggf_bbww_m1500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=100000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m750_madgraph",
    id=14147643,
    processes=[procs.graviton_hh_ggf_bbww_m750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=177999,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m2000_madgraph",
    id=14140836,
    processes=[procs.graviton_hh_ggf_bbww_m2000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=99998,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m300_madgraph",
    id=14141018,
    processes=[procs.graviton_hh_ggf_bbww_m300],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=299994,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m3000_madgraph",
    id=14157072,
    processes=[procs.graviton_hh_ggf_bbww_m3000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=68000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m850_madgraph",
    id=14143798,
    processes=[procs.graviton_hh_ggf_bbww_m850],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=199998,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m1250_madgraph",
    id=14140775,
    processes=[procs.graviton_hh_ggf_bbww_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=94998,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m270_madgraph",
    id=14145802,
    processes=[procs.graviton_hh_ggf_bbww_m270],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=399990,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m450_madgraph",
    id=14140497,
    processes=[procs.graviton_hh_ggf_bbww_m450],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=299996,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m1750_madgraph",
    id=14140772,
    processes=[procs.graviton_hh_ggf_bbww_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=99997,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m280_madgraph",
    id=14147581,
    processes=[procs.graviton_hh_ggf_bbww_m280],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=375997,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m650_madgraph",
    id=14140762,
    processes=[procs.graviton_hh_ggf_bbww_m650],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=200000,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m350_madgraph",
    id=14141675,
    processes=[procs.graviton_hh_ggf_bbww_m350],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=299994,
)

cpn.add_dataset(
    name="graviton_hh_ggf_bbww_m1000_madgraph",
    id=14144107,
    processes=[procs.graviton_hh_ggf_bbww_m1000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=99999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m350_madgraph",
    id=14140927,
    processes=[procs.radion_hh_ggf_bbww_m350],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=299995,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m1250_madgraph",
    id=14147471,
    processes=[procs.radion_hh_ggf_bbww_m1250],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=99998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m400_madgraph",
    id=14141152,
    processes=[procs.radion_hh_ggf_bbww_m400],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=300000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m250_madgraph",
    id=14140693,
    processes=[procs.radion_hh_ggf_bbww_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=399996,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m300_madgraph",
    id=14140668,
    processes=[procs.radion_hh_ggf_bbww_m300],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=293999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m270_madgraph",
    id=14140465,
    processes=[procs.radion_hh_ggf_bbww_m270],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=391999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m450_madgraph",
    id=14141645,
    processes=[procs.radion_hh_ggf_bbww_m450],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=299996,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m1000_madgraph",
    id=14140705,
    processes=[procs.radion_hh_ggf_bbww_m1000],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=99999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m900_madgraph",
    id=14145815,
    processes=[procs.radion_hh_ggf_bbww_m900],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=200000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m550_madgraph",
    id=14141875,
    processes=[procs.radion_hh_ggf_bbww_m550],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=287997,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m600_madgraph",
    id=14156241,
    processes=[procs.radion_hh_ggf_bbww_m600],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=199997,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m850_madgraph",
    id=14147559,
    processes=[procs.radion_hh_ggf_bbww_m850],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=175998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m500_madgraph",
    id=14140725,
    processes=[procs.radion_hh_ggf_bbww_m500],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=294999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m1750_madgraph",
    id=14143952,
    processes=[procs.radion_hh_ggf_bbww_m1750],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m700_madgraph",
    id=14140979,
    processes=[procs.radion_hh_ggf_bbww_m700],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=199995,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m260_madgraph",
    id=14140581,
    processes=[procs.radion_hh_ggf_bbww_m260],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=399998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m280_madgraph",
    id=14141238,
    processes=[procs.radion_hh_ggf_bbww_m280],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=399997,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m650_madgraph",
    id=14140943,
    processes=[procs.radion_hh_ggf_bbww_m650],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=189998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m320_madgraph",
    id=14140496,
    processes=[procs.radion_hh_ggf_bbww_m320],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=299999,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m750_madgraph",
    id=14140571,
    processes=[procs.radion_hh_ggf_bbww_m750],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=199998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m3000_madgraph",
    id=14140651,
    processes=[procs.radion_hh_ggf_bbww_m3000],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=99997,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m800_madgraph",
    id=14141876,
    processes=[procs.radion_hh_ggf_bbww_m800],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=199998,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m2000_madgraph",
    id=14140335,
    processes=[procs.radion_hh_ggf_bbww_m2000],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m2500_madgraph",
    id=14141423,
    processes=[procs.radion_hh_ggf_bbww_m2500],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

cpn.add_dataset(
    name="radion_hh_ggf_bbww_m1500_madgraph",
    id=14140358,
    processes=[procs.radion_hh_ggf_bbww_m1500],
    keys=[
        "/GluGluToRadionToHHTo2B2WToLNu2J_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=100000,
)
