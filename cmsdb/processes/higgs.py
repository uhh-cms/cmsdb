# coding: utf-8

"""
Single Higgs process definitions.

Production channel abbreviatons:
- h: inclusive Higgs production
- h_ggf: Higgs production via gluon-gluon fusion
- h_vbf: Higgs production via vector boson fusion
- vh: associated production with a vector boson
- zh: associated production with a Z boson
- zh_gg: associated production with a Z boson via gluon-gluon box diagram
- wh: associated production with a W boson
- tth: associated production with a top quark pair
- bbh: associated production with a bottom quark pair
- ttvh: associated production with a top quark pair and a vector boson
- ttzh: associated production with a top quark pair and a Z boson
- ttwh: associated production with a top quark pair and a W boson
- thw: associated production with a top quark and a W boson
- thq: associated production with a top quark and a light quark (also named tH t-channel)
- thb: associated production with a top quark and a bottom quark (also named tH s-channel)


Decay channel abbreviations:
- hbb: Higgs to bb
- hnonbb: Higgs to everything except bb
- hcc: Higgs to cc
- htt: Higgs to tau tau
- hww: Higgs to WW
- hzz: Higgs to ZZ
- hzg: Higgs to Zgamma
- hgg: Higgs to gamma gamma
- hmm: Higgs to mumu
- hww2l2nu: Higgs to WW(2l2nu)
- hwwqqlnu: Higgs to WW(qqlnu)
- hww4q:    Higgs to WW(4q)
- hzz4l:    Higgs to ZZ(4l)
- hzz2l2nu: Higgs to ZZ(2l2nu)
- hzz2l2q:  Higgs to ZZ(2l2q)
- hzz2q2nu: Higgs to ZZ(2q2nu)
- hzz4nu:   Higgs to ZZ(4nu)
- hzz4q:    Higgs to ZZ(4q)
- hzgll:    Higgs to Z(ll)gamma
- hzgqq:    Higgs to Z(qq)gamma
- hzgnunu:  Higgs to Z(nunu)gamma
- zll: Z to ll
- zqq: Z to qq
- znunu: Z to nunu
- wlnu: W to lnu
- wqq: W to qq

Process naming scheme: {prod}_{decay_v}_{decay_h}
- prod: production channel; options: h_ggf, h_vbf, vh, zh, ggf_zh, wh, wph, wmh, tth
- decay_v: decay of the vector boson; options: zll, zqq, znunu, wlnu, wqq
- decay_h: decay of the Higgs boson; options: hbb, hcc, htt, hww, hzz, hzg, hgg, hmm, hee;
           when vector bosons further decay, this is also included; options:
           hzz4l, hzz2l2nu, hzz2l2q, hzz2q2nu, hzz4nu, hzz4q,
           hww2l2nu, hww4l, hww4q, hzgll, hzgqq, hzgnunu

ID scheme:
- 1xxxx: single Higgs processes
- 2xxxx: double Higgs processes

Single Higgs production channels:
- 10xxx: h
- 11xxx: h_ggf
- 12xxx: h_vbf
- 13xxx: vh
- 14xxx: zh
- 15xxx: zh_gg
- 16xxx: wh
- 17xxx: wph
- 18xxx: wmh
- 19xxx: tth
- 110xxx: bbh
- 111xxx: ttvh
- 112xxx: ttzh
- 113xxx: ttwh
- 114xxx: thw
- 115xxx: thq
- 116xxx: thb

Single Higgs decay channels:
- 1x100: H->tau tau
- 1x200: H->WW
- 1x300: H->ZZ
- 1x400: H->bb
- 1x500: H->non-bb
- 1x600: H->cc
- 1x700: H->Zgamma
- 1x800: H->gamma gamma
- 1x900: H->mumu

ZZ decay channels:
- 1xx10: 4l
- 1xx20: 2l2nu
- 1xx30: 2l2q
- 1xx40: 2q2nu
- 1xx50: 4nu
- 1xx60: 4q

WW decay channels:
- 1xx10: 2l2nu
- 1xx20: 4l
- 1xx30: 4q

Z decay channels (for Zgamma):
- 1xx10: ll
- 1xx20: qq
- 1xx30: nunu

ZH Z decay channels:
- 14xx1: zll
- 14xx2: zqq
- 14xx3: znunu

WH W decay channels:
- 16xx1: wlnu
- 16xx2: wqq

ttH tt decay channels:
- 19xx1: sl
- 19xx2: dl
- 19xx3: fh

"""

from __future__ import annotations

