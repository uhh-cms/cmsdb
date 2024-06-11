# coding: utf-8

"""
HH -> bbtautau process definitions.

IDs are assigned in the range 21100-21199 for hh_ggf and 22100-22199 for hh_vbf.
For radion ggf, the IDs are the range 23100-23199.
For graviton ggf, the IDs are the range 24100-24199.
For radion vbf, the IDs are the range 25100-25199.
For graviton vbf, the IDs are the range 26100-26199.
"""

__all__ = [
    "hh_ggf_hbb_htt_kl1_kt1", "hh_ggf_hbb_htt_kl0_kt1", "hh_ggf_hbb_htt_kl0_kt1_c21",
    "hh_ggf_hbb_htt_kl1_kt1_c20p10", "hh_ggf_hbb_htt_kl1_kt1_c20p35", "hh_ggf_hbb_htt_kl1_kt1_c23",
    "hh_ggf_hbb_htt_kl1_kt1_c2m2", "hh_ggf_hbb_htt_kl2p45_kt1", "hh_ggf_hbb_htt_kl5_kt1",
    "hh_ggf_hbb_htt_node1", "hh_ggf_hbb_htt_node2", "hh_ggf_hbb_htt_node3",
    "hh_ggf_hbb_htt_node4", "hh_ggf_hbb_htt_node5", "hh_ggf_hbb_htt_node6",
    "hh_ggf_hbb_htt_node7", "hh_ggf_hbb_htt_node8", "hh_ggf_hbb_htt_node9",
    "hh_ggf_hbb_htt_node10", "hh_ggf_hbb_htt_node11", "hh_ggf_hbb_htt_node12",
    "radion_hh_ggf_hbb_htt",
    "radion_hh_ggf_hbb_htt_m250", "radion_hh_ggf_hbb_htt_m260", "radion_hh_ggf_hbb_htt_m270",
    "radion_hh_ggf_hbb_htt_m280", "radion_hh_ggf_hbb_htt_m300", "radion_hh_ggf_hbb_htt_m320",
    "radion_hh_ggf_hbb_htt_m350", "radion_hh_ggf_hbb_htt_m400", "radion_hh_ggf_hbb_htt_m450",
    "radion_hh_ggf_hbb_htt_m500", "radion_hh_ggf_hbb_htt_m550", "radion_hh_ggf_hbb_htt_m600",
    "radion_hh_ggf_hbb_htt_m650", "radion_hh_ggf_hbb_htt_m700", "radion_hh_ggf_hbb_htt_m750",
    "radion_hh_ggf_hbb_htt_m800", "radion_hh_ggf_hbb_htt_m850", "radion_hh_ggf_hbb_htt_m900",
    "radion_hh_ggf_hbb_htt_m1000", "radion_hh_ggf_hbb_htt_m1250", "radion_hh_ggf_hbb_htt_m1500",
    "radion_hh_ggf_hbb_htt_m1750", "radion_hh_ggf_hbb_htt_m2000", "radion_hh_ggf_hbb_htt_m2500",
    "radion_hh_ggf_hbb_htt_m3000", "radion_hh_ggf_hbb_htt_m1100", "radion_hh_ggf_hbb_htt_m2400",
    "radion_hh_ggf_hbb_htt_m1300", "radion_hh_ggf_hbb_htt_m1700", "radion_hh_ggf_hbb_htt_m1200",
    "radion_hh_ggf_hbb_htt_m2200", "radion_hh_ggf_hbb_htt_m2600", "radion_hh_ggf_hbb_htt_m1400",
    "radion_hh_ggf_hbb_htt_m2800", "radion_hh_ggf_hbb_htt_m1600", "radion_hh_ggf_hbb_htt_m1900",
    "radion_hh_ggf_hbb_htt_m1800",
    "graviton_hh_ggf_hbb_htt",
    "graviton_hh_ggf_hbb_htt_m250", "graviton_hh_ggf_hbb_htt_m260",
    "graviton_hh_ggf_hbb_htt_m270", "graviton_hh_ggf_hbb_htt_m280",
    "graviton_hh_ggf_hbb_htt_m300", "graviton_hh_ggf_hbb_htt_m320",
    "graviton_hh_ggf_hbb_htt_m350", "graviton_hh_ggf_hbb_htt_m400",
    "graviton_hh_ggf_hbb_htt_m450", "graviton_hh_ggf_hbb_htt_m500",
    "graviton_hh_ggf_hbb_htt_m550", "graviton_hh_ggf_hbb_htt_m600",
    "graviton_hh_ggf_hbb_htt_m650", "graviton_hh_ggf_hbb_htt_m700",
    "graviton_hh_ggf_hbb_htt_m750", "graviton_hh_ggf_hbb_htt_m800",
    "graviton_hh_ggf_hbb_htt_m850", "graviton_hh_ggf_hbb_htt_m900",
    "graviton_hh_ggf_hbb_htt_m1000", "graviton_hh_ggf_hbb_htt_m1250",
    "graviton_hh_ggf_hbb_htt_m1500", "graviton_hh_ggf_hbb_htt_m1750",
    "graviton_hh_ggf_hbb_htt_m2000", "graviton_hh_ggf_hbb_htt_m2500",
    "graviton_hh_ggf_hbb_htt_m3000",
    "hh_vbf_hbb_htt_kv1_k2v1_kl1", "hh_vbf_hbb_htt_kv1_k2v0_kl1", "hh_vbf_hbb_htt_kv1_k2v1_kl2",
    "hh_vbf_hbb_htt_kv1_k2v2_kl1", "hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hbb_htt_kvm0p012_k2v0p030_kl10p2", "hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43", "hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hbb_htt_kvm1p60_k2v2p72_klm1p36", "hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hbb_htt_kvm2p12_k2v3p87_klm5p96",
    "radion_hh_vbf_hbb_htt",
    "radion_hh_vbf_hbb_htt_m250", "radion_hh_vbf_hbb_htt_m260", "radion_hh_vbf_hbb_htt_m270",
    "radion_hh_vbf_hbb_htt_m280", "radion_hh_vbf_hbb_htt_m300", "radion_hh_vbf_hbb_htt_m320",
    "radion_hh_vbf_hbb_htt_m350", "radion_hh_vbf_hbb_htt_m400", "radion_hh_vbf_hbb_htt_m450",
    "radion_hh_vbf_hbb_htt_m500", "radion_hh_vbf_hbb_htt_m550", "radion_hh_vbf_hbb_htt_m600",
    "radion_hh_vbf_hbb_htt_m650", "radion_hh_vbf_hbb_htt_m700", "radion_hh_vbf_hbb_htt_m750",
    "radion_hh_vbf_hbb_htt_m800", "radion_hh_vbf_hbb_htt_m850", "radion_hh_vbf_hbb_htt_m900",
    "radion_hh_vbf_hbb_htt_m1000", "radion_hh_vbf_hbb_htt_m1250", "radion_hh_vbf_hbb_htt_m1500",
    "radion_hh_vbf_hbb_htt_m1750", "radion_hh_vbf_hbb_htt_m2000", "radion_hh_vbf_hbb_htt_m2500",
    "radion_hh_vbf_hbb_htt_m3000",
    "graviton_hh_vbf_hbb_htt",
    "graviton_hh_vbf_hbb_htt_m250", "graviton_hh_vbf_hbb_htt_m260",
    "graviton_hh_vbf_hbb_htt_m270", "graviton_hh_vbf_hbb_htt_m280",
    "graviton_hh_vbf_hbb_htt_m300", "graviton_hh_vbf_hbb_htt_m320",
    "graviton_hh_vbf_hbb_htt_m350", "graviton_hh_vbf_hbb_htt_m400",
    "graviton_hh_vbf_hbb_htt_m450", "graviton_hh_vbf_hbb_htt_m500",
    "graviton_hh_vbf_hbb_htt_m550", "graviton_hh_vbf_hbb_htt_m600",
    "graviton_hh_vbf_hbb_htt_m650", "graviton_hh_vbf_hbb_htt_m700",
    "graviton_hh_vbf_hbb_htt_m750", "graviton_hh_vbf_hbb_htt_m800",
    "graviton_hh_vbf_hbb_htt_m850", "graviton_hh_vbf_hbb_htt_m900",
    "graviton_hh_vbf_hbb_htt_m1000", "graviton_hh_vbf_hbb_htt_m1250",
    "graviton_hh_vbf_hbb_htt_m1500", "graviton_hh_vbf_hbb_htt_m1750",
    "graviton_hh_vbf_hbb_htt_m2000", "graviton_hh_vbf_hbb_htt_m2500",
    "graviton_hh_vbf_hbb_htt_m3000",
]

