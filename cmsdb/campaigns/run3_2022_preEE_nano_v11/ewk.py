# coding: utf-8

"""
Electroweak datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v11 import campaign_run3_2022_preEE_nano_v11 as cpn


#
# Drell-Yan
#

# inclusive (MadGraph)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYJetsToLL_M-50&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="dy_lep_m50_madgraph",
    id=14679260,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/Run3Summer22NanoAODv11-forPOG_126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=26047237,
)

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-2Jets_MLL-50&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14637757,
    is_data=False,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=71028905,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2L-4  # noqa
# missing as of 2023-07-01

# POWHEG (decay to muons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2Mu  # noqa
# DAS entries:
#     /DYto2Mu_MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM
#     /DYto2Mu_MLL-4000_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM

# POWHEG (decay to electrons, MLL-binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=DYto2E_MLL  # noqa
# missing as of 2023-07-01


#
# W boson production
#

# inclusive (aMC@NLO)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-2Jets&nanoaod_version=v11  # noqa  # noqa
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14611721,
    is_data=False,
    processes=[procs.w_lnu],
    keys=[
        "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=80257100,
)

# MadGraph (n-jet binned)
# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22wmLHEGS&dataset=WtoLNu-4Jets_%281%7C2%7C3%7C4%29J&nanoaod_version=v11  # noqa  # noqa
# missing as of 2023-07-01


#
# Diboson
#

# GrASP: https://cms-pdmv.cern.ch/grasp/samples?campaign=Run3Summer22GS&nanoaod_version=v11&short_name=VV  # noqa

cpn.add_dataset(
    name="zz_pythia",
    id=14587173,
    is_data=False,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1186860,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14596611,
    is_data=False,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=7744881,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14694767,
    is_data=False,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer22NanoAODv11-126X_mcRun3_2022_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=15474424,
)
