# coding: utf-8

"""
HH -> bbVV datasets for the 2024 data-taking campaign with datasets at NanoAOD tier in version 15.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn


#
# ggf -> HH
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl0_kt1_powheg",
    id=15437554,
    processes=[procs.hh_ggf_hbb_hvv_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2V_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=274,
    n_events=2_965_710,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl1_kt1_powheg",
    id=15436466,
    processes=[procs.hh_ggf_hbb_hvv_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2V_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=215,
    n_events=2_939_801,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=15537077,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2V_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=222,
    n_events=2_999_715,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl5_kt1_powheg",
    id=15440011,
    processes=[procs.hh_ggf_hbb_hvv_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2V_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=275,
    n_events=2_922_905,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl0_kt1_powheg",
    id=15541102,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=91,
    n_events=1_166_397,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl1_kt1_powheg",
    id=15436982,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=155,
    n_events=1_174_326,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=15432921,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=260,
    n_events=1_172_869,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl5_kt1_powheg",
    id=15436066,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2Vto2L2Nu_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=127,
    n_events=1_166_472,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl0_kt1_powheg",
    id=15546871,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl0_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-0p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=82,
    n_events=1_185_085,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=15542842,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=61,
    n_events=1_199_991,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=15547178,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-2p45-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=65,
    n_events=1_199_990,
)

cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl5_kt1_powheg",
    id=15545302,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl5_kt1],
    keys=[
        "/GluGlutoHHto2B2WtoLNu2Q_Par-c2-0p00-kl-5p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=140,
    n_events=1_191_631,
)

#
# vbf -> HH
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v0_kl1_madgraph",
    id=15548541,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2V_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=77,
    n_events=2_998_988,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v1_kl1_madgraph",
    id=15540098,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2V_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=66,
    n_events=2_948_988,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15539859,
    processes=[procs.hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2V_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=2_995_992,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15551051,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2V_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=86,
    n_events=2_877_982,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15551186,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2V_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=52,
    n_events=2_991_985,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15540857,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2V_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=47,
    n_events=2_987_985,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15546606,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2V_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=85,
    n_events=2_999_993,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15536739,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2V_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=2_999_986,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15541021,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2V_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=63,
    n_events=2_995_986,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15538779,
    processes=[procs.hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2V_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=2_999_985,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1_madgraph",
    id=15534650,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=28,
    n_events=1_199_995,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1_madgraph",
    id=15432384,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=31,
    n_events=1_199_996,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15539885,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1_199_996,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15541590,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=1_199_993,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15436549,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=1_199_997,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15435128,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=1_198_995,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15534643,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=1_199_993,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15468816,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=1_199_997,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15445359,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=1_199_998,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15437989,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2Vto2L2Nu_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=11,
    n_events=1_196_998,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1_madgraph",
    id=15557086,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-1-C2V-0-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=56,
    n_events=1_194_987,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1_madgraph",
    id=15549582,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-1-C2V-1-C3-1_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=59,
    n_events=1_198_992,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=15542760,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-1p74-C2V-1p37-C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=29,
    n_events=1_199_989,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=15542535,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m0p012-C2V-0p030-C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=30,
    n_events=1_197_993,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=15542177,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m0p758-C2V-1p44-C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=25,
    n_events=1_199_993,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=15542253,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m0p962-C2V-0p959-C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1_199_982,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=15549539,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m1p21-C2V-1p94-C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=53,
    n_events=1_199_988,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=15542530,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m1p60-C2V-2p72-C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=1_199_981,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39_madgraph",
    id=15556458,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-m1p83-C2V-3p57-C3-m3p39_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=1_197_988,
)

cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=15546327,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96],
    keys=[
        "/VBFHHto2B2WtoLNu2Q_Par-CV-2p12-C2V-3p87-C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa
    ],
    n_files=48,
    n_events=1_199_990,
)