from scinum import Number
import cmsdb.constants as const

from cmsdb.processes.hh import (
    hh_ggf, radion_hh_ggf, graviton_hh_ggf, hh_vbf, radion_hh_vbf, graviton_hh_vbf,
    hh_ggf_kl1_kt1, hh_ggf_kl0_kt1, hh_ggf_kl0_kt1_c21,
    hh_ggf_kl1_kt1_c20p10, hh_ggf_kl1_kt1_c20p35, hh_ggf_kl1_kt1_c23,
    hh_ggf_kl1_kt1_c2m2, hh_ggf_kl2p45_kt1, hh_ggf_kl5_kt1,
    hh_vbf_kv1_k2v1_kl1, hh_vbf_kv1_k2v0_kl1, hh_vbf_kv1_k2v1_kl2,
    hh_vbf_kv1_k2v2_kl1, hh_vbf_kv1p74_k2v1p37_kl14p4,
    hh_vbf_kvm0p012_k2v0p030_kl10p2, hh_vbf_kvm0p758_k2v1p44_klm19p3,
    hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_vbf_kvm1p21_k2v1p94_klm0p94,
    hh_vbf_kvm1p60_k2v2p72_klm1p36, hh_vbf_kvm1p83_k2v3p57_klm3p39,
    hh_vbf_kvm2p12_k2v3p87_klm5p96,
)
from cmsdb.xsec_bsm_nodes import calculate_xsec_node
#
# ggF -> H -> HH
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hbb_htt = hh_ggf.add_process(
    name="hh_ggf_hbb_htt",
    id=21100,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$",
)

