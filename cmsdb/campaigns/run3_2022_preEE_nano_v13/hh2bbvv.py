# coding: utf-8

"""
HH -> bbWW datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v13 import campaign_run3_2022_preEE_nano_v13 as cpn

#
# ggf, HH -> bbVV
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=15005110,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=219513,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=15005186,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=219487,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=15006294,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=12,
            n_events=88000,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=15005218,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=33,
            n_events=87544,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=15006214,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-0p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=86758,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=15006629,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-5p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=32,
            n_events=87393,
        ),
    ),
)

#
# vbf, HH -> bbVV
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14965511,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=27,
            n_events=219317,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14960983,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=87999,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=14964628,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m1p83_C2V-3p57_C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv13-133X_mcRun3_2022_realistic_ForNanov13_v1-v2/NANOAODSIM",  # noqa
            ],
            n_files=1,
            n_events=87999,
        ),
    ),
)
