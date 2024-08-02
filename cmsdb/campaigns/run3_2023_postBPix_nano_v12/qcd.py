# coding: utf-8

# Find information from here: https://docs.google.com/presentation/d/1TjPem5jX0fzqvTGl271_nQFoVBabsrdrO0i8Qo1uD5E/edit#slide=id.g289f499aa6b_2_58 

"""
QCD datasets for the 2023 postBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn


#
# QCD (pythia, pt-binned, muon enriched)
#

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14781363,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=4999275,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14781373,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=166,
    n_events=33206620,
)
# in addition to JMENano12p5, -KeepRAW_ also exists for this ^

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14784056,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=137,
    n_events=31900002,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14784155,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=12720414,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14784054,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=84,
    n_events=26692302,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14783279,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=85,
    n_events=22380325,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14783386,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=125,
    n_events=33223105,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14784117,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=122,
    n_events=31622567,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14783278,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=89,
    n_events=23080052,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14783146,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=113,
    n_events=22886334,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14783121,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=195,
    n_events=41077955,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14783282,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=15340005,
)


#
# QCD (pythia, pt-binned, electron enriched)
#

cpn.add_dataset(
    name="qcd_em_pt10to30_pythia",
    id=14788948,
    processes=[procs.qcd_em_pt10to30],
    keys=[
        "/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=1024670,
)

cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14790510,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1031074,
)

cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14790653,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=985509,
)

cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14790458,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=1021976,
)

cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14790461,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=1051454,
)

cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14790413,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=1073461,
)

cpn.add_dataset(
    name="qcd_em_pt300toinf_pythia",
    id=14790517,
    processes=[procs.qcd_em_pt300toinf],
    keys=[
        "/QCD_PT-300toInf_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=842285,
)


#
# QCD (pythia, pt-binned, double electron enriched)
#


# do not exist for 2023 yet