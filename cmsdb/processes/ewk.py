# coding: utf-8

"""
EWK-related process definitions.
"""

__all__ = [
    "dy",
    "dy_lep",
    "dy_lep_m50", "dy_lep_m50_1j", "dy_lep_m50_2j", "dy_lep_m50_3j", "dy_lep_m50_4j",
    "dy_lep_0j", "dy_lep_1j", "dy_lep_2j",
    "dy_lep_m50_ht70to100", "dy_lep_m50_ht100to200", "dy_lep_m50_ht200to400",
    "dy_lep_m50_ht400to600", "dy_lep_m50_ht600to800", "dy_lep_m50_ht800to1200",
    "dy_lep_m50_ht1200to2500", "dy_lep_m50_ht2500",
    "dy_lep_pt0To50", "dy_lep_pt50To100", "dy_lep_pt100To250", "dy_lep_pt250To400",
    "dy_lep_pt400To650", "dy_lep_pt650",
    "w",
    "w_lnu",
    "w_lnu_ht70To100", "w_lnu_ht100To200", "w_lnu_ht200To400", "w_lnu_ht400To600",
    "w_lnu_ht600To800", "w_lnu_ht800To1200", "w_lnu_ht1200To2500", "w_lnu_ht2500",
    "ewk",
    "ewk_wp_lnu_m50", "ewk_wm_lnu_m50", "ewk_z_ll_m50",
    "vv",
    "zz", "zz_qqll_m4", "zz_llnunu", "zz_llll",
    "wz", "wz_lllnu", "wz_qqll_m4",
    "ww", "ww_lnulnu",
    "vvv",
    "zzz", "wzz", "wwz", "www",
]

from order import Process
from scinum import Number

import cmsdb.constants as const


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    label="Drell-Yan",
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
    label=rf"{dy.label} ($Z \rightarrow ll$)",
    xsecs={13: Number(0.1)},  # TODO
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28

dy_lep_m50 = dy_lep.add_process(
    name="dy_lep_m50",
    id=51100,
    xsecs={13: Number(6077.22, {
        "integration": 1.49,  # error true? or is it error for Z-> mu mu?
        "scale": 0.02j,
        "pdf": 14.78,
    })},
)


# if needed for scaling from NLO to NNLO:
# NLO cross section, based on DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) in xsdb
# https://xsdb-temp.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS%3DDYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8
# created in 2021 by sdeng for EGM

dy_nlo_13TeV_xsec = Number(6404.0, {"tot": 27.69})

# if needed for scaling from LO to NNLO:
# LO cross section, based on DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO) in xsdb
# created in 2021 by sdeng for TAU

dy_lo_13TeV_xsec = Number(5398.0, {"tot": 13.12})

# based on datasets DY{i}JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO) in xsdb
# created in 2021 by sdeng for TAU
dy_lep_m50_1j = dy_lep_m50.add_process(
    name="dy_lep_m50_1j",
    id=51111,
    xsecs={13: Number(928.3, {
        "tot": 2.54,
    })},
)

dy_lep_m50_2j = dy_lep_m50.add_process(
    name="dy_lep_m50_2j",
    id=51112,
    xsecs={13: Number(293.6, {
        "tot": 0.8613,
    })},
)

dy_lep_m50_3j = dy_lep_m50.add_process(
    name="dy_lep_m50_3j",
    id=51113,
    xsecs={13: Number(86.53, {
        "tot": 0.2633,
    })},
)

dy_lep_m50_4j = dy_lep_m50.add_process(
    name="dy_lep_m50_4j",
    id=51114,
    xsecs={13: Number(41.28, {
        "tot": 0.1267,
    })},
)

# based on datasets DYJetsToLL_{i}J_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) in xsdb
# created in 2021 by sdeng for SMP
dy_lep_0j = dy_lep.add_process(
    name="dy_lep_0j",
    id=51200,
    xsecs={13: Number(5129.0, {
        "tot": 8.715,
    })},
)

dy_lep_1j = dy_lep.add_process(
    name="dy_lep_1j",
    id=51300,
    xsecs={13: Number(951.5, {
        "tot": 6.067,
    })},
)

dy_lep_2j = dy_lep.add_process(
    name="dy_lep_2j",
    id=51400,
    xsecs={13: Number(361.4, {
        "tot": 3.704,
    })},
)

# based on datasets DYJetsToLL_M-50_HT-{i}to{j}_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8 (Summer20UL17, LO)in xsdb
# created in 2023 by yuzhe for SUS
# chosen because only one with UL, but errors are larger
dy_lep_m50_ht70to100 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht70to100",
    id=51121,
    xsecs={13: Number(140.0, {
        "tot": 1.255,
    })},
)

