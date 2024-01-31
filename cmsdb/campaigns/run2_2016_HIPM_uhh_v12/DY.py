# coding: utf-8

'''
Drell-Yan datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_uhh_v12 import campaigns.run2_2016_HIPM_uhh_v12 as cpn

cpn.add_dataset(
    name="dy_lep_m50_amcatnlo",
    id=14212297,
    processes=[procs.dy_lep_m50],
    keys=[
        "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=49,
    n_events=90947213,
)

cpn.add_dataset(
    name="dy_lep_0j_amcatnlo",
    id=14212804,
    processes=[procs.dy_lep_0j],
    keys=[
        "/DYJetsToLL_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=41,
    n_events=79751592,
)

cpn.add_dataset(
    name="dy_lep_1j_amcatnlo",
    id=14238480,
    processes=[procs.dy_lep_1j],
    keys=[
        "/DYJetsToLL_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=54,
    n_events=88364975,
)

cpn.add_dataset(
    name="dy_lep_2j_amcatnlo",
    id=14212211,
    processes=[procs.dy_lep_2j],
    keys=[
        "/DYJetsToLL_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=32,
    n_events=42948118,
)

cpn.add_dataset(
    name="dy_lep_pt100To250_amcatnlo",
    id=14342843,
    processes=[procs.dy_lep_pt100To250],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-100To250_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=33,
    n_events=40104234,
)

cpn.add_dataset(
    name="dy_lep_pt250To400_amcatnlo",
    id=14346965,
    processes=[procs.dy_lep_pt250To400],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-250To400_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=13,
    n_events=12085183,
)

cpn.add_dataset(
    name="dy_lep_pt50To100_amcatnlo",
    id=14335914,
    processes=[procs.dy_lep_pt50To100],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-50To100_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=42,
    n_events=60848787,
)

cpn.add_dataset(
    name="dy_lep_pt0To50_amcatnlo",
    id=14339864,
    processes=[procs.dy_lep_pt0To50],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=62,
    n_events=101338633,
)

cpn.add_dataset(
    name="dy_lep_pt650ToInf_amcatnlo",
    id=14349654,
    processes=[procs.dy_lep_pt650ToInf],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-650ToInf_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1999583,
)

cpn.add_dataset(
    name="dy_lep_pt400To650_amcatnlo",
    id=14350490,
    processes=[procs.dy_lep_pt400To650],
    keys=[
        "/DYJetsToLL_LHEFilterPtZ-400To650_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM",  # noqa
    ],
    n_files=3,
    n_events=1993002,
)