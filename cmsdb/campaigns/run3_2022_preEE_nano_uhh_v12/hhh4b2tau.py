
import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12 import campaign_run3_2022_preEE_nano_uhh_v12 as cpn

# SM sample
cpn.add_dataset(
    name="hhh_4b2tau_c3_0_d4_0_madgraph",
    id=14791313,
    processes=[procs.hhh_4b2tau_c3_0_d4_0],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=24,
    n_events=9_399_560,
    aux={
        "merging_factors": {
            "nominal": 10,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_0_d4_99_madgraph",
    id=14802797,
    processes=[procs.hhh_4b2tau_c3_0_d4_99],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-99_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=387_652,
    aux={
        "merging_factors": {
            "nominal": 21,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_0_d4_minus1_madgraph",
    id=14796290,
    processes=[procs.hhh_4b2tau_c3_0_d4_minus1],
    keys=[
        "/HHHto4B2Tau_c3-0_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_610,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_19_d4_19_madgraph",
    id=14805828,
    processes=[procs.hhh_4b2tau_c3_19_d4_19],
    keys=[
        "/HHHto4B2Tau_c3-19_d4-19_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=393_190,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_1_d4_0_madgraph",
    id=14805288,
    processes=[procs.hhh_4b2tau_c3_1_d4_0],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=395_878,
    aux={
        "merging_factors": {
            "nominal": 19,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_1_d4_2_madgraph",
    id=14797469,
    processes=[procs.hhh_4b2tau_c3_1_d4_2],
    keys=[
        "/HHHto4B2Tau_c3-1_d4-2_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=407_634,
    aux={
        "merging_factors": {
            "nominal": 22,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_2_d4_minus1_madgraph",
    id=14794613,
    processes=[procs.hhh_4b2tau_c3_2_d4_minus1],
    keys=[
        "/HHHto4B2Tau_c3-2_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=396_595,
    aux={
        "merging_factors": {
            "nominal": 23,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_4_d4_9_madgraph",
    id=14885953,
    processes=[procs.hhh_4b2tau_c3_4_d4_9],
    keys=[
        "/HHHto4B2Tau_c3-4_d4-9_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v3/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=262_292,
    aux={
        "merging_factors": {
            "nominal": 15,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_minus1_d4_0_madgraph",
    id=14795194,
    processes=[procs.hhh_4b2tau_c3_minus1_d4_0],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-0_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=384_245,
    aux={
        "merging_factors": {
            "nominal": 25,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_minus1_d4_minus1_madgraph",
    id=14791288,
    processes=[procs.hhh_4b2tau_c3_minus1_d4_minus1],
    keys=[
        "/HHHto4B2Tau_c3-minus1_d4-minus1_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=398_634,
    aux={
        "merging_factors": {
            "nominal": 20,
        },
    },
)

cpn.add_dataset(
    name="hhh_4b2tau_c3_minus1p5_d4_minus0p5_madgraph",
    id=14792134,
    processes=[procs.hhh_4b2tau_c3_minus1p5_d4_minus0p5],
    keys=[
        "/HHHto4B2Tau_c3-minus1p5_d4-minus0p5_TuneCP5_13p6TeV_amcatnlo-pythia8/Run3Summer22MiniAODv4_NanoAODv12UHH-130X_mcRun3_2022_realistic_v5-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=406_138,
    aux={
        "merging_factors": {
            "nominal": 26,
        },
    },
)
