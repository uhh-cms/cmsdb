# coding: utf-8

"""
QCD-related process definitions.
"""

__all__ = [
    "qcd",
    "qcd_flat",
    "qcd_ht50to100",
    "qcd_ht100to200",
    "qcd_ht200to300",
    "qcd_ht300to500",
    "qcd_ht500to700",
    "qcd_ht700to1000",
    "qcd_ht1000to1500",
    "qcd_ht1500to2000",
    "qcd_ht2000toinf",
    # Run 3 datasets (different Ht bins)
    "qcd_ht70to100",
    "qcd_ht200to400",
    "qcd_ht400to600",
    "qcd_ht600to800",
    "qcd_ht800to1000",
    "qcd_ht1000to1200",
    "qcd_ht1200to1500",
    "qcd_pt15to30",
    "qcd_pt30to50",
    "qcd_pt50to80",
    "qcd_pt80to120",
    "qcd_pt120to170",
    "qcd_pt170to300",
    "qcd_pt300to470",
    "qcd_pt470to600",
    "qcd_pt600to800",
    "qcd_pt800to1000",
    "qcd_pt1000to1400",
    "qcd_pt1400to1800",
    "qcd_pt1800to2400",
    "qcd_pt2400to3200",
    "qcd_pt3200toinf",
    "qcd_mu",
    "qcd_mu_pt15to20",
    "qcd_mu_pt20to30",
    "qcd_mu_pt30to50",
    "qcd_mu_pt50to80",
    "qcd_mu_pt80to120",
    "qcd_mu_pt120to170",
    "qcd_mu_pt170to300",
    "qcd_mu_pt300to470",
    "qcd_mu_pt470to600",
    "qcd_mu_pt600to800",
    "qcd_mu_pt800to1000",
    "qcd_mu_pt1000toinf",
    "qcd_em",
    "qcd_em_pt15to20",
    "qcd_em_pt20to30",
    "qcd_em_pt30to50",
    "qcd_em_pt50to80",
    "qcd_em_pt80to120",
    "qcd_em_pt120to170",
    "qcd_em_pt170to300",
    "qcd_em_pt300toinf",
    "qcd_em_pt10to30",
    "qcd_bctoe",
    "qcd_bctoe_pt15to20",
    "qcd_bctoe_pt20to30",
    "qcd_bctoe_pt30to80",
    "qcd_bctoe_pt80to170",
    "qcd_bctoe_pt170to250",
    "qcd_bctoe_pt250toinf",
    "qcd_doubleem",
    "qcd_doubleem_pt30to40_mgg80toinf",
    "qcd_doubleem_pt40toinf_mgg80toinf",
    "qcd_doubleem_pt30toinf_mgg40to80",
]

from order import Process
from scinum import Number


#
# QCD
#

qcd = Process(
    name="qcd",
    id=30000,
    label="QCD",
)


#
# QCD (flat sample)
#

qcd_flat = Process(
    name="qcd_flat",
    id=30001,
    label="QCD",
)


#
# QCD HT-binned
#

qcd_ht50to100 = qcd.add_process(
    name="qcd_ht50to100",
    id=31001,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(185900000),
    },
)

qcd_ht100to200 = qcd.add_process(
    name="qcd_ht100to200",
    id=31002,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(23610000),
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-100to200_TuneCP5_13p6TeV_madgraphMLM-pythia8
        # 13.6: Number(),  # TODO
    },
)

qcd_ht200to300 = qcd.add_process(
    name="qcd_ht200to300",
    id=31003,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(1551000),
    },
)

qcd_ht300to500 = qcd.add_process(
    name="qcd_ht300to500",
    id=31004,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(324300),
    },
)

qcd_ht500to700 = qcd.add_process(
    name="qcd_ht500to700",
    id=31005,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(30340),
    },
)

qcd_ht700to1000 = qcd.add_process(
    name="qcd_ht700to1000",
    id=31006,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(6440),
    },
)

qcd_ht1000to1500 = qcd.add_process(
    name="qcd_ht1000to1500",
    id=31007,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(1118),
    },
)

qcd_ht1500to2000 = qcd.add_process(
    name="qcd_ht1500to2000",
    id=31008,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(108),
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-1500to2000_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(125.2, {"tot": 0.381}),
    },
)

qcd_ht2000toinf = qcd.add_process(
    name="qcd_ht2000toinf",
    id=31009,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(22),
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-2000_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(26.49, {"tot": 0.0807}),
    },
)

