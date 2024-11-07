# coding: utf-8

"""
Common, analysis independent definition of the 2016 data-taking campaign (HIPM)
with datasets at NanoAOD tier in version 9.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run2_2016_nano_v9 = Campaign(
    name="run2_HIPM_2016_nano_v9",
    id=2201601, # change ID
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2016,
        "version": 9,
    },
    tags={"preVFP", "APV", "HIPM"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_2016_HIPM_nano_v9.data  # noqa
