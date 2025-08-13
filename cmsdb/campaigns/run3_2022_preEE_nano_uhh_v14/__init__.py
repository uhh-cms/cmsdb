# coding: utf-8

"""
Custom campaign for Run 3 2022 preEE nanoAOD v14 production.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_uhh_v14 = Campaign(
    name="run3_2022_preEE_nano_uhh_v14",
    id=320221141,  # (run)3(year)2022(part)1(version)14(prod)1
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 14,
        "postfix": "",
        "custom": {
            "name": "run3_2022_preEE_nano_uhh_v14",
            "creator": "uhh",
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/nprouvos/nanogen_store/MergeNano/config_22pre_v14/prod1",  # noqa
            "nanogen_version": "prod1",
        },
    },
    tags={"preEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.data  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.top  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.higgs  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.hh2bbtautau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.hhh4b2tau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14.hh2ml  # noqa
