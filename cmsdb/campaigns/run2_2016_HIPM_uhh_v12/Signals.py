# coding: utf-8

'''
HH -> bbtautau datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2017_nano_uhh_v11 import campaign_run2_2017_nano_uhh_v11 as cpn

#####
# SM 
#####

# ggF -> H -> HH

'''
cpn.add_dataset(
    name="hh_ggf_bbtautau_madgraph",
    id=14333571,
    processes=[procs.hh_ggf_bbtautau],
    keys=[
        "/GluGluToHHTo2B2Tau_TuneCP5_PSWeights_node_SM_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)
'''

################
# BSM scenarios
################

# ggF -> radion -> HH

'''
cpn.add_dataset(
    name="radion_hh_ggf_bbtautau_m250_madgraph",
    id=14302699,
    processes=[procs.radion_hh_ggf_bbtautau_m250],
    keys=[
        "/GluGluToRadionToHHTo2B2Tau_M-250_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv11-106X_mc2017_realistic_v9-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=400000,
)
'''

# ggF -> graviton -> HH


# VBF -> radion -> HH

# VBF -> graviton -> HH

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m900_madgraph",
    id=14309476,
    processes=[procs.graviton_hh_vbf_bbtautau_m900],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-900_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=108000,
)

cpn.add_dataset(
    name="graviton_hh_vbf_bbtautau_m850_madgraph",
    id=14309603,
    processes=[procs.graviton_hh_vbf_bbtautau_m850],
    keys=[
        "/VBFToBulkGravitonToHHTo2B2Tau_M-850_TuneCP5_PSWeights_narrow_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=108000,
)


