# coding: utf-8

"""
Common, analysis independent definition of the 2017 data-taking campaign.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign

#
# campaign
#

campaign_run2_2017 = Campaign(
    name="run2_2017",
    id=220171,
    ecm=13,
    bx=25,
    aux={"year": 2017},
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_2017.data  # noqa
import cmsdb.campaigns.run2_2017.top  # noqa
import cmsdb.campaigns.run2_2017.ewk  # noqa
import cmsdb.campaigns.run2_2017.qcd  # noqa
import cmsdb.campaigns.run2_2017.higgs  # noqa
import cmsdb.campaigns.run2_2017.hh2bbtautau  # noqa
import cmsdb.campaigns.run2_2017.hh2bbww  # noqa
