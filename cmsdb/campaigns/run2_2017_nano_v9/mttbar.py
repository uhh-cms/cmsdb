# coding: utf-8

"""
Signal samples for m(ttbar) line search
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


cpn.add_dataset(
    name="zprime_tt_m_400_w_40_madgraph",
    id=14243245,
    processes=[procs.zprime_tt_m_400_w_40],
    keys=[
        "/ZPrimeToTT_M400_W40_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=497000,
)


cpn.add_dataset(
    name="zprime_tt_m_400_w_120_madgraph",
    id=14278504,
    processes=[procs.zprime_tt_m_400_w_120],
    keys=[
        "/ZPrimeToTT_M400_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_400_w_4_madgraph",
    id=14336497,
    processes=[procs.zprime_tt_m_400_w_4],
    keys=[
        "/ZprimeToTTJets_M400_W4_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=201853,
)


cpn.add_dataset(
    name="zprime_tt_m_500_w_50_madgraph",
    id=14281237,
    processes=[procs.zprime_tt_m_500_w_50],
    keys=[
        "/ZPrimeToTT_M500_W50_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=491000,
)


cpn.add_dataset(
    name="zprime_tt_m_500_w_150_madgraph",
    id=14281224,
    processes=[procs.zprime_tt_m_500_w_150],
    keys=[
        "/ZPrimeToTT_M500_W150_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=494000,
)


cpn.add_dataset(
    name="zprime_tt_m_500_w_5_madgraph",
    id=14360854,
    processes=[procs.zprime_tt_m_500_w_5],
    keys=[
        "/ZprimeToTTJets_M500_W5_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=188083,
)


cpn.add_dataset(
    name="zprime_tt_m_600_w_60_madgraph",
    id=14281128,
    processes=[procs.zprime_tt_m_600_w_60],
    keys=[
        "/ZPrimeToTT_M600_W60_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=494000,
)


cpn.add_dataset(
    name="zprime_tt_m_600_w_180_madgraph",
    id=14283411,
    processes=[procs.zprime_tt_m_600_w_180],
    keys=[
        "/ZPrimeToTT_M600_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=491000,
)


cpn.add_dataset(
    name="zprime_tt_m_600_w_6_madgraph",
    id=14332670,
    processes=[procs.zprime_tt_m_600_w_6],
    keys=[
        "/ZprimeToTTJets_M600_W6_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=198225,
)


cpn.add_dataset(
    name="zprime_tt_m_700_w_70_madgraph",
    id=14278238,
    processes=[procs.zprime_tt_m_700_w_70],
    keys=[
        "/ZPrimeToTT_M700_W70_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_700_w_210_madgraph",
    id=14281059,
    processes=[procs.zprime_tt_m_700_w_210],
    keys=[
        "/ZPrimeToTT_M700_W210_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_700_w_7_madgraph",
    id=14333023,
    processes=[procs.zprime_tt_m_700_w_7],
    keys=[
        "/ZprimeToTTJets_M700_W7_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=200215,
)


cpn.add_dataset(
    name="zprime_tt_m_800_w_80_madgraph",
    id=14279821,
    processes=[procs.zprime_tt_m_800_w_80],
    keys=[
        "/ZPrimeToTT_M800_W80_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=494000,
)


cpn.add_dataset(
    name="zprime_tt_m_800_w_240_madgraph",
    id=14254580,
    processes=[procs.zprime_tt_m_800_w_240],
    keys=[
        "/ZPrimeToTT_M800_W240_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_800_w_8_madgraph",
    id=14333373,
    processes=[procs.zprime_tt_m_800_w_8],
    keys=[
        "/ZprimeToTTJets_M800_W8_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=193169,
)


cpn.add_dataset(
    name="zprime_tt_m_900_w_90_madgraph",
    id=14284536,
    processes=[procs.zprime_tt_m_900_w_90],
    keys=[
        "/ZPrimeToTT_M900_W90_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_900_w_270_madgraph",
    id=14285297,
    processes=[procs.zprime_tt_m_900_w_270],
    keys=[
        "/ZPrimeToTT_M900_W270_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=461000,
)


cpn.add_dataset(
    name="zprime_tt_m_900_w_9_madgraph",
    id=14336552,
    processes=[procs.zprime_tt_m_900_w_9],
    keys=[
        "/ZprimeToTTJets_M900_W9_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=199844,
)


cpn.add_dataset(
    name="zprime_tt_m_1000_w_100_madgraph",
    id=14280940,
    processes=[procs.zprime_tt_m_1000_w_100],
    keys=[
        "/ZPrimeToTT_M1000_W100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_1000_w_300_madgraph",
    id=14300363,
    processes=[procs.zprime_tt_m_1000_w_300],
    keys=[
        "/ZPrimeToTT_M1000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_1000_w_10_madgraph",
    id=14336319,
    processes=[procs.zprime_tt_m_1000_w_10],
    keys=[
        "/ZprimeToTTJets_M1000_W10_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=194229,
)


cpn.add_dataset(
    name="zprime_tt_m_1200_w_120_madgraph",
    id=14302542,
    processes=[procs.zprime_tt_m_1200_w_120],
    keys=[
        "/ZPrimeToTT_M1200_W120_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=497000,
)


cpn.add_dataset(
    name="zprime_tt_m_1200_w_360_madgraph",
    id=14281223,
    processes=[procs.zprime_tt_m_1200_w_360],
    keys=[
        "/ZPrimeToTT_M1200_W360_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_1200_w_12_madgraph",
    id=14229932,
    processes=[procs.zprime_tt_m_1200_w_12],
    keys=[
        "/ZprimeToTT_M1200_W12_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=195613,
)


cpn.add_dataset(
    name="zprime_tt_m_1400_w_140_madgraph",
    id=14282426,
    processes=[procs.zprime_tt_m_1400_w_140],
    keys=[
        "/ZPrimeToTT_M1400_W140_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_1400_w_420_madgraph",
    id=14281274,
    processes=[procs.zprime_tt_m_1400_w_420],
    keys=[
        "/ZPrimeToTT_M1400_W420_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=488000,
)


cpn.add_dataset(
    name="zprime_tt_m_1400_w_14_madgraph",
    id=14230187,
    processes=[procs.zprime_tt_m_1400_w_14],
    keys=[
        "/ZprimeToTT_M1400_W14_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=208708,
)


cpn.add_dataset(
    name="zprime_tt_m_1600_w_160_madgraph",
    id=14281016,
    processes=[procs.zprime_tt_m_1600_w_160],
    keys=[
        "/ZPrimeToTT_M1600_W160_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=494000,
)


cpn.add_dataset(
    name="zprime_tt_m_1600_w_480_madgraph",
    id=14281289,
    processes=[procs.zprime_tt_m_1600_w_480],
    keys=[
        "/ZPrimeToTT_M1600_W480_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=497000,
)


cpn.add_dataset(
    name="zprime_tt_m_1600_w_16_madgraph",
    id=14231201,
    processes=[procs.zprime_tt_m_1600_w_16],
    keys=[
        "/ZprimeToTT_M1600_W16_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=219802,
)


cpn.add_dataset(
    name="zprime_tt_m_1800_w_180_madgraph",
    id=14282425,
    processes=[procs.zprime_tt_m_1800_w_180],
    keys=[
        "/ZPrimeToTT_M1800_W180_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=491000,
)


cpn.add_dataset(
    name="zprime_tt_m_1800_w_540_madgraph",
    id=14281392,
    processes=[procs.zprime_tt_m_1800_w_540],
    keys=[
        "/ZPrimeToTT_M1800_W540_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_1800_w_18_madgraph",
    id=14227878,
    processes=[procs.zprime_tt_m_1800_w_18],
    keys=[
        "/ZprimeToTT_M1800_W18_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=208252,
)


cpn.add_dataset(
    name="zprime_tt_m_2000_w_200_madgraph",
    id=14281145,
    processes=[procs.zprime_tt_m_2000_w_200],
    keys=[
        "/ZPrimeToTT_M2000_W200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_2000_w_600_madgraph",
    id=14251230,
    processes=[procs.zprime_tt_m_2000_w_600],
    keys=[
        "/ZPrimeToTT_M2000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_2000_w_20_madgraph",
    id=14229693,
    processes=[procs.zprime_tt_m_2000_w_20],
    keys=[
        "/ZprimeToTT_M2000_W20_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=211425,
)


cpn.add_dataset(
    name="zprime_tt_m_2500_w_250_madgraph",
    id=14281310,
    processes=[procs.zprime_tt_m_2500_w_250],
    keys=[
        "/ZPrimeToTT_M2500_W250_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=489000,
)


cpn.add_dataset(
    name="zprime_tt_m_2500_w_750_madgraph",
    id=14281195,
    processes=[procs.zprime_tt_m_2500_w_750],
    keys=[
        "/ZPrimeToTT_M2500_W750_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_2500_w_25_madgraph",
    id=14229120,
    processes=[procs.zprime_tt_m_2500_w_25],
    keys=[
        "/ZprimeToTT_M2500_W25_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=203518,
)


cpn.add_dataset(
    name="zprime_tt_m_3000_w_300_madgraph",
    id=14281572,
    processes=[procs.zprime_tt_m_3000_w_300],
    keys=[
        "/ZPrimeToTT_M3000_W300_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=491000,
)


cpn.add_dataset(
    name="zprime_tt_m_3000_w_900_madgraph",
    id=14281154,
    processes=[procs.zprime_tt_m_3000_w_900],
    keys=[
        "/ZPrimeToTT_M3000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=488000,
)


cpn.add_dataset(
    name="zprime_tt_m_3000_w_30_madgraph",
    id=14229343,
    processes=[procs.zprime_tt_m_3000_w_30],
    keys=[
        "/ZprimeToTT_M3000_W30_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=192535,
)


cpn.add_dataset(
    name="zprime_tt_m_3500_w_350_madgraph",
    id=14281316,
    processes=[procs.zprime_tt_m_3500_w_350],
    keys=[
        "/ZPrimeToTT_M3500_W350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_3500_w_1050_madgraph",
    id=14281186,
    processes=[procs.zprime_tt_m_3500_w_1050],
    keys=[
        "/ZPrimeToTT_M3500_W1050_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_3500_w_35_madgraph",
    id=14231079,
    processes=[procs.zprime_tt_m_3500_w_35],
    keys=[
        "/ZprimeToTT_M3500_W35_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=189565,
)


cpn.add_dataset(
    name="zprime_tt_m_4000_w_400_madgraph",
    id=14284374,
    processes=[procs.zprime_tt_m_4000_w_400],
    keys=[
        "/ZPrimeToTT_M4000_W400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_4000_w_1200_madgraph",
    id=14277978,
    processes=[procs.zprime_tt_m_4000_w_1200],
    keys=[
        "/ZPrimeToTT_M4000_W1200_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_4000_w_40_madgraph",
    id=14229745,
    processes=[procs.zprime_tt_m_4000_w_40],
    keys=[
        "/ZprimeToTT_M4000_W40_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=184083,
)


cpn.add_dataset(
    name="zprime_tt_m_4500_w_450_madgraph",
    id=14283349,
    processes=[procs.zprime_tt_m_4500_w_450],
    keys=[
        "/ZPrimeToTT_M4500_W450_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_4500_w_1350_madgraph",
    id=14284730,
    processes=[procs.zprime_tt_m_4500_w_1350],
    keys=[
        "/ZPrimeToTT_M4500_W1350_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=500000,
)


cpn.add_dataset(
    name="zprime_tt_m_4500_w_45_madgraph",
    id=14229612,
    processes=[procs.zprime_tt_m_4500_w_45],
    keys=[
        "/ZprimeToTT_M4500_W45_TuneCP2_PSweights_13TeV-madgraph-pythiaMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=174039,
)


cpn.add_dataset(
    name="zprime_tt_m_5000_w_500_madgraph",
    id=14332776,
    processes=[procs.zprime_tt_m_5000_w_500],
    keys=[
        "/ZPrimeToTT_M5000_W500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_5000_w_1500_madgraph",
    id=14349020,
    processes=[procs.zprime_tt_m_5000_w_1500],
    keys=[
        "/ZPrimeToTT_M5000_W1500_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_5000_w_50_madgraph",
    id=14336465,
    processes=[procs.zprime_tt_m_5000_w_50],
    keys=[
        "/ZprimeToTTJets_M5000_W50_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=194238,
)


cpn.add_dataset(
    name="zprime_tt_m_6000_w_600_madgraph",
    id=14333187,
    processes=[procs.zprime_tt_m_6000_w_600],
    keys=[
        "/ZPrimeToTT_M6000_W600_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=197000,
)


cpn.add_dataset(
    name="zprime_tt_m_6000_w_1800_madgraph",
    id=14333643,
    processes=[procs.zprime_tt_m_6000_w_1800],
    keys=[
        "/ZPrimeToTT_M6000_W1800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_6000_w_60_madgraph",
    id=14344862,
    processes=[procs.zprime_tt_m_6000_w_60],
    keys=[
        "/ZprimeToTTJets_M6000_W60_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=202610,
)


cpn.add_dataset(
    name="zprime_tt_m_7000_w_700_madgraph",
    id=14332787,
    processes=[procs.zprime_tt_m_7000_w_700],
    keys=[
        "/ZPrimeToTT_M7000_W700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_7000_w_2100_madgraph",
    id=14332786,
    processes=[procs.zprime_tt_m_7000_w_2100],
    keys=[
        "/ZPrimeToTT_M7000_W2100_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_7000_w_70_madgraph",
    id=14336584,
    processes=[procs.zprime_tt_m_7000_w_70],
    keys=[
        "/ZprimeToTTJets_M7000_W70_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=192854,
)


cpn.add_dataset(
    name="zprime_tt_m_8000_w_800_madgraph",
    id=14341073,
    processes=[procs.zprime_tt_m_8000_w_800],
    keys=[
        "/ZPrimeToTT_M8000_W800_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=190000,
)


cpn.add_dataset(
    name="zprime_tt_m_8000_w_2400_madgraph",
    id=14341059,
    processes=[procs.zprime_tt_m_8000_w_2400],
    keys=[
        "/ZPrimeToTT_M8000_W2400_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_8000_w_80_madgraph",
    id=14345474,
    processes=[procs.zprime_tt_m_8000_w_80],
    keys=[
        "/ZprimeToTTJets_M8000_W80_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=191551,
)


cpn.add_dataset(
    name="zprime_tt_m_9000_w_900_madgraph",
    id=14333371,
    processes=[procs.zprime_tt_m_9000_w_900],
    keys=[
        "/ZPrimeToTT_M9000_W900_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_9000_w_2700_madgraph",
    id=14332759,
    processes=[procs.zprime_tt_m_9000_w_2700],
    keys=[
        "/ZPrimeToTT_M9000_W2700_TuneCP2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=200000,
)


cpn.add_dataset(
    name="zprime_tt_m_9000_w_90_madgraph",
    id=14342305,
    processes=[procs.zprime_tt_m_9000_w_90],
    keys=[
        "/ZprimeToTTJets_M9000_W90_TuneCP2_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=182122,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_91p25_res_madgraph",
    id=14274405,
    processes=[procs.hpseudo_tt_sl_m_365_w_91p25_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=497000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_91p25_int_madgraph",
    id=14275759,
    processes=[procs.hpseudo_tt_sl_m_365_w_91p25_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_36p5_res_madgraph",
    id=14275955,
    processes=[procs.hpseudo_tt_sl_m_365_w_36p5_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=494000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_36p5_int_madgraph",
    id=14281052,
    processes=[procs.hpseudo_tt_sl_m_365_w_36p5_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=497000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_9p125_res_madgraph",
    id=14275721,
    processes=[procs.hpseudo_tt_sl_m_365_w_9p125_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_365_w_9p125_int_madgraph",
    id=14277890,
    processes=[procs.hpseudo_tt_sl_m_365_w_9p125_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_100p0_res_madgraph",
    id=14274326,
    processes=[procs.hpseudo_tt_sl_m_400_w_100p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_100p0_int_madgraph",
    id=14272588,
    processes=[procs.hpseudo_tt_sl_m_400_w_100p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=488000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_40p0_res_madgraph",
    id=14275830,
    processes=[procs.hpseudo_tt_sl_m_400_w_40p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=497000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_40p0_int_madgraph",
    id=14276084,
    processes=[procs.hpseudo_tt_sl_m_400_w_40p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_10p0_res_madgraph",
    id=14240629,
    processes=[procs.hpseudo_tt_sl_m_400_w_10p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=488000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_400_w_10p0_int_madgraph",
    id=14240655,
    processes=[procs.hpseudo_tt_sl_m_400_w_10p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=458000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_125p0_res_madgraph",
    id=14276068,
    processes=[procs.hpseudo_tt_sl_m_500_w_125p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_125p0_int_madgraph",
    id=14274305,
    processes=[procs.hpseudo_tt_sl_m_500_w_125p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_50p0_res_madgraph",
    id=14276098,
    processes=[procs.hpseudo_tt_sl_m_500_w_50p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_50p0_int_madgraph",
    id=14275833,
    processes=[procs.hpseudo_tt_sl_m_500_w_50p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=482000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_12p5_res_madgraph",
    id=14274303,
    processes=[procs.hpseudo_tt_sl_m_500_w_12p5_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_500_w_12p5_int_madgraph",
    id=14275598,
    processes=[procs.hpseudo_tt_sl_m_500_w_12p5_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_150p0_res_madgraph",
    id=14275768,
    processes=[procs.hpseudo_tt_sl_m_600_w_150p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=497000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_150p0_int_madgraph",
    id=14279461,
    processes=[procs.hpseudo_tt_sl_m_600_w_150p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_60p0_res_madgraph",
    id=14278291,
    processes=[procs.hpseudo_tt_sl_m_600_w_60p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_60p0_int_madgraph",
    id=14281149,
    processes=[procs.hpseudo_tt_sl_m_600_w_60p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_15p0_res_madgraph",
    id=14276407,
    processes=[procs.hpseudo_tt_sl_m_600_w_15p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_600_w_15p0_int_madgraph",
    id=14274442,
    processes=[procs.hpseudo_tt_sl_m_600_w_15p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=496000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_200p0_res_madgraph",
    id=14275481,
    processes=[procs.hpseudo_tt_sl_m_800_w_200p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_200p0_int_madgraph",
    id=14276069,
    processes=[procs.hpseudo_tt_sl_m_800_w_200p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=491000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_80p0_res_madgraph",
    id=14276012,
    processes=[procs.hpseudo_tt_sl_m_800_w_80p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_80p0_int_madgraph",
    id=14276360,
    processes=[procs.hpseudo_tt_sl_m_800_w_80p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=498000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_20p0_res_madgraph",
    id=14279434,
    processes=[procs.hpseudo_tt_sl_m_800_w_20p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_800_w_20p0_int_madgraph",
    id=14296517,
    processes=[procs.hpseudo_tt_sl_m_800_w_20p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=467000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_250p0_res_madgraph",
    id=14277928,
    processes=[procs.hpseudo_tt_sl_m_1000_w_250p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=498000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_250p0_int_madgraph",
    id=14274475,
    processes=[procs.hpseudo_tt_sl_m_1000_w_250p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_100p0_res_madgraph",
    id=14274418,
    processes=[procs.hpseudo_tt_sl_m_1000_w_100p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_100p0_int_madgraph",
    id=14274332,
    processes=[procs.hpseudo_tt_sl_m_1000_w_100p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=500000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_25p0_res_madgraph",
    id=14241343,
    processes=[procs.hpseudo_tt_sl_m_1000_w_25p0_res],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=497000,
)


cpn.add_dataset(
    name="hpseudo_tt_sl_m_1000_w_25p0_int_madgraph",
    id=14249272,
    processes=[procs.hpseudo_tt_sl_m_1000_w_25p0_int],
    keys=[
        "/HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_91p25_res_madgraph",
    id=14274676,
    processes=[procs.hscalar_tt_sl_m_365_w_91p25_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w91p25_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=496000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_91p25_int_madgraph",
    id=14274334,
    processes=[procs.hscalar_tt_sl_m_365_w_91p25_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w91p25_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_36p5_res_madgraph",
    id=14279145,
    processes=[procs.hscalar_tt_sl_m_365_w_36p5_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w36p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=494000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_36p5_int_madgraph",
    id=14289222,
    processes=[procs.hscalar_tt_sl_m_365_w_36p5_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w36p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_9p125_res_madgraph",
    id=14274416,
    processes=[procs.hscalar_tt_sl_m_365_w_9p125_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w9p125_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_365_w_9p125_int_madgraph",
    id=14281021,
    processes=[procs.hscalar_tt_sl_m_365_w_9p125_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m365_w9p125_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=497000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_100p0_res_madgraph",
    id=14275618,
    processes=[procs.hscalar_tt_sl_m_400_w_100p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_100p0_int_madgraph",
    id=14274362,
    processes=[procs.hscalar_tt_sl_m_400_w_100p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_40p0_res_madgraph",
    id=14288310,
    processes=[procs.hscalar_tt_sl_m_400_w_40p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w40p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_40p0_int_madgraph",
    id=14274962,
    processes=[procs.hscalar_tt_sl_m_400_w_40p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w40p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_10p0_res_madgraph",
    id=14251426,
    processes=[procs.hscalar_tt_sl_m_400_w_10p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w10p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=491000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_400_w_10p0_int_madgraph",
    id=14248632,
    processes=[procs.hscalar_tt_sl_m_400_w_10p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m400_w10p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_125p0_res_madgraph",
    id=14274427,
    processes=[procs.hscalar_tt_sl_m_500_w_125p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w125p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_125p0_int_madgraph",
    id=14275741,
    processes=[procs.hscalar_tt_sl_m_500_w_125p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w125p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=485000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_50p0_res_madgraph",
    id=14275773,
    processes=[procs.hscalar_tt_sl_m_500_w_50p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w50p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_50p0_int_madgraph",
    id=14275783,
    processes=[procs.hscalar_tt_sl_m_500_w_50p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w50p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=497000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_12p5_res_madgraph",
    id=14275965,
    processes=[procs.hscalar_tt_sl_m_500_w_12p5_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w12p5_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_500_w_12p5_int_madgraph",
    id=14275799,
    processes=[procs.hscalar_tt_sl_m_500_w_12p5_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m500_w12p5_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_150p0_res_madgraph",
    id=14278372,
    processes=[procs.hscalar_tt_sl_m_600_w_150p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w150p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_150p0_int_madgraph",
    id=14275881,
    processes=[procs.hscalar_tt_sl_m_600_w_150p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w150p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_60p0_res_madgraph",
    id=14277937,
    processes=[procs.hscalar_tt_sl_m_600_w_60p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w60p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=497000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_60p0_int_madgraph",
    id=14281292,
    processes=[procs.hscalar_tt_sl_m_600_w_60p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w60p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_15p0_res_madgraph",
    id=14277655,
    processes=[procs.hscalar_tt_sl_m_600_w_15p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w15p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_600_w_15p0_int_madgraph",
    id=14281221,
    processes=[procs.hscalar_tt_sl_m_600_w_15p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m600_w15p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_200p0_res_madgraph",
    id=14279147,
    processes=[procs.hscalar_tt_sl_m_800_w_200p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w200p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=498000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_200p0_int_madgraph",
    id=14276378,
    processes=[procs.hscalar_tt_sl_m_800_w_200p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w200p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_80p0_res_madgraph",
    id=14275775,
    processes=[procs.hscalar_tt_sl_m_800_w_80p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w80p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=497000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_80p0_int_madgraph",
    id=14276054,
    processes=[procs.hscalar_tt_sl_m_800_w_80p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w80p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_20p0_res_madgraph",
    id=14277314,
    processes=[procs.hscalar_tt_sl_m_800_w_20p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w20p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_800_w_20p0_int_madgraph",
    id=14279331,
    processes=[procs.hscalar_tt_sl_m_800_w_20p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m800_w20p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=494000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_250p0_res_madgraph",
    id=14278458,
    processes=[procs.hscalar_tt_sl_m_1000_w_250p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w250p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_250p0_int_madgraph",
    id=14274336,
    processes=[procs.hscalar_tt_sl_m_1000_w_250p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w250p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_100p0_res_madgraph",
    id=14275860,
    processes=[procs.hscalar_tt_sl_m_1000_w_100p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w100p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_100p0_int_madgraph",
    id=14275758,
    processes=[procs.hscalar_tt_sl_m_1000_w_100p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w100p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=496000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_25p0_res_madgraph",
    id=14241206,
    processes=[procs.hscalar_tt_sl_m_1000_w_25p0_res],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w25p0_res_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=500000,
)


cpn.add_dataset(
    name="hscalar_tt_sl_m_1000_w_25p0_int_madgraph",
    id=14241488,
    processes=[procs.hscalar_tt_sl_m_1000_w_25p0_int],
    keys=[
        "/HscalarToTTTo1L1Nu2J_m1000_w25p0_int_TuneCP5_13TeV-madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=482000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_500_pythia",
    id=14231292,
    processes=[procs.rsgluon_tt_m_500],
    keys=[
        "/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=500000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_1000_pythia",
    id=14231929,
    processes=[procs.rsgluon_tt_m_1000],
    keys=[
        "/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=485000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_1500_pythia",
    id=14227364,
    processes=[procs.rsgluon_tt_m_1500],
    keys=[
        "/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_2000_pythia",
    id=14230161,
    processes=[procs.rsgluon_tt_m_2000],
    keys=[
        "/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=494000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_2500_pythia",
    id=14231336,
    processes=[procs.rsgluon_tt_m_2500],
    keys=[
        "/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=497000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_3000_pythia",
    id=14232264,
    processes=[procs.rsgluon_tt_m_3000],
    keys=[
        "/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=500000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_3500_pythia",
    id=14231628,
    processes=[procs.rsgluon_tt_m_3500],
    keys=[
        "/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=497000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_4000_pythia",
    id=14231303,
    processes=[procs.rsgluon_tt_m_4000],
    keys=[
        "/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=497000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_4500_pythia",
    id=14231632,
    processes=[procs.rsgluon_tt_m_4500],
    keys=[
        "/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=488000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_5000_pythia",
    id=14231549,
    processes=[procs.rsgluon_tt_m_5000],
    keys=[
        "/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=500000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_5500_pythia",
    id=14231358,
    processes=[procs.rsgluon_tt_m_5500],
    keys=[
        "/RSGluonToTT_M-5500_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=494000,
)


cpn.add_dataset(
    name="rsgluon_tt_m_6000_pythia",
    id=14231365,
    processes=[procs.rsgluon_tt_m_6000],
    keys=[
        "/RSGluonToTT_M-6000_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=500000,
)