#
# QCD HT-binned (Run 3)
#

qcd_ht40to70 = qcd.add_process(
    name="qcd_ht40to70",
    id=31010,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-40to70_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(311400000, {"tot": 843600}),
    },
)

qcd_ht70to100 = qcd.add_process(
    name="qcd_ht70to100",
    id=31011,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-70to100_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(58500000, {"tot": 167400}),
    },
)

# qcd_ht100to200 implemented above

qcd_ht200to400 = qcd.add_process(
    name="qcd_ht200to400",
    id=31012,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-200to400_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(1961000, {"tot": 5862}),
    },
)

qcd_ht400to600 = qcd.add_process(
    name="qcd_ht400to600",
    id=31013,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-400to600_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(95620, {"tot": 289.3}),
    },
)

qcd_ht600to800 = qcd.add_process(
    name="qcd_ht600to800",
    id=31014,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-600to800_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(13540, {"tot": 41.11}),
    },
)

qcd_ht800to1000 = qcd.add_process(
    name="qcd_ht800to1000",
    id=31015,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-800to1000_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(3033, {"tot": 9.206}),
    },
)

qcd_ht1000to1200 = qcd.add_process(
    name="qcd_ht1000to1200",
    id=31016,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-1000to1200_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(883.7, {"tot": 2.69}),
    },
)

qcd_ht1200to1500 = qcd.add_process(
    name="qcd_ht1200to1500",
    id=31017,
    xsecs={
        # https://xsdb-temp.app.cern.ch/?searchQuery=DAS=QCD-4Jets_HT-1200to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8
        13.6: Number(383.5	, {"tot": 1.168	}),
    },
)

# qcd_ht1500to2000 implemented above

# qcd_ht2000 implemented above



#
# QCD pT-binned
#

# 13 TeV cross sections taken from:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2021/015 (v7, p. 11)

qcd_pt15to30 = qcd.add_process(
    name="qcd_pt15to30",
    id=31901,
    xsecs={
        13: Number(1821000000),
    },
)

qcd_pt30to50 = qcd.add_process(
    name="qcd_pt30to50",
    id=31902,
    xsecs={
        13: Number(138800000),
    },
)

qcd_pt50to80 = qcd.add_process(
    name="qcd_pt50to80",
    id=31903,
    xsecs={
        13: Number(19110000),
    },
)

qcd_pt80to120 = qcd.add_process(
    name="qcd_pt80to120",
    id=31904,
    xsecs={
        13: Number(2735000),
    },
)

qcd_pt120to170 = qcd.add_process(
    name="qcd_pt120to170",
    id=31905,
    xsecs={
        13: Number(466200),
    },
)

qcd_pt170to300 = qcd.add_process(
    name="qcd_pt170to300",
    id=31906,
    xsecs={
        13: Number(117200),
    },
)

qcd_pt300to470 = qcd.add_process(
    name="qcd_pt300to470",
    id=31907,
    xsecs={
        13: Number(7763),
    },
)

qcd_pt470to600 = qcd.add_process(
    name="qcd_pt470to600",
    id=31908,
    xsecs={
        13: Number(641),
    },
)

qcd_pt600to800 = qcd.add_process(
    name="qcd_pt600to800",
    id=31909,
    xsecs={
        13: Number(185.7),
    },
)

qcd_pt800to1000 = qcd.add_process(
    name="qcd_pt800to1000",
    id=31910,
    xsecs={
        13: Number(32.02),
    },
)

qcd_pt1000to1400 = qcd.add_process(
    name="qcd_pt1000to1400",
    id=31911,
    xsecs={
        13: Number(9.375),
    },
)

qcd_pt1400to1800 = qcd.add_process(
    name="qcd_pt1400to1800",
    id=31912,
    xsecs={
        13: Number(0.8384),
    },
)

qcd_pt1800to2400 = qcd.add_process(
    name="qcd_pt1800to2400",
    id=31913,
    xsecs={
        13: Number(0.1133),
    },
)

qcd_pt2400to3200 = qcd.add_process(
    name="qcd_pt2400to3200",
    id=31914,
    xsecs={
        13: Number(0.006746),
    },
)

qcd_pt3200toinf = qcd.add_process(
    name="qcd_pt3200toinf",
    id=31915,
    xsecs={
        13: Number(0.0001623),
    },
)

