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


#
# ttbar
# (ids up to 1999)
#
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO?rev=21#Updated_reference_cross_sections
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
# t- and tw-channel: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=20#Predictions_for_top_quark_produc  # noqa
# s-channel: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec?rev=36#Single_top_s_channel_cross_secti
# for the tW-channel, the t and tbar channels contribute equally as stated in
# Ref https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec?rev=36#Single_top_Wt_channel_cross_sect
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
        13: Number(214.2, {
            "scale": (2.4, 1.7),
            "pdf": (3.3, 2.0),  # includes alpha_s
            "mtop": (1.7, 1.9),
            "beam": (0.4, 0.3),
            "integration": 0.2,
        }),
    },
)

st_tchannel_t = st_tchannel.add_process(
    name="st_tchannel_t",
    id=2110,
    xsecs={
        13: Number(134.2, {
            "scale": (1.5, 1.1),
            "pdf": (2.1, 1.3),  # includes alpha_s
            "mtop": (1.0, 1.2),
            "beam": (0.2, 0.1),
            "integration": 0.1,
        }),
    },
)

st_tchannel_tbar = st_tchannel.add_process(
    name="st_tchannel_tbar",
    id=2120,
    xsecs={
        13: Number(80.0, {
            "scale": 0.8,
            "pdf": (1.6, 1.2),  # includes alpha_s
            "mtop": 0.7,
            "beam": (0.2, 0.1),
            "integration": 0.1,
        }),
    },
)

st_twchannel = st.add_process(
    name="st_twchannel",
    id=2200,
    label=f"{st.label}, tW-channel",
    xsecs={
        13: Number(79.3, {
            "scale": (1.9, 1.8),
            "pdf": 2.2,
            "mtop": 1.2,
            "beam": 0.2,
        }),
    },
)

st_twchannel_t = st_twchannel.add_process(
    name="st_twchannel_t",
    id=2210,
    xsecs={
        13: st_twchannel.get_xsec(13) / 2,
    },
)

st_twchannel_t_sl = st_twchannel_t.add_process(
    name="st_twchannel_t_sl",
    id=2211,
    xsecs={
        13: const.br_ww.sl * st_twchannel_t.get_xsec(13),
    },
)

st_twchannel_t_dl = st_twchannel_t.add_process(
    name="st_twchannel_t_dl",
    id=2212,
    xsecs={
        13: const.br_ww.dl * st_twchannel_t.get_xsec(13),
    },
)

st_twchannel_t_fh = st_twchannel_t.add_process(
    name="st_twchannel_t_fh",
    id=2213,
    xsecs={
        13: const.br_ww.fh * st_twchannel_t.get_xsec(13),
    },
)

st_twchannel_tbar = st_twchannel.add_process(
    name="st_twchannel_tbar",
    id=2220,
    xsecs={
        13: st_twchannel.get_xsec(13) / 2,
    },
)

st_twchannel_tbar_sl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_sl",
    id=2221,
    xsecs={
        13: const.br_ww.sl * st_twchannel_tbar.get_xsec(13),
    },
)

st_twchannel_tbar_dl = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_dl",
    id=2222,
    xsecs={
        13: const.br_ww.dl * st_twchannel_tbar.get_xsec(13),
    },
)

st_twchannel_tbar_fh = st_twchannel_tbar.add_process(
    name="st_twchannel_tbar_fh",
    id=2223,
    xsecs={
        13: const.br_ww.fh * st_twchannel_tbar.get_xsec(13),
    },
)

st_schannel = st.add_process(
    name="st_schannel",
    id=2300,
    label=f"{st.label}, s-channel",
    xsecs={
        13: Number(10.32, {
            "scale": (0.29, 0.24),
            "pdf": 0.27,
            "mtop": (0.23, 0.22),
            "beam": 0.01,
        }),
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
        13: Number(6.35, {
            "scale": (0.18, 0.15),
            "pdf": 0.14,
            "mtop": (0.14, 0.13),
            "beam": 0.01,
        }),
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
        13: Number(3.97, {
            "scale": (0.11, 0.09),
            "pdf": 0.15,
            "mtop": 0.09,
            "beam": 0.01,
        }),
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
# https://www.arxiv.org/pdf/2001.03031.pdf
#

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
    },
)

ttz_llnunu_m10 = ttz.add_process(
    name="ttz_llnunu_m10",  # non-hadronically decaying Z
    id=3110,
    xsecs={
        13: Number(0.2529, {
            "total": 0.0003378,
        }),  # Based on dataset TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8 in XSDB
    },
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
    },
)

ttw_lnu = ttw.add_process(
    name="ttw_lnu",
    id=3210,
    xsecs={
        13: const.br_w.lep * ttw.get_xsec(13),
    },
)

ttw_qq = ttw.add_process(
    name="ttw_qq",
    id=3220,
    xsecs={
        13: const.br_w.had * ttw.get_xsec(13),
    },
)

# define the combined ttv cross section as the sum of the two channels
ttv.set_xsec(
    13,
    ttz.get_xsec(13) + ttw.get_xsec(13),
)


#
# ttbar + 2 vector bosons
#
# https://arxiv.org/pdf/1610.07922.pdf page 165 Table 42
#

ttvv = Process(
    name="ttvv",
    id=4000,
    label=f"{tt.label} + VV",
)

ttzz = ttvv.add_process(
    name="ttzz",
    id=4100,
    xsecs={
        13: Number(1982E-6, {
            "scale": (0.052j, 0.090j),
            "pdf": 0.026j,
        }),
    },
)

ttwz = ttvv.add_process(
    name="ttwz",
    id=4200,
    xsecs={
        13: (
            Number(2705E-6, {"scale": (0.099j, 0.106j), "pdf": 0.027j}) +
            Number(1179E-6, {"scale": 0.112j, "pdf": 0.037j})
        ),
    },
)

ttww = ttvv.add_process(
    name="ttww",
    id=4300,
    xsecs={
        13: Number(8380E-6, {  # Calculation performed in 5FS
            "scale": (0.332j, 0.231j),
            "pdf": 0.030j,
        }),
    },
)

# define the combined ttvv cross section as the sum of the three channels
ttvv.set_xsec(
    13,
    ttzz.get_xsec(13) + ttwz.get_xsec(13) + ttww.get_xsec(13),
)