hh_ggf_hbb_htt_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hbb_htt_kl1_kt1",
    id=21101,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs={
        13: hh_ggf_kl1_kt1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl1_kt1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_node1 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node1",
    id=21102,
    label=f"{hh_ggf_hbb_htt.label} (node 1)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=1),
    },
)

hh_ggf_hbb_htt_node2 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node2",
    id=21103,
    label=f"{hh_ggf_hbb_htt.label} (node 2)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=2),
    },
)

hh_ggf_hbb_htt_node3 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node3",
    id=21104,
    label=f"{hh_ggf_hbb_htt.label} (node 3)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=3),
    },
)

hh_ggf_hbb_htt_node4 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node4",
    id=21105,
    label=f"{hh_ggf_hbb_htt.label} (node 4)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=4),
    },
)

hh_ggf_hbb_htt_node5 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node5",
    id=21106,
    label=f"{hh_ggf_hbb_htt.label} (node 5)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=5),
    },
)

hh_ggf_hbb_htt_node6 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node6",
    id=21107,
    label=f"{hh_ggf_hbb_htt.label} (node 6)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=6),
    },
)

hh_ggf_hbb_htt_node7 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node7",
    id=21108,
    label=f"{hh_ggf_hbb_htt.label} (node 7)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=7),
    },
)

hh_ggf_hbb_htt_node8 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node8",
    id=21109,
    label=f"{hh_ggf_hbb_htt.label} (node 8)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=8),
    },
)

hh_ggf_hbb_htt_node9 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node9",
    id=21110,
    label=f"{hh_ggf_hbb_htt.label} (node 9)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=9),
    },
)

hh_ggf_hbb_htt_node10 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node10",
    id=21111,
    label=f"{hh_ggf_hbb_htt.label} (node 10)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=10),
    },
)

hh_ggf_hbb_htt_node11 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node11",
    id=21112,
    label=f"{hh_ggf_hbb_htt.label} (node 11)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=11),
    },
)

hh_ggf_hbb_htt_node12 = hh_ggf.add_process(
    name="hh_ggf_hbb_htt_node12",
    id=21113,
    label=f"{hh_ggf_hbb_htt.label} (node 12)",
    xsecs={
        13: calculate_xsec_node(13, hh_ggf_hbb_htt_kl1_kt1.get_xsec(13), node_number=12),
    },
)

