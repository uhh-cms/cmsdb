
# coding: utf-8

"""
Common, analysis independent definition of the run3_2023_postBPix_nano_v12 campaign
with datasets at NanoAOD tier in version 12.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign

#
# campaign
#

campaign_run3_2023_postBPix_nano_v12 = Campaign(
    name="run3_2023_postBPix_nano_v12",
    id=320231202,  # 3 2023 12 02(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2023,
        "version": 12,
        "postfix": "BPix",
    },
    tags={"BPix", "postBPix"},
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.data  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.top  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.ewk  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.qcd  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.higgs  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.hh2bbvv  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.hh2bbtautau  # noqa
import cmsdb.campaigns.run3_2023_postBPix_nano_v12.hhh4b2tau  # noqa
