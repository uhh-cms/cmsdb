# # coding: utf-8

# """
# HH -> 4tau/4v/2tau2v (multi-lepton) datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
# version 14, created with custom content at UHH.
# """

# import cmsdb.processes as procs
# from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v14 import campaign_run3_2022_postEE_nano_uhh_v14 as cpn


# #
# # ggf -> HH -> 4tau
# #

# cpn.add_dataset(
#     name="hh_ggf_htt_htt_kl1_kt1_powheg",
#     id=14879347,
#     processes=[procs.hh_ggf_htt_htt_kl1_kt1],
#     keys=[
#         "/GluGlutoHHto4Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v5/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=767_655,
#     aux={
#         "merging_factors": {
#             "nominal": 55,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_htt_htt_kl0_kt1_powheg",
#     id=15004720,
#     processes=[procs.hh_ggf_htt_htt_kl0_kt1],
#     keys=[
#         "/GluGlutoHHto4Tau_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=775_360,
#     aux={
#         "merging_factors": {
#             "nominal": 38,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_htt_htt_kl5_kt1_powheg",
#     id=15005136,
#     processes=[procs.hh_ggf_htt_htt_kl5_kt1],
#     keys=[
#         "/GluGlutoHHto4Tau_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=776_790,
#     aux={
#         "merging_factors": {
#             "nominal": 42,
#         },
#     },
# )

# #
# # ggf -> HH -> 4v
# #

# cpn.add_dataset(
#     name="hh_ggf_hvv_hvv_kl1_kt1_powheg",
#     id=14857679,
#     processes=[procs.hh_ggf_hvv_hvv_kl1_kt1],
#     keys=[
#         "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#         "/GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6_ext1-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4 + 15,
#     n_events=1_536_558 + 6_137_408,
#     aux={
#         "merging_factors": {
#             "nominal": 40,
#             "nominal_ext1": 25,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_hvv_hvv_kl0_kt1_powheg",
#     id=15005157,
#     processes=[procs.hh_ggf_hvv_hvv_kl0_kt1],
#     keys=[
#         "/GluGlutoHHto4V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_544_689,
#     aux={
#         "merging_factors": {
#             "nominal": 47,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_hvv_hvv_kl5_kt1_powheg",
#     id=15005139,
#     processes=[procs.hh_ggf_hvv_hvv_kl5_kt1],
#     keys=[
#         "/GluGlutoHHto4V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22MiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=438_426,
#     aux={
#         "merging_factors": {
#             "nominal": 43,
#         },
#     },
# )

# #
# # ggf -> HH -> 2tau2v
# #

# cpn.add_dataset(
#     name="hh_ggf_htt_hvv_kl1_kt1_powheg",
#     id=14880211,
#     processes=[procs.hh_ggf_htt_hvv_kl1_kt1],
#     keys=[
#         "/GluGlutoHHto2Tau2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_132_924,
#     aux={
#         "merging_factors": {
#             "nominal": 16,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_htt_hvv_kl0_kt1_powheg",
#     id=15004472,
#     processes=[procs.hh_ggf_htt_hvv_kl0_kt1],
#     keys=[
#         "/GluGlutoHHto2Tau2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_164_730,
#     aux={
#         "merging_factors": {
#             "nominal": 47,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_ggf_htt_hvv_kl5_kt1_powheg",
#     id=15005151,
#     processes=[procs.hh_ggf_htt_hvv_kl5_kt1],
#     keys=[
#         "/GluGlutoHHto2Tau2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_166_354,
#     aux={
#         "merging_factors": {
#             "nominal": 35,
#         },
#     },
# )

# #
# # vbf -> HH -> 4tau qq
# #

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kv1_k2v1_kl1_madgraph",
#     id=14845912,
#     processes=[procs.hh_vbf_htt_htt_kv1_k2v1_kl1],
#     keys=[
#         "/VBFHHto4Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_373_210,
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kv1_k2v0_kl1_madgraph",
#     id=14790993,
#     processes=[procs.hh_vbf_htt_htt_kv1_k2v0_kl1],
#     keys=[
#         "/VBFHHto4Tau_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_363_025,
#     aux={
#         "merging_factors": {
#             "nominal": 13,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4_madgraph",
#     id=14879515,
#     processes=[procs.hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4],
#     keys=[
#         "/VBFHHto4Tau_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=309_188,
#     aux={
#         "merging_factors": {
#             "nominal": 23,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
#     id=14879942,
#     processes=[procs.hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2],
#     keys=[
#         "/VBFHHto4Tau_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=310_582,
#     aux={
#         "merging_factors": {
#             "nominal": 26,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
#     id=14879028,
#     processes=[procs.hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3],
#     keys=[
#         "/VBFHHto4Tau_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=311_292,
#     aux={
#         "merging_factors": {
#             "nominal": 24,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
#     id=14880673,
#     processes=[procs.hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43],
#     keys=[
#         "/VBFHHto4Tau_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=312_000,
#     aux={
#         "merging_factors": {
#             "nominal": 23,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
#     id=14879681,
#     processes=[procs.hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94],
#     keys=[
#         "/VBFHHto4Tau_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=307_830,
#     aux={
#         "merging_factors": {
#             "nominal": 29,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
#     id=14879932,
#     processes=[procs.hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36],
#     keys=[
#         "/VBFHHto4Tau_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=308_475,
#     aux={
#         "merging_factors": {
#             "nominal": 26,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
#     id=14885026,
#     processes=[procs.hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39],
#     keys=[
#         "/VBFHHto4Tau_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=310_592,
#     aux={
#         "merging_factors": {
#             "nominal": 19,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96_madgraph",
#     id=14880800,
#     processes=[procs.hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96],
#     keys=[
#         "/VBFHHto4Tau_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=1,
#     n_events=310_566,
#     aux={
#         "merging_factors": {
#             "nominal": 23,
#         },
#     },
# )

