# coding: utf-8

"""
HH -> bbWW datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn

#
# ggf
#

cpn.add_dataset(
    name="hh_ggf_kt_1_kl_0_bbww_sl_powheg",
    id=14057341,
    processes=[procs.hh_ggf_kt_1_kl_0_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=392598,
)

cpn.add_dataset(
    name="hh_ggf_kt_1_kl_1_bbww_sl_powheg",
    id=14065482,
    processes=[procs.hh_ggf_kt_1_kl_1_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM", # noqa
    ],
    n_files=24,
    n_events=399994,
)

cpn.add_dataset(
    name="hh_ggf_kt_1_kl_2p45_bbww_sl_powheg",
    id=14066581,
    processes=[procs.hh_ggf_kt_1_kl_2p45_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=399996,
)

cpn.add_dataset(
    name="hh_ggf_kt_1_kl_5_bbww_sl_powheg",
    id=14058363,
    processes=[procs.hh_ggf_kt_1_kl_5_bbww_sl],
    keys=[
        "/GluGluToHHTo2B2VLNu2J_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=395996,
)

#
# VBF (dipoleRecoilOff)
#

cpn.add_dataset(
    name="hh_vbf_cv_0p5_c2v_1_c3_1_bbww_sl_powheg",
    id=14151042,
    processes=[procs.hh_vbf_cv_0p5_c2v_1_c3_1_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=399998,
)

cpn.add_dataset(
    name="hh_vbf_cv_1p5_c2v_1_c3_1_bbww_sl_powheg",
    id=14149171,
    processes=[procs.hh_vbf_cv_1p5_c2v_1_c3_1_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399998,
)

cpn.add_dataset(
    name="hh_vbf_cv_1_c2v_0_c3_1_bbww_sl_powheg",
    id=14154259,
    processes=[procs.hh_vbf_cv_1_c2v_0_c3_1_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=399993,
)

cpn.add_dataset(
    name="hh_vbf_cv_1_c2v_1_c3_0_bbww_sl_powheg",
    id=14153107,
    processes=[procs.hh_vbf_cv_1_c2v_1_c3_0_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=389995,
)

cpn.add_dataset(
    name="hh_vbf_cv_1_c2v_1_c3_1_bbww_sl_powheg",
    id=14152276,
    processes=[procs.hh_vbf_cv_1_c2v_1_c3_1_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=396993,
)

cpn.add_dataset(
    name="hh_vbf_cv_1_c2v_1_c3_2_bbww_sl_powheg",
    id=14152113,
    processes=[procs.hh_vbf_cv_1_c2v_1_c3_2_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=399997,
)

cpn.add_dataset(
    name="hh_vbf_cv_1_c2v_2_c3_1_bbww_sl_powheg",
    id=14149758,
    processes=[procs.hh_vbf_cv_1_c2v_2_c3_1_bbww_sl],
    keys=[
        "/VBFHHTo2B2WToLNu2J_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=399997,
)
