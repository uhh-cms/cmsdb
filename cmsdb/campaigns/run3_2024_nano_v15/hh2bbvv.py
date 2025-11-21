# coding: utf-8

"""
HH -> bbVV datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ggf -> HH
#

# todo

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15437989,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=1196998,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15436549,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=11,  # 11-0
            n_events=1199997,
        ),
    ),
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15435128,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=25,  # 25-0
            n_events=1198995,
        ),
    ),
)

#
# ggf -> graviton -> HH
#

# todo

#
# ggf -> radion -> HH
#

# todo
