# coding: utf-8

"""
Common, analysis independent definition of the 2023 pre-BPix data-taking campaign
with datasets at NanoAOD tier in version 12.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2023_preBPix_nano_v12 = Campaign(
    name="run3_2023_preBPix_nano_v12",
    id=320231201,  # 3 2023 12 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2023,
        "version": 12,
        "postfix": "",
    },
    tags={"preBPix"},
)


# trailing imports to load datasets
# import cmsdb.campaigns.run3_2023_preBPix_nano_v12.data  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.top  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.ewk  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.qcd  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.higgs  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.hh2bbvv  # noqa
