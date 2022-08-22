# coding: utf-8

"""
Common, analysis independent definition of the 2018 data-taking campaign.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign, DatasetInfo

import cmsdb.processes as procs


#
# campaign
#

campaign_run2_2018 = Campaign(
    name="run2_2018",
    id=220181,
    ecm=13,
    bx=25,
    aux={"year": 2018},
)


#
# datasets
#

campaign_run2_2018.add_dataset(
    name="data_mu_a",
    id=14046760,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD",
    ],
    n_files=225,
    n_events=241608232,
)

campaign_run2_2018.add_dataset(
    name="st_tchannel_t",
    id=14293903,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=149,
            n_events=178336000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=75582000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=74992000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=62,
            n_events=59030000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=73014000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="st_tchannel_tbar",
    id=14296756,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=130,
            n_events=95627000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=36424000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=36144000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37268000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=37919000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="st_twchannel_t",
    id=14248830,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=7956000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="st_twchannel_tbar",
    id=14253778,
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=7749000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="tt_sl",
    id=14235437,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=476408000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=165,
            n_events=199394000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=156,
            n_events=189888000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=168,
            n_events=197814000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=171,
            n_events=193212000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="tt_dl",
    id=14234474,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=155,
            n_events=145020000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=57064000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=59853000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=54048000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=59958000,
        ),
    ),
)

campaign_run2_2018.add_dataset(
    name="tt_fh",
    id=14232068,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=339,
            n_events=334206000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=114,
            n_events=136785999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=131,
            n_events=139688000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=126,
            n_events=138026000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=139490000,
        ),
    ),
)
