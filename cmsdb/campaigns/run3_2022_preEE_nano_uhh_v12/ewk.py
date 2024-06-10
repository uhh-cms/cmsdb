# coding: utf-8

"""
Electroweak datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14950079,
    processes=[procs.dy_m4to10],
    keys=[
        "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=99_060_810,
    aux={
        "merging_factors": {
            "nominal": 38,
        },
    },
)

cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14803896,
    processes=[procs.dy_m10to50],
    keys=[
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=43 + 30,
    n_events=70_444_327 + 48_841_388,
    aux={
        "merging_factors": {
            "nominal": 22,
            "nominal_ext1": 23,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14796025,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext1-v1/NANOAODSIM",  # noqa
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5_ext2-v2/NANOAODSIM",  # noqa
    ],
    n_files=72 + 103 + 104,
    n_events=72_913_933 + 100_280_322 + 103_042_871,
    aux={
        "merging_factors": {
            "nominal": 17,
            "nominal_ext1": 18,
            "nominal_ext2": 25,
        },
    },
)

#
# W boson production
#

# inclusive
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14803849,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=70,
    n_events=87_502_461,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

#
# Z boson production -> only weird samples like binned in pT and nJets available, not processed
#

#
# EWK -> not available
# (vector boson emissions)
#

#
# Di-boson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14800066,
    processes=[procs.ww_pythia],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=15_405_496,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14803893,
    processes=[procs.wz_pythia],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=7_527_043,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="zz_pythia",
    id=14807788,
    processes=[procs.zz_pythia],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
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
    name="www_amcatnlo",
    id=14797810,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
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
    name="wwz_amcatnlo",
    id=14792468,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_950_044,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14792148,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_987_058,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14798395,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_970_234,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)