__all__ = [
    "h",
    "h_htt", "h_hww", "h_hzz", "h_hbb", "h_hnonbb", "h_hcc", "h_hzg", "h_hgg", "h_hmm",
    "h_hwwqqlnu", "h_hww2l2nu", "h_hww4q",
    "h_hzz4l", "h_hzz2l2nu", "h_hzz2l2q", "h_hzz2q2nu", "h_hzz4nu", "h_hzz4q",
    "h_hzg_zll", "h_hzg_zqq", "h_hzg_znunu",
    "h_ggf",
    "h_ggf_htt", "h_ggf_hww", "h_ggf_hzz", "h_ggf_hbb", "h_ggf_hnonbb", "h_ggf_hcc",
    "h_ggf_hzg", "h_ggf_hgg", "h_ggf_hmm",
    "h_ggf_hwwqqlnu", "h_ggf_hww2l2nu", "h_ggf_hww4q",
    "h_ggf_hzz4l", "h_ggf_hzz2l2nu", "h_ggf_hzz2l2q", "h_ggf_hzz2q2nu", "h_ggf_hzz4nu", "h_ggf_hzz4q",
    "h_ggf_hzg_zll", "h_ggf_hzg_zqq", "h_ggf_hzg_znunu",
    "h_vbf",
    "h_vbf_htt", "h_vbf_hww", "h_vbf_hzz", "h_vbf_hbb", "h_vbf_hnonbb", "h_vbf_hcc",
    "h_vbf_hzg", "h_vbf_hgg", "h_vbf_hmm",
    "h_vbf_hwwqqlnu", "h_vbf_hww2l2nu", "h_vbf_hww4q",
    "h_vbf_hzz4l", "h_vbf_hzz2l2nu", "h_vbf_hzz2l2q", "h_vbf_hzz2q2nu", "h_vbf_hzz4nu", "h_vbf_hzz4q",
    "h_vbf_hzg_zll", "h_vbf_hzg_zqq", "h_vbf_hzg_znunu",
    "vh",
    "vh", "vh_htt", "vh_hww", "vh_hzz", "vh_hbb", "vh_hnonbb", "vh_hcc",
    "vh_hzg", "vh_hgg", "vh_hmm",
    "vh_hwwqqlnu", "vh_hww2l2nu", "vh_hww4q",
    "vh_hzz4l", "vh_hzz2l2nu", "vh_hzz2l2q", "vh_hzz2q2nu", "vh_hzz4nu", "vh_hzz4q",
    "vh_zll", "vh_zll_htt", "vh_zll_hww", "vh_zll_hzz", "vh_zll_hbb", "vh_zll_hnonbb", "vh_zll_hcc",
    "vh_zll_hzg", "vh_zll_hgg", "vh_zll_hmm",
    "vh_zll_hwwqqlnu", "vh_zll_hww2l2nu", "vh_zll_hww4q",
    "vh_zll_hzz4l", "vh_zll_hzz2l2nu", "vh_zll_hzz2l2q", "vh_zll_hzz2q2nu", "vh_zll_hzz4nu", "vh_zll_hzz4q",
    "vh_zll_hzg_zll", "vh_zll_hzg_zqq", "vh_zll_hzg_znunu",
    "vh_zqq", "vh_zqq_htt", "vh_zqq_hww", "vh_zqq_hzz", "vh_zqq_hbb", "vh_zqq_hnonbb", "vh_zqq_hcc",
    "vh_zqq_hzg", "vh_zqq_hgg", "vh_zqq_hmm",
    "vh_zqq_hwwqqlnu", "vh_zqq_hww2l2nu", "vh_zqq_hww4q",
    "vh_zqq_hzz4l", "vh_zqq_hzz2l2nu", "vh_zqq_hzz2l2q", "vh_zqq_hzz2q2nu", "vh_zqq_hzz4nu", "vh_zqq_hzz4q",
    "vh_zqq_hzg_zll", "vh_zqq_hzg_zqq", "vh_zqq_hzg_znunu",
    "zh",
    "zh_htt", "zh_hww", "zh_hzz", "zh_hbb", "zh_hnonbb", "zh_hcc",
    "zh_hzg", "zh_hgg", "zh_hmm",
    "zh_hwwqqlnu", "zh_hww2l2nu", "zh_hww4q",
    "zh_hzz4l", "zh_hzz2l2nu", "zh_hzz2l2q", "zh_hzz2q2nu", "zh_hzz4nu", "zh_hzz4q",
    "zh_hzg", "zh_hzg_zll", "zh_hzg_zqq", "zh_hzg_znunu",
    "zh_zll", "zh_zll_htt", "zh_zll_hww", "zh_zll_hzz", "zh_zll_hbb", "zh_zll_hnonbb", "zh_zll_hcc",
    "zh_zll_hzg", "zh_zll_hgg", "zh_zll_hmm",
    "zh_zll_hwwqqlnu", "zh_zll_hww2l2nu", "zh_zll_hww4q",
    "zh_zll_hzz4l", "zh_zll_hzz2l2nu", "zh_zll_hzz2l2q", "zh_zll_hzz2q2nu", "zh_zll_hzz4nu", "zh_zll_hzz4q",
    "zh_zll_hzg_zll", "zh_zll_hzg_zqq", "zh_zll_hzg_znunu",
    "zh_zqq", "zh_zqq_htt", "zh_zqq_hww", "zh_zqq_hzz", "zh_zqq_hbb", "zh_zqq_hnonbb", "zh_zqq_hcc",
    "zh_zqq_hzg", "zh_zqq_hgg", "zh_zqq_hmm",
    "zh_zqq_hwwqqlnu", "zh_zqq_hww2l2nu", "zh_zqq_hww4q",
    "zh_zqq_hzz4l", "zh_zqq_hzz2l2nu", "zh_zqq_hzz2l2q", "zh_zqq_hzz2q2nu", "zh_zqq_hzz4nu", "zh_zqq_hzz4q",
    "zh_zqq_hzg_zll", "zh_zqq_hzg_zqq", "zh_zqq_hzg_znunu",
    "zh_znunu", "zh_znunu_htt", "zh_znunu_hww", "zh_znunu_hzz", "zh_znunu_hbb", "zh_znunu_hnonbb", "zh_znunu_hcc",
    "zh_znunu_hzg", "zh_znunu_hgg", "zh_znunu_hmm",
    "zh_znunu_hwwqqlnu", "zh_znunu_hww2l2nu", "zh_znunu_hww4q",
    "zh_znunu_hzz4l", "zh_znunu_hzz2l2nu", "zh_znunu_hzz2l2q", "zh_znunu_hzz2q2nu", "zh_znunu_hzz4nu", "zh_znunu_hzz4q",
    "zh_znunu_hzg_zll", "zh_znunu_hzg_zqq", "zh_znunu_hzg_znunu",
    "zh_gg",
    "zh_gg_htt", "zh_gg_hww", "zh_gg_hzz", "zh_gg_hbb", "zh_gg_hnonbb", "zh_gg_hcc",
    "zh_gg_hzg", "zh_gg_hgg", "zh_gg_hmm",
    "zh_gg_hwwqqlnu", "zh_gg_hww2l2nu", "zh_gg_hww4q",
    "zh_gg_hzz4l", "zh_gg_hzz2l2nu", "zh_gg_hzz2l2q", "zh_gg_hzz2q2nu", "zh_gg_hzz4nu", "zh_gg_hzz4q",
    "zh_gg_hzg", "zh_gg_hzg_zll", "zh_gg_hzg_zqq", "zh_gg_hzg_znunu",
    "zh_gg_zll", "zh_gg_zll_htt", "zh_gg_zll_hww", "zh_gg_zll_hzz",
    "zh_gg_zll_hbb", "zh_gg_zll_hnonbb", "zh_gg_zll_hcc",
    "zh_gg_zll_hzg", "zh_gg_zll_hgg", "zh_gg_zll_hmm",
    "zh_gg_zll_hwwqqlnu", "zh_gg_zll_hww2l2nu", "zh_gg_zll_hww4q",
    "zh_gg_zll_hzz4l", "zh_gg_zll_hzz2l2nu", "zh_gg_zll_hzz2l2q",
    "zh_gg_zll_hzz2q2nu", "zh_gg_zll_hzz4nu", "zh_gg_zll_hzz4q",
    "zh_gg_zll_hzg_zll", "zh_gg_zll_hzg_zqq", "zh_gg_zll_hzg_znunu",
    "zh_gg_zqq", "zh_gg_zqq_htt", "zh_gg_zqq_hww", "zh_gg_zqq_hzz",
    "zh_gg_zqq_hbb", "zh_gg_zqq_hnonbb", "zh_gg_zqq_hcc",
    "zh_gg_zqq_hzg", "zh_gg_zqq_hgg", "zh_gg_zqq_hmm",
    "zh_gg_zqq_hwwqqlnu", "zh_gg_zqq_hww2l2nu", "zh_gg_zqq_hww4q",
    "zh_gg_zqq_hzz4l", "zh_gg_zqq_hzz2l2nu", "zh_gg_zqq_hzz2l2q",
    "zh_gg_zqq_hzz2q2nu", "zh_gg_zqq_hzz4nu", "zh_gg_zqq_hzz4q",
    "zh_gg_zqq_hzg_zll", "zh_gg_zqq_hzg_zqq", "zh_gg_zqq_hzg_znunu",
    "zh_gg_znunu", "zh_gg_znunu_htt", "zh_gg_znunu_hww", "zh_gg_znunu_hzz",
    "zh_gg_znunu_hbb", "zh_gg_znunu_hnonbb", "zh_gg_znunu_hcc",
    "zh_gg_znunu_hzg", "zh_gg_znunu_hgg", "zh_gg_znunu_hmm",
    "zh_gg_znunu_hwwqqlnu", "zh_gg_znunu_hww2l2nu", "zh_gg_znunu_hww4q",
    "zh_gg_znunu_hzz4l", "zh_gg_znunu_hzz2l2nu", "zh_gg_znunu_hzz2l2q",
    "zh_gg_znunu_hzz2q2nu", "zh_gg_znunu_hzz4nu", "zh_gg_znunu_hzz4q",
    "zh_gg_znunu_hzg_zll", "zh_gg_znunu_hzg_zqq", "zh_gg_znunu_hzg_znunu",
    "wh", "wph", "wmh",
    "wh_htt", "wh_hww", "wh_hzz", "wh_hbb", "wh_hnonbb", "wh_hcc",
    "wh_hzg", "wh_hgg", "wh_hmm",
    "wh_hwwqqlnu", "wh_hww2l2nu", "wh_hww4q",
    "wh_hzz4l", "wh_hzz2l2nu", "wh_hzz2l2q", "wh_hzz2q2nu", "wh_hzz4nu", "wh_hzz4q",
    "wh_hzg_zll", "wh_hzg_zqq", "wh_hzg_znunu",
    "wph",
    "wph_htt", "wph_hww", "wph_hzz", "wph_hbb", "wph_hnonbb", "wph_hcc",
    "wph_hzg", "wph_hgg", "wph_hmm",
    "wph_hwwqqlnu", "wph_hww2l2nu", "wph_hww4q",
    "wph_hzz4l", "wph_hzz2l2nu", "wph_hzz2l2q", "wph_hzz2q2nu", "wph_hzz4nu", "wph_hzz4q",
    "wph_hzg_zll", "wph_hzg_zqq", "wph_hzg_znunu",
    "wmh_htt", "wmh_hww", "wmh_hzz", "wmh_hbb", "wmh_hnonbb", "wmh_hcc",
    "wmh_hzg", "wmh_hgg", "wmh_hmm",
    "wmh_hwwqqlnu", "wmh_hww2l2nu", "wmh_hww4q",
    "wmh_hzz4l", "wmh_hzz2l2nu", "wmh_hzz2l2q", "wmh_hzz2q2nu", "wmh_hzz4nu", "wmh_hzz4q",
    "wmh_hzg_zll", "wmh_hzg_zqq", "wmh_hzg_znunu",
    "wph_wlnu",
    "wph_wlnu_htt", "wph_wlnu_hww", "wph_wlnu_hzz", "wph_wlnu_hbb", "wph_wlnu_hnonbb", "wph_wlnu_hcc",
    "wph_wlnu_hzg", "wph_wlnu_hgg", "wph_wlnu_hmm",
    "wph_wlnu_hwwqqlnu", "wph_wlnu_hww2l2nu", "wph_wlnu_hww4q",
    "wph_wlnu_hzz4l", "wph_wlnu_hzz2l2nu", "wph_wlnu_hzz2l2q", "wph_wlnu_hzz2q2nu", "wph_wlnu_hzz4nu", "wph_wlnu_hzz4q",
    "wph_wlnu_hzg_zll", "wph_wlnu_hzg_zqq", "wph_wlnu_hzg_znunu",
    "wph_wqq",
    "wph_wqq_htt", "wph_wqq_hww", "wph_wqq_hzz", "wph_wqq_hbb", "wph_wqq_hnonbb", "wph_wqq_hcc",
    "wph_wqq_hzg", "wph_wqq_hgg", "wph_wqq_hmm",
    "wph_wqq_hwwqqlnu", "wph_wqq_hww2l2nu", "wph_wqq_hww4q",
    "wph_wqq_hzz4l", "wph_wqq_hzz2l2nu", "wph_wqq_hzz2l2q", "wph_wqq_hzz2q2nu", "wph_wqq_hzz4nu", "wph_wqq_hzz4q",
    "wph_wqq_hzg_zll", "wph_wqq_hzg_zqq", "wph_wqq_hzg_znunu",
    "wmh_wlnu",
    "wmh_wlnu_htt", "wmh_wlnu_hww", "wmh_wlnu_hzz", "wmh_wlnu_hbb", "wmh_wlnu_hnonbb", "wmh_wlnu_hcc",
    "wmh_wlnu_hzg", "wmh_wlnu_hgg", "wmh_wlnu_hmm",
    "wmh_wlnu_hwwqqlnu", "wmh_wlnu_hww2l2nu", "wmh_wlnu_hww4q",
    "wmh_wlnu_hzz4l", "wmh_wlnu_hzz2l2nu", "wmh_wlnu_hzz2l2q", "wmh_wlnu_hzz2q2nu", "wmh_wlnu_hzz4nu", "wmh_wlnu_hzz4q",
    "wmh_wlnu_hzg_zll", "wmh_wlnu_hzg_zqq", "wmh_wlnu_hzg_znunu",
    "wmh_wqq",
    "wmh_wqq_htt", "wmh_wqq_hww", "wmh_wqq_hzz", "wmh_wqq_hbb", "wmh_wqq_hnonbb", "wmh_wqq_hcc",
    "wmh_wqq_hzg", "wmh_wqq_hgg", "wmh_wqq_hmm",
    "wmh_wqq_hwwqqlnu", "wmh_wqq_hww2l2nu", "wmh_wqq_hww4q",
    "wmh_wqq_hzz4l", "wmh_wqq_hzz2l2nu", "wmh_wqq_hzz2l2q", "wmh_wqq_hzz2q2nu", "wmh_wqq_hzz4nu", "wmh_wqq_hzz4q",
    "wmh_wqq_hzg_zll", "wmh_wqq_hzg_zqq", "wmh_wqq_hzg_znunu",
    "tth",
    "tth_htt", "tth_hww", "tth_hzz", "tth_hbb", "tth_hnonbb", "tth_hcc", "tth_hzg", "tth_hgg", "tth_hmm",
    "tth_hwwqqlnu", "tth_hww2l2nu", "tth_hww4q",
    "tth_hzz4l", "tth_hzz2l2nu", "tth_hzz2l2q", "tth_hzz2q2nu", "tth_hzz4nu", "tth_hzz4q",
    "tth_hzg_zll", "tth_hzg_zqq", "tth_hzg_znunu",
    # TODO: the following processes are not yet implemented in full combination
    "bbh", "ttvh", "ttzh", "ttwh", "thw", "thq", "thb",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import add_xsecs, DotDict, add_decay_process, add_sub_decay_process

####################################################################################################
#
# Single Higgs
#
####################################################################################################

# 13 TeV source: xsecs were given in pb, uncertainties in %, values are taken for m_H = 125 GeV
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV?rev=24

# preliminary Higgs cross sections at 13.6 TeV taken from here:
# https://cds.cern.ch/record/2886099/files/LHCHWG-2024-001.pdf?version=2
# Twiki of (currently outdated) 13.6 TeV Higgs cross sections (might be a useful source when updated):
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWG136TeVxsec_extrap?rev=5

# top level parameters for Higgs decay channels
h_decay_map = DotDict.wrap({
    "htt": {
        "name": "htt",
        "id": 100,
        "br": const.br_h.tt,
        "label": r"$H \rightarrow \tau\tau$",
    },
    "hww": {
        "name": "hww",
        "id": 200,
        "br": const.br_h.ww,
        "label": r"$H \rightarrow WW$",
    },
    "hzz": {
        "name": "hzz",
        "id": 300,
        "br": const.br_h.zz,
        "label": r"$H \rightarrow ZZ$",
    },
    "hbb": {
        "name": "hbb",
        "id": 400,
        "br": const.br_h.bb,
        "label": r"$H \rightarrow bb$",
    },
    "hnonbb": {
        "name": "hnonbb",
        "id": 500,
        "br": 1 - const.br_h.bb,
        "label": r"$H \rightarrow$ non-$bb$",
    },
    "hcc": {
        "name": "hcc",
        "id": 600,
        "br": const.br_h.cc,
        "label": r"$H \rightarrow cc$",
    },
    "hzg": {
        "name": "hzg",
        "id": 700,
        "br": const.br_h.zg,
        "label": r"$H \rightarrow Z\gamma$",
    },
    "hgg": {
        "name": "hgg",
        "id": 800,
        "br": const.br_h.gg,
        "label": r"$H \rightarrow \gamma\gamma$",
    },
    "hmm": {
        "name": "hmm",
        "id": 900,
        "br": const.br_h.mm,
        "label": r"$H \rightarrow \mu\mu$",
    },
})

zz_decay_map = DotDict.wrap({
    "4l": {
        "name": "4l",
        "id": 10,
        "label": r"$(4\ell)$",
        "br": const.br_zz.llll,
    },
    "2l2nu": {
        "name": "2l2nu",
        "id": 20,
        "label": r"$(2\ell 2\nu)$",
        "br": const.br_zz.llnunu,
    },
    "2l2q": {
        "name": "2l2q",
        "id": 30,
        "label": r"$(2\ell 2q)$",
        "br": const.br_zz.llqq,
    },
    "2q2nu": {
        "name": "2q2nu",
        "id": 40,
        "label": r"$(2q 2\nu)$",
        "br": const.br_zz.qqnunu,
    },
    "4nu": {
        "name": "4nu",
        "id": 50,
        "label": r"$(4\nu)$",
        "br": const.br_zz.nunununu,
    },
    "4q": {
        "name": "4q",
        "id": 60,
        "label": r"$(4q)$",
        "br": const.br_zz.qqqq,
    },
})

ww_decay_map = DotDict.wrap({
    "qqlnu": {
        "name": "qqlnu",
        "id": 10,
        "label": r"$(qq\ell\nu)$",
        "br": const.br_ww.sl,
    },
    "2l2nu": {
        "name": "2l2nu",
        "id": 20,
        "label": r"$(2\ell 2\nu)$",
        "br": const.br_ww.dl,
    },
    "4q": {
        "name": "4q",
        "id": 30,
        "label": r"$(4q)$",
        "br": const.br_ww.fh,
    },
})

hzg_decay_map = DotDict.wrap({
    "zll": {
        "name": "zll",
        "id": 10,
        "label": r"$Z \rightarrow ll$",
        "br": const.br_z.clep,
    },
    "zqq": {
        "name": "zqq",
        "id": 20,
        "label": r"$Z \rightarrow qq$",
        "br": const.br_z.qq,
    },
    "znunu": {
        "name": "znunu",
        "id": 30,
        "label": r"$Z \rightarrow \nu\nu$",
        "br": const.br_z.nunu,
    },
})

z_decay_map = DotDict.wrap({
    "zll": {
        "name": "zll",
        "id": 1,
        "label": r"$Z \rightarrow ll$",
        "br": const.br_z.clep,
    },
    "zqq": {
        "name": "zqq",
        "id": 2,
        "label": r"$Z \rightarrow qq$",
        "br": const.br_z.qq,
    },
    "znunu": {
        "name": "znunu",
        "id": 3,
        "label": r"$Z \rightarrow \nu\nu$",
        "br": const.br_z.nunu,
    },
})

w_decay_map = DotDict.wrap({
    "wlnu": {
        "name": "wlnu",
        "id": 4,
        "label": r"$W \rightarrow l\nu$",
        "br": const.br_w.lep,
    },
    "wqq": {
        "name": "wqq",
        "id": 5,
        "label": r"$W \rightarrow qq$",
        "br": const.br_w.had,
    },
})

####################################################################################################
#
# Single H (inclusive)
#
####################################################################################################

h = Process(
    name="h",
    id=10000,
    label=r"$H$",
)

# Higgs decay channels
h_htt = add_decay_process(h, h_decay_map.htt, add_production_mode_parent=False)
h_hww = add_decay_process(h, h_decay_map.hww, add_production_mode_parent=False)
h_hzz = add_decay_process(h, h_decay_map.hzz, add_production_mode_parent=False)
h_hbb = add_decay_process(h, h_decay_map.hbb, add_production_mode_parent=False)
h_hnonbb = add_decay_process(h, h_decay_map.hnonbb, add_production_mode_parent=False)
h_hcc = add_decay_process(h, h_decay_map.hcc, add_production_mode_parent=False)
h_hzg = add_decay_process(h, h_decay_map.hzg, add_production_mode_parent=False)
h_hgg = add_decay_process(h, h_decay_map.hgg, add_production_mode_parent=False)
h_hmm = add_decay_process(h, h_decay_map.hmm, add_production_mode_parent=False)

# Higgs sub-decay channels
h_hwwqqlnu = add_sub_decay_process(h_hww, ww_decay_map["qqlnu"], add_production_mode_parent=False)
h_hww2l2nu = add_sub_decay_process(h_hww, ww_decay_map["2l2nu"], add_production_mode_parent=False)
h_hww4q = add_sub_decay_process(h_hww, ww_decay_map["4q"], add_production_mode_parent=False)
h_hzz4l = add_sub_decay_process(h_hzz, zz_decay_map["4l"], add_production_mode_parent=False)
h_hzz2l2nu = add_sub_decay_process(h_hzz, zz_decay_map["2l2nu"], add_production_mode_parent=False)
h_hzz2l2q = add_sub_decay_process(h_hzz, zz_decay_map["2l2q"], add_production_mode_parent=False)
h_hzz2q2nu = add_sub_decay_process(h_hzz, zz_decay_map["2q2nu"], add_production_mode_parent=False)
h_hzz4nu = add_sub_decay_process(h_hzz, zz_decay_map["4nu"], add_production_mode_parent=False)
h_hzz4q = add_sub_decay_process(h_hzz, zz_decay_map["4q"], add_production_mode_parent=False)
h_hzg_zll = add_decay_process(h_hzg, hzg_decay_map["zll"], add_production_mode_parent=False)
h_hzg_zqq = add_decay_process(h_hzg, hzg_decay_map["zqq"], add_production_mode_parent=False)
h_hzg_znunu = add_decay_process(h_hzg, hzg_decay_map["znunu"], add_production_mode_parent=False)

####################################################################################################
#
# ggf (ggH)
#
####################################################################################################

h_ggf = h.add_process(
    name="h_ggf",
    id=11000,
    label=r"$H_{ggf}$",
    xsecs={
        13: Number(4.858E+01, {
            "pdf": 0.032j,
            "th": (0.046j, 0.067j),
            "th_gaussian": 0.039j,
        }),
        13.6: Number(52.23, {  # value for mH=125 GeV
            "pdf": 0.032j,
            "th": (0.046j, 0.067j),
            "th_gaussian": 0.039,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)

# Higgs decay channels
h_ggf_htt = add_decay_process(h_ggf, h_decay_map.htt)
h_ggf_hww = add_decay_process(h_ggf, h_decay_map.hww)
h_ggf_hzz = add_decay_process(h_ggf, h_decay_map.hzz)
h_ggf_hbb = add_decay_process(h_ggf, h_decay_map.hbb)
h_ggf_hnonbb = add_decay_process(h_ggf, h_decay_map.hnonbb)
h_ggf_hcc = add_decay_process(h_ggf, h_decay_map.hcc)
h_ggf_hzg = add_decay_process(h_ggf, h_decay_map.hzg)
h_ggf_hgg = add_decay_process(h_ggf, h_decay_map.hgg)
h_ggf_hmm = add_decay_process(h_ggf, h_decay_map.hmm)

# Higgs sub-decay channels
# TODO: mapping of parent processes does not yet work here
h_ggf_hwwqqlnu = add_sub_decay_process(h_ggf_hww, ww_decay_map["qqlnu"])
h_ggf_hww2l2nu = add_sub_decay_process(h_ggf_hww, ww_decay_map["2l2nu"])
h_ggf_hww4q = add_sub_decay_process(h_ggf_hww, ww_decay_map["4q"])
h_ggf_hzz4l = add_sub_decay_process(h_ggf_hzz, zz_decay_map["4l"])
h_ggf_hzz2l2nu = add_sub_decay_process(h_ggf_hzz, zz_decay_map["2l2nu"])
h_ggf_hzz2l2q = add_sub_decay_process(h_ggf_hzz, zz_decay_map["2l2q"])
h_ggf_hzz2q2nu = add_sub_decay_process(h_ggf_hzz, zz_decay_map["2q2nu"])
h_ggf_hzz4nu = add_sub_decay_process(h_ggf_hzz, zz_decay_map["4nu"])
h_ggf_hzz4q = add_sub_decay_process(h_ggf_hzz, zz_decay_map["4q"])
h_ggf_hzg_zll = add_decay_process(h_ggf_hzg, hzg_decay_map["zll"])
h_ggf_hzg_zqq = add_decay_process(h_ggf_hzg, hzg_decay_map["zqq"])
h_ggf_hzg_znunu = add_decay_process(h_ggf_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# vbf (qqH)
#
####################################################################################################

h_vbf = h.add_process(
    name="h_vbf",
    id=12000,
    label=r"$H_{vbf}$",
    xsecs={
        13: Number(3.782E+00, {
            "pdf": 0.021j,
            "scale": (0.004j, 0.003j),
        }),
        13.6: Number(4.078, {  # value for mH=125 GeV
            "scale": (0.005j, 0.003j),
            "pdf": 0.021j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)

# Higgs decay channels
h_vbf_htt = add_decay_process(h_vbf, h_decay_map.htt)
h_vbf_hww = add_decay_process(h_vbf, h_decay_map.hww)
h_vbf_hzz = add_decay_process(h_vbf, h_decay_map.hzz)
h_vbf_hbb = add_decay_process(h_vbf, h_decay_map.hbb)
h_vbf_hnonbb = add_decay_process(h_vbf, h_decay_map.hnonbb)
h_vbf_hcc = add_decay_process(h_vbf, h_decay_map.hcc)
h_vbf_hzg = add_decay_process(h_vbf, h_decay_map.hzg)
h_vbf_hgg = add_decay_process(h_vbf, h_decay_map.hgg)
h_vbf_hmm = add_decay_process(h_vbf, h_decay_map.hmm)

# Higgs sub-decay channels
h_vbf_hwwqqlnu = add_sub_decay_process(h_vbf_hww, ww_decay_map["qqlnu"])
h_vbf_hww2l2nu = add_sub_decay_process(h_vbf_hww, ww_decay_map["2l2nu"])
h_vbf_hww4q = add_sub_decay_process(h_vbf_hww, ww_decay_map["4q"])
h_vbf_hzz4l = add_sub_decay_process(h_vbf_hzz, zz_decay_map["4l"])
h_vbf_hzz2l2nu = add_sub_decay_process(h_vbf_hzz, zz_decay_map["2l2nu"])
h_vbf_hzz2l2q = add_sub_decay_process(h_vbf_hzz, zz_decay_map["2l2q"])
h_vbf_hzz2q2nu = add_sub_decay_process(h_vbf_hzz, zz_decay_map["2q2nu"])
h_vbf_hzz4nu = add_sub_decay_process(h_vbf_hzz, zz_decay_map["4nu"])
h_vbf_hzz4q = add_sub_decay_process(h_vbf_hzz, zz_decay_map["4q"])
h_vbf_hzg_zll = add_decay_process(h_vbf_hzg, hzg_decay_map["zll"])
h_vbf_hzg_zqq = add_decay_process(h_vbf_hzg, hzg_decay_map["zqq"])
h_vbf_hzg_znunu = add_decay_process(h_vbf_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# VH base process
#
####################################################################################################

# empty, no value given
vh = h.add_process(
    name="vh",
    id=13000,
    label="VH",
)

zh = vh.add_process(
    name="zh",
    id=14000,
    label="ZH",
    xsecs={
        13: Number(8.839E-01, {
            "scale": (0.038j, 0.031j),
            "pdf": 0.016j,
        }),
        13.6: Number(0.9439, {  # value for mH=125 GeV
            "scale": (0.037j, 0.032j),
            "pdf": 0.016j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": vh},
)

zh_gg = vh.add_process(
    name="zh_gg",
    id=15000,
    xsecs={
        13: Number(0.1227, {
            "scale": (0.251j, 0.189j),
            "pdf": 0.019j,
        }),
        13.6: Number(0.1360, {  # value for mH=125 GeV
            "scale": (0.037j, 0.032j),
            "pdf": 0.016j,
        }),  # TODO: only preliminary
        # unclear if error (originally for ZH) is also applicable here.
        # only in original presentation:
        # https://indico.cern.ch/event/1119741/contributions/4715908/attachments/2383849/4073592/YR4_13p6_VH_update.pdf  # noqa
    },
    label=r"$ZH_{gg}$",
    aux={"production_mode_parent": vh},
)

wh = vh.add_process(
    name="wh",
    label="WH",
    id=16000,
    aux={"production_mode_parent": vh},
)

wph = wh.add_process(
    name="wph",
    id=17000,
    label=r"$W^+H$",
    xsecs={
        13: Number(8.400E-01, {
            "pdf": 0.019j,
            "scale": (0.005j, 0.007j),
        }),
        13.6: Number(0.8889, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  # TODO: only preliminary
        # only in original presentation:
        # https://indico.cern.ch/event/1119741/contributions/4715908/attachments/2383849/4073592/YR4_13p6_VH_update.pdf  # noqa
    },
    aux={"production_mode_parent": wh},
)

wmh = wh.add_process(
    name="wmh",
    id=18000,
    label=r"$W^-H$",
    xsecs={
        13: Number(5.328E-01, {
            "pdf": 0.019j,
            "scale": (0.005j, 0.007j),
        }),
        13.6: Number(0.5677, {  # value for mH=125 GeV
            "scale": (0.004j, 0.007j),
            "pdf": 0.018j,
        }),  # TODO: only preliminary
        # only in original presentation:
        # https://indico.cern.ch/event/1119741/contributions/4715908/attachments/2383849/4073592/YR4_13p6_VH_update.pdf  # noqa
    },
    aux={"production_mode_parent": wh},
)

vh.xsecs = add_xsecs(zh, wph, wmh)


####################################################################################################
#
# VH subprocesses
#
####################################################################################################


# Higgs decay channels
vh_htt = add_decay_process(vh, h_decay_map.htt)
vh_hww = add_decay_process(vh, h_decay_map.hww)
vh_hzz = add_decay_process(vh, h_decay_map.hzz)
vh_hbb = add_decay_process(vh, h_decay_map.hbb)
vh_hnonbb = add_decay_process(vh, h_decay_map.hnonbb)
vh_hcc = add_decay_process(vh, h_decay_map.hcc)
vh_hzg = add_decay_process(vh, h_decay_map.hzg)
vh_hgg = add_decay_process(vh, h_decay_map.hgg)
vh_hmm = add_decay_process(vh, h_decay_map.hmm)

# Higgs sub-decay channels
vh_hwwqqlnu = add_sub_decay_process(vh_hww, ww_decay_map["qqlnu"])
vh_hww2l2nu = add_sub_decay_process(vh_hww, ww_decay_map["2l2nu"])
vh_hww4q = add_sub_decay_process(vh_hww, ww_decay_map["4q"])
vh_hzz4l = add_sub_decay_process(vh_hzz, zz_decay_map["4l"])
vh_hzz2l2nu = add_sub_decay_process(vh_hzz, zz_decay_map["2l2nu"])
vh_hzz2l2q = add_sub_decay_process(vh_hzz, zz_decay_map["2l2q"])
vh_hzz2q2nu = add_sub_decay_process(vh_hzz, zz_decay_map["2q2nu"])
vh_hzz4nu = add_sub_decay_process(vh_hzz, zz_decay_map["4nu"])
vh_hzz4q = add_sub_decay_process(vh_hzz, zz_decay_map["4q"])
vh_hzg_zll = add_decay_process(vh_hzg, hzg_decay_map["zll"])
vh_hzg_zqq = add_decay_process(vh_hzg, hzg_decay_map["zqq"])
vh_hzg_znunu = add_decay_process(vh_hzg, hzg_decay_map["znunu"])

vh_zll = add_decay_process(vh, z_decay_map.zll, add_production_mode_parent=False)

# Higgs decay channels
vh_zll_htt = add_decay_process(vh_zll, h_decay_map.htt)
vh_zll_hww = add_decay_process(vh_zll, h_decay_map.hww)
vh_zll_hzz = add_decay_process(vh_zll, h_decay_map.hzz)
vh_zll_hbb = add_decay_process(vh_zll, h_decay_map.hbb)
vh_zll_hnonbb = add_decay_process(vh_zll, h_decay_map.hnonbb)
vh_zll_hcc = add_decay_process(vh_zll, h_decay_map.hcc)
vh_zll_hzg = add_decay_process(vh_zll, h_decay_map.hzg)
vh_zll_hgg = add_decay_process(vh_zll, h_decay_map.hgg)
vh_zll_hmm = add_decay_process(vh_zll, h_decay_map.hmm)

# Higgs sub-decay channels
vh_zll_hwwqqlnu = add_sub_decay_process(vh_zll_hww, ww_decay_map["qqlnu"])
vh_zll_hww2l2nu = add_sub_decay_process(vh_zll_hww, ww_decay_map["2l2nu"])
vh_zll_hww4q = add_sub_decay_process(vh_zll_hww, ww_decay_map["4q"])
vh_zll_hzz4l = add_sub_decay_process(vh_zll_hzz, zz_decay_map["4l"])
vh_zll_hzz2l2nu = add_sub_decay_process(vh_zll_hzz, zz_decay_map["2l2nu"])
vh_zll_hzz2l2q = add_sub_decay_process(vh_zll_hzz, zz_decay_map["2l2q"])
vh_zll_hzz2q2nu = add_sub_decay_process(vh_zll_hzz, zz_decay_map["2q2nu"])
vh_zll_hzz4nu = add_sub_decay_process(vh_zll_hzz, zz_decay_map["4nu"])
vh_zll_hzz4q = add_sub_decay_process(vh_zll_hzz, zz_decay_map["4q"])
vh_zll_hzg_zll = add_decay_process(vh_zll_hzg, hzg_decay_map["zll"])
vh_zll_hzg_zqq = add_decay_process(vh_zll_hzg, hzg_decay_map["zqq"])
vh_zll_hzg_znunu = add_decay_process(vh_zll_hzg, hzg_decay_map["znunu"])

vh_zqq = add_decay_process(vh, z_decay_map.zqq, add_production_mode_parent=False)

# Higgs decay channels
vh_zqq_htt = add_decay_process(vh_zqq, h_decay_map.htt)
vh_zqq_hww = add_decay_process(vh_zqq, h_decay_map.hww)
vh_zqq_hzz = add_decay_process(vh_zqq, h_decay_map.hzz)
vh_zqq_hbb = add_decay_process(vh_zqq, h_decay_map.hbb)
vh_zqq_hnonbb = add_decay_process(vh_zqq, h_decay_map.hnonbb)
vh_zqq_hcc = add_decay_process(vh_zqq, h_decay_map.hcc)
vh_zqq_hzg = add_decay_process(vh_zqq, h_decay_map.hzg)
vh_zqq_hgg = add_decay_process(vh_zqq, h_decay_map.hgg)
vh_zqq_hmm = add_decay_process(vh_zqq, h_decay_map.hmm)

# Higgs sub-decay channels
vh_zqq_hwwqqlnu = add_sub_decay_process(vh_zqq_hww, ww_decay_map["qqlnu"])
vh_zqq_hww2l2nu = add_sub_decay_process(vh_zqq_hww, ww_decay_map["2l2nu"])
vh_zqq_hww4q = add_sub_decay_process(vh_zqq_hww, ww_decay_map["4q"])
vh_zqq_hzz4l = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["4l"])
vh_zqq_hzz2l2nu = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["2l2nu"])
vh_zqq_hzz2l2q = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["2l2q"])
vh_zqq_hzz2q2nu = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["2q2nu"])
vh_zqq_hzz4nu = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["4nu"])
vh_zqq_hzz4q = add_sub_decay_process(vh_zqq_hzz, zz_decay_map["4q"])
vh_zqq_hzg_zll = add_decay_process(vh_zqq_hzg, hzg_decay_map["zll"])
vh_zqq_hzg_zqq = add_decay_process(vh_zqq_hzg, hzg_decay_map["zqq"])
vh_zqq_hzg_znunu = add_decay_process(vh_zqq_hzg, hzg_decay_map["znunu"])

vh_znunu = add_decay_process(vh, z_decay_map.znunu, add_production_mode_parent=False)

# Higgs decay channels
vh_znunu_htt = add_decay_process(vh_znunu, h_decay_map.htt)
vh_znunu_hww = add_decay_process(vh_znunu, h_decay_map.hww)
vh_znunu_hzz = add_decay_process(vh_znunu, h_decay_map.hzz)
vh_znunu_hbb = add_decay_process(vh_znunu, h_decay_map.hbb)
vh_znunu_hnonbb = add_decay_process(vh_znunu, h_decay_map.hnonbb)
vh_znunu_hcc = add_decay_process(vh_znunu, h_decay_map.hcc)
vh_znunu_hzg = add_decay_process(vh_znunu, h_decay_map.hzg)
vh_znunu_hgg = add_decay_process(vh_znunu, h_decay_map.hgg)
vh_znunu_hmm = add_decay_process(vh_znunu, h_decay_map.hmm)

# Higgs sub-decay channels
vh_znunu_hwwqqlnu = add_sub_decay_process(vh_znunu_hww, ww_decay_map["qqlnu"])
vh_znunu_hww2l2nu = add_sub_decay_process(vh_znunu_hww, ww_decay_map["2l2nu"])
vh_znunu_hww4q = add_sub_decay_process(vh_znunu_hww, ww_decay_map["4q"])
vh_znunu_hzz4l = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["4l"])
vh_znunu_hzz2l2nu = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["2l2nu"])
vh_znunu_hzz2l2q = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["2l2q"])
vh_znunu_hzz2q2nu = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["2q2nu"])
vh_znunu_hzz4nu = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["4nu"])
vh_znunu_hzz4q = add_sub_decay_process(vh_znunu_hzz, zz_decay_map["4q"])
vh_znunu_hzg_zll = add_decay_process(vh_znunu_hzg, hzg_decay_map["zll"])
vh_znunu_hzg_zqq = add_decay_process(vh_znunu_hzg, hzg_decay_map["zqq"])
vh_znunu_hzg_znunu = add_decay_process(vh_znunu_hzg, hzg_decay_map["znunu"])

vh_wlnu = add_decay_process(vh, w_decay_map.wlnu, add_production_mode_parent=False)

# Higgs decay channels
vh_wlnu_htt = add_decay_process(vh_wlnu, h_decay_map.htt)
vh_wlnu_hww = add_decay_process(vh_wlnu, h_decay_map.hww)
vh_wlnu_hzz = add_decay_process(vh_wlnu, h_decay_map.hzz)
vh_wlnu_hbb = add_decay_process(vh_wlnu, h_decay_map.hbb)
vh_wlnu_hnonbb = add_decay_process(vh_wlnu, h_decay_map.hnonbb)
vh_wlnu_hcc = add_decay_process(vh_wlnu, h_decay_map.hcc)
vh_wlnu_hzg = add_decay_process(vh_wlnu, h_decay_map.hzg)
vh_wlnu_hgg = add_decay_process(vh_wlnu, h_decay_map.hgg)
vh_wlnu_hmm = add_decay_process(vh_wlnu, h_decay_map.hmm)

# Higgs sub-decay channels
vh_wlnu_hwwqqlnu = add_sub_decay_process(vh_wlnu_hww, ww_decay_map["qqlnu"])
vh_wlnu_hww2l2nu = add_sub_decay_process(vh_wlnu_hww, ww_decay_map["2l2nu"])
vh_wlnu_hww4q = add_sub_decay_process(vh_wlnu_hww, ww_decay_map["4q"])
vh_wlnu_hzz4l = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["4l"])
vh_wlnu_hzz2l2nu = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["2l2nu"])
vh_wlnu_hzz2l2q = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["2l2q"])
vh_wlnu_hzz2q2nu = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["2q2nu"])
vh_wlnu_hzz4nu = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["4nu"])
vh_wlnu_hzz4q = add_sub_decay_process(vh_wlnu_hzz, zz_decay_map["4q"])
vh_wlnu_hzg_zll = add_decay_process(vh_wlnu_hzg, hzg_decay_map["zll"])
vh_wlnu_hzg_zqq = add_decay_process(vh_wlnu_hzg, hzg_decay_map["zqq"])
vh_wlnu_hzg_znunu = add_decay_process(vh_wlnu_hzg, hzg_decay_map["znunu"])

