# coding: utf-8

"""
HH -> bbVV process definitions.

IDs are assigned in the range 21200-21799 for hh_ggf and 22200-22799 for hh_vbf.
bbVV processes are assigned IDs in the range 21200-21399 and 22200-22399.
bbWW processes are assigned IDs in the range 21400-21599 and 22400-22599.
bbZZ processes are assigned IDs in the range 21600-21799 and 22600-22799.
For bbVV, the VV decay mode IDs correspond to:
- xxx20: qqlnu
- xxx40: 2l2nu
- xxx60: 4q
- xxx80: 2q2nu
- xx(x+1)00: 4nu
- xx(x+1)20: 4l
- xx(x+1)40: 2l2q

The code structure is designed to allow maintainance via a single source of truth for the decay maps,
using a handful of helper functions to add the processes to the main HH -> bbVV processes.

We first define the main HH -> bbVV processes with the *add_bbvv_decay_process* function,
then we define the HH -> bbWW and HH -> bbZZ processes with the *add_hvv_decay* function.
Afterwards, we assign the correct cross sections to the HH -> bbVV processes by adding the xsecs of the
HH -> bbWW and HH -> bbZZ processes to the HH -> bbVV processes.
Then we define all the VV sub-decay processes for the bbVV, bbWW, and bbZZ processes using the
*add_bbvv_sub_decay* function and assign the correct cross sections to the bbVV sub-processes aswell.
Lastly, we define the resonant (radion and graviton) HH -> bbWW processes.
"""

ggf_params = ["", "_kl0_kt1", "_kl1_kt1", "_kl2p45_kt1", "_kl5_kt1"]
vbf_params = [
    "", "_kv1_k2v1_kl1", "_kv1_k2v1_kl0", "_kv1_k2v1_kl2", "_kv1_k2v0_kl1",
    "_kv1_k2v2_kl1", "_kv0p5_k2v1_kl1", "_kv1p5_k2v1_kl1",
    "_kv1p74_k2v1p37_kl14p4", "_kvm0p012_k2v0p03_kl10p2", "_kvm0p758_k2v1p44_klm19p3",
    "_kvm0p962_k2v0p959_klm1p43", "_kvm1p21_k2v1p94_klm0p94", "_kvm1p6_k2v2p72_klm1p36",
    "_kvm1p83_k2v3p57_klm3p39", "_kv2p12_k2v3p87_klm5p96",
]
vv_decay_modes = ["", "qqlnu", "2l2nu", "4q", "2q2nu", "4nu", "4l", "2l2q"]
ww_decay_modes = ["", "qqlnu", "2l2nu", "4q"]
zz_decay_modes = ["", "2l2nu", "4q", "2q2nu", "4nu", "4l", "2l2q"]

