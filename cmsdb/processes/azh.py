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
# TODO Calculate xsec
)

#
# A->ZH->lltt
#

azh_htt_zll = azh.add_process(
    name="azh_htt_zll",
    label=azh.label,
    id=1000001,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 330$ GeV)",
    id=1000002,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 350$ GeV)",
    id=1000003,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 400$ GeV)",
    id=1000004,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 450$ GeV)",
    id=1000005,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 500$ GeV)",
    id=1000006,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 550$ GeV)",
    id=1000007,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 600$ GeV)",
    id=1000008,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 650$ GeV)",
    id=1000009,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 700$ GeV)",
    id=1000010,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 750$ GeV)",
    id=1000011,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 800$ GeV)",
    id=1000012,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 850$ GeV)",
    id=1000013,
    # TODO Calculate xsec
)

azh_htt_zll_a1000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 900$ GeV)",
    id=1000014,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 330$ GeV)",
    id=1000015,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 350$ GeV)",
    id=1000016,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 400$ GeV)",
    id=1000017,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 450$ GeV)",
    id=1000018,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 500$ GeV)",
    id=1000019,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 550$ GeV)",
    id=1000020,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 600$ GeV)",
    id=1000021,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 650$ GeV)",
    id=1000264,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 700$ GeV)",
    id=1000022,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 750$ GeV)",
    id=1000023,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 800$ GeV)",
    id=1000024,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 850$ GeV)",
    id=1000025,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 900$ GeV)",
    id=1000026,
    # TODO Calculate xsec
)

azh_htt_zll_a1050_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 950$ GeV)",
    id=1000027,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 1000$ GeV)",
    id=1000028,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 330$ GeV)",
    id=1000029,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 350$ GeV)",
    id=1000030,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 400$ GeV)",
    id=1000031,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 450$ GeV)",
    id=1000032,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 500$ GeV)",
    id=1000033,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 550$ GeV)",
    id=1000034,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 600$ GeV)",
    id=1000035,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 650$ GeV)",
    id=1000036,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 700$ GeV)",
    id=1000037,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 750$ GeV)",
    id=1000038,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 800$ GeV)",
    id=1000039,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 850$ GeV)",
    id=1000040,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 900$ GeV)",
    id=1000041,
    # TODO Calculate xsec
)

azh_htt_zll_a1100_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 950$ GeV)",
    id=1000042,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1050$ GeV)",
    id=1000043,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 330$ GeV)",
    id=1000044,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 350$ GeV)",
    id=1000045,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 400$ GeV)",
    id=1000266,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 450$ GeV)",
    id=1000046,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 500$ GeV)",
    id=1000267,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 550$ GeV)",
    id=1000047,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 600$ GeV)",
    id=1000268,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 650$ GeV)",
    id=1000048,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 700$ GeV)",
    id=1000269,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 750$ GeV)",
    id=1000049,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 800$ GeV)",
    id=1000270,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 850$ GeV)",
    id=1000050,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 900$ GeV)",
    id=1000271,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 950$ GeV)",
    id=1000051,
    # TODO Calculate xsec
)

azh_htt_zll_a1150_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1000$ GeV)",
    id=1000272,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1000$ GeV)",
    id=1000052,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1050$ GeV)",
    id=1000273,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1100$ GeV)",
    id=1000053,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 330$ GeV)",
    id=1000054,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 350$ GeV)",
    id=1000055,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 400$ GeV)",
    id=1000056,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 450$ GeV)",
    id=1000274,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 500$ GeV)",
    id=1000057,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 550$ GeV)",
    id=1000275,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 600$ GeV)",
    id=1000058,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 650$ GeV)",
    id=1000276,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 700$ GeV)",
    id=1000059,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 750$ GeV)",
    id=1000277,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 800$ GeV)",
    id=1000060,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 850$ GeV)",
    id=1000061,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 900$ GeV)",
    id=1000062,
    # TODO Calculate xsec
)

