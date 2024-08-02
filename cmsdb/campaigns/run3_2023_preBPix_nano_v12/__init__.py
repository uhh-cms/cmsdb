# coding: utf-8

"""

BPix issue:
After Technical Stop 1 from June 19-24, 2023, 27 modules in the Barrel Pixel Layer 3 and 4 became
inoperable due to a problem with the LHC clock distribution. These modules have been turned off
since then. Read more at https://cds.cern.ch/record/2888302/files/DP2024_005.pdf. 


See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

#
# campaign
#

from order import Campaign

campaign_run3_2023_preBPix_nano_v12 = Campaign(
    name="run3_2023_preBPix_nano_v12",
    id=320231201,  # 3 2023 12 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2023,
        "version": 12,
    },
)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.data  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.top  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.ewk  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.qcd  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.hh2bbww  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.hhh4b2tau  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_v12.hh2bbtautau # noqa