# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14_trg_v15 import campaign_run3_2022_postEE_nano_uhh_v14_trg_v15 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14853029,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_047_884,
    aux={
        "merging_factors": {
            "nominal": 40,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=15004156,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_079_518,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=14952632,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_435_020,
    aux={
        "merging_factors": {
            "nominal": 47,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=15050396,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_067_640,
    aux={
        "merging_factors": {
            "nominal": 34,
        },
    },
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=15376090,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_madgraph",
    id=15376587,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15377297,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_CV_1p74_C2V_1p37_C3_14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_492_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15378024,
    processes=[procs.hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_CV_2p12_C2V_3p87_C3_m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15377874,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p012_C2V_0p030_C3_10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_500_000,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15378001,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p758_C2V_1p44_C3_m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_496_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15377645,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_CV_m0p962_C2V_0p959_C3_m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_494_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15377691,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p21_C2V_1p94_C3_m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15377637,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p60_C2V_2p72_C3_m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15376478,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_CV_m1p83_C2V_3p57_C3_m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_498_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

#
# ggf -> graviton -> HH
#

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m450_madgraph",
    id=14861912,
    processes=[procs.graviton_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-450_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=300_960,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="graviton_hh_ggf_hbb_htt_m1200_madgraph",
    id=14864516,
    processes=[procs.graviton_hh_ggf_hbb_htt_m1200],
    keys=[
        "/GluGlutoBulkGravitontoHHto2B2Tau_M-1200_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=78_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

#
# ggf -> radion -> HH
#

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m450_madgraph",
    id=14862877,
    processes=[procs.radion_hh_ggf_hbb_htt_m450],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-450_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=310_624,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="radion_hh_ggf_hbb_htt_m1200_madgraph",
    id=14863692,
    processes=[procs.radion_hh_ggf_hbb_htt_m1200],
    keys=[
        "/GluGlutoRadiontoHHto2B2Tau_M-1200_narrow_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=75_352,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)
