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
# NLO cross section, based on GenXSecAnalyzer for
# DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see xsec_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8.log

dy_nlo_13TeV_xsec = Number(6421.0, {"tot": 11.25})

# if needed for scaling from LO to NNLO:
# LO cross section, based on GenXSecAnalyzer for DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# see xsec_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.log

dy_lo_13TeV_xsec = Number(5395.0, {"tot": 1.858})

# based on GenXSecAnalyzer
# for datasets DY{i}JetsToLL_M-50_MatchEWPDG20_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# see logs
dy_lep_m50_1j = dy_lep_m50.add_process(
    name="dy_lep_m50_1j",
    id=51111,
    xsecs={13: Number(926.8, {
        "tot": 0.3597,
    })},
)

dy_lep_m50_2j = dy_lep_m50.add_process(
    name="dy_lep_m50_2j",
    id=51112,
    xsecs={13: Number(294.5, {
        "tot": 0.1223,
    })},
)

dy_lep_m50_3j = dy_lep_m50.add_process(
    name="dy_lep_m50_3j",
    id=51113,
    xsecs={13: Number(86.53, {
        "tot": 0.03853,
    })},
)

dy_lep_m50_4j = dy_lep_m50.add_process(
    name="dy_lep_m50_4j",
    id=51114,
    xsecs={13: Number(41.21, {
        "tot": 0.02392,
    })},
)

# based on GenXSecAnalyzer
# for DYJetsToLL_{i}J_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see logs
dy_lep_0j = dy_lep.add_process(
    name="dy_lep_0j",
    id=51200,
    xsecs={13: Number(5134.0, {
        "tot": 5.365,
    })},
)

dy_lep_1j = dy_lep.add_process(
    name="dy_lep_1j",
    id=51300,
    xsecs={13: Number(952.7, {
        "tot": 2.174,
    })},
)

dy_lep_2j = dy_lep.add_process(
    name="dy_lep_2j",
    id=51400,
    xsecs={13: Number(359.1, {
        "tot": 1.533,
    })},
)

# based on GenXSecAnalyzer
# for DYJetsToLL_M-50_HT-{i}to{j}_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# see logs
dy_lep_m50_ht70to100 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht70to100",
    id=51121,
    xsecs={13: Number(139.9, {
        "tot": 0.5747,
    })},
)

dy_lep_m50_ht100to200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht100to200",
    id=51122,
    xsecs={13: Number(140.1, {
        "tot": 0.5875,
    })},
)

dy_lep_m50_ht200to400 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht200to400",
    id=51123,
    xsecs={13: Number(38.38, {
        "tot": 0.01628,
    })},
)

dy_lep_m50_ht400to600 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht400to600",
    id=51124,
    xsecs={13: Number(5.212, {
        "tot": 0.003149,
    })},
)

dy_lep_m50_ht600to800 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht600to800",
    id=51125,
    xsecs={13: Number(1.266, {
        "tot": 0.0007976,
    })},
)

dy_lep_m50_ht800to1200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht800to1200",
    id=51126,
    xsecs={13: Number(0.5684, {
        "tot": 0.0003515,
    })},
)

dy_lep_m50_ht1200to2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht1200to2500",
    id=51127,
    xsecs={13: Number(0.1332, {
        "tot": 0.00009084,
    })},
)

dy_lep_m50_ht2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht2500",
    id=51128,
    xsecs={13: Number(0.002977, {
        "tot": 0.000003412,
    })},
)

# based on GenXSecAnalyzer
# for DYJetsToLL_LHEFilterPtZ-{i}To{j}_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see logs
dy_lep_pt0To50 = dy_lep.add_process(
    name="dy_lep_pt0To50",
    id=51510,
    xsecs={13: Number(1494.0, {
        "tot": 1.751,
    })},
)

dy_lep_pt50To100 = dy_lep.add_process(
    name="dy_lep_pt50To100",
    id=51520,
    xsecs={13: Number(398.3, {
        "tot": 0.5600,
    })},
)

dy_lep_pt100To250 = dy_lep.add_process(
    name="dy_lep_pt100To250",
    id=51530,
    xsecs={13: Number(96.58, {
        "tot": 0.1370,
    })},
)

dy_lep_pt250To400 = dy_lep.add_process(
    name="dy_lep_pt250To400",
    id=51540,
    xsecs={13: Number(3.738, {
        "tot": 0.005305,
    })},
)

