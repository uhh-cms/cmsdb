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
    "hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_hvv_hvv",
    "hh_vbf_hvv_hvv_kv1_k2v0_kl1", "hh_vbf_hvv_hvv_kv1_k2v1_kl1", "hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2", "hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43", "hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36", "hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_htt_hvv",
    "hh_vbf_htt_hvv_kv1_k2v0_kl1", "hh_vbf_htt_hvv_kv1_k2v1_kl1", "hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2", "hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43", "hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36", "hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96",
]

import cmsdb.constants as const

from cmsdb.processes.hh import (
    hh_ggf,
    hh_ggf_kl1_kt1, hh_ggf_kl0_kt1, hh_ggf_kl5_kt1,
    hh_vbf,
    hh_vbf_kv1_k2v1_kl1, hh_vbf_kv1_k2v0_kl1, hh_vbf_kv1p74_k2v1p37_kl14p4, hh_vbf_kvm0p012_k2v0p03_kl10p2,
    hh_vbf_kvm0p758_k2v1p44_klm19p3, hh_vbf_kvm0p962_k2v0p959_klm1p43, hh_vbf_kvm1p21_k2v1p94_klm0p94,
    hh_vbf_kvm1p6_k2v2p72_klm1p36, hh_vbf_kvm1p83_k2v3p57_klm3p39, hh_vbf_kv2p12_k2v3p87_klm5p96,
)
from cmsdb.util import multiply_xsecs


#
# ggF -> HH -> 4tau
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_htt_htt = hh_ggf.add_process(
    name="hh_ggf_htt_htt",
    id=91000,
    label=r"$HH_{ggf} \rightarrow 4\tau$",
)

hh_ggf_htt_htt_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_htt_kl1_kt1",
    id=91001,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_htt_kl0_kt1",
    id=91002,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_htt_kl5_kt1",
    id=91003,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.tttt),
)

#
# ggF -> HH -> 4v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hvv_hvv = hh_ggf.add_process(
    name="hh_ggf_hvv_hvv",
    id=92000,
    label=r"$HH_{ggf} \rightarrow 4V$",
)

hh_ggf_hvv_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl1_kt1",
    id=92001,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl0_kt1",
    id=92002,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl5_kt1",
    id=92003,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv),
)

#
# ggF -> HH -> 2tau2v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_htt_hvv = hh_ggf.add_process(
    name="hh_ggf_htt_hvv",
    id=93000,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$",
)

hh_ggf_htt_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_hvv_kl1_kt1",
    id=93001,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_hvv_kl0_kt1",
    id=93002,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_hvv_kl5_kt1",
    id=93003,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=5$, $\kappa_t=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.ttvv),
)

#
# vbf -> HH -> 4tau
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_htt_htt = hh_vbf.add_process(
    name="hh_vbf_htt_htt",
    id=95000,
    label=r"$HH_{vbf} \rightarrow 4\tau$",
)

hh_vbf_htt_htt_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1",
    id=95001,
    label=r"$HH_{vbf} \rightarrow 4\tau$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1",
    id=95002,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4",
    id=95003,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2",
    id=95004,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3",
    id=95005,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43",
    id=95006,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94",
    id=95007,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36",
    id=95008,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.tttt),
)

hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39",
    id=95009,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96",
    id=95010,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.tttt),
)

#
# vbf -> HH -> 4v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hvv_hvv = hh_vbf.add_process(
    name="hh_vbf_hvv_hvv",
    id=96000,
    label=r"$HH_{vbf} \rightarrow 4V$",
)

hh_vbf_hvv_hvv_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1",
    id=96001,
    label=r"$HH_{vbf} \rightarrow 4V$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1",
    id=96002,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4",
    id=96003,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2",
    id=96004,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3",
    id=96005,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43",
    id=96006,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94",
    id=96007,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36",
    id=96008,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39",
    id=96009,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96",
    id=96010,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.vvvv),
)

#
# vbf -> HH -> 2tau2v
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_htt_hvv = hh_vbf.add_process(
    name="hh_vbf_htt_hvv",
    id=97000,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$",
)

hh_vbf_htt_hvv_kv1_k2v1_kl1 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1",
    id=97001,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ (SM)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv1_k2v0_kl1 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1",
    id=97002,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=0$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4",
    id=97003,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2",
    id=97004,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3",
    id=97005,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43",
    id=97006,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94",
    id=97007,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36",
    id=97008,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39",
    id=97009,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96",
    id=97010,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.ttvv),
)
