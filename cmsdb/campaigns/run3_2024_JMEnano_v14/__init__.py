# coding: utf-8

"""
Common, analysis independent definition of the 2024 data-taking campaign with datasets at NanoAOD tier in version 15,
fetched to local storage via rucio.
"""

from order import Campaign


#
# campaign
#

campaign_run3_2024_JMEnano_v14 = Campaign(
    name="run3_2024_JMEnano_v14",
    id=320241142,  # (run)3(year)2024(part)1(version)14(JMEnano)2
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2024,
        "version": 14,
        "postfix": "",
    },
    tags=set(),
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2024_JMEnano_v14.data  # noqa
import cmsdb.campaigns.run3_2024_JMEnano_v14.qcd  # noqa
