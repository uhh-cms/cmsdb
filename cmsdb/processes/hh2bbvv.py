# coding: utf-8

"""
HH -> bbVV process definitions.

IDs are assigned in the range 21200-21499 for hh_ggf and 22200-22499 for hh_vbf.
bbWW processes are assigned IDs in the range 21200-21299 and 22200-22299.
bbZZ processes are assigned IDs in the range 21300-21399 and 22300-22399.
bbVV processes are assigned IDs in the range 21400-21499 and 22400-22499.
qqlnu processes are assigned the ranges from 10-19 and 2l2nu processes from 20-29 (FH still missing)
The merged processes are assigned the ranges from 1-9.
"""

__all__ = [
    # HH -> bbVV, ggf
    "hh_ggf_hbb_hvv", "hh_ggf_kl_0_kt_1_hbb_hvv", "hh_ggf_kl_1_kt_1_hbb_hvv",
    "hh_ggf_kl_2p45_kt_1_hbb_hvv", "hh_ggf_kl_5_kt_1_hbb_hvv",
    # HH -> bbVV, vbf
    "hh_vbf_hbb_hvv", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv",
    # HH -> bbVV(2qlv), ggf
    "hh_ggf_hbb_hvvqqlnu", "hh_ggf_kl_0_kt_1_hbb_hvvqqlnu", "hh_ggf_kl_1_kt_1_hbb_hvvqqlnu",
    "hh_ggf_kl_2p45_kt_1_hbb_hvvqqlnu", "hh_ggf_kl_5_kt_1_hbb_hvvqqlnu",
    # HH -> bbVV(2qlv), vbf
    "hh_vbf_hbb_hvvqqlnu", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvvqqlnu", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvvqqlnu",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hvvqqlnu", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hvvqqlnu", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hvvqqlnu",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hvvqqlnu", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hvvqqlnu",
    # HH -> bbVV(2l2v), ggf
    "hh_ggf_hbb_hvv2l2nu", "hh_ggf_kl_0_kt_1_hbb_hvv2l2nu", "hh_ggf_kl_1_kt_1_hbb_hvv2l2nu",
    "hh_ggf_kl_2p45_kt_1_hbb_hvv2l2nu", "hh_ggf_kl_5_kt_1_hbb_hvv2l2nu",
    # HH -> bbVV(2l2v), vbf
    "hh_vbf_hbb_hvv2l2nu", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv2l2nu", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv2l2nu",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv2l2nu", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv2l2nu", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv2l2nu",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv2l2nu", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv2l2nu",
    # HH -> bbWW, ggf
    "hh_ggf_hbb_hww", "hh_ggf_kl_0_kt_1_hbb_hww", "hh_ggf_kl_1_kt_1_hbb_hww",
    "hh_ggf_kl_2p45_kt_1_hbb_hww", "hh_ggf_kl_5_kt_1_hbb_hww",
    # HH -> bbWW, vbf
    "hh_vbf_hbb_hww", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hww", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hww", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hww",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hww", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hww",
    # HH -> bbWW(qqlv), ggf
    "hh_ggf_hbb_hwwqqlnu", "hh_ggf_kl_0_kt_1_hbb_hwwqqlnu", "hh_ggf_kl_1_kt_1_hbb_hwwqqlnu",
    "hh_ggf_kl_2p45_kt_1_hbb_hwwqqlnu", "hh_ggf_kl_5_kt_1_hbb_hwwqqlnu",
    # HH -> bbWW(lvlv), ggf
    "hh_ggf_hbb_hww2l2nu", "hh_ggf_kl_0_kt_1_hbb_hww2l2nu", "hh_ggf_kl_1_kt_1_hbb_hww2l2nu",
    "hh_ggf_kl_2p45_kt_1_hbb_hww2l2nu", "hh_ggf_kl_5_kt_1_hbb_hww2l2nu",
    # HH -> bbWW(qqlv), vbf
    "hh_vbf_hbb_hwwqqlnu", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hwwqqlnu", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hwwqqlnu",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hwwqqlnu", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hwwqqlnu", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hwwqqlnu",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hwwqqlnu", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hwwqqlnu",
    # HH -> bbWW(lvlv), vbf
    "hh_vbf_hbb_hww2l2nu", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww2l2nu", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww2l2nu",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hww2l2nu", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hww2l2nu", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hww2l2nu",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hww2l2nu", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hww2l2nu",
    "hh_ggf_hbb_hzz",
    # HH -> bbZZ, ggf
    "hh_ggf_hbb_hzz", "hh_ggf_kl_0_kt_1_hbb_hzz", "hh_ggf_kl_1_kt_1_hbb_hzz",
    "hh_ggf_kl_2p45_kt_1_hbb_hzz", "hh_ggf_kl_5_kt_1_hbb_hzz",
    # HH -> bbZZ, vbf
    "hh_vbf_hbb_hzz", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz",
    # HH -> bbZZ(lvlv), ggf
    "hh_ggf_hbb_hzz2l2nu", "hh_ggf_kl_0_kt_1_hbb_hzz2l2nu", "hh_ggf_kl_1_kt_1_hbb_hzz2l2nu",
    "hh_ggf_kl_2p45_kt_1_hbb_hzz2l2nu", "hh_ggf_kl_5_kt_1_hbb_hzz2l2nu",
    # HH -> bbZZ(lvlv), vbf
    "hh_vbf_hbb_hzz2l2nu", "hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz2l2nu", "hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz2l2nu",
    "hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz2l2nu", "hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz2l2nu", "hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz2l2nu",
    "hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz2l2nu", "hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz2l2nu",
    # Resonant HH -> bbWW: radion
    "radion_hh_ggf_bbww",
    "radion_hh_ggf_bbww_m250", "radion_hh_ggf_bbww_m260", "radion_hh_ggf_bbww_m270",
    "radion_hh_ggf_bbww_m280", "radion_hh_ggf_bbww_m300", "radion_hh_ggf_bbww_m320",
    "radion_hh_ggf_bbww_m350", "radion_hh_ggf_bbww_m400", "radion_hh_ggf_bbww_m450",
    "radion_hh_ggf_bbww_m500", "radion_hh_ggf_bbww_m550", "radion_hh_ggf_bbww_m600",
    "radion_hh_ggf_bbww_m650", "radion_hh_ggf_bbww_m700", "radion_hh_ggf_bbww_m750",
    "radion_hh_ggf_bbww_m800", "radion_hh_ggf_bbww_m850", "radion_hh_ggf_bbww_m900",
    "radion_hh_ggf_bbww_m1000", "radion_hh_ggf_bbww_m1250", "radion_hh_ggf_bbww_m1500",
    "radion_hh_ggf_bbww_m1750", "radion_hh_ggf_bbww_m2000", "radion_hh_ggf_bbww_m2500",
    "radion_hh_ggf_bbww_m3000",
    # Resonant HH -> bbWW: graviton
    "graviton_hh_ggf_bbww",
    "graviton_hh_ggf_bbww_m250", "graviton_hh_ggf_bbww_m260",
    "graviton_hh_ggf_bbww_m270", "graviton_hh_ggf_bbww_m280",
    "graviton_hh_ggf_bbww_m300", "graviton_hh_ggf_bbww_m320",
    "graviton_hh_ggf_bbww_m350", "graviton_hh_ggf_bbww_m400",
    "graviton_hh_ggf_bbww_m450", "graviton_hh_ggf_bbww_m500",
    "graviton_hh_ggf_bbww_m550", "graviton_hh_ggf_bbww_m600",
    "graviton_hh_ggf_bbww_m650", "graviton_hh_ggf_bbww_m700",
    "graviton_hh_ggf_bbww_m750", "graviton_hh_ggf_bbww_m800",
    "graviton_hh_ggf_bbww_m850", "graviton_hh_ggf_bbww_m900",
    "graviton_hh_ggf_bbww_m1000", "graviton_hh_ggf_bbww_m1250",
    "graviton_hh_ggf_bbww_m1500", "graviton_hh_ggf_bbww_m1750",
    "graviton_hh_ggf_bbww_m2000", "graviton_hh_ggf_bbww_m2500",
    "graviton_hh_ggf_bbww_m3000",
]