#
# QCD pT-binned (muon enriched)
#

qcd_mu = qcd.add_process(
    name="qcd_mu",
    id=31100,
)

# 13 TeV xsecs based on datasets QCD_Pt-{i}To{j}_MuEnrichedPt5_TuneCP5_13TeV-pythia8 (Summer20UL16)
# https://cms-gen-dev.cern.ch/xsdb/?columns=37814272&currentPage=0&pageSize=10&searchQuery=DAS%3DQCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8  # noqa
# 13.6 TeV xsecs based on datasets QCD_PT-{i}to{j}_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8 (Run3Summer22)
# https://xsdb-temp.app.cern.ch/xsdb/?columns=37814272&currentPage=0&pageSize=10&searchQuery=DAS%3DQCD_PT-15to20_MuEnrichedPt5_TuneCP5_13p6TeV_pythia8  # noqa
qcd_mu_pt15to20 = qcd_mu.add_process(
    name="qcd_mu_pt15to20",
    id=31101,
    xsecs={
        13: Number(2797000.0),
        13.6: Number(2982000.0, {"tot": 29320.0}),
    },
)

qcd_mu_pt20to30 = qcd_mu.add_process(
    name="qcd_mu_pt20to30",
    id=31102,
    xsecs={
        13: Number(2518000.0),
        13.6: Number(2679000.0, {"tot": 26580.0}),
    },
)
qcd_mu_pt30to50 = qcd_mu.add_process(
    name="qcd_mu_pt30to50",
    id=31103,
    xsecs={
        13: Number(1361000.0),
        13.6: Number(1465000.0, {"tot": 14360.0}),
    },
)

qcd_mu_pt50to80 = qcd_mu.add_process(
    name="qcd_mu_pt50to80",
    id=31104,
    xsecs={
        13: Number(377800.0),
        13.6: Number(402900.0, {"tot": 3936.0}),
    },
)

qcd_mu_pt80to120 = qcd_mu.add_process(
    name="qcd_mu_pt80to120",
    id=31105,
    xsecs={
        13: Number(88620.0),
        13.6: Number(95130.0, {"tot": 933.5}),
    },
)

qcd_mu_pt120to170 = qcd_mu.add_process(
    name="qcd_mu_pt120to170",
    id=31106,
    xsecs={
        13: Number(21070.0),
        13.6: Number(22980.0, {"tot": 215.1}),
    },
)

qcd_mu_pt170to300 = qcd_mu.add_process(
    name="qcd_mu_pt170to300",
    id=31107,
    xsecs={
        13: Number(7019.0),
        13.6: Number(7763.0, {"tot": 23.67}),
    },
)

qcd_mu_pt300to470 = qcd_mu.add_process(
    name="qcd_mu_pt300to470",
    id=31108,
    xsecs={
        13: Number(622.4),
        13.6: Number(699.1, {"tot": 6.639}),
    },
)

qcd_mu_pt470to600 = qcd_mu.add_process(
    name="qcd_mu_pt470to600",
    id=31109,
    xsecs={
        13: Number(58.86),
        13.6: Number(68.24, {"tot": 0.2049}),
    },
)

qcd_mu_pt600to800 = qcd_mu.add_process(
    name="qcd_mu_pt600to800",
    id=31110,
    xsecs={
        13: Number(18.22),
        13.6: Number(21.37, {"tot": 0.199}),
    },
)

qcd_mu_pt800to1000 = qcd_mu.add_process(
    name="qcd_mu_pt800to1000",
    id=31111,
    xsecs={
        13: Number(3.25),
        13.6: Number(3.913, {"tot": 0.03526}),
    },
)

qcd_mu_pt1000toinf = qcd_mu.add_process(
    name="qcd_mu_pt1000toinf",
    id=31112,
    xsecs={
        13: Number(1.08),  # NOTE: not found via XSDB, taken from an old reference
        13.6: Number(1.323, {"tot": 0.003921}),
    },
)

#
# QCD pT-binned (EM enriched)
#

qcd_em = qcd.add_process(
    name="qcd_em",
    id=31200,
)

# based on datasets QCD_Pt-{i}to{j}_EMEnriched_TuneCP5_13TeV-pythia8 (Summer20UL16)
# https://cms-gen-dev.cern.ch/xsdb/?columns=37814272&currentPage=0&pageSize=10&searchQuery=DAS%3DQCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8  # noqa
qcd_em_pt15to20 = qcd_em.add_process(
    name="qcd_em_pt15to20",
    id=31201,
    xsecs={
        13: Number(1324000.0),
    },
)

