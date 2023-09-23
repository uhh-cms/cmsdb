import cmsdb.processes as procs
from cmsdb.campaigns.run2_2018_nano_v9 import campaign_run2_2018_nano_v9 as cpn

cpn.add_dataset(
    name="data_mu_a",
    id=14046760,
    is_data=True,
    processes=[procs.data_mu],
    keys=[
        "/SingleMuon/Run2018A-02Apr2020-v1/NANOAOD",
    ],
    n_files=225,
    n_events=241608232,
)
