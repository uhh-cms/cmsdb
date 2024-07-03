# coding: utf-8

"""
HHH process definitions.
"""

__all__ = [
    "hhh", "hhh_ggf", "coupling_combinations"
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs

hhh = Process(
    name="hhh",
    id=40000,
    # label="HHH",
    label="",
    xsecs={13.6: Number(0.1)},  # TODO
)

# source: HHH->6b analysis https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2023/028
# original paper: https://link.springer.com/content/pdf/10.1007/JHEP03(2020)155.pdf
hhh_ggf = hhh.add_process(
    name="hhh_ggf",
    id=41000,
    # label=f"${hhh.label}^{{ggf}}$",
    label="",
    xsecs={
        13: Number(
            0.0894e-3 # at NNLO value taken from HHH->6b analysis
            # 0.45255713867289865e-3,  # might be NLO, need k-factor of 1.55?
        ),
        13.6: Number(
            0.0976e-3 # estimate only TODO
        ),
        14: Number(
                0.103e-3, # NNLO value
                {
                    "scale": (0.05j, 0.08j),
                    "mtop": 0.15j,
                }
            ),
    }, # TODO
)

def xs_scaler(process_name = None, c3=None, d4=None):
    """
    scaling function originally taken from Maltoni et all: http://www.arxiv.org/pdf/1810.04665

    BEWARE: This scaling was originally done for HE-LHC, i.e. 27TeV.
    Still doing it now because the HHH->6b analysis also uses it
    """
    
    if not any([x for x in [c3, d4]]) and isinstance(process_name, str):
        # parse coupling values from process name
        parts = process_name.split("_")
        c3_idx = parts.index("c3") + 1
        d4_idx = parts.index("d4") + 1

        def convert_to_float(input):
            tmp = input.replace("minus", "-")
            try:
                converted = float(tmp)
            
            except Exception as e:
                raise e
            return converted
        c3 = convert_to_float(parts[c3_idx])
        d4 = convert_to_float(parts[d4_idx])
        
    return (
        1 - 0.79*c3 - 0.10*d4 + 0.81*c3**2 - 0.16*c3*d4 + 1.6e-2*d4**2
        - 0.23*c3**3 + 4.5e-2*c3**2*d4 + 3.5e-2*c3**4
    )

template = "hhh_c3_{c3}_d4_{d4}"

coupling_combinations = (
    # (c3, d4)
    (0, 0),
    (0, 99),
    (0, -1),
    (19, 19),
    (1, 0),
    (1, 2),
    (2, -1),
    (4, 9),
    (-1, 0),
    (-1, -1),
    (-1.5, -0.5),
)

for i, (c3, d4) in enumerate(coupling_combinations, 1):
    name = template.format(
        c3=str(c3).replace("-", "minus").replace(".", "p"),
        d4=str(d4).replace("-", "minus").replace(".", "p"),
    )
    locals().update({
        name: hhh_ggf.add_process(
            name=name,
            id=hhh_ggf.id + i,
            label=f"{hhh_ggf.label} $(c_{{3}}={c3}, d_{{4}}={d4})$",
            xsecs=multiply_xsecs(hhh_ggf, xs_scaler(c3=c3, d4=d4)), # TODO
        )
    })
    __all__.append(name)

    tmp = locals().get(name)
    locals().update({
        f"{name}_4b2tau": locals().get(name).add_process(
            name=f"{name}_4b2tau",
            id=tmp.id + 100,
            # label=f"{tmp.label} $\\rightarrow 4b2\\tau$",
            label=f"{tmp.label}",
            xsecs=multiply_xsecs(tmp, 3*const.br_h.tt*const.br_h.bb**2)
        )})
    __all__.append(f"{name}_4b2tau")

# BSM hypotheses
# XS \propto \kappa_{\lambda}*(1 + c3) * \kappa_{\lambda}*(1 + d4)
