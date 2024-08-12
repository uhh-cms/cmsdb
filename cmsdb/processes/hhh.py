# coding: utf-8

"""
HHH process definitions.
"""

__all__ = [  # noqa: F822
    "hhh", "hhh_ggf", "coupling_combinations",
    # general coupling hypotheses for hhh
    "hhh_c30_d40", "hhh_c30_d499", "hhh_c30_d4m1", "hhh_c319_d419",
    "hhh_c31_d40", "hhh_c31_d42", "hhh_c32_d4m1", "hhh_c34_d49",
    "hhh_c3m1_d40", "hhh_c3m1_d4m1", "hhh_c3m1p5_d4m0p5",
    # hypotheses for subdecay channels
    "hhh_4b2tau_c30_d40", "hhh_4b2tau_c30_d499", "hhh_4b2tau_c30_d4m1",
    "hhh_4b2tau_c319_d419", "hhh_4b2tau_c31_d40", "hhh_4b2tau_c31_d42",
    "hhh_4b2tau_c32_d4m1", "hhh_4b2tau_c34_d49", "hhh_4b2tau_c3m1_d40",
    "hhh_4b2tau_c3m1_d4m1", "hhh_4b2tau_c3m1p5_d4m0p5",
]


from order import Process
from scinum import Number

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs, DotDict

hhh = Process(
    name="hhh",
    id=40000,
    label="HHH",
    xsecs={13.6: Number(0.1)},  # TODO
)

# source: HHH->6b analysis https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2023/028
# original paper: https://link.springer.com/content/pdf/10.1007/JHEP03(2020)155.pdf
hhh_ggf = hhh.add_process(
    name="hhh_ggf",
    id=41000,
    label=f"${hhh.label}^{{ggf}}$",
    xsecs={
        13: Number(
            0.45255713867289865e-3,  # might be NLO, need k-factor of 1.55?
        ),
        13.6: Number(0.1),
        14: Number(
            0.103e-3,  # NNLO value
            {
                "scale": (0.05j, 0.08j),
                "mtop": 0.15j,
            },
        ),
    },  # TODO
)


def xs_scaler(process_name=None, c3=None, d4=None):
    """
    scaling function originally taken from Maltoni et all: http://www.arxiv.org/pdf/1810.04665

    BEWARE: This scaling was originally done for HE-LHC, i.e. 27TeV.
    Still doing it now because the HHH->6b analysis also uses it
    """

    if not any([x for x in [c3, d4]]) and isinstance(process_name, str):

        # preprocess process name to better identfy parameter values
        tmp_process_name = process_name.replace("_c3", "_c3_").replace("_d4", "_d4_")
        # parse coupling values from process name
        parts = tmp_process_name.split("_")
        c3_idx = parts.index("c3") + 1
        d4_idx = parts.index("d4") + 1

        def convert_to_float(input):
            tmp = input.replace("m", "-")
            try:
                converted = float(tmp)

            except Exception as e:
                raise e
            return converted
        c3 = convert_to_float(parts[c3_idx])
        d4 = convert_to_float(parts[d4_idx])

    return (
        1 - 0.79 * c3 - 0.10 * d4 + 0.81 * c3**2 - 0.16 * c3 * d4 + 1.6e-2 * d4**2
        - 0.23 * c3**3 + 4.5e-2 * c3**2 * d4 + 3.5e-2 * c3**4  # noqa
    )  # noqa


subdecay_dict = DotDict.wrap({
    "4b2tau": {
        "name": "4b2tau",
        "br": 3 * const.br_h.tt * const.br_h.bb**2,
        "id": 100,
        "label": r"$\rightarrow 4b2\tau$",
    },
})

coupling_combinations = DotDict.wrap({
    "c30_d40": {
        "id": 1,
        "c3": 0,
        "d4": 0,
        "name": "c30_d40",
    },
    "c30_d499": {
        "id": 2,
        "c3": 0,
        "d4": 99,
        "name": "c30_d499",
    },
    "c30_d4m1": {
        "id": 3,
        "c3": 0,
        "d4": -1,
        "name": "c30_d4m1",
    },
    "c319_d419": {
        "id": 4,
        "c3": 19,
        "d4": 19,
        "name": "c319_d419",
    },
    "c31_d40": {
        "id": 5,
        "c3": 1,
        "d4": 0,
        "name": "c31_d40",
    },
    "c31_d42": {
        "id": 6,
        "c3": 1,
        "d4": 2,
        "name": "c31_d42",
    },
    "c32_d4m1": {
        "id": 7,
        "c3": 2,
        "d4": -1,
        "name": "c32_d4m1",
    },
    "c34_d49": {
        "id": 8,
        "c3": 4,
        "d4": 9,
        "name": "c34_d49",
    },
    "c3m1_d40": {
        "id": 9,
        "c3": -1,
        "d4": 0,
        "name": "c3m1_d40",
    },
    "c3m1_d4m1": {
        "id": 10,
        "c3": -1,
        "d4": -1,
        "name": "c3m1_d4m1",
    },
    "c3m1p5_d4m0p5": {
        "id": 11,
        "c3": -1.5,
        "d4": -0.5,
        "name": "c3m1p5_d4m0p5",
    },
})

for decay_name, decay_dict in subdecay_dict.items():
    for coupling_comb, coupling_dict in coupling_combinations.items():
        name = f"hhh_{coupling_dict.name}"
        subdecay_name = f"hhh_{decay_dict.name}_{coupling_dict.name}"
        c3 = coupling_dict.c3
        d4 = coupling_dict.d4

        locals().update({
            name: hhh_ggf.add_process(
                name=name,
                id=hhh_ggf.id + coupling_dict.id,
                label=f"{hhh_ggf.label} $(c_{{3}}={c3}, d_{{4}}={d4})$",
                xsecs=multiply_xsecs(hhh_ggf, xs_scaler(c3=c3, d4=d4)),  # TODO
            ),
        })

        tmp = locals().get(name)
        locals().update({
            subdecay_name: locals().get(name).add_process(
                name=subdecay_name,
                id=tmp.id + decay_dict.id,
                label=f"{tmp.label} {decay_dict.label}",
                xsecs=multiply_xsecs(tmp, decay_dict.br),
            )})

# BSM hypotheses
# XS \propto \kappa_{\lambda}*(1 + c3) * \kappa_{\lambda}*(1 + d4)
