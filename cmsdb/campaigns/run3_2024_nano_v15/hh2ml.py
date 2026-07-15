# coding: utf-8

"""
HH -> 4tau/4v/2tau2v/2w2z (multi-lepton) datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in
version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ggf/vbf -> HH -> 4tau
#

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl0_kt1_powheg",
    id=15544701,
    processes=[procs.hh_ggf_htt_htt_kl0_kt1],
    keys=[
        "/GluGlutoHHto4Tau_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=139,
    n_events=989671,
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl1_kt1_powheg",
    id=15543589,
    processes=[procs.hh_ggf_htt_htt_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Tau_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=69,
    n_events=987220,
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl2p45_kt1_powheg",
    id=15546548,
    processes=[procs.hh_ggf_htt_htt_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto4Tau_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=88,
    n_events=1000000,
)

cpn.add_dataset(
    name="hh_ggf_htt_htt_kl5_kt1_powheg",
    id=15544753,
    processes=[procs.hh_ggf_htt_htt_kl5_kt1],
    keys=[
        "/GluGlutoHHto4Tau_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=106,
    n_events=983992,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1_madgraph",
    id=15556630,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4Tau_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=747000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1_madgraph",
    id=15554687,
    processes=[procs.hh_vbf_htt_htt_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Tau_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15547502,
    processes=[procs.hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4Tau_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15554105,
    processes=[procs.hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4Tau_Par-CV-m2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15550314,
    processes=[procs.hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4Tau_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=16,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15542832,
    processes=[procs.hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4Tau_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15551052,
    processes=[procs.hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4Tau_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=7,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15549901,
    processes=[procs.hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4Tau_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15554123,
    processes=[procs.hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4Tau_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=750000,
)

cpn.add_dataset(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15557586,
    processes=[procs.hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4Tau_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=750000,
)


#
# ggf/vbf -> HH -> 2tau2v
#

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl0_kt1_powheg",
    id=15544956,
    processes=[procs.hh_ggf_htt_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=194,
    n_events=1475834,
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl1_kt1_powheg",
    id=15544945,
    processes=[procs.hh_ggf_htt_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=118,
    n_events=1490653,
)

cpn.add_dataset(
    name="hh_ggf_htt_hvv_kl5_kt1_powheg",
    id=15543400,
    processes=[procs.hh_ggf_htt_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2Tau2V_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=209,
    n_events=1472666,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1_madgraph",
    id=15549173,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=1498983,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1_madgraph",
    id=15546755,
    processes=[procs.hh_vbf_htt_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=37,
    n_events=1499976,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15546932,
    processes=[procs.hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1499975,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15546647,
    processes=[procs.hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=1498980,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15546654,
    processes=[procs.hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1498979,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15542672,
    processes=[procs.hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=43,
    n_events=1499979,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15542348,
    processes=[procs.hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=1499972,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15549585,
    processes=[procs.hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=1485971,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15550784,
    processes=[procs.hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1497975,
)

cpn.add_dataset(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15541135,
    processes=[procs.hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2Tau2V_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=1499968,
)


#
# ggf/vbf -> HH -> 4V (2L+)
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_2lplus_kl0_kt1_powheg",
    id=15546485,
    processes=[procs.hh_ggf_hvv_hvv_2lplus_kl0_kt1],
    keys=[
        "/GluGlutoHHto4Vto2Lplus_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=168,
    n_events=1999457,
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_2lplus_kl1_kt1_powheg",
    id=15545073,
    processes=[procs.hh_ggf_hvv_hvv_2lplus_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Vto2Lplus_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=463,
    n_events=9858137,
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_2lplus_kl2p45_kt1_powheg",
    id=15543510,
    processes=[procs.hh_ggf_hvv_hvv_2lplus_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto4Vto2Lplus_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=369,
    n_events=1928736,
)

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_2lplus_kl5_kt1_powheg",
    id=15546497,
    processes=[procs.hh_ggf_hvv_hvv_2lplus_kl5_kt1],
    keys=[
        "/GluGlutoHHto4Vto2Lplus_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=223,
    n_events=1967567,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kv1_k2v0_kl1_madgraph",
    id=15498204,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=1995959,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kv1_k2v1_kl1_madgraph",
    id=15541128,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=103,
    n_events=4999914,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15546856,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1999961,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15541945,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1998965,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15545653,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=1999963,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15543648,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=55,
    n_events=1998967,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15541133,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1978964,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15549527,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1999963,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15542735,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=57,
    n_events=1951967,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15541995,
    processes=[procs.hh_vbf_hvv_hvv_2lplus_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto4Vto2Lplus_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=1998967,
)


#
# ggf/vbf -> HH -> 4V (1L)
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_1l_kl1_kt1_powheg",
    id=15541423,
    processes=[procs.hh_ggf_hvv_hvv_1l_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Vto1L_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=482191,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_1l_kv1_k2v1_kl1_madgraph",
    id=15548655,
    processes=[procs.hh_vbf_hvv_hvv_1l_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Vto1L_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=499991,
)


#
# ggf/vbf -> HH -> 4V (0L)
#

cpn.add_dataset(
    name="hh_ggf_hvv_hvv_0l_kl1_kt1_powheg",
    id=15541183,
    processes=[procs.hh_ggf_hvv_hvv_0l_kl1_kt1],
    keys=[
        "/GluGlutoHHto4Vto0L6Jplus_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=497061,
)

cpn.add_dataset(
    name="hh_vbf_hvv_hvv_0l_kv1_k2v1_kl1_madgraph",
    id=15549258,
    processes=[procs.hh_vbf_hvv_hvv_0l_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto4Vto0L6Jplus_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=499811,
)


#
# ggf/vbf -> HH -> 2W2Z (3L)
#

cpn.add_dataset(
    name="hh_ggf_hww_hzz_3l_kl0_kt1_powheg",
    id=15547225,
    processes=[procs.hh_ggf_hww_hzz_3l_kl0_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_3L_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=116,
    n_events=955226,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_3l_kl1_kt1_powheg",
    id=15547812,
    processes=[procs.hh_ggf_hww_hzz_3l_kl1_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_3L_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=67,
    n_events=992502,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_3l_kl2p45_kt1_powheg",
    id=15544943,
    processes=[procs.hh_ggf_hww_hzz_3l_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_3L_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=108,
    n_events=991719,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_3l_kl5_kt1_powheg",
    id=15540705,
    processes=[procs.hh_ggf_hww_hzz_3l_kl5_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_3L_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v1/NANOAODSIM",  # noqa
    ],
    n_files=78,
    n_events=979904,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kv1_k2v0_kl1_madgraph",
    id=15542821,
    processes=[procs.hh_vbf_hww_hzz_3l_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=499548,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kv1_k2v1_kl1_madgraph",
    id=15541314,
    processes=[procs.hh_vbf_hww_hzz_3l_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=500764,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15546872,
    processes=[procs.hh_vbf_hww_hzz_3l_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=501756,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15555642,
    processes=[procs.hh_vbf_hww_hzz_3l_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=488092,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15554224,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=499532,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15557531,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=499549,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15544069,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=499536,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15551996,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=497520,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15544396,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=15,
    n_events=500868,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_3l_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15542332,
    processes=[procs.hh_vbf_hww_hzz_3l_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_3L_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=499515,
)


#
# ggf/vbf -> HH -> 2W2Z (4L+)
#

cpn.add_dataset(
    name="hh_ggf_hww_hzz_4lplus_kl0_kt1_powheg",
    id=15543681,
    processes=[procs.hh_ggf_hww_hzz_4lplus_kl0_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_4Lplus_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=167,
    n_events=986156,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_4lplus_kl1_kt1_powheg",
    id=15544080,
    processes=[procs.hh_ggf_hww_hzz_4lplus_kl1_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_4Lplus_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=137,
    n_events=989527,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_4lplus_kl2p45_kt1_powheg",
    id=15546392,
    processes=[procs.hh_ggf_hww_hzz_4lplus_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_4Lplus_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=74,
    n_events=996194,
)

cpn.add_dataset(
    name="hh_ggf_hww_hzz_4lplus_kl5_kt1_powheg",
    id=15543293,
    processes=[procs.hh_ggf_hww_hzz_4lplus_kl5_kt1],
    keys=[
        "/GluGlutoHHto2W2ZVetoZto2Nu_4Lplus_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=40,
    n_events=1006969,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kv1_k2v0_kl1_madgraph",
    id=15554109,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=500732,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kv1_k2v1_kl1_madgraph",
    id=15542732,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=23,
    n_events=502133,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15551044,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=12,
    n_events=498428,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15547902,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=27,
    n_events=498490,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15542136,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=498461,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15553119,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=20,
    n_events=500704,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15554085,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=498400,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15549543,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=14,
    n_events=498404,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15547287,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=17,
    n_events=498420,
)

cpn.add_dataset(
    name="hh_vbf_hww_hzz_4lplus_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15554857,
    processes=[procs.hh_vbf_hww_hzz_4lplus_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2W2ZVetoZto2Nu_4Lplus_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=26,
    n_events=497407,
)
