# coding: utf-8

"""
Recorded datasets for the 2022 preEE data-taking campaign with datasets at NanoAOD tier in
version 12, created with custom content at UHH.
"""

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12 import campaign_run3_2022_postEE_nano_uhh_v12 as cpn  # noqa


#
# Muon
#

# TODO


#
# E/Gamma
#

# TODO


#
# Tau
#

cpn.add_dataset(
    name="data_tau_d",
    id=14783293,
    is_data=True,
    processes=[procs.data_tau],
    keys=[
        "/Tau/Run2022D-22Sep2023_NanoAODv12UHH-v1/NANOAOD",  # noqa
    ],
    n_files=28,
    n_events=16_686_692,
    aux={
        "nominal_merging_factor": 9,
        "era": "D",
    },
)
