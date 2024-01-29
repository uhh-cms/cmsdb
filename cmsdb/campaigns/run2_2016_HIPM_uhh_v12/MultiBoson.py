# coding: utf-8

'''
Multi boson datasets from the 2016 data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
'''

import cmsdb.processes as procs
from cmsdb.campaigns.run2_2016_HIPM_uhh_v12 import campaigns.run2_2016_HIPM_uhh_v12 as cpn

cpn.add_dataset(
    name="zzz_amcatnlo",
    id=14213425,
    processes=[procs.zzz],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=81000,
)

cpn.add_dataset(
    name="zzz_ext_amcatnlo",
    id=14215019,
    processes=[procs.zzz_ext],
    keys=[
        "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=5302000,
)

cpn.add_dataset(
    name="ww_pythia",
    id=14214902,
    processes=[procs.ww],
    keys=[
        "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=9,
    n_events=15859000,
)

cpn.add_dataset(
    name="wz_pythia",
    id=14214976,
    processes=[procs.wz],
    keys=[
        "/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=7934000,
)

cpn.add_dataset(
    name="zz_pythia",
    id=14214813,
    processes=[procs.zz],
    keys=[
        "/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files=1,
    n_events=1282000,
)

cpn.add_dataset(
    name="www_amcatnlo",
    id= ### TO FIX ###
    processes=[procs.www],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM",  # noqa
    ],
    n_files= ### TO FIX ###
    n_events= ### TO FIX ###

cpn.add_dataset(
    name="www_ext_amcatnlo",
    id=14215136,
    processes=[procs.www_ext],
    keys=[
        "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=5190000,
)

cpn.add_dataset(
    name="wzz_amcatnlo",
    id=14214901,
    processes=[procs.wzz],
    keys=[
        "/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=5394000,
)

cpn.add_dataset(
    name="wwz_amcatnlo",
    id=14214960,
    processes=[procs.wwz],
    keys=[
        "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM",  # noqa
    ],
    n_files=5,
    n_events=5072000,
)