# coding: utf-8

"""
Minimal set of external information and helpers to access cross sections extracted from stitching methods.
"""

from __future__ import annotations

import functools
import fnmatch

from scinum import Number


def _get_stitched_xsec(xsecs: dict[str, Number], name: str, ecm: float, *process_patterns: str) -> Number:
    if ecm != 13.6:
        raise NotImplementedError(f"ecm {ecm} not existing for stitched DY xsecs")

    # start with zero
    xsec = Number(0.0)

    # loop over processes and compare patterns
    for proc, _xsec in xsecs.items():
        if any(fnmatch.fnmatch(proc, pattern) for pattern in process_patterns):
            # add with uncorrelated uncertainties
            xsec.add(_xsec, rho=0.0, inplace=True)

    return xsec


# retrieved in 2022preEE from inclusive and exclusive samples, checking LHE-level quantities and comparing
# mc weight sum ratios
_dy_lep_m50toinf_13p6_xsecs = {
    "dy_ee_m50toinf_0j": Number(0.263901, 7.9e-05j),
    "dy_ee_m50toinf_1j_pt0to40": Number(0.0236902, 0.000165j),
    "dy_ee_m50toinf_1j_pt40to100": Number(0.0241268, 0.000133j),
    "dy_ee_m50toinf_1j_pt100to200": Number(0.00224175, 0.00046j),
    "dy_ee_m50toinf_1j_pt200to400": Number(0.000166087, 0.002005j),
    "dy_ee_m50toinf_1j_pt400to600": Number(5.96737e-06, 0.011408j),
    "dy_ee_m50toinf_1j_pt600toinf": Number(7.11127e-07, 0.033876j),
    "dy_ee_m50toinf_2j_pt0to40": Number(0.00727723, 0.000238j),
    "dy_ee_m50toinf_2j_pt40to100": Number(0.00898891, 0.000207j),
    "dy_ee_m50toinf_2j_pt100to200": Number(0.00269258, 0.000287j),
    "dy_ee_m50toinf_2j_pt200to400": Number(0.000375252, 0.000879j),
    "dy_ee_m50toinf_2j_pt400to600": Number(2.232e-05, 0.003899j),
    "dy_ee_m50toinf_2j_pt600toinf": Number(3.66072e-06, 0.009645j),
    "dy_mumu_m50toinf_0j": Number(0.264006, 7.9e-05j),
    "dy_mumu_m50toinf_1j_pt0to40": Number(0.0237118, 0.000165j),
    "dy_mumu_m50toinf_1j_pt40to100": Number(0.0241365, 0.000133j),
    "dy_mumu_m50toinf_1j_pt100to200": Number(0.00224151, 0.00046j),
    "dy_mumu_m50toinf_1j_pt200to400": Number(0.000166037, 0.002j),
    "dy_mumu_m50toinf_1j_pt400to600": Number(5.93393e-06, 0.011408j),
    "dy_mumu_m50toinf_1j_pt600toinf": Number(7.15219e-07, 0.033876j),
    "dy_mumu_m50toinf_2j_pt0to40": Number(0.00725694, 0.000238j),
    "dy_mumu_m50toinf_2j_pt40to100": Number(0.00897647, 0.000207j),
    "dy_mumu_m50toinf_2j_pt100to200": Number(0.00269189, 0.000287j),
    "dy_mumu_m50toinf_2j_pt200to400": Number(0.000375735, 0.000878j),
    "dy_mumu_m50toinf_2j_pt400to600": Number(2.24714e-05, 0.003899j),
    "dy_mumu_m50toinf_2j_pt600toinf": Number(3.69952e-06, 0.009645j),
    "dy_tautau_m50toinf_0j": Number(0.263458, 6.8e-05j),
    "dy_tautau_m50toinf_1j_pt0to40": Number(0.0236712, 0.000117j),
    "dy_tautau_m50toinf_1j_pt40to100": Number(0.0241854, 0.000119j),
    "dy_tautau_m50toinf_1j_pt100to200": Number(0.00225663, 0.000459j),
    "dy_tautau_m50toinf_1j_pt200to400": Number(0.000166239, 0.002005j),
    "dy_tautau_m50toinf_1j_pt400to600": Number(5.9539e-06, 0.011408j),
    "dy_tautau_m50toinf_1j_pt600toinf": Number(7.13889e-07, 0.033876j),
    "dy_tautau_m50toinf_2j_pt0to40": Number(0.0072732, 0.000151j),
    "dy_tautau_m50toinf_2j_pt40to100": Number(0.0090155, 0.000146j),
    "dy_tautau_m50toinf_2j_pt100to200": Number(0.00270554, 0.000218j),
    "dy_tautau_m50toinf_2j_pt200to400": Number(0.000380332, 0.000655j),
    "dy_tautau_m50toinf_2j_pt400to600": Number(2.21629e-05, 0.003084j),
    "dy_tautau_m50toinf_2j_pt600toinf": Number(3.75471e-06, 0.007865j),
}
get_stitched_dy_m50toinf_xsec = functools.partial(_get_stitched_xsec, _dy_lep_m50toinf_13p6_xsecs, "DY")

_w_lnu_13p6_xsecs = {
    "w_lnu_0j": Number(0.808247, 2.2e-05j),
    "w_lnu_1j_pt0to40": Number(0.0688332, 0.000139j),
    "w_lnu_1j_pt40to100": Number(0.0645822, 0.000141j),
    "w_lnu_1j_pt100to200": Number(0.00538203, 0.000402j),
    "w_lnu_1j_pt200to400": Number(0.000373607, 0.001777j),
    "w_lnu_1j_pt400to600": Number(1.26886e-05, 0.010522j),
    "w_lnu_1j_pt600toinf": Number(1.59701e-06, 0.031335j),
    "w_lnu_2j_pt0to40": Number(0.0215056, 0.000214j),
    "w_lnu_2j_pt40to100": Number(0.0237533, 0.000212j),
    "w_lnu_2j_pt100to200": Number(0.00640614, 0.000282j),
    "w_lnu_2j_pt200to400": Number(0.000845196, 0.000764j),
    "w_lnu_2j_pt400to600": Number(4.87396e-05, 0.003524j),
    "w_lnu_2j_pt600toinf": Number(8.27863e-06, 0.008918j),
}
get_stitched_w_lnu_xsec = functools.partial(_get_stitched_xsec, _w_lnu_13p6_xsecs, "W->lnu")
