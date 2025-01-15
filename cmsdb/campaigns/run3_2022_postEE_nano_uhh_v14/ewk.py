# coding: utf-8

"""
Electroweak datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn


#
# Drell-Yan
#

# tba

#
# Z to qq
#

# tba

#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14796080,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=280,
    n_events=288_582_950,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_0j_amcatnlo",
    id=14849099,
    processes=[procs.w_lnu_0j],
    keys=[
        "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=577,
    n_events=682_250_482,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_amcatnlo",
    id=14853363,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=557,
    n_events=522_743_298,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_amcatnlo",
    id=14850137,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=481,
    n_events=346_779_790,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=14849220,
    processes=[procs.w_lnu_1j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=411,
    n_events=361_316_919,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=14852862,
    processes=[procs.w_lnu_1j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=190,
    n_events=143_076_575,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=14870226,
    processes=[procs.w_lnu_1j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=9_506_066,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=14836889,
    processes=[procs.w_lnu_1j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
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
        "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_750_368,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=14847345,
    processes=[procs.w_lnu_2j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=472,
    n_events=348_453_544,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=14849305,
    processes=[procs.w_lnu_2j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=261,
    n_events=164_150_271,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=14827488,
    processes=[procs.w_lnu_2j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=18_316_631,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=14826842,
    processes=[procs.w_lnu_2j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_794_583,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=14827559,
    processes=[procs.w_lnu_2j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
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
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=53_112_080,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14799468,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=26_722_782,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="zz_pythia",
    id=14798176,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4_043_040,
    aux={
        "merging_factors": {
            "nominal": 17,
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
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
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
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=5_771_216,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14794158,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=5_751_288,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14803298,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5_872_560,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)
