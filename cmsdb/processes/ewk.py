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
    "dy_lep_pt50To100", "dy_lep_pt100To250", "dy_lep_pt250To400", "dy_lep_pt400To650",
    "dy_lep_pt650",
    "w",
    "w_lnu",
    "w_lnu_ht70To100", "w_lnu_ht100To200", "w_lnu_ht200To400", "w_lnu_ht400To600",
    "w_lnu_ht600To800", "w_lnu_ht800To1200", "w_lnu_ht1200To2500", "w_lnu_ht2500",
    "ewk",
    "ewk_wp_lnu", "ewk_wm_lnu", "ewk_z_ll",
    "vv",
    "zz", "zz_qqll_m4", "zz_llnunu", "zz_llll",
    "wz", "wz_lllnu", "wz_qqll_m4",
    "ww", "ww_lnulnu",
    "vvv",
    "zzz", "wzz", "wwz", "www",
]

from order import Process
from scinum import Number


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

dy_lep_m50 = dy_lep.add_process(
    name="dy_lep_m50",
    id=51100,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_1j = dy_lep_m50.add_process(
    name="dy_lep_m50_1j",
    id=51111,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_2j = dy_lep_m50.add_process(
    name="dy_lep_m50_2j",
    id=51112,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_3j = dy_lep_m50.add_process(
    name="dy_lep_m50_3j",
    id=51113,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_4j = dy_lep_m50.add_process(
    name="dy_lep_m50_4j",
    id=51114,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_0j = dy_lep.add_process(
    name="dy_lep_0j",
    id=51200,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_1j = dy_lep.add_process(
    name="dy_lep_1j",
    id=51300,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_2j = dy_lep.add_process(
    name="dy_lep_3j",
    id=51400,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht70to100 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht70to100",
    id=51121,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht100to200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht100to200",
    id=51122,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht200to400 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht200to400",
    id=51123,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht400to600 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht400to600",
    id=51124,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht600to800 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht600to800",
    id=51125,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht800to1200 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht800to1200",
    id=51126,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht1200to2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht1200to2500",
    id=51127,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_m50_ht2500 = dy_lep_m50.add_process(
    name="dy_lep_m50_ht2500",
    id=51128,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_pt50To100 = dy_lep.add_process(
    name="dy_lep_pt50To100",
    id=51510,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_pt100To250 = dy_lep.add_process(
    name="dy_lep_pt100To250",
    id=51520,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_pt250To400 = dy_lep.add_process(
    name="dy_lep_pt250To400",
    id=51530,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_pt400To650 = dy_lep.add_process(
    name="dy_lep_pt400To650",
    id=51540,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep_pt650 = dy_lep.add_process(
    name="dy_lep_pt650",
    id=51550,
    xsecs={13: Number(0.1)},  # TODO
)


#
# W boson
#

w = Process(
    name="w",
    id=6000,
    label="W + jets",
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
    label=rf"{w.label} ($W \rightarrow l\nu$)",
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht70To100 = w_lnu.add_process(
    name="w_lnu_ht70To100",
    id=6110,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht100To200 = w_lnu.add_process(
    name="w_lnu_ht100To200",
    id=6120,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht200To400 = w_lnu.add_process(
    name="w_lnu_ht200To400",
    id=6130,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht400To600 = w_lnu.add_process(
    name="w_lnu_ht400To600",
    id=6140,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht600To800 = w_lnu.add_process(
    name="w_lnu_ht600To800",
    id=6150,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht800To1200 = w_lnu.add_process(
    name="w_lnu_ht800To1200",
    id=6160,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht1200To2500 = w_lnu.add_process(
    name="w_lnu_ht1200To2500",
    id=6170,
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu_ht2500 = w_lnu.add_process(
    name="w_lnu_ht2500",
    id=6180,
    xsecs={13: Number(0.1)},  # TODO
)


#
# EWK radiations
#

ewk = Process(
    name="ewk",
    id=7000,
    label="EWK",
    xsecs={13: Number(0.1)},  # TODO
)

ewk_wp_lnu = ewk.add_process(
    name="ewk_wp_lnu",
    id=7100,
    xsecs={13: Number(0.1)},  # TODO
)

ewk_wm_lnu = ewk.add_process(
    name="ewk_wm_lnu",
    id=7200,
    xsecs={13: Number(0.1)},  # TODO
)

ewk_z_ll = ewk.add_process(
    name="ewk_z_ll",
    id=7300,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="Di-Boson",
    xsecs={13: Number(0.1)},  # TODO
)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={13: Number(0.1)},  # TODO
)

zz_qqll_m4 = zz.add_process(
    name="zz_qqll_m4",
    id=8110,
    xsecs={13: Number(0.1)},  # TODO
)

zz_llnunu = zz.add_process(
    name="zz_llnunu",
    id=8120,
    xsecs={13: Number(0.1)},  # TODO
)

zz_llll = zz.add_process(
    name="zz_llll",
    id=8130,
    xsecs={13: Number(0.1)},  # TODO
)

wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={13: Number(0.1)},  # TODO
)

wz_lllnu = wz.add_process(
    name="wz_lllnu",
    id=8210,
    xsecs={13: Number(0.1)},  # TODO
)

wz_qqll_m4 = wz.add_process(
    name="wz_qqll_m4",
    id=8220,
    xsecs={13: Number(0.1)},  # TODO
)

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={13: Number(0.1)},  # TODO
)

ww_lnulnu = ww.add_process(
    name="ww_lnulnu",
    id=8310,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Triple-boson
#

vvv = Process(
    name="vvv",
    id=9000,
    label="Triple-Boson",
    xsecs={13: Number(0.1)},  # TODO
)

zzz = vvv.add_process(
    name="zzz",
    id=9100,
    xsecs={13: Number(0.1)},  # TODO
)

wzz = vvv.add_process(
    name="wzz",
    id=9200,
    xsecs={13: Number(0.1)},  # TODO
)

wwz = vvv.add_process(
    name="wwz",
    id=9300,
    xsecs={13: Number(0.1)},  # TODO
)

www = vvv.add_process(
    name="www",
    id=9400,
    xsecs={13: Number(0.1)},  # TODO
)
