# coding: utf-8

"""
HHH process definitions.
"""

ww_decay_modes = ["", "_qqlnu", "_2l2nu", "_4q"]
coupling_params = [
    ("0", "0"), ("0", "99"), ("19", "19"), ("1", "0"),
    ("1", "2"), ("2", "m1"), ("4", "9"), ("m1", "m1"),
    ("m1p5", "m0p5"), ("0", "m1"), ("m1", "0"),
]

hhh_coupling_params = [""]
for param in coupling_params:
    hhh_coupling_params.append(f"_c3{param[0]}_d4{param[1]}")

__all__ = [  # noqa: F822
    "hhh", "hhh_ggf", "hhh_4b2w",
] + [
    f"hhh{comb}"
    for comb in hhh_coupling_params
] + [
    f"hhh_4b2w{comb}"
    for comb in hhh_coupling_params
] + [
    f"hhh_4b2w{ww}{comb}"
    for comb in hhh_coupling_params
    for ww in ("_2l2nu", "_4q", "_qqlnu")
] + [  # noqa: F822
    # hypotheses for subdecay channels tautau (copied from Than)
    "hhh_4b2tau_c30_d40", "hhh_4b2tau_c30_d499", "hhh_4b2tau_c30_d4m1",  # noqa: F822
    "hhh_4b2tau_c319_d419", "hhh_4b2tau_c31_d40", "hhh_4b2tau_c31_d42",  # noqa: F822
    "hhh_4b2tau_c32_d4m1", "hhh_4b2tau_c34_d49", "hhh_4b2tau_c3m1_d40",  # noqa: F822
    "hhh_4b2tau_c3m1_d4m1", "hhh_4b2tau_c3m1p5_d4m0p5",  # noqa: F822
]


from order import Process
from scinum import Number
from functools import partial

import cmsdb.constants as const
from cmsdb.util import multiply_xsecs, DotDict, add_decay_process


hhh = Process(
    name="hhh",
    id=40000,
    label="HHH",
)

hhh_13tev_xs = Number(
    0.0894e-3,
    {"total": 0.2j},
)

hhh_ggf = hhh.add_process(
    name="hhh_ggf",
    id=41000,
    label=f"${hhh.label}^{{ggf}}$",
    xsecs={
        13: hhh_13tev_xs,
        13.6: hhh_13tev_xs + (0.103e-3 - 0.0894e-3) * 0.6,
        14: Number(
            0.103e-3,
            {"scale": (0.05j, 0.08j), "mtop": 0.15j},
        ),
    },
)

hhh_4b2w = hhh.add_process(
    name="hhh_4b2w",
    id=43000,
    label=f"{hhh.label} $\\rightarrow 4b2W$",
    xsecs=multiply_xsecs(hhh_ggf, 3 * const.br_h.ww * const.br_h.bb**2),
)


def xs_scaler(process_name=None, c3=None, d4=None):
    if not any([x for x in [c3, d4]]) and isinstance(process_name, str):
        tmp_process_name = process_name.replace("_c3", "_c3_").replace("_d4", "_d4_")
        parts = tmp_process_name.split("_")
        c3_idx = parts.index("c3") + 1
        d4_idx = parts.index("d4") + 1

        def convert_to_float(input):
            tmp = input.replace("m", "-")
            return float(tmp)

        c3 = convert_to_float(parts[c3_idx])
        d4 = convert_to_float(parts[d4_idx])

    return (
        1 - 0.79 * c3 - 0.10 * d4 + 0.81 * c3**2 - 0.16 * c3 * d4 + 1.6e-2 * d4**2 - 0.23 * c3**3 + 4.5e-2 * c3**2 * d4 + 3.5e-2 * c3**4  # noqa E501
    )


subdecay_dict = DotDict.wrap({
    "4b2tau": {
        "name": "4b2tau",
        "br": 3 * const.br_h.tt * const.br_h.bb**2,
        "id": 100,
        "label": r"$\rightarrow 4b2\tau$",
    },
    "4b2w": {
        "name": "4b2w",
        "br": 3 * const.br_h.ww * const.br_h.bb**2,
        "id": 200,
        "label": r"$\rightarrow 4b2W$",
    },
})

