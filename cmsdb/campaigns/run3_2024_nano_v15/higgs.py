# coding: utf-8

"""
Higgs datasets for the 2024 data-taking campaign (Nano v15)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import run3_2024_nano_v15 as cpn


#
# Single Higgs
#


####################################################################################################
#
# h_ggf (H->TauTau)
#
####################################################################################################

cpn.add_dataset(
    name="h_ggf_htt_powheg",
    id=15349270,
    processes=[procs.h_ggf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-HTo2Tau_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=120,  # 120-0
            n_events=11984270,
        ),
    ),
)

####################################################################################################
#
# h_ggf (H->ZZ)
#
####################################################################################################

# 4l

cpn.add_dataset(
    name="h_ggf_hzz4l_powheg",
    id=15379753,
    processes=[procs.h_ggf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=1397000,
        ),
    ),
)

# 4 nu
cpn.add_dataset(
    name="h_ggf_hzz4nu_powheg",
    id=15351568,
    processes=[procs.h_ggf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2Zto4Nu_Bin-PT-150_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=251,  # 251-0
            n_events=15739013,
        ),
    ),
)

# llqq not yet

# llnunu not yet

####################################################################################################
#
# h_ggf (H->WW)
#
####################################################################################################

# 2lnu
cpn.add_dataset(
    name="h_ggf_hww2l2nu_powheg",
    id=15349216,
    processes=[procs.h_ggf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluHto2Wto2L2Nu_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=153,  # 153-0
            n_events=17941370,
        ),
    ),
)

# lnuqq not yet

####################################################################################################
#
# h_ggf (H->MuMu)
#
####################################################################################################

# amcatnlo
cpn.add_dataset(
    name="h_ggf_hmm_amcatnlo",
    id=15382509,
    processes=[procs.h_ggf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2Mu_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=80,  # 80-0
            n_events=2551454,
        ),
    ),
)

# powheg
cpn.add_dataset(
    name="h_ggf_hmm_powheg",
    id=15361348,
    processes=[procs.h_ggf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2Mu_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=72,  # 72-0
            n_events=2800000,
        ),
    ),
)

####################################################################################################
#
# h_ggf (H->gg)
#
####################################################################################################

# amcatnlo
cpn.add_dataset(
    name="PLACEHOLDER_amcatnlo",
    id=15289769,
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=118,  # 118-0
            n_events=7841082,
        ),
    ),
)

# powheg
cpn.add_dataset(
    name="h_ggf_hgg_powheg",
    id=15381593,
    processes=[procs.h_ggf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2G_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=1000000,
        ),
    ),
)

####################################################################################################
#
# h_ggf (H->bb)
#
####################################################################################################

# inclusive
cpn.add_dataset(
    name="h_ggf_hbb_powheg",
    id=15315620,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=36,  # 36-0
            n_events=9874198,
        ),
        extension=DatasetInfo(
            keys=[
                "/GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=188,  # 188-0
            n_events=19933636,
        ),
    ),
)

# boosted
cpn.add_dataset(
    name="h_ggf_hbb_boosted_powheg",
    id=15321774,
    processes=[procs.h_ggf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-Hto2B_Bin-PT-200_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=60,  # 60-0
            n_events=9693936,
        ),
    ),
)

####################################################################################################
#
# h_ggf (H->Zg)
#
####################################################################################################

cpn.add_dataset(
    name="h_ggf_hzg_powheg",
    id=15380444,
    processes=[procs.h_ggf_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGluH-HtoZG_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=599998,
        ),
    ),
)

####################################################################################################
#
# h_vbf (H->TauTau)
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_htt_powheg",
    id=15348632,
    processes=[procs.h_vbf_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-HTo2Tau_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=173,  # 173-0
            n_events=11987544,
        ),
    ),
)

####################################################################################################
#
# h_vbf (H->ZZ)
#
####################################################################################################

# 4l
cpn.add_dataset(
    name="h_vbf_hzz4l_powheg",
    id=15381251,
    processes=[procs.h_vbf_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=26,  # 26-0
            n_events=1372933,
        ),
        extension=DatasetInfo(
            keys=[
                "/VBFH-Hto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=19,  # 19-0
            n_events=1396000,
        ),
    ),
)

# 4nu NLO
cpn.add_dataset(
    name="h_vbf_hzz4nu_powheg",
    id=15353707,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2Zto4Nu_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=92,  # 92-0
            n_events=6999303,
        ),
    ),
)

# 4nu LO
cpn.add_dataset(
    name="h_vbf_hzz4nu_madgraph",
    id=15359537,
    processes=[procs.h_vbf_hzz4nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2Zto4Nu_Par-M-125_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=158,  # 158-0
            n_events=14000000,
        ),
    ),
)

# llqq not yet

# llnunu not yet

####################################################################################################
#
# h_vbf (H->WW)
#
####################################################################################################

# 2lnu
cpn.add_dataset(
    name="h_vbf_hww2l2nu_powheg",
    id=15349432,
    processes=[procs.h_vbf_hww2l2nu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHto2Wto2L2Nu_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=135,  # 135-0
            n_events=17957727,
        ),
    ),
)

# lnuqq not yet

####################################################################################################
#
# h_vbf (H->MuMu)
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_hmm_powheg",
    id=15352163,
    processes=[procs.h_vbf_hmm],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2Mu_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=99,  # 99-0
            n_events=5593000,
        ),
    ),
)

####################################################################################################
#
# h_vbf (H->gg)
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_hgg_amcatnlo",
    id=15290514,
    processes=[procs.h_vbf_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=4482288,
        ),
    ),
)

####################################################################################################
#
# h_vbf (H->bb)
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_hbb_powheg",
    id=15370443,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=40,  # 40-0
            n_events=9989440,
        ),
        extension=DatasetInfo(
            keys=[
                "/VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2_ext1-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=222,  # 222-0
            n_events=19990298,
        ),
    ),
)

cpn.add_dataset(
    name="h_vbf_hbb_amcatnlo",
    id=15290514,
    processes=[procs.h_vbf_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-Hto2G_Par-M-125_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=4482288,
        ),
    ),
)

####################################################################################################
#
# h_vbf (H->Zg)
#
####################################################################################################

cpn.add_dataset(
    name="h_vbf_hzg_powheg",
    id=15380757,
    processes=[procs.h_vbf_hzg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-HtoZG_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=600000,
        ),
    ),
)

cpn.add_dataset(
    name="h_vbf_hzg_zll_powheg",
    id=15380574,
    processes=[procs.h_vbf_hzg_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFH-HtoZGto2LG_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=41,  # 41-0
            n_events=1400000,
        ),
    ),
)

####################################################################################################
#
# WH
#
####################################################################################################

# non b
cpn.add_dataset(
    name="wph_hnonbb_amcatnlo",
    id=15349193,
    processes=[procs.wph_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=51,  # 51-0
            n_events=4074508,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_hnonbb_amcatnlo",
    id=15349203,
    processes=[procs.wmh_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=46,  # 46-0
            n_events=3697133,
        ),
    ),
)

# Hbb, W leptonic
cpn.add_dataset(
    name="wph_wlnu_hbb_powheg",
    id=15321740,
    processes=[procs.wph_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=28,  # 28-0
            n_events=3068881,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wlnu_hbb_powheg",
    id=15330078,
    processes=[procs.wmh_wlnu_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=20,  # 20-0
            n_events=1976960,
        ),
    ),
)

# Hbb, W hadronic
cpn.add_dataset(
    name="wph_wqq_hbb_powheg",
    id=15325013,
    processes=[procs.wph_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WplusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=30,  # 30-0
            n_events=6261825,
        ),
    ),
)
cpn.add_dataset(
    name="wmh_wqq_hbb_powheg",
    id=15341180,
    processes=[procs.wmh_wqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WminusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=3966909,
        ),
    ),
)


####################################################################################################
#
# ZH
#
####################################################################################################

# H non bb
cpn.add_dataset(
    name="zh_hnonbb_amcatnlo",
    id=15349371,
    processes=[procs.zh_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=46,  # 46-0
            n_events=4188141,
        ),
    ),
)

# Hbb
cpn.add_dataset(
    name="zh_zll_hbb_powheg",
    id=15370480,
    processes=[procs.zh_zll_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH-Zto2L-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=32,  # 32-0
            n_events=960506,
        ),
    ),
)
cpn.add_dataset(
    name="zh_zqq_hbb_powheg",
    id=15382483,
    processes=[procs.zh_zqq_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=23,  # 23-0
            n_events=2877591,
        ),
    ),
)

# Z to nunu
cpn.add_dataset(
    name="zh_znunu_powheg",
    id=15324831,
    processes=[procs.zh_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZH-Zto2Nu-Hto2S_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=13,  # 13-0
            n_events=250000,
        ),
    ),
)

####################################################################################################
#
# TTH
#
####################################################################################################

cpn.add_dataset(
    name="tth_hbb_powheg",
    id=15382320,
    processes=[procs.tth_hbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=22,  # 22-0
            n_events=2443910,
        ),
    ),
)
cpn.add_dataset(
    name="tth_hnonbb_powheg",
    id=15349148,
    processes=[procs.tth_hnonbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=531,  # 531-0
            n_events=53980865,
        ),
    ),
)

####################################################################################################
#
# tHq / tHW
#
####################################################################################################

# no thq/thw and ttZH

####################################################################################################
#
# TTVH
#
####################################################################################################

cpn.add_dataset(
    name="ttwh_madgraph",
    id=15396854,
    processes=[procs.ttwh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWH_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=100,  # 100-0
            n_events=10595000,
        ),
    ),
)

cpn.add_dataset(
    name="ttzh_hbb_zbb_madgraph",
    id=15292701,
    processes=[procs.ttzh_hbb_zbb],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZH-ZHto4B_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=9984820,
        ),
    ),
)

# inclusive ZH missing!

####################################################################################################
#
# bbH
#
####################################################################################################

cpn.add_dataset(
    name="bbh_hgg_powheg",
    id=15382441,
    processes=[procs.bbh_hgg],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/BBH-Hto2G_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=15,  # 15-0
            n_events=1499300,
        ),
    ),
)

cpn.add_dataset(
    name="bbh_htt_powheg",
    id=15350425,
    processes=[procs.bbh_htt],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/BBH-Hto2Tau_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=31,  # 31-0
            n_events=1754262,
        ),
    ),
)

cpn.add_dataset(
    name="bbh_hzz4l_pythia8",
    id=15379571,
    processes=[procs.bbh_hzz4l],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/BBH-Hto2Zto4L_Par-M-125_TuneCP5_13p6TeV_jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=1368210,
        ),
    ),
)
