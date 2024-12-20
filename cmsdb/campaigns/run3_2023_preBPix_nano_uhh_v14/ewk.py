# coding: utf-8

"""
Electroweak datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn  # noqa


#
# Drell-Yan
#

# tba

# jet-binned
# tba

# jet- and pT-binned
# tba

#
# W boson production
#

# inclusive
# tba

# jet-binned
# tba

# jet- and pT-binned
# tba

#
# Z boson production
#

cpn.add_dataset(
    name="z_qq_1j_pt100to200_amcatnlo",
    id=14888821,
    processes=[procs.z_qq_1j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=18_967_324,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt200to400_amcatnlo",
    id=14888424,
    processes=[procs.z_qq_1j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=8_982_365,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="z_qq_1j_pt400to600_amcatnlo",
    id=14888766,
    processes=[procs.z_qq_1j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=971_914,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)


cpn.add_dataset(
    name="z_qq_1j_pt600toinf_amcatnlo",
    id=14888969,
    processes=[procs.z_qq_1j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1_043_033,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt100to200_amcatnlo",
    id=14888631,
    processes=[procs.z_qq_2j_pt100to200],
    keys=[
        "/Zto2Q-2Jets_PTQQ-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=19_135_701,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt200to400_amcatnlo",
    id=14888772,
    processes=[procs.z_qq_2j_pt200to400],
    keys=[
        "/Zto2Q-2Jets_PTQQ-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=20_014_746,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt400to600_amcatnlo",
    id=14889107,
    processes=[procs.z_qq_2j_pt400to600],
    keys=[
        "/Zto2Q-2Jets_PTQQ-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_345_579,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="z_qq_2j_pt600toinf_amcatnlo",
    id=14888791,
    processes=[procs.z_qq_2j_pt600toinf],
    keys=[
        "/Zto2Q-2Jets_PTQQ-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_023_252,
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
    name="zz_pythia",
    id=14788274,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",
    ],
    n_files=3,
    n_events=2_517_000,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="ww_pythia",
    id=14784447,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",
    ],
    n_files=41,
    n_events=33_507_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="wz_pythia",
    id=14789732,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",
    ],
    n_files=20,
    n_events=16_770_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

# tba

#
# Triple-boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=14808796,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13p6TeV_amcatnlo-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=936_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14808744,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_576_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14808802,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=3_600_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=14808799,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=3_600_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

# tba
