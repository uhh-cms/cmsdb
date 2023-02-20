# coding: utf-8

"""
QCD datasets for the 2017 data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn

#
# QCD HT-binned
#

cpn.add_dataset(
    name="qcd_ht50to100_madgraph",
    id=14165805,
    processes=[procs.qcd_ht50to100],
    keys=[
        "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=40370559,
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=14165816,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=77551016,
)

cpn.add_dataset(
    name="qcd_ht200to300_madgraph",
    id=14165798,
    processes=[procs.qcd_ht200to300],
    keys=[
        "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=57400723,
)

cpn.add_dataset(
    name="qcd_ht300to500_madgraph",
    id=14165206,
    processes=[procs.qcd_ht300to500],
    keys=[
        "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=56549740,
)

cpn.add_dataset(
    name="qcd_ht500to700_madgraph",
    id=14165524,
    processes=[procs.qcd_ht500to700],
    keys=[
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
        "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=14 + 50,
    n_events=9027879 + 57880117,
)

cpn.add_dataset(
    name="qcd_ht700to1000_madgraph",
    id=14165795,
    processes=[procs.qcd_ht700to1000],
    keys=[
        "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=45812757,
)

cpn.add_dataset(
    name="qcd_ht1000to1500_madgraph",
    id=14165562,
    processes=[procs.qcd_ht1000to1500],
    keys=[
        "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=15346629,
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=14165704,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=10598209,
)

cpn.add_dataset(
    name="qcd_ht2000_madgraph",
    id=14165502,
    processes=[procs.qcd_ht2000],
    keys=[
        "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=5457021,
)

#
# QCD pt-binned (muon enriched)
#

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14278484,
    processes=[procs.qcd_mu_pt15to20],
    keys=[
        "/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=9019841,
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14285221,
    processes=[procs.qcd_mu_pt20to30],
    keys=[
        "/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=87,
    n_events=64623134,
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14285245,
    processes=[procs.qcd_mu_pt30to50],
    keys=[
        "/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=58639613,
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14288213,
    processes=[procs.qcd_mu_pt50to80],
    keys=[
        "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=40322726,
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14295914,
    processes=[procs.qcd_mu_pt80to120],
    keys=[
        "/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=60,
    n_events=45981017,
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14268599,
    processes=[procs.qcd_mu_pt120to170],
    keys=[
        "/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=78,
    n_events=39394151,
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14268251,
    processes=[procs.qcd_mu_pt170to300],
    keys=[
        "/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=94,
    n_events=73071987,
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14278866,
    processes=[procs.qcd_mu_pt300to470],
    keys=[
        "/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=68,
    n_events=58692910,
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14282294,
    processes=[procs.qcd_mu_pt470to600],
    keys=[
        "/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=39491752,
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14282441,
    processes=[procs.qcd_mu_pt600to800],
    keys=[
        "/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=39321940,
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14328314,
    processes=[procs.qcd_mu_pt800to1000],
    keys=[
        "/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=101,
    n_events=78215559,
)

cpn.add_dataset(
    name="qcd_mu_pt1000_pythia",
    id=14288345,
    processes=[procs.qcd_mu_pt1000],
    keys=[
        "/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=27478273,
)

#
# QCD pt-binned (electron enriched)
#

cpn.add_dataset(
    name="qcd_em_pt15to20_pythia",
    id=14356198,
    processes=[procs.qcd_em_pt15to20],
    keys=[
        "/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=7966910,
)

cpn.add_dataset(
    name="qcd_em_pt20to30_pythia",
    id=14345164,
    processes=[procs.qcd_em_pt20to30],
    keys=[
        "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=14166147,
)

cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14271784,
    processes=[procs.qcd_em_pt30to50],
    keys=[
        "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=8784542,
)

cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14278779,
    processes=[procs.qcd_em_pt50to80],
    keys=[
        "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=10210400,
)

cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14268373,
    processes=[procs.qcd_em_pt80to120],
    keys=[
        "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=9615795,
)

cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14268679,
    processes=[procs.qcd_em_pt120to170],
    keys=[
        "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=9904245,
)

cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14271994,
    processes=[procs.qcd_em_pt170to300],
    keys=[
        "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=3678200,
)

cpn.add_dataset(
    name="qcd_em_pt300toInf_pythia",
    id=14275722,
    processes=[procs.qcd_em_pt300toInf],
    keys=[
        "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2214934,
)

#
# QCD pt-binned (bcToE)
#

# TODO: id, numbers

cpn.add_dataset(
    name="qcd_bctoe_pt15to20_pythia",
    id=14403519,
    processes=[procs.qcd_bctoe_pt15to20],
    keys=[
        "/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=39,
    n_events=18671506,
)

cpn.add_dataset(
    name="qcd_bctoe_pt20to30_pythia",
    id=14342613,
    processes=[procs.qcd_bctoe_pt20to30],
    keys=[
        "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=42,
    n_events=14171260,
)

cpn.add_dataset(
    name="qcd_bctoe_pt30to80_pythia",
    id=14255941,
    processes=[procs.qcd_bctoe_pt30to80],
    keys=[
        "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=18,
    n_events=15238384,
)

cpn.add_dataset(
    name="qcd_bctoe_pt80to170_pythia",
    id=14262627,
    processes=[procs.qcd_bctoe_pt80to170],
    keys=[
        "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=14,
    n_events=15571255,
)

cpn.add_dataset(
    name="qcd_bctoe_pt170to250_pythia",
    id=14265770,
    processes=[procs.qcd_bctoe_pt170to250],
    keys=[
        "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=21,
    n_events=15502839,
)

cpn.add_dataset(
    name="qcd_bctoe_pt250toInf_pythia",
    id=14306070,
    processes=[procs.qcd_bctoe_pt250toInf],
    keys=[
        "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"  # NOQA
    ],
    n_files=26,
    n_events=15078102,
)
