# coding: utf-8

"""
Common, analysis independent definition of the 2022 pre-EE data-taking campaign
with datasets at NanoAOD tier in version 12, privately created by UHH. The 'pre-EE' refers to data
take before part of the positive ECAL endcap (EE+) had to be shut down because of a water
leak inside the detector in 2022 (https://cms.cern/news/problems-and-solutions-ecal-leak-story).
A corresponding set of MC samples was produced to simulate the effect of the missing
endcap region.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_uhh_v12 = Campaign(
    name="run3_2022_preEE_nano_uhh_v12",
    id=320221203,
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 12,
        "postfix": "",
        "custom": {
            "name": "run3_2022_preEE_nano_uhh_v12",
            "creator": "uhh",
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/nprouvos/nanogen_store/MergeNano/config_22pre_v12/prod3",  # noqa
        },
    },
    tags={"preEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.data  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.top  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.higgs  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.hh2bbtautau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.hhh4b2tau  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_uhh_v12.qcd  # noqa