qcd_em_pt20to30 = qcd_em.add_process(
    name="qcd_em_pt20to30",
    id=31202,
    xsecs={
        13: Number(4896000.0),
    },
)
qcd_em_pt30to50 = qcd_em.add_process(
    name="qcd_em_pt30to50",
    id=31203,
    xsecs={
        13: Number(6447000.0),
        13.6: Number(6698000.0, {"tot": 62870.0}),
    },
)

qcd_em_pt50to80 = qcd_em.add_process(
    name="qcd_em_pt50to80",
    id=31204,
    xsecs={
        13: Number(1988000.0),
        13.6: Number(2113000.0, {"tot": 19470.0}),
    },
)

qcd_em_pt80to120 = qcd_em.add_process(
    name="qcd_em_pt80to120",
    id=31205,
    xsecs={
        13: Number(367500.0),
        13.6: Number(409400.0, {"tot": 3771.0}),
    },
)

qcd_em_pt120to170 = qcd_em.add_process(
    name="qcd_em_pt120to170",
    id=31206,
    xsecs={
        13: Number(66590.0),
        13.6: Number(70290.0, {"tot": 625.9}),
    },
)

qcd_em_pt170to300 = qcd_em.add_process(
    name="qcd_em_pt170to300",
    id=31207,
    xsecs={
        13: Number(16620.0),
        13.6: Number(17920.0, {"tot": 164.5}),
    },
)

qcd_em_pt300toinf = qcd_em.add_process(
    name="qcd_em_pt300toinf",
    id=31208,
    xsecs={
        13: Number(1104.0),
        13.6: Number(1231.0, {"tot": 11.28}),
    },
)

qcd_em_pt10to30 = qcd_em.add_process(
    name="qcd_em_pt10to30",
    id=31209,
    xsecs={
        13.6: Number(6854000.0, {"tot": 68270.0}),
    },
)

#
# QCD pT-binned (bcToE)
#

qcd_bctoe = qcd.add_process(
    name="qcd_bctoe",
    id=31300,
)

# based on datasets QCD_Pt_{i}to{j}_bcToE_TuneCP5_13TeV_pythia8 (Autumn18 (pt15to20) or Fall17 (all other))
# https://cms-gen-dev.cern.ch/xsdb/?columns=37814272&currentPage=0&pageSize=10&searchQuery=DAS%3DQCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8
qcd_bctoe_pt15to20 = qcd_bctoe.add_process(
    name="qcd_bctoe_pt15to20",
    id=31301,
    xsecs={
        13: Number(186200.0),
    },
)

qcd_bctoe_pt20to30 = qcd_bctoe.add_process(
    name="qcd_bctoe_pt20to30",
    id=31302,
    xsecs={
        13: Number(303800.0),
    },
)
qcd_bctoe_pt30to80 = qcd_bctoe.add_process(
    name="qcd_bctoe_pt30to80",
    id=31303,
    xsecs={
        13: Number(362300.0),
    },
)

qcd_bctoe_pt80to170 = qcd_bctoe.add_process(
    name="qcd_bctoe_pt80to170",
    id=31304,
    xsecs={
        13: Number(33700.0),
    },
)

qcd_bctoe_pt170to250 = qcd_bctoe.add_process(
    name="qcd_bctoe_pt170to250",
    id=31305,
    xsecs={
        13: Number(2125.0),
    },
)

qcd_bctoe_pt250toinf = qcd_bctoe.add_process(
    name="qcd_bctoe_pt250toinf",
    id=31306,
    xsecs={
        13: Number(562.5),
    },
)

#
# QCD, double em, pt-binned
#

qcd_doubleem = qcd.add_process(
    name="qcd_doubleem",
    id=31400,
)

qcd_doubleem_pt30to40_mgg80toinf = qcd_doubleem.add_process(
    name="qcd_doubleem_pt30to40_mgg80toinf",
    id=31401,
)

qcd_doubleem_pt40toinf_mgg80toinf = qcd_doubleem.add_process(
    name="qcd_doubleem_pt40toinf_mgg80toinf",
    id=31402,
)

qcd_doubleem_pt30toinf_mgg40to80 = qcd_doubleem.add_process(
    name="qcd_doubleem_pt30toinf_mgg40to80",
    id=31403,
)