dy_lep_m50_ht100to200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht100to200",
    id=51122,
    xsecs={13: Number(139.2, {
        "tot": 1.249,
    })},
)

dy_lep_m50_ht200to400 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht200to400",
    id=51123,
    xsecs={13: Number(38.4, {
        "tot": 0.3494,
    })},
)

dy_lep_m50_ht400to600 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht400to600",
    id=51124,
    xsecs={13: Number(5.174, {
        "tot": 0.04871,
    })},
)

dy_lep_m50_ht600to800 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht600to800",
    id=51125,
    xsecs={13: Number(1.258, {
        "tot": 0.01194,
    })},
)

dy_lep_m50_ht800to1200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht800to1200",
    id=51126,
    xsecs={13: Number(0.5598, {
        "tot": 0.005237,
    })},
)

dy_lep_m50_ht1200to2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht1200to2500",
    id=51127,
    xsecs={13: Number(0.1305, {
        "tot": 0.001241,
    })},
)

dy_lep_m50_ht2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht2500",
    id=51128,
    xsecs={13: Number(0.002997, {
        "tot": 2.837 * 10**(-5),
    })},
)

# based on datasets DYJetsToLL_LHEFilterPtZ-{i}To{j}_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL17, NLO)
# in xsdb.
# created in 2022 by yuzhe for SMP
dy_lep_pt0To50 = dy_lep.add_process(
    name="dy_lep_pt0To50",
    id=51510,
    xsecs={13: Number(1485.0, {
        "tot": 8.457,
    })},
)

dy_lep_pt50To100 = dy_lep.add_process(
    name="dy_lep_pt50To100",
    id=51520,
    xsecs={13: Number(397.4, {
        "tot": 2.867,
    })},
)

dy_lep_pt100To250 = dy_lep.add_process(
    name="dy_lep_pt100To250",
    id=51530,
    xsecs={13: Number(97.2, {
        "tot": 0.7121,
    })},
)

dy_lep_pt250To400 = dy_lep.add_process(
    name="dy_lep_pt250To400",
    id=51540,
    xsecs={13: Number(3.701, {
        "tot": 0.02487,
    })},
)

dy_lep_pt400To650 = dy_lep.add_process(
    name="dy_lep_pt400To650",
    id=51550,
    xsecs={13: Number(0.5086, {
        "tot": 0.003171,
    })},
)

dy_lep_pt650 = dy_lep.add_process(
    name="dy_lep_pt650",
    id=51560,
    xsecs={13: Number(0.04728, {
        "tot": 0.0002801,
    })},
)


#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    xsecs={13: Number(0.1)},  # TODO, or use w.set_xsec(13, w_lnu.get_xsec(13) / const.br_w["lep"]) below?
)

# NNLO cross section, based on:
# https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=27

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={13: const.n_leps * Number(20508.9, {
        "scale": (165.7, 88.2),
        "pdf": 770.9,
    })},
)


# LO cross sections, scaled to NNLO

# needed for scaling to NNLO:
# inclusive LO cross section, based on WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO) in xsdb
# created in 2021 by sdeng for BTV

w_lo_13TeV_xsec = Number(53870.0, {"tot": 129.7})

# ht bins based on datasets WJetsToLNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO) in xsdb
# created in 2021 by sdeng for SUS
w_lnu_ht70To100 = w_lnu.add_process(
    name="w_lnu_ht70To100",
    id=6110,
    xsecs={13: w_lnu.get_xsec(13) * Number(1264.0, {"tot": 3.696}) / w_lo_13TeV_xsec},
)

w_lnu_ht100To200 = w_lnu.add_process(
    name="w_lnu_ht100To200",
    id=6120,
    xsecs={13: w_lnu.get_xsec(13) * Number(1256.0, {"tot": 3.724}) / w_lo_13TeV_xsec},
)

w_lnu_ht200To400 = w_lnu.add_process(
    name="w_lnu_ht200To400",
    id=6130,
    xsecs={13: w_lnu.get_xsec(13) * Number(335.5, {"tot": 1.007}) / w_lo_13TeV_xsec},
)

w_lnu_ht400To600 = w_lnu.add_process(
    name="w_lnu_ht400To600",
    id=6140,
    xsecs={13: w_lnu.get_xsec(13) * Number(45.25, {"tot": 0.136}) / w_lo_13TeV_xsec},
)

w_lnu_ht600To800 = w_lnu.add_process(
    name="w_lnu_ht600To800",
    id=6150,
    xsecs={13: w_lnu.get_xsec(13) * Number(10.97, {"tot": 0.03307}) / w_lo_13TeV_xsec},
)

w_lnu_ht800To1200 = w_lnu.add_process(
    name="w_lnu_ht800To1200",
    id=6160,
    xsecs={13: w_lnu.get_xsec(13) * Number(4.993, {"tot": 0.01492}) / w_lo_13TeV_xsec},
)

