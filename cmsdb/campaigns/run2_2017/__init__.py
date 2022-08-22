# coding: utf-8

"""
Common, analysis independent definition of the 2017 data-taking campaign.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign, DatasetInfo

import cmsdb.processes as procs


#
# campaign
#

campaign_run2_2017 = Campaign(
    name="run2_2017",
    id=220171,
    ecm=13,
    bx=25,
    aux={"year": 2017},
)


#
# real data
#

# SingleElectron
campaign_run2_2017.add_dataset(
    name="data_e_b",
    id=14226251,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=60537490,
)

campaign_run2_2017.add_dataset(
    name="data_e_c",
    id=14226092,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=136637888,
)

campaign_run2_2017.add_dataset(
    name="data_e_d",
    id=14227611,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=37,
    n_events=51512837,
)

campaign_run2_2017.add_dataset(
    name="data_e_e",
    id=14226090,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=51,
    n_events=102122055,
)

campaign_run2_2017.add_dataset(
    name="data_e_f",
    id=14226476,
    is_data=True,
    processes=[procs.data_e],
    keys=[
        "/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=66,
    n_events=128467223,
)

# SingleMuon
campaign_run2_2017.add_dataset(
    name="data_mu_b",
    id=14226191,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=79,
    n_events=136300266,
)

campaign_run2_2017.add_dataset(
    name="data_mu_c",
    id=14226140,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=117,
    n_events=165652756,
)

campaign_run2_2017.add_dataset(
    name="data_mu_d",
    id=14226234,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=47,
    n_events=70361660,
)

campaign_run2_2017.add_dataset(
    name="data_mu_e",
    id=14235644,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=78,
    n_events=154618774,
)

campaign_run2_2017.add_dataset(
    name="data_mu_f",
    id=14226183,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=115,
    n_events=242140980,
)

# Tau
campaign_run2_2017.add_dataset(
    name="data_tau_b",
    id=14233603,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=32,
    n_events=38158216,
)

campaign_run2_2017.add_dataset(
    name="data_tau_c",
    id=14233706,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=45,
    n_events=55416425,
)

campaign_run2_2017.add_dataset(
    name="data_tau_d",
    id=14233103,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=13,
    n_events=20530776,
)

campaign_run2_2017.add_dataset(
    name="data_tau_e",
    id=14233325,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=0,
    n_events=0,
)

campaign_run2_2017.add_dataset(
    name="data_tau_f",
    id=14232807,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=59,
    n_events=88502118,
)

# MET
campaign_run2_2017.add_dataset(
    name="data_met_b",
    id=14225468,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=43,
    n_events=51623474,
)

campaign_run2_2017.add_dataset(
    name="data_met_c",
    id=14226051,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=53,
    n_events=115906496,
)

campaign_run2_2017.add_dataset(
    name="data_met_d",
    id=14230935,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=15,
    n_events=20075033,
)

campaign_run2_2017.add_dataset(
    name="data_met_e",
    id=14225819,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=48,
    n_events=71418865,
)

campaign_run2_2017.add_dataset(
    name="data_met_f",
    id=14224849,
    is_data=True,
    processes=[procs.data_met],
    keys=[
        "/MET/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD",
    ],
    n_files=133,
    n_events=177521562,
)


#
# ttbar
#

campaign_run2_2017.add_dataset(
    name="tt_sl_powheg",
    id=14231639,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=297,
            n_events=346052000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=142,
            n_events=137062000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=122,
            n_events=134394000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=119,
            n_events=132184000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=119,
            n_events=133515999,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=142,
            n_events=137904000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=111,
            n_events=132484000,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="tt_dl_powheg",
    id=14265841,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=106724000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=42388000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=39285000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=39884000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=39380000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=42742000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=40782000,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="tt_fh_powheg",
    id=14299346,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=199,
            n_events=232999999,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=100,
            n_events=95255999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=91,
            n_events=96999000,

        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=93,
            n_events=99000000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=103,
            n_events=95286000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=89579000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=108,
            n_events=96894000,
        ),
    ),
)


#
# ttbar + 1 vector boson
#

campaign_run2_2017.add_dataset(
    name="ttz_llnunu_amcatnlo",
    id=14229512,
    processes=[procs.ttz_llnunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=14036000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5up_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=5700000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5down_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=5699999,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="ttw_nlu_amcatnlo",
    id=14228083,
    processes=[procs.ttw_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=7140411,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5up_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=2920612,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=2891483,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="ttw_qq_amcatnlo",
    id=14235122,
    processes=[procs.ttw_qq],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=655018,
)


#
# ttbar + 2 vector bosons
#

campaign_run2_2017.add_dataset(
    name="ttzz_madgraph",
    id=14234743,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=327000,
)

campaign_run2_2017.add_dataset(
    name="ttwz_madgraph",
    id=14230416,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=350000,
)

campaign_run2_2017.add_dataset(
    name="ttww_madgraph",
    id=14234141,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=698000,
)


#
# single top
#

campaign_run2_2017.add_dataset(
    name="st_tchannel_t",
    id=14296960,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=197,
            n_events=129903000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=91,
            n_events=52891000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=108,
            n_events=53646000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=54669000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=98,
            n_events=54055000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=115,
            n_events=51652000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=78,
            n_events=54413000,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="st_tchannel_tbar",
    id=14296742,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=69793000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=26488000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=27196000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=26783000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=49,
            n_events=26461000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=26921000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=27001900,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="st_twchannel_t_powheg",
    id=14246131,
    processes=[procs.st_twchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=5649000,
        ),
        # additional shifts, however, for non-fully-hadronic decays
        # /ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
        # /ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
        # /ST_tW_top_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_top_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_top_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
        # /ST_tW_top_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
    ),
)

campaign_run2_2017.add_dataset(
    name="st_twchannel_tbar_powheg",
    id=14248566,
    processes=[procs.st_twchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=5674000,
        ),
        # additional shifts, however, for non-fully-hadronic decays
        # /ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM
        # /ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_antitop_5f_hdampup_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_antitop_5f_hdampdown_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1735_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
        # /ST_tW_antitop_5f_NoFullyHadronicDecays_mtop1715_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
    ),
)

campaign_run2_2017.add_dataset(
    name="st_schannel_lep_amcatnlo",
    id=14235125,
    processes=[procs.st_schannel_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=13620000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_s-channel_4f_leptonDecays_TuneCP5up_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=5562000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_s-channel_4f_leptonDecays_TuneCP5down_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=15,
            n_events=5496000,
        ),
    ),
)

campaign_run2_2017.add_dataset(
    name="st_schannel_had_amcatnlo",
    id=14378997,
    processes=[procs.st_schannel_had],
    keys=[
        "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=11696999,
)


#
# Drell-Yan
#

# jet binned, madgraph
campaign_run2_2017.add_dataset(
    name="dy_lep_m50_1j_madgraph",
    id=14242968,
    processes=[procs.dy_lep_m50_1j],
    keys=[
        "/DY1JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=65903452,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_2j_madgraph",
    id=14235404,
    processes=[procs.dy_lep_m50_2j],
    keys=[
        "/DY2JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=27099640,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_3j_madgraph",
    id=14235548,
    processes=[procs.dy_lep_m50_3j],
    keys=[
        "/DY3JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=20165687,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_4j_madgraph",
    id=14235551,
    processes=[procs.dy_lep_m50_4j],
    keys=[
        "/DY4JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=10872554,
)

# jet binned, amcatnlo
campaign_run2_2017.add_dataset(
    name="dy_lep_0j_amcatnlo",
    id=14302706,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=78288099,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_1j_amcatnlo",
    id=14300055,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=84321311,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_2j_amcatnlo",
    id=14231469,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=46395058,
)

# ht binned
campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht70to100_madgraph",
    id=14235248,
    processes=[procs.dy_lep_m50_ht70to100],
    keys=[
        "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=12205958,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht100to200_madgraph",
    id=14235412,
    processes=[procs.dy_lep_m50_ht100to200],
    keys=[
        "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=18648544,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht200to400_madgraph",
    id=14235285,
    processes=[procs.dy_lep_m50_ht200to400],
    keys=[
        "/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=12451701,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht400to600_madgraph",
    id=14234754,
    processes=[procs.dy_lep_m50_ht400to600],
    keys=[
        "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5384252,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht600to800_madgraph",
    id=14234976,
    processes=[procs.dy_lep_m50_ht600to800],
    keys=[
        "/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=5118706,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht800to1200_madgraph",
    id=14234833,
    processes=[procs.dy_lep_m50_ht800to1200],
    keys=[
        "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4347168,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht1200to2500_madgraph",
    id=14243239,
    processes=[procs.dy_lep_m50_ht1200to2500],
    keys=[
        "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=4725936,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_m50_ht2500_madgraph",
    id=14244972,
    processes=[procs.dy_lep_m50_ht2500],
    keys=[
        "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=1480047,
)

# pt binned
campaign_run2_2017.add_dataset(
    name="dy_lep_pt50To100_amcatnlo",
    id=14231159,
    processes=[procs.dy_lep_pt50To100],
    keys=[
        "/DYJetsToLL_Pt-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=107079717,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_pt100To250_amcatnlo",
    id=14300156,
    processes=[procs.dy_lep_pt100To250],
    keys=[
        "/DYJetsToLL_Pt-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=75818801,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_pt250To400_amcatnlo",
    id=14235259,
    processes=[procs.dy_lep_pt250To400],
    keys=[
        "/DYJetsToLL_Pt-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=18739246,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_pt400To650_amcatnlo",
    id=14228178,
    processes=[procs.dy_lep_pt400To650],
    keys=[
        "/DYJetsToLL_Pt-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1895259,
)

campaign_run2_2017.add_dataset(
    name="dy_lep_pt650_amcatnlo",
    id=14232153,
    processes=[procs.dy_lep_pt650],
    keys=[
        "/DYJetsToLL_Pt-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=1921546,
)


#
# W boson production
#

# inclusive
campaign_run2_2017.add_dataset(
    name="w_lnu_madgraph",
    id=14233715,
    processes=[procs.w_lnu],
    keys=[
        "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=81,
    n_events=78307186,
)

# ht binned
campaign_run2_2017.add_dataset(
    name="w_lnu_ht70To100_madgraph",
    id=14245091,
    processes=[procs.w_lnu_ht70To100],
    keys=[
        "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=36,
    n_events=44576510,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht100To200_madgraph",
    id=14231627,
    processes=[procs.w_lnu_ht100To200],
    keys=[
        "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=47424468,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht200To400_madgraph",
    id=14239255,
    processes=[procs.w_lnu_ht200To400],
    keys=[
        "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=42281979,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht400To600_madgraph",
    id=14231356,
    processes=[procs.w_lnu_ht400To600],
    keys=[
        "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=5468473,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht600To800_madgraph",
    id=14230638,
    processes=[procs.w_lnu_ht600To800],
    keys=[
        "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=5545298,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht800To1200_madgraph",
    id=14346984,
    processes=[procs.w_lnu_ht800To1200],
    keys=[
        "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v3/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=5088483,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht1200To2500_madgraph",
    id=14231551,
    processes=[procs.w_lnu_ht1200To2500],
    keys=[
        "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=4752118,
)

campaign_run2_2017.add_dataset(
    name="w_lnu_ht2500_madgraph",
    id=14267094,
    processes=[procs.w_lnu_ht2500],
    keys=[
        "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=1185699,
)


#
# EWK
# (vector boson emissions)
#

campaign_run2_2017.add_dataset(
    name="ewk_wm_lnu_madgraph",
    id=14301832,
    processes=[procs.ewk_wm_lnu],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=4077000,
)

campaign_run2_2017.add_dataset(
    name="ewk_w_lnu_madgraph",
    id=14300978,
    processes=[procs.ewk_wp_lnu],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=3595000,
)

campaign_run2_2017.add_dataset(
    name="ewk_z_ll_madgraph",
    id=14301412,
    processes=[procs.ewk_z_ll],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=19,
    n_events=579000,
)


#
# Di-boson
#

# ZZ
campaign_run2_2017.add_dataset(
    name="zz_pythia",
    id=14227451,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2706000,
)

campaign_run2_2017.add_dataset(
    name="zz_qqll_m4_amcatnlo",
    id=14298864,
    processes=[procs.zz_qqll_m4],
    keys=[
        "/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=29521496,
)

campaign_run2_2017.add_dataset(
    name="zz_llnunu_powheg",
    id=14237024,
    processes=[procs.zz_llnunu],
    keys=[
        "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=40839000,
)

campaign_run2_2017.add_dataset(
    name="zz_llll_powheg",
    id=14243658,
    processes=[procs.zz_llll],
    keys=[
        "/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=109,
    n_events=99388000,
)

# WZ
campaign_run2_2017.add_dataset(
    name="wz_pythia",
    id=14230373,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=7889000,
)

campaign_run2_2017.add_dataset(
    name="wz_lllnu_amcatnlo",
    id=14253602,
    processes=[procs.wz_lllnu],
    keys=[
        "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=10339582,
)

campaign_run2_2017.add_dataset(
    name="wz_qqll_m4_amcatnlo",
    id=14328000,
    processes=[procs.wz_qqll_m4],
    keys=[
        "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=29091996,
)

# WW
campaign_run2_2017.add_dataset(
    name="ww_pythia",
    id=14229298,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=15634000,
)

campaign_run2_2017.add_dataset(
    name="ww_lnulnu_powheg",
    id=14241651,
    processes=[procs.ww_lnulnu],
    keys=[
        "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7098000,
)


#
# Triple-boson
#

campaign_run2_2017.add_dataset(
    name="zzz_amcatnlo",
    id=14231380,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=15 + 31,
    n_events=178000 + 9524000,
)

campaign_run2_2017.add_dataset(
    name="wzz_amcatnlo",
    id=14247843,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=2 + 23,
    n_events=298000 + 9898000,
)

campaign_run2_2017.add_dataset(
    name="wwz_amcatnlo",
    id=14231348,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=5 + 41,
    n_events=178000 + 9938400,
)

campaign_run2_2017.add_dataset(
    name="www_amcatnlo",
    id=14231501,
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=16 + 43,
    n_events=171000 + 9854000,
)


#
# Single Higgs
#

# ggf
campaign_run2_2017.add_dataset(
    name="h_ggf_tautau_powheg",
    id=14230587,
    processes=[procs.h_ggf_tautau],
    keys=[
        "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=44,
    n_events=12974000,
)

# vbf
campaign_run2_2017.add_dataset(
    name="h_vbf_tautau_powheg",
    id=14232168,
    processes=[procs.h_vbf_tautau],
    keys=[
        "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=2811630,
)

# H radiation
campaign_run2_2017.add_dataset(
    name="zh_tautau_powheg",
    id=14363472,
    processes=[procs.zh_tautau],
    keys=[
        "/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=4614054,
)

campaign_run2_2017.add_dataset(
    name="zh_bb_powheg",
    id=14275939,
    processes=[procs.zh_bb],
    keys=[
        "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=4958035,
)

campaign_run2_2017.add_dataset(
    name="wph_tautau_powheg",
    id=14232214,
    processes=[procs.wph_tautau],
    keys=[
        "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=45,
    n_events=3985990,
)

campaign_run2_2017.add_dataset(
    name="wmh_tautau_powheg",
    id=14231275,
    processes=[procs.wmh_tautau],
    keys=[
        "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=3828192,
)

campaign_run2_2017.add_dataset(
    name="ggzh_llbb_powheg",
    id=14355451,
    processes=[procs.ggzh_llbb],
    keys=[
        "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=4673000,
)

# ttH
campaign_run2_2017.add_dataset(
    name="tth_tautau_powheg",
    id=14230113,
    processes=[procs.tth_tautau],
    keys=[
        "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=68,
    n_events=21165000,
)

campaign_run2_2017.add_dataset(
    name="tth_bb_powheg",
    id=14260809,
    processes=[procs.tth_bb],
    keys=[
        "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=7825000,
)

campaign_run2_2017.add_dataset(
    name="tth_nonbb_powheg",
    id=14261730,
    processes=[procs.tth_nonbb],
    keys=[
        "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=35,
    n_events=5070989,
)


#
# ggF -> H -> HH
#

# SM
campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_madgraph",
    id=14336680,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=400000,
)

# BSM scenarios
campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node1_madgraph",
    id=14366362,
    processes=[procs.hh_ggf_bbtautau_node1],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_1_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=400000,
)

# missing
# campaign_run2_2017.add_dataset(
#     name="hh_ggf_bbtautau_node2_madgraph",
#     id=,
#     processes=[procs.hh_ggf_bbtautau_node2],
#     keys=[
#         "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_2_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=,
#     n_events=,
# )

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node3_madgraph",
    id=14369747,
    processes=[procs.hh_ggf_bbtautau_node3],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_3_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node4_madgraph",
    id=14368375,
    processes=[procs.hh_ggf_bbtautau_node4],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_4_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node5_madgraph",
    id=14364195,
    processes=[procs.hh_ggf_bbtautau_node5],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node6_madgraph",
    id=14368376,
    processes=[procs.hh_ggf_bbtautau_node6],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_6_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node7_madgraph",
    id=14369764,
    processes=[procs.hh_ggf_bbtautau_node7],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_7_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node8_madgraph",
    id=14370426,
    processes=[procs.hh_ggf_bbtautau_node8],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_8_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node9_madgraph",
    id=14366977,
    processes=[procs.hh_ggf_bbtautau_node9],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_9_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node10_madgraph",
    id=14369844,
    processes=[procs.hh_ggf_bbtautau_node10],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_10_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node11_madgraph",
    id=14368408,
    processes=[procs.hh_ggf_bbtautau_node11],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_11_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="hh_ggf_bbtautau_node12_madgraph",
    id=14368374,
    processes=[procs.hh_ggf_bbtautau_node12],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_12_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=400000,
)


#
# ggF -> radion -> HH
#

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m250_madgraph",
    id=14302777,
    processes=[procs.radion_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m260_madgraph",
    id=14346707,
    processes=[procs.radion_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m270_madgraph",
    id=14308899,
    processes=[procs.radion_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=393000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m280_madgraph",
    id=14346524,
    processes=[procs.radion_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=388000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m300_madgraph",
    id=14305216,
    processes=[procs.radion_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=276000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m320_madgraph",
    id=14317863,
    processes=[procs.radion_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=286000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m350_madgraph",
    id=14305228,
    processes=[procs.radion_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=282000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m400_madgraph",
    id=14304148,
    processes=[procs.radion_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=288000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m450_madgraph",
    id=14327613,
    processes=[procs.radion_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=294000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m500_madgraph",
    id=14305221,
    processes=[procs.radion_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=285000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m550_madgraph",
    id=14302808,
    processes=[procs.radion_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m600_madgraph",
    id=14308469,
    processes=[procs.radion_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m650_madgraph",
    id=14346493,
    processes=[procs.radion_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m700_madgraph",
    id=14346372,
    processes=[procs.radion_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m750_madgraph",
    id=14346507,
    processes=[procs.radion_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=191000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m800_madgraph",
    id=14327247,
    processes=[procs.radion_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m850_madgraph",
    id=14329740,
    processes=[procs.radion_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=189000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m900_madgraph",
    id=14346605,
    processes=[procs.radion_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m1000_madgraph",
    id=14305457,
    processes=[procs.radion_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m1250_madgraph",
    id=14302759,
    processes=[procs.radion_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m1500_madgraph",
    id=14304452,
    processes=[procs.radion_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m1750_madgraph",
    id=14302315,
    processes=[procs.radion_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m2000_madgraph",
    id=14304853,
    processes=[procs.radion_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=97000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m2500_madgraph",
    id=14305723,
    processes=[procs.radion_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_ggf_bbtautau_m3000_madgraph",
    id=14346584,
    processes=[procs.radion_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=100000,
)


#
# ggF -> bulk graviton -> HH
#

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m250_madgraph",
    id=14309793,
    processes=[procs.graviton_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m260_madgraph",
    id=14302792,
    processes=[procs.graviton_hh_ggf_bbtautau_m260],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m270_madgraph",
    id=14330676,
    processes=[procs.graviton_hh_ggf_bbtautau_m270],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m280_madgraph",
    id=14330326,
    processes=[procs.graviton_hh_ggf_bbtautau_m280],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m300_madgraph",
    id=14346485,
    processes=[procs.graviton_hh_ggf_bbtautau_m300],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=300000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m320_madgraph",
    id=14335123,
    processes=[procs.graviton_hh_ggf_bbtautau_m320],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=297000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m350_madgraph",
    id=14346502,
    processes=[procs.graviton_hh_ggf_bbtautau_m350],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=285000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m400_madgraph",
    id=14346355,
    processes=[procs.graviton_hh_ggf_bbtautau_m400],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=300000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m450_madgraph",
    id=14311442,
    processes=[procs.graviton_hh_ggf_bbtautau_m450],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=286000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m500_madgraph",
    id=14307226,
    processes=[procs.graviton_hh_ggf_bbtautau_m500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=300000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m550_madgraph",
    id=14302414,
    processes=[procs.graviton_hh_ggf_bbtautau_m550],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m600_madgraph",
    id=14302378,
    processes=[procs.graviton_hh_ggf_bbtautau_m600],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m650_madgraph",
    id=14309720,
    processes=[procs.graviton_hh_ggf_bbtautau_m650],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m700_madgraph",
    id=14305200,
    processes=[procs.graviton_hh_ggf_bbtautau_m700],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=198000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m750_madgraph",
    id=14346504,
    processes=[procs.graviton_hh_ggf_bbtautau_m750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m800_madgraph",
    id=14346495,
    processes=[procs.graviton_hh_ggf_bbtautau_m800],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m850_madgraph",
    id=14346604,
    processes=[procs.graviton_hh_ggf_bbtautau_m850],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m900_madgraph",
    id=14330168,
    processes=[procs.graviton_hh_ggf_bbtautau_m900],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=189000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1000_madgraph",
    id=14307192,
    processes=[procs.graviton_hh_ggf_bbtautau_m1000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=95000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1250_madgraph",
    id=14305219,
    processes=[procs.graviton_hh_ggf_bbtautau_m1250],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=98000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1500_madgraph",
    id=14302337,
    processes=[procs.graviton_hh_ggf_bbtautau_m1500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m1750_madgraph",
    id=14307183,
    processes=[procs.graviton_hh_ggf_bbtautau_m1750],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2000_madgraph",
    id=14304912,
    processes=[procs.graviton_hh_ggf_bbtautau_m2000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m2500_madgraph",
    id=14306377,
    processes=[procs.graviton_hh_ggf_bbtautau_m2500],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_ggf_bbtautau_m3000_madgraph",
    id=14305674,
    processes=[procs.graviton_hh_ggf_bbtautau_m3000],
    keys=[
        "/GluGluToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=100000,
)


#
# vbf -> radion -> HH
#

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m250_madgraph",
    id=14313383,
    processes=[procs.radion_hh_vbf_bbtautau_m250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=397000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m260_madgraph",
    id=14312102,
    processes=[procs.radion_hh_vbf_bbtautau_m260],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=394000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m270_madgraph",
    id=14315423,
    processes=[procs.radion_hh_vbf_bbtautau_m270],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=8,
    n_events=379000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m280_madgraph",
    id=14315394,
    processes=[procs.radion_hh_vbf_bbtautau_m280],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=394000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m300_madgraph",
    id=14312259,
    processes=[procs.radion_hh_vbf_bbtautau_m300],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=294000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m320_madgraph",
    id=14315335,
    processes=[procs.radion_hh_vbf_bbtautau_m320],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=276000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m350_madgraph",
    id=14315249,
    processes=[procs.radion_hh_vbf_bbtautau_m350],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=297000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m400_madgraph",
    id=14315364,
    processes=[procs.radion_hh_vbf_bbtautau_m400],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=297000,
)

# missing
# campaign_run2_2017.add_dataset(
#     name="radion_hh_vbf_bbtautau_m450_madgraph",
#     id=,
#     processes=[procs.radion_hh_vbf_bbtautau_m450],
#     keys=[
#         "/VBFToRadionToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=,
#     n_events=,
# )

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m500_madgraph",
    id=14315911,
    processes=[procs.radion_hh_vbf_bbtautau_m500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=300000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m550_madgraph",
    id=14313492,
    processes=[procs.radion_hh_vbf_bbtautau_m550],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m600_madgraph",
    id=14313271,
    processes=[procs.radion_hh_vbf_bbtautau_m600],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m650_madgraph",
    id=14313413,
    processes=[procs.radion_hh_vbf_bbtautau_m650],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m700_madgraph",
    id=14312044,
    processes=[procs.radion_hh_vbf_bbtautau_m700],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=194000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m750_madgraph",
    id=14313296,
    processes=[procs.radion_hh_vbf_bbtautau_m750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m800_madgraph",
    id=14311221,
    processes=[procs.radion_hh_vbf_bbtautau_m800],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=194000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m850_madgraph",
    id=14312594,
    processes=[procs.radion_hh_vbf_bbtautau_m850],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m900_madgraph",
    id=14312083,
    processes=[procs.radion_hh_vbf_bbtautau_m900],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=197000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m1000_madgraph",
    id=14311676,
    processes=[procs.radion_hh_vbf_bbtautau_m1000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=97000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m1250_madgraph",
    id=14313782,
    processes=[procs.radion_hh_vbf_bbtautau_m1250],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m1500_madgraph",
    id=14315286,
    processes=[procs.radion_hh_vbf_bbtautau_m1500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=97000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m1750_madgraph",
    id=14314144,
    processes=[procs.radion_hh_vbf_bbtautau_m1750],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m2000_madgraph",
    id=14319538,
    processes=[procs.radion_hh_vbf_bbtautau_m2000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=94000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m2500_madgraph",
    id=14316124,
    processes=[procs.radion_hh_vbf_bbtautau_m2500],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=97000,
)

campaign_run2_2017.add_dataset(
    name="radion_hh_vbf_bbtautau_m3000_madgraph",
    id=14316141,
    processes=[procs.radion_hh_vbf_bbtautau_m3000],
    keys=[
        "/VBFToRadionToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=100000,
)


#
# vbf -> bulk graviton -> HH
#

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m250_madgraph",
    id=14313377,
    processes=[procs.graviton_hh_vbf_bbtautau_m250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=399000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m260_madgraph",
    id=14312620,
    processes=[procs.graviton_hh_vbf_bbtautau_m260],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-260_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=394000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m270_madgraph",
    id=14311771,
    processes=[procs.graviton_hh_vbf_bbtautau_m270],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-270_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m280_madgraph",
    id=14313366,
    processes=[procs.graviton_hh_vbf_bbtautau_m280],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-280_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=400000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m300_madgraph",
    id=14312031,
    processes=[procs.graviton_hh_vbf_bbtautau_m300],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-300_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=291000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m320_madgraph",
    id=14312181,
    processes=[procs.graviton_hh_vbf_bbtautau_m320],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-320_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=300000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m350_madgraph",
    id=14312121,
    processes=[procs.graviton_hh_vbf_bbtautau_m350],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-350_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=297000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m400_madgraph",
    id=14312057,
    processes=[procs.graviton_hh_vbf_bbtautau_m400],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-400_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=300000,
)

# missing
# campaign_run2_2017.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m450_madgraph",
#     id=,
#     processes=[procs.graviton_hh_vbf_bbtautau_m450],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-450_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=,
#     n_events=,
# )

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m500_madgraph",
    id=14312369,
    processes=[procs.graviton_hh_vbf_bbtautau_m500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=297000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m550_madgraph",
    id=14312211,
    processes=[procs.graviton_hh_vbf_bbtautau_m550],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-550_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m600_madgraph",
    id=14312266,
    processes=[procs.graviton_hh_vbf_bbtautau_m600],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-600_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m650_madgraph",
    id=14312370,
    processes=[procs.graviton_hh_vbf_bbtautau_m650],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-650_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m700_madgraph",
    id=14313347,
    processes=[procs.graviton_hh_vbf_bbtautau_m700],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-700_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=198000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m750_madgraph",
    id=14312212,
    processes=[procs.graviton_hh_vbf_bbtautau_m750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m800_madgraph",
    id=14312060,
    processes=[procs.graviton_hh_vbf_bbtautau_m800],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-800_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=18,
    n_events=200000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m850_madgraph",
    id=14312295,
    processes=[procs.graviton_hh_vbf_bbtautau_m850],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=200000,
)

# missing
# campaign_run2_2017.add_dataset(
#     name="graviton_hh_vbf_bbtautau_m900_madgraph",
#     id=,
#     processes=[procs.graviton_hh_vbf_bbtautau_m900],
#     keys=[
#         "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=,
#     n_events=,
# )

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1000_madgraph",
    id=14312631,
    processes=[procs.graviton_hh_vbf_bbtautau_m1000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1250_madgraph",
    id=14311308,
    processes=[procs.graviton_hh_vbf_bbtautau_m1250],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1500_madgraph",
    id=14311279,
    processes=[procs.graviton_hh_vbf_bbtautau_m1500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m1750_madgraph",
    id=14312650,
    processes=[procs.graviton_hh_vbf_bbtautau_m1750],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-1750_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m2000_madgraph",
    id=14312081,
    processes=[procs.graviton_hh_vbf_bbtautau_m2000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m2500_madgraph",
    id=14312147,
    processes=[procs.graviton_hh_vbf_bbtautau_m2500],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-2500_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=100000,
)

campaign_run2_2017.add_dataset(
    name="graviton_hh_vbf_bbtautau_m3000_madgraph",
    id=14313382,
    processes=[procs.graviton_hh_vbf_bbtautau_m3000],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-3000_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=100000,
)
