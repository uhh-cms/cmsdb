# coding: utf-8


"""
Single Top datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""


import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn
from order import DatasetInfo

# ST_tW_top
cpn.add_dataset(
    name="st_twchannel_t_powheg",
    id=14213957,
    processes=[procs.st_twchannel_t],
    keys=[
        "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=2_300_000,
)

# ST_tW_antitop
cpn.add_dataset(
    name="st_twchannel_tbar_powheg",
    id=14212973,
    processes=[procs.st_twchannel_tbar],
    keys=[
        "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v1/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=2_300_000,
)


# ST_t-channel_antitop
cpn.add_dataset(
    name="st_tchannel_tbar_powheg",
    id=14225486,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=580,
            n_events=31_024_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=10_854_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=196,
            n_events=10_715_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=240,
            n_events=10_626_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=256,
            n_events=11_101_000,
        ),
    ),
)


# ST_t-channel_top
cpn.add_dataset(
    name="st_tchannel_t_powheg",
    id=14224840,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=908,
            n_events=55_961_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=366,
            n_events=22_073_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=374,
            n_events=21_927_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=452,
            n_events=22_239_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_NanoAODAPVv12UHH-v3/NANOAODSIM",  # noqa
            ],
            n_files=461,
            n_events=22_499_000,
        ),
    ),
)
