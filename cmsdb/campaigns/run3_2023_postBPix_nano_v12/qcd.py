
# coding: utf-8

""""
QCD datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import campaign_run3_2023_postBPix_nano_v12 as cpn

#
# qcd_mu
#

cpn.add_dataset(
    name="qcd_mu_pt15to20_pythia",
    id=14781363,
    processes=[procs.qcd_mu_pt15to20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=4999275,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt20to30_pythia",
    id=14781373,
    processes=[procs.qcd_mu_pt20to30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-20to30_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=166,
            n_events=33206620,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt30to50_pythia",
    id=14784056,
    processes=[procs.qcd_mu_pt30to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-30to50_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=137,
            n_events=31900002,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt50to80_pythia",
    id=14784155,
    processes=[procs.qcd_mu_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-50to80_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=53,
            n_events=12720414,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt80to120_pythia",
    id=14784054,
    processes=[procs.qcd_mu_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-80to120_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=84,
            n_events=26692302,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt120to170_pythia",
    id=14783279,
    processes=[procs.qcd_mu_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-120to170_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=85,
            n_events=22380325,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt170to300_pythia",
    id=14783386,
    processes=[procs.qcd_mu_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-170to300_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=125,
            n_events=33223105,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt300to470_pythia",
    id=14784117,
    processes=[procs.qcd_mu_pt300to470],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-300to470_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=122,
            n_events=31622567,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt470to600_pythia",
    id=14783278,
    processes=[procs.qcd_mu_pt470to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-470to600_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=23080052,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt600to800_pythia",
    id=14783146,
    processes=[procs.qcd_mu_pt600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-600to800_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=113,
            n_events=22886334,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt800to1000_pythia",
    id=14783121,
    processes=[procs.qcd_mu_pt800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-800to1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=195,
            n_events=41077955,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_mu_pt1000toinf_pythia",
    id=14783282,
    processes=[procs.qcd_mu_pt1000toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1000_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=82,
            n_events=15340005,
        ),
    ),
)

#
# qcd_em
#

cpn.add_dataset(
    name="qcd_em_pt10to30_pythia",
    id=14788948,
    processes=[procs.qcd_em_pt10to30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=1024670,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt20to30_pythia",
    id=14839068,
    processes=[procs.qcd_em_pt20to30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-20to30_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=490689,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt30to50_pythia",
    id=14790510,
    processes=[procs.qcd_em_pt30to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=1031074,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt50to80_pythia",
    id=14790653,
    processes=[procs.qcd_em_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=985509,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt170to300_pythia",
    id=14790413,
    processes=[procs.qcd_em_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=1073461,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt80to120_pythia",
    id=14790458,
    processes=[procs.qcd_em_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=1021976,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt120to170_pythia",
    id=14790461,
    processes=[procs.qcd_em_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=1051454,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_em_pt300toinf_pythia",
    id=14791448,
    processes=[procs.qcd_em_pt300toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-300_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=979712,
        ),
    ),
)

#
# qcd_bctoe
#

cpn.add_dataset(
    name="qcd_bctoe_pt15to20_pythia",
    id=14788413,
    processes=[procs.qcd_bctoe_pt15to20],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-15to20_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=1031112,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_bctoe_pt20to30_pythia",
    id=14790357,
    processes=[procs.qcd_bctoe_pt20to30],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-20to30_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=8,
            n_events=1081911,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_bctoe_pt30to80_pythia",
    id=14789857,
    processes=[procs.qcd_bctoe_pt30to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-30to80_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=1064292,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_bctoe_pt80to170_pythia",
    id=14790910,
    processes=[procs.qcd_bctoe_pt80to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-80to170_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=7,
            n_events=1054505,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_bctoe_pt170to250_pythia",
    id=14791454,
    processes=[procs.qcd_bctoe_pt170to250],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-170to250_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=6,
            n_events=1074495,
        ),
    ),
)
cpn.add_dataset(
    name="qcd_bctoe_pt250toinf_pythia",
    id=14789426,
    processes=[procs.qcd_bctoe_pt250toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-250_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=1029902,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt80to120_pythia",
    id=14784328,
    processes=[procs.qcd_pt80to120],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,  # 36-0
            n_events=8967000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt50to80_pythia",
    id=14784058,
    processes=[procs.qcd_pt50to80],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=5988000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt3200toinf_pythia",
    id=14784336,
    processes=[procs.qcd_pt3200toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3,  # 3-0
            n_events=240000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt170to300_pythia",
    id=14784113,
    processes=[procs.qcd_pt170to300],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=37,  # 37-0
            n_events=8934000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt600to800_pythia",
    id=14784216,
    processes=[procs.qcd_pt600to800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=97,  # 97-0
            n_events=20374000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt120to170_pythia",
    id=14784225,
    processes=[procs.qcd_pt120to170],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,  # 36-0
            n_events=8964000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt300to470_pythia",
    id=14784205,
    processes=[procs.qcd_pt300to470],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=83,  # 83-0
            n_events=17354000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt470to600_pythia",
    id=14784208,
    processes=[procs.qcd_pt470to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=45,  # 45-0
            n_events=8384000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1000to1400_pythia",
    id=14784236,
    processes=[procs.qcd_pt1000to1400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=5980000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt800to1000_pythia",
    id=14784239,
    processes=[procs.qcd_pt800to1000],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=61,  # 61-0
            n_events=11976000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt2400to3200_pythia",
    id=14784267,
    processes=[procs.qcd_pt2400to3200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=5,  # 5-0
            n_events=599000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1400to1800_pythia",
    id=14784325,
    processes=[procs.qcd_pt1400to1800],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=10,  # 10-0
            n_events=1794000,
        ),
    ),
)

cpn.add_dataset(
    name="qcd_pt1800to2400_pythia",
    id=14784360,
    processes=[procs.qcd_pt1800to2400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=6,  # 6-0
            n_events=900000,
        ),
    ),
)

# cpn.add_dataset(
#     name="qcd_pt600toinf_pythia",
#     id=14839841,
#     processes=[procs.qcd_pt600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_PT-600_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
#             ],
#             aux={
#                 "broken_files": [],
#             },
#             n_files=46,  # 46-0
#             n_events=998000,
#         ),
#     ),
# )

cpn.add_dataset(
    name="qcd_pt30to50_pythia",
    id=14839424,
    processes=[procs.qcd_pt30to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/QCD_PT-30to50_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=46,  # 46-0
            n_events=3994000,
        ),
    ),
)