__all__ = [
    f"hh_ggf_hbb_hvv{vv}{params}"
    for params in ggf_params
    for vv in vv_decay_modes
] + [
    f"hh_vbf_hbb_hvv{vv}{params}"
    for params in vbf_params
    for vv in vv_decay_modes
] + [
    f"hh_ggf_hbb_hww{ww}{params}"
    for params in ggf_params
    for ww in ww_decay_modes
] + [
    f"hh_vbf_hbb_hww{ww}{params}"
    for params in vbf_params
    for ww in ww_decay_modes
] + [
    f"hh_ggf_hbb_hzz{zz}{params}"
    for params in ggf_params
    for zz in zz_decay_modes
] + [
    f"hh_vbf_hbb_hzz{zz}{params}"
    for params in vbf_params
    for zz in zz_decay_modes
] + [
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

from functools import partial

import cmsdb.constants as const
from cmsdb.util import DotDict, add_decay_process, add_xsecs
from cmsdb.processes.hh import (
    hh_ggf, hh_ggf_kl0_kt1, hh_ggf_kl1_kt1, hh_ggf_kl2p45_kt1, hh_ggf_kl5_kt1,
    hh_vbf, hh_vbf_kv1_k2v1_kl1, hh_vbf_kv1_k2v1_kl0, hh_vbf_kv1_k2v1_kl2,
    hh_vbf_kv1_k2v0_kl1, hh_vbf_kv1_k2v2_kl1, hh_vbf_kv0p5_k2v1_kl1, hh_vbf_kv1p5_k2v1_kl1,
    hh_vbf_kv1p74_k2v1p37_kl14p4, hh_vbf_kvm0p012_k2v0p03_kl10p2, hh_vbf_kvm0p758_k2v1p44_klm19p3,
    hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_vbf_kvm1p21_k2v1p94_klm0p94, hh_vbf_kvm1p6_k2v2p72_klm1p36,
    hh_vbf_kvm1p83_k2v3p57_klm3p39, hh_vbf_kv2p12_k2v3p87_klm5p96,
    radion_hh_ggf, graviton_hh_ggf,
)

#
# Helper
#

# NOTE: The IDs of the hh_ggf_hbb_hvv processes are set to 200 + ID of the VV decay mode
# NOTE: The BR of the hbb_hvv process is set to 1. The hbb_hvv process xsecs are later set the
# sum of the xsecs of the hbb_hww and hbb_hzz processes
hh_decay_map = DotDict.wrap({
    "hbb_hvv": {
        "name": "hbb_hvv",
        "id": 200,
        "br": 1,
        "label": r"$\rightarrow bbVV$",
    },
    "hbb_hww": {
        "name": "hbb_hww",
        "id": 200,  # corresponds to 200 + 200 = 400
        "br": const.br_hh.bbww,
        "label": r"$\rightarrow bbWW$",
    },
    "hbb_hzz": {
        "name": "hbb_hzz",
        "id": 400,  # corresponds to 200 + 400 = 600
        "br": const.br_hh.bbzz,
        "label": r"$\rightarrow bbZZ$",
    },
})

# NOTE: IDs between VV, WW, and ZZ are not always consistent
# NOTE: BRs are first set to -1 and then set to the correct value in the decay maps below
# The hbb_hvv sub-process xsecs are later set to the sum of the xsecs of the hbb_hww and hbb_hzz sub-processes
vv_decay_map = DotDict.wrap({
    "qqlnu": {
        "name": "qqlnu",
        "id": 20,
        "label": r"$(qq\ell\nu)$",
        "br": -1,
    },
    "2l2nu": {
        "name": "2l2nu",
        "id": 40,
        "label": r"$(2\ell 2\nu)$",
        "br": -1,
    },
    "4q": {
        "name": "4q",
        "id": 60,
        "label": r"$(4q)$",
        "br": -1,
    },
    "2q2nu": {
        "name": "2q2nu",
        "id": 80,
        "label": r"$(2q2\nu)$",
        "br": -1,
    },
    "4nu": {
        "name": "4nu",
        "id": 100,
        "label": r"$(4\nu)$",
        "br": -1,
    },
    "4l": {
        "name": "4l",
        "id": 120,
        "label": r"$(4\ell)$",
        "br": -1,
    },
    "2l2q": {
        "name": "2l2q",
        "id": 140,
        "label": r"$(2\ell 2q)$",
        "br": -1,
    },
})

zz_decay_map = DotDict.wrap({
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("4l", "2l2nu", "2l2q", "2q2nu", "4nu", "4q")
})
zz_decay_map["4l"]["br"] = const.br_zz.llll
zz_decay_map["2l2nu"]["br"] = const.br_zz.llnunu
zz_decay_map["2l2q"]["br"] = const.br_zz.llqq
zz_decay_map["2q2nu"]["br"] = const.br_zz.qqnunu
zz_decay_map["4nu"]["br"] = const.br_zz.nunununu
zz_decay_map["4q"]["br"] = const.br_zz.qqqq


ww_decay_map = DotDict.wrap({
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("2l2nu", "4q", "qqlnu")
})
ww_decay_map["2l2nu"]["br"] = const.br_ww.dl
ww_decay_map["4q"]["br"] = const.br_ww.fh
ww_decay_map["qqlnu"]["br"] = const.br_ww.sl

"""
This function is used to add the main hbb_hvv processes to the hh_ggf and hh_vbf processes and
is needed to follow our naming conventions, inserting the hh decay in front of the k-parameters,
e.g. hh_ggf_hbb_hvv_kl1_kt1
"""
add_bbvv_decay_process = partial(
    add_decay_process,
    name_func=lambda parent_name, decay_name: (
        parent_name.replace("_k", f"_{decay_name}_k", 1)
        if "_k" in parent_name else f"{parent_name}_{decay_name}"
    ),
    label_func=lambda parent_label, decay_label: f"{parent_label}{decay_label}",
)

"""
This function is used to add the VV sub-decay processes to the hbb_hvv processes and is needed
to insert the VV decay mode in the middle of the hh decay and the k-parameters,
e.g. hh_ggf_hbb_hvv2l2nu_kl1_kt1
"""
add_bbvv_sub_decay = partial(
    add_decay_process,
    name_func=lambda parent_name, decay_name: (
        parent_name.replace("_k", f"{decay_name}_k", 1)
        if "_k" in parent_name else f"{parent_name}{decay_name}"
    ),
    label_func=lambda parent_label, decay_label: f"{parent_label}{decay_label}",
)


def add_hvv_decay(parent, decay_map, add_production_mode_parent=True):
    """
    This function is used to add the hbb_hww and hbb_hzz to the hbb_hvv processes and is needed to replace
    the VV decay mode with the WW or ZZ decay mode, e.g. hh_ggf_hbb_hww_kl1_kt1.
    The *aux* argument is used to perform some magic such that each process gets assigned the correct sub-process.
    """
    child = add_decay_process(
        parent=parent,
        decay_map=decay_map,
        add_production_mode_parent=add_production_mode_parent,
        name_func=lambda parent_name, decay_name: parent_name.replace(hh_decay_map.hbb_hvv.name, decay_name),
        label_func=lambda parent_label, decay_label: parent_label.replace(hh_decay_map.hbb_hvv.label, decay_label),
        aux={"production_mode_parent": [parent.name]},
    )
    return child


#############################################################
#
# HH -> bbVV (incl)
#
#############################################################

# NOTE: we could also add hh_hbb_hvv processes (to merge ggf and vbf)

hh_ggf_hbb_hvv = add_bbvv_decay_process(hh_ggf, hh_decay_map.hbb_hvv, add_production_mode_parent=False)
hh_ggf_hbb_hvv_kl0_kt1 = add_bbvv_decay_process(hh_ggf_kl0_kt1, hh_decay_map.hbb_hvv)
hh_ggf_hbb_hvv_kl1_kt1 = add_bbvv_decay_process(hh_ggf_kl1_kt1, hh_decay_map.hbb_hvv)
hh_ggf_hbb_hvv_kl2p45_kt1 = add_bbvv_decay_process(hh_ggf_kl2p45_kt1, hh_decay_map.hbb_hvv)
hh_ggf_hbb_hvv_kl5_kt1 = add_bbvv_decay_process(hh_ggf_kl5_kt1, hh_decay_map.hbb_hvv)

hh_vbf_hbb_hvv = add_bbvv_decay_process(hh_vbf, hh_decay_map.hbb_hvv, add_production_mode_parent=False)
hh_vbf_hbb_hvv_kv1_k2v1_kl1 = add_bbvv_decay_process(hh_vbf_kv1_k2v1_kl1, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1_k2v1_kl0 = add_bbvv_decay_process(hh_vbf_kv1_k2v1_kl0, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1_k2v1_kl2 = add_bbvv_decay_process(hh_vbf_kv1_k2v1_kl2, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1_k2v0_kl1 = add_bbvv_decay_process(hh_vbf_kv1_k2v0_kl1, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1_k2v2_kl1 = add_bbvv_decay_process(hh_vbf_kv1_k2v2_kl1, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv0p5_k2v1_kl1 = add_bbvv_decay_process(hh_vbf_kv0p5_k2v1_kl1, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1p5_k2v1_kl1 = add_bbvv_decay_process(hh_vbf_kv1p5_k2v1_kl1, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4 = add_bbvv_decay_process(hh_vbf_kv1p74_k2v1p37_kl14p4, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2 = add_bbvv_decay_process(hh_vbf_kvm0p012_k2v0p03_kl10p2, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3 = add_bbvv_decay_process(hh_vbf_kvm0p758_k2v1p44_klm19p3, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43 = add_bbvv_decay_process(hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_decay_map.hbb_hvv)  # noqa
hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94 = add_bbvv_decay_process(hh_vbf_kvm1p21_k2v1p94_klm0p94, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36 = add_bbvv_decay_process(hh_vbf_kvm1p6_k2v2p72_klm1p36, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39 = add_bbvv_decay_process(hh_vbf_kvm1p83_k2v3p57_klm3p39, hh_decay_map.hbb_hvv)
hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96 = add_bbvv_decay_process(hh_vbf_kv2p12_k2v3p87_klm5p96, hh_decay_map.hbb_hvv)

####################################################################################################
#
# HH -> bbWW (incl)
#
####################################################################################################

hh_ggf_hbb_hww = add_hvv_decay(hh_ggf_hbb_hvv, hh_decay_map.hbb_hww, add_production_mode_parent=False)
hh_ggf_hbb_hww_kl0_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl0_kt1, hh_decay_map.hbb_hww)
hh_ggf_hbb_hww_kl1_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl1_kt1, hh_decay_map.hbb_hww)
hh_ggf_hbb_hww_kl2p45_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl2p45_kt1, hh_decay_map.hbb_hww)
hh_ggf_hbb_hww_kl5_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl5_kt1, hh_decay_map.hbb_hww)

hh_vbf_hbb_hww = add_hvv_decay(hh_vbf_hbb_hvv, hh_decay_map.hbb_hww, add_production_mode_parent=False)
hh_vbf_hbb_hww_kv1_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1_k2v1_kl0 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1_k2v1_kl2 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1_k2v0_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1_k2v2_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv0p5_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1p5_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv1p74_k2v1p37_kl14p4 = add_hvv_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm0p012_k2v0p03_kl10p2 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm0p758_k2v1p44_klm19p3 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm0p962_k2v0p959_klm1p43 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm1p21_k2v1p94_klm0p94 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm1p6_k2v2p72_klm1p36 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kvm1p83_k2v3p57_klm3p39 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, hh_decay_map.hbb_hww)
hh_vbf_hbb_hww_kv2p12_k2v3p87_klm5p96 = add_hvv_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, hh_decay_map.hbb_hww)

####################################################################################################
#
# HH -> bbZZ (incl)
#
####################################################################################################

hh_ggf_hbb_hzz = add_hvv_decay(hh_ggf_hbb_hvv, hh_decay_map.hbb_hzz, add_production_mode_parent=False)
hh_ggf_hbb_hzz_kl0_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl0_kt1, hh_decay_map.hbb_hzz)
hh_ggf_hbb_hzz_kl1_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl1_kt1, hh_decay_map.hbb_hzz)
hh_ggf_hbb_hzz_kl2p45_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl2p45_kt1, hh_decay_map.hbb_hzz)
hh_ggf_hbb_hzz_kl5_kt1 = add_hvv_decay(hh_ggf_hbb_hvv_kl5_kt1, hh_decay_map.hbb_hzz)

hh_vbf_hbb_hzz = add_hvv_decay(hh_vbf_hbb_hvv, hh_decay_map.hbb_hzz, add_production_mode_parent=False)
hh_vbf_hbb_hzz_kv1_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1_k2v1_kl0 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1_k2v1_kl2 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1_k2v0_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1_k2v2_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv0p5_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1p5_k2v1_kl1 = add_hvv_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4 = add_hvv_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43 = add_hvv_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39 = add_hvv_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, hh_decay_map.hbb_hzz)
hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96 = add_hvv_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, hh_decay_map.hbb_hzz)

#
# assign cross sections to HH -> bbVV processes
#

for proc_name in [
    f"hh_ggf_hbb_hvv{params}"
    for params in ggf_params
] + [
    f"hh_vbf_hbb_hvv{params}"
    for params in vbf_params
]:
    proc = locals()[proc_name]
    proc.xsecs = add_xsecs(
        proc.get_process(proc.name.replace("hvv", "hww")),
        proc.get_process(proc.name.replace("hvv", "hzz")),
    )

####################################################################################################
#
# HH -> bbVV (decays)
#
####################################################################################################

hh_ggf_hbb_hvvqqlnu = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["qqlnu"], add_production_mode_parent=False)
hh_ggf_hbb_hvvqqlnu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["qqlnu"])
hh_ggf_hbb_hvvqqlnu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["qqlnu"])
hh_ggf_hbb_hvvqqlnu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["qqlnu"])
hh_ggf_hbb_hvvqqlnu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["qqlnu"])