from scinum import Number
from functools import partial

import cmsdb.constants as const
from cmsdb.util import (
    multiply_xsecs, DotDict, add_decay_process, add_sub_decay_process,
    add_the_production_mode_parent,
)
add_bbvv_decay_process = partial(add_decay_process, label_separator="")


from cmsdb.processes.hh import (
    hh_ggf, hh_ggf_kl_0_kt_1, hh_ggf_kl_1_kt_1, hh_ggf_kl_2p45_kt_1, hh_ggf_kl_5_kt_1,
    hh_vbf, hh_vbf_kv_1_k2v_1_kl_1, hh_vbf_kv_1_k2v_1_kl_0, hh_vbf_kv_1_k2v_1_kl_2,
    hh_vbf_kv_1_k2v_0_kl_1, hh_vbf_kv_1_k2v_2_kl_1, hh_vbf_kv_0p5_k2v_1_kl_1, hh_vbf_kv_1p5_k2v_1_kl_1,
    radion_hh_ggf, graviton_hh_ggf,
)

#
# Helper
#

hh_decay_map = DotDict.wrap({
    "hbb_hvv": {
        "name": "hbb_hvv",
        "id": 400,
        "br": const.br_hh.bbww + const.br_hh.bbzz,
        "label": r"$\rightarrow bbVV$",
    },
    "hbb_hww": {
        "name": "hbb_hww",
        "id": 200,
        "br": const.br_hh.bbww,
        "label": r"$\rightarrow bbWW$",
    },
    "hbb_hzz": {
        "name": "hbb_hzz",
        "id": 300,
        "br": const.br_hh.bbzz,
        "label": r"$\rightarrow bbZZ$",
    },
})

