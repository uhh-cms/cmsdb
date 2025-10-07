# coding: utf-8

"""
Electroweak datasets for the 2024 data-taking campaign (Nano v15)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import run3_2024_nano_v15 as cpn

####################################################################################################
#
# Drell-Yan
#
####################################################################################################


# inclusive, LO, forPog (above 50)
cpn.add_dataset(
    name="dy_m50toinf_for_pog_madgraph",
    id=15237161,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-Pilot2024wmLHEGS_150X_mcRun3_2024_realistic_v1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1,
            n_events=20023,
        ),
    ),
)

# powheg, binned in EE/MuMu/Mll

# e
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=15297455,
    processes=[procs.dy_ee_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=395,
            n_events=348121585,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=15296064,
    processes=[procs.dy_ee_m50to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=656,
            n_events=477172288,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=15304457,
    processes=[procs.dy_ee_m120to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=110,
            n_events=48821981,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=15302364,
    processes=[procs.dy_ee_m200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,
            n_events=6823360,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=15304418,
    processes=[procs.dy_ee_m400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=14,
            n_events=977525,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=15304552,
    processes=[procs.dy_ee_m800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,
            n_events=992750,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=15304463,
    processes=[procs.dy_ee_m1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,
            n_events=998592,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=15304648,
    processes=[procs.dy_ee_m2500to4000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,
            n_events=996630,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=15297360,
    processes=[procs.dy_ee_m4000to6000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=7,
            n_events=984688,
        ),
    ),
)

cpn.add_dataset(
    name="dy_ee_m6000toinf_powheg",
    id=15304478,
    processes=[procs.dy_ee_m6000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=21,
            n_events=998101,
        ),
    ),
)

# mu

cpn.add_dataset(
    name="dy_mumu_m10to50_powheg",
    id=15297453,
    processes=[procs.dy_mumu_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=405,
            n_events=341634068,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m50to120_powheg",
    id=15304408,
    processes=[procs.dy_mumu_m50to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=640,
            n_events=492270708,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m120to200_powheg",
    id=15304438,
    processes=[procs.dy_mumu_m120to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=110,
            n_events=48037000,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m200to400_powheg",
    id=15304520,
    processes=[procs.dy_mumu_m200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,
            n_events=6588316,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m400to800_powheg",
    id=15304525,
    processes=[procs.dy_mumu_m400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,
            n_events=977500,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m800to1500_powheg",
    id=15304358,
    processes=[procs.dy_mumu_m800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,
            n_events=979723,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m1500to2500_powheg",
    id=15304537,
    processes=[procs.dy_mumu_m1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,
            n_events=962340,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m2500to4000_powheg",
    id=15304508,
    processes=[procs.dy_mumu_m2500to4000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,
            n_events=934352,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m4000to6000_powheg",
    id=15304549,
    processes=[procs.dy_mumu_m4000to6000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=9,
            n_events=999261,
        ),
    ),
)

cpn.add_dataset(
    name="dy_mumu_m6000toinf_powheg",
    id=15304533,
    processes=[procs.dy_mumu_m6000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=29,
            n_events=998508,
        ),
    ),
)

# tau
cpn.add_dataset(
    name="dy_tautau_m10to50_powheg",
    id=15297458,
    processes=[procs.dy_tautau_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=400,
            n_events=344069532,
        ),
    ),

)
cpn.add_dataset(
    name="dy_tautau_m50to120_powheg",
    id=15297457,
    processes=[procs.dy_tautau_m50to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=564,
            n_events=486994937,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m120to200_powheg",
    id=15304444,
    processes=[procs.dy_tautau_m120to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=113,
            n_events=48376250,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m200to400_powheg",
    id=15304498,
    processes=[procs.dy_tautau_m200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=41,
            n_events=6779206,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m400to800_powheg",
    id=15304534,
    processes=[procs.dy_tautau_m400to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,
            n_events=991838,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m800to1500_powheg",
    id=15304579,
    processes=[procs.dy_tautau_m800to1500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=8,
            n_events=987369,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m1500to2500_powheg",
    id=15304532,
    processes=[procs.dy_tautau_m1500to2500],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,
            n_events=964672,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m2500to4000_powheg",
    id=15304551,
    processes=[procs.dy_tautau_m2500to4000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=24,
            n_events=996340,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m4000to6000_powheg",
    id=15304360,
    processes=[procs.dy_tautau_m4000to6000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,
            n_events=942725,
        ),
    ),
)

cpn.add_dataset(
    name="dy_tautau_m6000toinf_powheg",
    id=15304550,
    processes=[procs.dy_tautau_m6000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,
            n_events=992190,
        ),
    ),
)

# AMCatNLO (incomplete: Mll<50 and MMl>50 pt 0-40...)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=15300236,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3045,  # 3045-0
            n_events=479655476,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=15304428,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=355,  # 355-0
            n_events=227319605,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=15304451,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=22383959,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=15304493,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=10404540,
        ),
    ),
)
cpn.add_dataset(
    name="Pdy_m50toinf_1j_pt600toinf_amcatnlo",
    id=15304449,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=42,  # 42-0
            n_events=9996457,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=15300484,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1787,  # 1787-0
            n_events=247167836,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=15296152,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=389,  # 389-0
            n_events=246696940,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=15304466,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=139,  # 139-0
            n_events=44028174,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=15304446,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=9893470,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=15304548,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=50,  # 50-0
            n_events=9801431,
        ),
    ),
)

# no process/xs yet

"""
cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15300391,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=548,  # 548-0
            n_events=453230267,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15304256,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=534,  # 534-0
            n_events=466773211,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15292625,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v4/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2990,  # 2990-0
            n_events=486448139,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15302208,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Mu-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2975,  # 2975-0
            n_events=490076405,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15397048,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2Tau-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v6/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2784,  # 2784-0
            n_events=572145744,
        ),
    ),
)
"""

####################################################################################################
#
# W boson production
#
####################################################################################################

# NLO up to two jets (leptonic)
cpn.add_dataset(
    name="w_enu_2j_inc_amcatnlo",
    id=15297431,
    processes=[procs.w_enu_2j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoENu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3017,  # 3017-0
            n_events=553868158,
        ),
    ),
)

cpn.add_dataset(
    name="w_munu_2j_inc_amcatnlo",
    id=15292952,
    processes=[procs.w_munu_2j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoMuNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2962,  # 2962-0
            n_events=534824098,
        ),
    ),
)

cpn.add_dataset(
    name="w_taunu_2j_inc_amcatnlo",
    id=15292944,
    processes=[procs.w_taunu_2j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoTauNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2747,  # 2747-0
            n_events=500139084,
        ),
    ),
)

cpn.add_dataset(
    name="w_enu_2j_0j_amcatnlo",
    id=15300303,
    processes=[procs.w_enu_2j_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoENu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=491,  # 491-0
            n_events=478887010,
        ),
    ),
)

cpn.add_dataset(
    name="w_munu_2j_0j_amcatnlo",
    id=15296227,
    processes=[procs.w_munu_2j_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoMuNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=495,  # 495-0
            n_events=464632230,
        ),
    ),
)

cpn.add_dataset(
    name="w_taunu_2j_0j_amcatnlo",
    id=15304427,
    processes=[procs.w_taunu_2j_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoTauNu-2Jets_Bin-0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=504,  # 504-0
            n_events=442672319,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=15297303,
    processes=[procs.w_lnu_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3384,  # 3384-0
            n_events=447467775,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=15300033,
    processes=[procs.w_lnu_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3089,  # 3089-0
            n_events=494167270,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=15304490,
    processes=[procs.w_lnu_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=109,  # 109-0
            n_events=45096548,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=15304489,
    processes=[procs.w_lnu_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=14159808,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=15304609,
    processes=[procs.w_lnu_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=15305397,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=15300032,
    processes=[procs.w_lnu_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3309,  # 3309-0
            n_events=483030994,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=15299994,
    processes=[procs.w_lnu_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3262,  # 3262-0
            n_events=470520533,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=15304499,
    processes=[procs.w_lnu_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=136,  # 136-0
            n_events=75124628,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=15304459,
    processes=[procs.w_lnu_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=51,  # 51-0
            n_events=14222725,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=15304506,
    processes=[procs.w_lnu_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=67,  # 67-0
            n_events=14991109,
        ),
    ),
)

# LO up to four jets (leptonic)
cpn.add_dataset(
    name="w_enu_4j_inc_madgraph",
    id=15301798,
    processes=[procs.w_enu_4j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoENu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2952,  # 2952-0
            n_events=500792358,
        ),
    ),
)

cpn.add_dataset(
    name="w_munu_4j_inc_madgraph",
    id=15305399,
    processes=[procs.w_munu_4j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoMuNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2366,  # 2366-0
            n_events=425220142,
        ),
    ),
)

cpn.add_dataset(
    name="w_taunu_4j_inc_madgraph",
    id=15304606,
    processes=[procs.w_taunu_4j_inc],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoTauNu-4Jets_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2589,  # 2589-0
            n_events=481997294,
        ),
    ),
)

cpn.add_dataset(
    name="w_enu_4j_1j_madgraph",
    id=15300448,
    processes=[procs.w_enu_4j_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoENu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2648,  # 2648-0
            n_events=479079357,
        ),
    ),
)

cpn.add_dataset(
    name="w_munu_4j_1j_madgraph",
    id=15304622,
    processes=[procs.w_munu_4j_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoMuNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2513,  # 2513-0
            n_events=445870925,
        ),
    ),
)

cpn.add_dataset(
    name="w_taunu_4j_1j_madgraph",
    id=15305387,
    processes=[procs.w_taunu_4j_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoTauNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2589,  # 2589-0
            n_events=471084889,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=15316677,
    processes=[procs.w_lnu_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2491,  # 2491-0
            n_events=429800607,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=15298612,
    processes=[procs.w_lnu_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1632,  # 1632-0
            n_events=286526689,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=15298945,
    processes=[procs.w_lnu_3j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=915,  # 915-0
            n_events=139773986,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=15298088,
    processes=[procs.w_lnu_4j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=644,  # 644-0
            n_events=85950957,
        ),
    ),
)

# hadronic/other with no process/xs yet
"""
cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15407579,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-2Jets_Bin-PTQQ-200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=994,  # 994-0
            n_events=156003498,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15407581,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-2Jets_Bin-PTQQ-400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=356,  # 356-0
            n_events=47423661,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15411349,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-2Jets_Bin-PTQQ-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=389,  # 389-0
            n_events=51483908,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=15404212,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-3Jets_Bin-HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1925,  # 1925-0
            n_events=383183449,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=15404438,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-3Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=372,  # 372-0
            n_events=48297099,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_madgraph",
    id=15407704,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Wto2Q-3Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=414,  # 414-0
            n_events=53389988,
        ),
    ),
)