vh_wqq = add_decay_process(vh, w_decay_map.wqq, add_production_mode_parent=False)

# Higgs decay channels
vh_wqq_htt = add_decay_process(vh_wqq, h_decay_map.htt)
vh_wqq_hww = add_decay_process(vh_wqq, h_decay_map.hww)
vh_wqq_hzz = add_decay_process(vh_wqq, h_decay_map.hzz)
vh_wqq_hbb = add_decay_process(vh_wqq, h_decay_map.hbb)
vh_wqq_hnonbb = add_decay_process(vh_wqq, h_decay_map.hnonbb)
vh_wqq_hcc = add_decay_process(vh_wqq, h_decay_map.hcc)
vh_wqq_hzg = add_decay_process(vh_wqq, h_decay_map.hzg)
vh_wqq_hgg = add_decay_process(vh_wqq, h_decay_map.hgg)
vh_wqq_hmm = add_decay_process(vh_wqq, h_decay_map.hmm)

# Higgs sub-decay channels
vh_wqq_hwwqqlnu = add_sub_decay_process(vh_wqq_hww, ww_decay_map["qqlnu"])
vh_wqq_hww2l2nu = add_sub_decay_process(vh_wqq_hww, ww_decay_map["2l2nu"])
vh_wqq_hww4q = add_sub_decay_process(vh_wqq_hww, ww_decay_map["4q"])
vh_wqq_hzz4l = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["4l"])
vh_wqq_hzz2l2nu = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["2l2nu"])
vh_wqq_hzz2l2q = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["2l2q"])
vh_wqq_hzz2q2nu = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["2q2nu"])
vh_wqq_hzz4nu = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["4nu"])
vh_wqq_hzz4q = add_sub_decay_process(vh_wqq_hzz, zz_decay_map["4q"])
vh_wqq_hzg_zll = add_decay_process(vh_wqq_hzg, hzg_decay_map["zll"])
vh_wqq_hzg_zqq = add_decay_process(vh_wqq_hzg, hzg_decay_map["zqq"])
vh_wqq_hzg_znunu = add_decay_process(vh_wqq_hzg, hzg_decay_map["znunu"])


