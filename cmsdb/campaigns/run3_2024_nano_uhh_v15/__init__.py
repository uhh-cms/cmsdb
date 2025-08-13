# coding: utf-8

"""
Common, analysis independent definition of the 2024 data-taking campaign with datasets at NanoAOD tier in version 15,
privately created by UHH.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2024_nano_uhh_v15 = Campaign(
    name="run3_2024_nano_uhh_v15",
    id=320241151,  # (run)3(year)2024(part)1(version)15(prod)1
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2024,
        "version": 15,
        "postfix": "",
        "custom": {
            "name": "run3_2024_nano_uhh_v15",
            "creator": "uhh",
            # TODO: location still to be decided
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/nprouvos/nanogen_store/MergeNano/config_24_v15/prod1",  # noqa
            "nanogen_version": "prod1",
        },
    },
    tags=set(),
)


# trailing imports to load datasets
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.data  # noqa
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.top  # noqa
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.ewk  # noqa
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.higgs  # noqa
import cmsdb.campaigns.run3_2024_nano_uhh_v15.hh2bbtautau  # noqa
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.hhh4b2tau  # noqa
# import cmsdb.campaigns.run3_2024_nano_uhh_v15.hh2ml  # noqa
