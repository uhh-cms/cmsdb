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
