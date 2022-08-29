# coding: utf-8

"""
QCD-related process definitions.
"""

__all__ = [
    "qcd",
    "qcd_ht50to100", "qcd_ht100to200", "qcd_ht200to300", "qcd_ht300to500", "qcd_ht500to700",
    "qcd_ht700to1000", "qcd_ht1000to1500", "qcd_ht1500to2000", "qcd_ht2000",
]

from order import Process
from scinum import Number


#
# QCD
#

qcd = Process(
    name="qcd",
    id=30000,
    label="QCD",
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht50to100 = qcd.add_process(
    name="qcd_ht50to100",
    id=31001,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht100to200 = qcd.add_process(
    name="qcd_ht100to200",
    id=31002,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht200to300 = qcd.add_process(
    name="qcd_ht200to300",
    id=31003,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht300to500 = qcd.add_process(
    name="qcd_ht300to500",
    id=31004,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht500to700 = qcd.add_process(
    name="qcd_ht500to700",
    id=31005,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht700to1000 = qcd.add_process(
    name="qcd_ht700to1000",
    id=31006,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht1000to1500 = qcd.add_process(
    name="qcd_ht1000to1500",
    id=31007,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht1500to2000 = qcd.add_process(
    name="qcd_ht1500to2000",
    id=31008,
    xsecs={13: Number(0.1)},  # TODO
)

qcd_ht2000 = qcd.add_process(
    name="qcd_ht2000",
    id=31090,
    xsecs={13: Number(0.1)},  # TODO
)
