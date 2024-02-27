# coding: utf-8

"""
Top-related process definitions.
"""

__all__ = [
    "tt",
    "tt_sl", "tt_dl", "tt_fh",
    "st",
    "st_tchannel", "st_tchannel_t", "st_tchannel_tbar",
    "st_twchannel", "st_twchannel_t", "st_twchannel_tbar",
    "st_twchannel_t_sl", "st_twchannel_tbar_sl",
    "st_twchannel_t_dl", "st_twchannel_tbar_dl",
    "st_twchannel_t_fh", "st_twchannel_tbar_fh",
    "st_schannel", "st_schannel_lep", "st_schannel_had",
    "st_schannel_t", "st_schannel_t_lep", "st_schannel_t_had",
    "st_schannel_tbar", "st_schannel_tbar_lep", "st_schannel_tbar_had",
    "ttv",
    "ttz", "ttz_llnunu_m10",
    "ttw", "ttw_lnu", "ttw_qq",
    "ttvv",
    "ttzz", "ttwz", "ttww",
]

from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs


#
# ttbar
# (ids up to 1999)
#
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO?rev=21#Recommendations_for_most_analyse
# cross sections correspond to mtop = 172.5 GeV, see
# https://twiki.cern.ch/twiki/bin/view/CMS/TopMonteCarloSystematics?rev=7#mtop
#


tt = Process(
    name="tt",
    id=1000,
    label=r"$t\bar{t}$ + Jets",
    color=(205, 0, 9),
    xsecs={
        13: Number(833.9, {
            "scale": (20.5, 30.0),
            "pdf": 21.0,
            "mtop": (23.2, 22.5),
        }),
        13.6: Number(923.6, {
            "scale": (22.6, 33.4),
            "pdf": 22.8,
            "mtop": (25.4, 24.6),
        }),
    },
)

tt_sl = tt.add_process(
    name="tt_sl",
    id=1100,
    label=f"{tt.label}, SL",
    color=(205, 0, 9),
    xsecs=multiply_xsecs(tt, const.br_ww.sl),
)

tt_dl = tt.add_process(
    name="tt_dl",
    id=1200,
    label=f"{tt.label}, DL",
    color=(235, 230, 10),
    xsecs=multiply_xsecs(tt, const.br_ww.dl),
)

tt_fh = tt.add_process(
    name="tt_fh",
    id=1300,
    label=f"{tt.label}, FH",
    color=(255, 153, 0),
    xsecs=multiply_xsecs(tt, const.br_ww.fh),
)


#
# single-top
#
# all st cross sections except s-channel are taken from here:
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=20
#
# 13 TeV s-channel cross sections from here:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma?rev=12#Single_Top_Cross_sections_at_13?rev=12

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
        13: Number(214.2, dict(
            scale=(2.4, 1.7),
            pdf=(3.3, 2.2),  # includes alpha_s
            mtop=(1.7, 1.9),
            E_beam=(0.4, 0.3),
            integration=0.2,
        )),
        13.6: Number(232.2, dict(
            scale=(2.6, 1.9),
            pdf=(3.4, 2.2),  # includes alpha_s
            mtop=(1.9, 1.6),
            E_beam=(0.6, 0.5),
            integration=0.2,
        )),
    },
)

st_tchannel_t = st_tchannel.add_process(
    name="st_tchannel_t",
    id=2110,
    xsecs={
        13: Number(134.2, dict(
            scale=(1.5, 1.1),
            pdf=(2.1, 1.3),  # includes alpha_s
            mtop=(1.0, 1.2),
            E_beam=(0.2, 0.2),
            integration=0.1,
        )),
        13.6: Number(145.0, dict(
            scale=(1.7, 1.1),
            pdf=(2.3, 1.5),  # includes alpha_s
            mtop=(1.3, 0.9),
            E_beam=(0.4, 0.3),
            integration=0.1,

        )),
    },
)

st_tchannel_tbar = st_tchannel.add_process(
    name="st_tchannel_tbar",
    id=2120,
    xsecs={
        13: Number(80.0, dict(
            scale=(1.5, 1.1),
            pdf=(1.6, 1.2),  # includes alpha_s
            mtop=(0.7, 0.7),
            E_beam=(0.2, 0.1),
            integration=0.1,
        )),
        13.6: Number(87.2, dict(
            scale=(0.9, 0.8),
            pdf=(1.5, 1.3),  # includes alpha_s
            mtop=(0.6, 0.7),
            E_beam=(0.2, 0.2),
            integration=0.1,
        )),
    },
)

st_twchannel = st.add_process(
    name="st_twchannel",
    id=2200,
    label=f"{st.label}, tW-channel",
    xsecs={
        13: Number(79.3, dict(
            scale=(1.9, 1.8),
            pdf=2.2,  # includes alpha_s
            mtop=1.2,
            E_beam=0.2,
        )),
        13.6: Number(87.9, dict(
            scale=(2.0, 1.9),
            pdf=2.4,  # includes alpha_s
            mtop=1.3,
            E_beam=0.2,
        )),
    },
)

st_twchannel_t = st_twchannel.add_process(
    name="st_twchannel_t",
    id=2210,
    xsecs={
        13: st_twchannel.get_xsec(13) / 2,
        13.6: st_twchannel.get_xsec(13.6) / 2,
    },
)

