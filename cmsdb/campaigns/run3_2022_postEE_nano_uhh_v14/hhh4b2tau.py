# # coding: utf-8

# """
# HHH -> bbbbtautau datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
# version 14, created with custom content at UHH.
# """

# import cmsdb.processes as procs
# from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn


# #
# # HHH
# #

# cpn.add_dataset(
#     name="hhh_4b2tau_c31_d40_amcatnlo",
#     id=14795416,
#     processes=[procs.hhh_4b2tau_c31_d40],
#     keys=[
#         "/HHHto4B2Tau_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_375_520,
#     aux={
#         "merging_factors": {
#             "nominal": 11,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c34_d49_amcatnlo",
#     id=14792341,
#     processes=[procs.hhh_4b2tau_c34_d49],
#     keys=[
#         "/HHHto4B2Tau_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_385_237,
#     aux={
#         "merging_factors": {
#             "nominal": 9,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c3m1_d40_amcatnlo",
#     id=14801983,
#     processes=[procs.hhh_4b2tau_c3m1_d40],
#     keys=[
#         "/HHHto4B2Tau_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_377_362,
#     aux={
#         "merging_factors": {
#             "nominal": 11,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c31_d42_amcatnlo",
#     id=14793990,
#     processes=[procs.hhh_4b2tau_c31_d42],
#     keys=[
#         "/HHHto4B2Tau_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_318_128,
#     aux={
#         "merging_factors": {
#             "nominal": 10,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c32_d4m1_amcatnlo",
#     id=14800924,
#     processes=[procs.hhh_4b2tau_c32_d4m1],
#     keys=[
#         "/HHHto4B2Tau_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_346_201,
#     aux={
#         "merging_factors": {
#             "nominal": 10,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c30_d40_amcatnlo",
#     id=14791947,
#     processes=[procs.hhh_4b2tau_c30_d40],
#     keys=[
#         "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=90,
#     n_events=33_444_440,
#     aux={
#         "merging_factors": {
#             "nominal": 9,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c30_d499_amcatnlo",
#     id=14791856,
#     processes=[procs.hhh_4b2tau_c30_d499],
#     keys=[
#         "/HHHto4B2Tau_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_397_915,
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c30_d4m1_amcatnlo",
#     id=14791893,
#     processes=[procs.hhh_4b2tau_c30_d4m1],
#     keys=[
#         "/HHHto4B2Tau_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_367_993,
#     aux={
#         "merging_factors": {
#             "nominal": 12,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c319_d419_amcatnlo",
#     id=14797468,
#     processes=[procs.hhh_4b2tau_c319_d419],
#     keys=[
#         "/HHHto4B2Tau_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_393_835,
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c3m1_d4m1_amcatnlo",
#     id=14800863,
#     processes=[procs.hhh_4b2tau_c3m1_d4m1],
#     keys=[
#         "/HHHto4B2Tau_c3-minus1_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_466_975,
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hhh_4b2tau_c3m1p5_d4m0p5_amcatnlo",
#     id=14791669,
#     processes=[procs.hhh_4b2tau_c3m1p5_d4m0p5],
#     keys=[
#         "/HHHto4B2Tau_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_381_552,
#     aux={
#         "merging_factors": {
#             "nominal": 11,
#         },
#     },
# )
