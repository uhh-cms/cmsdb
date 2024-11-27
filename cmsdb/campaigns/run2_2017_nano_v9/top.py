# coding: utf-8

"""
top quark datasets for the 2017 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_v9 import campaign_run2_2017_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
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

cpn.add_dataset(
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

cpn.add_dataset(
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
    ),
)


cpn.add_dataset(
    name="tt_fh_166p5_powheg",
    id=14242959,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=94184000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_169p5_powheg",
    id=14235980,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=76,
            n_events=90427000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_171p5_powheg",
    id=14243327,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=108,
            n_events=96894000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_173p5_powheg",
    id=14235630,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=89579000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_175p5_powheg",
    id=14242924,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=98568000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_178p5_powheg",
    id=14242958,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
            ],
            n_files=101,
            n_events=95963000,
        ),
    ),
)


#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttz_zlep_m10toinf_amcatnlo",
    id=14229512,
    processes=[procs.ttz_zlep_m10toinf],
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

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=14228083,
    processes=[procs.ttw_wlnu],
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

cpn.add_dataset(
    name="ttw_wqq_amcatnlo",
    id=14235122,
    processes=[procs.ttw_wqq],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=655018,
)


#
# ttbar + 2 vector bosons
#

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14234743,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=327000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14230416,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=350000,
)

cpn.add_dataset(
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

cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
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

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
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

cpn.add_dataset(
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

cpn.add_dataset(
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

cpn.add_dataset(
    name="st_schannel_lep_4f_amcatnlo",
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

cpn.add_dataset(
    name="st_schannel_had_4f_amcatnlo",
    id=14378997,
    processes=[procs.st_schannel_had],
    keys=[
        "/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
    ],
    n_files=34,
    n_events=11696999,
)
