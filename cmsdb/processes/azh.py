# coding: utf-8

"""
azh resonance search signal process definitions
"""

__all__ = [
    "azh",
    "azh_htt_zll",
    "azh_htt_zll_a1000_h330",
    "azh_htt_zll_a1000_h350",
    "azh_htt_zll_a1000_h400",
    "azh_htt_zll_a1000_h450",
    "azh_htt_zll_a1000_h500",
    "azh_htt_zll_a1000_h550",
    "azh_htt_zll_a1000_h600",
    "azh_htt_zll_a1000_h650",
    "azh_htt_zll_a1000_h700",
    "azh_htt_zll_a1000_h750",
    "azh_htt_zll_a1000_h800",
    "azh_htt_zll_a1000_h850",
    "azh_htt_zll_a1000_h900",
    "azh_htt_zll_a1050_h330",
    "azh_htt_zll_a1050_h350",
    "azh_htt_zll_a1050_h400",
    "azh_htt_zll_a1050_h450",
    "azh_htt_zll_a1050_h500",
    "azh_htt_zll_a1050_h550",
    "azh_htt_zll_a1050_h600",
    "azh_htt_zll_a1050_h650",
    "azh_htt_zll_a1050_h700",
    "azh_htt_zll_a1050_h750",
    "azh_htt_zll_a1050_h800",
    "azh_htt_zll_a1050_h850",
    "azh_htt_zll_a1050_h900",
    "azh_htt_zll_a1050_h950",
    "azh_htt_zll_a1100_h1000",
    "azh_htt_zll_a1100_h330",
    "azh_htt_zll_a1100_h350",
    "azh_htt_zll_a1100_h400",
    "azh_htt_zll_a1100_h450",
    "azh_htt_zll_a1100_h500",
    "azh_htt_zll_a1100_h550",
    "azh_htt_zll_a1100_h600",
    "azh_htt_zll_a1100_h650",
    "azh_htt_zll_a1100_h700",
    "azh_htt_zll_a1100_h750",
    "azh_htt_zll_a1100_h800",
    "azh_htt_zll_a1100_h850",
    "azh_htt_zll_a1100_h900",
    "azh_htt_zll_a1100_h950",
    "azh_htt_zll_a1150_h1050",
    "azh_htt_zll_a1150_h330",
    "azh_htt_zll_a1150_h350",
    "azh_htt_zll_a1150_h400",
    "azh_htt_zll_a1150_h450",
    "azh_htt_zll_a1150_h500",
    "azh_htt_zll_a1150_h550",
    "azh_htt_zll_a1150_h600",
    "azh_htt_zll_a1150_h650",
    "azh_htt_zll_a1150_h700",
    "azh_htt_zll_a1150_h750",
    "azh_htt_zll_a1150_h800",
    "azh_htt_zll_a1150_h850",
    "azh_htt_zll_a1150_h900",
    "azh_htt_zll_a1150_h950",
    "azh_htt_zll_a1150_h1000",
    "azh_htt_zll_a1200_h1000",
    "azh_htt_zll_a1200_h1050",
    "azh_htt_zll_a1200_h1100",
    "azh_htt_zll_a1200_h330",
    "azh_htt_zll_a1200_h350",
    "azh_htt_zll_a1200_h400",
    "azh_htt_zll_a1200_h450",
    "azh_htt_zll_a1200_h500",
    "azh_htt_zll_a1200_h550",
    "azh_htt_zll_a1200_h600",
    "azh_htt_zll_a1200_h650",
    "azh_htt_zll_a1200_h700",
    "azh_htt_zll_a1200_h750",
    "azh_htt_zll_a1200_h800",
    "azh_htt_zll_a1200_h850",
    "azh_htt_zll_a1200_h900",
    "azh_htt_zll_a1200_h950",
    "azh_htt_zll_a1250_h330",
    "azh_htt_zll_a1250_h350",
    "azh_htt_zll_a1250_h400",
    "azh_htt_zll_a1250_h450",
    "azh_htt_zll_a1250_h500",
    "azh_htt_zll_a1250_h550",
    "azh_htt_zll_a1250_h600",
    "azh_htt_zll_a1250_h650",
    "azh_htt_zll_a1250_h700",
    "azh_htt_zll_a1250_h750",
    "azh_htt_zll_a1250_h800",
    "azh_htt_zll_a1250_h850",
    "azh_htt_zll_a1250_h900",
    "azh_htt_zll_a1250_h950",
    "azh_htt_zll_a1250_h1000",
    "azh_htt_zll_a1250_h1050",
    "azh_htt_zll_a1250_h1100",
    "azh_htt_zll_a1250_h1150",
    "azh_htt_zll_a1250_h1000",
    "azh_htt_zll_a1300_h1000",
    "azh_htt_zll_a1300_h1100",
    "azh_htt_zll_a1300_h1200",
    "azh_htt_zll_a1300_h350",
    "azh_htt_zll_a1300_h400",
    "azh_htt_zll_a1300_h500",
    "azh_htt_zll_a1300_h600",
    "azh_htt_zll_a1300_h700",
    "azh_htt_zll_a1300_h800",
    "azh_htt_zll_a1300_h900",
    "azh_htt_zll_a1400_h1000",
    "azh_htt_zll_a1400_h1100",
    "azh_htt_zll_a1400_h1200",
    "azh_htt_zll_a1400_h1300",
    "azh_htt_zll_a1400_h350",
    "azh_htt_zll_a1400_h400",
    "azh_htt_zll_a1400_h500",
    "azh_htt_zll_a1400_h600",
    "azh_htt_zll_a1400_h700",
    "azh_htt_zll_a1400_h800",
    "azh_htt_zll_a1400_h900",
    "azh_htt_zll_a1500_h1000",
    "azh_htt_zll_a1500_h1100",
    "azh_htt_zll_a1500_h1200",
    "azh_htt_zll_a1500_h1300",
    "azh_htt_zll_a1500_h1400",
    "azh_htt_zll_a1500_h350",
    "azh_htt_zll_a1500_h400",
    "azh_htt_zll_a1500_h500",
    "azh_htt_zll_a1500_h600",
    "azh_htt_zll_a1500_h700",
    "azh_htt_zll_a1500_h800",
    "azh_htt_zll_a1500_h900",
    "azh_htt_zll_a1600_h1000",
    "azh_htt_zll_a1600_h1100",
    "azh_htt_zll_a1600_h1200",
    "azh_htt_zll_a1600_h1300",
    "azh_htt_zll_a1600_h1400",
    "azh_htt_zll_a1600_h1500",
    "azh_htt_zll_a1600_h350",
    "azh_htt_zll_a1600_h400",
    "azh_htt_zll_a1600_h500",
    "azh_htt_zll_a1600_h600",
    "azh_htt_zll_a1600_h700",
    "azh_htt_zll_a1600_h800",
    "azh_htt_zll_a1600_h900",
    "azh_htt_zll_a1700_h1000",
    "azh_htt_zll_a1700_h1100",
    "azh_htt_zll_a1700_h1200",
    "azh_htt_zll_a1700_h1300",
    "azh_htt_zll_a1700_h1400",
    "azh_htt_zll_a1700_h1500",
    "azh_htt_zll_a1700_h1600",
    "azh_htt_zll_a1700_h350",
    "azh_htt_zll_a1700_h400",
    "azh_htt_zll_a1700_h500",
    "azh_htt_zll_a1700_h600",
    "azh_htt_zll_a1700_h700",
    "azh_htt_zll_a1700_h800",
    "azh_htt_zll_a1700_h900",
    "azh_htt_zll_a1800_h1000",
    "azh_htt_zll_a1800_h1100",
    "azh_htt_zll_a1800_h1200",
    "azh_htt_zll_a1800_h1300",
    "azh_htt_zll_a1800_h1400",
    "azh_htt_zll_a1800_h1500",
    "azh_htt_zll_a1800_h1600",
    "azh_htt_zll_a1800_h1700",
    "azh_htt_zll_a1800_h350",
    "azh_htt_zll_a1800_h400",
    "azh_htt_zll_a1800_h500",
    "azh_htt_zll_a1800_h600",
    "azh_htt_zll_a1800_h700",
    "azh_htt_zll_a1800_h800",
    "azh_htt_zll_a1800_h900",
    "azh_htt_zll_a1900_h1000",
    "azh_htt_zll_a1900_h1100",
    "azh_htt_zll_a1900_h1200",
    "azh_htt_zll_a1900_h1300",
    "azh_htt_zll_a1900_h1400",
    "azh_htt_zll_a1900_h1500",
    "azh_htt_zll_a1900_h1600",
    "azh_htt_zll_a1900_h1700",
    "azh_htt_zll_a1900_h1800",
    "azh_htt_zll_a1900_h350",
    "azh_htt_zll_a1900_h400",
    "azh_htt_zll_a1900_h500",
    "azh_htt_zll_a1900_h600",
    "azh_htt_zll_a1900_h700",
    "azh_htt_zll_a1900_h800",
    "azh_htt_zll_a1900_h900",
    "azh_htt_zll_a2000_h1000",
    "azh_htt_zll_a2000_h1100",
    "azh_htt_zll_a2000_h1200",
    "azh_htt_zll_a2000_h1300",
    "azh_htt_zll_a2000_h1400",
    "azh_htt_zll_a2000_h1500",
    "azh_htt_zll_a2000_h1600",
    "azh_htt_zll_a2000_h1700",
    "azh_htt_zll_a2000_h1800",
    "azh_htt_zll_a2000_h1900",
    "azh_htt_zll_a2000_h350",
    "azh_htt_zll_a2000_h400",
    "azh_htt_zll_a2000_h500",
    "azh_htt_zll_a2000_h600",
    "azh_htt_zll_a2000_h700",
    "azh_htt_zll_a2000_h800",
    "azh_htt_zll_a2000_h900",
    "azh_htt_zll_a2100_h1000",
    "azh_htt_zll_a2100_h1100",
    "azh_htt_zll_a2100_h1200",
    "azh_htt_zll_a2100_h1300",
    "azh_htt_zll_a2100_h1400",
    "azh_htt_zll_a2100_h1500",
    "azh_htt_zll_a2100_h1600",
    "azh_htt_zll_a2100_h1700",
    "azh_htt_zll_a2100_h1800",
    "azh_htt_zll_a2100_h1900",
    "azh_htt_zll_a2100_h2000",
    "azh_htt_zll_a2100_h350",
    "azh_htt_zll_a2100_h400",
    "azh_htt_zll_a2100_h500",
    "azh_htt_zll_a2100_h600",
    "azh_htt_zll_a2100_h700",
    "azh_htt_zll_a2100_h800",
    "azh_htt_zll_a2100_h900",
    "azh_htt_zll_a430_h330",
    "azh_htt_zll_a450_h330",
    "azh_htt_zll_a450_h350",
    "azh_htt_zll_a500_h330",
    "azh_htt_zll_a500_h350",
    "azh_htt_zll_a500_h370",
    "azh_htt_zll_a500_h400",
    "azh_htt_zll_a550_h330",
    "azh_htt_zll_a550_h350",
    "azh_htt_zll_a550_h400",
    "azh_htt_zll_a550_h450",
    "azh_htt_zll_a600_h330",
    "azh_htt_zll_a600_h350",
    "azh_htt_zll_a600_h400",
    "azh_htt_zll_a600_h450",
    "azh_htt_zll_a600_h500",
    "azh_htt_zll_a650_h330",
    "azh_htt_zll_a650_h350",
    "azh_htt_zll_a650_h400",
    "azh_htt_zll_a650_h450",
    "azh_htt_zll_a650_h500",
    "azh_htt_zll_a650_h550",
    "azh_htt_zll_a700_h330",
    "azh_htt_zll_a700_h350",
    "azh_htt_zll_a700_h370",
    "azh_htt_zll_a700_h400",
    "azh_htt_zll_a700_h450",
    "azh_htt_zll_a700_h500",
    "azh_htt_zll_a700_h550",
    "azh_htt_zll_a700_h600",
    "azh_htt_zll_a750_h330",
    "azh_htt_zll_a750_h350",
    "azh_htt_zll_a750_h400",
    "azh_htt_zll_a750_h450",
    "azh_htt_zll_a750_h500",
    "azh_htt_zll_a750_h550",
    "azh_htt_zll_a750_h600",
    "azh_htt_zll_a750_h650",
    "azh_htt_zll_a800_h330",
    "azh_htt_zll_a800_h350",
    "azh_htt_zll_a800_h400",
    "azh_htt_zll_a800_h450",
    "azh_htt_zll_a800_h500",
    "azh_htt_zll_a800_h550",
    "azh_htt_zll_a800_h600",
    "azh_htt_zll_a800_h650",
    "azh_htt_zll_a800_h700",
    "azh_htt_zll_a850_h330",
    "azh_htt_zll_a850_h350",
    "azh_htt_zll_a850_h400",
    "azh_htt_zll_a850_h450",
    "azh_htt_zll_a850_h500",
    "azh_htt_zll_a850_h550",
    "azh_htt_zll_a850_h600",
    "azh_htt_zll_a850_h650",
    "azh_htt_zll_a850_h700",
    "azh_htt_zll_a850_h750",
    "azh_htt_zll_a900_h330",
    "azh_htt_zll_a900_h350",
    "azh_htt_zll_a900_h370",
    "azh_htt_zll_a900_h400",
    "azh_htt_zll_a900_h450",
    "azh_htt_zll_a900_h550",
    "azh_htt_zll_a900_h500",
    "azh_htt_zll_a900_h600",
    "azh_htt_zll_a900_h650",
    "azh_htt_zll_a900_h700",
    "azh_htt_zll_a900_h750",
    "azh_htt_zll_a900_h800",
    "azh_htt_zll_a950_h330",
    "azh_htt_zll_a950_h350",
    "azh_htt_zll_a950_h400",
    "azh_htt_zll_a950_h450",
    "azh_htt_zll_a950_h500",
    "azh_htt_zll_a950_h550",
    "azh_htt_zll_a950_h600",
    "azh_htt_zll_a950_h650",
    "azh_htt_zll_a950_h700",
    "azh_htt_zll_a950_h750",
    "azh_htt_zll_a950_h800",
    "azh_htt_zll_a950_h850",
]

