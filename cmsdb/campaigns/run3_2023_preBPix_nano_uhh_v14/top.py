# coding: utf-8

"""
Top quark related datasets for the 2023 preBPix data-taking campaign with datasets at NanoAOD tier
in version 14, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14 import campaign_run3_2023_preBPix_nano_uhh_v14 as cpn  # noqa


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14808300,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=343,
            n_events=152_653_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=145,
            n_events=65_733_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=142,
            n_events=63_552_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=147,
            n_events=65_859_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=147,
            n_events=65_403_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=149,
            n_events=64_449_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=144,
            n_events=65_829_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 13,
            "hdamp_down": 14,
            "hdamp_up": 14,
            "mtop_down": 12,
            "mtop_up": 12,
            "tune_down": 14,
            "tune_up": 14,
        },
    },
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14821822,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=102,
            n_events=48_104_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=19_646_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=46,
            n_events=19_631_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=19_805_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=19_604_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=19_573_999,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=19_694_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 12,
            "hdamp_down": 13,
            "hdamp_up": 12,
            "mtop_down": 12,
            "mtop_up": 12,
            "tune_down": 13,
            "tune_up": 12,
        },
    },
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14809512,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=236,
            n_events=104_963_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=101,
            n_events=45_736_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=102,
            n_events=44_992_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=103,
            n_events=44_365_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=45_748_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=97,
            n_events=45_205_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=99,
            n_events=45_873_999,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 12,
            "hdamp_down": 14,
            "hdamp_up": 13,
            "mtop_down": 14,
            "mtop_up": 15,
            "tune_down": 11,
            "tune_up": 11,
        },
    },
)

#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15138235,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=460_305,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo",
    id=14995482,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=591_000,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo",
    id=14998320,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=791_000,
    aux={
        "merging_factors": {
            "nominal": 16,
        },
    },
)

cpn.add_dataset(
    name="ttz_znunu_amcatnlo",
    id=14930188,
    processes=[procs.ttz_znunu],
    keys=[
        "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=976_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

#
# ttbar + 2 vector boson
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14942215,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=14_598_000,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14969090,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14942734,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=1_994_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

#
# single top
#

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14819509,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=9_650_268,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=9_888_273,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=9_602_848,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=9_734_131,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=9_651_040,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=9_821_540,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=9_758_668,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 16,
            "hdamp_down": 15,
            "hdamp_up": 14,
            "mtop_down": 15,
            "mtop_up": 14,
            "tune_down": 15,
            "tune_up": 14,
        },
    },
)

# TODO: st_twchannel_tbar_sl_powheg nominal missing, variations are produced but not added here without nominal


cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14834108,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_985_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_961_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_982_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_970_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_937_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_982_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_956_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 15,
            "hdamp_down": 16,
            "hdamp_up": 10,
            "mtop_down": 17,
            "mtop_up": 14,
            "tune_down": 16,
            "tune_up": 18,
        },
    },
)


cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14929075,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_907_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_676_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_888_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_880_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_960_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_925_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_913_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 14,
            "hdamp_down": 16,
            "hdamp_up": 14,
            "mtop_down": 15,
            "mtop_up": 15,
            "tune_down": 15,
            "tune_up": 13,
        },
    },
)


cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14825787,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_919_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_943_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_937_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_940_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_880_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_610_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v14-v2/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_991_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 11,
            "hdamp_down": 11,
            "hdamp_up": 13,
            "mtop_down": 14,
            "mtop_up": 15,
            "tune_down": 13,
            "tune_up": 13,
        },
    },
)


cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14929407,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_970_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=8_000_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_865_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_757_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_853_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_835_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=7_862_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 12,
            "hdamp_down": 16,
            "hdamp_up": 12,
            "mtop_down": 12,
            "mtop_up": 14,
            "tune_down": 13,
            "tune_up": 13,
        },
    },
)


cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=15017144,
    processes=[procs.st_tchannel_t_4f],
    keys=[
        "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=10,
    n_events=5_908_000,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)


cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=15017107,
    processes=[procs.st_tchannel_tbar_4f],
    keys=[
        "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2_878_000,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)


cpn.add_dataset(
    name="st_schannel_t_lep_4f_amcatnlo",
    id=14980849,
    processes=[procs.st_schannel_t_lep_4f],
    keys=[
        "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=2_588_000,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="st_schannel_tbar_lep_4f_amcatnlo",
    id=14982343,
    processes=[procs.st_schannel_tbar_lep_4f],
    keys=[
        "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23MiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_v15-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_600_000,
    aux={
        "merging_factors": {
            "nominal": 24,
        },
    },
)
