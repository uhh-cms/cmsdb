# coding: utf-8

"""
QCD datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v12 import campaign_run3_2022_postEE_nano_v12 as cpn


cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14805741,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=16022411,
)
cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14791836,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=156,
    n_events=111483708,
)
cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14790872,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=221,
    n_events=102351102,
)
cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14790975,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=39665709,
)
cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14808161,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=159,
    n_events=98693572,
)
cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14805262,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=71463810,
)
cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14797549,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=264,
    n_events=109991815,
)
cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14792096,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=300,
    n_events=104186366,
)
cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14801374,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=222,
    n_events=71895522,
)
cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14805693,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=150,
    n_events=72668622,
)
cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14802178,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=375,
    n_events=132056316,
)
cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14791859,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=129,
    n_events=45523614,
)


#
# QCD (pythia, pt-binned, electron enriched)
#


cpn.add_dataset(
    name="qcd_em_pt10to30_pythia",
    id=14793132,
    # processes=[procs.qcd_em_pt10to30],
    keys=[
        "/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=3535208,
)
cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14800791,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=3271724,
)
cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14804630,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=3535752,
)
cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14800178,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=3396424,
)
cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14795445,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=3218461,
)
cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14811043,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=3542697,
)
cpn.add_dataset(
    name="qcd_em_pt300toInf_pythia",
    id=14791344,
    processes=[procs.qcd_em_pt300toInf],
    keys=[
        "/QCD_PT-300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=3254133,
)


#
# QCD (pythia, pt-binned, double electron enriched)
#


cpn.add_dataset(
    name="qcd_doubleem_pt30to40_pythia",
    id=14798807,
    # processes=[procs.qcd_doubleem_pt30to40],
    keys=[
        "/QCD_PT-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=118,
    n_events=4581753,
)
cpn.add_dataset(
    name="qcd_doubleem_pt30toInf_pythia",
    id=14797413,
    # processes=[procs.qcd_doubleem_pt30toInf],
    keys=[
        "/QCD_PT-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=9929160,
)
cpn.add_dataset(
    name="qcd_doubleem_pt40toInf_pythia",
    id=14810606,
    # processes=[procs.qcd_doubleem_pt40toInf],
    keys=[
        "/QCD_PT-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv12-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=10278008,
)
