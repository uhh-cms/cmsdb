
# coding: utf-8

""""
HH -> bbVV datasets for the run3_2023_postBPix_nano_v12 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2023_postBPix_nano_v12 import run3_2023_postBPix_nano_v12 as cpn


cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=14951647,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v1/NANOAODSIM",  # noqa
            ],
            n_files=89,
            n_events=594432,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=14932796,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=149854,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=14854361,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v2-v2/NANOAODSIM",  # noqa
            ],
            n_files=50,
            n_events=495374,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=14945507,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer23BPixNanoAODv12-130X_mcRun3_2023_realistic_postBPix_v6-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=149445,
        ),
    ),
)
