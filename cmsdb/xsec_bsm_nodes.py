from __future__ import annotations

# A_i fitparameter according to recommendation in "https://arxiv.org/pdf/1610.07922.pdf" S.201
_a_fit_parameter = {
    13: {
        "A_1": 2.09,
        "A_2": 10.15,
        "A_3": 0.28,
        "A_4": 0.10,
        "A_5": 1.33,
        "A_6": -8.51,
        "A_7": -1.37,
        "A_8": 2.83,
        "A_9": 1.46,
        "A_10": -4.92,
        "A_11": -0.68,
        "A_12": 1.86,
        "A_13": 0.32,
        "A_14": -0.84,
        "A_15": -0.57,
    },
    14: {
        "A_1": 2.08,
        "A_2": 10.20,
        "A_3": 0.28,
        "A_4": 0.10,
        "A_5": 1.37,
        "A_6": -8.49,
        "A_7": -1.36,
        "A_8": 2.80,
        "A_9": 1.44,
        "A_10": -4.90,
        "A_11": -0.66,
        "A_12": 1.84,
        "A_13": 0.32,
        "A_14": -0.83,
        "A_15": -0.56,
    },
}

# TODO: plain copy of 13 TeV values for now as there are no 13.6 TeV values
_a_fit_parameter[13.6] = _a_fit_parameter[13]

# chosen EFT parameter according to "https://arxiv.org/pdf/1610.07922.pdf" S.202
_coefficient_EFT_benchmarks = {
    1: {
        "k_l": 7.5,
        "k_t": 1.0,
        "c_2": -1.0,
        "c_g": 0.0,
        "c_2_g": 0.0,
    },
    2: {
        "k_l": 1.0,
        "k_t": 1.0,
        "c_2": 0.5,
        "c_g": -0.8,
        "c_2_g": 0.6,
    },
    3: {
        "k_l": 1.0,
        "k_t": 1.0,
        "c_2": -1.5,
        "c_g": 0.0,
        "c_2_g": -0.8,
    },
    4: {
        "k_l": -3.5,
        "k_t": 1.5,
        "c_2": -3.0,
        "c_g": 0.0,
        "c_2_g": 0.0,
    },
    5: {
        "k_l": 1.0,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": 0.8,
        "c_2_g": -1,
    },
    6: {
        "k_l": 2.4,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": 0.2,
        "c_2_g": -0.2,
    },
    7: {
        "k_l": 5.0,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": 0.2,
        "c_2_g": -0.2,
    },
    8: {
        "k_l": 15.0,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": -1,
        "c_2_g": 1,
    },
    9: {
        "k_l": 1.0,
        "k_t": 1.0,
        "c_2": 1.0,
        "c_g": -0.6,
        "c_2_g": 0.6,
    },
    10: {
        "k_l": 10.0,
        "k_t": 1.5,
        "c_2": -1.0,
        "c_g": 0.0,
        "c_2_g": 0.0,
    },
    11: {
        "k_l": 2.4,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": 1,
        "c_2_g": -1,
    },
    12: {
        "k_l": 15.0,
        "k_t": 1.0,
        "c_2": 1.0,
        "c_g": 0.0,
        "c_2_g": 0.0,
    },
    "SM": {
        "k_l": 1.0,
        "k_t": 1.0,
        "c_2": 0.0,
        "c_g": 0.0,
        "c_2_g": 0.0,
    },
}


def calculate_r_hh(center_of_mass_energy: float, k_l: float, k_t: float, c_2: float, c_g: float, c_2_g: float): # noqa
    # formula for r_hh is defined in https://arxiv.org/pdf/1610.07922.pdf S.200
    # rename fit parameter
    a = _a_fit_parameter[center_of_mass_energy]

    # split calculation in parts for more readability
    formular = [
        a["A_1"] * k_t ** 4,
        a["A_2"] * c_2 ** 2,
        a["A_3"] * k_t ** 2 * k_l ** 2,
        a["A_4"] * c_g ** 2 * k_l ** 2,
        a["A_5"] * c_2_g ** 2,
        a["A_6"] * c_2 * k_t ** 2,
        a["A_7"] * k_t * k_l * k_t ** 2,
        a["A_8"] * k_t * k_l * c_2,
        a["A_9"] * c_g * k_l * c_2,
        a["A_10"] * c_2 * c_2_g,
        a["A_11"] * c_g * k_l * k_t ** 2,
        a["A_12"] * c_2_g * k_t ** 2,
        a["A_13"] * k_l * c_g * k_t * k_l,
        a["A_14"] * c_2_g * k_t * k_l,
        a["A_15"] * c_g * c_2_g * k_l,
    ]
    return sum(formular)


def calculate_xsec_node(center_of_mass_energy: float, xsec_sm: float, node_number: int): # noqa
    """

    Formula to calculate cross section for BSM nodes in EFT in pb.
    The exact procedure is described in the Yellow Pages Report 4.
    https://arxiv.org/pdf/1610.07922.pdf S.200

    For 13.6 TeV no table values are given.
    TODO: maybe do an interpolation between 13 and 14 TeV? Or wait for further information

    Args:
        center_of_mass_energy (float): Energy in TeV
        xsec_sm (float): Cross section of the Standard Model process in pb
        node_numbers int): Node number for which you want to calculate the xsec.

    Returns:
        TYPE: Description
    """
    if node_number not in list(range(1, 13)):
        raise ValueError(f"Node number is {node_number}, but must be between 1 and 12")

    eft_coefficients = _coefficient_EFT_benchmarks[node_number]
    r_hh = calculate_r_hh(center_of_mass_energy, **eft_coefficients)
    xsec_bsm = xsec_sm * r_hh
    return xsec_bsm
