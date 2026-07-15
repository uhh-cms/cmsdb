# coding: utf-8

"""
HH -> 4tau/4v/2tau2v/2w2z (multi-lepton) process definitions.
"""

__all__ = [
    "hh_ggf_htt_htt",
    "hh_ggf_htt_htt_kl0_kt1",
    "hh_ggf_htt_htt_kl1_kt1",
    "hh_ggf_htt_htt_kl2p45_kt1",
    "hh_ggf_htt_htt_kl5_kt1",
    "hh_ggf_htt_hvv",
    "hh_ggf_htt_hvv_kl0_kt1",
    "hh_ggf_htt_hvv_kl1_kt1",
    "hh_ggf_htt_hvv_kl5_kt1",
    "hh_ggf_hvv_hvv",
    "hh_ggf_hvv_hvv_0l_kl1_kt1",
    "hh_ggf_hvv_hvv_1l_kl1_kt1",
    "hh_ggf_hvv_hvv_2lplus_kl0_kt1",
    "hh_ggf_hvv_hvv_2lplus_kl1_kt1",
    "hh_ggf_hvv_hvv_2lplus_kl2p45_kt1",
    "hh_ggf_hvv_hvv_2lplus_kl5_kt1",
    "hh_ggf_hvv_hvv_kl0_kt1",
    "hh_ggf_hvv_hvv_kl1_kt1",
    "hh_ggf_hvv_hvv_kl5_kt1",
    "hh_ggf_hww_hzz_3l_kl0_kt1",
    "hh_ggf_hww_hzz_3l_kl1_kt1",
    "hh_ggf_hww_hzz_3l_kl2p45_kt1",
    "hh_ggf_hww_hzz_3l_kl5_kt1",
    "hh_ggf_hww_hzz_4lplus_kl0_kt1",
    "hh_ggf_hww_hzz_4lplus_kl1_kt1",
    "hh_ggf_hww_hzz_4lplus_kl2p45_kt1",
    "hh_ggf_hww_hzz_4lplus_kl5_kt1",
    "hh_vbf_htt_htt",
    "hh_vbf_htt_htt_kv1_k2v0_kl1",
    "hh_vbf_htt_htt_kv1_k2v1_kl1",
    "hh_vbf_htt_htt_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_htt_htt_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_htt_htt_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_htt_htt_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_htt_htt_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_htt_htt_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_htt_htt_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_htt_htt_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_htt_hvv",
    "hh_vbf_htt_hvv_kv1_k2v0_kl1",
    "hh_vbf_htt_hvv_kv1_k2v1_kl1",
    "hh_vbf_htt_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_htt_hvv_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_htt_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_htt_hvv_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_htt_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_htt_hvv_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_htt_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hvv_hvv",
    "hh_vbf_hvv_hvv_0l_kv1_k2v1_kl1",
    "hh_vbf_hvv_hvv_1l_kv1_k2v1_kl1",
    "hh_vbf_hvv_hvv_2lplus_kv1_k2v0_kl1",
    "hh_vbf_hvv_hvv_2lplus_kv1_k2v1_kl1",
    "hh_vbf_hvv_hvv_2lplus_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hvv_hvv_2lplus_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_hvv_hvv_2lplus_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_hvv_hvv_2lplus_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hvv_hvv_2lplus_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_hvv_hvv_2lplus_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hvv_hvv_2lplus_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_hvv_hvv_2lplus_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hvv_hvv_kv1_k2v0_kl1",
    "hh_vbf_hvv_hvv_kv1_k2v1_kl1",
    "hh_vbf_hvv_hvv_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_hvv_hvv_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_hvv_hvv_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hvv_hvv_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_hvv_hvv_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hvv_hvv_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_hvv_hvv_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hww_hzz_3l_kv1_k2v0_kl1",
    "hh_vbf_hww_hzz_3l_kv1_k2v1_kl1",
    "hh_vbf_hww_hzz_3l_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hww_hzz_3l_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_hww_hzz_3l_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_hww_hzz_3l_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hww_hzz_3l_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_hww_hzz_3l_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hww_hzz_3l_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_hww_hzz_3l_kvm1p83_k2v3p57_klm3p39",
    "hh_vbf_hww_hzz_4lplus_kv1_k2v0_kl1",
    "hh_vbf_hww_hzz_4lplus_kv1_k2v1_kl1",
    "hh_vbf_hww_hzz_4lplus_kv1p74_k2v1p37_kl14p4",
    "hh_vbf_hww_hzz_4lplus_kv2p12_k2v3p87_klm5p96",
    "hh_vbf_hww_hzz_4lplus_kvm0p012_k2v0p03_kl10p2",
    "hh_vbf_hww_hzz_4lplus_kvm0p758_k2v1p44_klm19p3",
    "hh_vbf_hww_hzz_4lplus_kvm0p962_k2v0p959_klm1p43",
    "hh_vbf_hww_hzz_4lplus_kvm1p21_k2v1p94_klm0p94",
    "hh_vbf_hww_hzz_4lplus_kvm1p6_k2v2p72_klm1p36",
    "hh_vbf_hww_hzz_4lplus_kvm1p83_k2v3p57_klm3p39",
]

