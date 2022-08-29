# coding: utf-8

"""
HH -> bbWW datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs

from cmsdb.campaigns import run2_2017

run2_2017.campaign_run2_2017.add_dataset(
    name="hh_ggf_kt_1_kl_0_bbww_sl_powheg",
    id=14057341,
    processes=[procs.hh_ggf_kt_1_kl_0_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=392598,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="hh_ggf_kt_1_kl_1_bbww_sl_powheg",
    id=14065482,
    processes=[procs.hh_ggf_kt_1_kl_1_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", # noqa
    ],
    n_files=24,
    n_events=399994,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="hh_ggf_kt_1_kl_2p45_bbww_sl_powheg",
    id=14066581,
    processes=[procs.hh_ggf_kt_1_kl_2p45_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=399996,
)

run2_2017.campaign_run2_2017.add_dataset(
    name="hh_ggf_kt_1_kl_5_bbww_sl_powheg",
    id=14058363,
    processes=[procs.hh_ggf_kt_1_kl_5_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=395996,
)
