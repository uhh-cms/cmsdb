# coding: utf-8

"""
Custom campaign for Run 3 2022 preEE nanoAOD v14 production.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_uhh_v14_trg_v15 = Campaign(
    name="run3_2022_preEE_nano_uhh_v14_trg_v15",
    id=320221142,  # (run)3(year)2022(part)1(version)14(prod)2
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 14,
        "postfix": "",
        "custom": {
            "name": "run3_2022_preEE_nano_uhh_v14_trg_v15",
            "creator": "uhh",
            "nanogen_version": "prod2",
            "locations": {
                "desy": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/nprouvos/nanogen_store/MergeNano/config_22pre_v14/prod2",  # noqa
            },
        },
    },
    tags={"preEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.data  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.top  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.higgs  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.hh2bbtautau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.hh2bbvv  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.hhh4b2tau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v14_trg_v15.hh2ml  # noqa
