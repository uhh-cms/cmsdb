# coding: utf-8

"""
Electroweak datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn  # noqa


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

# tba

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

# tba

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

# tba
