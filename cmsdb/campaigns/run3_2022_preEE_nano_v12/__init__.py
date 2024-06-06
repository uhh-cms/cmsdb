# coding: utf-8

"""
Common, analysis independent definition of the 2022 pre-EE data-taking campaign
with datasets at NanoAOD tier in version 12. The 'pre-EE' refers to data taken
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

campaign_run3_2022_preEE_nano_v12 = Campaign(
    name="run3_2022_preEE_nano_v12",
    id=320221201,  # 3 2022 12 01(u)
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2022,
        "version": 12,
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2022_preEE_nano_v12.data  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v12.top  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v12.ewk  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v12.qcd  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v12.hh2bbww  # noqa
import cmsdb.campaigns.run3_2022_preEE_nano_v12.hhh4b2tau  # noqa
