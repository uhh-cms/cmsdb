
# coding: utf-8

""""
Electroweak datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import run3_2023_postBPix_nano_v12 as cpn


#
# dy (NLO)
#

cpn.add_dataset(
    name="dy_m4to10_amcatnlo",
    id=14940060,
    processes=[procs.dy_m4to10],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-4to10_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=269,
            n_events=97791089,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m10to50_amcatnlo",
    id=14905314,
    processes=[procs.dy_m10to50],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2_ext1-v3/NANOAODSIM",  # noqa
            ],
            n_files=328,
            n_events=100386286,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_amcatnlo",
    id=14851777,
    processes=[procs.dy_m50toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=221,
            n_events=95472230,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_0j_amcatnlo",
    id=14892918,
    processes=[procs.dy_m50toinf_0j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=310,
            n_events=96625525,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_amcatnlo",
    id=14897399,
    processes=[procs.dy_m50toinf_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=408,
            n_events=68804529,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_amcatnlo",
    id=14894111,
    processes=[procs.dy_m50toinf_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
            ],
            n_files=330,
            n_events=91293455,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=14826831,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=184,
            n_events=51259552,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=14826692,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=133,
            n_events=19223496,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=14830394,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=1921207,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=14824633,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=459553,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=14826181,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=456439,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt40to100_amcatnlo",
    id=14826590,
    processes=[procs.dy_m50toinf_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=160,
            n_events=20410287,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt100to200_amcatnlo",
    id=14826152,
    processes=[procs.dy_m50toinf_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=117,
            n_events=19286517,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt200to400_amcatnlo",
    id=14823828,
    processes=[procs.dy_m50toinf_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=3623077,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt400to600_amcatnlo",
    id=14825726,
    processes=[procs.dy_m50toinf_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=493730,
        ),
    ),
)
cpn.add_dataset(
    name="dy_m50toinf_2j_pt600toinf_amcatnlo",
    id=14832728,
    processes=[procs.dy_m50toinf_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_MLL-50_PTLL-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v1/NANOAODSIM",  # noqa
            ],
            n_files=29,
            n_events=477040,
        ),
    ),
)

#
# w_lnu
#
cpn.add_dataset(
    name="w_lnu_amcatnlo",
    id=14978436,
    processes=[procs.w_lnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=352,
            n_events=95759797,
        ),
    ),
)
# cpn.add_dataset(
#     name="w_lnu_0j_amcatnlo",
#     id=14911430,
#     processes=[procs.w_lnu_0j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=620,
#             n_events=199057715,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_amcatnlo",
#     id=14896271,
#     processes=[procs.w_lnu_1j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=704,
#             n_events=149340770,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_amcatnlo",
#     id=14912985,
#     processes=[procs.w_lnu_2j],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
#             ],
#             n_files=458,
#             n_events=99486651,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu100to200_amcatnlo",
#     id=14892199,
#     processes=[procs.w_lnu_1j_ptlnu100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-100to200_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=278,
#             n_events=46180146,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu40to100_amcatnlo",
#     id=14890369,
#     processes=[procs.w_lnu_1j_ptlnu40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-40to100_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=447,
#             n_events=99944613,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu200to400_amcatnlo",
#     id=14890786,
#     processes=[procs.w_lnu_1j_ptlnu200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-200to400_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=13,
#             n_events=2804887,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu400to600_amcatnlo",
#     id=14892483,
#     processes=[procs.w_lnu_1j_ptlnu400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-400to600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=19,
#             n_events=511690,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_1j_ptlnu600toinf_amcatnlo",
#     id=14895242,
#     processes=[procs.w_lnu_1j_ptlnu600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-600_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=20,
#             n_events=552078,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu40to100_amcatnlo",
#     id=14892446,
#     processes=[procs.w_lnu_2j_ptlnu40to100],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-40to100_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=460,
#             n_events=98450124,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu100to200_amcatnlo",
#     id=14893885,
#     processes=[procs.w_lnu_2j_ptlnu100to200],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-100to200_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=207,
#             n_events=48375806,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu200to400_amcatnlo",
#     id=14892582,
#     processes=[procs.w_lnu_2j_ptlnu200to400],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-200to400_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=87,
#             n_events=5237325,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu400to600_amcatnlo",
#     id=14889898,
#     processes=[procs.w_lnu_2j_ptlnu400to600],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-400to600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=7,
#             n_events=498986,
#         ),
#     ),
# )
# cpn.add_dataset(
#     name="w_lnu_2j_ptlnu600toinf_amcatnlo",
#     id=14890643,
#     processes=[procs.w_lnu_2j_ptlnu600toinf],
#     info=dict(
#         nominal=DatasetInfo(
#             keys=[
#                 "/WtoLNu-2Jets_PTLNu-600_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v3/NANOAODSIM",  # noqa
#             ],
#             n_files=34,
#             n_events=477908,
#         ),
#     ),
# )

#
# diboson
#

cpn.add_dataset(
    name="ww_pythia",
    id=14783236,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=54,
            n_events=16734000,
        ),
    ),
)
cpn.add_dataset(
    name="zz_pythia",
    id=14784123,
    processes=[procs.zz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=1254000,
        ),
    ),
)
cpn.add_dataset(
    name="wz_pythia",
    id=14784070,
    processes=[procs.wz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZ_TuneCP5_13p6TeV_pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=8379000,
        ),
    ),
)
