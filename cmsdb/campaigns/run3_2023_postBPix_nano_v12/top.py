
# coding: utf-8

""""
top quark datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

#
# ttbar
#

# cpn.add_dataset(
#     name="tt_sl_9j_ht500toinf_powheg",
#     id=14916723,
#     processes=[procs.tt_sl_9j_ht500toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTtoLNu2Q_HT-500_NJet-9_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=71,
#             n_events=1919279,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TTtoLNu2Q_HT-500_NJet-9_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=78,
#             n_events=1010179,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TTtoLNu2Q_HT-500_NJet-9_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=65,
#             n_events=988828,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TTtoLNu2Q_HT-500_NJet-9_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=35,
#             n_events=1111382,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TTtoLNu2Q_HT-500_NJet-9_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=148,
#             n_events=1010771,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="tt_dl_7j_ht500toinf_powheg",
#     id=14917727,
#     processes=[procs.tt_dl_7j_ht500toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/TTto2L2Nu_HT-500_NJet-7_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=32,
#             n_events=2023507,
#         ),
#         hdamp_up=DatasetInfo(
#             keys=[
#                 "/TTto2L2Nu_HT-500_NJet-7_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=31,
#             n_events=965714,
#         ),
#         hdamp_down=DatasetInfo(
#             keys=[
#                 "/TTto2L2Nu_HT-500_NJet-7_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=39,
#             n_events=1044835,
#         ),
#         tune_down=DatasetInfo(
#             keys=[
#                 "/TTto2L2Nu_HT-500_NJet-7_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=37,
#             n_events=933911,
#         ),
#         tune_up=DatasetInfo(
#             keys=[
#                 "/TTto2L2Nu_HT-500_NJet-7_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=35,
#             n_events=981780,
#         ),
#     ),
# )
cpn.add_dataset(
    name="tt_sl_powheg",
    id=14808334,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=492,
            n_events=82058000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=307,
            n_events=32916000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=218,
            n_events=32046000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=281,
            n_events=31781999,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=183,
            n_events=32436000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=200,
            n_events=32406000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=348,
            n_events=32130000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=247,
            n_events=32910000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=184,
            n_events=32640000,
        ),
    ),
)
cpn.add_dataset(
    name="tt_dl_amcatnlo",
    id=14837042,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=476,
            n_events=46623781,
        ),
    ),
)
cpn.add_dataset(
    name="tt_dl_powheg",
    id=14835967,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=150,
            n_events=24649000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=83,
            n_events=9913000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=69,
            n_events=9640000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=9997000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=9745000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=9763000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=55,
            n_events=9766000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=9871000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=9880000,
        ),
    ),
)
cpn.add_dataset(
    name="tt_fh_amcatnlo",
    id=14885067,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=697,
            n_events=81363574,
        ),
    ),
)
cpn.add_dataset(
    name="tt_fh_powheg",
    id=14808891,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=429,
            n_events=53044000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=92,
            n_events=22919000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=234,
            n_events=22961000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=206,
            n_events=22466000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=198,
            n_events=22100000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=270,
            n_events=22289000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=202,
            n_events=21865999,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=281,
            n_events=22961000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=242,
            n_events=22886000,
        ),
    ),
)

#
# single top, s-channel
#

cpn.add_dataset(
    name="st_schannel_t_lep_4f_amcatnlo",
    id=14977863,
    processes=[procs.st_schannel_t_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=1276000,
        ),
    ),
)
cpn.add_dataset(
    name="st_schannel_tbar_lep_4f_amcatnlo",
    id=14977873,
    processes=[procs.st_schannel_tbar_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=788000,
        ),
    ),
)

#
# single top, t-channel
#

cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=15016893,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=84,
            n_events=2954000,
        ),
    ),
)
cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=15018232,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=1488000,
        ),
    ),
)

#
# single top, tW-channel
#
cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14812782,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=4952467,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=35,
            n_events=5048960,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=5040352,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=4888605,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=94,
            n_events=4955507,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=5043341,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=60,
            n_events=5114762,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=5169872,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=4959659,
        ),
    ),
)
cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14836358,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=2479000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=2425000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=2485000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=2404000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=2428000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=2488000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=2494000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=2383000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=2356000,
        ),
    ),
)
cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14819392,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=3964000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=3871000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=3907000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=3937000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=3961000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=3940000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=3835000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=3952000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=3940000,
        ),
    ),
)
cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14928656,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=5177861,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=4688170,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=4787655,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=4989681,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=36,
            n_events=5003322,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=4959854,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=58,
            n_events=4924253,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=47,
            n_events=4769760,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=4769064,
        ),
    ),
)
cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14930339,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=2488000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=2449000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=2488000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=2479000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=2491000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=2446000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=2494000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=2347000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=2458000,
        ),
    ),
)
cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14928584,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=3967000,
        ),
        cr_1=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR1_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=3961000,
        ),
        cr_2=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5CR2_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=3913000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=3997000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=3991000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=3958000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=3949000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=3946000,
        ),
    ),
)

#
# ttW
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15137890,
    processes=[procs.ttw_wlnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=1,
            n_events=256078,
        ),
    ),
)

#
# ttZ
#

cpn.add_dataset(
    name="ttz_zqq_amcatnlo",
    id=15141013,
    processes=[procs.ttz_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=388921,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=14982175,
    processes=[procs.ttz_zll_m4to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=294000,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=14989610,
    processes=[procs.ttz_zll_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=400000,
        ),
        extension=DatasetInfo(
            keys=[
                "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6_ext1-v2/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=3856000,
        ),
    ),
)
cpn.add_dataset(
    name="ttz_znunu_amcatnlo",
    id=14928725,
    processes=[procs.ttz_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=492000,
        ),
    ),
)

#
# ttVV
#

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14937861,
    processes=[procs.ttzz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=992000,
        ),
    ),
)
cpn.add_dataset(
    name="ttww_madgraph",
    id=14931988,
    processes=[procs.ttww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=74,
            n_events=7288000,
        ),
    ),
)
cpn.add_dataset(
    name="ttwz_madgraph",
    id=14969073,
    processes=[procs.ttwz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=497000,
        ),
    ),
)

#
# tttt
#


cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14987188,
    processes=[procs.tttt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=43,  # 43-0
            n_events=2477775,
        ),
    ),
)

#
# ttg, tg
#

cpn.add_dataset(
    name="ttg_pt10to100_amcatnlo",
    id=14998315,
    processes=[procs.ttg_pt10to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=966829,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt200toinf_amcatnlo",
    id=14987335,
    processes=[procs.ttg_pt200toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=17,  # 17-0
            n_events=274550,
        ),
    ),
)

cpn.add_dataset(
    name="ttg_pt100to200_amcatnlo",
    id=14998309,
    processes=[procs.ttg_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=18,  # 18-0
            n_events=299074,
        ),
    ),
)

cpn.add_dataset(
    name="tgqb_amcatnlo",
    id=15200781,
    processes=[procs.tgqb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,  # 31-0
            n_events=2194000,
        ),
    ),
)