dy_lep_pt400To650 = dy_lep.add_process(
    name="dy_lep_pt400To650",
    id=51550,
    xsecs={13: Number(0.5050, {
        "tot": 0.0008169,
    })},
)

dy_lep_pt650 = dy_lep.add_process(
    name="dy_lep_pt650",
    id=51560,
    xsecs={13: Number(0.04763, {
        "tot": 0.00007206,
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


# LO cross section, needed for scaling to NNLO:
# based on GenXSecAnalyzer
# for WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# see logs

w_lnu_lo_13TeV_xsec = Number(54070.0, {"tot": 18.32})

# LO cross sections, scaled to NNLO

# ht bins based on GenXSecAnalyzer
# for WJetsToLNu_HT-{i}To{j}_TuneCP5_13TeV-madgraphMLM-pythia8 (Summer20UL16, LO)
# see logs
w_lnu_ht70To100 = w_lnu.add_process(
    name="w_lnu_ht70To100",
    id=6110,
    xsecs={13: w_lnu.get_xsec(13) * Number(1270.0, {"tot": 0.5259}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht100To200 = w_lnu.add_process(
    name="w_lnu_ht100To200",
    id=6120,
    xsecs={13: w_lnu.get_xsec(13) * Number(1254.0, {"tot": 0.5274}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht200To400 = w_lnu.add_process(
    name="w_lnu_ht200To400",
    id=6130,
    xsecs={13: w_lnu.get_xsec(13) * Number(336.6, {"tot": 0.1528}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht400To600 = w_lnu.add_process(
    name="w_lnu_ht400To600",
    id=6140,
    xsecs={13: w_lnu.get_xsec(13) * Number(45.21, {"tot": 0.02966}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht600To800 = w_lnu.add_process(
    name="w_lnu_ht600To800",
    id=6150,
    xsecs={13: w_lnu.get_xsec(13) * Number(10.98, {"tot": 0.006997}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht800To1200 = w_lnu.add_process(
    name="w_lnu_ht800To1200",
    id=6160,
    xsecs={13: w_lnu.get_xsec(13) * Number(4.927, {"tot": 0.003229}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht1200To2500 = w_lnu.add_process(
    name="w_lnu_ht1200To2500",
    id=6170,
    xsecs={13: w_lnu.get_xsec(13) * Number(1.157, {"tot": 0.0007663}) / w_lnu_lo_13TeV_xsec},
)

w_lnu_ht2500 = w_lnu.add_process(
    name="w_lnu_ht2500",
    id=6180,
    xsecs={13: w_lnu.get_xsec(13) * Number(0.02624, {"tot": 0.00002981}) / w_lnu_lo_13TeV_xsec},
)


#
# EWK radiations
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    xsecs={13: Number(0.1)},  # TODO? Sum over the other? maybe with scaled w xsec to inclusive?
)

# based on GenXSecAnalyzer
# for EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# see logs
ewk_wp_lnu_m50 = ewk.add_process(
    name="ewk_wp_lnu_m50",
    id=7100,
    xsecs={13: Number(39.07, {"tot": 0.006454})},
)

# based on GenXSecAnalyzer
# for EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# see logs
ewk_wm_lnu_m50 = ewk.add_process(
    name="ewk_wm_lnu_m50",
    id=7200,
    xsecs={13: Number(32.10, {"tot": 0.005308})},
)

# based on GenXSecAnalyzer
# for EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8 (Summer20UL16, LO)
# see logs
ewk_z_ll_m50 = ewk.add_process(
    name="ewk_z_ll_m50",
    id=7300,
    xsecs={13: Number(6.206, {"tot": 0.002081})},
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13: Number(0.1)},  # updated below as the sum over WW, WZ, ZZ
)

# ZZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(12.13) (LO)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        13: Number(15.99, {"scale": (0.037j, 0.026j)}),
    },
)

# based on GenXSecAnalyzer
# for ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see logs
zz_qqll_m4 = zz.add_process(
    name="zz_qqll_m4",
    id=8110,
    xsecs={13: Number(3.697, {"tot": 0.002713})},
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_2L2NU_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# for ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8 (Summer20UL16, NLO)
# see logs
zz_llnunu = zz.add_process(
    name="zz_llnunu",
    id=8120,
    xsecs={13: Number(0.9738, {"tot": 0.0009971})},
)

# looking at the generator config:
# https://raw.githubusercontent.com/cms-sw/genproductions/ce68f8a7ab05f530e0a99124088c08d1cc2bf355/bin/Powheg/production/2017/13TeV/ZZ/ZZ_4L_NNPDF31_13TeV.input  # noqa
# it seems that there is a lepton mass cut of 4 GeV, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# from ZZTo4L_TuneCP5_13TeV_powheg_pythia8 (Summer20UL16, NLO)
# see logs
zz_llll = zz.add_process(
    name="zz_llll",
    id=8130,
    xsecs={13: Number(1.325, {"tot": 0.00122})},
)


# WZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
# can this be used too? https://arxiv.org/pdf/2110.11231.pdf -> actual measurement, no theory prediction
wp_z_xsec = {13: Number(28.55, {"scale": (0.041j, 0.032j)})}

wm_z_xsec = {13: Number(18.19, {"scale": (0.041j, 0.033j)})}

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(25.56) (LO)
wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # as a remark, the W cross section calculation from
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
        # shows a permille difference in the values calculated directly and the ones added from w+ and w-
        13: wp_z_xsec[13] + wm_z_xsec[13],
    },
)

# looking at the generator config:
# https://github.com/cms-sw/genproductions/blob/2422e1837f93f875c54f8ace0f02d3dc962eca41/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WZTo3LNu01j_5f_NLO_FXFX/WZTo3LNu01j_5f_NLO_FXFX_run_card.dat  # noqa
# it seems that there is a lepton mass cut of 4 GeV for leptons from Z, like in the ZZTo2Q2L channel
# therefore values from GenXSecAnalyzer
# for WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see logs
wz_lllnu = wz.add_process(
    name="wz_lllnu",
    id=8210,
    xsecs={13: Number(5.218, {"tot": 0.00525})},
)

# based on GenXSecAnalyzer
# for WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8 (Summer20UL16, NLO)
# see logs
wz_qqll_m4 = wz.add_process(
    name="wz_qqll_m4",
    id=8220,
    xsecs={13: Number(6.431, {"tot": 0.007851})},
)

# NNLO QCD from https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV?rev=28
# itself from https://arxiv.org/pdf/1408.5243.pdf v1

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(75.91) (LO)
ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        13: Number(118.7, {"scale": (0.025j, 0.022j)}),
    },
)

# update vv cross section
for cme in [13]:
    vv.set_xsec(cme, ww.get_xsec(cme) + wz.get_xsec(cme) + zz.get_xsec(cme))

# no additional cut found in generator card:
# https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/Powheg/production/2017/13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV/WWTo2L2Nu_NNPDF31nnlo_13TeV.input  # noqa
# therefore, value obtained from branching ratio.
# Log for GenXSecAnalyzer of
# WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 (Summer20UL16, NLO) with Number(11.09, {"tot": 0.00704})
# also available, but not used here
ww_lnulnu = ww.add_process(
    name="ww_lnulnu",
    id=8310,
    xsecs={13: ww.get_xsec(13) * const.br_ww.dl},  # value around 12.6 for comparison to GenXSecAnalyzer NLO result
)


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    xsecs={13: Number(0.1)},  # updated below as sum over individual processes
)

# based on GenXSecAnalyzer
# for ZZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO)
# remark: calculated xsec has lower error for sample without ext-1 as not all events were used for calculation of ext-1
# therefore the value for the sample without ext-1 is taken
# see logs
zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={13: Number(0.01476, {"tot": 2.347 * 10**(-6)})},
)

# based on GenXSecAnalyzer
# for WZZ_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# see logs
wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={13: Number(0.05709, {"tot": 6.213 * 10**(-5)})},
)

# based on GenXSecAnalyzer
# for WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# see logs
wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={13: Number(0.1707, {"tot": 0.0001757})},
)

# based on GenXSecAnalyzer
# for WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO, ext-1)
# remark: calculated xsec is the same for simple sample and ext-1 sample
# see logs
www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={13: Number(0.2158, {"tot": 0.0002479})},
)

# update vvv cross section
for cme in [13]:
    vvv.set_xsec(cme, www.get_xsec(cme) + wwz.get_xsec(cme) + wzz.get_xsec(cme) + zzz.get_xsec(cme))
