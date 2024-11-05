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
    xsecs={13: Number(0.1)},  # TODO
)


#
# QCD (flat sample)
#

qcd_flat = Process(
    name="qcd_flat",
    id=30001,
    label="QCD",
    xsecs={13: Number(0.1)},  # TODO
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
    },
)

qcd_ht2000toinf = qcd.add_process(
    name="qcd_ht2000toinf",
    id=31009,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(22),
    },
)

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
    xsecs={13: Number(0.1)},  # TODO
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
        13.6: Number(2982000.0),
    },
)

qcd_mu_pt20to30 = qcd_mu.add_process(
    name="qcd_mu_pt20to30",
    id=31102,
    xsecs={
        13: Number(2518000.0),
        13.6: Number(2679000.0),
    },
)
qcd_mu_pt30to50 = qcd_mu.add_process(
    name="qcd_mu_pt30to50",
    id=31103,
    xsecs={
        13: Number(1361000.0),
        13.6: Number(1465000.0),
    },
)

qcd_mu_pt50to80 = qcd_mu.add_process(
    name="qcd_mu_pt50to80",
    id=31104,
    xsecs={
        13: Number(377800.0),
        13.6: Number(402900.0),
    },
)

qcd_mu_pt80to120 = qcd_mu.add_process(
    name="qcd_mu_pt80to120",
    id=31105,
    xsecs={
        13: Number(88620.0),
        13.6: Number(95130.0),
    },
)

qcd_mu_pt120to170 = qcd_mu.add_process(
    name="qcd_mu_pt120to170",
    id=31106,
    xsecs={
        13: Number(21070.0),
        13.6: Number(22980.0),
    },
)

qcd_mu_pt170to300 = qcd_mu.add_process(
    name="qcd_mu_pt170to300",
    id=31107,
    xsecs={
        13: Number(7019.0),
        # 13.6: missing in XSDB
    },
)

qcd_mu_pt300to470 = qcd_mu.add_process(
    name="qcd_mu_pt300to470",
    id=31108,
    xsecs={
        13: Number(622.4),
        13.6: Number(699.1),
    },
)

qcd_mu_pt470to600 = qcd_mu.add_process(
    name="qcd_mu_pt470to600",
    id=31109,
    xsecs={
        13: Number(58.86),
        # 13.6: missing in XSDB
    },
)

qcd_mu_pt600to800 = qcd_mu.add_process(
    name="qcd_mu_pt600to800",
    id=31110,
    xsecs={
        13: Number(18.22),
        13.6: Number(21.37),
    },
)

qcd_mu_pt800to1000 = qcd_mu.add_process(
    name="qcd_mu_pt800to1000",
    id=31111,
    xsecs={
        13: Number(3.25),
        13.6: Number(3.913),
    },
)

qcd_mu_pt1000toinf = qcd_mu.add_process(
    name="qcd_mu_pt1000toinf",
    id=31112,
    xsecs={
        13: Number(1.08),  # NOTE: not found via XSDB, taken from an old reference
        # 13.6: missing in XSDB
    },
)

#
# QCD pT-binned (EM enriched)
#

qcd_em = qcd.add_process(
    name="qcd_em",
    id=31200,
    xsecs={13: Number(0.1)},  # TODO
)

# based on datasets QCD_Pt-{i}to{j}_EMEnriched_TuneCP5_13TeV-pythia8 (Run3Summer22EE)
# https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&ordDirection=-1&ordFieldName=energy&pageSize=50&searchQuery=DAS%3DQCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8%20  # noqa
qcd_em_pt10to30 = qcd_em.add_process(
    name="qcd_em_pt10to30",
    id=31201,
    xsecs={
        13.6: Number(6854000.0),
    },
)

qcd_em_pt30to50 = qcd_em.add_process(
    name="qcd_em_pt30to50",
    id=31202,
    xsecs={
        13.6: Number(6686000.0),
    },
)

qcd_em_pt50to80 = qcd_em.add_process(
    name="qcd_em_pt50to80",
    id=31204,
    xsecs={
        13.6: Number(2118000.0),
    },
)

qcd_em_pt80to120 = qcd_em.add_process(
    name="qcd_em_pt80to120",
    id=31205,
    xsecs={
        13.6: Number(409400.0),
    },
)

qcd_em_pt120to170 = qcd_em.add_process(
    name="qcd_em_pt120to170",
    id=31206,
    xsecs={
        13.6: Number(72170.0),
    },
)

qcd_em_pt170to300 = qcd_em.add_process(
    name="qcd_em_pt170to300",
    id=31207,
    xsecs={
        13.6: Number(17920.0),
    },
)

qcd_em_pt300toinf = qcd_em.add_process(
    name="qcd_em_pt300toinf",
    id=31208,
    xsecs={
        13.6: Number(1224.0),
    },
)

#
# QCD pT-binned (bcToE)
#

qcd_bctoe = qcd.add_process(
    name="qcd_bctoe",
    id=31300,
    xsecs={13: Number(0.1)},  # TODO
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
    xsecs={13: Number(0.1)},  # TODO
)

qcd_doubleem_pt30to40_mgg80toinf = qcd_doubleem.add_process(
    name="qcd_doubleem_pt30to40_mgg80toinf",
    id=31401,
    xsecs={
        13: Number(0.1),  # TODO
    },
)

qcd_doubleem_pt40toinf_mgg80toinf = qcd_doubleem.add_process(
    name="qcd_doubleem_pt40toinf_mgg80toinf",
    id=31402,
    xsecs={
        13: Number(0.1),  # TODO
    },
)

qcd_doubleem_pt30toinf_mgg40to80 = qcd_doubleem.add_process(
    name="qcd_doubleem_pt30toinf_mgg40to80",
    id=31403,
    xsecs={
        13: Number(0.1),  # TODO
    },
)
