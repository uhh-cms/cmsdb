
# coding: utf-8

""""
QCD datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import run3_2023_postBPix_nano_v12 as cpn

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
# cpn.add_dataset(
#     name="qcd_em_pt300toinf_pythia",
#     id=14790517,
#     processes=[procs.qcd_em_pt300toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_PT-300toInf_EMEnriched_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=5,
#             n_events=842285,
#         ),
#     ),
# )

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
# cpn.add_dataset(
#     name="qcd_bctoe_pt250toinf_pythia",
#     id=14791904,
#     processes=[procs.qcd_bctoe_pt250toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/QCD_PT-250toInf_bcToE_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=6,
#             n_events=879679,
#         ),
#     ),
# )
