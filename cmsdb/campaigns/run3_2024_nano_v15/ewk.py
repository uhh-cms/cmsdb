
# coding: utf-8

""""
Electroweak datasets for the run3_2024_nano_v15 campaign.
"""

from order import DatasetInfo

import cmsdb.processes as procs
from cmsdb.campaigns.run3_2024_nano_v15 import campaign_run3_2024_nano_v15 as cpn

#
# DY (NLO)
#

# m_ll > 50, binned in pt_ll, 1 additional jet

cpn.add_dataset(
    name="dy_m50toinf_1j_pt40to100_amcatnlo",
    id=15300236,
    processes=[procs.dy_m50toinf_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3045,  # 3045-0
            n_events=479655476,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt100to200_amcatnlo",
    id=15304428,
    processes=[procs.dy_m50toinf_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=355,  # 355-0
            n_events=227319605,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt200to400_amcatnlo",
    id=15304451,
    processes=[procs.dy_m50toinf_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=54,  # 54-0
            n_events=22383959,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt400to600_amcatnlo",
    id=15304493,
    processes=[procs.dy_m50toinf_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=58,  # 58-0
            n_events=10404540,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_1j_pt600toinf_amcatnlo",
    id=15304449,
    processes=[procs.dy_m50toinf_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=42,  # 42-0
            n_events=9996457,
        ),
    ),
)

# m_ll > 50, binned in pt_ll, 2 additional jets

cpn.add_dataset(
    name="dy_m50toinf_pt40to100_amcatnlo",
    id=15300484,
    processes=[procs.dy_m50toinf_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1787,  # 1787-0
            n_events=247167836,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50inf_pt100to200_amcatnlo",
    id=15296152,
    processes=[procs.dy_m50inf_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=389,  # 389-0
            n_events=246696940,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_pt200to400_amcatnlo",
    id=15304466,
    processes=[procs.dy_m50toinf_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=139,  # 139-0
            n_events=44028174,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_pt400to600_amcatnlo",
    id=15304446,
    processes=[procs.dy_m50toinf_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=47,  # 47-0
            n_events=9893470,
        ),
    ),
)

cpn.add_dataset(
    name="dy_m50toinf_pt600toinf_amcatnlo",
    id=15304548,
    processes=[procs.dy_m50toinf_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=50,  # 50-0
            n_events=9801431,
        ),
    ),
)

#
# w_lnu (NLO?)
#

# binned in pt_lnu, 1 additional jet

cpn.add_dataset(
    name="w_lnu_1j_pt40to100_amcatnlo",
    id=15297303,
    processes=[procs.w_lnu_1j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3384,  # 3384-0
            n_events=447467775,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt100to200_amcatnlo",
    id=15300033,
    processes=[procs.w_lnu_1j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3089,  # 3089-0
            n_events=494167270,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt200to400_amcatnlo",
    id=15304490,
    processes=[procs.w_lnu_1j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=109,  # 109-0
            n_events=45096548,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt400to600_amcatnlo",
    id=15304489,
    processes=[procs.w_lnu_1j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=62,  # 62-0
            n_events=14159808,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_1j_pt600toinf_amcatnlo",
    id=15304609,
    processes=[procs.w_lnu_1j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=27,  # 27-0
            n_events=15305397,
        ),
    ),
)

# binned in pt_lnu, 2 additional jets

cpn.add_dataset(
    name="w_lnu_2j_pt40to100_amcatnlo",
    id=15300032,
    processes=[procs.w_lnu_2j_pt40to100],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3309,  # 3309-0
            n_events=483030994,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt100to200_amcatnlo",
    id=15299994,
    processes=[procs.w_lnu_2j_pt100to200],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=3262,  # 3262-0
            n_events=470520533,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt200to400_amcatnlo",
    id=15304499,
    processes=[procs.w_lnu_2j_pt200to400],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=136,  # 136-0
            n_events=75124628,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt400to600_amcatnlo",
    id=15304459,
    processes=[procs.w_lnu_2j_pt400to600],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=51,  # 51-0
            n_events=14222725,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_pt600toinf_amcatnlo",
    id=15304506,
    processes=[procs.w_lnu_2j_pt600toinf],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=67,  # 67-0
            n_events=14991109,
        ),
    ),
)

# binned in jet multiplicity (LO?)

cpn.add_dataset(
    name="w_lnu_1j_madgraph",
    id=15316677,
    processes=[procs.w_lnu_1j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=2491,  # 2491-0
            n_events=429800607,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_2j_madgraph",
    id=15298612,
    processes=[procs.w_lnu_2j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=1632,  # 1632-0
            n_events=286526689,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_3j_madgraph",
    id=15298945,
    processes=[procs.w_lnu_3j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=915,  # 915-0
            n_events=139773986,
        ),
    ),
)

cpn.add_dataset(
    name="w_lnu_4j_madgraph",
    id=15298088,
    processes=[procs.w_lnu_4j],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=644,  # 644-0
            n_events=85950957,
        ),
    ),
)

#
# diboson
#

cpn.add_dataset(
    name="ww_pythia",
    id=15315231,
    processes=[procs.ww],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WW_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=518,  # 518-0
            n_events=63986968,
        ),
    ),
)

cpn.add_dataset(
    name="zz_pythia",
    id=15315163,
    processes=[procs.zz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=76,  # 76-0
            n_events=4800000,
        ),
    ),
)

cpn.add_dataset(
    name="wz_pythia",
    id=15315210,
    processes=[procs.wz],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=307,  # 307-0
            n_events=30547825,
        ),
    ),
)

cpn.add_dataset(
    name="ww_dl_powheg",
    id=15304453,
    processes=[procs.ww_dl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=278,  # 278-0
            n_events=239943886,
        ),
    ),
)

cpn.add_dataset(
    name="ww_fh_powheg",
    id=15304426,
    processes=[procs.ww_fh],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=185,  # 185-0
            n_events=151214029,
        ),
    ),
)

cpn.add_dataset(
    name="ww_sl_powheg",
    id=15296280,
    processes=[procs.ww_sl],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=326,  # 326-0
            n_events=275723961,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zll_znunu_powheg",
    id=15304432,
    processes=[procs.zz_zll_znunu],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=228,  # 228-0
            n_events=188715312,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zqq_zll_powheg",
    id=15304456,
    processes=[procs.zz_zqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=215,  # 215-0
            n_events=171627615,
        ),
    ),
)

cpn.add_dataset(
    name="zz_znunu_zqq_powheg",
    id=15304447,
    processes=[procs.zz_znunu_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=65,  # 65-0
            n_events=46047410,
        ),
    ),
)

cpn.add_dataset(
    name="zz_zll_zll_powheg",
    id=15297464,
    processes=[procs.zz_zll_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=273,  # 273-0
            n_events=236757511,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wqq_zll_powheg",
    id=15300434,
    processes=[procs.wz_wqq_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=257,  # 257-0
            n_events=236049432,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wlnu_zll_powheg",
    id=15304502,
    processes=[procs.wz_wlnu_zll],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=296,  # 296-0
            n_events=248149069,
        ),
    ),
)

cpn.add_dataset(
    name="wz_wlnu_zqq_powheg",
    id=15304500,
    processes=[procs.wz_wlnu_zqq],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM",  # noqa: E501
            ],
            aux={
                "broken_files": [],
            },
            n_files=156,  # 156-0
            n_events=143874689,
        ),
    ),
)