azh_htt_zll_a1200_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 950$ GeV)",
    id=1000278,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 330$ GeV)",
    id=1000283,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 350$ GeV)",
    id=1000284,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 400$ GeV)",
    id=1000285,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 450$ GeV)",
    id=1000286,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 500$ GeV)",
    id=1000287,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 550$ GeV)",
    id=1000288,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 600$ GeV)",
    id=1000289,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 650$ GeV)",
    id=1000290,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 700$ GeV)",
    id=1000291,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 750$ GeV)",
    id=1000292,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 800$ GeV)",
    id=1000293,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 850$ GeV)",
    id=1000294,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 900$ GeV)",
    id=1000295,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 950$ GeV)",
    id=1000296,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1000$ GeV)",
    id=1000279,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1050$ GeV)",
    id=1000280,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1100$ GeV)",
    id=1000281,
    # TODO Calculate xsec
)

azh_htt_zll_a1250_h1150 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1250_h1150",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1250$ GeV, $m_H = 1150$ GeV)",
    id=1000282,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1000$ GeV)",
    id=1000063,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1100$ GeV)",
    id=1000064,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1200$ GeV)",
    id=1000065,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 350$ GeV)",
    id=1000066,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 400$ GeV)",
    id=1000067,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 500$ GeV)",
    id=1000068,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 600$ GeV)",
    id=1000069,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 700$ GeV)",
    id=1000070,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 800$ GeV)",
    id=1000071,
    # TODO Calculate xsec
)

azh_htt_zll_a1300_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 900$ GeV)",
    id=1000072,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1000$ GeV)",
    id=1000073,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1100$ GeV)",
    id=1000074,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1200$ GeV)",
    id=1000075,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1300$ GeV)",
    id=1000076,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 350$ GeV)",
    id=1000077,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 400$ GeV)",
    id=1000078,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 500$ GeV)",
    id=1000079,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 600$ GeV)",
    id=1000080,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 700$ GeV)",
    id=1000081,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 800$ GeV)",
    id=1000082,
    # TODO Calculate xsec
)

azh_htt_zll_a1400_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 900$ GeV)",
    id=1000083,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1000$ GeV)",
    id=1000084,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1100$ GeV)",
    id=1000085,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1200$ GeV)",
    id=1000086,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1300$ GeV)",
    id=1000087,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1400$ GeV)",
    id=1000088,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 350$ GeV)",
    id=1000089,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 400$ GeV)",
    id=1000090,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 500$ GeV)",
    id=1000091,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 600$ GeV)",
    id=1000092,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 700$ GeV)",
    id=1000093,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 800$ GeV)",
    id=1000297,
    # TODO Calculate xsec
)

azh_htt_zll_a1500_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 900$ GeV)",
    id=1000094,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1000$ GeV)",
    id=1000095,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1100$ GeV)",
    id=1000096,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1200$ GeV)",
    id=1000097,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1300$ GeV)",
    id=1000098,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1400$ GeV)",
    id=1000099,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1500$ GeV)",
    id=1000100,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 350$ GeV)",
    id=1000101,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 400$ GeV)",
    id=1000102,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 500$ GeV)",
    id=1000103,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 600$ GeV)",
    id=1000104,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 700$ GeV)",
    id=1000298,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 800$ GeV)",
    id=1000299,
    # TODO Calculate xsec
)

azh_htt_zll_a1600_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 900$ GeV)",
    id=1000105,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1000$ GeV)",
    id=1000106,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1100$ GeV)",
    id=1000107,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1200$ GeV)",
    id=1000108,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1300$ GeV)",
    id=1000109,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1400$ GeV)",
    id=1000110,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1500$ GeV)",
    id=1000111,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1600$ GeV)",
    id=1000112,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 350$ GeV)",
    id=1000113,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 400$ GeV)",
    id=1000114,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 500$ GeV)",
    id=1000115,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 600$ GeV)",
    id=1000116,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 700$ GeV)",
    id=1000117,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 800$ GeV)",
    id=1000118,
    # TODO Calculate xsec
)

azh_htt_zll_a1700_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 900$ GeV)",
    id=1000119,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1000$ GeV)",
    id=1000120,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1100$ GeV)",
    id=1000121,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1200$ GeV)",
    id=1000122,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1300$ GeV)",
    id=1000123,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1400$ GeV)",
    id=1000124,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1500$ GeV)",
    id=1000125,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1600$ GeV)",
    id=1000126,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1700$ GeV)",
    id=1000127,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 350$ GeV)",
    id=1000128,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 400$ GeV)",
    id=1000129,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 500$ GeV)",
    id=1000130,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 600$ GeV)",
    id=1000131,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 700$ GeV)",
    id=1000132,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 800$ GeV)",
    id=1000133,
    # TODO Calculate xsec
)

