# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14 import campaign_run3_2022_preEE_nano_uhh_v14 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14875846,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=913_840,
    aux={
        "merging_factors": {
            "nominal": 59,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=15006763,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-ggHH_powheg_bugfix_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=870_340,
    aux={
        "merging_factors": {
            "nominal": 62,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=14953035,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=891_890,
    aux={
        "merging_factors": {
            "nominal": 36,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=15004257,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-ggHH_powheg_bugfix_130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=877_968,
    aux={
        "merging_factors": {
            "nominal": 43,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_c21_powheg",
    id=14802513,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1_c21],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-1p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=98_902,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p10_powheg",
    id=14808587,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p10],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p10_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=98_551,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=14802756,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p35_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=98_705,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=14800332,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-3p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=14797893,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-m2p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=100_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=15376348,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=991_000,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_madgraph",
    id=15375971,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=998_000,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15377293,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=998_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15378006,
    processes=[procs.hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_CV_2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15377652,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15377996,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15377922,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15378003,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15377919,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15377649,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

# privately produced datasets (note the "prv" flag)
cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_prv_madgraph",
    id=22761001,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=980_000,
    aux={
        "merging_factors": {
            "nominal": 654,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_prv_madgraph",
    id=22761002,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_055_000,
    aux={
        "merging_factors": {
            "nominal": 704,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_prv_madgraph",
    id=22761003,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_040_500,
    aux={
        "merging_factors": {
            "nominal": 694,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_prv_madgraph",
    id=22761004,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=976_000,
    aux={
        "merging_factors": {
            "nominal": 651,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_prv_madgraph",
    id=22761005,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=986_500,
    aux={
        "merging_factors": {
            "nominal": 658,
        },
        "private": True,
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_prv_madgraph",
    id=22761006,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4UHH_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=980_000,
    aux={
        "merging_factors": {
            "nominal": 654,
        },
        "private": True,
    },
)

#
# ggf -> graviton -> HH
#

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m250_madgraph",
    id=14856827,
    processes=[procs.graviton_hh_ggf_hbb_htt_m250],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-250_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m260_madgraph",
    id=14873688,
    processes=[procs.graviton_hh_ggf_hbb_htt_m260],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-260_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=84_490,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m270_madgraph",
    id=14858113,
    processes=[procs.graviton_hh_ggf_hbb_htt_m270],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-270_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m280_madgraph",
    id=14867634,
    processes=[procs.graviton_hh_ggf_hbb_htt_m280],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-280_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m300_madgraph",
    id=14867934,
    processes=[procs.graviton_hh_ggf_hbb_htt_m300],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-300_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_304,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m350_madgraph",
    id=14868051,
    processes=[procs.graviton_hh_ggf_hbb_htt_m350],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-350_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_303,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m450_madgraph",
    id=14857139,
    processes=[procs.graviton_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-450_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m550_madgraph",
    id=14875152,
    processes=[procs.graviton_hh_ggf_hbb_htt_m550],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-550_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_312,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m600_madgraph",
    id=14858155,
    processes=[procs.graviton_hh_ggf_hbb_htt_m600],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-600_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m650_madgraph",
    id=14856595,
    processes=[procs.graviton_hh_ggf_hbb_htt_m650],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-650_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m700_madgraph",
    id=14872537,
    processes=[procs.graviton_hh_ggf_hbb_htt_m700],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-700_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_310,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m800_madgraph",
    id=14856808,
    processes=[procs.graviton_hh_ggf_hbb_htt_m800],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-800_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1000_madgraph",
    id=14854546,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1000],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1200_madgraph",
    id=14872343,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1200],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1200_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=21_332,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1400_madgraph",
    id=14856666,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1400],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1400_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1600_madgraph",
    id=14856941,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1600],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1600_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1800_madgraph",
    id=14858127,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1800],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1800_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 5,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m2000_madgraph",
    id=14854608,
    processes=[procs.graviton_hh_ggf_hbb_htt_m2000],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-2000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m2500_madgraph",
    id=14865095,
    processes=[procs.graviton_hh_ggf_hbb_htt_m2500],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-2500_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m3000_madgraph",
    id=14858129,
    processes=[procs.graviton_hh_ggf_hbb_htt_m3000],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-3000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m4000_madgraph",
    id=14885096,
    processes=[procs.graviton_hh_ggf_hbb_htt_m4000],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-4000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=21_342,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m5000_madgraph",
    id=14857131,
    processes=[procs.graviton_hh_ggf_hbb_htt_m5000],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-5000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

#
# ggf -> radion -> HH
#

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m250_madgraph",
    id=14857343,
    processes=[procs.radion_hh_ggf_hbb_htt_m250],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-250_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=85_196,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m260_madgraph",
    id=14856713,
    processes=[procs.radion_hh_ggf_hbb_htt_m260],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-260_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_279,
    aux={
        "merging_factors": {
            "nominal": 6,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m270_madgraph",
    id=14865091,
    processes=[procs.radion_hh_ggf_hbb_htt_m270],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-270_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=87_298,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m280_madgraph",
    id=14853129,
    processes=[procs.radion_hh_ggf_hbb_htt_m280],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-280_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m300_madgraph",
    id=14856618,
    processes=[procs.radion_hh_ggf_hbb_htt_m300],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-300_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 5,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m350_madgraph",
    id=14865104,
    processes=[procs.radion_hh_ggf_hbb_htt_m350],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-350_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m450_madgraph",
    id=14856872,
    processes=[procs.radion_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-450_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m550_madgraph",
    id=14852999,
    processes=[procs.radion_hh_ggf_hbb_htt_m550],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-550_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=85_915,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m600_madgraph",
    id=14857113,
    processes=[procs.radion_hh_ggf_hbb_htt_m600],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-600_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 5,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m650_madgraph",
    id=14856968,
    processes=[procs.radion_hh_ggf_hbb_htt_m650],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-650_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 5,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m700_madgraph",
    id=14855971,
    processes=[procs.radion_hh_ggf_hbb_htt_m700],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-700_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 6,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m800_madgraph",
    id=14856917,
    processes=[procs.radion_hh_ggf_hbb_htt_m800],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-800_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1000_madgraph",
    id=14856932,
    processes=[procs.radion_hh_ggf_hbb_htt_m1000],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=88_000,
    aux={
        "merging_factors": {
            "nominal": 6,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1200_madgraph",
    id=14856857,
    processes=[procs.radion_hh_ggf_hbb_htt_m1200],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1200_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 3,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1400_madgraph",
    id=14856881,
    processes=[procs.radion_hh_ggf_hbb_htt_m1400],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1400_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1600_madgraph",
    id=14872393,
    processes=[procs.radion_hh_ggf_hbb_htt_m1600],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1600_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=21_345,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1800_madgraph",
    id=14856885,
    processes=[procs.radion_hh_ggf_hbb_htt_m1800],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1800_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 2,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m2000_madgraph",
    id=14854659,
    processes=[procs.radion_hh_ggf_hbb_htt_m2000],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-2000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m2500_madgraph",
    id=14874111,
    processes=[procs.radion_hh_ggf_hbb_htt_m2500],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-2500_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m3000_madgraph",
    id=14874977,
    processes=[procs.radion_hh_ggf_hbb_htt_m3000],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-3000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m4000_madgraph",
    id=14856844,
    processes=[procs.radion_hh_ggf_hbb_htt_m4000],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-4000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m5000_madgraph",
    id=14854551,
    processes=[procs.radion_hh_ggf_hbb_htt_m5000],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-5000_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=22_000,
    aux={
        "merging_factors": {
            "nominal": 4,
        },
    },
)
