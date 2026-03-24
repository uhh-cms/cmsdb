# coding: utf-8

"""
HH -> bbtautau datasets for the 2023 pre-BPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v13 import campaign_run3_2023_preBPix_nano_v13 as cpn

#
# ggf, HH -> bbtautau
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14961145,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v3/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=2665667,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=14966831,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-ggHH_powheg_bugfix_133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=296,
    n_events=2654123,
)
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=14966810,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv13-ggHH_powheg_bugfix_133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=217,
    n_events=2653047,
)

#
# vbf, HH -> bbtautau
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_madgraph",
    id=14961633,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2666667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=14965663,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=2645667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966905,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=2657667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14964861,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=2657667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14964962,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=2663667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14964547,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2654667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964528,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=2666667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14966454,
    processes=[procs.hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=2662667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964497,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=2666667,
)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14964408,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23NanoAODv13-133X_mcRun3_2023_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=2657667,
)