import cmsdb.constants as const

from cmsdb.processes.hh import (
    hh_ggf,
    hh_ggf_kl1_kt1, hh_ggf_kl0_kt1, hh_ggf_kl2p45_kt1, hh_ggf_kl5_kt1,
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

hh_ggf_htt_htt_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_htt_kl0_kt1",
    id=91001,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_htt_kl1_kt1",
    id=91002,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_htt_htt_kl2p45_kt1",
    id=91003,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.tttt),
)

hh_ggf_htt_htt_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_htt_kl5_kt1",
    id=91004,
    label=r"$HH_{ggf} \rightarrow 4\tau$ ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
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

hh_ggf_hvv_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl0_kt1",
    id=92001,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl1_kt1",
    id=92002,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl2p45_kt1",
    id=92003,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.vvvv),
)

hh_ggf_hvv_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_kl5_kt1",
    id=92004,
    label=r"$HH_{ggf} \rightarrow 4V$ ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv),
)


#
# ggF -> HH -> 4v (2L+)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hvv_hvv_2lplus = hh_ggf.add_process(
    name="hh_ggf_hvv_hvv_2lplus",
    id=92100,
    label=r"$HH_{ggf} \rightarrow 4V$ (2L+)",
)

hh_ggf_hvv_hvv_2lplus_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_2lplus_kl0_kt1",
    id=92101,
    label=r"$HH_{ggf} \rightarrow 4V$ (2L+) ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv_2lplus),
)

hh_ggf_hvv_hvv_2lplus_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_2lplus_kl1_kt1",
    id=92102,
    label=r"$HH_{ggf} \rightarrow 4V$ (2L+) ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv_2lplus),
)

hh_ggf_hvv_hvv_2lplus_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hvv_hvv_2lplus_kl2p45_kt1",
    id=92103,
    label=r"$HH_{ggf} \rightarrow 4V$ (2L+) ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.vvvv_2lplus),
)

hh_ggf_hvv_hvv_2lplus_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_2lplus_kl5_kt1",
    id=92104,
    label=r"$HH_{ggf} \rightarrow 4V$ (2L+) ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv_2lplus),
)


#
# ggF -> HH -> 4v (1L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hvv_hvv_1l = hh_ggf.add_process(
    name="hh_ggf_hvv_hvv_1l",
    id=92200,
    label=r"$HH_{ggf} \rightarrow 4V$ (1L)",
)

hh_ggf_hvv_hvv_1l_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_1l_kl0_kt1",
    id=92201,
    label=r"$HH_{ggf} \rightarrow 4V$ (1L) ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv_1l),
)

hh_ggf_hvv_hvv_1l_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_1l_kl1_kt1",
    id=92202,
    label=r"$HH_{ggf} \rightarrow 4V$ (1L) ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv_1l),
)

hh_ggf_hvv_hvv_1l_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hvv_hvv_1l_kl2p45_kt1",
    id=92203,
    label=r"$HH_{ggf} \rightarrow 4V$ (1L) ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.vvvv_1l),
)

hh_ggf_hvv_hvv_1l_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_1l_kl5_kt1",
    id=92204,
    label=r"$HH_{ggf} \rightarrow 4V$ (1L) ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv_1l),
)


#
# ggF -> HH -> 4v (0L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hvv_hvv_0l = hh_ggf.add_process(
    name="hh_ggf_hvv_hvv_0l",
    id=92300,
    label=r"$HH_{ggf} \rightarrow 4V$ (0L)",
)

hh_ggf_hvv_hvv_0l_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hvv_hvv_0l_kl0_kt1",
    id=92301,
    label=r"$HH_{ggf} \rightarrow 4V$ (0L) ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.vvvv_0l),
)

hh_ggf_hvv_hvv_0l_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hvv_hvv_0l_kl1_kt1",
    id=92302,
    label=r"$HH_{ggf} \rightarrow 4V$ (0L) ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.vvvv_0l),
)

