# coding: utf-8

"""
Common, analysis independent definition of the 2023 post-BPix data-taking campaign
with datasets at NanoAOD tier in version 13.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2023_postBPix_nano_v13 = Campaign(
    name="run3_2023_postBPix_nano_v13",
    id=320231301,  # 3 2023 13 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2023,
        "version": 13,
        "postfix": "",
    },
    tags={"postBPix"},
)


# trailing imports to load datasets
# import cmsdb.campaigns.run3_2023_postBPix_nano_v13.data  # noqa
# import cmsdb.campaigns.run3_2023_postBPix_nano_v13.top  # noqa
# import cmsdb.campaigns.run3_2023_postBPix_nano_v13.ewk  # noqa
# import cmsdb.campaigns.run3_2023_postBPix_nano_v13.qcd  # noqa
# import cmsdb.campaigns.run3_2023_postBPix_nano_v13.higgs  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v13.hh2bbvv  # noqa
