# coding: utf-8

"""
Common, analysis independent definition of the 2022 post-EE data-taking campaign
with datasets at NanoAOD tier in version 11.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_postEE_nano_v11 = Campaign(
    name="run3_2022_postEE_nano_v11",
    id=320221102,  # 3 2022 11 02(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2022,
        "version": 11,
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_postEE_nano_v11.data  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_v11.top  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_v11.ewk  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_v11.qcd  # noqa
