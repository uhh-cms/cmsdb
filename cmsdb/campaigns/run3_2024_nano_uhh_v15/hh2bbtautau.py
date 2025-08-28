# coding: utf-8

"""
HH -> bbtautau datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15,
created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_uhh_v15 import campaign_run3_2024_nano_uhh_v15 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=15310876,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=957_840,
    aux={
        "merging_factors": {
            "nominal": 43,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=15357596,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=988_954,
    aux={
        "merging_factors": {
            "nominal": 28,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=15357954,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=951_424,
    aux={
        "merging_factors": {
            "nominal": 30,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=15352757,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_000_000,
    aux={
        "merging_factors": {
            "nominal": 32,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=15355649,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-m2p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=996_178,
    aux={
        "merging_factors": {
            "nominal": 35,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p1_powheg",
    id=15348575,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p10-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=988_063,
    aux={
        "merging_factors": {
            "nominal": 68,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=15350639,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p35-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=976_285,
    aux={
        "merging_factors": {
            "nominal": 46,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c21_powheg",
    id=15351267,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c21],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-1p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=998_025,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=15352090,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-3p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6_NanoAODv15UHH-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=999_563,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)
