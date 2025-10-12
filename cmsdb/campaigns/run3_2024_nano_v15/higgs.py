# coding: utf-8

"""
Higgs datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# Single Higgs
#

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=15381457,
    processes=[procs.h_ggf_htt],
    keys=[
        "/GluGluHto2Tau_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=146,
    n_events=14_994_000,
)

cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=15349216,
    processes=[procs.h_ggf_hww2l2nu],
    keys=[
        "/GluGluHto2Wto2L2Nu_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=153,
    n_events=17_941_370,
)

cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=15381502,
    processes=[procs.h_ggf_hzz4l],
    keys=[
        "/GluGluHto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=157,
    n_events=14_967_000,
)

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=15348632,
    processes=[procs.h_vbf_htt],
    keys=[
        "/VBFH-HTo2Tau_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=173,
    n_events=11_987_544,
)

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=15370443,
    processes=[procs.h_vbf_hbb],
    keys=[
        "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
        "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2_ext1-v2/NANOAODSIM",  # noqa
    ],
    n_files=40 + 222,
    n_events=9_989_440 + 19_990_298,
)

cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=15349432,
    processes=[procs.h_vbf_hww2l2nu],
    keys=[
        "/VBFHto2Wto2L2Nu_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=135,
    n_events=17_957_727,
)

cpn.add_dataset(
    name="h_vbf_hzz4l_powheg",
    id=15381251,
    processes=[procs.h_vbf_hzz4l],
    keys=[
        "/VBFHto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=1_372_933,
)

cpn.add_dataset(
    name="wph_htt_powheg",
    id=15383312,
    processes=[procs.wph_htt],
    keys=[
        "/WplusH-Hto2TauUncorrelatedDecay_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=280_000,
)

cpn.add_dataset(
    name="wmh_htt_powheg",
    id=15383101,
    processes=[procs.wmh_htt],
    keys=[
        "/WminusH-Hto2TauUncorrelatedDecay_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=280_000,
)

cpn.add_dataset(
    name="zh_htt_powheg",
    id=15383091,
    processes=[procs.zh_htt],
    keys=[
        "/ZH-Hto2TauUncorrelatedDecay_Par-M-125_TuneCP5_13p6TeV_powhegMINNLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=280_000,
)

cpn.add_dataset(
    name="zh_gg_zll_hbb_powheg",
    id=15315686,
    processes=[procs.zh_gg_zll_hbb],
    keys=[
        "/GluGluZH-Zto2L-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=500_000,
)

cpn.add_dataset(
    name="zh_gg_zqq_hbb_powheg",
    id=15324846,
    processes=[procs.zh_gg_zqq_hbb],
    keys=[
        "/GluGluZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=500_000,
)

cpn.add_dataset(
    name="zh_gg_znunu_hbb_powheg",
    id=15325070,
    processes=[procs.zh_gg_znunu_hbb],
    keys=[
        "/GluGluZH-Zto2Nu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=1_000_000,
)

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=15382320,
    processes=[procs.tth_hbb],
    keys=[
        "/TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=22,
    n_events=2_443_910,
)

cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=15349148,
    processes=[procs.tth_hnonbb],
    keys=[
        "/TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=531,
    n_events=53_980_865,
)

#
# tH
#

# tba

#
# ttVH
#

cpn.add_dataset(
    name="ttwh_madgraph",
    id=15396854,
    processes=[procs.ttwh],
    keys=[
        "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=100,
    n_events=10_595_000,
)
