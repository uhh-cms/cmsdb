# coding: utf-8

"""
Top quark related datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

# from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn


#
# ttbar
#

# tba

#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=14850108,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v4/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=335_985,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="ttz_zqq_amcatnlo",
    id=14792049,
    processes=[procs.ttz_zqq],
    keys=[
        "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_330_390,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=14790944,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_049_999,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=14791092,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_386_140,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

cpn.add_dataset(
    name="ttz_znunu_amcatnlo",
    id=14881355,
    processes=[procs.ttz_znunu],
    keys=[
        "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_746_360,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

#
# ttbar + 2 vector bosons
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14797703,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_536_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=15007010,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_500_000,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14826274,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1_519_000,
    aux={
        "merging_factors": {
            "nominal": 9,
        },
    },
)

#
# single top
#

# tba
