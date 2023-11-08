# coding: utf-8

"""
Top quark datasets for the 2018 data-taking campaign with datasets at NanoAOD tier in
version 11, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_uhh_v11 import campaign_run2_2018_nano_uhh_v11 as cpn

#
# ttbar
#
# semi leptonic
cpn.add_dataset(
    name="tt_sl_powheg",
    id=,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[

            ],
            n_files=,
            n_events=,
        ),
        tune_down=DatasetInfo(
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=179,
            n_events=190086000,
        ),
        hdamp_down=DatasetInfo(
               ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=198,
            n_events=199398000,
        ),
        mtop171p5=DatasetInfo(
        ),
        mtop173p5=DatasetInfo(


        ),
    ),
)








cpn.add_dataset(
    name="tt_dl_powheg",
    id=14188237,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[

            ],
            n_files=123,
            n_events=106724000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=4891000,
        ),
        tune_up=DatasetInfo(
            keys=[

            ],
            n_files=123,
            n_events=106724000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=59958000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=52,
            n_events=54510000,
        ),
        mtop171p5=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=59846000,
        ),
        mtop173p5=DatasetInfo(


        ),
    ),
)



# Fully hadronic
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14222447,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[

            ],
            n_files=,
            n_events=,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=139,
            n_events=139820000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
            ],
            n_files=296,
            n_events=235719999,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=138,
            n_events=139490000,
               ),
        hdamp_up=DatasetInfo(
            keys=[
                ,  # noqa
            ],
            n_files=,
            n_events=,
        ),
        mtop171p5=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=134,
            n_events=135314000,
        ),
        mtop173p5=DatasetInfo(
            keys=[
            "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=138,
            n_events=139624000,
        ),
    ),
)










cpn.add_dataset(
    name="THE_NAME",
    id=14206476,
    processes=[procs.THE_PROCESS],
    keys=[
        "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=136,
    n_events=137313999,
)


#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttz_2l2nu_amcatnlo",
    id=14241155,
    processes=[procs.ttz_2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=19608000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5up_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=7930000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5down_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=7990000,
        ),
    ),
)


cpn.add_dataset(
    name="ttw_lnu_amcatnlo",
    id=14197046,
    processes=[procs.ttw_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
            ],
            n_files=14,
            n_events=10516349,
        ),
        tune_down=DatasetInfo(
            keys=[
            "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=4214235,
        ),
        tune_up=DatasetInfo(
            keys=[
            "/TTWJetsToLNu_TuneCP5up_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM",  # noqa
        ],
        n_files=6,
        n_events=4169942,
        ),
    ),
)



cpn.add_dataset(
    name="ttw_2q_amcatnlo",
    id=14207353,
    processes=[procs.ttw_2q],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=970179,
)

#
# ttbar + 2 vector bosons
#
cpn.add_dataset(
    name="ttzz_madgraph",
    id=14211818,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=498000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14213045,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=498000,
)


cpn.add_dataset(
    name="ttww_madgraph",
    id=14218071,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv12-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=944000,
)

#
# single top
#

# cpn.add_dataset(
#     name="st_tchannel_t_powheg",
#     id=14294738,
#     processes=[procs.st_tchannel_t],
#     keys=[
#         "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=124,
#     n_events=129903000,
# )

# cpn.add_dataset(
#     name="st_tchannel_tbar_powheg",
#     id=14296512,
#     processes=[procs.st_tchannel_tbar],
#     keys=[
#         "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=70,
#     n_events=69921000,
# )
# cpn.add_dataset(
#     name="st_twchannel_t_powheg",
#     id=14246006,
#     processes=[procs.st_twchannel_t],
#     keys=[
#         "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=5649000,
# )

# cpn.add_dataset(
#     name="st_twchannel_tbar_powheg",
#     id=14251337,
#     processes=[procs.st_twchannel_tbar],
#     keys=[
#         "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=5674000,
# )
