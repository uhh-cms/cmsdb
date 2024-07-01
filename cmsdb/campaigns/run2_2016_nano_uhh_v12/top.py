# coding: utf-8

"""
Top quark datasets for the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_nano_uhh_v12 import campaign_run2_2016_nano_uhh_v12 as cpn


#
# ttbar
#

cpn.add_dataset(
    name="tt_sl_powheg",
    id=14212177,
    processes=[procs.tt_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=139,
            n_events=144618000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=56,
            n_events=57993000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=19427000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=60846000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=59,
            n_events=60649000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=62911000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=61,
            n_events=62829000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_dl_powheg",
    id=14212174,
    processes=[procs.tt_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=43538000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=18066000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=18389000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=18874000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=17,
            n_events=18100999,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=18685000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=16,
            n_events=17209000,
        ),
    ),
)

cpn.add_dataset(
    name="tt_fh_powheg",
    id=14212786,
    processes=[procs.tt_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=106,
            n_events=109380000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5up_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=42,
            n_events=41851000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTToHadronic_TuneCP5down_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=38,
            n_events=38870000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=42050000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=41,
            n_events=41728000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop173p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=39,
            n_events=39493000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=43,
            n_events=43046000,
        ),
    ),
)


#
# ttbar + 1 vector boson
#

cpn.add_dataset(
    name="ttz_zlep_m10toinf_amcatnlo",
    id=14213407,
    processes=[procs.ttz_zlep_m10toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM" # noqa
            ],
            n_files=7,
            n_events=6057000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5up_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2570000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTZToLLNuNu_M-10_TuneCP5down_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=3,
            n_events=2480000,
        ),
    ),
)

cpn.add_dataset(
    name="ttw_wlnu_amcatnlo",
    id=14212801,
    processes=[procs.ttw_wlnu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=5,
            n_events=3322643,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5up_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=1367538,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
            ],
            n_files=2,
            n_events=1368511,
        ),
    ),
)

cpn.add_dataset(
    name="ttw_wqq_amcatnlo",
    id=14213083,
    processes=[procs.ttw_wqq],
    keys=[
        "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=308983,
)


#
# ttbar + 2 vector bosons
#

cpn.add_dataset(
    name="ttzz_madgraph",
    id=14212920,
    processes=[procs.ttzz],
    keys=[
        "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=152000,
)

cpn.add_dataset(
    name="ttwz_madgraph",
    id=14212504,
    processes=[procs.ttwz],
    keys=[
        "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=159000,
)

cpn.add_dataset(
    name="ttww_madgraph",
    id=14215222,
    processes=[procs.ttww],
    keys=[
        "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=309000,
)

#
# single top
#

cpn.add_dataset(
    name="st_tchannel_t_5f_powheg",
    id=14211875,
    processes=[procs.st_tchannel_t],
    keys=[
        "/ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=39,
    n_events=55783000,
)

cpn.add_dataset(
    name="st_tchannel_t_4f_powheg",
    id=14223742,
    processes=[procs.st_tchannel_t],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=45,
            n_events=63073000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=25025000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=23751000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=18,
            n_events=24584000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=25401000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=24764000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_top_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=19,
            n_events=24833000,
        ),
    ),
)

cpn.add_dataset(
    name="st_tchannel_tbar_5f_powheg",
    id=14212314,
    processes=[procs.st_tchannel_tbar],
    keys=[
        "/ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
    ],
    n_files=21,
    n_events=29394000,
)

cpn.add_dataset(
    name="st_tchannel_tbar_4f_powheg",
    id=14225640,
    processes=[procs.st_tchannel_tbar],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=23,
            n_events=30609000,
        ),
        tune_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=12523000,
        ),
        tune_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=12042000,
        ),
        hdamp_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=12590000,
        ),
        hdamp_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=11902000,
        ),
        mtop_up=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1735_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=9,
            n_events=12319000,
        ),
        mtop_down=DatasetInfo(
            keys=[
                "/ST_t-channel_antitop_4f_InclusiveDecays_mtop1715_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v3/NANOAODSIM",  # noqa
            ],
            n_files=10,
            n_events=12661000,
        ),
    ),
)

cpn.add_dataset(
    name="st_twchannel_t_powheg",
    id=14238196,
    processes=[procs.st_twchannel_t],
    keys=[
        "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2491000,
)

cpn.add_dataset(
    name="st_twchannel_tbar_powheg",
    id=14238473,
    processes=[procs.st_twchannel_tbar],
    keys=[
        "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv12-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=2554000,
)
