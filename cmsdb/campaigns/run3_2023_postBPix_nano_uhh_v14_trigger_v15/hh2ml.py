# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn


#
# ggf -> HH -> 4tau
#

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl1_kt1_powheg",
    id=14960792,
    processes=[procs.hh_ggf_htt_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=332_033,
    aux={
        "merging_factors": {
            "nominal": 64,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl0_kt1_powheg",
    id=14961265,
    processes=[procs.hh_ggf_htt_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_050,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl5_kt1_powheg",
    id=14962331,
    processes=[procs.hh_ggf_htt_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto4Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_006,
    aux={
        "merging_factors": {
            "nominal": 69,
        },
    },
)

#
# ggf -> HH -> 4v
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl1_kt1_powheg",
    id=14959459,
    processes=[procs.hh_ggf_hvv_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
        "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 7,
    n_events=665_890 + 2_655_432,
    aux={
        "merging_factors": {
            "nominal": 34,
            "nominal_ext1": 22,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl0_kt1_powheg",
    id=14962159,
    processes=[procs.hh_ggf_hvv_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=659_979,
    aux={
        "merging_factors": {
            "nominal": 50,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_kl5_kt1_powheg",
    id=14961093,
    processes=[procs.hh_ggf_hvv_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto4V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_661,
    aux={
        "merging_factors": {
            "nominal": 52,
        },
    },
)

#
# ggf -> HH -> 2tau2v
#

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl1_kt1_powheg",
    id=14960926,
    processes=[procs.hh_ggf_htt_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=499_411,
    aux={
        "merging_factors": {
            "nominal": 44,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl0_kt1_powheg",
    id=14961386,
    processes=[procs.hh_ggf_htt_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=492_697,
    aux={
        "merging_factors": {
            "nominal": 142,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl5_kt1_powheg",
    id=14965652,
    processes=[procs.hh_ggf_htt_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=478_378,
    aux={
        "merging_factors": {
            "nominal": 114,
        },
    },
)

#
# vbf -> HH -> 4tau qq
#

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1_madgraph",
    id=14962045,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1_madgraph",
    id=14964852,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14965459,
    processes=[procs.hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14961515,
    processes=[procs.hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14965542,
    processes=[procs.hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14961963,
    processes=[procs.hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=330_333,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14965505,
    processes=[procs.hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14963884,
    processes=[procs.hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=324_333,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964557,
    processes=[procs.hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=330_333,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14962114,
    processes=[procs.hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4Tau_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=333_333,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

#
# vbf -> HH -> 4v qq
#

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1_madgraph",
    id=14964552,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_663,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1_madgraph",
    id=14964786,
    processes=[procs.hh_vbf_hvv_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=660_662,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14963908,
    processes=[procs.hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=667_364,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14961687,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_664,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14962840,
    processes=[procs.hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_666,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14961097,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_657,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14962671,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=660_660,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14966403,
    processes=[procs.hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=648_662,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14961385,
    processes=[procs.hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_666,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

#
# vbf -> HH -> 2tau2v qq
#

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1_madgraph",
    id=14965141,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=499_996,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1_madgraph",
    id=14965678,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2Tau2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=496_996,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14965606,
    processes=[procs.hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2Tau2V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=496_997,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14964865,
    processes=[procs.hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2Tau2V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=496_994,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14967111,
    processes=[procs.hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2Tau2V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=490_995,
    aux={
        "merging_factors": {
            "nominal": 31,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14963913,
    processes=[procs.hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=499_991,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14964504,
    processes=[procs.hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=499_990,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964034,
    processes=[procs.hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2Tau2V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=481_998,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14963039,
    processes=[procs.hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2Tau2V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=487_992,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)
