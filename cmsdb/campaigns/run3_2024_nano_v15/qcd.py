
# coding: utf-8

""""
QCD datasets for the run3_2024_nano_v15 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# QCD
#

# muon enriched, pt-binned

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=15316273,
    processes=[procs.qcd_mu_pt15to20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-15to20_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=859,  # 859-0
            n_events=124873343,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=15315886,
    processes=[procs.qcd_mu_pt20to30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-20to30_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=657,  # 657-0
            n_events=93246015,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=15315309,
    processes=[procs.qcd_mu_pt30to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-30to50_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=729,  # 729-0
            n_events=95229839,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=15316568,
    processes=[procs.qcd_mu_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-50to80_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=714,  # 714-0
            n_events=107361868,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=15316584,
    processes=[procs.qcd_mu_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=680,  # 680-0
            n_events=94158748,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=15316135,
    processes=[procs.qcd_mu_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=683,  # 683-0
            n_events=99977764,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=15315581,
    processes=[procs.qcd_mu_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=695,  # 695-0
            n_events=94354003,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=15315699,
    processes=[procs.qcd_mu_pt300to470],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=591,  # 591-0
            n_events=79686379,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=15316109,
    processes=[procs.qcd_mu_pt470to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=590,  # 590-0
            n_events=71842009,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=15315212,
    processes=[procs.qcd_mu_pt600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=764,  # 764-0
            n_events=85759452,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=15315633,
    processes=[procs.qcd_mu_pt800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=673,  # 673-0
            n_events=81633640,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_mu_pt1000toinf_pythia",
    id=15316533,
    processes=[procs.qcd_mu_pt1000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-PT-1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=703,  # 703-0
            n_events=87267908,
        ),
    ),
)

# double em enriched, pt > 30, 40 < m_gg < 80 

cpn.add_dataset(
    name="qcd_doubleem_pt30toinf_mgg40to80_pythia",
    id=15316662,
    processes=[procs.qcd_doubleem_pt30toinf_mgg40to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-MGG-40to80-PT-30_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=169,  # 169-0
            n_events=26481058,
        ),
    ),
)

# double em enriched, pt-binned, m_gg > 80

cpn.add_dataset(
    name="qcd_doubleem_pt30to40_mgg80toinf_pythia",
    id=15315165,
    processes=[procs.qcd_doubleem_pt30to40_mgg80toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-MGG-80-PT-30to40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=160,  # 160-0
            n_events=13681212,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_doubleem_pt40toinf_mgg80toinf_pythia",
    id=15295980,
    processes=[procs.qcd_doubleem_pt40toinf_mgg80toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_Bin-MGG-80-PT-40_Fil-DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=190,  # 190-0
            n_events=27404416,
        ),
    ),
)

# ht-binned

cpn.add_dataset(
    name="qcd_ht40to70_madgraph",
    id=15301246,
    processes=[procs.qcd_ht40to70],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=123,  # 123-0
            n_events=110777315,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht70to100_madgraph",
    id=15300355,
    processes=[procs.qcd_ht70to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=136,  # 136-0
            n_events=108584880,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht100to200_madgraph",
    id=15291916,
    processes=[procs.qcd_ht100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=169,  # 169-0
            n_events=120453600,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht200to400_madgraph",
    id=15300347,
    processes=[procs.qcd_ht200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=163,  # 163-0
            n_events=115255250,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht400to600_madgraph",
    id=15300312,
    processes=[procs.qcd_ht400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=173,  # 173-0
            n_events=106725734,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht600to800_madgraph",
    id=15300360,
    processes=[procs.qcd_ht600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=229,  # 229-0
            n_events=128235651,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht800to1000_madgraph",
    id=15300390,
    processes=[procs.qcd_ht800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=262,  # 262-0
            n_events=124956604,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1000to1200_madgraph",
    id=15301287,
    processes=[procs.qcd_ht1000to1200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=224,  # 224-0
            n_events=114436708,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1200to1500_madgraph",
    id=15291917,
    processes=[procs.qcd_ht1200to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=230,  # 230-0
            n_events=107835822,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht1500to2000_madgraph",
    id=15300329,
    processes=[procs.qcd_ht1500to2000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=248,  # 248-0
            n_events=113208234,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_ht2000toinf_madgraph",
    id=15291920,
    processes=[procs.qcd_ht2000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD-4Jets_Bin-HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=221,  # 221-0
            n_events=91953615,
        ),
    ),
)

