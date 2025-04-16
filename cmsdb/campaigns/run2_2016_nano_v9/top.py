# coding: utf-8

"""
top quark datasets for the 2016 data-taking campaign
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_v9 import campaign_run2_2016_nano_v9 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14231933,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=146,
            n_events=107067000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=41683000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=48,
            n_events=38870000,

        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=41882000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=88,
            n_events=40796000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt166p5_powheg",
    id=14232002,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=57,
            n_events=39944000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt169p5_powheg",
    id=14235854,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=41386000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt171p5_powheg",
    id=14234936,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=37,
            n_events=42710000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt173p5_powheg",
    id=14341256,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=39493000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt175p5_powheg",
    id=14235163,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=44,
            n_events=40447000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_mt178p5_powheg",
    id=14341801,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=49,
            n_events=40281000,
        ),
    ),
)
