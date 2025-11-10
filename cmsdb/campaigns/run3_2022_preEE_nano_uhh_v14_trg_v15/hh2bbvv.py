# coding: utf-8

"""
HH -> bbVV datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15 import campaign_run3_2022_preEE_nano_uhh_v14_trg_v15 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=15005094,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_594,
    aux={
        "merging_factors": {
            "nominal": 35,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl1_kt1_powheg",
    id=14863904,
    processes=[procs.hh_ggf_hbb_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=229_178,
    aux={
        "merging_factors": {
            "nominal": 50,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=14953160,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=398_014,
    aux={
        "merging_factors": {
            "nominal": 111,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=15005189,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_487,
    aux={
        "merging_factors": {
            "nominal": 40,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=15005093,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl1_kt1_powheg",
    id=14843883,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=91_700,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=14952639,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=99_913,
    aux={
        "merging_factors": {
            "nominal": 46,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=15001978,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_544,
    aux={
        "merging_factors": {
            "nominal": 34,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=15006240,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=86_758,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=14868357,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=91_699,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=14953155,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=99_103,
    aux={
        "merging_factors": {
            "nominal": 38,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=15006631,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_595,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14877312,
    processes=[procs.hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_300,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14876249,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_999,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14877934,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_307,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877520,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=220_000,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878394,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=217_965,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14877525,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=215_824,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14965307,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_317,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14878390,
    processes=[procs.hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=219_289,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v0_kl1_madgraph",
    id=14861695,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=995_923,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v1_kl1_madgraph",
    id=14868430,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=997_227,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14876166,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399_999,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14877648,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=398_627,
    aux={
        "merging_factors": {
            "nominal": 29,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14879110,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_845,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14878409,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399_995,
    aux={
        "merging_factors": {
            "nominal": 38,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878358,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=396_574,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14877851,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_200,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14960980,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_999,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14877654,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399_998,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1_madgraph",
    id=14791641,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_727,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1_madgraph",
    id=14790732,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=390_211,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14878357,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_210,
    aux={
        "merging_factors": {
            "nominal": 33,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14878908,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_777,
    aux={
        "merging_factors": {
            "nominal": 31,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14875920,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=381_664,
    aux={
        "merging_factors": {
            "nominal": 29,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877650,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_909,
    aux={
        "merging_factors": {
            "nominal": 31,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878393,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_851,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14875615,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=398_680,
    aux={
        "merging_factors": {
            "nominal": 31,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964627,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_280,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14877660,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=399_286,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1_madgraph",
    id=14793259,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=397_940,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1_madgraph",
    id=14791562,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=392_767,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)
