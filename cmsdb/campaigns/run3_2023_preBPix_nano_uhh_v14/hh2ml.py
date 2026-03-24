# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn


#
# ggf -> HH -> 4tau
#

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl1_kt1_powheg",
    id=14960936,
    processes=[procs.hh_ggf_htt_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_987,
    aux={
        "merging_factors": {
            "nominal": 41,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl0_kt1_powheg",
    id=14961266,
    processes=[procs.hh_ggf_htt_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=664_607,
    aux={
        "merging_factors": {
            "nominal": 72,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl5_kt1_powheg",
    id=14961399,
    processes=[procs.hh_ggf_htt_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=662_792,
    aux={
        "merging_factors": {
            "nominal": 86,
        },
    },
)

#
# ggf -> HH -> 4v
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl1_kt1_powheg",
    id=14952310,
    processes=[procs.hh_ggf_hvv_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_330_572,
    aux={
        "merging_factors": {
            "nominal": 49,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl0_kt1_powheg",
    id=14961420,
    processes=[procs.hh_ggf_hvv_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_329_675,
    aux={
        "merging_factors": {
            "nominal": 106,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl5_kt1_powheg",
    id=14961406,
    processes=[procs.hh_ggf_hvv_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_328_318,
    aux={
        "merging_factors": {
            "nominal": 82,
        },
    },
)

#
# ggf -> HH -> 2tau2v
#

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl1_kt1_powheg",
    id=14959876,
    processes=[procs.hh_ggf_htt_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=993_043,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl0_kt1_powheg",
    id=14960873,
    processes=[procs.hh_ggf_htt_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=990_548,
    aux={
        "merging_factors": {
            "nominal": 77,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl5_kt1_powheg",
    id=14961465,
    processes=[procs.hh_ggf_htt_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=996_603,
    aux={
        "merging_factors": {
            "nominal": 88,
        },
    },
)

#
# vbf -> HH -> 4tau qq
#

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1_madgraph",
    id=14965121,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=662_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1_madgraph",
    id=14961676,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_667,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14967201,
    processes=[procs.hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=650_667,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964323,
    processes=[procs.hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_667,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14966282,
    processes=[procs.hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_667,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14966897,
    processes=[procs.hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_667,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14965208,
    processes=[procs.hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_667,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14966212,
    processes=[procs.hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=662_667,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14966393,
    processes=[procs.hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_667,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14966401,
    processes=[procs.hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4Tau_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_667,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

#
# vbf -> HH -> 4v qq
#

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1_madgraph",
    id=14961521,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_333_326,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1_madgraph",
    id=14961101,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_333_324,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14966796,
    processes=[procs.hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_291_328,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14964806,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_327_321,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14966397,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_321_325,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14964796,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_333_326,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14964537,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_333_327,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14967496,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_333_324,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14966382,
    processes=[procs.hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_324_320,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

#
# vbf -> HH -> 2tau2v qq
#

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1_madgraph",
    id=14963889,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=975_988,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1_madgraph",
    id=14962117,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=996_989,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14964046,
    processes=[procs.hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2Tau2V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_976,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14965559,
    processes=[procs.hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2Tau2V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_981,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14964252,
    processes=[procs.hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2Tau2V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_985,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14964584,
    processes=[procs.hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=996_976,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14968167,
    processes=[procs.hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=990_976,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14966843,
    processes=[procs.hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_985,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14966806,
    processes=[procs.hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2Tau2V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=984_987,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)
