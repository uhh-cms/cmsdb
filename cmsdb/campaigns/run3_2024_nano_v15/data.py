# coding: utf-8

"""
CMS datasets from the 2024 data-taking campaign (atill preliminary)
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2022_preEE_nano_v12 import campaign_run3_2022_preEE_nano_v12 as cpn

cpn.add_dataset(
    name="data_mu_b",
    id=14944499,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=69 + 68,
            n_events=4356828 + 4351648,
        ),
        aux={
            "era": "B",
        },
    ),
)

cpn.add_dataset(
    name="data_mu_c",
    id=14950367,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=311 + 311,
            n_events=99560627 + 99546845,
            aux={
                "era": "C",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_d",
    id=14959682,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=327 + 320,
            n_events=122737270 + 122726921,
            aux={
                "era": "D",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_e1",
    id=14965070,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=265 + 264,
            n_events=97002595 + 96996813,
            aux={
                "era": "E",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_e2",
    id=14972652,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
                "/Muon1/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            n_files=176 + 177,
            n_events=79363754 + 79359841,
            aux={
                "era": "E",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_f",
    id=14986475,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=1074 + 1064,
            n_events=446085730 + 446051284,
            aux={
                "era": "F",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_g",
    id=15042671,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=1438 + 1432,
            n_events=647360838 + 647340693,
            aux={
                "era": "G",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_h",
    id=15075248,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=219 + 229,
            n_events=94449581 + 94447297,
            aux={
                "era": "H",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_i1",
    id=15091445,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
                "/Muon1/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=209 + 213,
            n_events=100329358 + 100325747,
            aux={
                "era": "I",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_mu_i2",
    id=15102828,  # id from Muon0 dataset
    processes=[procs.data_mu],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Muon0/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
                "/Muon1/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            n_files=247 + 248,
            n_events=106485742 + 106479336,
            aux={
                "era": "I",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_b",
    id=14944488,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=78 + 83,
            n_events=9709645,
            aux={
                "era": "B",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_c",
    id=14949784,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=410 + 404,
            n_events=162344928 + 162330796,
            aux={
                "era": "C",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_d",
    id=14960439,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=374 + 376,
            n_events=159682409 + 159668543,
            aux={
                "era": "D",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_e1",
    id=14965415,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=317 + 312,
            n_events=139307881 + 139308688,
            aux={
                "era": "E",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_e2",
    id=14972622,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            n_files=212 + 219,
            n_events=117664197 + 117660063,
            aux={
                "era": "E",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_f",
    id=14986997,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=1257 + 1286,
            n_events=638990898 + 638980684,
            aux={
                "era": "F",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_g",
    id=15042761,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=1739 + 1729,
            n_events=914645988 + 913963326,
            aux={
                "era": "G",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_h",
    id=15075278,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=273 + 281,
            n_events=135902643 + 135899057,
            aux={
                "era": "G",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_i1",
    id=15091503,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            n_files=259 + 250,
            n_events=137599442 + 137596331,
            aux={
                "era": "G",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_egamma_i2",
    id=15103445,  # id from EGamma0 dataset
    processes=[procs.data_egamma],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/EGamma0/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
                "/EGamma1/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            n_files=287 + 295,
            n_events=153078631 + 153075941,
            aux={
                "era": "G",
            },
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_b",
    id=14943657,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/002/00000/f59c0e0b-7b74-4490-87e2-9a586ca7faf3.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/168/00000/6af61df1-17fc-43ea-a7f6-9d3ebd4b3f62.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/166/00000/89ef08f7-5725-4985-a117-739f1afe24d2.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/169/00000/73e0c7dd-f4e7-4314-b88a-971a7c3ebc13.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/178/00000/c7b9143a-e0dd-4d77-b4f4-66d8b97e3990.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/163/00000/ab3c79db-f4ec-4ec8-a0a7-64b4cbc1f008.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/160/00000/974e787c-f4a3-4050-b0e1-cee7d8ebaac0.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/146/00000/dc6f8878-74ad-41dc-b438-bd1fef5b1f84.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/170/00000/e6160a2d-d140-4fd4-99c6-d110545e93e0.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/171/00000/76d07a91-f94c-4fc1-a9a3-fa9e4a600bd8.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/237/00000/9f1d2a73-f6c1-438a-bd35-87a850101cef.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/247/00000/9e37b714-e698-43f7-8bce-95253cfa79e2.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/MuonEG/NANOAOD/PromptReco-v1/000/379/337/00000/0d412293-06de-44b0-beda-aba1fdc12360.root",  # empty  # noqa: E501
                ],
                "era": "B",
            },
            n_files=40,  # 53-13
            n_events=771939,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_c",
    id=14950039,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/466/00000/c708aec1-aae5-454d-89e1-6692863ff97c.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/487/00000/5ce49c7f-92a6-433b-9b7b-db88391ccdeb.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/525/00000/a196a63a-5585-4d82-9def-69bf153b4dac.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/619/00000/1fe53fb0-a964-41d2-8dce-bff30f8240e7.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/614/00000/199ac04e-ad8b-4261-803f-df6ce923728d.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/615/00000/8e43bce9-dfdf-41e9-880f-2ee5f716207f.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/379/862/00000/701a1631-ba97-4cbd-a3a6-73fa2f35778c.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/380/031/00000/7e201b65-8d4b-4947-8190-39d94fc31caa.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/380/194/00000/e18b664c-c391-40d1-992d-33520c672f25.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/380/193/00000/747ba74b-e178-4c91-bd21-561baef1f585.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/MuonEG/NANOAOD/PromptReco-v1/000/380/129/00000/f2519b5a-0845-45cc-a007-31f138b03fba.root",  # empty  # noqa: E501
                ],
                "era": "C",
            },
            n_files=87,  # 98-11
            n_events=18475163,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_d",
    id=14959503,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/255/00000/da926229-9a27-47fc-9e1e-019e416ae2ed.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/329/00000/39a04360-d715-4416-a361-bd9902f37dfc.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/442/00000/0a16cf06-90e3-4d98-b8b3-22c81655c875.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/443/00000/9cea2af2-7b34-4037-a2ec-ee47e85c0d87.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/535/00000/21ad2e22-a94c-4494-840f-eb42dc514e59.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/565/00000/474574b3-c519-4061-ac8a-ea332eb87982.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/723/00000/69162b8e-4971-4b3f-b8b0-af5267c45e8b.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/727/00000/64a08fbd-de2b-4ffe-aaa0-4fe590050c25.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/809/00000/640264f1-9515-4ea9-8a23-dca372b500ff.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/812/00000/58345a17-514d-4222-986f-9a702fcdbb4f.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/817/00000/9108f3ba-7359-4acf-b594-2d5d7e4370d6.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/818/00000/3ec1c090-6b39-4568-a943-3cb1ea1f0e86.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/924/00000/7316a388-d18d-4444-88a1-5735d9404f91.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/925/00000/b8695b31-fdd3-4f44-8938-189de8afedb3.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/MuonEG/NANOAOD/PromptReco-v1/000/380/883/00000/1cfbbb39-17ad-4c65-b80c-4c541f77d6c2.root",  # empty  # noqa: E501
                ],
                "era": "D",
            },
            n_files=85,  # 100-15
            n_events=18964349,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_e1",
    id=14964947,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/380/956/00000/601dbaf3-2b8f-497d-a783-533f423ec992.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/012/00000/ff40d7a2-e342-45f9-92d7-09f0ec1e21bf.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/017/00000/cde88d23-91cd-42de-b6ef-41734df6e001.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/189/00000/8aedd7b8-b90e-421c-8cf0-d44c9e4b8a51.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/277/00000/9f974240-5031-41f6-a001-356787988807.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/292/00000/5c97dbda-ee6e-43da-b097-08fc7b9389d3.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/291/00000/26e46654-20f8-44d1-8998-a27540664165.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/290/00000/b182e6dc-9890-44a7-a89b-0c2b8d798b75.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/304/00000/bd4682cd-438b-4601-962d-af52bc932a71.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v1/000/381/294/00000/c16a2342-029a-4046-b90d-d0f84c294071.root",  # empty  # noqa: E501
                ],
                "era": "E",
            },
            n_files=68,  # 78-10
            n_events=14604264,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_e2",
    id=14972628,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v2/000/381/458/00000/8a59b6a5-f4f2-4f2c-96f1-0e8b4086602a.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v2/000/381/465/00000/2527e8ad-2915-4f66-88ec-e1de788c4da2.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/MuonEG/NANOAOD/PromptReco-v2/000/381/542/00000/ae79d13a-637c-4a7a-92b7-f95ed86bc06f.root",  # empty  # noqa: E501
                ],
                "era": "E",
            },
            n_files=38,  # 41-3
            n_events=11724202,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_f",
    id=14986238,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/381/946/00000/d50b437e-f2f4-4395-b300-e8150ec207fc.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/010/00000/92a890e2-8f41-4f69-8849-8bae94ba09db.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/013/00000/9ae30a83-2076-4880-b3f7-38dae569bbfd.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/074/00000/dbce3ec1-4391-43fd-892e-eb5b597da645.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/047/00000/05b3173e-23d1-4410-b3b8-09a1f2ebd09a.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/169/00000/00fce174-ff60-484b-b938-1e288d428ae5.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/054/00000/b311577c-3eb0-4721-aaf2-3648aaf19508.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/159/00000/ac2416e4-439a-447b-93d6-ce88d9722e99.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/171/00000/18e059ac-00c8-4835-b8fb-88d17b062abb.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/070/00000/44940c7b-9619-4ca3-ae0c-626e18b71ddb.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/014/00000/23ecf5cb-3c7d-40c9-8a7b-ecdce9119ee9.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/165/00000/61a4ffe7-bf2b-49be-90e3-855a72d34050.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/160/00000/9e040656-039a-400b-b9c3-0f25e2184953.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/063/00000/6a91cf0e-a9fd-4d00-b63c-424e365d3739.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/064/00000/ba339b76-d1b4-4ab2-ad60-cacd3f0e0d70.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/046/00000/5cdd1cce-4030-4ba2-a363-746914917165.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/075/00000/f3da93e3-e2a2-4cc7-9e38-19913b2b6837.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/036/00000/54059ae4-73b5-40d4-badf-c7f747ab28bd.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/204/00000/a855774f-7760-46c8-ab12-5bc29e176154.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/180/00000/2d96eb5f-9f00-4181-8b23-b60123e36bbf.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/192/00000/f689a989-937b-44ea-91e3-ddec6d9f5d0e.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/260/00000/a346afd8-1f17-4b65-b344-21e32f8dbedd.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/261/00000/50d0fb8b-7495-418e-85ea-362d0013bae3.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/251/00000/96ede0f0-3eef-40c2-83fa-7723c28e903d.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/470/00000/b3858183-38d6-43d0-a75e-29b1343dc8fb.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/393/00000/737fbfcf-ed7e-450b-a237-74e83af34196.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/382/593/00000/c37fa026-f31c-47a1-a2af-62d5f04170c0.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/033/00000/f832a4e8-4cc8-461c-97d3-e98dff5e4319.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/322/00000/83da99c5-e067-4f4e-9427-b537a4de715e.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/333/00000/05661085-d5d3-4d69-ae7a-7c10688aece7.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/327/00000/e5d2b1c6-5f18-4c90-8b46-b36f1ab665c5.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/362/00000/6526df1c-57ad-4124-aa34-1ecbce847fbf.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/MuonEG/NANOAOD/PromptReco-v1/000/383/628/00000/ced9ae4b-9d18-472d-89c2-c5d7026c12ec.root",  # empty  # noqa: E501
                ],
                "era": "F",
            },
            n_files=275,  # 308-33
            n_events=67410940,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_g",
    id=15042067,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/113/00000/e0d7ca23-fb41-4ff6-81a2-ab2bc1713a06.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/276/00000/269f560c-8d74-46dd-a822-8dcccbfa9dfa.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/277/00000/6910f570-4bcd-49a9-bdfa-08fcce97fa51.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/289/00000/4fb673ce-9c05-4961-b970-021782550fef.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/272/00000/7e561672-03d3-4efc-bb77-79d2e9d6d855.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/654/00000/4c77f942-c430-42af-96a5-895fe2475c59.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/660/00000/d12d53fe-959d-4466-89e4-914a50b59782.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/753/00000/9e31b8fc-9316-4ff3-b654-36f39bf9ac4e.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/858/00000/1aa12fb2-ca3b-49a7-a600-19741fc094ed.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/815/00000/eb1429ad-9ac9-4e82-8873-f76967b15e99.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/384/935/00000/338f388a-c3d8-4dca-bc49-996fa50b7417.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/385/344/00000/3568d30a-fc8f-4ebb-a65d-28404f9b75ab.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/385/384/00000/cce1c975-d9da-4a5f-b19b-26adcf99740a.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/385/532/00000/fd448cec-da20-4253-b457-3579bc628aaa.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/385/554/00000/8860b59c-2232-4638-8575-40260a79e74e.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/MuonEG/NANOAOD/PromptReco-v1/000/385/739/00000/d6884db5-09dc-4be2-85ea-817e492545ba.root",  # empty  # noqa: E501
                ],
                "era": "G",
            },
            n_files=370,  # 386-16
            n_events=98051356,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_h",
    id=15074996,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024H/MuonEG/NANOAOD/PromptReco-v1/000/385/976/00000/ea8d77db-680e-47b6-a3ae-2e4dd01e0167.root",  # empty  # noqa: E501
                    "/store/data/Run2024H/MuonEG/NANOAOD/PromptReco-v1/000/386/119/00000/b9c7421d-c1ca-4a3d-b612-ddf267a6e466.root",  # empty  # noqa: E501
                    "/store/data/Run2024H/MuonEG/NANOAOD/PromptReco-v1/000/386/323/00000/c82274db-a7a1-4f2a-8613-37fa27323c28.root",  # empty  # noqa: E501
                ],
                "era": "H",
            },
            n_files=58,  # 61-3
            n_events=14329916,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_i1",
    id=15091494,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024I/MuonEG/NANOAOD/PromptReco-v1/000/386/446/00000/6bcbc36f-33a5-4378-b2a8-b737187448b7.root",  # empty  # noqa: E501
                    "/store/data/Run2024I/MuonEG/NANOAOD/PromptReco-v1/000/386/477/00000/aa0db52e-e790-498b-9e95-0a1ae5b9c0a2.root",  # empty  # noqa: E501
                    "/store/data/Run2024I/MuonEG/NANOAOD/PromptReco-v1/000/386/543/00000/3cbeeab4-608b-4394-bd21-9ea6cc2e53f5.root",  # empty  # noqa: E501
                ],
                "era": "I",
            },
            n_files=59,  # 62-3
            n_events=14794396,
        ),
    ),
)

cpn.add_dataset(
    name="data_muoneg_i2",
    id=15102845,
    processes=[procs.data_muoneg],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/MuonEG/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024I/MuonEG/NANOAOD/PromptReco-v2/000/386/908/00000/5a2d108e-8471-4e68-9dfa-4d004e1e2320.root",  # empty  # noqa: E501
                    "/store/data/Run2024I/MuonEG/NANOAOD/PromptReco-v2/000/386/974/00000/02801b67-dd1d-4dea-abaf-918d0ad5ff1a.root",  # empty  # noqa: E501
                ],
                "era": "I",
            },
            n_files=56,  # 58-2
            n_events=14753953,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_b",
    id=14943817,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/160/00000/0bd67af7-30ba-4f9a-b586-dbbe1c69ee1c.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/163/00000/b6023e4d-7469-47c9-94e0-574ff15a72a7.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/169/00000/467bc30f-2b6b-417e-ba26-69db4af741c0.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/166/00000/8b61af8f-a509-41ef-8dac-0baee65fbe8a.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/170/00000/7a07a3b5-77d5-40b3-8740-1c6e0e261d0d.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/168/00000/8a1f3c1d-9577-4d58-b19e-c07e386a5f0d.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/171/00000/fbd003a8-4968-41b9-9499-0eb93ac6465a.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/178/00000/f00d66fe-089e-4e6f-8d87-1a30e32e5031.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/247/00000/8ec4f999-a3f4-41cc-9f0a-ea752de69346.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/237/00000/246c30e6-05cb-4c99-820e-c96a9767ce3b.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/337/00000/21f59062-f181-4871-adfd-59607545eea4.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/356/00000/84ccf24d-dfad-4e00-88f8-b5b115e4fec1.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/357/00000/456cf482-4b7e-40df-98d8-a66072c9aed8.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/367/00000/d14d472a-ed6d-4c37-8756-5c9753b99bc1.root",  # empty  # noqa: E501
                    "/store/data/Run2024B/Tau/NANOAOD/PromptReco-v1/000/379/391/00000/9a742a2b-7247-411c-aaab-46d7a2f80608.root",  # empty  # noqa: E501
                ],
                "era": "B",
            },
            n_files=38,  # 53-15
            n_events=1336155,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_c",
    id=14950130,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/379/466/00000/87ff48b9-ff6f-4784-a023-a52ab621b042.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/379/487/00000/27214e28-ff06-424d-95cf-7fe504e7bb87.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/379/619/00000/2205daba-53ff-4227-9c2e-230623bac2de.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/379/862/00000/37d9ff8e-e6f3-4358-b948-38727c46ff24.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/380/129/00000/1717da76-ccd6-4e1f-9348-4893fb73c24e.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/380/193/00000/448ecdd2-8da4-4d42-9cd8-8423fd8e53c7.root",  # empty  # noqa: E501
                    "/store/data/Run2024C/Tau/NANOAOD/PromptReco-v1/000/380/194/00000/44440872-ac94-4852-a998-c27b3da34605.root",  # empty  # noqa: E501
                ],
                "era": "C",
            },
            n_files=184,  # 191-7
            n_events=51206850,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_d",
    id=14959635,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/255/00000/dcc3de8c-db50-4f20-9a45-6de343e39650.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/329/00000/16ea1aae-70fc-42d3-b4bc-e5eaa63fb942.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/442/00000/dc908f5a-564f-431e-a643-25667610c80c.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/443/00000/daae15bb-025b-4cb6-bf09-745a725a93c4.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/809/00000/2dac325b-9cf3-454c-9c30-fe61510c6cf5.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/723/00000/13e40979-c9b8-4a87-8e34-467f0aec26b8.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/727/00000/606871fe-959f-4337-80bf-995b60860a9b.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/812/00000/4d7c6da0-8257-4c3e-9645-c879ed9a6b3a.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/817/00000/35b2bb10-4ec2-44e3-87a0-4bc8884372ef.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/818/00000/f93a2859-948c-4621-a1e6-344863060dbf.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/925/00000/63498683-a9ea-4cce-bc6d-584234c62b3a.root",  # empty  # noqa: E501
                    "/store/data/Run2024D/Tau/NANOAOD/PromptReco-v1/000/380/924/00000/2f58288d-ac2d-4523-b405-9578af38bc95.root",  # empty  # noqa: E501
                ],
                "era": "D",
            },
            n_files=204,  # 216-12
            n_events=59126000,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_e1",
    id=14964934,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/380/956/00000/f2b6f26e-7b16-4b6e-ac90-23b376f5c996.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/017/00000/dc163516-f95d-4f7b-8451-3a206e18eed6.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/012/00000/53868b80-676e-493f-b737-88e52d6f4f40.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/189/00000/ebb3591a-629b-4085-a535-0ce0d1d3f2fd.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/304/00000/8b05a0e1-c5c0-445e-8548-ed580c1e7497.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/294/00000/34ac0d20-b035-48ce-ba8b-764eb3c02096.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v1/000/381/291/00000/668bd40f-b5d7-4056-843a-3c5a55e0caa0.root",  # empty  # noqa: E501
                ],
                "era": "E",
            },
            n_files=163,  # 170-7
            n_events=47650900,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_e2",
    id=14973897,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v2/000/381/465/00000/9cde4cd4-d94b-4f73-987e-7ec6e54ef796.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v2/000/381/458/00000/79efee33-a906-4016-bcf1-8803ab662695.root",  # empty  # noqa: E501
                    "/store/data/Run2024E/Tau/NANOAOD/PromptReco-v2/000/381/542/00000/6cba0fee-0b49-4221-8ce3-90bb992cd43f.root",  # empty  # noqa: E501
                ],
                "era": "E",
            },
            n_files=109,  # 112-3
            n_events=37800903,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_f",
    id=14986260,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/010/00000/d9052ba7-a898-47b5-9117-eec9d7d800d4.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/013/00000/fc7abfce-0c96-4b34-b586-9f26f02f7ee2.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/047/00000/dbc88e78-fecf-4d11-b4d4-3638630077bd.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/046/00000/53e2e29e-51da-4c12-94d4-09c1655ff20e.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/165/00000/89b448b7-82a4-4b2f-84eb-333310bd2a45.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/169/00000/041c0cfa-ae89-4076-bfba-756f2e29d1b1.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/159/00000/bb908745-fcf4-4e84-a7c9-7f999022e9b3.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/054/00000/a1921872-dcde-471b-9e08-abeeb9abe1de.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/014/00000/53948765-5878-4b60-a491-7a7d49ae2589.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/160/00000/36538052-89fc-4ce2-97b5-a84601ba302d.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/070/00000/97b855b6-35bd-4bc2-819b-be139d7d10b7.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/074/00000/b66a1704-fc35-46f2-804e-0a5dc5cf6301.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/075/00000/3039d922-c66b-4992-bd68-75a97576ba7f.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/171/00000/1b4a6408-12eb-4ee6-bc74-f2dac5c04df8.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/036/00000/01f26745-5cc7-42ac-95d8-c39d3ab0b6e1.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/064/00000/5ce7a2d1-1cd4-423e-9b93-5a38cb5930fd.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/063/00000/6b093bd3-cb76-43e6-a775-4b0a67f15286.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/192/00000/2fa0260e-b240-4e1c-9409-177cfeb917c6.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/180/00000/5874e090-bf02-464c-b123-03e3b8c68322.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/204/00000/138c41cc-c9d6-46e1-867d-5498819d267a.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/251/00000/ca326f91-edd8-4966-82c0-7be31f1ab8d1.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/261/00000/239627cd-e084-485d-bc1b-6dfb530c0175.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/393/00000/74bf9a7e-7a80-4460-afe4-dbcd0cce345f.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/470/00000/d2c7aa67-5545-4b65-8a84-675258d8eab9.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/593/00000/830506b3-22c9-4513-bb63-95029e824d6f.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/382/923/00000/19c9f3f8-197a-428f-9944-bfab0f3f2e25.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/383/033/00000/b529682b-e7bc-4640-a2fa-ea7250921146.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/383/322/00000/b349eb2b-18f1-4172-a720-28d9fcf5a930.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/383/362/00000/b7bc7267-21df-49f2-9113-3f69c593d760.root",  # empty  # noqa: E501
                    "/store/data/Run2024F/Tau/NANOAOD/PromptReco-v1/000/383/628/00000/6d027554-78a8-49d2-85e3-ac6156131a76.root",  # empty  # noqa: E501
                ],
                "era": "F",
            },
            n_files=729,  # 759-30
            n_events=234185907,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_g",
    id=15042117,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/276/00000/cdcfadf6-f35a-4eb3-ae70-392c712edf82.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/277/00000/8f127e0e-b42f-48a6-9947-d6cacc30055e.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/289/00000/316daabf-5891-4729-86b2-b71783855f77.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/272/00000/ded7ba3a-ae08-4a11-b391-7fbc8c0d69bc.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/654/00000/d8efe28d-dec5-4f34-8446-d2ab01dcb55a.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/660/00000/35ed1989-b2bc-4e7a-81d6-eee47b97c9fd.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/753/00000/166691d8-90e5-48ff-b6b2-d04d9ea749bf.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/815/00000/6954a35d-945b-45ce-9aad-55c3c1c200ec.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/384/858/00000/d61c906c-e9b1-4c64-98e2-05afefd53cad.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/385/344/00000/8cd95f4a-cb46-4a85-a5e5-d8b19c86e3f4.root",  # empty  # noqa: E501
                    "/store/data/Run2024G/Tau/NANOAOD/PromptReco-v1/000/385/554/00000/e085467e-470e-44d6-9da0-d8c08e6e3eed.root",  # empty  # noqa: E501
                ],
                "era": "G",
            },
            n_files=1035,  # 1046-11
            n_events=328373676,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_h",
    id=15075078,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024H/Tau/NANOAOD/PromptReco-v1/000/385/976/00000/05e4f449-9f56-4923-b6b8-238d204d663d.root",  # empty  # noqa: E501
                    "/store/data/Run2024H/Tau/NANOAOD/PromptReco-v1/000/386/323/00000/6715e927-925a-4607-9776-dcf494bef059.root",  # empty  # noqa: E501
                ],
                "era": "H",
            },
            n_files=165,  # 167-2
            n_events=49168606,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_i1",
    id=15091434,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024I/Tau/NANOAOD/PromptReco-v1/000/386/477/00000/7198aa5e-83ad-46ac-b62d-d71e56bb460a.root",  # empty  # noqa: E501
                    "/store/data/Run2024I/Tau/NANOAOD/PromptReco-v1/000/386/543/00000/9a2a10a5-0986-4305-afff-03941487c515.root",  # empty  # noqa: E501
                ],
                "era": "I",
            },
            n_files=150,  # 152-2
            n_events=47950221,
        ),
    ),
)

cpn.add_dataset(
    name="data_tau_i2",
    id=15102391,
    processes=[procs.data_tau],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/Tau/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "broken_files": [
                    "/store/data/Run2024I/Tau/NANOAOD/PromptReco-v2/000/386/908/00000/3fab6b44-a217-4dc2-911a-414863c88802.root",  # empty  # noqa: E501
                    "/store/data/Run2024I/Tau/NANOAOD/PromptReco-v2/000/386/974/00000/d0a3be83-2f85-4ecc-a3b4-b7902fcd8faa.root",  # empty  # noqa: E501
                ],
                "era": "I",
            },
            n_files=160,  # 162-2
            n_events=47637180,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_b",
    id=14944569,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024B-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "B",
            },
            n_files=72 + 71,
            n_events=8646489 + 8637923,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_c",
    id=14949695,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024C-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "C",
            },
            n_files=264 + 259,
            n_events=71253034 + 71237941,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_d",
    id=14959521,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024D-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "D",
            },
            n_files=266 + 263,
            n_events=77429100 + 77411277,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_e1",
    id=14965363,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024E-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "E",
            },
            n_files=232 + 231,
            n_events=69338632 + 69326400,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_e2",
    id=14973267,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024E-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "E",
            },
            n_files=150 + 145,
            n_events=57056487 + 57052071,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_f",
    id=14986313,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024F-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "F",
            },
            n_files=942 + 957,
            n_events=312020081 + 311961806,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_g",
    id=15042681,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024G-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "G",
            },
            n_files=1193 + 1187,
            n_events=401282045 + 401204775,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_h",
    id=15075256,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024H-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "H",
            },
            n_files=186 + 189,
            n_events=56068074 + 56056824,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_i1",
    id=15090029,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-PromptReco-v1/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "I",
            },
            n_files=178 + 174,
            n_events=60800805 + 60787485,
        ),
    ),
)

cpn.add_dataset(
    name="data_met_i2",
    id=15102368,  # id from JetMET0 dataset
    processes=[procs.data_met],
    is_data=True,
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/JetMET0/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
                "/JetMET1/Run2024I-PromptReco-v2/NANOAOD",  # noqa: E501
            ],
            aux={
                "era": "I",
            },
            n_files=238 + 240,
            n_events=116871063 + 116855237,
        ),
    ),
)
