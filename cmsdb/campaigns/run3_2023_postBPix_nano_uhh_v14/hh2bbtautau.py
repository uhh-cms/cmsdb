# coding: utf-8

"""
HH -> bbtautau datasets for the 2023 postBPix data-taking campaign with datasets at NanoAOD tier in
version 14, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_uhh_v14 import campaign_run3_2023_postBPix_nano_uhh_v14 as cpn  # noqa


#
# ggF -> H -> HH
#

# SM
cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=14960628,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixMiniAODv4_NanoAODv14UHH-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1_331_688,
    aux={
        "merging_factors": {
            "nominal": 42,
        },
    },
)

# different couplings, keeping c2 = 0
# tba

# different bsm couplings, with c2 != 0
# tba

#
# vbf -> H -> HH
#

# tba

#
# ggf -> graviton -> HH
#

# tba

#
# ggf -> radion -> HH
#

# tba