hh_vbf_hbb_hvvqqlnu = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["qqlnu"], add_production_mode_parent=False)
hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["qqlnu"])
hh_vbf_hbb_hvvqqlnu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hvvqqlnu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["qqlnu"])  # noqa

hh_ggf_hbb_hvv2l2nu = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["2l2nu"], add_production_mode_parent=False)
hh_ggf_hbb_hvv2l2nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["2l2nu"])
hh_ggf_hbb_hvv2l2nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["2l2nu"])
hh_ggf_hbb_hvv2l2nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["2l2nu"])
hh_ggf_hbb_hvv2l2nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["2l2nu"])

hh_vbf_hbb_hvv2l2nu = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["2l2nu"], add_production_mode_parent=False)
hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["2l2nu"])
hh_vbf_hbb_hvv2l2nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hvv2l2nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["2l2nu"])  # noqa


hh_ggf_hbb_hvv4q = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["4q"], add_production_mode_parent=False)
hh_ggf_hbb_hvv4q_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["4q"])
hh_ggf_hbb_hvv4q_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["4q"])
hh_ggf_hbb_hvv4q_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["4q"])
hh_ggf_hbb_hvv4q_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["4q"])

hh_vbf_hbb_hvv4q = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["4q"], add_production_mode_parent=False)
hh_vbf_hbb_hvv4q_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["4q"])
hh_vbf_hbb_hvv4q_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["4q"])  # noqa
hh_vbf_hbb_hvv4q_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["4q"])  # noqa

