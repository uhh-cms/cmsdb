# coding: utf-8

"""
Common, analysis independent definition of the 2018 data-taking campaign
with datasets at NanoAOD tier in version 9.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign, DatasetInfo

import cmsdb.processes as procs


#
# campaign
#

cpn = campaign_run2_2018_nano_v9 = Campaign(
    name="run2_2018_nano_v9",
    id=220181,
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 2,
        "year": 2018,
        "version": 9,
        "postfix": "",
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run2_2018_nano_v9.data  # noqa
import cmsdb.campaigns.run2_2018_nano_v9.qcd  # noqa
import cmsdb.campaigns.run2_2018_nano_v9.top  # noqa

#
# datasets
#

cpn.add_dataset(
    name="data_mu_a",
    id=14046760,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD",
    ],
    n_files=225,
    n_events=241608232,
)
