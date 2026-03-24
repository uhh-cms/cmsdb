# coding: utf-8

"""
Electroweak datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15 import campaign_run3_2022_preEE_nano_uhh_v14_trg_v15 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14796025,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext2-v2/NANOAODSIM",  # noqa
    ],
    n_files=94 + 133 + 137,
    n_events=72_913_933 + 100_280_322 + 103_042_871,
    aux={
        "merging_factors": {
            "nominal": 13,
            "nominal_ext1": 14,
            "nominal_ext2": 19,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14791239,
    processes=[procs.dy_m50toinf_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=105,
    n_events=87_955_912,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14791368,
    processes=[procs.dy_m50toinf_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=138,
    n_events=96_932_233,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14790842,
    processes=[procs.dy_m50toinf_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=126,
    n_events=71_990_957,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14825012,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=78,
    n_events=50_272_820,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14824884,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=18_682_106,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14826002,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_939_721,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14822087,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=503_786,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14830407,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=508_646,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14822136,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=19_307_377,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14825259,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=19_139_796,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14824840,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=3_651_560,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14822163,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=488_707,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14825895,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=474_576,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

#
# Drell-Yan amcatnlo, tautau reprocessed in njet bins
#

cpn.add_dataset(
    name="dy_tautau_m50toinf_0j_amcatnlo",
    id=15361199,
    processes=[procs.dy_tautau_m50toinf_0j],
    keys=[
        "/DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=39_627_426,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_1j_amcatnlo",
    id=15361289,
    processes=[procs.dy_tautau_m50toinf_1j],
    keys=[
        "/DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=56_687_827,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_2j_amcatnlo",
    id=15361314,
    processes=[procs.dy_tautau_m50toinf_2j],
    keys=[
        "/DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=175,
    n_events=107_747_888,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

#
# Drell-Yan amcatnlo, tautau reprocessed in njet bins, filtered to some tautau kinematic phase space
# (see fragment in https://cms-pdmv-prod.web.cern.ch/mcm/requests?prepid=HIG-Run3Summer22EEwmLHEGS-01476&page=0&shown=140737488355327)  # noqa
#

cpn.add_dataset(
    name="dy_tautau_m50toinf_0j_filtered_amcatnlo",
    id=15364909,
    processes=[procs.dy_tautau_m50toinf_0j_filtered],
    keys=[
        "/DYto2Tau-2Jets_M-50_0J_Filtered_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=12_631_795,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_1j_filtered_amcatnlo",
    id=15363827,
    processes=[procs.dy_tautau_m50toinf_1j_filtered],
    keys=[
        "/DYto2Tau-2Jets_M-50_1J_Filtered_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=20_230_695,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="dy_tautau_m50toinf_2j_filtered_amcatnlo",
    id=15363828,
    processes=[procs.dy_tautau_m50toinf_2j_filtered],
    keys=[
        "/DYto2Tau-2Jets_M-50_2J_Filtered_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v4/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=32_440_564,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803849,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=93,
    n_events=87_502_461,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_0j_amcatnlo",
    id=14848502,
    processes=[procs.w_lnu_0j],
    keys=[
        "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=181,
    n_events=191_268_400,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_amcatnlo",
    id=14850193,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=141_411_157,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=14823511,
    processes=[procs.w_lnu_1j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=119,
    n_events=93_802_769,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=14826852,
    processes=[procs.w_lnu_1j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=40_296_254,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=14850711,
    processes=[procs.w_lnu_1j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_031_278,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=14821860,
    processes=[procs.w_lnu_1j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=485_577,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=14825295,
    processes=[procs.w_lnu_1j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=472_466,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_amcatnlo",
    id=14850095,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=161,
    n_events=102_668_792,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=14847376,
    processes=[procs.w_lnu_2j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=145,
    n_events=96_227_072,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=14826687,
    processes=[procs.w_lnu_2j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=80,
    n_events=46_710_602,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=14826710,
    processes=[procs.w_lnu_2j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=5_488_647,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=14831405,
    processes=[procs.w_lnu_2j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=467_510,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=14826832,
    processes=[procs.w_lnu_2j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=458_648,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

#
# Z boson production (non-DY)
#

cpn.add_dataset(
    name="z_qq_1j_pt100to200_amcatnlo",
    id=14821998,
    processes=[procs.z_qq_1j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=10_154_543,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt200to400_amcatnlo",
    id=14819696,
    processes=[procs.z_qq_1j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=4_474_590,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt400to600_amcatnlo",
    id=14819096,
    processes=[procs.z_qq_1j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=481_551,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt600toinf_amcatnlo",
    id=14831037,
    processes=[procs.z_qq_1j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=519_778,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt100to200_amcatnlo",
    id=14819477,
    processes=[procs.z_qq_2j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=8_995_099,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt200to400_amcatnlo",
    id=14815862,
    processes=[procs.z_qq_2j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=9_816_008,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt400to600_amcatnlo",
    id=14825756,
    processes=[procs.z_qq_2j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=710_337,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt600toinf_amcatnlo",
    id=14824862,
    processes=[procs.z_qq_2j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=540_869,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

#
# W/Z VBF production
#

cpn.add_dataset(
    name="w_vbf_wlnu_madgraph",
    id=15015923,
    processes=[procs.w_vbf_wlnu],
    keys=[
        "/VBFtoLNu_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=9_958_336,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="z_vbf_zll_m50toinf_madgraph",
    id=15015907,
    processes=[procs.z_vbf_zll_m50toinf],
    keys=[
        "/VBFto2L_MLL-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3_492_580,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

#
# Di-boson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800066,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",
    ],
    n_files=20,
    n_events=15_405_496,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14803893,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",
    ],
    n_files=10,
    n_events=7_479_528,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="zz_pythia",
    id=14807788,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",
    ],
    n_files=2,
    n_events=1_181_750,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

#
# Triple-boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14797810,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=450_000,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14792468,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_950_044,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14792148,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_987_058,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14798395,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_970_234,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)
