# coding: utf-8

"""
Scientific constants.
"""

from scinum import Number, Correlation, combine_uncertainties

from cmsdb.util import DotDict

# misc
n_leps = Number(3)

# Z and W branching ratios and masses from
# https://pdg.lbl.gov/2023/tables/contents_tables.html
# Cut-off date for Listings/Summary Tables was Jan. 15, 2023, content of the 2023 Review of Particle Physics

# masses
m_z = Number(91.1876, {"z_mass": 0.0021})

# branching ratios
br_w = DotDict()
br_w["had"] = Number(0.6741, {"br_w_had": 0.0027})
br_w["lep"] = 1 - br_w.had

br_ww = DotDict(
    fh=br_w.had ** 2,
    dl=br_w.lep ** 2,
    sl=2 * ((br_w.had * Correlation(br_w_had=-1)) * br_w.lep),  # what does this correlation term do?
)

br_z = DotDict(
    qq=Number(0.69911, {"br_z_qq": 0.00056}),
    clep=Number(0.033658, {"br_z_clep": 0.000023}) * n_leps,
)

# higgs branching ratios from lhchwg, taken for mH = 125GeV
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR?rev=23

# explanation on uncertainties and how to combine them:
# https://cds.cern.ch/record/1416519/files/CERN-2012-002.pdf?version=1
# section 2.1.3 : procedure to determine uncertainties


br_h_ww_full = Number(0.2137, {"theo": (0.0099j, 0.0099j), "m_q": (0.0099j, 0.0098j), "alpha_s": (0.0066j, 0.0063j)})
br_h_zz_full = Number(0.02619, {"theo": (0.0099j, 0.0099j), "m_q": (0.0099j, 0.0098j), "alpha_s": (0.0066j, 0.0063j)})
br_h_gg_full = Number(0.002270, {"theo": (0.0173j, 0.0172j), "m_q": (0.0093j, 0.0099j), "alpha_s": (0.0061j, 0.0062j)})
br_h_bb_full = Number(0.5824, {"theo": (0.0065j, 0.0065j), "m_q": (0.0072j, 0.0074j), "alpha_s": (0.0078j, 0.0080j)})
br_h_tt_full = Number(0.06272, {"theo": (0.0117j, 0.0116j), "m_q": (0.0098j, 0.0099j), "alpha_s": (0.0062j, 0.0062j)})


def combine_uncertainties_higgs_br(number: Number):
    parametric_uncertainties = {
        direction: combine_uncertainties("+", number.u("m_q", direction), number.u("alpha_s", direction), rho=0)
        for direction in ["up", "down"]
    }
    return (
        combine_uncertainties("+", number.u("theo", direction), parametric_uncertainties[direction], rho=1)
        for direction in ["up", "down"]
    )


br_h = DotDict(
    ww=Number(br_h_ww_full.n, {"br_h_ww": tuple(combine_uncertainties_higgs_br(br_h_ww_full))}),
    zz=Number(br_h_zz_full.n, {"br_h_zz": tuple(combine_uncertainties_higgs_br(br_h_zz_full))}),
    gg=Number(br_h_gg_full.n, {"br_h_gg": tuple(combine_uncertainties_higgs_br(br_h_gg_full))}),
    bb=Number(br_h_bb_full.n, {"br_h_bb": tuple(combine_uncertainties_higgs_br(br_h_bb_full))}),
    tt=Number(br_h_tt_full.n, {"br_h_tt": tuple(combine_uncertainties_higgs_br(br_h_tt_full))}),
)


br_hh = DotDict(
    bbbb=br_h.bb ** 2,
    bbvv=2 * br_h.bb * (br_h.ww + br_h.zz),
    bbww=2 * br_h.bb * br_h.ww,
    bbzz=2 * br_h.bb * br_h.zz,
    bbtt=2 * br_h.bb * br_h.tt,
    bbgg=2 * br_h.bb * br_h.gg,
    ttww=2 * br_h.tt * br_h.ww,
    ttzz=2 * br_h.tt * br_h.zz,
    tttt=br_h.tt ** 2,
    wwww=br_h.ww ** 2,
    zzzz=br_h.zz ** 2,
    wwzz=2 * br_h.ww * br_h.zz,
    wwgg=2 * br_h.ww * br_h.gg,
)
