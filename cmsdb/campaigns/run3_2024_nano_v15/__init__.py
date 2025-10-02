# coding: utf-8

"""
Common, analysis independent definition of the 2024 data-taking campaign
with datasets at NanoAOD tier in version 14.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2024_nano_v14 = Campaign(
    name="run3_2024_nano_v14",
    id=320241401,  # 3 2024 14 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2024,
        "version": 15,
        "postfix": "",
    },
    tags={},
)


# trailing imports to load datasets
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.data  # noqa
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.top  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.ewk  # noqa
import cmsdb.campaigns.run3_2024_nano_v15.qcd  # noqa
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.higgs  # noqa
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.hh2bbtautau  # noqa
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.hh2bbvv  # noqa
# import cmsdb.campaigns.run3_2022_preEE_nano_v12.hhh4b2tau  # noqa