hh_ggf_hbb_htt_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hbb_htt_kl0_kt1",
    id=21114,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs={
        13: hh_ggf_kl0_kt1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl0_kt1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl0_kt1_c21 = hh_ggf_kl0_kt1_c21.add_process(
    name="hh_ggf_hbb_htt_kl0_kt1_c21",
    id=21115,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 0$, $\kappa_t = 1, C_2 = 1$)",
    xsecs={
        13: hh_ggf_kl0_kt1_c21.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl0_kt1_c21.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl1_kt1_c20p10 = hh_ggf_kl1_kt1_c20p10.add_process(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p10",
    id=21116,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 0.1$)",
    xsecs={
        13: hh_ggf_kl1_kt1_c20p10.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl1_kt1_c20p10.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl1_kt1_c20p35 = hh_ggf_kl1_kt1_c20p35.add_process(
    name="hh_ggf_hbb_htt_kl1_kt1_c20p35",
    id=21117,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 0.35$)",
    xsecs={
        13: hh_ggf_kl1_kt1_c20p35.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl1_kt1_c20p35.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl1_kt1_c23 = hh_ggf_kl1_kt1_c23.add_process(
    name="hh_ggf_hbb_htt_kl1_kt1_c23",
    id=21118,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = 3$)",
    xsecs={
        13: hh_ggf_kl1_kt1_c23.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl1_kt1_c23.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl1_kt1_c2m2 = hh_ggf_kl1_kt1_c2m2.add_process(
    name="hh_ggf_hbb_htt_kl1_kt1_c2m2",
    id=21119,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 1$, $\kappa_t = 1, C_2 = -2$)",
    xsecs={
        13: hh_ggf_kl1_kt1_c2m2.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl1_kt1_c2m2.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hbb_htt_kl2p45_kt1",
    id=21120,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 2.45$, $\kappa_t = 1$)",
    xsecs={
        13: hh_ggf_kl2p45_kt1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl2p45_kt1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_ggf_hbb_htt_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hbb_htt_kl5_kt1",
    id=21121,
    label=r"$HH_{ggf} \rightarrow bb\tau\tau$ ($\kappa_{\lambda} = 5$, $\kappa_t = 1$)",
    xsecs={
        13: hh_ggf_kl5_kt1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_ggf_kl5_kt1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)


#
# ggF -> radion -> HH
#

radion_hh_ggf_hbb_htt = radion_hh_ggf.add_process(
    name="radion_hh_ggf_hbb_htt",
    id=23100,
    label=rf"{radion_hh_ggf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: radion_hh_ggf.get_xsec(13) * const.br_hh.bbtt},  # TODO
)

radion_hh_ggf_hbb_htt_m250 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m250",
    id=23101,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m260 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m260",
    id=23102,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m270 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m270",
    id=23103,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m280 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m280",
    id=23104,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m300 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m300",
    id=23105,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m320 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m320",
    id=23106,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m350 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m350",
    id=23107,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m400 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m400",
    id=23108,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m450 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m450",
    id=23109,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m500 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m500",
    id=23110,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m550 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m550",
    id=23111,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m600 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m600",
    id=23112,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m650 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m650",
    id=23113,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m700 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m700",
    id=23114,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m750 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m750",
    id=23115,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m800 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m800",
    id=23116,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m850 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m850",
    id=23117,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m900 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m900",
    id=23118,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1000 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1000",
    id=23119,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1250 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1250",
    id=23120,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1500 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1500",
    id=23121,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1750 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1750",
    id=23122,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2000 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2000",
    id=23123,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2500 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2500",
    id=23124,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m3000 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m3000",
    id=23125,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1100 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1100",
    id=23126,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2400 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2400",
    id=23127,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1300 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1300",
    id=23128,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1700 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1700",
    id=23129,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1200 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1200",
    id=23130,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2200 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2200",
    id=23131,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2600 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2600",
    id=23132,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1400 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1400",
    id=23133,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m2800 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m2800",
    id=23134,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1600 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1600",
    id=23135,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_ggf_hbb_htt_m1900 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1900",
    id=23136,
    xsecs={13: Number(0.1)},  # TODO
)


radion_hh_ggf_hbb_htt_m1800 = radion_hh_ggf_hbb_htt.add_process(
    name="radion_hh_ggf_hbb_htt_m1800",
    id=23137,
    xsecs={13: Number(0.1)},  # TODO
)

#
# ggF -> bulk graviton -> HH
#

graviton_hh_ggf_hbb_htt = graviton_hh_ggf.add_process(
    name="graviton_hh_ggf_hbb_htt",
    id=24100,
    label=rf"{graviton_hh_ggf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: graviton_hh_ggf.get_xsec(13) * const.br_hh.bbtt},  # TODO
)

graviton_hh_ggf_hbb_htt_m250 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m250",
    id=24101,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m260 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m260",
    id=24102,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m270 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m270",
    id=24103,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m280 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m280",
    id=24104,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m300 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m300",
    id=24105,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m320 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m320",
    id=24106,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m350 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m350",
    id=24107,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m400 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m400",
    id=24108,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m450 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m450",
    id=24109,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m500 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m500",
    id=24110,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m550 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m550",
    id=24111,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m600 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m600",
    id=24112,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m650 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m650",
    id=24113,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m700 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m700",
    id=24114,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m750 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m750",
    id=24115,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m800 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m800",
    id=24116,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m850 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m850",
    id=24117,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m900 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m900",
    id=24118,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m1000 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m1000",
    id=24119,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m1250 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m1250",
    id=24120,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m1500 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m1500",
    id=24121,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m1750 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m1750",
    id=24122,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m2000 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m2000",
    id=24123,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m2500 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m2500",
    id=24124,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_ggf_hbb_htt_m3000 = graviton_hh_ggf_hbb_htt.add_process(
    name="graviton_hh_ggf_hbb_htt_m3000",
    id=24125,
    xsecs={13: Number(0.1)},  # TODO
)

#
# vbf -> H -> HH
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hbb_htt = hh_vbf.add_process(
    name="hh_vbf_hbb_htt",
    id=22100,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$",
)

hh_vbf_hbb_htt_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl1",
    id=22101,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ (SM)",
    xsecs={
        13: hh_vbf_kv1_k2v1_kl1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kv1_k2v1_kl1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hbb_htt_kv1_k2v0_kl1",
    id=22102,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs={
        13: hh_vbf_kv1_k2v0_kl1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kv1_k2v0_kl1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kv1_k2v1_kl2 = hh_vbf_kv1_k2v1_kl2.add_process(
    name="hh_vbf_hbb_htt_kv1_k2v1_kl2",
    id=22103,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=2$)",
    xsecs={
        13: hh_vbf_kv1_k2v1_kl2.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kv1_k2v1_kl2.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kv1_k2v2_kl1 = hh_vbf_kv1_k2v2_kl1.add_process(
    name="hh_vbf_hbb_htt_kv1_k2v2_kl1",
    id=22104,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=2$, $\kappa_{\lambda}=1$)",
    xsecs={
        13: hh_vbf_kv1_k2v2_kl1.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kv1_k2v2_kl1.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hbb_htt_kv1p74_k2v1p37_kl14p4",
    id=22105,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs={
        13: hh_vbf_kv1p74_k2v1p37_kl14p4.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kv1p74_k2v1p37_kl14p4.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm0p012_k2v0p030_kl10p2 = hh_vbf_kvm0p012_k2v0p030_kl10p2.add_process(
    name="hh_vbf_hbb_htt_kvm0p012_k2v0p030_kl10p2",
    id=22106,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.030$, $\kappa_{\lambda}=10.2$)",
    xsecs={
        13: hh_vbf_kvm0p012_k2v0p030_kl10p2.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm0p012_k2v0p030_kl10p2.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hbb_htt_kvm0p758_k2v1p44_klm19p3",
    id=22107,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs={
        13: hh_vbf_kvm0p758_k2v1p44_klm19p3.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm0p758_k2v1p44_klm19p3.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hbb_htt_kvm0p962_k2v0p959_klm1p43",
    id=22108,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs={
        13: hh_vbf_kvm0p962_k2v0p959_klm1p43.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm0p962_k2v0p959_klm1p43.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hbb_htt_kvm1p21_k2v1p94_klm0p94",
    id=22109,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs={
        13: hh_vbf_kvm1p21_k2v1p94_klm0p94.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm1p21_k2v1p94_klm0p94.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm1p60_k2v2p72_klm1p36 = hh_vbf_kvm1p60_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hbb_htt_kvm1p60_k2v2p72_klm1p36",
    id=22110,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-1.60$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs={
        13: hh_vbf_kvm1p60_k2v2p72_klm1p36.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm1p60_k2v2p72_klm1p36.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hbb_htt_kvm1p83_k2v3p57_klm3p39",
    id=22111,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs={
        13: hh_vbf_kvm1p83_k2v3p57_klm3p39.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm1p83_k2v3p57_klm3p39.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

hh_vbf_hbb_htt_kvm2p12_k2v3p87_klm5p96 = hh_vbf_kvm2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hbb_htt_kvm2p12_k2v3p87_klm5p96",
    id=22112,
    label=r"$HH_{vbf} \rightarrow bb\tau\tau$ ($\kappa_{V}=-2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs={
        13: hh_vbf_kvm2p12_k2v3p87_klm5p96.get_xsec(13) * const.br_hh.bbtt,
        13.6: hh_vbf_kvm2p12_k2v3p87_klm5p96.get_xsec(13.6) * const.br_hh.bbtt,
    },
)

#
# vbf -> radion -> HH
#

radion_hh_vbf_hbb_htt = radion_hh_vbf.add_process(
    name="radion_hh_vbf_hbb_htt",
    id=25100,
    label=rf"{radion_hh_vbf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: radion_hh_vbf.get_xsec(13) * const.br_hh.bbtt},  # TODO
)

radion_hh_vbf_hbb_htt_m250 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m250",
    id=25101,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m260 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m260",
    id=25102,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m270 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m270",
    id=25103,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m280 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m280",
    id=25104,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m300 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m300",
    id=25105,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m320 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m320",
    id=25106,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m350 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m350",
    id=25107,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m400 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m400",
    id=25108,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m450 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m450",
    id=25109,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m500 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m500",
    id=25110,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m550 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m550",
    id=25111,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m600 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m600",
    id=25112,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m650 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m650",
    id=25113,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m700 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m700",
    id=25114,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m750 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m750",
    id=25115,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m800 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m800",
    id=25116,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m850 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m850",
    id=25117,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m900 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m900",
    id=25118,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m1000 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m1000",
    id=25119,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m1250 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m1250",
    id=25120,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m1500 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m1500",
    id=25121,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m1750 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m1750",
    id=25122,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m2000 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m2000",
    id=25123,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m2500 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m2500",
    id=25124,
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf_hbb_htt_m3000 = radion_hh_vbf_hbb_htt.add_process(
    name="radion_hh_vbf_hbb_htt_m3000",
    id=25125,
    xsecs={13: Number(0.1)},  # TODO
)


#
# vbf -> bulk graviton -> HH
#

graviton_hh_vbf_hbb_htt = graviton_hh_vbf.add_process(
    name="graviton_hh_vbf_hbb_htt",
    id=26100,
    label=rf"{graviton_hh_vbf.label} $\rightarrow bb\tau\tau$",
    xsecs={13: graviton_hh_vbf.get_xsec(13) * const.br_hh.bbtt},  # TODO
)

graviton_hh_vbf_hbb_htt_m250 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m250",
    id=26101,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m260 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m260",
    id=26102,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m270 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m270",
    id=26103,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m280 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m280",
    id=26104,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m300 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m300",
    id=26105,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m320 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m320",
    id=26106,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m350 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m350",
    id=26107,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m400 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m400",
    id=26108,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m450 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m450",
    id=26109,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m500 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m500",
    id=26110,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m550 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m550",
    id=26111,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m600 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m600",
    id=26112,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m650 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m650",
    id=26113,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m700 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m700",
    id=26114,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m750 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m750",
    id=26115,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m800 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m800",
    id=26116,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m850 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m850",
    id=26117,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m900 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m900",
    id=26118,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m1000 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m1000",
    id=26119,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m1250 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m1250",
    id=26120,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m1500 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m1500",
    id=26121,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m1750 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m1750",
    id=26122,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m2000 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m2000",
    id=26123,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m2500 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m2500",
    id=26124,
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf_hbb_htt_m3000 = graviton_hh_vbf_hbb_htt.add_process(
    name="graviton_hh_vbf_hbb_htt_m3000",
    id=26125,
    xsecs={13: Number(0.1)},  # TODO
)