####################################################################################################
#
# ZH subprocesses
#
####################################################################################################

# Higgs decay channels
zh_htt = add_decay_process(zh, h_decay_map.htt)
zh_hww = add_decay_process(zh, h_decay_map.hww)
zh_hzz = add_decay_process(zh, h_decay_map.hzz)
zh_hbb = add_decay_process(zh, h_decay_map.hbb)
zh_hnonbb = add_decay_process(zh, h_decay_map.hnonbb)
zh_hcc = add_decay_process(zh, h_decay_map.hcc)
zh_hzg = add_decay_process(zh, h_decay_map.hzg)
zh_hgg = add_decay_process(zh, h_decay_map.hgg)
zh_hmm = add_decay_process(zh, h_decay_map.hmm)

# Higgs sub-decay channels
zh_hwwqqlnu = add_sub_decay_process(zh_hww, ww_decay_map["qqlnu"])
zh_hww2l2nu = add_sub_decay_process(zh_hww, ww_decay_map["2l2nu"])
zh_hww4q = add_sub_decay_process(zh_hww, ww_decay_map["4q"])
zh_hzz4l = add_sub_decay_process(zh_hzz, zz_decay_map["4l"])
zh_hzz2l2nu = add_sub_decay_process(zh_hzz, zz_decay_map["2l2nu"])
zh_hzz2l2q = add_sub_decay_process(zh_hzz, zz_decay_map["2l2q"])
zh_hzz2q2nu = add_sub_decay_process(zh_hzz, zz_decay_map["2q2nu"])
zh_hzz4nu = add_sub_decay_process(zh_hzz, zz_decay_map["4nu"])
zh_hzz4q = add_sub_decay_process(zh_hzz, zz_decay_map["4q"])
zh_hzg_zll = add_decay_process(zh_hzg, hzg_decay_map["zll"])
zh_hzg_zqq = add_decay_process(zh_hzg, hzg_decay_map["zqq"])
zh_hzg_znunu = add_decay_process(zh_hzg, hzg_decay_map["znunu"])