st_twchannel_t_sl = st_twchannel_t.add_process(
    name="st_twchannel_t_sl",
    id=2211,
    xsecs=multiply_xsecs(st_twchannel_t, const.br_ww.sl),
)

st_twchannel_t_dl = st_twchannel_t.add_process(
    name="st_twchannel_t_dl",
    id=2212,
    xsecs=multiply_xsecs(st_twchannel_t, const.br_ww.dl),
)

st_twchannel_t_fh = st_twchannel_t.add_process(
    name="st_twchannel_t_fh",
    id=2213,
    xsecs=multiply_xsecs(st_twchannel_t, const.br_ww.fh),
)

st_twchannel_tbar = st_twchannel.add_process(
    name="st_twchannel_tbar",
    id=2220,
    xsecs={
        13: st_twchannel.get_xsec(13) / 2,
        13.6: st_twchannel.get_xsec(13.6) / 2,
    },
)

st_twchannel_tbar_sl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_sl",
    id=2221,
    xsecs=multiply_xsecs(st_twchannel_tbar, const.br_ww.sl),
)

st_twchannel_tbar_dl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_dl",
    id=2222,
    xsecs=multiply_xsecs(st_twchannel_tbar, const.br_ww.dl),
)

st_twchannel_tbar_fh = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_fh",
    id=2223,
    xsecs=multiply_xsecs(st_twchannel_tbar, const.br_ww.fh),
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
        # TODO: 13.6 TeV xsecs
    },
)

st_schannel_lep = st_schannel.add_process(
    name="st_schannel_lep",
    id=2301,
    xsecs=multiply_xsecs(st_schannel, const.br_w.lep),
)

st_schannel_had = st_schannel.add_process(
    name="st_schannel_had",
    id=2302,
    xsecs=multiply_xsecs(st_schannel, const.br_w.had),
)

st_schannel_t = st_schannel.add_process(
    name="st_schannel_t",
    id=2310,
    xsecs={
        13: Number(7.20, dict(
            scale=0.13,
            pdf=(0.29, 0.23),
        )),
        # TODO: 13.6 TeV xsecs
    },
)

st_schannel_t_lep = st_schannel_t.add_process(
    name="st_schannel_t_lep",
    id=2311,
    xsecs=multiply_xsecs(st_schannel_t, const.br_w.lep),
)

st_schannel_t_had = st_schannel_t.add_process(
    name="st_schannel_t_had",
    id=2312,
    xsecs=multiply_xsecs(st_schannel_t, const.br_w.had),
)

st_schannel_tbar = st_schannel.add_process(
    name="st_schannel_tbar",
    id=2320,
    xsecs={
        13: Number(4.16, dict(
            scale=0.05,
            pdf=(0.12, 0.23),
        )),
        # TODO: 13.6 TeV xsecs
    },
)

st_schannel_tbar_lep = st_schannel_tbar.add_process(
    name="st_schannel_tbar_lep",
    id=2321,
    xsecs=multiply_xsecs(st_schannel_tbar, const.br_w.lep),
)

st_schannel_tbar_had = st_schannel_tbar.add_process(
    name="st_schannel_tbar_had",
    id=2322,
    xsecs=multiply_xsecs(st_schannel_tbar, const.br_w.had),
)

# define the combined single top cross section as the sum of the three channels
st.set_xsec(
    13,
    st_tchannel.get_xsec(13) + st_twchannel.get_xsec(13) + st_schannel.get_xsec(13),
)


#
# ttbar + 1 vector boson
#

# ttv cross section values based on
# 13 TeV: https://www.arxiv.org/abs/2001.03031
# 14 TeV: https://www.arxiv.org/abs/1812.08622

ttv = Process(
    name="ttv",
    id=3000,
    label=f"{tt.label} + V",
)

ttz = ttv.add_process(
    name="ttz",
    id=3100,
    label=f"{tt.label} + Z",
    xsecs={
        13: Number(0.859, {
            "scale": (8.6j, 9.5j),
            "pdf": 2.3j,
        }),
        14: Number(1.045, {
            "scale": (8.8j, 9.9j),
            "pdf": 3.1j,
        }),
    },
)

ttz_llnunu_m10 = ttz.add_process(
    name="ttz_llnunu_m10",  # non-hadronically decaying Z
    id=3110,
    xsecs={13: Number(0.1)},  # TODO
)

ttw = ttv.add_process(
    name="ttw",
    id=3200,
    label=f"{tt.label} + W",
    xsecs={
        13: Number(592, {
            "scale": (26.1j, 16.2j),
            "pdf": 2.1j,
        }),
        14: Number(0.429, {  # ttW+
            "scale": (26.4j, 16.7j),
            "pdf": 3.2j,
        }) + Number(0.224, {  # ttW-
            "scale": (26.4j, 16.4j),
            "pdf": 3.6j,
        }),
    },
)

# set combined cross sections
for ecm in (13, 14):
    ttv.set_xsec(ecm, ttw.get_xsec(ecm) + ttz.get_xsec(ecm))

ttw_lnu = ttw.add_process(
    name="ttw_lnu",
    id=3210,
    xsecs=multiply_xsecs(ttw, const.br_w.lep),
)

ttw_qq = ttw.add_process(
    name="ttw_qq",
    id=3220,
    xsecs=multiply_xsecs(ttw, const.br_w.had),
)


#
# ttbar + 2 vector bosons
#

ttvv = Process(
    name="ttvv",
    id=4000,
    label=f"{tt.label} + VV",
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
