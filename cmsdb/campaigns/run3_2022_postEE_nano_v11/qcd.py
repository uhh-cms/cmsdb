# coding: utf-8

"""
QCD datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v11 import campaign_run3_2022_postEE_nano_v11 as cpn


#
# QCD flat samples
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&dataset=QCD_PT-15*Flat2018&chained_request=Premix  # noqa
# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_flat2018_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_flat],
#     keys=[
#         "/QCD_PT-15_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&dataset=QCD_PT-15*Flat2018&chained_request=EpsilonPU  # noqa
cpn.add_dataset(
    name="qcd_flat2018_epsilon_pu_pythia",
    id=14685056,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15to7000_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22EENanoAODv11-EpsilonPU_126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=499399,
)


#
# QCD (MadGraph HT-binned)
#

# missing as of 2023-07-01


#
# QCD (Pythia pT-binned)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F0_TuneCP5&chained_request=Premix  # noqa

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_pt15to30_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_pt15to30],
#     keys=[
#         "/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1149000,
# )

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_pt30to50_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_pt30to50],
#     keys=[
#         "/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1189766,
# )

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14693393,
    is_data=False,
    processes=[procs.qcd_pt50to80],
    keys=[
        "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=19940303,
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14694837,
    is_data=False,
    processes=[procs.qcd_pt80to120],
    keys=[
        "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=29751976,
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14693403,
    is_data=False,
    processes=[procs.qcd_pt120to170],
    keys=[
        "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=26612745,
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14694848,
    is_data=False,
    processes=[procs.qcd_pt170to300],
    keys=[
        "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=27857315,
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14646803,
    is_data=False,
    processes=[procs.qcd_pt300to470],
    keys=[
        "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=55758810,
)

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14650352,
    is_data=False,
    processes=[procs.qcd_pt470to600],
    keys=[
        "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=26859708,
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14694849,
    is_data=False,
    processes=[procs.qcd_pt600to800],
    keys=[
        "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=62618820,
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14694802,
    is_data=False,
    processes=[procs.qcd_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=37290125,
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14646103,
    is_data=False,
    processes=[procs.qcd_pt1000to1400],
    keys=[
        "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=19351665,
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14693445,
    is_data=False,
    processes=[procs.qcd_pt1400to1800],
    keys=[
        "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=5471723,
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14645373,
    is_data=False,
    processes=[procs.qcd_pt1800to2400],
    keys=[
        "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2814872,
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14645367,
    is_data=False,
    processes=[procs.qcd_pt2400to3200],
    keys=[
        "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1904460,
)

cpn.add_dataset(
    name="qcd_pt3200_pythia",
    id=14645371,
    is_data=False,
    processes=[procs.qcd_pt3200],
    keys=[
        "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=800000,
)


#
# QCD (Pythia pT-binned, muon-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F_MuEnrichedPt5_TuneCP5&chained_request=Premix  # noqa

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14665668,
    is_data=False,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=16191725,
)

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_mu_pt20to30_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_mu_pt20to30],
#     keys=[
#         "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14686504,
    is_data=False,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=102973356,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14693382,
    is_data=False,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=39807191,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14626691,
    is_data=False,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=88063539,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14687921,
    is_data=False,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=69916479,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14689691,
    is_data=False,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=91,
    n_events=109775023,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14686495,
    is_data=False,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=94,
    n_events=103836309,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14687895,
    is_data=False,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=69,
    n_events=72243705,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14686293,
    is_data=False,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=73248078,
)

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_mu_pt800to1000_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_mu_pt800to1000],
#     keys=[
#         "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14687958,
    is_data=False,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=47564636,
)


#
# QCD (Pythia pT-binned, EM-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F_EMEnriched_TuneCP5&chained_request=Premix  # noqa
# missing as of 2023-07-01