zh_zll = add_decay_process(zh, z_decay_map.zll)

# Higgs decay channels
zh_zll_htt = add_decay_process(zh_zll, h_decay_map.htt)
zh_zll_hww = add_decay_process(zh_zll, h_decay_map.hww)
zh_zll_hzz = add_decay_process(zh_zll, h_decay_map.hzz)
zh_zll_hbb = add_decay_process(zh_zll, h_decay_map.hbb)
zh_zll_hnonbb = add_decay_process(zh_zll, h_decay_map.hnonbb)
zh_zll_hcc = add_decay_process(zh_zll, h_decay_map.hcc)
zh_zll_hzg = add_decay_process(zh_zll, h_decay_map.hzg)
zh_zll_hgg = add_decay_process(zh_zll, h_decay_map.hgg)
zh_zll_hmm = add_decay_process(zh_zll, h_decay_map.hmm)

# Higgs sub-decay channels
zh_zll_hwwqqlnu = add_sub_decay_process(zh_zll_hww, ww_decay_map["qqlnu"])
zh_zll_hww2l2nu = add_sub_decay_process(zh_zll_hww, ww_decay_map["2l2nu"])
zh_zll_hww4q = add_sub_decay_process(zh_zll_hww, ww_decay_map["4q"])
zh_zll_hzz4l = add_sub_decay_process(zh_zll_hzz, zz_decay_map["4l"])
zh_zll_hzz2l2nu = add_sub_decay_process(zh_zll_hzz, zz_decay_map["2l2nu"])
zh_zll_hzz2l2q = add_sub_decay_process(zh_zll_hzz, zz_decay_map["2l2q"])
zh_zll_hzz2q2nu = add_sub_decay_process(zh_zll_hzz, zz_decay_map["2q2nu"])
zh_zll_hzz4nu = add_sub_decay_process(zh_zll_hzz, zz_decay_map["4nu"])
zh_zll_hzz4q = add_sub_decay_process(zh_zll_hzz, zz_decay_map["4q"])
zh_zll_hzg_zll = add_decay_process(zh_zll_hzg, hzg_decay_map["zll"])
zh_zll_hzg_zqq = add_decay_process(zh_zll_hzg, hzg_decay_map["zqq"])
zh_zll_hzg_znunu = add_decay_process(zh_zll_hzg, hzg_decay_map["znunu"])

zh_zqq = add_decay_process(zh, z_decay_map.zqq)

# Higgs decay channels
zh_zqq_htt = add_decay_process(zh_zqq, h_decay_map.htt)
zh_zqq_hww = add_decay_process(zh_zqq, h_decay_map.hww)
zh_zqq_hzz = add_decay_process(zh_zqq, h_decay_map.hzz)
zh_zqq_hbb = add_decay_process(zh_zqq, h_decay_map.hbb)
zh_zqq_hnonbb = add_decay_process(zh_zqq, h_decay_map.hnonbb)
zh_zqq_hcc = add_decay_process(zh_zqq, h_decay_map.hcc)
zh_zqq_hzg = add_decay_process(zh_zqq, h_decay_map.hzg)
zh_zqq_hgg = add_decay_process(zh_zqq, h_decay_map.hgg)
zh_zqq_hmm = add_decay_process(zh_zqq, h_decay_map.hmm)

# Higgs sub-decay channels
zh_zqq_hwwqqlnu = add_sub_decay_process(zh_zqq_hww, ww_decay_map["qqlnu"])
zh_zqq_hww2l2nu = add_sub_decay_process(zh_zqq_hww, ww_decay_map["2l2nu"])
zh_zqq_hww4q = add_sub_decay_process(zh_zqq_hww, ww_decay_map["4q"])
zh_zqq_hzz4l = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["4l"])
zh_zqq_hzz2l2nu = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["2l2nu"])
zh_zqq_hzz2l2q = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["2l2q"])
zh_zqq_hzz2q2nu = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["2q2nu"])
zh_zqq_hzz4nu = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["4nu"])
zh_zqq_hzz4q = add_sub_decay_process(zh_zqq_hzz, zz_decay_map["4q"])
zh_zqq_hzg_zll = add_decay_process(zh_zqq_hzg, hzg_decay_map["zll"])
zh_zqq_hzg_zqq = add_decay_process(zh_zqq_hzg, hzg_decay_map["zqq"])
zh_zqq_hzg_znunu = add_decay_process(zh_zqq_hzg, hzg_decay_map["znunu"])

zh_znunu = add_decay_process(zh, z_decay_map.znunu)

# Higgs decay channels
zh_znunu_htt = add_decay_process(zh_znunu, h_decay_map.htt)
zh_znunu_hww = add_decay_process(zh_znunu, h_decay_map.hww)
zh_znunu_hzz = add_decay_process(zh_znunu, h_decay_map.hzz)
zh_znunu_hbb = add_decay_process(zh_znunu, h_decay_map.hbb)
zh_znunu_hnonbb = add_decay_process(zh_znunu, h_decay_map.hnonbb)
zh_znunu_hcc = add_decay_process(zh_znunu, h_decay_map.hcc)
zh_znunu_hzg = add_decay_process(zh_znunu, h_decay_map.hzg)
zh_znunu_hgg = add_decay_process(zh_znunu, h_decay_map.hgg)
zh_znunu_hmm = add_decay_process(zh_znunu, h_decay_map.hmm)

