# coding: utf-8

"""
QCD datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# QCD flat samples
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&dataset=QCD_PT-15*Flat2018&chained_request=Premix
cpn.add_dataset(
    name="qcd_flat2018_pythia",
    id=14636176,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=8,
    n_events=9251295,
)

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&dataset=QCD_PT-15*Flat2018&chained_request=EpsilonPU
cpn.add_dataset(
    name="qcd_flat2018_epsilonPU_pythia",
    id=14685183,
    is_data=False,
    processes=[procs.qcd_flat],
    keys=[
        "/QCD_PT-15to7000_TuneCP5_Flat2018_13p6TeV_pythia8/Run3Summer22NanoAODv11-EpsilonPU_126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=3,
    n_events=499387,
)


#
# QCD (MadGraph HT-binned)
#

# missing as of 2023-07-01


#
# QCD (Pythia pT-binned)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F0_TuneCP5&chained_request=Premix

cpn.add_dataset(
    name="qcd_pt15to30_pythia",
    id=14689890,
    is_data=False,
    processes=[procs.qcd_pt15to30],
    keys=[
        "/QCD_PT-15to30_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=2,
    n_events=1149000,
)

cpn.add_dataset(
    name="qcd_pt30to50_pythia",
    id=14689122,
    is_data=False,
    processes=[procs.qcd_pt30to50],
    keys=[
        "/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=2,
    n_events=1189766,
)

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14693446,
    is_data=False,
    processes=[procs.qcd_pt50to80],
    keys=[
        "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=12,
    n_events=19722512,
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14694162,
    is_data=False,
    processes=[procs.qcd_pt80to120],
    keys=[
        "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=17,
    n_events=29209440,
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14693352,
    is_data=False,
    processes=[procs.qcd_pt120to170],
    keys=[
        "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=21,
    n_events=29908875,
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14694835,
    is_data=False,
    processes=[procs.qcd_pt170to300],
    keys=[
        "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=21,
    n_events=28624020,
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14694880,
    is_data=False,
    processes=[procs.qcd_pt300to470],
    keys=[
        "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=45,
    n_events=57525303,
)

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14693379,
    is_data=False,
    processes=[procs.qcd_pt470to600],
    keys=[
        "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=22,
    n_events=27577568,
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14694728,
    is_data=False,
    processes=[procs.qcd_pt600to800],
    keys=[
        "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=57,
    n_events=66884777,
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14694323,
    is_data=False,
    processes=[procs.qcd_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=35,
    n_events=39451059,
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14694841,
    is_data=False,
    processes=[procs.qcd_pt1000to1400],
    keys=[
        "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=21,
    n_events=19882169,
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14637819,
    is_data=False,
    processes=[procs.qcd_pt1400to1800],
    keys=[
        "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=8,
    n_events=5836650,
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14641606,
    is_data=False,
    processes=[procs.qcd_pt1800to2400],
    keys=[
        "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=4,
    n_events=2989840,
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14693239,
    is_data=False,
    processes=[procs.qcd_pt2400to3200],
    keys=[
        "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=3,
    n_events=1963904,
)

cpn.add_dataset(
    name="qcd_pt3200_pythia",
    id=14645062,
    is_data=False,
    processes=[procs.qcd_pt3200],
    keys=[
        "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2_ext1-v1/NANOAODSIM",
    ],
    n_files=1,
    n_events=782175,
)


#
# QCD (Pythia pT-binned, muon-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F_MuEnrichedPt5_TuneCP5&chained_request=Premix

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14637754,
    is_data=False,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=4,
    n_events=4529335,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14689998,
    is_data=False,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=19,
    n_events=29845469,
)

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_mu_pt30to50_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_mu_pt30to50],
#     keys=[
#         "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14694803,
    is_data=False,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=25,
    n_events=41159366,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14625411,
    is_data=False,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=18,
    n_events=25108328,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14686500,
    is_data=False,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=20,
    n_events=18849346,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14687812,
    is_data=False,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=34,
    n_events=36140731,
)

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="qcd_mu_pt300to470_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.qcd_mu_pt300to470],
#     keys=[
#         "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14686361,
    is_data=False,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=21,
    n_events=18066469,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14687893,
    is_data=False,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=19,
    n_events=19989674,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14620509,
    is_data=False,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=44,
    n_events=39272493,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14694180,
    is_data=False,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",
    ],
    n_files=17,
    n_events=14214939,
)


#
# QCD (Pythia pT-binned, EM-enriched)
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&dataset=QCD_PT-*%28to*%29%3F_EMEnriched_TuneCP5&chained_request=Premix
# missing as of 2023-07-01 (only v10 available)
