# coding: utf-8

"""
HHH process definitions.
"""

__all__ = [
    "hhh", "hhh_ggf", "hhh_ggf_4b2tau",
]


from order import Process
from scinum import Number

import cmsdb.constants as const

hhh = Process(
    name="hhh",
    id=40000,
    label="HHH",
    xsecs={13.6: Number(0.1)},  # TODO
)

hhh_ggf = hhh.add_process(
    name="hhh_ggf",
    id=41000,
    label=f"${hhh.label}^{{ggf}}$",
    xsecs={13.6: Number(0.1)},  # TODO
)

hhh_ggf_4b2tau = hhh_ggf.add_process(
    name="hhh_ggf_4b2tau",
    id=41100,
    label=f"${hhh.label}_{{ggf}} \\rightarrow 4b2\\tau$",
    xsecs={13.6: hhh_ggf.get_xsec(13.6) * 3 * const.br_h.tt * const.br_h.bb**2},  # TODO
)

# BSM hypotheses
# XS \propto \kappa_{\lambda}*(1 + c3) * \kappa_{\lambda}*(1 + d4)
