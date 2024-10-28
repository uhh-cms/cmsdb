# coding: utf-8

"""
Electroweak datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14940404,
    processes=[procs.dy_m4to10],
    keys=[
        "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=102 + 77,
    n_events=197_298_815 + 148_437_348,
    aux={
        "merging_factors": {
            "nominal": 35,
            "nominal_ext1": 36,
        },
    },
)

cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14803270,
    processes=[procs.dy_m10to50],
    keys=[
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=132 + 102,
    n_events=226_070_829 + 172_564_148,
    aux={
        "merging_factors": {
            "nominal": 22,
            "nominal_ext1": 35,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14790485,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v1/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6_ext2-v2/NANOAODSIM",  # noqa
    ],
    n_files=210 + 327 + 365,
    n_events=215_642_133 + 333_589_016 + 360_626_787,
    aux={
        "merging_factors": {
            "nominal": 17,
            "nominal_ext1": 18,
            "nominal_ext2": 23,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14790238,
    processes=[procs.dy_m50toinf_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=291,
    n_events=346_131_555,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14790670,
    processes=[procs.dy_m50toinf_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=355,
    n_events=323_113_968,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14801012,
    processes=[procs.dy_m50toinf_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=384,
    n_events=277_816_186,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14821835,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=200,
    n_events=173_415_327,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14822194,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=90,
    n_events=66_051_870,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14822120,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=6_667_050,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14823819,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_722_633,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14870367,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_861_585,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14868305,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=102,
    n_events=72_553_546,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14868381,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=117,
    n_events=70_064_268,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14853112,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=12_755_867,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14827309,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_739_647,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14822095,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_682_240,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

#
# Z to qq
#

cpn.add_dataset(
    name="z_qq_1j_pt100to200_amcatnlo",
    id=14819376,
    processes=[procs.z_qq_1j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=34_083_732,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt200to400_amcatnlo",
    id=14871605,
    processes=[procs.z_qq_1j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=14_783_966,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt400to600_amcatnlo",
    id=14877318,
    processes=[procs.z_qq_1j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_699_376,
    aux={
        "merging_factors": {
            "nominal": 37,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt600toinf_amcatnlo",
    id=14875462,
    processes=[procs.z_qq_1j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_759_042,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt100to200_amcatnlo",
    id=14819417,
    processes=[procs.z_qq_2j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=34_235_822,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt200to400_amcatnlo",
    id=14851845,
    processes=[procs.z_qq_2j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=33_185_013,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt400to600_amcatnlo",
    id=14815668,
    processes=[procs.z_qq_2j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2_230_714,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt600toinf_amcatnlo",
    id=14821896,
    processes=[procs.z_qq_2j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_644_027,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14796080,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=227,
    n_events=288_582_950,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_0j_amcatnlo",
    id=14849099,
    processes=[procs.w_lnu_0j],
    keys=[
        "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=491,
    n_events=682_250_482,
    aux={
        "merging_factors": {
            "nominal": 27,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_amcatnlo",
    id=14853363,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=485,
    n_events=522_743_298,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_amcatnlo",
    id=14850137,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=409,
    n_events=346_779_790,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=14849220,
    processes=[procs.w_lnu_1j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=342,
    n_events=361_316_919,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=14852862,
    processes=[procs.w_lnu_1j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=159,
    n_events=143_076_575,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=14870226,
    processes=[procs.w_lnu_1j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=9_506_066,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=14836889,
    processes=[procs.w_lnu_1j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_643_010,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=14825896,
    processes=[procs.w_lnu_1j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_750_368,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=14847345,
    processes=[procs.w_lnu_2j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=404,
    n_events=348_453_544,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=14849305,
    processes=[procs.w_lnu_2j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=224,
    n_events=164_150_271,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=14827488,
    processes=[procs.w_lnu_2j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=18_316_631,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=14826842,
    processes=[procs.w_lnu_2j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_794_583,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=14827559,
    processes=[procs.w_lnu_2j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_632_052,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

#
# Di-boson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800910,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=53_112_080,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14799468,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=26_722_782,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="zz_pythia",
    id=14798176,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=4_043_040,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

#
# Triple-boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14791571,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_482_480,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14792375,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5_771_216,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14794158,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5_751_288,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14803298,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_872_560,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)