hh_ggf_hbb_hvv2q2nu = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["2q2nu"], add_production_mode_parent=False)
hh_ggf_hbb_hvv2q2nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["2q2nu"])
hh_ggf_hbb_hvv2q2nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["2q2nu"])
hh_ggf_hbb_hvv2q2nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["2q2nu"])
hh_ggf_hbb_hvv2q2nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["2q2nu"])

hh_vbf_hbb_hvv2q2nu = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["2q2nu"], add_production_mode_parent=False)
hh_vbf_hbb_hvv2q2nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["2q2nu"])
hh_vbf_hbb_hvv2q2nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hvv2q2nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["2q2nu"])  # noqa

hh_ggf_hbb_hvv4nu = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["4nu"], add_production_mode_parent=False)
hh_ggf_hbb_hvv4nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["4nu"])
hh_ggf_hbb_hvv4nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["4nu"])
hh_ggf_hbb_hvv4nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["4nu"])
hh_ggf_hbb_hvv4nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["4nu"])

hh_vbf_hbb_hvv4nu = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["4nu"], add_production_mode_parent=False)
hh_vbf_hbb_hvv4nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["4nu"])
hh_vbf_hbb_hvv4nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["4nu"])  # noqa
hh_vbf_hbb_hvv4nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["4nu"])  # noqa