vv_decay_map = DotDict.wrap({
    "qqlnu": {
        "name": "qqlnu",
        "id": 10,
        "label": r"$(qq\ell\nu)$",
        "br": const.br_ww.sl,
    },
    "2l2nu": {
        "name": "2l2nu",
        "id": 20,
        "label": r"$(2\ell 2\nu)$",
        "br": const.br_ww.dl + const.br_zz.llnunu,
    },
    "4q": {
        "name": "4q",
        "id": 30,
        "label": r"$(4q)$",
        "br": const.br_ww.fh + const.br_zz.qqqq,
    },
    # NOTE: we could also add the remaining ZZ decay modes
})

from cmsdb.processes.higgs import ww_decay_map, zz_decay_map


def add_hvv_decay(base_process, hvv_parent, decay_map: DotDict, add_production_mode_parent=True):
    """
    Custom function to add sub processes, where the base process and the direct parent are not the same

    :param base_process: the parent process that is the production mode
    :param hvv_parent: the parent process that is the direct parent
    :param decay_map: Dictionary with decay channel information.
    """
    kwargs = {
        "name": f"{base_process.name}_{decay_map.name}",
        "id": base_process.id + decay_map.id,
        "label": f"{base_process.label}{decay_map.label}",
        "xsecs": multiply_xsecs(base_process, decay_map.br),
    }

    child = hvv_parent.add_process(**kwargs)

    if add_production_mode_parent:
        add_the_production_mode_parent(child, base_process)

    return child


#############################################################
#
# HH -> bbVV
#
#############################################################

#
# HH -> bbVV (incl)
#

hh_ggf_hbb_hvv = add_bbvv_decay_process(hh_ggf, hh_decay_map.hbb_hvv, add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hvv = add_bbvv_decay_process(hh_ggf_kl_0_kt_1, hh_decay_map.hbb_hvv)
hh_ggf_kl_1_kt_1_hbb_hvv = add_bbvv_decay_process(hh_ggf_kl_1_kt_1, hh_decay_map.hbb_hvv)
hh_ggf_kl_2p45_kt_1_hbb_hvv = add_bbvv_decay_process(hh_ggf_kl_2p45_kt_1, hh_decay_map.hbb_hvv)
hh_ggf_kl_5_kt_1_hbb_hvv = add_bbvv_decay_process(hh_ggf_kl_5_kt_1, hh_decay_map.hbb_hvv)


hh_vbf_hbb_hvv = add_bbvv_decay_process(hh_vbf, hh_decay_map.hbb_hvv, add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1_k2v_1_kl_1, hh_decay_map.hbb_hvv)
hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1_k2v_1_kl_0, hh_decay_map.hbb_hvv)
hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1_k2v_1_kl_2, hh_decay_map.hbb_hvv)
hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1_k2v_0_kl_1, hh_decay_map.hbb_hvv)
hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1_k2v_2_kl_1, hh_decay_map.hbb_hvv)
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1, hh_decay_map.hbb_hvv)
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv = add_bbvv_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1, hh_decay_map.hbb_hvv)

