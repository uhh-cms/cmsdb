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

# none yet

####################################################################################################
#
# ZZ boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# ZGamma boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# WZ boson production
#
####################################################################################################

# none yet

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

# none yet

####################################################################################################
#
# WWZ boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# WZZ boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# ZZZ boson production
#
####################################################################################################

# none yet

####################################################################################################
#
# WZGamma boson production
#
####################################################################################################

# none yet
