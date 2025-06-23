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
    "ttg", "ttg_pt10to100", "ttg_pt100to200", "ttg_pt200toinf",
    "tg", "tgqb",
    "ttv",
    "ttz", "ttz_zqq", "ttz_zlep_m10toinf", "ttz_zll_m4to50", "ttz_zll_m50toinf", "ttz_znunu",
    "ttw", "ttw_wlnu", "ttw_wqq",
    "ttvv",
    "ttzz", "ttwz", "ttww",
    "tttt",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs


#
# ttbar
# (ids up to 1999)
#
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO?rev=21#Updated_reference_cross_sections
# cross sections correspond to mtop = 172.5 GeV
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
# using updated tables from 2022
# t- and tw-channel:
#   - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=20#Predictions_for_top_quark_produc  # noqa
# s-channel:
#   - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=21 (NNLO)
#   - we used NLO before from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec?rev=36#Single_top_s_channel_cross_secti  # noqa
# tW-channel:
#   - the t and tbar channels contribute equally as stated in
#   - https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec?rev=36#Single_top_Wt_channel_cross_sect

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
            E_beam=0.2,
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
            scale=0.8,
            pdf=(1.6, 1.2),  # includes alpha_s
            mtop=0.7,
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
        # only scale uncertainty is given in the twiki
        # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=21
        13: Number(11.073, {
            "scale": (0.058, 0.034),
        }),
        13.6: Number(11.778, {
            "scale": (0.059, 0.043),
        }),
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
        # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=21
        # no scale uncertainties given for t/tbar subchannels, so assume 100% correlation and split
        # scale uncertainty on sum of t + tbar accordingly
        13: Number(6.828, {
            "scale": tuple(
                tot * 6.828 / st_schannel.get_xsec(13).n
                for tot in st_schannel.get_xsec(13).u("scale")
            ),
        }),
        13.6: Number(7.244, {
            "scale": tuple(
                tot * 7.244 / st_schannel.get_xsec(13.6).n
                for tot in st_schannel.get_xsec(13.6).u("scale")
            ),
        }),
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
        # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopNNLORef?rev=21
        # no scale uncertainties given for t/tbar subchannels, so assume 100% correlation and split
        # scale uncertainty on sum of t + tbar accordingly
        13: Number(4.245, {
            "scale": tuple(
                tot * 4.245 / st_schannel.get_xsec(13).n
                for tot in st_schannel.get_xsec(13).u("scale")
            ),
        }),
        13.6: Number(4.534, {
            "scale": tuple(
                tot * 4.534 / st_schannel.get_xsec(13.6).n
                for tot in st_schannel.get_xsec(13.6).u("scale")
            ),
        }),
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

st.set_xsec(
    13.6,
    st_tchannel.get_xsec(13.6) + st_twchannel.get_xsec(13.6) + st_schannel.get_xsec(13.6),
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
            "scale": (0.086j, 0.095j),
            "pdf": 0.023j,
        }),
        # from xsdb for ttz_zqq: https://xsdb-temp.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=process_name%3D%5ETTZ-ZtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8%24  # noqa
        13.6: Number(0.660300, {
            "total": 0.003767,
        }) / const.br_z.qq,
        14: Number(1.045, {
            "scale": (0.088j, 0.099j),
            "pdf": 0.031j,
        }),
    },
)

# based on GenXSecAnalyzer
# for TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8 (Summer20UL16, NLO)
# using command ./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1 -n 5000000  # noqa

# zlep = zll or znunu, both decays present in samples
ttz_zlep_m10toinf = ttz.add_process(
    name="ttz_zlep_m10toinf",  # non-hadronically decaying Z
    id=3110,
    xsecs={
        13: Number(0.2439, {
            "total": 0.0002995,
        }),
    },
)

ttz_zll_m4to50 = ttz.add_process(
    name="ttz_zll_m4to50",
    id=3115,
    xsecs={
        # XSDB
        13.6: Number(0.03949, {
            "total": 0.00002728,
        }),
    },
)

ttz_zll_m50toinf = ttz.add_process(
    name="ttz_zll_m50toinf",
    id=3116,
    xsecs={
        # XSDB
        13.6: Number(0.08646, {
            "total": 0.0000552,
        }),
    },
)

ttz_znunu = ttz.add_process(
    name="ttz_znunu",
    id=3118,
    xsecs={
        # XSDB
        13.6: Number(0.1638, {
            "total": 0.00007274,
        }),
    },
)

ttz_zqq = ttz.add_process(
    name="ttz_zqq",
    id=3120,
    xsecs=multiply_xsecs(ttz, const.br_z.qq),
)

