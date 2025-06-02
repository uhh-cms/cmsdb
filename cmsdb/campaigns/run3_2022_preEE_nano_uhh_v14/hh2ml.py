# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14 import campaign_run3_2022_preEE_nano_uhh_v14 as cpn


#
# ggf -> HH -> 4tau
#

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl1_kt1_powheg",
    id=14857591,
    processes=[procs.hh_ggf_htt_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=230_000,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl0_kt1_powheg",
    id=15005190,
    processes=[procs.hh_ggf_htt_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_645,
    aux={
        "merging_factors": {
            "nominal": 55,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl5_kt1_powheg",
    id=15007970,
    processes=[procs.hh_ggf_htt_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=215_929,
    aux={
        "merging_factors": {
            "nominal": 66,
        },
    },
)

#
# ggf -> HH -> 4v
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl1_kt1_powheg",
    id=14857198,
    processes=[procs.hh_ggf_hvv_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
        "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1 + 5,
    n_events=454_270 + 1_817_666,
    aux={
        "merging_factors": {
            "nominal": 86,
            "nominal_ext1": 39,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl0_kt1_powheg",
    id=15004943,
    processes=[procs.hh_ggf_hvv_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=438_027,
    aux={
        "merging_factors": {
            "nominal": 74,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl5_kt1_powheg",
    id=15001952,
    processes=[procs.hh_ggf_hvv_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_553_819,
    aux={
        "merging_factors": {
            "nominal": 39,
        },
    },
)

#
# ggf -> HH -> 2tau2v
#

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl1_kt1_powheg",
    id=14868338,
    processes=[procs.hh_ggf_htt_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=344_531,
    aux={
        "merging_factors": {
            "nominal": 43,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl0_kt1_powheg",
    id=15005250,
    processes=[procs.hh_ggf_htt_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=328_456,
    aux={
        "merging_factors": {
            "nominal": 42,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl5_kt1_powheg",
    id=15007752,
    processes=[procs.hh_ggf_htt_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=327_109,
    aux={
        "merging_factors": {
            "nominal": 33,
        },
    },
)

#
# vbf -> HH -> 4tau qq
#

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1_madgraph",
    id=14791984,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=394_344,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1_madgraph",
    id=14810912,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400_000,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14878521,
    processes=[procs.hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4Tau_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14879641,
    processes=[procs.hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4Tau_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=86_600,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14878382,
    processes=[procs.hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4Tau_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877534,
    processes=[procs.hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4Tau_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878543,
    processes=[procs.hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4Tau_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=86_800,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14879007,
    processes=[procs.hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4Tau_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_295,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14965535,
    processes=[procs.hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4Tau_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=86_610,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14878379,
    processes=[procs.hh_vbf_htt_htt_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4Tau_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

#
# vbf -> HH -> 4v qq
#

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1_madgraph",
    id=14792163,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=388_164,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1_madgraph",
    id=14793914,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_275,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14878484,
    processes=[procs.hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_301,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14878564,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=262_619,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14877669,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=262_558,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877681,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_998,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14877136,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_996,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14876429,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_294,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14961135,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_998,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14878719,
    processes=[procs.hh_vbf_hvv_hvv_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=261_885,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

#
# vbf -> HH -> 2tau2v qq
#

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1_madgraph",
    id=14801283,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=788_355,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1_madgraph",
    id=14791435,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=782_013,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14879590,
    processes=[procs.hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2Tau2V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=174_581,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14876204,
    processes=[procs.hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2Tau2V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=175_298,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14878639,
    processes=[procs.hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2Tau2V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=175_292,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14878404,
    processes=[procs.hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2Tau2V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=172_524,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878475,
    processes=[procs.hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2Tau2V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=174_623,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14876209,
    processes=[procs.hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2Tau2V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=175_996,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14961057,
    processes=[procs.hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2Tau2V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=175_998,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14877315,
    processes=[procs.hh_vbf_htt_hvv_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2Tau2V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=175_288,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)