from order import Process
from scinum import Number


azh = Process(
    name="azh",
    label=r"AtoZH",
    id=1000000,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

#
# A->ZH->lltt
#

azh_htt_zll = azh.add_process(
    name="azh_htt_zll",
    label=azh.label,
    id=1000001,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 330$ GeV)",
    id=1000002,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 350$ GeV)",
    id=1000003,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 400$ GeV)",
    id=1000004,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 450$ GeV)",
    id=1000005,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 500$ GeV)",
    id=1000006,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 550$ GeV)",
    id=1000007,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 600$ GeV)",
    id=1000008,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 650$ GeV)",
    id=1000009,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 700$ GeV)",
    id=1000010,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 750$ GeV)",
    id=1000011,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 800$ GeV)",
    id=1000012,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 850$ GeV)",
    id=1000013,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 900$ GeV)",
    id=1000014,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 330$ GeV)",
    id=1000015,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 350$ GeV)",
    id=1000016,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 400$ GeV)",
    id=1000017,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 450$ GeV)",
    id=1000018,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 500$ GeV)",
    id=1000019,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 550$ GeV)",
    id=1000020,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 600$ GeV)",
    id=1000021,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 650$ GeV)",
    id=1000264,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 700$ GeV)",
    id=1000022,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 750$ GeV)",
    id=1000023,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 800$ GeV)",
    id=1000024,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 850$ GeV)",
    id=1000025,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 900$ GeV)",
    id=1000026,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1050_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 950$ GeV)",
    id=1000027,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 1000$ GeV)",
    id=1000028,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 330$ GeV)",
    id=1000029,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 350$ GeV)",
    id=1000030,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 400$ GeV)",
    id=1000031,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 450$ GeV)",
    id=1000032,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 500$ GeV)",
    id=1000033,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 550$ GeV)",
    id=1000034,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 600$ GeV)",
    id=1000035,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 650$ GeV)",
    id=1000036,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 700$ GeV)",
    id=1000037,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 750$ GeV)",
    id=1000038,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 800$ GeV)",
    id=1000039,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 850$ GeV)",
    id=1000040,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 900$ GeV)",
    id=1000041,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1100_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 950$ GeV)",
    id=1000042,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1050$ GeV)",
    id=1000043,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 330$ GeV)",
    id=1000044,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 350$ GeV)",
    id=1000045,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 400$ GeV)",
    id=1000266,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 450$ GeV)",
    id=1000046,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 500$ GeV)",
    id=1000267,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 550$ GeV)",
    id=1000047,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 600$ GeV)",
    id=1000268,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 650$ GeV)",
    id=1000048,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 700$ GeV)",
    id=1000269,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 750$ GeV)",
    id=1000049,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 800$ GeV)",
    id=1000270,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 850$ GeV)",
    id=1000050,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 900$ GeV)",
    id=1000271,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 950$ GeV)",
    id=1000051,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1150_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1000$ GeV)",
    id=1000272,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1000$ GeV)",
    id=1000052,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1050$ GeV)",
    id=1000273,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1100$ GeV)",
    id=1000053,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 330$ GeV)",
    id=1000054,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 350$ GeV)",
    id=1000055,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 400$ GeV)",
    id=1000056,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 450$ GeV)",
    id=1000274,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 500$ GeV)",
    id=1000057,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 550$ GeV)",
    id=1000275,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 600$ GeV)",
    id=1000058,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 650$ GeV)",
    id=1000276,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 700$ GeV)",
    id=1000059,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 750$ GeV)",
    id=1000277,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 800$ GeV)",
    id=1000060,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 850$ GeV)",
    id=1000061,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 900$ GeV)",
    id=1000062,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1200_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 950$ GeV)",
    id=1000278,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 330$ GeV)",
    id=1000283,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 350$ GeV)",
    id=1000284,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 400$ GeV)",
    id=1000285,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 450$ GeV)",
    id=1000286,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 500$ GeV)",
    id=1000287,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 550$ GeV)",
    id=1000288,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 600$ GeV)",
    id=1000289,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 650$ GeV)",
    id=1000290,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 700$ GeV)",
    id=1000291,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 750$ GeV)",
    id=1000292,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 800$ GeV)",
    id=1000293,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 850$ GeV)",
    id=1000294,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 900$ GeV)",
    id=1000295,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 950$ GeV)",
    id=1000296,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1000$ GeV)",
    id=1000279,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1050$ GeV)",
    id=1000280,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1100$ GeV)",
    id=1000281,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1250_h1150 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1150",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1150$ GeV)",
    id=1000282,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1000$ GeV)",
    id=1000063,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1100$ GeV)",
    id=1000064,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1200$ GeV)",
    id=1000065,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 350$ GeV)",
    id=1000066,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 400$ GeV)",
    id=1000067,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 500$ GeV)",
    id=1000068,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 600$ GeV)",
    id=1000069,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 700$ GeV)",
    id=1000070,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 800$ GeV)",
    id=1000071,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1300_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 900$ GeV)",
    id=1000072,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1000$ GeV)",
    id=1000073,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1100$ GeV)",
    id=1000074,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1200$ GeV)",
    id=1000075,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1300$ GeV)",
    id=1000076,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 350$ GeV)",
    id=1000077,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 400$ GeV)",
    id=1000078,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 500$ GeV)",
    id=1000079,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 600$ GeV)",
    id=1000080,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 700$ GeV)",
    id=1000081,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 800$ GeV)",
    id=1000082,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1400_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 900$ GeV)",
    id=1000083,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1000$ GeV)",
    id=1000084,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1100$ GeV)",
    id=1000085,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1200$ GeV)",
    id=1000086,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1300$ GeV)",
    id=1000087,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1400$ GeV)",
    id=1000088,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 350$ GeV)",
    id=1000089,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 400$ GeV)",
    id=1000090,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 500$ GeV)",
    id=1000091,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 600$ GeV)",
    id=1000092,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 700$ GeV)",
    id=1000093,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 800$ GeV)",
    id=1000297,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1500_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 900$ GeV)",
    id=1000094,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1000$ GeV)",
    id=1000095,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1100$ GeV)",
    id=1000096,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1200$ GeV)",
    id=1000097,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1300$ GeV)",
    id=1000098,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1400$ GeV)",
    id=1000099,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1500$ GeV)",
    id=1000100,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 350$ GeV)",
    id=1000101,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 400$ GeV)",
    id=1000102,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 500$ GeV)",
    id=1000103,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 600$ GeV)",
    id=1000104,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 700$ GeV)",
    id=1000298,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 800$ GeV)",
    id=1000299,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1600_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 900$ GeV)",
    id=1000105,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1000$ GeV)",
    id=1000106,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1100$ GeV)",
    id=1000107,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1200$ GeV)",
    id=1000108,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1300$ GeV)",
    id=1000109,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1400$ GeV)",
    id=1000110,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1500$ GeV)",
    id=1000111,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1600$ GeV)",
    id=1000112,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 350$ GeV)",
    id=1000113,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 400$ GeV)",
    id=1000114,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 500$ GeV)",
    id=1000115,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 600$ GeV)",
    id=1000116,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 700$ GeV)",
    id=1000117,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 800$ GeV)",
    id=1000118,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1700_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 900$ GeV)",
    id=1000119,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1000$ GeV)",
    id=1000120,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1100$ GeV)",
    id=1000121,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1200$ GeV)",
    id=1000122,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1300$ GeV)",
    id=1000123,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1400$ GeV)",
    id=1000124,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1500$ GeV)",
    id=1000125,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1600$ GeV)",
    id=1000126,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1700$ GeV)",
    id=1000127,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 350$ GeV)",
    id=1000128,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 400$ GeV)",
    id=1000129,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 500$ GeV)",
    id=1000130,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 600$ GeV)",
    id=1000131,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 700$ GeV)",
    id=1000132,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 800$ GeV)",
    id=1000133,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1800_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 900$ GeV)",
    id=1000134,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1000$ GeV)",
    id=1000135,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1100$ GeV)",
    id=1000136,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1200$ GeV)",
    id=1000137,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1300$ GeV)",
    id=1000138,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1400$ GeV)",
    id=1000139,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1500$ GeV)",
    id=1000140,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1600$ GeV)",
    id=1000141,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1700$ GeV)",
    id=1000142,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1800$ GeV)",
    id=1000143,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 350$ GeV)",
    id=1000144,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 400$ GeV)",
    id=1000145,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 500$ GeV)",
    id=1000146,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 600$ GeV)",
    id=1000147,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 700$ GeV)",
    id=1000148,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 800$ GeV)",
    id=1000149,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a1900_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 900$ GeV)",
    id=1000150,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1000$ GeV)",
    id=1000151,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1100$ GeV)",
    id=1000152,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1200$ GeV)",
    id=1000153,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1300$ GeV)",
    id=1000154,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1400$ GeV)",
    id=1000155,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1500$ GeV)",
    id=1000300,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1600$ GeV)",
    id=1000156,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1700$ GeV)",
    id=1000157,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1800$ GeV)",
    id=1000158,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1900$ GeV)",
    id=1000159,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 350$ GeV)",
    id=1000160,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 400$ GeV)",
    id=1000161,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 500$ GeV)",
    id=1000162,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 600$ GeV)",
    id=1000163,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 700$ GeV)",
    id=1000164,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 800$ GeV)",
    id=1000165,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 900$ GeV)",
    id=1000166,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1000$ GeV)",
    id=1000167,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1100$ GeV)",
    id=1000168,
    xsecs={
        13: Number(0.1),
    },  13.6: Number(1),
)
azh_htt_zll_a2100_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1200$ GeV)",
    id=1000169,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1300$ GeV)",
    id=1000170,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1400$ GeV)",
    id=1000171,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1500$ GeV)",
    id=1000172,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1600$ GeV)",
    id=1000301,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1700$ GeV)",
    id=1000173,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1800$ GeV)",
    id=1000174,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1900$ GeV)",
    id=1000175,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h2000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h2000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 2000$ GeV)",
    id=1000176,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 350$ GeV)",
    id=1000177,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 400$ GeV)",
    id=1000178,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 500$ GeV)",
    id=1000179,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 600$ GeV)",
    id=1000180,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 700$ GeV)",
    id=1000181,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 800$ GeV)",
    id=1000182,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a2100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 900$ GeV)",
    id=1000183,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a430_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a430_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 430$ GeV, $m_H = 330$ GeV)",
    id=1000184,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a450_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 330$ GeV)",
    id=1000185,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a450_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 350$ GeV)",
    id=1000186,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a500_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 330$ GeV)",
    id=1000187,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 350$ GeV)",
    id=1000188,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a500_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 370$ GeV)",
    id=1000189,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 400$ GeV)",
    id=1000190,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a550_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 330$ GeV)",
    id=1000191,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a550_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 350$ GeV)",
    id=1000192,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a550_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 400$ GeV)",
    id=1000193,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a550_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 450$ GeV)",
    id=1000194,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a600_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 330$ GeV)",
    id=1000195,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 350$ GeV)",
    id=1000196,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 400$ GeV)",
    id=1000197,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a600_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 450$ GeV)",
    id=1000198,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 500$ GeV)",
    id=1000199,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 330$ GeV)",
    id=1000200,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 350$ GeV)",
    id=1000201,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 400$ GeV)",
    id=1000202,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 450$ GeV)",
    id=1000203,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 500$ GeV)",
    id=1000204,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a650_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 550$ GeV)",
    id=1000205,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 330$ GeV)",
    id=1000206,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 350$ GeV)",
    id=1000207,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 370$ GeV)",
    id=1000208,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 400$ GeV)",
    id=1000209,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 450$ GeV)",
    id=1000210,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 500$ GeV)",
    id=1000211,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 550$ GeV)",
    id=1000212,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 600$ GeV)",
    id=1000302,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 330$ GeV)",
    id=1000213,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 350$ GeV)",
    id=1000214,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 400$ GeV)",
    id=1000215,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 450$ GeV)",
    id=1000216,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 500$ GeV)",
    id=1000217,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 550$ GeV)",
    id=1000218,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 600$ GeV)",
    id=1000219,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a750_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 650$ GeV)",
    id=1000220,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 330$ GeV)",
    id=1000221,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 350$ GeV)",
    id=1000222,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 400$ GeV)",
    id=1000223,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 450$ GeV)",
    id=1000224,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 500$ GeV)",
    id=1000225,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 550$ GeV)",
    id=1000226,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 600$ GeV)",
    id=1000227,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 650$ GeV)",
    id=1000228,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 700$ GeV)",
    id=1000229,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 330$ GeV)",
    id=1000230,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 350$ GeV)",
    id=1000231,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 400$ GeV)",
    id=1000232,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 450$ GeV)",
    id=1000233,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 500$ GeV)",
    id=1000234,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 550$ GeV)",
    id=1000235,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 600$ GeV)",
    id=1000236,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 650$ GeV)",
    id=1000237,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 700$ GeV)",
    id=1000238,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a850_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 750$ GeV)",
    id=1000239,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 330$ GeV)",
    id=1000240,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 350$ GeV)",
    id=1000241,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 370$ GeV)",
    id=1000242,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 400$ GeV)",
    id=1000243,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 450$ GeV)",
    id=1000244,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 550$ GeV)",
    id=1000245,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 500$ GeV)",
    id=1000246,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 600$ GeV)",
    id=1000247,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 650$ GeV)",
    id=1000248,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 700$ GeV)",
    id=1000249,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 750$ GeV)",
    id=1000250,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 800$ GeV)",
    id=1000251,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 330$ GeV)",
    id=1000252,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 350$ GeV)",
    id=1000253,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 400$ GeV)",
    id=1000254,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 450$ GeV)",
    id=1000255,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 500$ GeV)",
    id=1000256,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 550$ GeV)",
    id=1000257,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 600$ GeV)",
    id=1000258,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 650$ GeV)",
    id=1000259,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 700$ GeV)",
    id=1000260,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 750$ GeV)",
    id=1000261,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 800$ GeV)",
    id=1000262,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)

azh_htt_zll_a950_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 850$ GeV)",
    id=1000263,
    xsecs={
        13: Number(1),
        13.6: Number(1),
    },
)
