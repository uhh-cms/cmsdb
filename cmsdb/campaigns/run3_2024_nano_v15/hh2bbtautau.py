# coding: utf-8

"""
HH -> bbtautau datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_powheg",
    id=15311493,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=101,
    n_events=957_670,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl0_kt1_powheg",
    id=15358679,
    processes=[procs.hh_ggf_hbb_htt_kl0_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=988_954,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl2p45_kt1_powheg",
    id=15360433,
    processes=[procs.hh_ggf_hbb_htt_kl2p45_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=951_424,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl5_kt1_powheg",
    id=15352759,
    processes=[procs.hh_ggf_hbb_htt_kl5_kt1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=1_000_000,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2_powheg",
    id=15357546,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c2m2],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-m2p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=72,
    n_events=996_178,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p1_powheg",
    id=15348599,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p1],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p10-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=177,
    n_events=987_994,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35_powheg",
    id=15350646,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c20p35],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-0p35-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=110,
    n_events=976_200,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c21_powheg",
    id=15351264,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c21],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-1p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=998_815,
)

cpn.add_dataset(
    name="hh_ggf_hbb_htt_kl1_kt1_c23_powheg",
    id=15352094,
    processes=[procs.hh_ggf_hbb_htt_kl1_kt1_c23],
    keys=[
        "/GluGluHHto2B2Tau_Par-c2-3p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-PowhegBugFix_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=999_563,
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1_madgraph",
    id=15415832,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=4_863_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1_madgraph",
    id=15415606,
    processes=[procs.hh_vbf_hbb_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=5_000_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15415579,
    processes=[procs.hh_vbf_hbb_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=50,
    n_events=5_000_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15415906,
    processes=[procs.hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=4_999_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15415745,
    processes=[procs.hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=4_859_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15415789,
    processes=[procs.hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=4_924_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15415597,
    processes=[procs.hh_vbf_hbb_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=5_000_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15415831,
    processes=[procs.hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=5_000_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15415631,
    processes=[procs.hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Tau_Par-CV1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=4_876_000,
)

cpn.add_dataset(
    name="hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15415634,
    processes=[procs.hh_vbf_hbb_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Tau_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=46,
    n_events=5_000_000,
)

#
# ggf -> graviton -> HH
#

# tba

#
# ggf -> radion -> HH
#

# tba