azh_htt_zll_a1800_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 900$ GeV)",
    id=1000134,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1000$ GeV)",
    id=1000135,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1100$ GeV)",
    id=1000136,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1200$ GeV)",
    id=1000137,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1300$ GeV)",
    id=1000138,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1400$ GeV)",
    id=1000139,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1500$ GeV)",
    id=1000140,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1600$ GeV)",
    id=1000141,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1700$ GeV)",
    id=1000142,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1800$ GeV)",
    id=1000143,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 350$ GeV)",
    id=1000144,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 400$ GeV)",
    id=1000145,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 500$ GeV)",
    id=1000146,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 600$ GeV)",
    id=1000147,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 700$ GeV)",
    id=1000148,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 800$ GeV)",
    id=1000149,
    # TODO Calculate xsec
)

azh_htt_zll_a1900_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 900$ GeV)",
    id=1000150,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1000$ GeV)",
    id=1000151,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1100$ GeV)",
    id=1000152,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1200$ GeV)",
    id=1000153,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1300$ GeV)",
    id=1000154,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1400$ GeV)",
    id=1000155,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1500$ GeV)",
    id=1000300,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1600$ GeV)",
    id=1000156,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1700$ GeV)",
    id=1000157,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1800$ GeV)",
    id=1000158,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1900$ GeV)",
    id=1000159,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 350$ GeV)",
    id=1000160,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 400$ GeV)",
    id=1000161,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 500$ GeV)",
    id=1000162,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 600$ GeV)",
    id=1000163,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 700$ GeV)",
    id=1000164,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 800$ GeV)",
    id=1000165,
    # TODO Calculate xsec
)

azh_htt_zll_a2000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 900$ GeV)",
    id=1000166,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1000$ GeV)",
    id=1000167,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1100$ GeV)",
    id=1000168,
    xsecs={
        13: Number(0.1),
    },  # TODO
)
azh_htt_zll_a2100_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1200$ GeV)",
    id=1000169,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1300$ GeV)",
    id=1000170,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1400$ GeV)",
    id=1000171,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1500$ GeV)",
    id=1000172,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1600$ GeV)",
    id=1000301,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1700$ GeV)",
    id=1000173,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1800$ GeV)",
    id=1000174,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1900$ GeV)",
    id=1000175,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h2000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h2000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 2000$ GeV)",
    id=1000176,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 350$ GeV)",
    id=1000177,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 400$ GeV)",
    id=1000178,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 500$ GeV)",
    id=1000179,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 600$ GeV)",
    id=1000180,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 700$ GeV)",
    id=1000181,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 800$ GeV)",
    id=1000182,
    # TODO Calculate xsec
)

azh_htt_zll_a2100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 900$ GeV)",
    id=1000183,
    # TODO Calculate xsec
)

azh_htt_zll_a430_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a430_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 430$ GeV, $m_H = 330$ GeV)",
    id=1000184,
    # TODO Calculate xsec
)

azh_htt_zll_a450_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 330$ GeV)",
    id=1000185,
    # TODO Calculate xsec
)

azh_htt_zll_a450_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 350$ GeV)",
    id=1000186,
    # TODO Calculate xsec
)

azh_htt_zll_a500_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 330$ GeV)",
    id=1000187,
    # TODO Calculate xsec
)

azh_htt_zll_a500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 350$ GeV)",
    id=1000188,
    # TODO Calculate xsec
)

azh_htt_zll_a500_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 370$ GeV)",
    id=1000189,
    # TODO Calculate xsec
)

azh_htt_zll_a500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 400$ GeV)",
    id=1000190,
    # TODO Calculate xsec
)

azh_htt_zll_a550_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 330$ GeV)",
    id=1000191,
    # TODO Calculate xsec
)

azh_htt_zll_a550_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 350$ GeV)",
    id=1000192,
    # TODO Calculate xsec
)

