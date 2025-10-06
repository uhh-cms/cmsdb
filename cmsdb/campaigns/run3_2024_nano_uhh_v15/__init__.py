# coding: utf-8

"""
Common, analysis independent definition of the 2024 data-taking campaign with datasets at NanoAOD tier in version 15,
fetched to local storage via rucio.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2024_nano_uhh_v15 = Campaign(
    name="run3_2024_nano_uhh_v15",
    id=320241150,  # (run)3(year)2024(part)1(version)15(prod)0, 0 -> central nano fetched via rucio
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
            "creator": "rucio",
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2",
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
