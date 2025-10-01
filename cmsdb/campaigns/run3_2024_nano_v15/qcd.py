# coding: utf-8

"""
QCD datasets for the 2022 pre-EE data-taking campaign
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v14 import campaign_run3_2024_nano_v14 as cpn


#
# QCD (pythia, pt-binned, muon enriched) (different threshold than before?)
#

cpn.add_dataset(
    name="qcd_fil_mu_pt15to20_pythia",
    id=15316273,
    processes=[procs.qcd_fil_mu_pt15to20],
    keys=[
        "/QCD_Bin-PT-15to20_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=859,
    n_events=124873343,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt20to30_pythia",
    id=15315886,
    processes=[procs.qcd_fil_mu_pt20to30],
    keys=[
        "/QCD_Bin-PT-20to30_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=657,
    n_events=93246015,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt30to50_pythia",
    id=15315309,
    processes=[procs.qcd_fil_mu_pt30to50],
    keys=[
        "/QCD_Bin-PT-30to50_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=729,
    n_events=95229839,

)

cpn.add_dataset(
    name="qcd_fil_mu_pt50to80_pythia",
    id=15316568,
    processes=[procs.qcd_fil_mu_pt50to80],
    keys=[
        "/QCD_Bin-PT-50to80_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=714,
    n_events=107361868,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt80to120_pythia",
    id=15316584,
    processes=[procs.qcd_fil_mu_pt80to120],
    keys=[
        "/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=680,
    n_events=94158748,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt120to170_pythia",
    id=15316135,
    processes=[procs.qcd_fil_mu_pt120to170],
    keys=[
        "/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=683,
    n_events=99977764,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt170to300_pythia",
    id=15315581,
    processes=[procs.qcd_fil_mu_pt170to300],
    keys=[
        "/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=695,
    n_events=94354003,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt300to470_pythia",
    id=15315699,
    processes=[procs.qcd_fil_mu_pt300to470],
    keys=[
        "/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=591,
    n_events=79686379,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt470to600_pythia",
    id=15316109,
    processes=[procs.qcd_fil_mu_pt470to600],
    keys=[
        "/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=590,
    n_events=71842009,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt600to800_pythia",
    id=15315212,
    processes=[procs.qcd_fil_mu_pt600to800],
    keys=[
        "/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=764,
    n_events=85759452,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt800to1000_pythia",
    id=15315633,
    processes=[procs.qcd_fil_mu_pt800to1000],
    keys=[
        "/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=673,
    n_events=81633640,
)

cpn.add_dataset(
    name="qcd_fil_mu_pt1000toinf_pythia",
    id=15316533,
    processes=[procs.qcd_fil_mu_pt1000toinf],
    keys=[
        "/QCD_Bin-PT-1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=703,
    n_events=87267908,
)

#
# QCD (pythia, pt-binned, electron enriched)
#

# Not yet

#
# QCD (pythia, pt-binned, double electron enriched)
#

cpn.add_dataset(
    name="qcd_doubleem_pt30to40_mgg80toinf_pythia",
    id=15315165,
    processes=[procs.qcd_doubleem_pt30to40_mgg80toinf],
    keys=[
        "/QCD_Bin-MGG-80-PT-30to40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
    ],
    n_files=160,
    n_events=13681212,
)

cpn.add_dataset(
    name="qcd_doubleem_pt30toinf_mgg40to80_pythia",
    id=15316662,
    processes=[procs.qcd_doubleem_pt30toinf_mgg40to80],
    keys=[
        "/QCD_Bin-MGG-40to80-PT-30_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
    ],
    n_files=169,
    n_events=26481058,
)

cpn.add_dataset(
    name="qcd_doubleem_pt40toinf_mgg80toinf_pythia",
    id=15295980,
    processes=[procs.qcd_doubleem_pt40toinf_mgg80toinf],
    keys=[
        "/QCD_Bin-MGG-80-PT-40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
    ],
    n_files=190,
    n_events=27404416,
)

#
# QCD (pythia, pt-binned)
#

cpn.add_dataset(
    name="qcd_pt15to20",
    id=15315874,
    processes=[procs.qcd_pt15to20],
    keys=[
        "/QCD_Bin-PT-15to20_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=566,
    n_events=99984691,
)

cpn.add_dataset(
    name="qcd_pt20to30",
    id=15316550,
    processes=[procs.qcd_pt20to30],
    keys=[
        "/QCD_Bin-PT-20to30_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=578,
    n_events=99972336,
)

cpn.add_dataset(
    name="qcd_pt30to50",
    id=15315325,
    processes=[procs.qcd_pt30to50],
    keys=[
        "/QCD_Bin-PT-30to50_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=631,
    n_events=99983302,
)

cpn.add_dataset(
    name="qcd_pt50to80",
    id=15315188,
    processes=[procs.qcd_pt50to80],
    keys=[
        "/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=660,
    n_events=97814968,
)

cpn.add_dataset(
    name="qcd_pt80to120",
    id=15315195,
    processes=[procs.qcd_pt80to120],
    keys=[
        "/QCD_Bin-PT-80to120_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=750,
    n_events=99244066,
)

cpn.add_dataset(
    name="qcd_pt120to170",
    id=15316666,
    processes=[procs.qcd_pt120to170],
    keys=[
        "/QCD_Bin-PT-120to170_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=668,
    n_events=99956202,
)

cpn.add_dataset(
    name="qcd_pt170to300",
    id=15316566,
    processes=[procs.qcd_pt170to300],
    keys=[
        "/QCD_Bin-PT-170to300_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=678,
    n_events=99860965,

)

cpn.add_dataset(
    name="qcd_pt300to470",
    id=15315306,
    processes=[procs.qcd_pt300to470],
    keys=[
        "/QCD_Bin-PT-300to470_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=630,
    n_events=79821382,
)

cpn.add_dataset(
    name="qcd_pt470to600",
    id=15316542,
    processes=[procs.qcd_pt470to600],
    keys=[
        "/QCD_Bin-PT-470to600_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=600,  # 600-0
    n_events=77529080,
)

cpn.add_dataset(
    name="qcd_pt600to800",
    id=15315319,
    processes=[procs.qcd_pt600to800],
    keys=[
        "/QCD_Bin-PT-600to800_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=690,  # 690-0
    n_events=79708520,
)

cpn.add_dataset(
    name="qcd_pt800to1000",
    id=15315356,
    processes=[procs.qcd_pt800to1000],
    keys=[
        "/QCD_Bin-PT-800to1000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=650,
    n_events=79505640,
)

cpn.add_dataset(
    name="qcd_pt1000to1500",
    id=15315846,
    processes=[procs.qcd_pt1000to1500],
    keys=[
        "/QCD_Bin-PT-1000to1500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=621,
    n_events=79974618,
)

cpn.add_dataset(
    name="qcd_pt1500to2000",
    id=15315893,
    processes=[procs.qcd_pt1500to2000],
    keys=[
        "/QCD_Bin-PT-1500to2000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=225,
    n_events=19997308,
)

cpn.add_dataset(
    name="qcd_pt2000to2500",
    id=15315211,
    processes=[procs.qcd_pt2000to2500],
    keys=[
        "/QCD_Bin-PT-2000to2500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=250,
    n_events=19311060,
)

cpn.add_dataset(
    name="qcd_pt2500to3000",
    id=15315583,
    processes=[procs.qcd_pt2500to3000],
    keys=[
        "/QCD_Bin-PT-2500to3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=222,
    n_events=19996725,
)

cpn.add_dataset(
    name="qcd_pt3000toinf",
    id=15315205,
    processes=[procs.qcd_pt3000toinf],
    keys=[
        "/QCD_Bin-PT-3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=315,
    n_events=19347697,
)

#
# QCD (pythia, ht-binned)
#

cpn.add_dataset(
    name="qcd_ht40to70",
    id=15301246,
    processes=[procs.qcd_ht40to70],
    keys=[
        "/QCD-4Jets_Bin-HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=123,
    n_events=110777315,
)

cpn.add_dataset(
    name="qcd_ht70to100",
    id=15300355,
    processes=[procs.qcd_ht70to100],
    keys=[
        "/QCD-4Jets_Bin-HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=136,
    n_events=108584880,
)

cpn.add_dataset(
    name="qcd_ht100to200",
    id=15291916,
    processes=[procs.qcd_ht100to200],
    keys=[
        "/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=169,  # 169-0
    n_events=120453600,
)

cpn.add_dataset(
    name="qcd_ht200to400",
    id=15300347,
    processes=[procs.qcd_ht200to400],
    keys=[
        "/QCD-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=163,
    n_events=115255250,
)

cpn.add_dataset(
    name="qcd_ht400to600",
    id=15300312,
    processes=[procs.qcd_ht400to600],
    keys=[
        "/QCD-4Jets_Bin-HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=173,
    n_events=106725734,
)

cpn.add_dataset(
    name="qcd_ht600to800",
    id=15300360,
    processes=[procs.qcd_ht600to800],
    keys=[
        "/QCD-4Jets_Bin-HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=229,
    n_events=128235651,
)

cpn.add_dataset(
    name="qcd_ht800to1000",
    id=15300390,
    processes=[procs.qcd_ht800to1000],
    keys=[
        "/QCD-4Jets_Bin-HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=262,
    n_events=124956604,
)

cpn.add_dataset(
    name="qcd_ht1000to1200",
    id=15301287,
    processes=[procs.qcd_ht1000to1200],
    keys=[
        "/QCD-4Jets_Bin-HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=224,
    n_events=114436708,
)

cpn.add_dataset(
    name="qcd_ht1200to1500",
    id=15291917,
    processes=[procs.qcd_ht1200to1500],
    keys=[
        "/QCD-4Jets_Bin-HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=230,
    n_events=107835822,
)

cpn.add_dataset(
    name="qcd_ht1500to2000",
    id=15300329,
    processes=[procs.qcd_ht1500to2000],
    keys=[
        "/QCD-4Jets_Bin-HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=248,
    n_events=113208234,
)

cpn.add_dataset(
    name="qcd_ht2000toinf",
    id=15291920,
    processes=[procs.qcd_ht2000toinf],
    keys=[
        "/QCD-4Jets_Bin-HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
    ],
    n_files=221,
    n_events=91953615,
)
