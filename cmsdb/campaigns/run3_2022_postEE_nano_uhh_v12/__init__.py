# coding: utf-8

"""
Common, analysis independent definition of the 2022 post-EE data-taking campaign
with datasets at NanoAOD tier in version 12. The 'post-EE' refers to data taken
after part of the positive ECAL endcap (EE+) had to be shut down because of a water
leak inside the detector in late 2022 (more details can be found at
https://cms.cern/news/problems-and-solutions-ecal-leak-story).
A corresponding set of MC samples was produced to simulate the effect of the missing
endcap region.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_postEE_nano_uhh_v12 = Campaign(
    name="run3_2022_postEE_nano_uhh_v12",
    id=320222121,  # (run)3(year)2022(part)2(version)12(prod)1
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 12,
        "postfix": "EE",
        "custom": {
            "name": "run3_2022_postEE_nano_uhh_v12",
            "creator": "uhh",
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/aalvesan/nanogen_store/MergeNano/config_22post_v12/prod1",  # noqa
        },
    },
    tags={"EE", "postEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12.data  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12.top  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12.ewk  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12.higgs  # noqa
import cmsdb.campaigns.run3_2022_postEE_nano_uhh_v12.hh2bbtautau # noqa