hh_ggf_hbb_hvv4l = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["4l"], add_production_mode_parent=False)
hh_ggf_hbb_hvv4l_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["4l"])
hh_ggf_hbb_hvv4l_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["4l"])
hh_ggf_hbb_hvv4l_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["4l"])
hh_ggf_hbb_hvv4l_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["4l"])

hh_vbf_hbb_hvv4l = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["4l"], add_production_mode_parent=False)
hh_vbf_hbb_hvv4l_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["4l"])
hh_vbf_hbb_hvv4l_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["4l"])  # noqa
hh_vbf_hbb_hvv4l_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["4l"])  # noqa

hh_ggf_hbb_hvv2l2q = add_bbvv_sub_decay(hh_ggf_hbb_hvv, vv_decay_map["2l2q"], add_production_mode_parent=False)
hh_ggf_hbb_hvv2l2q_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl0_kt1, vv_decay_map["2l2q"])
hh_ggf_hbb_hvv2l2q_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl1_kt1, vv_decay_map["2l2q"])
hh_ggf_hbb_hvv2l2q_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl2p45_kt1, vv_decay_map["2l2q"])
hh_ggf_hbb_hvv2l2q_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hvv_kl5_kt1, vv_decay_map["2l2q"])

hh_vbf_hbb_hvv2l2q = add_bbvv_sub_decay(hh_vbf_hbb_hvv, vv_decay_map["2l2q"], add_production_mode_parent=False)
hh_vbf_hbb_hvv2l2q_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl1, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl0, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v1_kl2, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v0_kl1, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1_k2v2_kl1, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv0p5_k2v1_kl1, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p5_k2v1_kl1, vv_decay_map["2l2q"])
hh_vbf_hbb_hvv2l2q_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv1p74_k2v1p37_kl14p4, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p012_k2v0p03_kl10p2, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p758_k2v1p44_klm19p3, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm0p962_k2v0p959_klm1p43, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p21_k2v1p94_klm0p94, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p6_k2v2p72_klm1p36, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kvm1p83_k2v3p57_klm3p39, vv_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hvv2l2q_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hvv_kv2p12_k2v3p87_klm5p96, vv_decay_map["2l2q"])  # noqa

####################################################################################################
#
# HH -> bbWW (decays)
#
####################################################################################################

hh_ggf_hbb_hww2l2nu = add_bbvv_sub_decay(hh_ggf_hbb_hww, ww_decay_map["2l2nu"])
hh_ggf_hbb_hww2l2nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl0_kt1, ww_decay_map["2l2nu"])
hh_ggf_hbb_hww2l2nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl1_kt1, ww_decay_map["2l2nu"])
hh_ggf_hbb_hww2l2nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl2p45_kt1, ww_decay_map["2l2nu"])
hh_ggf_hbb_hww2l2nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl5_kt1, ww_decay_map["2l2nu"])