# Higgs sub-decay channels
zh_znunu_hwwqqlnu = add_sub_decay_process(zh_znunu_hww, ww_decay_map["qqlnu"])
zh_znunu_hww2l2nu = add_sub_decay_process(zh_znunu_hww, ww_decay_map["2l2nu"])
zh_znunu_hww4q = add_sub_decay_process(zh_znunu_hww, ww_decay_map["4q"])
zh_znunu_hzz4l = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["4l"])
zh_znunu_hzz2l2nu = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["2l2nu"])
zh_znunu_hzz2l2q = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["2l2q"])
zh_znunu_hzz2q2nu = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["2q2nu"])
zh_znunu_hzz4nu = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["4nu"])
zh_znunu_hzz4q = add_sub_decay_process(zh_znunu_hzz, zz_decay_map["4q"])
zh_znunu_hzg_zll = add_decay_process(zh_znunu_hzg, hzg_decay_map["zll"])
zh_znunu_hzg_zqq = add_decay_process(zh_znunu_hzg, hzg_decay_map["zqq"])
zh_znunu_hzg_znunu = add_decay_process(zh_znunu_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# ggZH subprocesses
#
####################################################################################################

# Higgs decay channels
zh_gg_htt = add_decay_process(zh_gg, h_decay_map.htt)
zh_gg_hww = add_decay_process(zh_gg, h_decay_map.hww)
zh_gg_hzz = add_decay_process(zh_gg, h_decay_map.hzz)
zh_gg_hbb = add_decay_process(zh_gg, h_decay_map.hbb)
zh_gg_hnonbb = add_decay_process(zh_gg, h_decay_map.hnonbb)
zh_gg_hcc = add_decay_process(zh_gg, h_decay_map.hcc)
zh_gg_hzg = add_decay_process(zh_gg, h_decay_map.hzg)
zh_gg_hgg = add_decay_process(zh_gg, h_decay_map.hgg)
zh_gg_hmm = add_decay_process(zh_gg, h_decay_map.hmm)

# Higgs sub-decay channels
zh_gg_hwwqqlnu = add_sub_decay_process(zh_gg_hww, ww_decay_map["qqlnu"])
zh_gg_hww2l2nu = add_sub_decay_process(zh_gg_hww, ww_decay_map["2l2nu"])
zh_gg_hww4q = add_sub_decay_process(zh_gg_hww, ww_decay_map["4q"])
zh_gg_hzz4l = add_sub_decay_process(zh_gg_hzz, zz_decay_map["4l"])
zh_gg_hzz2l2nu = add_sub_decay_process(zh_gg_hzz, zz_decay_map["2l2nu"])
zh_gg_hzz2l2q = add_sub_decay_process(zh_gg_hzz, zz_decay_map["2l2q"])
zh_gg_hzz2q2nu = add_sub_decay_process(zh_gg_hzz, zz_decay_map["2q2nu"])
zh_gg_hzz4nu = add_sub_decay_process(zh_gg_hzz, zz_decay_map["4nu"])
zh_gg_hzz4q = add_sub_decay_process(zh_gg_hzz, zz_decay_map["4q"])
zh_gg_hzg_zll = add_decay_process(zh_gg_hzg, hzg_decay_map["zll"])
zh_gg_hzg_zqq = add_decay_process(zh_gg_hzg, hzg_decay_map["zqq"])
zh_gg_hzg_znunu = add_decay_process(zh_gg_hzg, hzg_decay_map["znunu"])

zh_gg_zll = add_decay_process(zh_gg, z_decay_map.zll)

# Higgs decay channels
zh_gg_zll_htt = add_decay_process(zh_gg_zll, h_decay_map.htt)
zh_gg_zll_hww = add_decay_process(zh_gg_zll, h_decay_map.hww)
zh_gg_zll_hzz = add_decay_process(zh_gg_zll, h_decay_map.hzz)
zh_gg_zll_hbb = add_decay_process(zh_gg_zll, h_decay_map.hbb)
zh_gg_zll_hnonbb = add_decay_process(zh_gg_zll, h_decay_map.hnonbb)
zh_gg_zll_hcc = add_decay_process(zh_gg_zll, h_decay_map.hcc)
zh_gg_zll_hzg = add_decay_process(zh_gg_zll, h_decay_map.hzg)
zh_gg_zll_hgg = add_decay_process(zh_gg_zll, h_decay_map.hgg)
zh_gg_zll_hmm = add_decay_process(zh_gg_zll, h_decay_map.hmm)

# Higgs sub-decay channels
zh_gg_zll_hwwqqlnu = add_sub_decay_process(zh_gg_zll_hww, ww_decay_map["qqlnu"])
zh_gg_zll_hww2l2nu = add_sub_decay_process(zh_gg_zll_hww, ww_decay_map["2l2nu"])
zh_gg_zll_hww4q = add_sub_decay_process(zh_gg_zll_hww, ww_decay_map["4q"])
zh_gg_zll_hzz4l = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["4l"])
zh_gg_zll_hzz2l2nu = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["2l2nu"])
zh_gg_zll_hzz2l2q = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["2l2q"])
zh_gg_zll_hzz2q2nu = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["2q2nu"])
zh_gg_zll_hzz4nu = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["4nu"])
zh_gg_zll_hzz4q = add_sub_decay_process(zh_gg_zll_hzz, zz_decay_map["4q"])
zh_gg_zll_hzg_zll = add_decay_process(zh_gg_zll_hzg, hzg_decay_map["zll"])
zh_gg_zll_hzg_zqq = add_decay_process(zh_gg_zll_hzg, hzg_decay_map["zqq"])
zh_gg_zll_hzg_znunu = add_decay_process(zh_gg_zll_hzg, hzg_decay_map["znunu"])

zh_gg_zqq = add_decay_process(zh_gg, z_decay_map.zqq)

# Higgs decay channels
zh_gg_zqq_htt = add_decay_process(zh_gg_zqq, h_decay_map.htt)
zh_gg_zqq_hww = add_decay_process(zh_gg_zqq, h_decay_map.hww)
zh_gg_zqq_hzz = add_decay_process(zh_gg_zqq, h_decay_map.hzz)
zh_gg_zqq_hbb = add_decay_process(zh_gg_zqq, h_decay_map.hbb)
zh_gg_zqq_hnonbb = add_decay_process(zh_gg_zqq, h_decay_map.hnonbb)
zh_gg_zqq_hcc = add_decay_process(zh_gg_zqq, h_decay_map.hcc)
zh_gg_zqq_hzg = add_decay_process(zh_gg_zqq, h_decay_map.hzg)
zh_gg_zqq_hgg = add_decay_process(zh_gg_zqq, h_decay_map.hgg)
zh_gg_zqq_hmm = add_decay_process(zh_gg_zqq, h_decay_map.hmm)

# Higgs sub-decay channels
zh_gg_zqq_hwwqqlnu = add_sub_decay_process(zh_gg_zqq_hww, ww_decay_map["qqlnu"])
zh_gg_zqq_hww2l2nu = add_sub_decay_process(zh_gg_zqq_hww, ww_decay_map["2l2nu"])
zh_gg_zqq_hww4q = add_sub_decay_process(zh_gg_zqq_hww, ww_decay_map["4q"])
zh_gg_zqq_hzz4l = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["4l"])
zh_gg_zqq_hzz2l2nu = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["2l2nu"])
zh_gg_zqq_hzz2l2q = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["2l2q"])
zh_gg_zqq_hzz2q2nu = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["2q2nu"])
zh_gg_zqq_hzz4nu = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["4nu"])
zh_gg_zqq_hzz4q = add_sub_decay_process(zh_gg_zqq_hzz, zz_decay_map["4q"])
zh_gg_zqq_hzg_zll = add_decay_process(zh_gg_zqq_hzg, hzg_decay_map["zll"])
zh_gg_zqq_hzg_zqq = add_decay_process(zh_gg_zqq_hzg, hzg_decay_map["zqq"])
zh_gg_zqq_hzg_znunu = add_decay_process(zh_gg_zqq_hzg, hzg_decay_map["znunu"])

zh_gg_znunu = add_decay_process(zh_gg, z_decay_map.znunu)

# Higgs decay channels
zh_gg_znunu_htt = add_decay_process(zh_gg_znunu, h_decay_map.htt)
zh_gg_znunu_hww = add_decay_process(zh_gg_znunu, h_decay_map.hww)
zh_gg_znunu_hzz = add_decay_process(zh_gg_znunu, h_decay_map.hzz)
zh_gg_znunu_hbb = add_decay_process(zh_gg_znunu, h_decay_map.hbb)
zh_gg_znunu_hnonbb = add_decay_process(zh_gg_znunu, h_decay_map.hnonbb)
zh_gg_znunu_hcc = add_decay_process(zh_gg_znunu, h_decay_map.hcc)
zh_gg_znunu_hzg = add_decay_process(zh_gg_znunu, h_decay_map.hzg)
zh_gg_znunu_hgg = add_decay_process(zh_gg_znunu, h_decay_map.hgg)
zh_gg_znunu_hmm = add_decay_process(zh_gg_znunu, h_decay_map.hmm)

