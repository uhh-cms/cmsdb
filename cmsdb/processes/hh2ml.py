# coding: utf-8

"""
HH -> 4tau/4v/2tau2v (multi-lepton) process definitions.
"""

__all__ = [
    "hh_ggf_htt_htt", "hh_ggf_htt_htt_kl0_kt1", "hh_ggf_htt_htt_kl1_kt1", "hh_ggf_htt_htt_kl5_kt1",
    "hh_ggf_hvv_hvv", "hh_ggf_hvv_hvv_kl0_kt1", "hh_ggf_hvv_hvv_kl1_kt1", "hh_ggf_hvv_hvv_kl5_kt1",
    "hh_ggf_htt_hvv", "hh_ggf_htt_hvv_kl0_kt1", "hh_ggf_htt_hvv_kl1_kt1", "hh_ggf_htt_hvv_kl5_kt1",
    "hh_vbf_htt_htt",
    "hh_vbf_htt_htt_kv1_k2v0_kl1", "hh_vbf_htt_htt_kv1_k2v1_kl1", "hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2", "hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43", "hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36", "hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_htt_htt_kvm2p12_k2v3p87_klm5p96",
    "hh_vbf_hvv_hvv",
    "hh_vbf_hvv_hvv_kv1_k2v0_kl1", "hh_vbf_hvv_hvv_kv1_k2v1_kl1", "hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2", "hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43", "hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36", "hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hvv_hvv_kvm2p12_k2v3p87_klm5p96",
    "hh_vbf_htt_hvv",
    "hh_vbf_htt_hvv_kv1_k2v0_kl1", "hh_vbf_htt_hvv_kv1_k2v1_kl1", "hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2", "hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43", "hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36", "hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_htt_hvv_kvm2p12_k2v3p87_klm5p96",
]

import cmsdb.constants as const

from cmsdb.processes.hh import (
    hh_ggf,
    hh_ggf_kl1_kt1, hh_ggf_kl0_kt1, hh_ggf_kl5_kt1,
    hh_vbf,
    hh_vbf_kv1_k2v1_kl1, hh_vbf_kv1_k2v0_kl1, hh_vbf_kv1p74_k2v1p37_kl14p4, hh_vbf_kvm0p012_k2v0p03_kl10p2,
    hh_vbf_kvm0p758_k2v1p44_klm19p3, hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_vbf_kvm1p21_k2v1p94_klm0p94,
    hh_vbf_kvm1p6_k2v2p72_klm1p36, hh_vbf_kvm1p83_k2v3p57_klm3p39, hh_vbf_kvm2p12_k2v3p87_klm5p96,
)
from cmsdb.util import multiply_xsecs


#
# ggF -> HH -> 4tau
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_htt_htt = hh_ggf.add_process(
    name="hh_ggf_htt_htt",
    id=31000,
    label=r"$HH_{ggf} \rightarrow 4\tau$",
)

hh_ggf_htt_htt_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_htt_kl1_kt1",
    id=31001,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_htt_kl0_kt1",
    id=31002,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_htt_kl5_kt1",
    id=31003,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.tttt),
)

#
# ggF -> HH -> 4v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hvv_hvv = hh_ggf.add_process(
    name="hh_ggf_hvv_hvv",
    id=32000,
    label=r"$HH_{ggf} \rightarrow 4V$",
)

hh_ggf_hvv_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl1_kt1",
    id=32001,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl0_kt1",
    id=32002,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl5_kt1",
    id=32003,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv),
)

#
# ggF -> HH -> 2tau2v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_htt_hvv = hh_ggf.add_process(
    name="hh_ggf_htt_hvv",
    id=33000,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$",
)

hh_ggf_htt_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_hvv_kl1_kt1",
    id=33001,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_hvv_kl0_kt1",
    id=33002,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_hvv_kl5_kt1",
    id=33003,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.ttvv),
)

#
# vbf -> HH -> 4tau
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_htt_htt = hh_vbf.add_process(
    name="hh_vbf_htt_htt",
    id=35000,
    label=r"$HH_{vbf} \rightarrow 4\tau$",
)

hh_vbf_htt_htt_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1",
    id=35001,
    label=r"$HH_{vbf} \rightarrow 4\tau$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1",
    id=35002,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4",
    id=35003,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2",
    id=35004,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3",
    id=35005,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43",
    id=35006,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94",
    id=35007,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36",
    id=35008,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39",
    id=35009,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm2p12_k2v3p87_klm5p96 = hh_vbf_kvm2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_htt_htt_kvm2p12_k2v3p87_klm5p96",
    id=35010,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kvm2p12_k2v3p87_klm5p96, const.br_hh.tttt),
)

#
# vbf -> HH -> 4v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hvv_hvv = hh_vbf.add_process(
    name="hh_vbf_hvv_hvv",
    id=36000,
    label=r"$HH_{vbf} \rightarrow 4V$",
)

hh_vbf_hvv_hvv_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1",
    id=36001,
    label=r"$HH_{vbf} \rightarrow 4V$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1",
    id=36002,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4",
    id=36003,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2",
    id=36004,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3",
    id=36005,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43",
    id=36006,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94",
    id=36007,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36",
    id=36008,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39",
    id=36009,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm2p12_k2v3p87_klm5p96 = hh_vbf_kvm2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_kvm2p12_k2v3p87_klm5p96",
    id=36010,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kvm2p12_k2v3p87_klm5p96, const.br_hh.vvvv),
)

#
# vbf -> HH -> 2tau2v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_htt_hvv = hh_vbf.add_process(
    name="hh_vbf_htt_hvv",
    id=37000,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$",
)

hh_vbf_htt_hvv_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1",
    id=37001,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1",
    id=37002,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4",
    id=37003,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2",
    id=37004,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3",
    id=37005,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43",
    id=37006,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94",
    id=37007,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36",
    id=37008,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39",
    id=37009,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm2p12_k2v3p87_klm5p96 = hh_vbf_kvm2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_htt_hvv_kvm2p12_k2v3p87_klm5p96",
    id=37010,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kvm2p12_k2v3p87_klm5p96, const.br_hh.ttvv),
)