hh_vbf_hbb_hww2l2nu = add_bbvv_sub_decay(hh_vbf_hbb_hww, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl1, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl0, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl2, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v0_kl1, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v2_kl1, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv0p5_k2v1_kl1, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p5_k2v1_kl1, ww_decay_map["2l2nu"])
hh_vbf_hbb_hww2l2nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p74_k2v1p37_kl14p4, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p012_k2v0p03_kl10p2, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p758_k2v1p44_klm19p3, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p962_k2v0p959_klm1p43, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p21_k2v1p94_klm0p94, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p6_k2v2p72_klm1p36, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p83_k2v3p57_klm3p39, ww_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hww2l2nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv2p12_k2v3p87_klm5p96, ww_decay_map["2l2nu"])  # noqa

hh_ggf_hbb_hwwqqlnu = add_bbvv_sub_decay(hh_ggf_hbb_hww, ww_decay_map["qqlnu"])
hh_ggf_hbb_hwwqqlnu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl0_kt1, ww_decay_map["qqlnu"])
hh_ggf_hbb_hwwqqlnu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl1_kt1, ww_decay_map["qqlnu"])
hh_ggf_hbb_hwwqqlnu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl2p45_kt1, ww_decay_map["qqlnu"])
hh_ggf_hbb_hwwqqlnu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl5_kt1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu = add_bbvv_sub_decay(hh_vbf_hbb_hww, ww_decay_map["qqlnu"])

hh_vbf_hbb_hwwqqlnu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl0, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl2, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v0_kl1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v2_kl1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv0p5_k2v1_kl1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p5_k2v1_kl1, ww_decay_map["qqlnu"])
hh_vbf_hbb_hwwqqlnu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p74_k2v1p37_kl14p4, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p012_k2v0p03_kl10p2, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p758_k2v1p44_klm19p3, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p962_k2v0p959_klm1p43, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p21_k2v1p94_klm0p94, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p6_k2v2p72_klm1p36, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p83_k2v3p57_klm3p39, ww_decay_map["qqlnu"])  # noqa
hh_vbf_hbb_hwwqqlnu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv2p12_k2v3p87_klm5p96, ww_decay_map["qqlnu"])  # noqa

hh_ggf_hbb_hww4q = add_bbvv_sub_decay(hh_ggf_hbb_hww, ww_decay_map["4q"])
hh_ggf_hbb_hww4q_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl0_kt1, ww_decay_map["4q"])
hh_ggf_hbb_hww4q_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl1_kt1, ww_decay_map["4q"])
hh_ggf_hbb_hww4q_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl2p45_kt1, ww_decay_map["4q"])
hh_ggf_hbb_hww4q_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hww_kl5_kt1, ww_decay_map["4q"])

hh_vbf_hbb_hww4q = add_bbvv_sub_decay(hh_vbf_hbb_hww, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl1, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl0, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v1_kl2, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v0_kl1, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1_k2v2_kl1, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv0p5_k2v1_kl1, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p5_k2v1_kl1, ww_decay_map["4q"])
hh_vbf_hbb_hww4q_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv1p74_k2v1p37_kl14p4, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p012_k2v0p03_kl10p2, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p758_k2v1p44_klm19p3, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm0p962_k2v0p959_klm1p43, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p21_k2v1p94_klm0p94, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p6_k2v2p72_klm1p36, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kvm1p83_k2v3p57_klm3p39, ww_decay_map["4q"])  # noqa
hh_vbf_hbb_hww4q_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hww_kv2p12_k2v3p87_klm5p96, ww_decay_map["4q"])  # noqa

####################################################################################################
#
# HH -> bbZZ (decays)
#
####################################################################################################

hh_ggf_hbb_hzz2l2nu = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["2l2nu"])
hh_ggf_hbb_hzz2l2nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["2l2nu"])
hh_ggf_hbb_hzz2l2nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["2l2nu"])
hh_ggf_hbb_hzz2l2nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["2l2nu"])
hh_ggf_hbb_hzz2l2nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["2l2nu"])

hh_vbf_hbb_hzz2l2nu = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["2l2nu"])
hh_vbf_hbb_hzz2l2nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["2l2nu"])  # noqa
hh_vbf_hbb_hzz2l2nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["2l2nu"])  # noqa

hh_ggf_hbb_hzz4q = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["4q"])
hh_ggf_hbb_hzz4q_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["4q"])
hh_ggf_hbb_hzz4q_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["4q"])
hh_ggf_hbb_hzz4q_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["4q"])
hh_ggf_hbb_hzz4q_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["4q"])

hh_vbf_hbb_hzz4q = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["4q"])
hh_vbf_hbb_hzz4q_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["4q"])  # noqa
hh_vbf_hbb_hzz4q_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["4q"])  # noqa

