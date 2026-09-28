# coding: utf-8

"""
Common, analysis independent definition of the 2026 data-taking campaign with datasets at NanoAOD tier in version 15,
fetched to local storage via rucio.
"""

from order import Campaign

from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15
from cmsdb.util import transfer_datasets

#
# campaign
#

campaign_run3_2026_nano_v15 = Campaign(
    name="run3_2026_nano_v15",
    id=32026115,  # (run)3(year)2026(part)1(version)15
    ecm=13.6,
    bx=25,
    aux={
        "tier": "NanoAOD",
        "run": 3,
        "year": 2026,
        "version": 15,
        "postfix": "",
    },
    tags=set(),
)


# trailing imports to load datasets
import cmsdb.campaigns.run3_2026_nano_v15.data  # noqa

# transfer all but data from the 2024 campaign
transfer_datasets(campaign_run3_2024_nano_v15, campaign_run3_2026_nano_v15, skip_fn=lambda d: d.is_data)


#
# variant of the campaign with datasets fetched to local resources via rucio
# (the main difference is the "custom" aux entry with additional info that can be interpreted by analyses)
#

campaign_run3_2026_nano_local_v15 = Campaign(
    name="run3_2026_nano_local_v15",
    id=10 * campaign_run3_2026_nano_v15.id,  # adds trailing 0
    ecm=campaign_run3_2026_nano_v15.ecm,
    bx=campaign_run3_2026_nano_v15.bx,
    aux={
        **campaign_run3_2026_nano_v15.aux,
        "custom": {
            "name": "run3_2026_nano_local_v15",
            "creator": "rucio",
            "locations": {
                "desy": {
                    "site": "T2_DE_DESY",
                    "uri": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2",
                },
                "cern": {
                    "site": "T2_CH_CERN",
                    "uri": "root://eoscms.cern.ch/eos/cms",
                },
            },
        },
    },
    tags=campaign_run3_2026_nano_v15.tags,
)

transfer_datasets(campaign_run3_2026_nano_v15, campaign_run3_2026_nano_local_v15)