# #
# # vbf -> HH -> 4v qq
# #

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kv1_k2v1_kl1_madgraph",
#     id=14836647,
#     processes=[procs.hh_vbf_hvv_hvv_kv1_k2v1_kl1],
#     keys=[
#         "/VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v1/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1_325_841,
#     aux={
#         "merging_factors": {
#             "nominal": 12,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kv1_k2v0_kl1_madgraph",
#     id=14791476,
#     processes=[procs.hh_vbf_hvv_hvv_kv1_k2v0_kl1],
#     keys=[
#         "/VBFHHto4V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=1_373_999,
#     aux={
#         "merging_factors": {
#             "nominal": 9,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
#     id=14879568,
#     processes=[procs.hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4],
#     keys=[
#         "/VBFHHto4V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=933_147,
#     aux={
#         "merging_factors": {
#             "nominal": 22,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
#     id=14877377,
#     processes=[procs.hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2],
#     keys=[
#         "/VBFHHto4V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=929_125,
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
#     id=14879244,
#     processes=[procs.hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3],
#     keys=[
#         "/VBFHHto4V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=935_281,
#     aux={
#         "merging_factors": {
#             "nominal": 20,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
#     id=14880695,
#     processes=[procs.hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43],
#     keys=[
#         "/VBFHHto4V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=933_124,
#     aux={
#         "merging_factors": {
#             "nominal": 22,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
#     id=14880243,
#     processes=[procs.hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94],
#     keys=[
#         "/VBFHHto4V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=932_587,
#     aux={
#         "merging_factors": {
#             "nominal": 16,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
#     id=14879041,
#     processes=[procs.hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36],
#     keys=[
#         "/VBFHHto4V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=917_798,
#     aux={
#         "merging_factors": {
#             "nominal": 32,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
#     id=14884457,
#     processes=[procs.hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39],
#     keys=[
#         "/VBFHHto4V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=926_429,
#     aux={
#         "merging_factors": {
#             "nominal": 31,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
#     id=14879358,
#     processes=[procs.hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96],
#     keys=[
#         "/VBFHHto4V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=935_994,
#     aux={
#         "merging_factors": {
#             "nominal": 17,
#         },
#     },
# )

# #
# # vbf -> HH -> 2tau2v qq
# #

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kv1_k2v1_kl1_madgraph",
#     id=14791224,
#     processes=[procs.hh_vbf_htt_hvv_kv1_k2v1_kl1],
#     keys=[
#         "/VBFHHto2Tau2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=2_714_037,
#     aux={
#         "merging_factors": {
#             "nominal": 10,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kv1_k2v0_kl1_madgraph",
#     id=14801500,
#     processes=[procs.hh_vbf_htt_hvv_kv1_k2v0_kl1],
#     keys=[
#         "/VBFHHto2Tau2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=7,
#     n_events=2_715_133,
#     aux={
#         "merging_factors": {
#             "nominal": 8,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
#     id=14879626,
#     processes=[procs.hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4],
#     keys=[
#         "/VBFHHto2Tau2V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=620_460,
#     aux={
#         "merging_factors": {
#             "nominal": 18,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
#     id=14879630,
#     processes=[procs.hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=619_852,
#     aux={
#         "merging_factors": {
#             "nominal": 19,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
#     id=14879602,
#     processes=[procs.hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=623_992,
#     aux={
#         "merging_factors": {
#             "nominal": 14,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
#     id=14879214,
#     processes=[procs.hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=622_603,
#     aux={
#         "merging_factors": {
#             "nominal": 17,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
#     id=14879557,
#     processes=[procs.hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=622_618,
#     aux={
#         "merging_factors": {
#             "nominal": 20,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
#     id=14879215,
#     processes=[procs.hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=623_988,
#     aux={
#         "merging_factors": {
#             "nominal": 18,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
#     id=14885331,
#     processes=[procs.hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=602_633,
#     aux={
#         "merging_factors": {
#             "nominal": 19,
#         },
#     },
# )

# cpn.add_dataset(
#     name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
#     id=14879703,
#     processes=[procs.hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96],
#     keys=[
#         "/VBFHHto2Tau2V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22EEMiniAODv4_NanoAODv14UHH-130X_mcRun3_2022_realistic_postEE_v6-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=617_659,
#     aux={
#         "merging_factors": {
#             "nominal": 16,
#         },
#     },
# )