hh_ggf_hbb_hzz2q2nu = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["2q2nu"])
hh_ggf_hbb_hzz2q2nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["2q2nu"])
hh_ggf_hbb_hzz2q2nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["2q2nu"])
hh_ggf_hbb_hzz2q2nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["2q2nu"])
hh_ggf_hbb_hzz2q2nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["2q2nu"])

hh_vbf_hbb_hzz2q2nu = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["2q2nu"])
hh_vbf_hbb_hzz2q2nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["2q2nu"])  # noqa
hh_vbf_hbb_hzz2q2nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["2q2nu"])  # noqa

hh_ggf_hbb_hzz4nu = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["4nu"])
hh_ggf_hbb_hzz4nu_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["4nu"])
hh_ggf_hbb_hzz4nu_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["4nu"])
hh_ggf_hbb_hzz4nu_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["4nu"])
hh_ggf_hbb_hzz4nu_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["4nu"])

hh_vbf_hbb_hzz4nu = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["4nu"])
hh_vbf_hbb_hzz4nu_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["4nu"])  # noqa
hh_vbf_hbb_hzz4nu_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["4nu"])  # noqa

hh_ggf_hbb_hzz4l = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["4l"])
hh_ggf_hbb_hzz4l_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["4l"])
hh_ggf_hbb_hzz4l_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["4l"])
hh_ggf_hbb_hzz4l_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["4l"])
hh_ggf_hbb_hzz4l_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["4l"])

hh_vbf_hbb_hzz4l = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["4l"])
hh_vbf_hbb_hzz4l_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["4l"])  # noqa
hh_vbf_hbb_hzz4l_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["4l"])  # noqa

hh_ggf_hbb_hzz2l2q = add_bbvv_sub_decay(hh_ggf_hbb_hzz, zz_decay_map["2l2q"])
hh_ggf_hbb_hzz2l2q_kl0_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl0_kt1, zz_decay_map["2l2q"])
hh_ggf_hbb_hzz2l2q_kl1_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl1_kt1, zz_decay_map["2l2q"])
hh_ggf_hbb_hzz2l2q_kl2p45_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl2p45_kt1, zz_decay_map["2l2q"])
hh_ggf_hbb_hzz2l2q_kl5_kt1 = add_bbvv_sub_decay(hh_ggf_hbb_hzz_kl5_kt1, zz_decay_map["2l2q"])

hh_vbf_hbb_hzz2l2q = add_bbvv_sub_decay(hh_vbf_hbb_hzz, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl1, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1_k2v1_kl0 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl0, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1_k2v1_kl2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v1_kl2, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1_k2v0_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v0_kl1, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1_k2v2_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1_k2v2_kl1, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv0p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv0p5_k2v1_kl1, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1p5_k2v1_kl1 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p5_k2v1_kl1, zz_decay_map["2l2q"])
hh_vbf_hbb_hzz2l2q_kv1p74_k2v1p37_kl14p4 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv1p74_k2v1p37_kl14p4, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm0p012_k2v0p03_kl10p2 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p012_k2v0p03_kl10p2, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm0p758_k2v1p44_klm19p3 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p758_k2v1p44_klm19p3, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm0p962_k2v0p959_klm1p43 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm0p962_k2v0p959_klm1p43, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm1p21_k2v1p94_klm0p94 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p21_k2v1p94_klm0p94, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm1p6_k2v2p72_klm1p36 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p6_k2v2p72_klm1p36, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kvm1p83_k2v3p57_klm3p39 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kvm1p83_k2v3p57_klm3p39, zz_decay_map["2l2q"])  # noqa
hh_vbf_hbb_hzz2l2q_kv2p12_k2v3p87_klm5p96 = add_bbvv_sub_decay(hh_vbf_hbb_hzz_kv2p12_k2v3p87_klm5p96, zz_decay_map["2l2q"])  # noqa

#
# Assign cross sections to hbb_hvv sub-processes by adding the hbb_hww and hbb_hzz sub-process cross sections
#

for proc_name in [
    f"hh_ggf_hbb_hvv{vv}{params}"
    for params in ggf_params
    for vv in ["qqlnu", "2l2nu", "4q", "2q2nu", "4nu", "4l", "2l2q"]
] + [
    f"hh_vbf_hbb_hvv{vv}{params}"
    for params in vbf_params
    for vv in ["qqlnu", "2l2nu", "4q", "2q2nu", "4nu", "4l", "2l2q"]
]:
    proc = locals()[proc_name]
    sub_procs = [
        sub_proc for sub_proc in proc.processes
        if sub_proc.name in (proc_name.replace("hvv", "hww"), proc_name.replace("hvv", "hzz"))
    ]
    proc.xsecs = add_xsecs(*sub_procs)

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
)