azh_htt_zll_a550_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 400$ GeV)",
    id=1000193,
    # TODO Calculate xsec
)

azh_htt_zll_a550_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 450$ GeV)",
    id=1000194,
    # TODO Calculate xsec
)

azh_htt_zll_a600_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 330$ GeV)",
    id=1000195,
    # TODO Calculate xsec
)

azh_htt_zll_a600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 350$ GeV)",
    id=1000196,
    # TODO Calculate xsec
)

azh_htt_zll_a600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 400$ GeV)",
    id=1000197,
    # TODO Calculate xsec
)

azh_htt_zll_a600_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 450$ GeV)",
    id=1000198,
    # TODO Calculate xsec
)

azh_htt_zll_a600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 500$ GeV)",
    id=1000199,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 330$ GeV)",
    id=1000200,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 350$ GeV)",
    id=1000201,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 400$ GeV)",
    id=1000202,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 450$ GeV)",
    id=1000203,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 500$ GeV)",
    id=1000204,
    # TODO Calculate xsec
)

azh_htt_zll_a650_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 550$ GeV)",
    id=1000205,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 330$ GeV)",
    id=1000206,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 350$ GeV)",
    id=1000207,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 370$ GeV)",
    id=1000208,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 400$ GeV)",
    id=1000209,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 450$ GeV)",
    id=1000210,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 500$ GeV)",
    id=1000211,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 550$ GeV)",
    id=1000212,
    # TODO Calculate xsec
)

azh_htt_zll_a700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 600$ GeV)",
    id=1000302,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 330$ GeV)",
    id=1000213,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 350$ GeV)",
    id=1000214,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 400$ GeV)",
    id=1000215,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 450$ GeV)",
    id=1000216,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 500$ GeV)",
    id=1000217,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 550$ GeV)",
    id=1000218,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 600$ GeV)",
    id=1000219,
    # TODO Calculate xsec
)

azh_htt_zll_a750_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 650$ GeV)",
    id=1000220,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 330$ GeV)",
    id=1000221,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 350$ GeV)",
    id=1000222,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 400$ GeV)",
    id=1000223,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 450$ GeV)",
    id=1000224,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 500$ GeV)",
    id=1000225,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 550$ GeV)",
    id=1000226,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 600$ GeV)",
    id=1000227,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 650$ GeV)",
    id=1000228,
    # TODO Calculate xsec
)

azh_htt_zll_a800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 700$ GeV)",
    id=1000229,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 330$ GeV)",
    id=1000230,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 350$ GeV)",
    id=1000231,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 400$ GeV)",
    id=1000232,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 450$ GeV)",
    id=1000233,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 500$ GeV)",
    id=1000234,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 550$ GeV)",
    id=1000235,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 600$ GeV)",
    id=1000236,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 650$ GeV)",
    id=1000237,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 700$ GeV)",
    id=1000238,
    # TODO Calculate xsec
)

azh_htt_zll_a850_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 750$ GeV)",
    id=1000239,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 330$ GeV)",
    id=1000240,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 350$ GeV)",
    id=1000241,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 370$ GeV)",
    id=1000242,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 400$ GeV)",
    id=1000243,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 450$ GeV)",
    id=1000244,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 550$ GeV)",
    id=1000245,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 500$ GeV)",
    id=1000246,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 600$ GeV)",
    id=1000247,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 650$ GeV)",
    id=1000248,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 700$ GeV)",
    id=1000249,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 750$ GeV)",
    id=1000250,
    # TODO Calculate xsec
)

azh_htt_zll_a900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 800$ GeV)",
    id=1000251,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 330$ GeV)",
    id=1000252,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 350$ GeV)",
    id=1000253,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 400$ GeV)",
    id=1000254,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 450$ GeV)",
    id=1000255,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 500$ GeV)",
    id=1000256,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 550$ GeV)",
    id=1000257,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 600$ GeV)",
    id=1000258,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 650$ GeV)",
    id=1000259,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 700$ GeV)",
    id=1000260,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 750$ GeV)",
    id=1000261,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 800$ GeV)",
    id=1000262,
    # TODO Calculate xsec
)

azh_htt_zll_a950_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 850$ GeV)",
    id=1000263,
    # TODO Calculate xsec
)
