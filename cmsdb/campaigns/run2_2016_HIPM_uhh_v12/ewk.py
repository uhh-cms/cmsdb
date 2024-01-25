# coding: utf-8

'''
Electroweak datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_uhh_v12 import campaigns.run2_2016_HIPM_uhh_v12 as cpn

cpn.add_dataset(
    name="ewk_wm_lnu_m50_madgraph",
    id=14217420,
    processes=[procs.ewk_wm_lnu_m50],
    keys=[
        "/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2248000,
)

cpn.add_dataset(
    name="ewk_w_lnu_m50_madgraph",
    id=14216470,
    processes=[procs.ewk_wp_lnu_m50],
    keys=[
        "/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=2,
    n_events=2185000,
)

cpn.add_dataset(
    name="ewk_z_ll_m50_madgraph",
    id=14214791,
    processes=[procs.ewk_z_ll_m50],
    keys=[
        "/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=500000,
)