cpn.add_dataset(
    name="PLACEHOLDER_pythia8",
    id=15321748,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoTauNu-Tauto3Mu_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=3963712,
        ),
    ),
)
"""

cpn.add_dataset(
    name="w_vbf_qq_madgraph",
    id=15304404,
    processes=[procs.w_vbf_qq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFWto2Q_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=349,  # 349-0
            n_events=218132349,
        ),
    ),
)

cpn.add_dataset(
    name="z_vbf_zqq_madgraph",
    id=15304454,
    processes=[procs.z_vbf_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFZto2Q_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=74,  # 74-0
            n_events=13834407,
        ),
    ),
)

####################################################################################################
#
# ZZ boson production
#
####################################################################################################
# qqZZ

# inclusive
cpn.add_dataset(
    name="zz_pythia8",
    id=15315163,
    processes=[procs.zz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=4800000,
        ),
    ),
)

# per decay mode
cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=15297464,
    processes=[procs.zz_zll_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=273,  # 273-0
            n_events=236757511,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zqq_zll_powheg",
    id=15304456,
    processes=[procs.zz_zqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=215,  # 215-0
            n_events=171627615,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zll_znunu_powheg",
    id=15304432,
    processes=[procs.zz_zll_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=228,  # 228-0
            n_events=188715312,
        ),
    ),
)

cpn.add_dataset(
    name="zz_znunu_zqq_powheg",
    id=15304447,
    processes=[procs.zz_znunu_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=65,  # 65-0
            n_events=46047410,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zqq_zqq_amcatnlo",
    id=15377566,
    processes=[procs.zz_zqq_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto4Q-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=4971870,
        ),
    ),
)

# split by lepton decay, are the previous ones really ggZZ as the XS indicates? what about qqZZ?

cpn.add_dataset(
    name="zz_zee_zee_pythia8",
    id=15415633,
    processes=[procs.zz_zee_zee],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,  # 33-0
            n_events=2100000,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zee_zmumu_pythia8",
    id=15415905,
    processes=[procs.zz_zee_zmumu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto2E2Mu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
            n_events=2078216,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zee_ztautau_pythia8",
    id=15414868,
    processes=[procs.zz_zee_ztautau],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto2E2Tau_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=51,  # 51-0
            n_events=2100000,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zmumu_zmumu_pythia8",
    id=15415766,
    processes=[procs.zz_zmumu_zmumu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=2097498,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zmumu_ztautau_pythia8",
    id=15415743,
    processes=[procs.zz_zmumu_ztautau],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,  # 31-0
            n_events=2095000,
        ),
    ),
)

cpn.add_dataset(
    name="zz_ztautau_ztautau_pythia8",
    id=15415794,
    processes=[procs.zz_ztautau_ztautau],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlu2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34,  # 34-0
            n_events=2099160,
        ),
    ),
)

####################################################################################################
#
# ZGamma boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# WW boson production
#
####################################################################################################

# inclusive
cpn.add_dataset(
    name="ww_pythia8",
    id=15315231,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=518,  # 518-0
            n_events=63986968,
        ),
        # xxx=DatasetInfo(
        #     keys=[
        #         "/WW-DPS_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
        #     ],
        #     aux={
        #         "broken_files": [],
        #     },
        #     n_files=104,  # 104-0
        #     n_events=9500000,
        # ),
    ),
)

# per decay mode
cpn.add_dataset(
    name="ww_dl_powheg",
    id=15304453,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=278,  # 278-0
            n_events=239943886,
        ),
    ),
)

cpn.add_dataset(
    name="ww_sl_powheg",
    id=15296280,
    processes=[procs.ww_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=326,  # 326-0
            n_events=275723961,
        ),
    ),
)

cpn.add_dataset(
    name="ww_fh_powheg",
    id=15304426,
    processes=[procs.ww_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=185,  # 185-0
            n_events=151214029,
        ),
    ),
)

# finer lepton decay modes (or different production mode?)

cpn.add_dataset(
    name="ww_wenu_wenu_pythia8",
    id=15349213,
    processes=[procs.ww_wenu_wenu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWto2E2Nu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=64,  # 64-0
            n_events=1994224,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wenu_wmunu_pythia8",
    id=15350676,  # id from GluGluWWtoENuMuNu
    processes=[procs.ww_wenu_wmunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWtoENuMuNu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
                "/GluGluWWtoMuNuENu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=48 + 29,  # 48-0 / 29-0
            n_events=1992025 + 1999275,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wenu_wtaunu_pythia8",
    id=15348543,  # id from GluGluWWtoENuTauNu
    processes=[procs.ww_wenu_wtaunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWtoENuTauNu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
                "/GluGluWWtoTauNuENu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=34 + 32,  # 34-0 / 32-0
            n_events=1994939 + 1997822,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wmunu_wmunu_pythia8",
    id=15349364,
    processes=[procs.ww_wmunu_wmunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWto2Mu2Nu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=33,  # 33-0
            n_events=1997092,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wmunu_wtaunu_pythia8",
    id=15349359,  # id from GluGluWWtoMuNuTauNu
    processes=[procs.ww_wmunu_wtaunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWtoMuNuTauNu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
                "/GluGluWWtoTauNuMuNu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31 + 93,  # 31-0 / 93-0
            n_events=1997816 + 1998548,
        ),
    ),
)

cpn.add_dataset(
    name="ww_wtaunu_wtaunu_pythia8",
    id=15349363,
    processes=[procs.ww_wtaunu_wtaunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluWWto2Tau2Nu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=35,  # 35-0
            n_events=1999273,
        ),
    ),
)

####################################################################################################
#
# WZ boson production
#
####################################################################################################

# inclusive pythia
cpn.add_dataset(
    name="wz_pythia8",
    id=15315210,
    processes=[procs.wz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=307,  # 307-0
            n_events=30547825,
        ),
    ),
)

# by decay powheg ((semi-)leptonic)/amcatnlo(fully hadronic)
cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=15304502,
    processes=[procs.wz_wlnu_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=296,  # 296-0
            n_events=248149069,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wqq_zll_powheg",
    id=15300434,
    processes=[procs.wz_wqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=257,  # 257-0
            n_events=236049432,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wlnu_zqq_powheg",
    id=15304500,
    processes=[procs.wz_wlnu_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=156,  # 156-0
            n_events=143874689,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wqq_zqq_amcatnlo",
    id=15393674,
    processes=[procs.wz_wqq_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZto4Q-1Jets-4FS_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=52,  # 52-0
            n_events=6163657,
        ),
    ),
)

####################################################################################################
#
# WGamma boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# WWW boson production
#
####################################################################################################

cpn.add_dataset(
    name="www_amcatnlo",
    id=15349413,
    processes=[procs.www],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=49,  # 49-0
            n_events=4299284,
        ),
    ),
)

####################################################################################################
#
# WWZ boson production
#
####################################################################################################

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=15348589,
    processes=[procs.wwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=171,  # 171-0
            n_events=16184379,
        ),
    ),
)

####################################################################################################
#
# WZZ boson production
#
####################################################################################################

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=15348847,
    processes=[procs.wwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=127,  # 127-0
            n_events=16199286,
        ),
    ),
)

####################################################################################################
#
# ZZZ boson production
#
####################################################################################################

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=15349235,
    processes=[procs.zzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=201,  # 201-0
            n_events=16192091,
        ),
    ),
)

####################################################################################################
#
# WZGamma boson production
#
####################################################################################################

cpn.add_dataset(
    name="wzg_lnuzg_amcatnlo",
    id=15348696,
    processes=[procs.wzg_lnuzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZGtoLNuZG_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=39,  # 39-0
            n_events=2800000,
        ),
    ),
)
