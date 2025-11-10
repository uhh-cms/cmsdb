# coding: utf-8

"""
Common, analysis independent definition of the 2024 pre-BPix data-taking campaign
with datasets at NanoAOD tier in version 14, privately created by UHH.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2023_preBPix_nano_uhh_v14_trg_v15 = Campaign(
    name="run3_2023_preBPix_nano_uhh_v14_trg_v15",
    id=320231142,  # (run)3(year)2023(part)1(version)14(prod)2
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2023,
        "version": 14,
        "postfix": "",
        "custom": {
            "name": "run3_2023_preBPix_nano_uhh_v14_trg_v15",
            "creator": "uhh",
            "nanogen_version": "prod2",
            "locations": {
                "desy": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/bwieders/nanogen_store/MergeNano/config_23pre_v14/prod2",  # noqa
            },
        },
    },
    tags={"preBPix"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15.data  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15.top  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15.ewk  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15.higgs  # noqa
import cmsdb.campaigns.run3_2023_preBPix_nano_uhh_v14_trg_v15.hh2bbtautau  # noqa