hh_ggf_hvv_hvv_0l_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hvv_hvv_0l_kl2p45_kt1",
    id=92303,
    label=r"$HH_{ggf} \rightarrow 4V$ (0L) ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.vvvv_0l),
)

hh_ggf_hvv_hvv_0l_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hvv_hvv_0l_kl5_kt1",
    id=92304,
    label=r"$HH_{ggf} \rightarrow 4V$ (0L) ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.vvvv_0l),
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

hh_ggf_htt_hvv_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_htt_hvv_kl0_kt1",
    id=93001,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_htt_hvv_kl1_kt1",
    id=93002,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_htt_hvv_kl2p45_kt1",
    id=93003,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.ttvv),
)

hh_ggf_htt_hvv_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_htt_hvv_kl5_kt1",
    id=93004,
    label=r"$HH_{ggf} \rightarrow \tau\tau VV$ ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.ttvv),
)


#
# ggF -> HH -> 2w2z (3L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hww_hzz_3l = hh_ggf.add_process(
    name="hh_ggf_hww_hzz_3l",
    id=94000,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (3L)",
)

hh_ggf_hww_hzz_3l_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hww_hzz_3l_kl0_kt1",
    id=94001,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (3L) ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.wwzz_veto_nunu_3l),
)

hh_ggf_hww_hzz_3l_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hww_hzz_3l_kl1_kt1",
    id=94002,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (3L) ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.wwzz_veto_nunu_3l),
)

hh_ggf_hww_hzz_3l_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hww_hzz_3l_kl2p45_kt1",
    id=94003,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (3L) ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.wwzz_veto_nunu_3l),
)

hh_ggf_hww_hzz_3l_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hww_hzz_3l_kl5_kt1",
    id=94004,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (3L) ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.wwzz_veto_nunu_3l),
)


#
# ggF -> HH -> 2w2z (4L+)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_ggf_hww_hzz_4lplus = hh_ggf.add_process(
    name="hh_ggf_hww_hzz_4lplus",
    id=94100,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (4L+)",
)

hh_ggf_hww_hzz_4lplus_kl0_kt1 = hh_ggf_kl0_kt1.add_process(
    name="hh_ggf_hww_hzz_4lplus_kl0_kt1",
    id=94101,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (4L+) ($\kappa_{\lambda}=0$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl0_kt1, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_ggf_hww_hzz_4lplus_kl1_kt1 = hh_ggf_kl1_kt1.add_process(
    name="hh_ggf_hww_hzz_4lplus_kl1_kt1",
    id=94102,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (4L+) ($\kappa_{\lambda}=1$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl1_kt1, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_ggf_hww_hzz_4lplus_kl2p45_kt1 = hh_ggf_kl2p45_kt1.add_process(
    name="hh_ggf_hww_hzz_4lplus_kl2p45_kt1",
    id=94103,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (4L+) ($\kappa_{\lambda}=2.45$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl2p45_kt1, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_ggf_hww_hzz_4lplus_kl5_kt1 = hh_ggf_kl5_kt1.add_process(
    name="hh_ggf_hww_hzz_4lplus_kl5_kt1",
    id=94104,
    label=r"$HH_{ggf} \rightarrow WWZZ$ (4L+) ($\kappa_{\lambda}=5$, $\kappa_{t}=1$)",
    xsecs=multiply_xsecs(hh_ggf_kl5_kt1, const.br_hh.wwzz_veto_nunu_4lplus),
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

hh_vbf_htt_htt_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_htt_htt_kv1_k2v0_kl1",
    id=95001,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.tttt),
)

hh_vbf_htt_htt_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_htt_htt_kv1_k2v1_kl1",
    id=95002,
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.tttt),
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
    label=r"$HH_{vbf} \rightarrow 4\tau$ ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
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

hh_vbf_hvv_hvv_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v0_kl1",
    id=96001,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hvv_hvv_kv1_k2v1_kl1",
    id=96002,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv),
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
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv),
)

hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_kv2p12_k2v3p87_klm5p96",
    id=96010,
    label=r"$HH_{vbf} \rightarrow 4V$ ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.vvvv),
)


#
# vbf -> HH -> 4v (2L+)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hvv_hvv_2lplus = hh_vbf.add_process(
    name="hh_vbf_hvv_hvv_2lplus",
    id=96100,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+)",
)