#
# HH -> bbVV(qqlv), ggf
#

hh_ggf_hbb_hvv2l2nu = add_sub_decay_process(hh_ggf_hbb_hvv, vv_decay_map["2l2nu"], add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hvv2l2nu = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_ggf_kl_1_kt_1_hbb_hvv2l2nu = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_ggf_kl_2p45_kt_1_hbb_hvv2l2nu = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_ggf_kl_5_kt_1_hbb_hvv2l2nu = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hvv, vv_decay_map["2l2nu"])

hh_vbf_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_hbb_hvv, vv_decay_map["2l2nu"], add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["2l2nu"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv2l2nu = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["2l2nu"])

hh_ggf_hbb_hvvqqlnu = add_sub_decay_process(hh_ggf_hbb_hvv, vv_decay_map["qqlnu"], add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hvvqqlnu = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_ggf_kl_1_kt_1_hbb_hvvqqlnu = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_ggf_kl_2p45_kt_1_hbb_hvvqqlnu = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_ggf_kl_5_kt_1_hbb_hvvqqlnu = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hvv, vv_decay_map["qqlnu"])

hh_vbf_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_hbb_hvv, vv_decay_map["qqlnu"], add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["qqlnu"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvvqqlnu = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["qqlnu"])

hh_ggf_hbb_hvv4q = add_sub_decay_process(hh_ggf_hbb_hvv, vv_decay_map["4q"], add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hvv4q = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hvv, vv_decay_map["4q"])
hh_ggf_kl_1_kt_1_hbb_hvv4q = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hvv, vv_decay_map["4q"])
hh_ggf_kl_2p45_kt_1_hbb_hvv4q = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hvv, vv_decay_map["4q"])
hh_ggf_kl_5_kt_1_hbb_hvv4q = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hvv, vv_decay_map["4q"])

hh_vbf_hbb_hvv4q = add_sub_decay_process(hh_vbf_hbb_hvv, vv_decay_map["4q"], add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["4q"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv4q = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv, vv_decay_map["4q"])


####################################################################################################
#
# HH -> bbWW
#
####################################################################################################


hh_ggf_hbb_hww = add_hvv_decay(hh_ggf, hh_ggf_hbb_hvv, hh_decay_map.hbb_hww, add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hww = add_hvv_decay(hh_ggf_kl_0_kt_1, hh_ggf_kl_0_kt_1_hbb_hvv, hh_decay_map.hbb_hww)
hh_ggf_kl_1_kt_1_hbb_hww = add_hvv_decay(hh_ggf_kl_1_kt_1, hh_ggf_kl_1_kt_1_hbb_hvv, hh_decay_map.hbb_hww)
hh_ggf_kl_2p45_kt_1_hbb_hww = add_hvv_decay(hh_ggf_kl_2p45_kt_1, hh_ggf_kl_2p45_kt_1_hbb_hvv, hh_decay_map.hbb_hww)
hh_ggf_kl_5_kt_1_hbb_hww = add_hvv_decay(hh_ggf_kl_5_kt_1, hh_ggf_kl_5_kt_1_hbb_hvv, hh_decay_map.hbb_hww)

hh_vbf_hbb_hww = add_hvv_decay(hh_vbf, hh_vbf_hbb_hvv, hh_decay_map.hbb_hww, add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hww = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_1, hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_1_k2v_1_kl_0_hbb_hww = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_0, hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_1_k2v_1_kl_2_hbb_hww = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_2, hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_1_k2v_0_kl_1_hbb_hww = add_hvv_decay(hh_vbf_kv_1_k2v_0_kl_1, hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_1_k2v_2_kl_1_hbb_hww = add_hvv_decay(hh_vbf_kv_1_k2v_2_kl_1, hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww = add_hvv_decay(hh_vbf_kv_0p5_k2v_1_kl_1, hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hww)  # noqa
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww = add_hvv_decay(hh_vbf_kv_1p5_k2v_1_kl_1, hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hww)  # noqa

hh_ggf_hbb_hww2l2nu = add_sub_decay_process(hh_ggf_hbb_hww, ww_decay_map["2l2nu"])
hh_ggf_kl_0_kt_1_hbb_hww2l2nu = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hww, ww_decay_map["2l2nu"])
hh_ggf_kl_1_kt_1_hbb_hww2l2nu = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hww, ww_decay_map["2l2nu"])
hh_ggf_kl_2p45_kt_1_hbb_hww2l2nu = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hww, ww_decay_map["2l2nu"])
hh_ggf_kl_5_kt_1_hbb_hww2l2nu = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hww, ww_decay_map["2l2nu"])

hh_vbf_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_1_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww2l2nu = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww, ww_decay_map["2l2nu"])