# Higgs sub-decay channels
zh_gg_znunu_hwwqqlnu = add_sub_decay_process(zh_gg_znunu_hww, ww_decay_map["qqlnu"])
zh_gg_znunu_hww2l2nu = add_sub_decay_process(zh_gg_znunu_hww, ww_decay_map["2l2nu"])
zh_gg_znunu_hww4q = add_sub_decay_process(zh_gg_znunu_hww, ww_decay_map["4q"])
zh_gg_znunu_hzz4l = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["4l"])
zh_gg_znunu_hzz2l2nu = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["2l2nu"])
zh_gg_znunu_hzz2l2q = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["2l2q"])
zh_gg_znunu_hzz2q2nu = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["2q2nu"])
zh_gg_znunu_hzz4nu = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["4nu"])
zh_gg_znunu_hzz4q = add_sub_decay_process(zh_gg_znunu_hzz, zz_decay_map["4q"])
zh_gg_znunu_hzg_zll = add_decay_process(zh_gg_znunu_hzg, hzg_decay_map["zll"])
zh_gg_znunu_hzg_zqq = add_decay_process(zh_gg_znunu_hzg, hzg_decay_map["zqq"])
zh_gg_znunu_hzg_znunu = add_decay_process(zh_gg_znunu_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# WH subprocesses
#
####################################################################################################

# Higgs decay channels
wh_htt = add_decay_process(wh, h_decay_map.htt)
wh_hww = add_decay_process(wh, h_decay_map.hww)
wh_hzz = add_decay_process(wh, h_decay_map.hzz)
wh_hbb = add_decay_process(wh, h_decay_map.hbb)
wh_hnonbb = add_decay_process(wh, h_decay_map.hnonbb)
wh_hcc = add_decay_process(wh, h_decay_map.hcc)
wh_hzg = add_decay_process(wh, h_decay_map.hzg)
wh_hgg = add_decay_process(wh, h_decay_map.hgg)
wh_hmm = add_decay_process(wh, h_decay_map.hmm)

# Higgs sub-decay channels
wh_hwwqqlnu = add_sub_decay_process(wh_hww, ww_decay_map["qqlnu"])
wh_hww2l2nu = add_sub_decay_process(wh_hww, ww_decay_map["2l2nu"])
wh_hww4q = add_sub_decay_process(wh_hww, ww_decay_map["4q"])
wh_hzz4l = add_sub_decay_process(wh_hzz, zz_decay_map["4l"])
wh_hzz2l2nu = add_sub_decay_process(wh_hzz, zz_decay_map["2l2nu"])
wh_hzz2l2q = add_sub_decay_process(wh_hzz, zz_decay_map["2l2q"])
wh_hzz2q2nu = add_sub_decay_process(wh_hzz, zz_decay_map["2q2nu"])
wh_hzz4nu = add_sub_decay_process(wh_hzz, zz_decay_map["4nu"])
wh_hzz4q = add_sub_decay_process(wh_hzz, zz_decay_map["4q"])
wh_hzg_zll = add_decay_process(wh_hzg, hzg_decay_map["zll"])
wh_hzg_zqq = add_decay_process(wh_hzg, hzg_decay_map["zqq"])
wh_hzg_znunu = add_decay_process(wh_hzg, hzg_decay_map["znunu"])

wh_wlnu = add_decay_process(wh, w_decay_map.wlnu)

# Higgs decay channels
wh_wlnu_htt = add_decay_process(wh_wlnu, h_decay_map.htt)
wh_wlnu_hww = add_decay_process(wh_wlnu, h_decay_map.hww)
wh_wlnu_hzz = add_decay_process(wh_wlnu, h_decay_map.hzz)
wh_wlnu_hbb = add_decay_process(wh_wlnu, h_decay_map.hbb)
wh_wlnu_hnonbb = add_decay_process(wh_wlnu, h_decay_map.hnonbb)
wh_wlnu_hcc = add_decay_process(wh_wlnu, h_decay_map.hcc)
wh_wlnu_hzg = add_decay_process(wh_wlnu, h_decay_map.hzg)
wh_wlnu_hgg = add_decay_process(wh_wlnu, h_decay_map.hgg)
wh_wlnu_hmm = add_decay_process(wh_wlnu, h_decay_map.hmm)

# Higgs sub-decay channels
wh_wlnu_hwwqqlnu = add_sub_decay_process(wh_wlnu_hww, ww_decay_map["qqlnu"])
wh_wlnu_hww2l2nu = add_sub_decay_process(wh_wlnu_hww, ww_decay_map["2l2nu"])
wh_wlnu_hww4q = add_sub_decay_process(wh_wlnu_hww, ww_decay_map["4q"])
wh_wlnu_hzz4l = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["4l"])
wh_wlnu_hzz2l2nu = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["2l2nu"])
wh_wlnu_hzz2l2q = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["2l2q"])
wh_wlnu_hzz2q2nu = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["2q2nu"])
wh_wlnu_hzz4nu = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["4nu"])
wh_wlnu_hzz4q = add_sub_decay_process(wh_wlnu_hzz, zz_decay_map["4q"])
wh_wlnu_hzg_zll = add_decay_process(wh_wlnu_hzg, hzg_decay_map["zll"])
wh_wlnu_hzg_zqq = add_decay_process(wh_wlnu_hzg, hzg_decay_map["zqq"])
wh_wlnu_hzg_znunu = add_decay_process(wh_wlnu_hzg, hzg_decay_map["znunu"])

wh_wqq = add_decay_process(wh, w_decay_map.wqq)

# Higgs decay channels
wh_wqq_htt = add_decay_process(wh_wqq, h_decay_map.htt)
wh_wqq_hww = add_decay_process(wh_wqq, h_decay_map.hww)
wh_wqq_hzz = add_decay_process(wh_wqq, h_decay_map.hzz)
wh_wqq_hbb = add_decay_process(wh_wqq, h_decay_map.hbb)
wh_wqq_hnonbb = add_decay_process(wh_wqq, h_decay_map.hnonbb)
wh_wqq_hcc = add_decay_process(wh_wqq, h_decay_map.hcc)
wh_wqq_hzg = add_decay_process(wh_wqq, h_decay_map.hzg)
wh_wqq_hgg = add_decay_process(wh_wqq, h_decay_map.hgg)
wh_wqq_hmm = add_decay_process(wh_wqq, h_decay_map.hmm)

# Higgs sub-decay channels
wh_wqq_hwwqqlnu = add_sub_decay_process(wh_wqq_hww, ww_decay_map["qqlnu"])
wh_wqq_hww2l2nu = add_sub_decay_process(wh_wqq_hww, ww_decay_map["2l2nu"])
wh_wqq_hww4q = add_sub_decay_process(wh_wqq_hww, ww_decay_map["4q"])
wh_wqq_hzz4l = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["4l"])
wh_wqq_hzz2l2nu = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["2l2nu"])
wh_wqq_hzz2l2q = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["2l2q"])
wh_wqq_hzz2q2nu = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["2q2nu"])
wh_wqq_hzz4nu = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["4nu"])
wh_wqq_hzz4q = add_sub_decay_process(wh_wqq_hzz, zz_decay_map["4q"])
wh_wqq_hzg_zll = add_decay_process(wh_wqq_hzg, hzg_decay_map["zll"])
wh_wqq_hzg_zqq = add_decay_process(wh_wqq_hzg, hzg_decay_map["zqq"])
wh_wqq_hzg_znunu = add_decay_process(wh_wqq_hzg, hzg_decay_map["znunu"])


####################################################################################################
#
# W+ H subprocesses
#
####################################################################################################

# Higgs decay channels
wph_htt = add_decay_process(wph, h_decay_map.htt)
wph_hww = add_decay_process(wph, h_decay_map.hww)
wph_hzz = add_decay_process(wph, h_decay_map.hzz)
wph_hbb = add_decay_process(wph, h_decay_map.hbb)
wph_hnonbb = add_decay_process(wph, h_decay_map.hnonbb)
wph_hcc = add_decay_process(wph, h_decay_map.hcc)
wph_hzg = add_decay_process(wph, h_decay_map.hzg)
wph_hgg = add_decay_process(wph, h_decay_map.hgg)
wph_hmm = add_decay_process(wph, h_decay_map.hmm)

# Higgs sub-decay channels
wph_hwwqqlnu = add_sub_decay_process(wph_hww, ww_decay_map["qqlnu"])
wph_hww2l2nu = add_sub_decay_process(wph_hww, ww_decay_map["2l2nu"])
wph_hww4q = add_sub_decay_process(wph_hww, ww_decay_map["4q"])
wph_hzz4l = add_sub_decay_process(wph_hzz, zz_decay_map["4l"])
wph_hzz2l2nu = add_sub_decay_process(wph_hzz, zz_decay_map["2l2nu"])
wph_hzz2l2q = add_sub_decay_process(wph_hzz, zz_decay_map["2l2q"])
wph_hzz2q2nu = add_sub_decay_process(wph_hzz, zz_decay_map["2q2nu"])
wph_hzz4nu = add_sub_decay_process(wph_hzz, zz_decay_map["4nu"])
wph_hzz4q = add_sub_decay_process(wph_hzz, zz_decay_map["4q"])
wph_hzg_zll = add_decay_process(wph_hzg, hzg_decay_map["zll"])
wph_hzg_zqq = add_decay_process(wph_hzg, hzg_decay_map["zqq"])
wph_hzg_znunu = add_decay_process(wph_hzg, hzg_decay_map["znunu"])

wph_wlnu = add_decay_process(wph, w_decay_map.wlnu)

# Higgs decay channels
wph_wlnu_htt = add_decay_process(wph_wlnu, h_decay_map.htt)
wph_wlnu_hww = add_decay_process(wph_wlnu, h_decay_map.hww)
wph_wlnu_hzz = add_decay_process(wph_wlnu, h_decay_map.hzz)
wph_wlnu_hbb = add_decay_process(wph_wlnu, h_decay_map.hbb)
wph_wlnu_hnonbb = add_decay_process(wph_wlnu, h_decay_map.hnonbb)
wph_wlnu_hcc = add_decay_process(wph_wlnu, h_decay_map.hcc)
wph_wlnu_hzg = add_decay_process(wph_wlnu, h_decay_map.hzg)
wph_wlnu_hgg = add_decay_process(wph_wlnu, h_decay_map.hgg)
wph_wlnu_hmm = add_decay_process(wph_wlnu, h_decay_map.hmm)

# Higgs sub-decay channels
wph_wlnu_hwwqqlnu = add_sub_decay_process(wph_wlnu_hww, ww_decay_map["qqlnu"])
wph_wlnu_hww2l2nu = add_sub_decay_process(wph_wlnu_hww, ww_decay_map["2l2nu"])
wph_wlnu_hww4q = add_sub_decay_process(wph_wlnu_hww, ww_decay_map["4q"])
wph_wlnu_hzz4l = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["4l"])
wph_wlnu_hzz2l2nu = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["2l2nu"])
wph_wlnu_hzz2l2q = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["2l2q"])
wph_wlnu_hzz2q2nu = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["2q2nu"])
wph_wlnu_hzz4nu = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["4nu"])
wph_wlnu_hzz4q = add_sub_decay_process(wph_wlnu_hzz, zz_decay_map["4q"])
wph_wlnu_hzg_zll = add_decay_process(wph_wlnu_hzg, hzg_decay_map["zll"])
wph_wlnu_hzg_zqq = add_decay_process(wph_wlnu_hzg, hzg_decay_map["zqq"])
wph_wlnu_hzg_znunu = add_decay_process(wph_wlnu_hzg, hzg_decay_map["znunu"])

wph_wqq = add_decay_process(wph, w_decay_map.wqq)

# Higgs decay channels
wph_wqq_htt = add_decay_process(wph_wqq, h_decay_map.htt)
wph_wqq_hww = add_decay_process(wph_wqq, h_decay_map.hww)
wph_wqq_hzz = add_decay_process(wph_wqq, h_decay_map.hzz)
wph_wqq_hbb = add_decay_process(wph_wqq, h_decay_map.hbb)
wph_wqq_hnonbb = add_decay_process(wph_wqq, h_decay_map.hnonbb)
wph_wqq_hcc = add_decay_process(wph_wqq, h_decay_map.hcc)
wph_wqq_hzg = add_decay_process(wph_wqq, h_decay_map.hzg)
wph_wqq_hgg = add_decay_process(wph_wqq, h_decay_map.hgg)
wph_wqq_hmm = add_decay_process(wph_wqq, h_decay_map.hmm)