ttw = ttv.add_process(
    name="ttw",
    id=3200,
    label=f"{tt.label} + W",
    xsecs={
        13: Number(0.592, {
            "scale": (0.261j, 0.162j),
            "pdf": 0.021j,
        }),
        # XSDB: only LO in database, estimate an energy scaling factor from LO samples and multiply
        # to 13 TeV value for now, TODO
        13.6: 0.2505 / 0.2149 * Number(0.592, {
            "scale": (0.261j, 0.162j),
            "pdf": 0.021j,
        }),
        14: Number(0.429, {  # ttW+
            "scale": (0.264j, 0.167j),
            "pdf": 0.032j,
        }) + Number(0.224, {  # ttW-
            "scale": (0.264j, 0.164j),
            "pdf": 0.036j,
        }),
    },
)

# set combined cross sections
for ecm in (13, 14):
    ttv.set_xsec(ecm, ttw.get_xsec(ecm) + ttz.get_xsec(ecm))

ttw_wlnu = ttw.add_process(
    name="ttw_wlnu",
    id=3210,
    xsecs=multiply_xsecs(ttw, const.br_w.lep),
)

ttw_wqq = ttw.add_process(
    name="ttw_wqq",
    id=3220,
    xsecs=multiply_xsecs(ttw, const.br_w.had),
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
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        13.6: Number(0.001562, {
            "tot": 0.0000003675,  # xsdb Number(0.001579, {"tot": 0.000003248})
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
        # 13.6 from GenXSecAnalyzer:
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS%3DTTWZ_TuneCP5_13p6TeV_madgraph-pythia8  # noqa
        13.6: Number(0.002715, {"tot": 5.963e-7}),  # might need a k-factor of 1.13 here
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
        # 13.6 from GenXSecAnalyzer:
        # similar values also found in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2023_179_v6.pdf
        13.6: Number(0.008165, {
            "tot": 0.000002113,  # xsdb Number(0.008203, {"tot": 0.00001404})
        }),
    },
)

# define the combined ttvv cross section as the sum of the three channels
for xs in (13, 13.6):
    ttvv.set_xsec(
        xs,
        ttzz.get_xsec(xs) + ttwz.get_xsec(xs) + ttww.get_xsec(xs),
    )
ttvv.set_xsec(
    13,
    ttzz.get_xsec(13) + ttwz.get_xsec(13) + ttww.get_xsec(13),
)

#
# 4 top quarks
#

tttt = Process(
    name="tttt",
    id=4400,
    label=r"$t\bar{t}t\bar{t}$",
    xsecs={
        # source: https://www.arxiv.org/abs/2212.03259
        13: Number(13.37e-03, {
            "scale": (0.48, 1.52),
            "pdf": 0.92,
        }),
        13.6: Number(15.82e-03, {
            "scale": (0.24, 1.83),
            "pdf": 1.06,
        }),
    },
)

#
# top quarks + photons
#


# ttg NLO k-factor taken from: https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2020/186 (v14)
k_factor_ttg = 1.4852
ttg = Process(
    name="ttg",
    id=4500,
    label=r"$t\bar{t} + \gamma$",
)

ttg_pt10to100 = ttg.add_process(
    name="ttg_pt10to100",
    id=4510,
    label=rf"{ttg.label}, $p_T^{{\gamma}} > 10 GeV$",
    xsecs={
        13.6: Number(4.216, {"tot": 0.02245}) * k_factor_ttg,  # source: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=39845888&currentPage=0&pageSize=10&searchQuery=DAS%3DTTG-1Jets_PTG-10to100_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8  # noqa: E501
    },
)

ttg_pt100to200 = ttg.add_process(
    name="ttg_pt100to200",
    id=4520,
    label=rf"{ttg.label}, $100 GeV < p_T^{{\gamma}} < 200 GeV$",
    xsecs={
        13.6: Number(0.4114, {"tot": 0.002858}) * k_factor_ttg,  # source: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=39845888&currentPage=0&pageSize=10&searchQuery=DAS%3DTTG-1Jets_PTG-100to200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8  # noqa: E501
    },
)

ttg_pt200toinf = ttg.add_process(
    name="ttg_pt200toinf",
    id=4530,
    label=rf"{ttg.label}, $p_T^{{\gamma}} > 200 GeV$",
    xsecs={
        13.6: Number(0.1284, {"tot": 0.0009248}) * k_factor_ttg,  # source: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=39845888&currentPage=0&pageSize=10&searchQuery=DAS%3DTTG-1Jets_PTG-200_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8  # noqa: E501
    },
)

# TODO: are there other top + gamma processes? Is it necessary to separate tg processes?
tg = Process(
    name="tg",
    id=4600,
    label=r"$t + \gamma$",
)

tgqb = tg.add_process(
    name="tgqb",
    id=4610,
    label=r"$t\gamma qb$",
    xsecs={
        13: Number(2.967),
        13.6: Number(3.873, {"tot": 0.006143}),  # source: https://xsecdb-xsdb-official.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=10&searchQuery=DAS%3DTGQB-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8  # noqa: E501
    },
)
