# coding: utf-8

"""
HH -> bbtautau datasets for the 2022 postEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn  # noqa


#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14853029,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22EEMiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_postEE_v6-v3/NANOAODSIM",  # noqa
    ],
    n_files=6,
    n_events=3_047_884,
    aux={
        "merging_factors": {
            "nominal": 54,
        },
    },
)

# different couplings, keeping c2 = 0

# different bsm couplings, with c2 != 0


#
# VBF -> H -> HH
#

#
# ggf -> graviton -> HH
#

#
# ggf -> radion -> HH
#