hh_vbf_hvv_hvv_2lplus_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kv1_k2v0_kl1",
    id=96101,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kv1_k2v1_kl1",
    id=96102,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kv1p74_k2v1p37_kl14p4",
    id=96103,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p012_k2v0p03_kl10p2",
    id=96104,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p758_k2v1p44_klm19p3",
    id=96105,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm0p962_k2v0p959_klm1p43",
    id=96106,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p21_k2v1p94_klm0p94",
    id=96107,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p6_k2v2p72_klm1p36",
    id=96108,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kvm1p83_k2v3p57_klm3p39",
    id=96109,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv_2lplus),
)

hh_vbf_hvv_hvv_2lplus_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_2lplus_kv2p12_k2v3p87_klm5p96",
    id=96110,
    label=r"$HH_{vbf} \rightarrow 4V$ (2L+) ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.vvvv_2lplus),
)


#
# vbf -> HH -> 4v (1L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hvv_hvv_1l = hh_vbf.add_process(
    name="hh_vbf_hvv_hvv_1l",
    id=96200,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L)",
)

hh_vbf_hvv_hvv_1l_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hvv_hvv_1l_kv1_k2v0_kl1",
    id=96201,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hvv_hvv_1l_kv1_k2v1_kl1",
    id=96202,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_1l_kv1p74_k2v1p37_kl14p4",
    id=96203,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm0p012_k2v0p03_kl10p2",
    id=96204,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm0p758_k2v1p44_klm19p3",
    id=96205,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm0p962_k2v0p959_klm1p43",
    id=96206,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm1p21_k2v1p94_klm0p94",
    id=96207,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm1p6_k2v2p72_klm1p36",
    id=96208,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hvv_hvv_1l_kvm1p83_k2v3p57_klm3p39",
    id=96209,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv_1l),
)

hh_vbf_hvv_hvv_1l_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_1l_kv2p12_k2v3p87_klm5p96",
    id=96210,
    label=r"$HH_{vbf} \rightarrow 4V$ (1L) ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.vvvv_1l),
)


#
# vbf -> HH -> 4v (0L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hvv_hvv_0l = hh_vbf.add_process(
    name="hh_vbf_hvv_hvv_0l",
    id=96300,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L)",
)

hh_vbf_hvv_hvv_0l_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hvv_hvv_0l_kv1_k2v0_kl1",
    id=96301,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hvv_hvv_0l_kv1_k2v1_kl1",
    id=96302,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hvv_hvv_0l_kv1p74_k2v1p37_kl14p4",
    id=96303,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm0p012_k2v0p03_kl10p2",
    id=96304,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm0p758_k2v1p44_klm19p3",
    id=96305,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm0p962_k2v0p959_klm1p43",
    id=96306,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm1p21_k2v1p94_klm0p94",
    id=96307,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm1p6_k2v2p72_klm1p36",
    id=96308,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hvv_hvv_0l_kvm1p83_k2v3p57_klm3p39",
    id=96309,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.vvvv_0l),
)

hh_vbf_hvv_hvv_0l_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hvv_hvv_0l_kv2p12_k2v3p87_klm5p96",
    id=96310,
    label=r"$HH_{vbf} \rightarrow 4V$ (0L) ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.vvvv_0l),
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

hh_vbf_htt_hvv_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v0_kl1",
    id=97001,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_htt_hvv_kv1_k2v1_kl1",
    id=97002,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.ttvv),
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
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.ttvv),
)

hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_htt_hvv_kv2p12_k2v3p87_klm5p96",
    id=97010,
    label=r"$HH_{vbf} \rightarrow \tau\tau VV$ ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.ttvv),
)


#
# vbf -> HH -> 2w2z (3L)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hww_hzz_3l = hh_vbf.add_process(
    name="hh_vbf_hww_hzz_3l",
    id=98000,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L)",
)

hh_vbf_hww_hzz_3l_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hww_hzz_3l_kv1_k2v0_kl1",
    id=98001,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hww_hzz_3l_kv1_k2v1_kl1",
    id=98002,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hww_hzz_3l_kv1p74_k2v1p37_kl14p4",
    id=98003,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hww_hzz_3l_kvm0p012_k2v0p03_kl10p2",
    id=98004,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hww_hzz_3l_kvm0p758_k2v1p44_klm19p3",
    id=98005,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hww_hzz_3l_kvm0p962_k2v0p959_klm1p43",
    id=98006,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hww_hzz_3l_kvm1p21_k2v1p94_klm0p94",
    id=98007,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hww_hzz_3l_kvm1p6_k2v2p72_klm1p36",
    id=98008,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hww_hzz_3l_kvm1p83_k2v3p57_klm3p39",
    id=98009,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.wwzz_veto_nunu_3l),
)

