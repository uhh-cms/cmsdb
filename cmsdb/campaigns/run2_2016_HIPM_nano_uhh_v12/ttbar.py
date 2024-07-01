# coding: utf-8


"""
ttbar datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""


import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn
from order import DatasetInfo

# TTWW
cpn.add_dataset(
    name="ttww_madgraph",
    id=14214929,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=278_000,
)

# TTZToLLNuNu
cpn.add_dataset(
    name="ttz_zlep_m10toinf_amcatnlo",
    id=14213080,
    processes=[procs.ttz_zlep_m10toinf],
    keys=[
        "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=5_792_000,
)

# TTWJetsToQQ
cpn.add_dataset(
    name="ttw_wqq_amcatnlo",
    id=14286376,
    processes=[procs.ttw_wqq],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=271_496,
)

# TTWJetsToLNu
cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=14251563,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=2_850_164,
)

# TTWZ
cpn.add_dataset(
    name="ttwz_madgraph",
    id=14213653,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=140_000,
)

# TTZZ
cpn.add_dataset(
    name="ttzz_madgraph",
    id=14213601,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=140_000,
)

# TTTo2L2Nu
cpn.add_dataset(
    name="tt_dl_powheg",
    id=14213146,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=594,
            n_events=37_505_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=340,
            n_events=21_583_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=173,
            n_events=10_311_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=286,
            n_events=16_973_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=249,
            n_events=14_865_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=268,
            n_events=16_828_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=280,
            n_events=16_848_000,
        ),
    ),
)

# TTToHadronic
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14212988,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=1_458,
            n_events=97_600_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=623,
            n_events=39_035_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=456,
            n_events=28_866_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=569,
            n_events=36_956_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=483,
            n_events=30_504_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=501,
            n_events=32_237_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=589,
            n_events=39_151_000,
        ),
    ),
)

# TTToSemiLeptonic
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14213040,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=1_979,
            n_events=132_178_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=837,
            n_events=55_755_500,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=690,
            n_events=46_535_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=706,
            n_events=47_238_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=818,
            n_events=56_968_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=840,
            n_events=55_256_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2_NanoAODv12UHH-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
            ],
            n_files=821,
            n_events=53_342_000,
        ),
    ),
)