hh_ggf_hbb_hwwqqlnu = add_sub_decay_process(hh_ggf_hbb_hww, ww_decay_map["qqlnu"])
hh_ggf_kl_0_kt_1_hbb_hwwqqlnu = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hww, ww_decay_map["qqlnu"])
hh_ggf_kl_1_kt_1_hbb_hwwqqlnu = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hww, ww_decay_map["qqlnu"])
hh_ggf_kl_2p45_kt_1_hbb_hwwqqlnu = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hww, ww_decay_map["qqlnu"])
hh_ggf_kl_5_kt_1_hbb_hwwqqlnu = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hww, ww_decay_map["qqlnu"])

hh_vbf_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_1_kl_1_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww, ww_decay_map["qqlnu"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hwwqqlnu = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww, ww_decay_map["qqlnu"])

hh_ggf_hbb_hww4q = add_sub_decay_process(hh_ggf_hbb_hww, ww_decay_map["4q"])
hh_ggf_kl_0_kt_1_hbb_hww4q = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hww, ww_decay_map["4q"])
hh_ggf_kl_1_kt_1_hbb_hww4q = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hww, ww_decay_map["4q"])
hh_ggf_kl_2p45_kt_1_hbb_hww4q = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hww, ww_decay_map["4q"])
hh_ggf_kl_5_kt_1_hbb_hww4q = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hww, ww_decay_map["4q"])

