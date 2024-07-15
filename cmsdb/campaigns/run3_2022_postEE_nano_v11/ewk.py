# coding: utf-8

"""
Electroweak datasets for the 2022 post-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_v11 import campaign_run3_2022_postEE_nano_v11 as cpn


#
# Drell-Yan
#

# inclusive (MadGraph)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_m50toinf_madgraph",
    id=14679709,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22EENanoAODv11-forPOG_126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=96296977,
)

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14615268,
    is_data=False,
    processes=[procs.dy_m50toinf],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=125,
    n_events=215543566,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2L-4  # noqa
# missing as of 2023-07-01

# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2Mu  # noqa
# DAS entries:
#     /DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v2/NANOAODSIM

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=DYto2E_MLL  # noqa
# missing as of 2023-07-01


#
# W boson production
#

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14716346,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=161,
    n_events=291650146,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEwmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa
# missing as of 2023-07-01


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22EEGS&nanoaod_version=v11&short_name=VV  # noqa

# missing as of 2023-07-01
# cpn.add_dataset(
#     name="zz_pythia",
#     id=None,
#     is_data=False,
#     processes=[procs.zz],
#     keys=[
#         "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=None,
#     n_events=None,
# )

cpn.add_dataset(
    name="wz_pythia",
    id=14597897,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=27291718,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14596976,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22EENanoAODv11-126X_mcRun3_2022_realistic_postEE_v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=54649280,
)
