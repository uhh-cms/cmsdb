# coding: utf-8

"""
Electroweak datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# Drell-Yan, NLO
#

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=15300236,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3_045,
    n_events=479_655_476,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=15304428,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=355,
    n_events=227_319_605,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=15304451,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=22_383_959,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=15304493,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=58,
    n_events=10_404_540,
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=15304449,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=9_996_457,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=15300484,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=1_787,
    n_events=247_167_836,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=15296152,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=389,
    n_events=246_696_940,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=15304466,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=139,
    n_events=44_028_174,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=15304446,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=9_893_470,
)

cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=15304548,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    keys=[
        "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=9_801_431,
)

#
# Drell-Yan powheg
#

# 2 e
cpn.add_dataset(
    name="dy_ee_m10to50_powheg",
    id=15297455,
    processes=[procs.dy_ee_m10to50],
    keys=[
        "/DYto2E_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=395,
    n_events=348_121_585,
)

cpn.add_dataset(
    name="dy_ee_m50to120_powheg",
    id=15296064,
    processes=[procs.dy_ee_m50to120],
    keys=[
        "/DYto2E_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=656,
    n_events=477_172_288,
)

cpn.add_dataset(
    name="dy_ee_m120to200_powheg",
    id=15304457,
    processes=[procs.dy_ee_m120to200],
    keys=[
        "/DYto2E_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=48_821_981,
)

cpn.add_dataset(
    name="dy_ee_m200to400_powheg",
    id=15302364,
    processes=[procs.dy_ee_m200to400],
    keys=[
        "/DYto2E_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=6_823_360,
)

cpn.add_dataset(
    name="dy_ee_m400to800_powheg",
    id=15304418,
    processes=[procs.dy_ee_m400to800],
    keys=[
        "/DYto2E_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=977_525,
)

cpn.add_dataset(
    name="dy_ee_m800to1500_powheg",
    id=15304552,
    processes=[procs.dy_ee_m800to1500],
    keys=[
        "/DYto2E_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=992_750,
)

cpn.add_dataset(
    name="dy_ee_m1500to2500_powheg",
    id=15304463,
    processes=[procs.dy_ee_m1500to2500],
    keys=[
        "/DYto2E_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=998_592,
)

cpn.add_dataset(
    name="dy_ee_m2500to4000_powheg",
    id=15304648,
    processes=[procs.dy_ee_m2500to4000],
    keys=[
        "/DYto2E_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=996_630,
)

cpn.add_dataset(
    name="dy_ee_m4000to6000_powheg",
    id=15297360,
    processes=[procs.dy_ee_m4000to6000],
    keys=[
        "/DYto2E_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=984_688,
)

cpn.add_dataset(
    name="dy_ee_m6000toinf_powheg",
    id=15304478,
    processes=[procs.dy_ee_m6000toinf],
    keys=[
        "/DYto2E_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=998_101,
)

# 2 mu
cpn.add_dataset(
    name="dy_mumu_m10to50_powheg",
    id=15297453,
    processes=[procs.dy_mumu_m10to50],
    keys=[
        "/DYto2Mu_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=405,
    n_events=341_634_068,
)

cpn.add_dataset(
    name="dy_mumu_m50to120_powheg",
    id=15304408,
    processes=[procs.dy_mumu_m50to120],
    keys=[
        "/DYto2Mu_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=640,
    n_events=492_270_708,
)

cpn.add_dataset(
    name="dy_mumu_m120to200_powheg",
    id=15304438,
    processes=[procs.dy_mumu_m120to200],
    keys=[
        "/DYto2Mu_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=48_037_000,
)

cpn.add_dataset(
    name="dy_mumu_m200to400_powheg",
    id=15304520,
    processes=[procs.dy_mumu_m200to400],
    keys=[
        "/DYto2Mu_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=6_588_316,
)

cpn.add_dataset(
    name="dy_mumu_m400to800_powheg",
    id=15304525,
    processes=[procs.dy_mumu_m400to800],
    keys=[
        "/DYto2Mu_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=977_500,
)

cpn.add_dataset(
    name="dy_mumu_m800to1500_powheg",
    id=15304358,
    processes=[procs.dy_mumu_m800to1500],
    keys=[
        "/DYto2Mu_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=979_723,
)

cpn.add_dataset(
    name="dy_mumu_m1500to2500_powheg",
    id=15304537,
    processes=[procs.dy_mumu_m1500to2500],
    keys=[
        "/DYto2Mu_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=962_340,
)

cpn.add_dataset(
    name="dy_mumu_m2500to4000_powheg",
    id=15304508,
    processes=[procs.dy_mumu_m2500to4000],
    keys=[
        "/DYto2Mu_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=934_352,
)

cpn.add_dataset(
    name="dy_mumu_m4000to6000_powheg",
    id=15304549,
    processes=[procs.dy_mumu_m4000to6000],
    keys=[
        "/DYto2Mu_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=999_261,
)

cpn.add_dataset(
    name="dy_mumu_m6000toinf_powheg",
    id=15304533,
    processes=[procs.dy_mumu_m6000toinf],
    keys=[
        "/DYto2Mu_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=998_508,
)

# 2 tau
cpn.add_dataset(
    name="dy_tautau_m10to50_powheg",
    id=15297458,
    processes=[procs.dy_tautau_m10to50],
    keys=[
        "/DYto2Tau_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=400,
    n_events=344_069_532,
)

cpn.add_dataset(
    name="dy_tautau_m50to120_powheg",
    id=15297457,
    processes=[procs.dy_tautau_m50to120],
    keys=[
        "/DYto2Tau_Bin-MLL-50to120_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=564,
    n_events=486_994_937,
)

cpn.add_dataset(
    name="dy_tautau_m120to200_powheg",
    id=15304444,
    processes=[procs.dy_tautau_m120to200],
    keys=[
        "/DYto2Tau_Bin-MLL-120to200_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=113,
    n_events=48_376_250,
)

cpn.add_dataset(
    name="dy_tautau_m200to400_powheg",
    id=15304498,
    processes=[procs.dy_tautau_m200to400],
    keys=[
        "/DYto2Tau_Bin-MLL-200to400_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=6_779_206,
)

cpn.add_dataset(
    name="dy_tautau_m400to800_powheg",
    id=15304534,
    processes=[procs.dy_tautau_m400to800],
    keys=[
        "/DYto2Tau_Bin-MLL-400to800_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=991_838,
)

cpn.add_dataset(
    name="dy_tautau_m800to1500_powheg",
    id=15304579,
    processes=[procs.dy_tautau_m800to1500],
    keys=[
        "/DYto2Tau_Bin-MLL-800to1500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=987_369,
)

cpn.add_dataset(
    name="dy_tautau_m1500to2500_powheg",
    id=15304532,
    processes=[procs.dy_tautau_m1500to2500],
    keys=[
        "/DYto2Tau_Bin-MLL-1500to2500_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=964_672,
)

cpn.add_dataset(
    name="dy_tautau_m2500to4000_powheg",
    id=15304551,
    processes=[procs.dy_tautau_m2500to4000],
    keys=[
        "/DYto2Tau_Bin-MLL-2500to4000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=996_340,
)

cpn.add_dataset(
    name="dy_tautau_m4000to6000_powheg",
    id=15304360,
    processes=[procs.dy_tautau_m4000to6000],
    keys=[
        "/DYto2Tau_Bin-MLL-4000to6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=942_725,
)

cpn.add_dataset(
    name="dy_tautau_m6000toinf_powheg",
    id=15304550,
    processes=[procs.dy_tautau_m6000toinf],
    keys=[
        "/DYto2Tau_Bin-MLL-6000_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=992_190,
)

#
# Drell-Yan amcatnlo, tautau reprocessed in njet bins
#

# tba

#
# W boson production
#

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=15297303,
    processes=[procs.w_lnu_1j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3_384,
    n_events=447_467_775,
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=15300033,
    processes=[procs.w_lnu_1j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3_089,
    n_events=494_167_270,
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=15304490,
    processes=[procs.w_lnu_1j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=45_096_548,
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=15304489,
    processes=[procs.w_lnu_1j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=14_159_808,
)

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=15300032,
    processes=[procs.w_lnu_2j_pt40to100],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3_309,
    n_events=483_030_994,
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=15299994,
    processes=[procs.w_lnu_2j_pt100to200],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=3_262,
    n_events=470_520_533,
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=15304499,
    processes=[procs.w_lnu_2j_pt200to400],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=136,
    n_events=75_124_628,
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=15304459,
    processes=[procs.w_lnu_2j_pt400to600],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=14_222_725,
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=15304609,
    processes=[procs.w_lnu_1j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=15_305_397,
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=15304506,
    processes=[procs.w_lnu_2j_pt600toinf],
    keys=[
        "/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=14_991_109,
)


#
# Z boson production (non-DY)
#

# tba

#
# W/Z VBF production
#

cpn.add_dataset(
    name="w_vbf_wlnu_madgraph",
    id=15304421,
    processes=[procs.w_vbf_wlnu],
    keys=[
        "/VBFtoLNu_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=213,
    n_events=113_042_539,
)

cpn.add_dataset(
    name="z_vbf_zll_m50toinf_madgraph",
    id=15304452,
    processes=[procs.z_vbf_zll_m50toinf],
    keys=[
        "/VBFto2L_Bin-MLL-50_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=0,
    n_events=0,
)

#
# Di-boson
#

cpn.add_dataset(
    name="ww_pythia",
    id=15315231,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=518,
    n_events=63_986_968,
)

cpn.add_dataset(
    name="wz_pythia",
    id=15315210,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=307,
    n_events=30_547_825,
)

cpn.add_dataset(
    name="zz_pythia",
    id=15315163,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",
    ],
    n_files=76,
    n_events=4_800_000,
)

#
# Triple-boson
#

cpn.add_dataset(
    name="www_4f_amcatnlo",
    id=15349413,
    processes=[procs.www],
    keys=[
        "/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=4_299_284,
)

cpn.add_dataset(
    name="wwz_4f_amcatnlo",
    id=15348589,
    processes=[procs.wwz],
    keys=[
        "/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=171,
    n_events=16_184_379,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=15348847,
    processes=[procs.wzz],
    keys=[
        "/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=16_199_286,
)

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=15349235,
    processes=[procs.zzz],
    keys=[
        "/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=201,
    n_events=16_192_091,
)
