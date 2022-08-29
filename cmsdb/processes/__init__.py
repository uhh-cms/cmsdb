# coding: utf-8

"""
Physics processes and cross sections.
"""

from order import Process
from scinum import Number

import cmsdb.constants as const


#
# data
# (ids up to 999)
#

data = Process(
    name="data",
    id=1,
    is_data=True,
    label="data",
)

data_e = data.add_process(
    name="data_e",
    id=10,
    is_data=True,
    label=r"Data $e$",
)

data_mu = data.add_process(
    name="data_mu",
    id=20,
    is_data=True,
    label=r"Data $\mu$",
)

data_tau = data.add_process(
    name="data_tau",
    id=30,
    is_data=True,
    label=r"Data $\tau$",
)

data_met = data.add_process(
    name="data_met",
    id=40,
    is_data=True,
    label=r"Data MET",
)


#
# ttbar
# (ids up to 1999)
#
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO?rev=16#Top_quark_pair_cross_sections_at
# use mtop = 172.5 GeV, see
# https://twiki.cern.ch/twiki/bin/view/CMS/TopMonteCarloSystematics?rev=7#mtop
#

tt = Process(
    name="tt",
    id=1000,
    label=r"$t\bar{t}$ + Jets",
    color=(205, 0, 9),
    xsecs={
        13: Number(831.76, {
            "scale": (19.77, 29.20),
            "pdf": 35.06,
            "mtop": (23.18, 22.45),
        }),
    },
)

tt_sl = tt.add_process(
    name="tt_sl",
    id=1100,
    label=f"{tt.label}, SL",
    color=(205, 0, 9),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.sl,
    },
)

tt_dl = tt.add_process(
    name="tt_dl",
    id=1200,
    label=f"{tt.label}, DL",
    color=(235, 230, 10),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.dl,
    },
)

tt_fh = tt.add_process(
    name="tt_fh",
    id=1300,
    label=f"{tt.label}, FH",
    color=(255, 153, 0),
    xsecs={
        13: tt.get_xsec(13) * const.br_ww.fh,
    },
)


#
# single-top
#
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma?rev=12#Single_Top_Cross_sections_at_13
#

st = Process(
    name="st",
    id=2000,
    label=r"Single $t$/$\bar{t}$",
    color=(2, 210, 209),
)

st_tchannel = st.add_process(
    name="st_tchannel",
    id=2100,
    label=f"{st.label}, t-channel",
    xsecs={
        13: Number(216.99, dict(
            scale=(6.62, 4.64),
            pdf=6.16,  # includes alpha_s
            mtop=1.81,
        )),
    },
)

st_tchannel_t = st_tchannel.add_process(
    name="st_tchannel_t",
    id=2110,
    xsecs={
        13: Number(136.02, dict(
            scale=(4.09, 2.92),
            pdf=3.52,  # includes alpha_s
            mtop=1.11,
        )),
    },
)

st_tchannel_tbar = st_tchannel.add_process(
    name="st_tchannel_tbar",
    id=2120,
    xsecs={
        13: Number(80.95, dict(
            scale=(2.53, 1.71),
            pdf=3.18,  # includes alpha_s
            mtop=(0.71, 0.70),
        )),
    },
)

st_twchannel = st.add_process(
    name="st_twchannel",
    id=2200,
    label=f"{st.label}, tW-channel",
    xsecs={
        13: Number(71.7, dict(
            scale=1.8,
            pdf=3.4,
        )),
    },
)

st_twchannel_t = st_twchannel.add_process(
    name="st_twchannel_t",
    id=2210,
    xsecs={
        13: Number(35.85, dict(
            scale=0.90,
            pdf=1.70,
        )),
    },
)

st_twchannel_tbar = st_twchannel.add_process(
    name="st_twchannel_tbar",
    id=2220,
    xsecs={
        13: Number(35.85, dict(
            scale=0.90,
            pdf=1.70,
        )),
    },
)

st_schannel = st.add_process(
    name="st_schannel",
    id=2300,
    label=f"{st.label}, s-channel",
    xsecs={
        13: Number(11.36, dict(
            scale=0.18,
            pdf=(0.40, 0.45),
        )),
    },
)