hh_vbf_hww_hzz_3l_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hww_hzz_3l_kv2p12_k2v3p87_klm5p96",
    id=98010,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (3L) ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.wwzz_veto_nunu_3l),
)


#
# vbf -> HH -> 2w2z (4L+)
#

# placeholder for the general process, not used as parent process and should not have a cross section
hh_vbf_hww_hzz_4lplus = hh_vbf.add_process(
    name="hh_vbf_hww_hzz_4lplus",
    id=98100,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+)",
)

hh_vbf_hww_hzz_4lplus_kv1_k2v0_kl1 = hh_vbf_kv1_k2v0_kl1.add_process(
    name="hh_vbf_hww_hzz_4lplus_kv1_k2v0_kl1",
    id=98101,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=1$, $\kappa_{2V}=0$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v0_kl1, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kv1_k2v1_kl1 = hh_vbf_kv1_k2v1_kl1.add_process(
    name="hh_vbf_hww_hzz_4lplus_kv1_k2v1_kl1",
    id=98102,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=1$, $\kappa_{2V}=1$, $\kappa_{\lambda}=1$)",
    xsecs=multiply_xsecs(hh_vbf_kv1_k2v1_kl1, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kv1p74_k2v1p37_kl14p4 = hh_vbf_kv1p74_k2v1p37_kl14p4.add_process(
    name="hh_vbf_hww_hzz_4lplus_kv1p74_k2v1p37_kl14p4",
    id=98103,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=1.74$, $\kappa_{2V}=1.37$, $\kappa_{\lambda}=14.4$)",
    xsecs=multiply_xsecs(hh_vbf_kv1p74_k2v1p37_kl14p4, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm0p012_k2v0p03_kl10p2 = hh_vbf_kvm0p012_k2v0p03_kl10p2.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm0p012_k2v0p03_kl10p2",
    id=98104,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-0.012$, $\kappa_{2V}=0.03$, $\kappa_{\lambda}=10.2$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p012_k2v0p03_kl10p2, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm0p758_k2v1p44_klm19p3 = hh_vbf_kvm0p758_k2v1p44_klm19p3.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm0p758_k2v1p44_klm19p3",
    id=98105,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-0.758$, $\kappa_{2V}=1.44$, $\kappa_{\lambda}=-19.3$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p758_k2v1p44_klm19p3, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm0p962_k2v0p959_klm1p43 = hh_vbf_kvm0p962_k2v0p959_klm1p43.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm0p962_k2v0p959_klm1p43",
    id=98106,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-0.962$, $\kappa_{2V}=0.959$, $\kappa_{\lambda}=-1.43$)",
    xsecs=multiply_xsecs(hh_vbf_kvm0p962_k2v0p959_klm1p43, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm1p21_k2v1p94_klm0p94 = hh_vbf_kvm1p21_k2v1p94_klm0p94.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm1p21_k2v1p94_klm0p94",
    id=98107,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-1.21$, $\kappa_{2V}=1.94$, $\kappa_{\lambda}=-0.94$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p21_k2v1p94_klm0p94, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm1p6_k2v2p72_klm1p36 = hh_vbf_kvm1p6_k2v2p72_klm1p36.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm1p6_k2v2p72_klm1p36",
    id=98108,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-1.6$, $\kappa_{2V}=2.72$, $\kappa_{\lambda}=-1.36$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p6_k2v2p72_klm1p36, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kvm1p83_k2v3p57_klm3p39 = hh_vbf_kvm1p83_k2v3p57_klm3p39.add_process(
    name="hh_vbf_hww_hzz_4lplus_kvm1p83_k2v3p57_klm3p39",
    id=98109,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=-1.83$, $\kappa_{2V}=3.57$, $\kappa_{\lambda}=-3.39$)",
    xsecs=multiply_xsecs(hh_vbf_kvm1p83_k2v3p57_klm3p39, const.br_hh.wwzz_veto_nunu_4lplus),
)

hh_vbf_hww_hzz_4lplus_kv2p12_k2v3p87_klm5p96 = hh_vbf_kv2p12_k2v3p87_klm5p96.add_process(
    name="hh_vbf_hww_hzz_4lplus_kv2p12_k2v3p87_klm5p96",
    id=98110,
    label=r"$HH_{vbf} \rightarrow WWZZ$ (4L+) ($\kappa_{V}=2.12$, $\kappa_{2V}=3.87$, $\kappa_{\lambda}=-5.96$)",
    xsecs=multiply_xsecs(hh_vbf_kv2p12_k2v3p87_klm5p96, const.br_hh.wwzz_veto_nunu_4lplus),
)