radion_hh_ggf_bbww_m250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m250",
    id=23201,
)

radion_hh_ggf_bbww_m260 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m260",
    id=23202,
)

radion_hh_ggf_bbww_m270 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m270",
    id=23203,
)

radion_hh_ggf_bbww_m280 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m280",
    id=23204,
)

radion_hh_ggf_bbww_m300 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m300",
    id=23205,
)

radion_hh_ggf_bbww_m320 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m320",
    id=23206,
)

radion_hh_ggf_bbww_m350 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m350",
    id=23207,
)

radion_hh_ggf_bbww_m400 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m400",
    id=23208,
)

radion_hh_ggf_bbww_m450 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m450",
    id=23209,
)

radion_hh_ggf_bbww_m500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m500",
    id=23210,
)

radion_hh_ggf_bbww_m550 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m550",
    id=23211,
)

radion_hh_ggf_bbww_m600 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m600",
    id=23212,
)

radion_hh_ggf_bbww_m650 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m650",
    id=23213,
)

radion_hh_ggf_bbww_m700 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m700",
    id=23214,
)

radion_hh_ggf_bbww_m750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m750",
    id=23215,
)

radion_hh_ggf_bbww_m800 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m800",
    id=23216,
)

radion_hh_ggf_bbww_m850 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m850",
    id=23217,
)

radion_hh_ggf_bbww_m900 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m900",
    id=23218,
)

radion_hh_ggf_bbww_m1000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1000",
    id=23219,
)

radion_hh_ggf_bbww_m1250 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1250",
    id=23220,
)

radion_hh_ggf_bbww_m1500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1500",
    id=23221,
)

radion_hh_ggf_bbww_m1750 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m1750",
    id=23222,
)

radion_hh_ggf_bbww_m2000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2000",
    id=23223,
)

radion_hh_ggf_bbww_m2500 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m2500",
    id=23224,
)

radion_hh_ggf_bbww_m3000 = radion_hh_ggf_bbww.add_process(
    name="radion_hh_ggf_bbww_m3000",
    id=23225,
)


#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf_bbww = graviton_hh_ggf.add_process(
    name="graviton_hh_ggf_bbww",
    id=24200,
    label=rf"{graviton_hh_ggf.label} $\rightarrow bbWW$",
)

graviton_hh_ggf_bbww_m250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m250",
    id=24201,
)

graviton_hh_ggf_bbww_m260 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m260",
    id=24202,
)

graviton_hh_ggf_bbww_m270 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m270",
    id=24203,
)

graviton_hh_ggf_bbww_m280 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m280",
    id=24204,
)

graviton_hh_ggf_bbww_m300 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m300",
    id=24205,
)

graviton_hh_ggf_bbww_m320 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m320",
    id=24206,
)

graviton_hh_ggf_bbww_m350 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m350",
    id=24207,
)

graviton_hh_ggf_bbww_m400 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m400",
    id=24208,
)

graviton_hh_ggf_bbww_m450 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m450",
    id=24209,
)

graviton_hh_ggf_bbww_m500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m500",
    id=24210,
)

graviton_hh_ggf_bbww_m550 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m550",
    id=24211,
)

graviton_hh_ggf_bbww_m600 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m600",
    id=24212,
)

graviton_hh_ggf_bbww_m650 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m650",
    id=24213,
)

graviton_hh_ggf_bbww_m700 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m700",
    id=24214,
)

graviton_hh_ggf_bbww_m750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m750",
    id=24215,
)

graviton_hh_ggf_bbww_m800 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m800",
    id=24216,
)

graviton_hh_ggf_bbww_m850 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m850",
    id=24217,
)

graviton_hh_ggf_bbww_m900 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m900",
    id=24218,
)

graviton_hh_ggf_bbww_m1000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1000",
    id=24219,
)

graviton_hh_ggf_bbww_m1250 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1250",
    id=24220,
)

graviton_hh_ggf_bbww_m1500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1500",
    id=24221,
)

graviton_hh_ggf_bbww_m1750 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m1750",
    id=24222,
)

graviton_hh_ggf_bbww_m2000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2000",
    id=24223,
)

graviton_hh_ggf_bbww_m2500 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m2500",
    id=24224,
)

graviton_hh_ggf_bbww_m3000 = graviton_hh_ggf_bbww.add_process(
    name="graviton_hh_ggf_bbww_m3000",
    id=24225,
)