st_schannel_lep = st_schannel.add_process(
    name="st_schannel_lep",
    id=2301,
    xsecs={
        13: st_schannel.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_had = st_schannel.add_process(
    name="st_schannel_had",
    id=2302,
    xsecs={
        13: st_schannel.get_xsec(13) * const.br_w.had,
    },
)

st_schannel_t = st_schannel.add_process(
    name="st_schannel_t",
    id=2310,
    xsecs={
        13: Number(7.20, dict(
            scale=0.13,
            pdf=(0.29, 0.23),
        )),
    },
)

st_schannel_t_lep = st_schannel_t.add_process(
    name="st_schannel_t_lep",
    id=2311,
    xsecs={
        13: st_schannel_t.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_t_had = st_schannel_t.add_process(
    name="st_schannel_t_had",
    id=2312,
    xsecs={
        13: st_schannel_t.get_xsec(13) * const.br_w.had,
    },
)

st_schannel_tbar = st_schannel.add_process(
    name="st_schannel_tbar",
    id=2320,
    xsecs={
        13: Number(4.16, dict(
            scale=0.05,
            pdf=(0.12, 0.23),
        )),
    },
)

st_schannel_tbar_lep = st_schannel_tbar.add_process(
    name="st_schannel_tbar_lep",
    id=2321,
    xsecs={
        13: st_schannel_tbar.get_xsec(13) * const.br_w.lep,
    },
)

st_schannel_tbar_had = st_schannel_tbar.add_process(
    name="st_schannel_tbar_had",
    id=2322,
    xsecs={
        13: st_schannel_tbar.get_xsec(13) * const.br_w.had,
    },
)

# define the combined single top cross section as the sum of the three channels
st.set_xsec(
    13,
    st_tchannel.get_xsec(13) + st_twchannel.get_xsec(13) + st_schannel.get_xsec(13),
)


#
# ttbar + 1 vector boson
#

ttv = Process(
    name="ttv",
    id=3000,
    xsecs={13: Number(0.1)},  # TODO
)

ttz = ttv.add_process(
    name="ttv",
    id=3100,
    xsecs={13: Number(0.1)},  # TODO
)

ttz_llnunu = ttz.add_process(
    name="ttz_llnunu",
    id=3110,
    xsecs={13: Number(0.1)},  # TODO
)

ttw = ttv.add_process(
    name="ttw",
    id=3200,
    xsecs={13: Number(0.1)},  # TODO
)

ttw_lnu = ttz.add_process(
    name="ttw_lnu",
    id=3210,
    xsecs={13: Number(0.1)},  # TODO
)

ttw_qq = ttz.add_process(
    name="ttw_qq",
    id=3220,
    xsecs={13: Number(0.1)},  # TODO
)


#
# ttbar + 2 vector bosons
#

ttvv = Process(
    name="ttvv",
    id=4000,
    xsecs={13: Number(0.1)},  # TODO
)

ttzz = ttvv.add_process(
    name="ttzz",
    id=4100,
    xsecs={13: Number(0.1)},  # TODO
)

ttwz = ttvv.add_process(
    name="ttwz",
    id=4200,
    xsecs={13: Number(0.1)},  # TODO
)

ttww = ttvv.add_process(
    name="ttww",
    id=4300,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Drell-Yan
#

dy = Process(
    name="dy",
    id=50000,
    xsecs={13: Number(0.1)},  # TODO
)

dy_lep = dy.add_process(
    name="dy_lep",
    id=51000,
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
    xsecs={13: Number(0.1)},  # TODO
)

w_lnu = w.add_process(
    name="w_lnu",
    id=6100,
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
    xsecs={13: Number(0.1)},  # TODO
)

zz = vv.add_process(
    name="zz",
    id=8100,
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


#
# Single Higgs
#

h = Process(
    name="h",
    id=10000,
    xsecs={13: Number(0.1)},  # TODO
)

h_ggf = h.add_process(
    name="h_ggf",
    id=11000,
    xsecs={13: Number(0.1)},  # TODO
)

h_ggf_tautau = h_ggf.add_process(
    name="h_ggf_tautau",
    id=11100,
    xsecs={13: Number(0.1)},  # TODO
)

h_vbf = h.add_process(
    name="h_vbf",
    id=12000,
    xsecs={13: Number(0.1)},  # TODO
)

h_vbf_tautau = h_vbf.add_process(
    name="h_vbf_tautau",
    id=12100,
    xsecs={13: Number(0.1)},  # TODO
)

vh = h.add_process(
    name="vh",
    id=13000,
    xsecs={13: Number(0.1)},  # TODO
)

zh = vh.add_process(
    name="zh",
    id=13100,
    xsecs={13: Number(0.1)},  # TODO
)

zh_tautau = zh.add_process(
    name="zh_tautau",
    id=13110,
    xsecs={13: Number(0.1)},  # TODO
)

zh_bb = zh.add_process(
    name="zh_bb",
    id=13120,
    xsecs={13: Number(0.1)},  # TODO
)

wph = vh.add_process(
    name="wph",
    id=13200,
    xsecs={13: Number(0.1)},  # TODO
)

wph_tautau = wph.add_process(
    name="wph_tautau",
    id=13210,
    xsecs={13: Number(0.1)},  # TODO
)

wmh = vh.add_process(
    name="wmh",
    id=13300,
    xsecs={13: Number(0.1)},  # TODO
)

wmh_tautau = wmh.add_process(
    name="wmh_tautau",
    id=13310,
    xsecs={13: Number(0.1)},  # TODO
)

ggzh = vh.add_process(
    name="ggzh",
    id=14000,
    xsecs={13: Number(0.1)},  # TODO
)

ggzh_llbb = ggzh.add_process(
    name="ggzh_llbb",
    id=14100,
    xsecs={13: Number(0.1)},  # TODO
)

tth = h.add_process(
    name="tth",
    id=15000,
    xsecs={13: Number(0.1)},  # TODO
)

tth_tautau = tth.add_process(
    name="tth_tautau",
    id=15100,
    xsecs={13: Number(0.1)},  # TODO
)

tth_bb = tth.add_process(
    name="tth_bb",
    id=15200,
    xsecs={13: Number(0.1)},  # TODO
)

tth_nonbb = tth.add_process(
    name="tth_nonbb",
    id=15300,
    xsecs={13: Number(0.1)},  # TODO
)


#
# HH
#

hh = Process(
    name="hh",
    id=20000,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf = hh.add_process(
    name="hh_ggf",
    id=21000,
    xsecs={13: Number(0.1)},  # TODO
)

hh_vbf = hh.add_process(
    name="hh_vbf",
    id=22000,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_kt_1_kl_0 = hh_ggf.add_process(
    name="hh_ggf_kt_1_kl_0",
    id=21001,
    xsecs={
        13: Number(0.07038, {
            "scale": (0.024j, 0.061j),
            "pdf": 0.03j,
            "mtop": (0.06j, 0.12j),
        }),
    },
)

hh_ggf_kt_1_kl_1 = hh_ggf.add_process(
    name="hh_ggf_kt_1_kl_1",
    id=21002,
    xsecs={
        13: Number(0.03105, {
            "scale": (0.022j, 0.050j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.18j),
        }),
    },
)

hh_ggf_kt_1_kl_2p45 = hh_ggf.add_process(
    name="hh_ggf_kt_1_kl_2p45",
    id=21003,
    xsecs={
        13: Number(0.01310, {
            "scale": (0.023j, 0.051j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.22j),
        }),
    },
)

hh_ggf_kt_1_kl_5 = hh_ggf.add_process(
    name="hh_ggf_kt_1_kl_5",
    id=21004,
    xsecs={
        13: Number(0.09482, {
            "scale": (0.049j, 0.088j),
            "pdf": 0.03j,
            "mtop": (0.13j, 0.04j),
        }),
    },
)

#
# HH -> bbWW -> bbWWqqlnu
#

hh_ggf_kt_1_kl_0_bbww_sl = hh_ggf_kt_1_kl_0.add_process(
    name="hh_ggf_kt_1_kl_0_bbww_sl",
    id=21220,
    xsecs={13: hh_ggf_kt_1_kl_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl},
)
hh_ggf_kt_1_kl_1_bbww_sl = hh_ggf_kt_1_kl_1.add_process(
    name="hh_ggf_kt_1_kl_1_bbww_sl",
    id=21221,
    xsecs={13: hh_ggf_kt_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl},
)
hh_ggf_kt_1_kl_2p45_bbww_sl = hh_ggf_kt_1_kl_2p45.add_process(
    name="hh_ggf_kt_1_kl_2p45_bbww_sl",
    id=21222,
    xsecs={13: hh_ggf_kt_1_kl_2p45.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl},
)
hh_ggf_kt_1_kl_5_bbww_sl = hh_ggf_kt_1_kl_5.add_process(
    name="hh_ggf_kt_1_kl_5_bbww_sl",
    id=21223,
    xsecs={13: hh_ggf_kt_1_kl_5.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl},
)

#
# HH -> bbtautau
#

#
# ggF -> H -> HH
#

hh_ggf_bbtautau = hh_ggf.add_process(
    name="hh_ggf_bbtautau",
    id=21100,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node1 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node1",
    id=21101,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node2 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node2",
    id=21102,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node3 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node3",
    id=21103,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node4 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node4",
    id=21104,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node5 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node5",
    id=21105,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node6 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node6",
    id=21106,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node7 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node7",
    id=21107,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node8 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node8",
    id=21108,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node9 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node9",
    id=21109,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node10 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node10",
    id=21110,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node11 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node11",
    id=21111,
    xsecs={13: Number(0.1)},  # TODO
)

hh_ggf_bbtautau_node12 = hh_ggf.add_process(
    name="hh_ggf_bbtautau_node12",
    id=21112,
    xsecs={13: Number(0.1)},  # TODO
)


#
# ggF -> radion -> HH
#

radion_hh_ggf = hh_ggf.add_process(
    name="radion_hh_ggf",
    id=23000,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau = hh_ggf.add_process(
    name="radion_hh_ggf_bbtautau",
    id=23100,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m250 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m250",
    id=23101,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m260 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m260",
    id=23102,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m270 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m270",
    id=23103,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m280 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m280",
    id=23104,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m300 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m300",
    id=23105,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m320 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m320",
    id=23106,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m350 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m350",
    id=23107,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m400 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m400",
    id=23108,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m450 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m450",
    id=23109,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m500 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m500",
    id=23110,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m550 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m550",
    id=23111,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m600 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m600",
    id=23112,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m650 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m650",
    id=23113,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m700 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m700",
    id=23114,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m750 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m750",
    id=23115,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m800 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m800",
    id=23116,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m850 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m850",
    id=23117,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m900 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m900",
    id=23118,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m1000 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m1000",
    id=23119,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m1250 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m1250",
    id=23120,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m1500 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m1500",
    id=23121,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m1750 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m1750",
    id=23122,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m2000 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m2000",
    id=23123,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m2500 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m2500",
    id=23124,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbtautau_m3000 = radion_hh_ggf_bbtautau.add_process(
    name="radion_hh_ggf_bbtautau_m3000",
    id=23125,
    xsecs={13: Number(0.1)},  # TODO
)


#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf = hh_ggf.add_process(
    name="graviton_hh_ggf",
    id=24000,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau = hh_ggf.add_process(
    name="graviton_hh_ggf_bbtautau",
    id=24100,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m250 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m250",
    id=24101,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m260 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m260",
    id=24102,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m270 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m270",
    id=24103,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m280 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m280",
    id=24104,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m300 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m300",
    id=24105,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m320 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m320",
    id=24106,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m350 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m350",
    id=24107,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m400 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m400",
    id=24108,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m450 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m450",
    id=24109,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m500 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m500",
    id=24110,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m550 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m550",
    id=24111,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m600 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m600",
    id=24112,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m650 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m650",
    id=24113,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m700 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m700",
    id=24114,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m750 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m750",
    id=24115,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m800 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m800",
    id=24116,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m850 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m850",
    id=24117,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m900 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m900",
    id=24118,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m1000 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m1000",
    id=24119,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m1250 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m1250",
    id=24120,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m1500 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m1500",
    id=24121,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m1750 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m1750",
    id=24122,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m2000 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m2000",
    id=24123,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m2500 = graviton_hh_ggf_bbtautau.add_process(
    name="graviton_hh_ggf_bbtautau_m2500",
    id=24124,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbtautau_m3000 = graviton_hh_ggf_bbtautau.add_process(
    name="hh_ggf_graviton_bbtautau_m3000",
    id=24125,
    xsecs={13: Number(0.1)},  # TODO
)


#
# vbf -> radion -> HH
#

radion_hh_vbf = hh_vbf.add_process(
    name="radion_hh_vbf",
    id=25000,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau = hh_vbf.add_process(
    name="radion_hh_vbf_bbtautau",
    id=25100,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m250 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m250",
    id=25101,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m260 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m260",
    id=25102,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m270 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m270",
    id=25103,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m280 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m280",
    id=25104,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m300 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m300",
    id=25105,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m320 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m320",
    id=25106,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m350 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m350",
    id=25107,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m400 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m400",
    id=25108,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m450 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m450",
    id=25109,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m500 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m500",
    id=25110,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m550 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m550",
    id=25111,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m600 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m600",
    id=25112,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m650 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m650",
    id=25113,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m700 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m700",
    id=25114,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m750 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m750",
    id=25115,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m800 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m800",
    id=25116,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m850 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m850",
    id=25117,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m900 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m900",
    id=25118,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m1000 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m1000",
    id=25119,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m1250 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m1250",
    id=25120,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m1500 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m1500",
    id=25121,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m1750 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m1750",
    id=25122,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m2000 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m2000",
    id=25123,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m2500 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m2500",
    id=25124,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_bbtautau_m3000 = radion_hh_vbf_bbtautau.add_process(
    name="radion_hh_vbf_bbtautau_m3000",
    id=25125,
    xsecs={13: Number(0.1)},  # TODO
)


#
# vbf -> bulk graviton -> HH
#

graviton_hh_vbf = hh_vbf.add_process(
    name="graviton_hh_vbf",
    id=26000,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau = hh_vbf.add_process(
    name="graviton_hh_vbf_bbtautau",
    id=26100,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m250 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m250",
    id=26101,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m260 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m260",
    id=26102,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m270 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m270",
    id=26103,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m280 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m280",
    id=26104,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m300 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m300",
    id=26105,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m320 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m320",
    id=26106,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m350 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m350",
    id=26107,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m400 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m400",
    id=26108,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m450 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m450",
    id=26109,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m500 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m500",
    id=26110,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m550 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m550",
    id=26111,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m600 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m600",
    id=26112,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m650 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m650",
    id=26113,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m700 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m700",
    id=26114,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m750 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m750",
    id=26115,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m800 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m800",
    id=26116,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m850 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m850",
    id=26117,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m900 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m900",
    id=26118,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m1000 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m1000",
    id=26119,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m1250 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m1250",
    id=26120,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m1500 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m1500",
    id=26121,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m1750 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m1750",
    id=26122,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m2000 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m2000",
    id=26123,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m2500 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m2500",
    id=26124,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_bbtautau_m3000 = graviton_hh_vbf_bbtautau.add_process(
    name="graviton_hh_vbf_bbtautau_m3000",
    id=26125,
    xsecs={13: Number(0.1)},  # TODO
)


#
# QCD
#

qcd = Process(
    name="qcd",
    id=30000,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht50to100 = qcd.add_process(
    name="qcd_ht50to100",
    id=31001,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht100to200 = qcd.add_process(
    name="qcd_ht100to200",
    id=31002,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht200to300 = qcd.add_process(
    name="qcd_ht200to300",
    id=31003,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht300to500 = qcd.add_process(
    name="qcd_ht300to500",
    id=31004,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht500to700 = qcd.add_process(
    name="qcd_ht500to700",
    id=31005,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht700to1000 = qcd.add_process(
    name="qcd_ht700to1000",
    id=31006,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht1000to1500 = qcd.add_process(
    name="qcd_ht1000to1500",
    id=31007,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht1500to2000 = qcd.add_process(
    name="qcd_ht1500to2000",
    id=31008,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht2000 = qcd.add_process(
    name="qcd_ht2000",
    id=31090,
    xsecs={13: Number(0.1)},  # TODO
)