w_lnu_ht1200To2500 = w_lnu.add_process(
    name="w_lnu_ht1200To2500",
    id=6170,
    xsecs={13: w_lnu.get_xsec(13) * Number(1.16, {"tot": 0.003605}) / w_lo_13TeV_xsec},
)

# NOTE: Summer20UL16 not available in xsdb, Fall17 cross section is used instead
w_lnu_ht2500 = w_lnu.add_process(
    name="w_lnu_ht2500",
    id=6180,
    xsecs={13: w_lnu.get_xsec(13) * Number(0.008001, {"tot": 2.486 * 10**(-5)}) / w_lo_13TeV_xsec},
)


#
# EWK radiations
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    xsecs={13: Number(0.1)},  # TODO? Sum over the other?
)

# from EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO) on xsdb
# created in 2021 by sdeng for HIG
ewk_wp_lnu_m50 = ewk.add_process(
    name="ewk_wp_lnu_m50",
    id=7100,
    xsecs={13: Number(39.05, {"tot": 0.0291})},
)

# from EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO) on xsdb
# created in 2021 by sdeng for HIG
ewk_wm_lnu_m50 = ewk.add_process(
    name="ewk_wm_lnu_m50",
    id=7200,
    xsecs={13: Number(32.05, {"tot": 0.02492})},
)

# from EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO) on xsdb
# created in 2021 by sdeng for HIG
ewk_z_ll_m50 = ewk.add_process(
    name="ewk_z_ll_m50",
    id=7300,
    xsecs={13: Number(6.215, {"tot": 0.004456})},
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13: Number(0.1)},  # TODO? Sum over WW WZ and ZZ?
)

# ZZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # old: https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(12.13) (LO)
        13: Number(15.99, {"scale": (0.037j, 0.026j)}),
    },
)

# from ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL17, NLO) on xsdb
# created 2023 by yuzhe for SMP
zz_qqll_m4 = zz.add_process(
    name="zz_qqll_m4",
    id=8110,
    xsecs={13: Number(3.676, {"tot": 0.03147})},  # TODO
)

# from ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8 (Summer20UL17, NLO) on xsdb
# created 2023 by yuzhe for SUS
zz_llnunu = zz.add_process(
    name="zz_llnunu",
    id=8120,
    xsecs={13: Number(0.9738, {"tot": 0.0009971})},  # TODO
)

# from ZZTo4L_TuneCP5_13TeV_powheg_pythia8 (Autumn18, NLO) on xsdb
# created 2020 by sdeng for HIG
# maybe better from branching ratios?
zz_llll = zz.add_process(
    name="zz_llll",
    id=8130,
    xsecs={13: Number(1.325, {"tot": 0.00122})},  # TODO
)


# WZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
# can this be used too? https://arxiv.org/pdf/2110.11231.pdf -> actual measurement, no theory prediction
wp_z_xsec = {13: Number(28.55, {"scale": (0.041j, 0.032j)})}

wm_z_xsec = {13: Number(18.19, {"scale": (0.041j, 0.033j)})}

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # old: https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(25.56) (LO)
        13: wp_z_xsec[13] + wm_z_xsec[13],
    },
)

# from WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SMP
# maybe better from branching ratios?
wz_lllnu = wz.add_process(
    name="wz_lllnu",
    id=8210,
    xsecs={13: Number(5.213, {"tot": 0.01618})},
)

# from WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SMP
# maybe better from branching ratios?
wz_qqll_m4 = wz.add_process(
    name="wz_qqll_m4",
    id=8220,
    xsecs={13: Number(6.419, {"tot": 0.01984})},
)

# NNLO QCD from https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=28
# itself from https://arxiv.org/pdf/1408.5243.pdf v1
ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        # old: https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(75.91) (LO)
        13: Number(118.7, {"scale": (0.025j, 0.022j)}),
    },
)

# from WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SUS
# maybe better from branching ratios?
ww_lnulnu = ww.add_process(
    name="ww_lnulnu",
    id=8310,
    xsecs={13: Number(11.09, {"tot": 0.00704})},
)


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    xsecs={13: Number(0.1)},  # TODO, or sum over the ones below?
)

# from ZZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SUS
zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={13: Number(0.01476, {"tot": 2.5 * 10**(-6)})},
)

# from WZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SMP
wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={13: Number(0.05709, {"tot": 6.213 * 10**(-5)})},
)

# from WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SUS
wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={13: Number(0.1707, {"tot": 0.0001757})},
)

# from WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO) on xsdb
# created in 2021 by sdeng for SUS
www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={13: Number(0.2158, {"tot": 0.0002479})},
)
