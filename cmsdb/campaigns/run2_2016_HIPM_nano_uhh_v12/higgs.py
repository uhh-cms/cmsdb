# coding: utf-8


"""Single Higgs datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH."""


import cmsdb.processes as procs  # noqa
from cmsdb.campaigns.run2_2016_HIPM_nano_uhh_v12 import campaign_run2_2016_HIPM_nano_uhh_v12 as cpn  # noqa

# ggf

# cpn.add_dataset(
#     name="h_ggf_htt_powheg",
#     id=14314017,
#     processes=[procs.h_ggf_htt],
#     keys=[
#         "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=4,
#     n_events=6430000,
# )

# vbf

# cpn.add_dataset(
#     name="h_vbf_htt_powheg",
#     id=14346935,
#     processes=[procs.h_vbf_htt],
#     keys=[
#         "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1395000,
# )

# H radiation

# cpn.add_dataset(
#     name="zh_htt_powheg",
#     id=14284521,
#     processes=[procs.zh_htt],
#     keys=[
#         "/ZHToTauTau_M125_CP5_13TeV-powheg-pythia8_ext1/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=2481740,
# )

# cpn.add_dataset(
#     name="wph_htt_powheg",
#     id=14337370,
#     processes=[procs.wph_htt],
#     keys=[
#         "/WplusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1915820,
# )

# cpn.add_dataset(
#     name="wmh_htt_powheg",
#     id=14335155,
#     processes=[procs.wmh_htt],
#     keys=[
#         "/WminusHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=2,
#     n_events=1976651,
# )


# ttH

# cpn.add_dataset(
#     name="tth_htt_powheg",
#     id=14340599,
#     processes=[procs.tth_htt],
#     keys=[
#         "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=15,
#     n_events=10865700,
# )

# cpn.add_dataset(
#     name="tth_hnonbb_powheg",
#     id=14278195,
#     processes=[procs.tth_hnonbb],
#     keys=[
#         "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=3,
#     n_events=1977996,
# )

# cpn.add_dataset(
#     name="tth_hbb_powheg",
#     id=14284890,
#     processes=[procs.tth_hbb],
#     keys=[
#         "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
#     ],
#     n_files=6,
#     n_events=4622000,
# )
