# coding: utf-8

"""
Electroweak datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn


#
# Drell-Yan
#

cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14940059,
    processes=[procs.dy_m4to10],
    keys=[
        "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=97_699_308,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)

cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14905232,
    processes=[procs.dy_m10to50],
    keys=[
        "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2_ext1-v3/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=100_269_476,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14851213,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=119,
    n_events=95_646_832,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14892800,
    processes=[procs.dy_m50toinf_0j],
    keys=[
        "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=104,
    n_events=96_541_209,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14893834,
    processes=[procs.dy_m50toinf_1j],
    keys=[
        "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=130,
    n_events=91_332_285,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14897349,
    processes=[procs.dy_m50toinf_2j],
    keys=[
        "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=131,
    n_events=77_408_545,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14826069,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=76,
    n_events=52_938_287,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14826410,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=19_384_285,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14825925,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_985_212,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14824627,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=459_553,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14825270,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=456_439,
    aux={
        "merging_factors": {
            "nominal": 33,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14825645,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=20_416_556,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14826149,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=19_943_443,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14822125,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=3_623_077,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14823406,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=493_730,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14825018,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=477_040,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14978098,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=96,
    n_events=95_603_855,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_0j_amcatnlo",
    id=14911283,
    processes=[procs.w_lnu_0j],
    keys=[
        "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=170,
    n_events=198_993_882,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_amcatnlo",
    id=14895847,
    processes=[procs.w_lnu_1j],
    keys=[
        "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=170,
    n_events=149_508_424,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_amcatnlo",
    id=14912929,
    processes=[procs.w_lnu_2j],
    keys=[
        "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=138,
    n_events=99_673_760,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=14890303,
    processes=[procs.w_lnu_1j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=118,
    n_events=100_269_999,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=14891928,
    processes=[procs.w_lnu_1j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=64,
    n_events=46_147_267,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=14890787,
    processes=[procs.w_lnu_1j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2_804_887,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=14892481,
    processes=[procs.w_lnu_1j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=511_690,
    aux={
        "merging_factors": {
            "nominal": 29,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=14892447,
    processes=[procs.w_lnu_2j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=138,
    n_events=98_365_047,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=14893884,
    processes=[procs.w_lnu_2j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=81,
    n_events=48_661_402,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=14892478,
    processes=[procs.w_lnu_2j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5_240_236,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=14889914,
    processes=[procs.w_lnu_2j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=498_986,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=14894918,
    processes=[procs.w_lnu_1j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=552_078,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=14890482,
    processes=[procs.w_lnu_2j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=477_908,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

#
# Z boson production (non-DY)
#

cpn.add_dataset(
    name="z_qq_1j_pt100to200_amcatnlo",
    id=14888626,
    processes=[procs.z_qq_1j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=10_126_628,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt200to400_amcatnlo",
    id=14888588,
    processes=[procs.z_qq_1j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=4_484_374,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt400to600_amcatnlo",
    id=14889627,
    processes=[procs.z_qq_1j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=491_910,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt600toinf_amcatnlo",
    id=14888968,
    processes=[procs.z_qq_1j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=481_973,
    aux={
        "merging_factors": {
            "nominal": 35,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt100to200_amcatnlo",
    id=14888586,
    processes=[procs.z_qq_2j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=9_629_569,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt200to400_amcatnlo",
    id=14888881,
    processes=[procs.z_qq_2j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=10_218_032,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt400to600_amcatnlo",
    id=14889086,
    processes=[procs.z_qq_2j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=720_919,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt600toinf_amcatnlo",
    id=14888363,
    processes=[procs.z_qq_2j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=505_354,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

#
# W/Z VBF production
#

cpn.add_dataset(
    name="w_vbf_wlnu_madgraph",
    id=15016689,
    processes=[procs.w_vbf_wlnu],
    keys=[
        "/VBFtoLNu_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=9_808_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="z_vbf_zll_m50toinf_madgraph",
    id=15015836,
    processes=[procs.z_vbf_zll_m50toinf],
    keys=[
        "/VBFto2L_MLL-50_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3_488_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

#
# Di-boson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14783170,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=16_545_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14784069,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=8_379_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="zz_pythia",
    id=14784122,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1_254_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

#
# Triple-boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14787824,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=466_500,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14827006,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_743_000,
    aux={
        "merging_factors": {
            "nominal": 18,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14788045,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_788_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14784432,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_788_000,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)