hh_vbf_hbb_hww4q = add_sub_decay_process(hh_vbf_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_1_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hww, ww_decay_map["4q"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww4q = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hww, ww_decay_map["4q"])

####################################################################################################
#
# HH -> bbZZ
#
####################################################################################################

hh_ggf_hbb_hzz = add_hvv_decay(hh_ggf, hh_ggf_hbb_hvv, hh_decay_map.hbb_hzz, add_production_mode_parent=False)
hh_ggf_kl_0_kt_1_hbb_hzz = add_hvv_decay(hh_ggf_kl_0_kt_1, hh_ggf_kl_0_kt_1_hbb_hvv, hh_decay_map.hbb_hzz)
hh_ggf_kl_1_kt_1_hbb_hzz = add_hvv_decay(hh_ggf_kl_1_kt_1, hh_ggf_kl_1_kt_1_hbb_hvv, hh_decay_map.hbb_hzz)
hh_ggf_kl_2p45_kt_1_hbb_hzz = add_hvv_decay(hh_ggf_kl_2p45_kt_1, hh_ggf_kl_2p45_kt_1_hbb_hvv, hh_decay_map.hbb_hzz)
hh_ggf_kl_5_kt_1_hbb_hzz = add_hvv_decay(hh_ggf_kl_5_kt_1, hh_ggf_kl_5_kt_1_hbb_hvv, hh_decay_map.hbb_hzz)

hh_vbf_hbb_hzz = add_hvv_decay(hh_vbf, hh_vbf_hbb_hvv, hh_decay_map.hbb_hzz, add_production_mode_parent=False)
hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_1, hh_vbf_kv_1_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_0, hh_vbf_kv_1_k2v_1_kl_0_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz = add_hvv_decay(hh_vbf_kv_1_k2v_1_kl_2, hh_vbf_kv_1_k2v_1_kl_2_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz = add_hvv_decay(hh_vbf_kv_1_k2v_0_kl_1, hh_vbf_kv_1_k2v_0_kl_1_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz = add_hvv_decay(hh_vbf_kv_1_k2v_2_kl_1, hh_vbf_kv_1_k2v_2_kl_1_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz = add_hvv_decay(hh_vbf_kv_0p5_k2v_1_kl_1, hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz = add_hvv_decay(hh_vbf_kv_1p5_k2v_1_kl_1, hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hvv, hh_decay_map.hbb_hzz)  # noqa

hh_ggf_hbb_hzz2l2nu = add_sub_decay_process(hh_ggf_hbb_hzz, zz_decay_map["2l2nu"])
hh_ggf_kl_0_kt_1_hbb_hzz2l2nu = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_ggf_kl_1_kt_1_hbb_hzz2l2nu = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_ggf_kl_2p45_kt_1_hbb_hzz2l2nu = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_ggf_kl_5_kt_1_hbb_hzz2l2nu = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hzz, zz_decay_map["2l2nu"])

hh_vbf_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz2l2nu = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz, zz_decay_map["2l2nu"])

hh_ggf_hbb_hzz4q = add_sub_decay_process(hh_ggf_hbb_hzz, zz_decay_map["4q"])
hh_ggf_kl_0_kt_1_hbb_hzz4q = add_sub_decay_process(hh_ggf_kl_0_kt_1_hbb_hzz, zz_decay_map["4q"])
hh_ggf_kl_1_kt_1_hbb_hzz4q = add_sub_decay_process(hh_ggf_kl_1_kt_1_hbb_hzz, zz_decay_map["4q"])
hh_ggf_kl_2p45_kt_1_hbb_hzz4q = add_sub_decay_process(hh_ggf_kl_2p45_kt_1_hbb_hzz, zz_decay_map["4q"])
hh_ggf_kl_5_kt_1_hbb_hzz4q = add_sub_decay_process(hh_ggf_kl_5_kt_1_hbb_hzz, zz_decay_map["4q"])

hh_vbf_hbb_hzz4q = add_sub_decay_process(hh_vbf_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_1_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_0_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1_k2v_1_kl_2_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1_k2v_0_kl_1_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1_k2v_2_kl_1_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_0p5_k2v_1_kl_1_hbb_hzz, zz_decay_map["4q"])
hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz4q = add_sub_decay_process(hh_vbf_kv_1p5_k2v_1_kl_1_hbb_hzz, zz_decay_map["4q"])

####################################################################################################
#
# HH resonant
#
####################################################################################################


#
# ggF -> radion -> HH
#

radion_hh_ggf_bbww = radion_hh_ggf.add_process(
    name="radion_hh_ggf_bbww",
    id=23200,
    label=rf"{radion_hh_ggf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m250",
    id=23201,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m260 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m260",
    id=23202,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m270 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m270",
    id=23203,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m280 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m280",
    id=23204,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m300 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m300",
    id=23205,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m320 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m320",
    id=23206,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m350 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m350",
    id=23207,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m400 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m400",
    id=23208,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m450 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m450",
    id=23209,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m500",
    id=23210,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m550 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m550",
    id=23211,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m600 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m600",
    id=23212,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m650 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m650",
    id=23213,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m700 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m700",
    id=23214,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m750",
    id=23215,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m800 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m800",
    id=23216,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m850 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m850",
    id=23217,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m900 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m900",
    id=23218,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1000",
    id=23219,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1250",
    id=23220,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1500",
    id=23221,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m1750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1750",
    id=23222,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m2000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2000",
    id=23223,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m2500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2500",
    id=23224,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_bbww_m3000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m3000",
    id=23225,
    xsecs={13: Number(0.1)},  # TODO
)


#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf_bbww = graviton_hh_ggf.add_process(
    name="graviton_hh_ggf_bbww",
    id=24200,
    label=rf"{graviton_hh_ggf.label} $\rightarrow bbWW$",
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m250",
    id=24201,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m260 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m260",
    id=24202,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m270 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m270",
    id=24203,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m280 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m280",
    id=24204,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m300 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m300",
    id=24205,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m320 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m320",
    id=24206,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m350 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m350",
    id=24207,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m400 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m400",
    id=24208,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m450 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m450",
    id=24209,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m500",
    id=24210,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m550 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m550",
    id=24211,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m600 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m600",
    id=24212,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m650 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m650",
    id=24213,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m700 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m700",
    id=24214,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m750",
    id=24215,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m800 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m800",
    id=24216,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m850 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m850",
    id=24217,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m900 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m900",
    id=24218,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1000",
    id=24219,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1250",
    id=24220,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1500",
    id=24221,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m1750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1750",
    id=24222,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m2000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2000",
    id=24223,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m2500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2500",
    id=24224,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_bbww_m3000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m3000",
    id=24225,
    xsecs={13: Number(0.1)},  # TODO
)
