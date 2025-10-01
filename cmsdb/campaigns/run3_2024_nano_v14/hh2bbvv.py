# coding: utf-8

"""
HH -> bbWW datasets for the 2022 pre-EE data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn


#
# hh_ggf
#

cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl1_kt1_powheg",
    id=14863914,
    processes=[procs.hh_ggf_hbb_hvv_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=229178,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv_kl2p45_kt1_powheg",
    id=14953184,
    processes=[procs.hh_ggf_hbb_hvv_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2V_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=104,
            n_events=398014,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl1_kt1_powheg",
    id=14847284,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v1/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=86800,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvv2l2nu_kl2p45_kt1_powheg",
    id=14952638,
    processes=[procs.hh_ggf_hbb_hvv2l2nu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2Vto2L2Nu_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=99913,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl1_kt1_powheg",
    id=14868316,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl1_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=31,
            n_events=89899,
        ),
    ),
)
cpn.add_dataset(
    name="hh_ggf_hbb_hvvqqlnu_kl2p45_kt1_powheg",
    id=14953185,
    processes=[procs.hh_ggf_hbb_hvvqqlnu_kl2p45_kt1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/GluGlutoHHto2B2WtoLNu2Q_kl-2p45_kt-1p00_c2-0p00_LHEweights_TuneCP5_13p6TeV_powheg-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=99103,
        ),
    ),
)

#
# hh_vbf
#

cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v1_kl1_madgraph",
    id=14868431,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=28,
            n_events=997227,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1_k2v0_kl1_madgraph",
    id=14861718,
    processes=[procs.hh_vbf_hbb_hvv_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
            ],
            n_files=40,
            n_events=999997,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877532,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=220000,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14877536,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=215824,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14877313,
    processes=[procs.hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=219300,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14879027,
    processes=[procs.hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=217965,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14878523,
    processes=[procs.hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=219289,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14876253,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=217235,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14877935,
    processes=[procs.hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2V_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=219307,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1_madgraph",
    id=14792455,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=20,
            n_events=390211,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1_madgraph",
    id=14795845,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=393727,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14877665,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=399998,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14878661,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=30,
            n_events=399995,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14877853,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=397200,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878771,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=396574,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14876167,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=399999,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14879250,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=397845,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14877649,
    processes=[procs.hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2Vto2L2Nu_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=21,
            n_events=398627,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1_madgraph",
    id=14793960,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_0_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=22,
            n_events=397940,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1_madgraph",
    id=14794554,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=13,
            n_events=392767,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36_madgraph",
    id=14875616,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m1p60_C2V-2p72_C3-m1p36_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=398680,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2_madgraph",
    id=14878911,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m0p012_C2V-0p030_C3-10p2_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=24,
            n_events=393777,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3_madgraph",
    id=14875921,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m0p758_C2V-1p44_C3-m19p3_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=398583,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4_madgraph",
    id=14878677,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-1p74_C2V-1p37_C3-14p4_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=397210,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96_madgraph",
    id=14877670,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m2p12_C2V-3p87_C3-m5p96_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=25,
            n_events=399286,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94_madgraph",
    id=14878772,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m1p21_C2V-1p94_C3-m0p94_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=393851,
        ),
    ),
)
cpn.add_dataset(
    name="hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43_madgraph",
    id=14877655,
    processes=[procs.hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/VBFHHto2B2WtoLNu2Q_CV-m0p962_C2V-0p959_C3-m1p43_TuneCP5_13p6TeV_madgraph-pythia8/Run3Summer22NanoAODv12-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
            ],
            n_files=26,
            n_events=397909,
        ),
    ),
)
