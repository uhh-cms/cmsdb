# coding: utf-8

"""
Common, analysis independent definition of the 2025 data-taking campaign with datasets at NanoAOD tier in version 15,
fetched to local storage via rucio.
"""

from order import Campaign

from cmsdb.util import transfer_datasets
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn24


#
# campaign
#

campaign_run3_2025_nano_v15 = cpn24.copy()
campaign_run3_2025_nano_v15.name = "run3_2025_nano_v15"
campaign_run3_2025_nano_v15.id = 32025115  # (run)3(year)2025(part)1(version)15
campaign_run3_2025_nano_v15.set_aux("year", 2025)

# remove 'data_' datasets from the 2024 campaign
for ds in campaign_run3_2025_nano_v15.datasets.names():
    if ds.startswith("data_"):
        campaign_run3_2025_nano_v15.remove_dataset(ds)

# trailing imports to load datasets
import cmsdb.campaigns.run3_2025_nano_v15.data  # noqa


#
# variant of the campaign with datasets fetched to local resources via rucio
# (the main difference is the "custom" aux entry with additional info that can be interpreted by analyses)
#

campaign_run3_2025_nano_local_v15 = Campaign(
    name="run3_2025_nano_local_v15",
    id=10 * campaign_run3_2025_nano_v15.id,  # adds trailing 0
    ecm=campaign_run3_2025_nano_v15.ecm,
    bx=campaign_run3_2025_nano_v15.bx,
    aux={
        **campaign_run3_2025_nano_v15.aux,
        "custom": {
            "name": "run3_2025_nano_local_v15",
            "creator": "rucio",
            "locations": {
                "desy": "davs://dcache-cms-webdav-wan.desy.de:2880/pnfs/desy.de/cms/tier2",
                "cern": "root://eoscms.cern.ch/eos/cms",
            },
        },
    },
    tags=campaign_run3_2025_nano_v15.tags,
)

transfer_datasets(campaign_run3_2025_nano_v15, campaign_run3_2025_nano_local_v15)