coupling_combinations = DotDict.wrap({
    "c30_d40": {"id": 1, "c3": 0, "d4": 0, "name": "c30_d40"},
    "c30_d499": {"id": 2, "c3": 0, "d4": 99, "name": "c30_d499"},
    "c30_d4m1": {"id": 3, "c3": 0, "d4": -1, "name": "c30_d4m1"},
    "c319_d419": {"id": 4, "c3": 19, "d4": 19, "name": "c319_d419"},
    "c31_d40": {"id": 5, "c3": 1, "d4": 0, "name": "c31_d40"},
    "c31_d42": {"id": 6, "c3": 1, "d4": 2, "name": "c31_d42"},
    "c32_d4m1": {"id": 7, "c3": 2, "d4": -1, "name": "c32_d4m1"},
    "c34_d49": {"id": 8, "c3": 4, "d4": 9, "name": "c34_d49"},
    "c3m1_d40": {"id": 9, "c3": -1, "d4": 0, "name": "c3m1_d40"},
    "c3m1_d4m1": {"id": 10, "c3": -1, "d4": -1, "name": "c3m1_d4m1"},
    "c3m1p5_d4m0p5": {"id": 11, "c3": -1.5, "d4": -0.5, "name": "c3m1p5_d4m0p5"},
})

# ----------------------------------------------------------
# 1) Create coupling parents under hhh (needed by util)
# ----------------------------------------------------------
for cdict in coupling_combinations.values():
    # __import__("IPython").embed()
    globals()[f"hhh_{cdict.name}"] = hhh.add_process(
        name=f"hhh_{cdict.name}",
        id=42000 + cdict.id,
        label=f"{hhh.label} $(c_{{3}}={cdict.c3}, d_{{4}}={cdict.d4})$",
        xsecs=multiply_xsecs(hhh_ggf, xs_scaler(c3=cdict.c3, d4=cdict.d4)),
    )

# ----------------------------------------------------------
# 2) Create coupling parents under hhh_ggf (xsec scaling)
# ----------------------------------------------------------
for cdict in coupling_combinations.values():
    globals()[f"hhh_ggf_{cdict.name}"] = hhh_ggf.add_process(
        name=f"hhh_ggf_{cdict.name}",
        id=41100 + cdict.id,
        label=f"{hhh_ggf.label} $(c_{{3}}={cdict.c3}, d_{{4}}={cdict.d4})$",
        xsecs=multiply_xsecs(hhh_ggf, xs_scaler(c3=cdict.c3, d4=cdict.d4)),
    )

# ----------------------------------------------------------
# 3) Add 4b2tau and 4b2w under each hhh_cXX_dYY
# ----------------------------------------------------------
for cdict in coupling_combinations.values():
    parent = globals()[f"hhh_{cdict.name}"]

    for dname, ddict in subdecay_dict.items():
        globals()[f"hhh_{dname}_{cdict.name}"] = parent.add_process(
            name=f"hhh_{dname}_{cdict.name}",
            id=parent.id + ddict.id,
            label=f"{parent.label} {ddict.label}",
            xsecs=multiply_xsecs(parent, ddict.br),
        )

# ----------------------------------------------------------
# 4) Add WW subdecays to 4b2w
# ----------------------------------------------------------
vv_decay_map = DotDict.wrap({
    "qqlnu": {"name": "_qqlnu", "id": 20, "label": r"$(qq\ell\nu)$", "br": -1},
    "2l2nu": {"name": "_2l2nu", "id": 40, "label": r"$(2\ell 2\nu)$", "br": -1},
    "4q": {"name": "_4q", "id": 60, "label": r"$(4q)$", "br": -1},
})

ww_decay_map = DotDict.wrap({
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("2l2nu", "4q", "qqlnu")
})
ww_decay_map["2l2nu"]["br"] = const.br_ww.dl
ww_decay_map["4q"]["br"] = const.br_ww.fh
ww_decay_map["qqlnu"]["br"] = const.br_ww.sl

# ----------------------------------------------------------
# 3.5) Create inclusive WW subdecays for hhh_4b2w
# ----------------------------------------------------------
for ww in ("2l2nu", "4q", "qqlnu"):
    globals()[f"hhh_4b2w_{ww}"] = hhh_4b2w.add_process(
        name=f"hhh_4b2w_{ww}",
        id=hhh_4b2w.id + ww_decay_map[ww]["id"],
        label=f"{hhh_4b2w.label} {ww_decay_map[ww]['label']}",
        xsecs=multiply_xsecs(hhh_4b2w, ww_decay_map[ww]["br"]),
    )


add_4b2v_sub_decay = partial(
    add_decay_process,
    name_func=lambda parent_name, decay_name: parent_name.replace(
        "4b2w", f"4b2w_{decay_name}", 1,
    ),
    label_func=lambda parent_label, decay_label: f"{parent_label}{decay_label}",
)

for cdict in coupling_combinations.values():
    parent = globals()[f"hhh_4b2w_{cdict.name}"]

    for ww in ("2l2nu", "4q", "qqlnu"):
        globals()[f"hhh_4b2w_{ww}_{cdict.name}"] = parent.add_process(
            name=f"hhh_4b2w_{ww}_{cdict.name}",
            id=parent.id + ww_decay_map[ww]["id"],
            label=f"{parent.label} {ww_decay_map[ww]['label']}",
            xsecs=multiply_xsecs(parent, ww_decay_map[ww]["br"]),
        )
