# coding: utf-8

"""
Common, analysis independent definition of the 2016 data-taking campaign
with datasets at NanoAOD tier in version 12, created with custom content at UHH.
See https://python-order.readthedocs.io/en/latest/quickstart.html#analysis-campaign-and-config.

Dataset ids are identical to those of MiniAOD input datasets in DAS (https://cmsweb.cern.ch/das).

Since this is a custom production, neither can LFNs be obtained through DAS (or dasgloclient), nor
can PFNs be located through the usual, central redirectors.

They are centrally saved at the dCache instance at DESY (e.g. dcache-door-cms04.desy.de) under
/pnfs/desy.de/cms/tier2/store/user/nprouvos/nano_uhh_v12.
"""

from order import Campaign


#
# campaign
#

campaign_run2_2016_nano_uhh_v12 = Campaign(
    name="run2_2016_nano_uhh_v12",
    id=220161221,  # 2 2016 12 21(u)
    ecm=13,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "year": 2016,
        "version": 12,
        "vfp": "post",
        "custom": {
            "name": "run2_2016_nano_uhh_v12",
            "creator": "uhh",
            "location": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2/store/user/nprouvos/nano_uhh_v12/merged_2048.0MB",  # noqa
        },
    },
)


# trailing imports to load datasets
import cmsdb.campaigns.run2_2016_nano_uhh_v12.data  # noqa
import cmsdb.campaigns.run2_2016_nano_uhh_v12.top  # noqa
import cmsdb.campaigns.run2_2016_nano_uhh_v12.ewk  # noqa
import cmsdb.campaigns.run2_2016_nano_uhh_v12.qcd  # noqa
import cmsdb.campaigns.run2_2016_nano_uhh_v12.higgs  # noqa
import cmsdb.campaigns.run2_2016_nano_uhh_v12.hh2bbtautau  # noqa
