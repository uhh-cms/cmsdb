# coding: utf-8

"""
HH -> bbtautau datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14961129,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_665_667,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=14966800,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-ggHH_powheg_bugfix_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_653_047,
    aux={
        "merging_factors": {
            "nominal": 46,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=14940579,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2_860_485,
    aux={
        "merging_factors": {
            "nominal": 43,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=14966812,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-ggHH_powheg_bugfix_130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_654_347,
    aux={
        "merging_factors": {
            "nominal": 59,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p1_powheg",
    id=14930912,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=990_960,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=14931211,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=998_174,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=14930639,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=990_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=14930972,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=990_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_c21_powheg",
    id=14931201,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1_c21],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=994_000,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=15376360,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_641_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

# TODO: k2v0 sample still being centrally processed

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15376486,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_631_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15376445,
    processes=[procs.hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_CV_2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_631_667,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15376474,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2_626_667,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15376345,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2_626_667,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15376510,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_646_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15376502,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2_656_667,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15376430,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=2_656_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15377642,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=2_651_667,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

# privately produced datasets (note the "prv" flag)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_prv_madgraph",
    id=22761201,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_988_500,
    aux={
        "merging_factors": {
            "nominal": 796,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_prv_madgraph",
    id=22761202,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=1_982_000,
    aux={
        "merging_factors": {
            "nominal": 661,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_prv_madgraph",
    id=22761203,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_991_500,
    aux={
        "merging_factors": {
            "nominal": 797,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_prv_madgraph",
    id=22761204,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=1_996_000,
    aux={
        "merging_factors": {
            "nominal": 666,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_prv_madgraph",
    id=22761205,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_994_500,
    aux={
        "merging_factors": {
            "nominal": 798,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_prv_madgraph",
    id=22761206,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=1_999_500,
    aux={
        "merging_factors": {
            "nominal": 667,
        },
        "private": True,
    },
)

#
# ggf -> graviton -> HH
#

# tba

#
# ggf -> radion -> HH
#

# tba