# Higgs sub-decay channels
wph_wqq_hwwqqlnu = add_sub_decay_process(wph_wqq_hww, ww_decay_map["qqlnu"])
wph_wqq_hww2l2nu = add_sub_decay_process(wph_wqq_hww, ww_decay_map["2l2nu"])
wph_wqq_hww4q = add_sub_decay_process(wph_wqq_hww, ww_decay_map["4q"])
wph_wqq_hzz4l = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["4l"])
wph_wqq_hzz2l2nu = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["2l2nu"])
wph_wqq_hzz2l2q = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["2l2q"])
wph_wqq_hzz2q2nu = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["2q2nu"])
wph_wqq_hzz4nu = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["4nu"])
wph_wqq_hzz4q = add_sub_decay_process(wph_wqq_hzz, zz_decay_map["4q"])
wph_wqq_hzg_zll = add_decay_process(wph_wqq_hzg, hzg_decay_map["zll"])
wph_wqq_hzg_zqq = add_decay_process(wph_wqq_hzg, hzg_decay_map["zqq"])
wph_wqq_hzg_znunu = add_decay_process(wph_wqq_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# W- H subprocesses
#
####################################################################################################

# Higgs decay channels
wmh_htt = add_decay_process(wmh, h_decay_map.htt)
wmh_hww = add_decay_process(wmh, h_decay_map.hww)
wmh_hzz = add_decay_process(wmh, h_decay_map.hzz)
wmh_hbb = add_decay_process(wmh, h_decay_map.hbb)
wmh_hnonbb = add_decay_process(wmh, h_decay_map.hnonbb)
wmh_hcc = add_decay_process(wmh, h_decay_map.hcc)
wmh_hzg = add_decay_process(wmh, h_decay_map.hzg)
wmh_hgg = add_decay_process(wmh, h_decay_map.hgg)
wmh_hmm = add_decay_process(wmh, h_decay_map.hmm)

# Higgs sub-decay channels
wmh_hwwqqlnu = add_sub_decay_process(wmh_hww, ww_decay_map["qqlnu"])
wmh_hww2l2nu = add_sub_decay_process(wmh_hww, ww_decay_map["2l2nu"])
wmh_hww4q = add_sub_decay_process(wmh_hww, ww_decay_map["4q"])
wmh_hzz4l = add_sub_decay_process(wmh_hzz, zz_decay_map["4l"])
wmh_hzz2l2nu = add_sub_decay_process(wmh_hzz, zz_decay_map["2l2nu"])
wmh_hzz2l2q = add_sub_decay_process(wmh_hzz, zz_decay_map["2l2q"])
wmh_hzz2q2nu = add_sub_decay_process(wmh_hzz, zz_decay_map["2q2nu"])
wmh_hzz4nu = add_sub_decay_process(wmh_hzz, zz_decay_map["4nu"])
wmh_hzz4q = add_sub_decay_process(wmh_hzz, zz_decay_map["4q"])
wmh_hzg_zll = add_decay_process(wmh_hzg, hzg_decay_map["zll"])
wmh_hzg_zqq = add_decay_process(wmh_hzg, hzg_decay_map["zqq"])
wmh_hzg_znunu = add_decay_process(wmh_hzg, hzg_decay_map["znunu"])

wmh_wlnu = add_decay_process(wmh, w_decay_map.wlnu)

# Higgs decay channels
wmh_wlnu_htt = add_decay_process(wmh_wlnu, h_decay_map.htt)
wmh_wlnu_hww = add_decay_process(wmh_wlnu, h_decay_map.hww)
wmh_wlnu_hzz = add_decay_process(wmh_wlnu, h_decay_map.hzz)
wmh_wlnu_hbb = add_decay_process(wmh_wlnu, h_decay_map.hbb)
wmh_wlnu_hnonbb = add_decay_process(wmh_wlnu, h_decay_map.hnonbb)
wmh_wlnu_hcc = add_decay_process(wmh_wlnu, h_decay_map.hcc)
wmh_wlnu_hzg = add_decay_process(wmh_wlnu, h_decay_map.hzg)
wmh_wlnu_hgg = add_decay_process(wmh_wlnu, h_decay_map.hgg)
wmh_wlnu_hmm = add_decay_process(wmh_wlnu, h_decay_map.hmm)

# Higgs sub-decay channels
wmh_wlnu_hwwqqlnu = add_sub_decay_process(wmh_wlnu_hww, ww_decay_map["qqlnu"])
wmh_wlnu_hww2l2nu = add_sub_decay_process(wmh_wlnu_hww, ww_decay_map["2l2nu"])
wmh_wlnu_hww4q = add_sub_decay_process(wmh_wlnu_hww, ww_decay_map["4q"])
wmh_wlnu_hzz4l = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["4l"])
wmh_wlnu_hzz2l2nu = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["2l2nu"])
wmh_wlnu_hzz2l2q = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["2l2q"])
wmh_wlnu_hzz2q2nu = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["2q2nu"])
wmh_wlnu_hzz4nu = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["4nu"])
wmh_wlnu_hzz4q = add_sub_decay_process(wmh_wlnu_hzz, zz_decay_map["4q"])
wmh_wlnu_hzg_zll = add_decay_process(wmh_wlnu_hzg, hzg_decay_map["zll"])
wmh_wlnu_hzg_zqq = add_decay_process(wmh_wlnu_hzg, hzg_decay_map["zqq"])
wmh_wlnu_hzg_znunu = add_decay_process(wmh_wlnu_hzg, hzg_decay_map["znunu"])

wmh_wqq = add_decay_process(wmh, w_decay_map.wqq)

# Higgs decay channels
wmh_wqq_htt = add_decay_process(wmh_wqq, h_decay_map.htt)
wmh_wqq_hww = add_decay_process(wmh_wqq, h_decay_map.hww)
wmh_wqq_hzz = add_decay_process(wmh_wqq, h_decay_map.hzz)
wmh_wqq_hbb = add_decay_process(wmh_wqq, h_decay_map.hbb)
wmh_wqq_hnonbb = add_decay_process(wmh_wqq, h_decay_map.hnonbb)
wmh_wqq_hcc = add_decay_process(wmh_wqq, h_decay_map.hcc)
wmh_wqq_hzg = add_decay_process(wmh_wqq, h_decay_map.hzg)
wmh_wqq_hgg = add_decay_process(wmh_wqq, h_decay_map.hgg)
wmh_wqq_hmm = add_decay_process(wmh_wqq, h_decay_map.hmm)

# Higgs sub-decay channels
wmh_wqq_hwwqqlnu = add_sub_decay_process(wmh_wqq_hww, ww_decay_map["qqlnu"])
wmh_wqq_hww2l2nu = add_sub_decay_process(wmh_wqq_hww, ww_decay_map["2l2nu"])
wmh_wqq_hww4q = add_sub_decay_process(wmh_wqq_hww, ww_decay_map["4q"])
wmh_wqq_hzz4l = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["4l"])
wmh_wqq_hzz2l2nu = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["2l2nu"])
wmh_wqq_hzz2l2q = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["2l2q"])
wmh_wqq_hzz2q2nu = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["2q2nu"])
wmh_wqq_hzz4nu = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["4nu"])
wmh_wqq_hzz4q = add_sub_decay_process(wmh_wqq_hzz, zz_decay_map["4q"])
wmh_wqq_hzg_zll = add_decay_process(wmh_wqq_hzg, hzg_decay_map["zll"])
wmh_wqq_hzg_zqq = add_decay_process(wmh_wqq_hzg, hzg_decay_map["zqq"])
wmh_wqq_hzg_znunu = add_decay_process(wmh_wqq_hzg, hzg_decay_map["znunu"])


# add xsecs from wph and wmh
wh.xsecs = add_xsecs(wph, wmh)


####################################################################################################
#
# ttH
#
####################################################################################################

tth = h.add_process(
    name="tth",
    id=19000,
    label=r"$t\bar{t}H$",
    xsecs={
        13: Number(5.071E-01, {
            "scale": (0.058j, 0.092j),
            "pdf": 0.036j,
        }),
        13.6: Number(0.5700, {  # value for mH=125 GeV
            "scale": (0.060j, 0.093j),
            "pdf": 0.035j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)

# Higgs decay channels
tth_htt = add_decay_process(tth, h_decay_map.htt)
tth_hww = add_decay_process(tth, h_decay_map.hww)
tth_hzz = add_decay_process(tth, h_decay_map.hzz)
tth_hbb = add_decay_process(tth, h_decay_map.hbb)
tth_hnonbb = add_decay_process(tth, h_decay_map.hnonbb)
tth_hcc = add_decay_process(tth, h_decay_map.hcc)
tth_hzg = add_decay_process(tth, h_decay_map.hzg)
tth_hgg = add_decay_process(tth, h_decay_map.hgg)
tth_hmm = add_decay_process(tth, h_decay_map.hmm)

# Higgs sub-decay channels
tth_hwwqqlnu = add_sub_decay_process(tth_hww, ww_decay_map["qqlnu"])
tth_hww2l2nu = add_sub_decay_process(tth_hww, ww_decay_map["2l2nu"])
tth_hww4q = add_sub_decay_process(tth_hww, ww_decay_map["4q"])
tth_hzz4l = add_sub_decay_process(tth_hzz, zz_decay_map["4l"])
tth_hzz2l2nu = add_sub_decay_process(tth_hzz, zz_decay_map["2l2nu"])
tth_hzz2l2q = add_sub_decay_process(tth_hzz, zz_decay_map["2l2q"])
tth_hzz2q2nu = add_sub_decay_process(tth_hzz, zz_decay_map["2q2nu"])
tth_hzz4nu = add_sub_decay_process(tth_hzz, zz_decay_map["4nu"])
tth_hzz4q = add_sub_decay_process(tth_hzz, zz_decay_map["4q"])
tth_hzg_zll = add_decay_process(tth_hzg, hzg_decay_map["zll"])
tth_hzg_zqq = add_decay_process(tth_hzg, hzg_decay_map["zqq"])
tth_hzg_znunu = add_decay_process(tth_hzg, hzg_decay_map["znunu"])

####################################################################################################
#
# bbH, ttVH, tHq, tHW, tH
#
####################################################################################################

# TODO: in full combination and with correct xsecs

bbh = h.add_process(
    name="bbh",
    id=100000,
    label=r"$b\bar{b}H$",
    xsecs={
        13: Number(4.880E-01, {
            "scale_pdf": (0.202j, 0.239j),
        }),
        13.6: Number(0.5269, {  # value for mH=125 GeV
            "scale_pdf": (0.201j, 0.240j),
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)

ttvh = h.add_process(
    name="ttvh",
    id=110000,
    label=r"$t\bar{t}VH$",
    aux={"production_mode_parent": h},
)
ttzh = ttvh.add_process(
    name="ttzh",
    id=120000,
    label=r"$t\bar{t}ZH$",
    aux={"production_mode_parent": ttvh},
)
ttwh = ttvh.add_process(
    name="ttwh",
    id=130000,
    label=r"$t\bar{t}WH$",
    aux={"production_mode_parent": ttvh},
)
thw = h.add_process(
    name="thw",
    id=140000,
    label=r"$tHW$",
    xsecs={
        13: Number(1.517E-02, {
            "scale": (4.9j, 6.7j),
            "pdf": 6.3j,
        }),
        13.6: Number(1.720E-02, {
            "scale": (2.4j, 1.7j),
            "pdf": 2.2j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)
# also named tH t-channel
thq = h.add_process(
    name="thq",
    id=150000,
    label=r"$tHq$",
    xsecs={
        13: Number(7.425E-02, {
            "scale": (0.065j, 0.149j),
            "pdf": 3.7j,
        }),
        13.6: Number(8.362E-02, {  # value for mH=125 GeV
            "scale": (0.065j, 0.148j),
            "pdf": 3.7j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)
# also named tH s-channel
thb = h.add_process(
    name="thb",
    id=160000,
    label=r"$tHb$",
    xsecs={
        13: Number(2.879E-03, {
            "scale": (0.024j, 0.018j),
            "pdf": 2.2j,
        }),
        13.6: Number(3.068E-03, {  # value for mH=125 GeV
            "scale": (0.024j, 0.017j),
            "pdf": 2.2j,
        }),  # TODO: only preliminary
    },
    aux={"production_mode_parent": h},
)
