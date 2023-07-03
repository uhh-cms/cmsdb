# coding: utf-8

"""
QCD-related process definitions.
"""

__all__ = [
    "qcd",
    "qcd_ht50to100", "qcd_ht100to200", "qcd_ht200to300", "qcd_ht300to500", "qcd_ht500to700",
    "qcd_ht700to1000", "qcd_ht1000to1500", "qcd_ht1500to2000", "qcd_ht2000",
    "qcd_mu", "qcd_em", "qcd_bctoe",
    "qcd_mu_pt15to20", "qcd_mu_pt20to30", "qcd_mu_pt30to50", "qcd_mu_pt50to80",
    "qcd_mu_pt80to120", "qcd_mu_pt120to170", "qcd_mu_pt170to300", "qcd_mu_pt300to470",
    "qcd_mu_pt470to600", "qcd_mu_pt600to800", "qcd_mu_pt800to1000", "qcd_mu_pt1000",
    "qcd_em_pt15to20", "qcd_em_pt20to30", "qcd_em_pt30to50", "qcd_em_pt50to80",
    "qcd_em_pt80to120", "qcd_em_pt120to170", "qcd_em_pt170to300", "qcd_em_pt300toInf",
    "qcd_bctoe_pt15to20", "qcd_bctoe_pt20to30", "qcd_bctoe_pt30to80", "qcd_bctoe_pt80to170",
    "qcd_bctoe_pt170to250", "qcd_bctoe_pt250toInf",
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

qcd_ht2000 = qcd.add_process(
    name="qcd_ht2000",
    id=31009,
    xsecs={
        # https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3)
        13: Number(22),
    },
)

#
# QCD pT-binned
#

qcd_pt15to30 = qcd.add_process(
    name="qcd_pt15to30",
    id=31901,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt30to50 = qcd.add_process(
    name="qcd_pt30to50",
    id=31902,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt50to80 = qcd.add_process(
    name="qcd_pt50to80",
    id=31903,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt80to120 = qcd.add_process(
    name="qcd_pt80to120",
    id=31904,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt120to170 = qcd.add_process(
    name="qcd_pt120to170",
    id=31905,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt170to300 = qcd.add_process(
    name="qcd_pt170to300",
    id=31906,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt300to470 = qcd.add_process(
    name="qcd_pt300to470",
    id=31907,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt470to600 = qcd.add_process(
    name="qcd_pt470to600",
    id=31908,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt600to800 = qcd.add_process(
    name="qcd_pt600to800",
    id=31909,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt800to1000 = qcd.add_process(
    name="qcd_pt800to1000",
    id=31910,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt1000to1400 = qcd.add_process(
    name="qcd_pt1000to1400",
    id=31911,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt1400to1800 = qcd.add_process(
    name="qcd_pt1400to1800",
    id=31912,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt1800to2400 = qcd.add_process(
    name="qcd_pt1800to2400",
    id=31913,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt2400to3200 = qcd.add_process(
    name="qcd_pt2400to3200",
    id=31914,
    xsecs={
        13: Number(0.01),  # TODO
    },
)

qcd_pt3200 = qcd.add_process(
    name="qcd_pt3200",
    id=31915,
    xsecs={
        13: Number(0.01),  # TODO
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

# based on datasets QCD_Pt-{i}To{j}_MuEnrichedPt5_TuneCP5_13TeV-pythia8 (Summer20UL16)
# https://cms-gen-dev.cern.ch/xsdb/?columns=37814272&currentPage=0&pageSize=10&searchQuery=DAS%3DQCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8  # noqa
qcd_mu_pt15to20 = qcd_mu.add_process(
    name="qcd_mu_pt15to20",
    id=31101,
    xsecs={
        13: Number(2797000.0),
    },
)

qcd_mu_pt20to30 = qcd_mu.add_process(
    name="qcd_mu_pt20to30",
    id=31102,
    xsecs={
        13: Number(2518000.0),
    },
)
qcd_mu_pt30to50 = qcd_mu.add_process(
    name="qcd_mu_pt30to50",
    id=31103,
    xsecs={
        13: Number(1361000.0),
    },
)

qcd_mu_pt50to80 = qcd_mu.add_process(
    name="qcd_mu_pt50to80",
    id=31104,
    xsecs={
        13: Number(377800.0),
    },
)

qcd_mu_pt80to120 = qcd_mu.add_process(
    name="qcd_mu_pt80to120",
    id=31105,
    xsecs={
        13: Number(88620.0),
    },
)

qcd_mu_pt120to170 = qcd_mu.add_process(
    name="qcd_mu_pt120to170",
    id=31106,
    xsecs={
        13: Number(21070.0),
    },
)

qcd_mu_pt170to300 = qcd_mu.add_process(
    name="qcd_mu_pt170to300",
    id=31107,
    xsecs={
        13: Number(7019.0),
    },
)

qcd_mu_pt300to470 = qcd_mu.add_process(
    name="qcd_mu_pt300to470",
    id=31108,
    xsecs={
        13: Number(622.4),
    },
)

qcd_mu_pt470to600 = qcd_mu.add_process(
    name="qcd_mu_pt470to600",
    id=31109,
    xsecs={
        13: Number(58.86),
    },
)

qcd_mu_pt600to800 = qcd_mu.add_process(
    name="qcd_mu_pt600to800",
    id=31110,
    xsecs={
        13: Number(18.22),
    },
)

qcd_mu_pt800to1000 = qcd_mu.add_process(
    name="qcd_mu_pt800to1000",
    id=31111,
    xsecs={
        13: Number(3.25),
    },
)

qcd_mu_pt1000 = qcd_mu.add_process(
    name="qcd_mu_pt1000",
    id=31112,
    xsecs={
        13: Number(1.08),  # NOTE: not found via XSDB, taken from an old reference
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
    },
)

qcd_em_pt50to80 = qcd_em.add_process(
    name="qcd_em_pt50to80",
    id=31204,
    xsecs={
        13: Number(1988000.0),
    },
)

qcd_em_pt80to120 = qcd_em.add_process(
    name="qcd_em_pt80to120",
    id=31205,
    xsecs={
        13: Number(367500.0),
    },
)

qcd_em_pt120to170 = qcd_em.add_process(
    name="qcd_em_pt120to170",
    id=31206,
    xsecs={
        13: Number(66590.0),
    },
)

qcd_em_pt170to300 = qcd_em.add_process(
    name="qcd_em_pt170to300",
    id=31207,
    xsecs={
        13: Number(16620.0),
    },
)

qcd_em_pt300toInf = qcd_em.add_process(
    name="qcd_em_pt300toInf",
    id=31208,
    xsecs={
        13: Number(1104.0),
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

qcd_bctoe_pt250toInf = qcd_bctoe.add_process(
    name="qcd_bctoe_pt250toInf",
    id=31306,
    xsecs={
        13: Number(562.5),
    },
)
