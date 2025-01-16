# coding: utf-8

"""
HHH -> bbbbtautau datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14 import campaign_run3_2022_preEE_nano_uhh_v14 as cpn


#
# HHH
#

cpn.add_dataset(
    name="hhh_4b2tau_c31_d40_amcatnlo",
    id=14805288,
    processes=[procs.hhh_4b2tau_c31_d40],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=395_878,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c34_d49_amcatnlo",
    id=14885953,
    processes=[procs.hhh_4b2tau_c34_d49],
    keys=[
        "/HHHto4B2Tau_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=262_292,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1_d40_amcatnlo",
    id=14795194,
    processes=[procs.hhh_4b2tau_c3m1_d40],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=384_245,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c31_d42_amcatnlo",
    id=14797469,
    processes=[procs.hhh_4b2tau_c31_d42],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=407_634,
    aux={
        "merging_factors": {
            "nominal": 11,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c32_d4m1_amcatnlo",
    id=14794613,
    processes=[procs.hhh_4b2tau_c32_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=396_595,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c30_d40_amcatnlo",
    id=14791313,
    processes=[procs.hhh_4b2tau_c30_d40],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=9_399_560,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c30_d499_amcatnlo",
    id=14802797,
    processes=[procs.hhh_4b2tau_c30_d499],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=387_652,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c30_d4m1_amcatnlo",
    id=14796290,
    processes=[procs.hhh_4b2tau_c30_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_610,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c319_d419_amcatnlo",
    id=14805828,
    processes=[procs.hhh_4b2tau_c319_d419],
    keys=[
        "/HHHto4B2Tau_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_190,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1_d4m1_amcatnlo",
    id=14791288,
    processes=[procs.hhh_4b2tau_c3m1_d4m1],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=398_634,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3m1p5_d4m0p5_amcatnlo",
    id=14792134,
    processes=[procs.hhh_4b2tau_c3m1p5_d4m0p5],
    keys=[
        "/HHHto4B2Tau_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=406_138,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)
