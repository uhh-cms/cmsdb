# coding: utf-8

"""
Common, analysis independent definition of the 2022 pre-EE data-taking campaign
with datasets at NanoAOD tier in version 11. The 'pre-EE' refers to data taken
before part of the positive ECAL endcap (EE+) had to be shut down because of a water
leak inside the detector in late 2022 (more details can be found at
https://cms.cern/news/problems-and-solutions-ecal-leak-story).
The corresponding set of MC samples include a simulation of the detector including
the endcap region that was later affected by the leak.

See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those in DAS (https://cmsweb.cern.ch/das).
"""

from order import Campaign


#
# campaign
#

campaign_run3_2022_preEE_nano_v11 = Campaign(
    name="run3_2022_preEE_nano_v11",
    id=320221101,  # 3 2022 11 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2022,
        "version": 11,
        "postfix": "",
    },
    tags={"preEE"},
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_v11.data  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v11.top  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v11.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v11.qcd  # noqa
