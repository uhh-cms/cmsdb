# coding: utf-8

"""
Top quark related datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=15292847,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=790,
            n_events=484_475_057,
        ),
        # missing:
        # hdamp_down
        # hdamp_up
        # mtop_down
        # mtop_up
        # tune_down
        # tune_up
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=15304231,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=780,
            n_events=470_123_263,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=406,
            n_events=59_915_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=368,
            n_events=59_985_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=372,
            n_events=59_987_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=373,
            n_events=59_982_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=379,
            n_events=59_967_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=383,
            n_events=59_987_000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=15296265,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=773,
            n_events=472_535_695,
        ),
        # missing:
        # hdamp_down
        # hdamp_up
        # mtop_down
        # mtop_up
        # tune_down
        # tune_up
    ),
)

#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15393690,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-EWK_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=38,
    n_events=2_999_000,
)

# missing
# cpn.add_dataset(
#     name="ttz_zqq_amcatnlo",
#     ...
# )

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=15390973,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=2_965_000,
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=15390855,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=3_952_000,
)

# missing
# cpn.add_dataset(
#     name="ttz_znunu_amcatnlo",
#     ...
# )

#
# ttbar + 2 vector boson
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=15393150,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=5_801_000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=15393070,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=51,
    n_events=5_529_000,
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=15292170,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ-ZZto4B_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=9_911_305,
)

#
# single top
#

cpn.add_dataset(
    name="st_tchannel_t_had_4f_powheg",
    id=15370314,
    processes=[procs.st_tchannel_t_had],
    keys=[
        "/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=778,
    n_events=87_576_444,
)

cpn.add_dataset(
    name="st_tchannel_tbar_had_4f_powheg",
    id=15363774,
    processes=[procs.st_tchannel_tbar_had],
    keys=[
        "/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=825,
    n_events=43_273_264,
)

cpn.add_dataset(
    name="st_tchannel_t_lep_4f_powheg",
    id=15316276,
    processes=[procs.st_tchannel_t_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=391,
            n_events=44_258_039,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=218,
            n_events=21_903_026,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TBbarQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=389,
            n_events=22_008_628,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_lep_4f_powheg",
    id=15316115,
    processes=[procs.st_tchannel_tbar_lep],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=249,
            n_events=22_102_160,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5Down_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=188,
            n_events=10_997_130,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarBQtoLNu-t-channel-4FS_TuneCP5Up_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=11_000_625,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=15377565,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=252,
            n_events=28_763_293,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=233,
            n_events=29_787_089,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=254,
            n_events=29_889_675,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=238,
            n_events=31_799_777,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=236,
            n_events=29_671_243,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=209,
            n_events=30_179_634,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=247,
            n_events=28_506_776,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=15376087,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=252,
            n_events=29_395_659,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=251,
            n_events=32_748_146,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=218,
            n_events=27_886_841,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=234,
            n_events=31_313_302,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=251,
            n_events=28_932_755,
        ),
        # missing:
        # tune_down
        # tune_up
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=15376104,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=176,
            n_events=14_998_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=150,
            n_events=14_980_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=172,
            n_events=14_998_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=14_986_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=226,
            n_events=14_861_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=111,
            n_events=15_000_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=206,
            n_events=14_972_000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=15376044,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=90,
            n_events=15_000_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=167,
            n_events=15_000_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=145,
            n_events=15_000_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=163,
            n_events=14_998_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=186,
            n_events=15_000_000,
        ),
        # missing:
        # tune_down
        # tune_up
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=15375712,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=154,
            n_events=23_999_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=203,
            n_events=23_991_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=216,
            n_events=23_992_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=182,
            n_events=23_991_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=160,
            n_events=23_948_000,
        ),
        # missing:
        # tune_down
        # tune_up
    ),
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=15375023,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=195,
            n_events=24_000_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=203,
            n_events=24_000_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=223,
            n_events=23_997_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=180,
            n_events=23_999_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Par-MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=222,
            n_events=23_996_000,
        ),
        # missing:
        # tune_down
        # tune_up
    ),
)

# missing
# cpn.add_dataset(
#     name="st_schannel_t_lep_4f_amcatnlo",
#     ...
# )

# missing
# cpn.add_dataset(
#     name="st_schannel_tbar_lep_4f_amcatnlo",
#     ...
# )

#
# 4 top
#

# missing
# cpn.add_dataset(
#     name="tttt_amcatnlo",
#     ...
# )
