# coding: utf-8

"""
HH -> bbVV datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=14961400,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=661_694,
    aux={
        "merging_factors": {
            "nominal": 73,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl1_kt1_powheg",
    id=14961348,
    processes=[procs.hh_ggf_hbb_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_665,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=14940643,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_192_340,
    aux={
        "merging_factors": {
            "nominal": 61,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=14960677,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_764,
    aux={
        "merging_factors": {
            "nominal": 74,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=14963911,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_667,
    aux={
        "merging_factors": {
            "nominal": 62,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl1_kt1_powheg",
    id=14961107,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_483,
    aux={
        "merging_factors": {
            "nominal": 37,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=14932680,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=299_375,
    aux={
        "merging_factors": {
            "nominal": 71,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=14964738,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=265_999,
    aux={
        "merging_factors": {
            "nominal": 41,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=14965393,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=261_556,
    aux={
        "merging_factors": {
            "nominal": 45,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=14960636,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_489,
    aux={
        "merging_factors": {
            "nominal": 56,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=14940820,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=299_199,
    aux={
        "merging_factors": {
            "nominal": 48,
        },
    },
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=14961727,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_232,
    aux={
        "merging_factors": {
            "nominal": 45,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v0_kl1_madgraph",
    id=14961134,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_664,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v1_kl1_madgraph",
    id=14964018,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=660_666,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14966808,
    processes=[procs.hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2V_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=648_665,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964326,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2V_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_663,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14964513,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2V_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=660_664,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14967713,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2V_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=651_662,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966837,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2V_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_664,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14965344,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2V_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_662,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964511,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2V_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=666_663,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966434,
    processes=[procs.hh_vbf_hbb_hvv_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2V_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=663_665,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1_madgraph",
    id=14964661,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_666,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1_madgraph",
    id=14965470,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=260_666,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14967619,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_666,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14964871,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_667,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14962861,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=260_666,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14967622,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_666,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966286,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_666,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14964577,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_666,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14968357,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_667,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966238,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_666,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1_madgraph",
    id=14964333,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_663,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1_madgraph",
    id=14963812,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_665,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14968350,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_663,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14966289,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_661,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14961034,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=260_665,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14966265,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_664,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14966379,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_664,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14966838,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_663,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964445,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=266_663,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm2p12_k2v3p87_klm5p96_madgraph",
    id=14966353,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_m2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=263_665,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)
