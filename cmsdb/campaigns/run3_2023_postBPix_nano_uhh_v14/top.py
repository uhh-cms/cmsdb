# coding: utf-8

"""
Top quark related datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier
in version 14, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14808105,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=153,
            n_events=63_875_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=75,
            n_events=31_941_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=32_343_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=78,
            n_events=31_646_999,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=77,
            n_events=32_862_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=78,
            n_events=32_022_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTtoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=79,
            n_events=32_910_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 13,
            "hdamp_down": 14,
            "hdamp_up": 14,
            "mtop_down": 13,
            "mtop_up": 13,
            "tune_down": 13,
            "tune_up": 13,
        },
    },
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14835872,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=24_556_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=9_628_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=9_838_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=9_871_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=9_901_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=9_718_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=9_631_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 12,
            "hdamp_down": 12,
            "hdamp_up": 14,
            "mtop_down": 12,
            "mtop_up": 13,
            "tune_down": 12,
            "tune_up": 12,
        },
    },
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14808894,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=124,
            n_events=52_849_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=22_337_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=22_109_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=22_862_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=51,
            n_events=22_091_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=22_976_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=22_937_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 14,
            "hdamp_down": 14,
            "hdamp_up": 15,
            "mtop_down": 15,
            "mtop_up": 14,
            "tune_down": 15,
            "tune_up": 14,
        },
    },
)

#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=15137889,
    processes=[procs.ttw_wlnu],
    keys=[
        "/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=256_078,
    aux={
        "merging_factors": {
            "nominal": 7,
        },
    },
)

cpn.add_dataset(
    name="ttz_zqq_amcatnlo",
    id=15139133,
    processes=[procs.ttz_zqq],
    keys=[
        "/TTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=388_921,
    aux={
        "merging_factors": {
            "nominal": 14,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m4to50_amcatnlo", # -> checked entry by hand (9th Sep 2025), issue with DAS files not found
    id=14982174,
    processes=[procs.ttz_zll_m4to50],
    keys=[
        "/TTLL_MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=294_000,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="ttz_zll_m50toinf_amcatnlo", # -> checked entry by hand (9th Sep 2025), issue with DAS files not found
    id=14989609,
    processes=[procs.ttz_zll_m50toinf],
    keys=[
        "/TTLL_MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=400_000,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="ttz_znunu_amcatnlo",
    id=14928724,
    processes=[procs.ttz_znunu],
    keys=[
        "/TTNuNu_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=492_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

#
# ttbar + 2 vector boson
#

cpn.add_dataset(
    name="ttww_madgraph",
    id=14931912,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=7_418_000,
    aux={
        "merging_factors": {
            "nominal": 12,
        },
    },
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14969071,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=497_000,
    aux={
        "merging_factors": {
            "nominal": 8,
        },
    },
)

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14937859,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13p6TeV_madgraph-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=4,
    n_events=954_000,
    aux={
        "merging_factors": {
            "nominal": 13,
        },
    },
)

#
# single top
#

cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=15016763,
    processes=[procs.st_tchannel_t],
    keys=[
        "/TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=2_954_000,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=15018188,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_488_000,
    aux={
        "merging_factors": {
            "nominal": 29,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_t_sl_powheg",
    id=14812740,
    processes=[procs.st_twchannel_t_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_943_378,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_888_605,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=5_048_960,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=5_068_156,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=5_043_341,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=5_157_188,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=5_018_950,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 14,
            "hdamp_down": 16,
            "hdamp_up": 13,
            "mtop_down": 15,
            "mtop_up": 13,
            "tune_down": 12,
            "tune_up": 15,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_tbar_sl_powheg",
    id=14928655,
    processes=[procs.st_twchannel_tbar_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=5_146_630,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_924_253,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_772_037,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=5_033_791,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_989_681,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=4_644_563,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplustoLNu2Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=11,
            n_events=4_769_760,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 12,
            "hdamp_down": 16,
            "hdamp_up": 12,
            "mtop_down": 12,
            "mtop_up": 15,
            "tune_down": 16,
            "tune_up": 13,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_t_dl_powheg",
    id=14836225,
    processes=[procs.st_twchannel_t_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_479_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=2_422_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_485_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=2_377_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_428_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=2_383_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=2_266_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 16,
            "hdamp_down": 16,
            "hdamp_up": 15,
            "mtop_down": 17,
            "mtop_up": 12,
            "tune_down": 18,
            "tune_up": 18,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_tbar_dl_powheg",
    id=14930337,
    processes=[procs.st_twchannel_tbar_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_488_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_488_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_494_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_466_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_449_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_458_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto2L2Nu_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=2_491_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 17,
            "hdamp_down": 14,
            "hdamp_up": 13,
            "mtop_down": 14,
            "mtop_up": 15,
            "tune_down": 14,
            "tune_up": 12,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_t_fh_powheg",
    id=14819393,
    processes=[procs.st_twchannel_t_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_934_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_961_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_898_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_940_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_937_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=3_796_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TWminusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_877_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 11,
            "hdamp_down": 13,
            "hdamp_up": 13,
            "mtop_down": 14,
            "mtop_up": 14,
            "tune_down": 16,
            "tune_up": 13,
        },
    },
)

cpn.add_dataset(
    name="st_twchannel_tbar_fh_powheg",
    id=14928583,
    processes=[procs.st_twchannel_tbar_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_976_000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-158_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_946_000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_Hdamp-418_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_940_000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-171p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_997_000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_MT-173p5_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_958_000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Down_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_994_000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TbarWplusto4Q_TuneCP5Up_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3_991_000,
        ),
    ),
    aux={
        "merging_factors": {
            "nominal": 13,
            "hdamp_down": 12,
            "hdamp_up": 11,
            "mtop_down": 11,
            "mtop_up": 14,
            "tune_down": 10,
            "tune_up": 12,
        },
    },
)

cpn.add_dataset(
    name="st_schannel_t_lep_4f_amcatnlo",
    id=14977859,
    processes=[procs.st_schannel_t_lep],
    keys=[
        "/TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=1_288_000,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="st_schannel_tbar_lep_4f_amcatnlo",
    id=14977861,
    processes=[procs.st_schannel_tbar_lep],
    keys=[
        "/TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=784_000,
    aux={
        "merging_factors": {
            "nominal": 17,
        },
    },
)

#
# 4 top
#

cpn.add_dataset(
    name="tttt_amcatnlo",
    id=14987007,
    processes=[procs.tttt],
    keys=[
        "/TTTT_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=2_477_775,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)
