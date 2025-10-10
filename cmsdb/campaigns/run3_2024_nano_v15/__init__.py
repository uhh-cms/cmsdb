
# coding: utf-8

"""
Common, analysis independent definition of the run3_2024_nano_v15 campaign
with datasets at NanoAOD tier in version 15.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign

#
# campaign
#

campaign_run3_2024_nano_v15 = Campaign(
    name="run3_2024_nano_v15",
    id=320241502,
    ecm=13.0,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2024,
        "version": 15,
        "postfix": "TODO",
    },
    tags={"TODO"},
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2024_nano_v15.data  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.top  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.ewk  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.qcd  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.higgs  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.hh2bbvv  # noqa

