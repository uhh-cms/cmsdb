# coding: utf-8

"""
HH -> bbWW datasets for the 2023 pre-BPix data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_preBPix_nano_v12 import campaign_run3_2023_preBPix_nano_v12 as cpn


cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=14932681,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=65,
            n_events=299375,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=14940655,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v3/NANOAODSIM",  # noqa
            ],
            n_files=161,
            n_events=1191452,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=14940898,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v15-v4/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=299199,
        ),
    ),
)
