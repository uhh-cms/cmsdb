# coding: utf-8

"""
QCD datasets for the 2023 preBPix data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


#
# QCD (pythia, pt-binned, muon enriched)
#

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14790601,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v3/NANOAODSIM",  # noqa
    ],
    n_files=75,
    n_events=9975115,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14784713,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=320,
    n_events=67051286,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14786118,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=242,
    n_events=63799051,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14784497,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=107,
    n_events=25399473,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14787197,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=185,
    n_events=53224427,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14784873,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=44453475,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14786774,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=244,
    n_events=66085188,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14788145,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=260,
    n_events=63027869,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14788781,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=191,
    n_events=45774064,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14784843,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=233,
    n_events=46077770,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14784446,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=397,
    n_events=84055579,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14784746,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=162,
    n_events=31590388,
)



#
# QCD (pythia, pt-binned, electron enriched)
#

cpn.add_dataset(
    name="qcd_em_pt10to30_pythia",
    id=14788282,
    processes=[procs.qcd_em_pt10to30],
    keys=[
        "/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=2121779,
)

cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14790908,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2053805,
)

cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14790503,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=1990713,
)

cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14789970,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=2076482,
)

cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14790533,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=2100319,
)

cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14790618,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=2141399,
)

cpn.add_dataset(
    name="qcd_em_pt300toinf_pythia",
    id=14790606,
    processes=[procs.qcd_em_pt300toinf],
    keys=[
        "/QCD_PT-300toInf_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=1582951,
)


#
# QCD (pythia, pt-binned, double electron enriched)
#

# do not exist so far for 2023