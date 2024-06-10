# coding: utf-8

"""
Di-Higgs process definitions.

- hh: inclusive di-Higgs production
- hh_ggf: di-Higgs production via gluon-gluon fusion
- hh_vbf: di-Higgs production via vector boson fusion
- radion: radion production
- graviton: graviton production

Di-Higgs production channels:
- 20xxx: HH
- 21xxx: hh_ggf
- 22xxx: hh_vbf
- 23xxx: radion HH
- 24xxx: graviton HH
- 25xxx: radion VBF
- 26xxx: graviton VBF

"""

from __future__ import annotations

from order import Process
from scinum import Number

from cmsdb.util import add_xsecs


__all__ = [
    # Di-Higgs
    "hh",
    "hh_ggf", "hh_ggf_kl0_kt1", "hh_ggf_kl1_kt1", "hh_ggf_kl2p45_kt1", "hh_ggf_kl5_kt1",
    "hh_vbf", "hh_vbf_kv1_k2v1_kl1", "hh_vbf_kv1_k2v1_kl0", "hh_vbf_kv1_k2v1_kl2",
    "hh_vbf_kv1_k2v0_kl1", "hh_vbf_kv1_k2v2_kl1", "hh_vbf_kv0p5_k2v1_kl1", "hh_vbf_kv1p5_k2v1_kl1",
    "radion_hh_ggf", "graviton_hh_ggf", "radion_hh_vbf", "graviton_hh_vbf",
]

####################################################################################################
#
# HH
#
####################################################################################################


# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=90#Current_recommendations_for_HH_c
# scale is according to recommendation: scale + mtop unc
# pdf is according to recommendation: pdf + aS

hh = Process(
    name="hh",
    id=20000,
    label="HH",
)

hh_ggf = hh.add_process(
    name="hh_ggf",
    id=21000,
    label=r"$HH_{ggf}$",
    xsecs={
        13: 0.001 * Number(31.05, {
            "pdf": 0.03j,
            "scale": (0.06j, 0.23j),
        }),
        13.6: 0.001 * Number(34.43, {
            "pdf": 0.03j,
            "scale": (0.06j, 0.23j),
        }),
    },
    aux={"production_mode_parent": hh},
)

# Naming conventions, cross sections and uncertainties are based on:
# https://gitlab.cern.ch/hh/naming-conventions
# Missing uncertainties are based on:
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=89

hh_ggf_kl0_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl0_kt1",
    id=21001,
    xsecs={
        13: Number(0.069725, {
            "scale": (0.024j, 0.061j),
            "pdf": 0.03j,
            "mtop": (0.06j, 0.12j),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl1_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl1_kt1",
    id=21002,
    xsecs={
        13: Number(0.031047, {
            "scale": (0.022j, 0.050j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.18j),
        }),
        13.6: Number(0.03443, {  # value for mH=125 GeV
            "scale": (0.021j, 0.049j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.18j),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl2p45_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl2p45_kt1",
    id=21003,
    xsecs={
        13: Number(0.013124, {
            "scale": (0.023j, 0.051j),
            "pdf": 0.03j,
            "mtop": (0.04j, 0.22j),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

hh_ggf_kl5_kt1 = hh_ggf.add_process(
    name="hh_ggf_kl5_kt1",
    id=21004,
    xsecs={
        13: Number(0.091172, {
            "scale": (0.049j, 0.088j),
            "pdf": 0.03j,
            "mtop": (0.13j, 0.04j),
        }),
    },
    aux={"production_mode_parent": hh_ggf},
)

# Source: xsecs were given in fb but are converted to pb,
# uncertainties in %, values are taken for m_H = 125 GeV
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/LHCHWGHH?rev=90#HHjj_VBF

hh_vbf = hh.add_process(
    name="hh_vbf",
    id=22000,
    label=r"$HH_{vbf}$",
    xsecs={
        13: 0.001 * Number(1.726, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh},
)

hh_vbf_kv1_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl1",
    id=22001,
    xsecs={
        13: Number(0.0017260, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v1_kl0 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl0",
    id=22002,
    xsecs={
        13: Number(0.0046089, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v1_kl2 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v1_kl2",
    id=22003,
    xsecs={
        13: Number(0.0014228, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v0_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v0_kl1",
    id=22004,
    xsecs={
        13: Number(0.0270800, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1_k2v2_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1_k2v2_kl1",
    id=22005,
    xsecs={
        13: Number(0.00142178, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv0p5_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv0p5_k2v1_kl1",
    id=22006,
    xsecs={
        13: Number(0.0108237, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh_vbf_kv1p5_k2v1_kl1 = hh_vbf.add_process(
    name="hh_vbf_kv1p5_k2v1_kl1",
    id=22007,
    xsecs={
        13: Number(0.0660185, {
            "scale": (0.0003j, 0.0004j),
            "pdf": 0.021j,
        }),
    },
    aux={"production_mode_parent": hh_vbf},
)

hh.xsecs = add_xsecs(hh_ggf, hh_vbf)

####################################################################################################
#
# Resonant BSM HH production
#
####################################################################################################

radion_hh_ggf = hh_ggf.add_process(
    name="radion_hh_ggf",
    id=23000,
    label=r"Radion $\rightarrow HH_{ggf}$",
    xsecs={
        13: Number(0.1)},  # TODO
)

graviton_hh_ggf = hh_ggf.add_process(
    name="graviton_hh_ggf",
    id=24000,
    label=r"Graviton $\rightarrow HH_{ggf}$",
    xsecs={13: Number(0.1)},  # TODO
)

radion_hh_vbf = hh_vbf.add_process(
    name="radion_hh_vbf",
    id=25000,
    label=r"Radion $\rightarrow HH_{vbf}$",
    xsecs={13: Number(0.1)},  # TODO
)

graviton_hh_vbf = hh_vbf.add_process(
    name="graviton_hh_vbf",
    id=26000,
    label=r"Graviton $\rightarrow HH_{vbf}$",
    xsecs={13: Number(0.1)},  # TODO
)
