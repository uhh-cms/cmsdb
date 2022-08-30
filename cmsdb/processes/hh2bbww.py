# coding: utf-8

"""
HH -> bbWW process definitions.
"""

__all__ = [
    "hh_ggf_kt_1_kl_0_bbww_sl", "hh_ggf_kt_1_kl_1_bbww_sl", "hh_ggf_kt_1_kl_2p45_bbww_sl",
    "hh_ggf_kt_1_kl_5_bbww_sl",
]

import cmsdb.constants as const
from cmsdb.processes.higgs import (
    hh_ggf_kt_1_kl_0, hh_ggf_kt_1_kl_1, hh_ggf_kt_1_kl_2p45, hh_ggf_kt_1_kl_5,
)


#
# HH -> bbWW -> bbWWqqlnu
#

hh_ggf_kt_1_kl_0_bbww_sl = hh_ggf_kt_1_kl_0.add_process(
    name="hh_ggf_kt_1_kl_0_bbww_sl",
    id=21220,
    label=r"$\mathrm{HH \rightarrow bbWW(qql\nu), (\kappa_{\lambda}=0)}$",
    xsecs={
        13: hh_ggf_kt_1_kl_0.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_1_bbww_sl = hh_ggf_kt_1_kl_1.add_process(
    name="hh_ggf_kt_1_kl_1_bbww_sl",
    label=r"$\mathrm{HH \rightarrow bbWW(qql\nu), (\kappa_{\lambda}=1)}$",
    id=21221,
    xsecs={
        13: hh_ggf_kt_1_kl_1.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_2p45_bbww_sl = hh_ggf_kt_1_kl_2p45.add_process(
    name="hh_ggf_kt_1_kl_2p45_bbww_sl",
    label=r"$\mathrm{HH \rightarrow bbWW(qql\nu), (\kappa_{\lambda}=2.45)}$",
    id=21222,
    xsecs={
        13: hh_ggf_kt_1_kl_2p45.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)

hh_ggf_kt_1_kl_5_bbww_sl = hh_ggf_kt_1_kl_5.add_process(
    name="hh_ggf_kt_1_kl_5_bbww_sl",
    label=r"$\mathrm{HH \rightarrow bbWW(qql\nu), (\kappa_{\lambda}=5)}$",
    id=21223,
    xsecs={
        13: hh_ggf_kt_1_kl_5.get_xsec(13) * const.br_hh.bbww * const.br_ww.sl,
    },
)
