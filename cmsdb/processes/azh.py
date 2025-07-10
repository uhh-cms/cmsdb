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
    "azh_htt_zll_a1150_h450",
    "azh_htt_zll_a1150_h550",
    "azh_htt_zll_a1150_h650",
    "azh_htt_zll_a1150_h750",
    "azh_htt_zll_a1150_h850",
    "azh_htt_zll_a1150_h950",
    "azh_htt_zll_a1200_h1000",
    "azh_htt_zll_a1200_h1100",
    "azh_htt_zll_a1200_h330",
    "azh_htt_zll_a1200_h350",
    "azh_htt_zll_a1200_h400",
    "azh_htt_zll_a1200_h500",
    "azh_htt_zll_a1200_h600",
    "azh_htt_zll_a1200_h700",
    "azh_htt_zll_a1200_h800",
    "azh_htt_zll_a1200_h850",
    "azh_htt_zll_a1200_h900",
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


azh = Process(
    name="azh",
    label=r"AtoZH",
    id=1000000,
)

#
# A->ZH->lltt
#

azh_htt_zll = azh.add_process(
    name="azh_htt_zll",
    label=azh.label,
    id=1000001,
)

azh_htt_zll_a1000_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 330$ GeV)",
    id=1000002,
)

azh_htt_zll_a1000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 350$ GeV)",
    id=1000003,
)

azh_htt_zll_a1000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 400$ GeV)",
    id=1000004,
)

azh_htt_zll_a1000_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 450$ GeV)",
    id=1000005,
)

azh_htt_zll_a1000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 500$ GeV)",
    id=1000006,
)

azh_htt_zll_a1000_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 550$ GeV)",
    id=1000007,
)

azh_htt_zll_a1000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 600$ GeV)",
    id=1000008,
)

azh_htt_zll_a1000_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 650$ GeV)",
    id=1000009,
)

azh_htt_zll_a1000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 700$ GeV)",
    id=1000010,
)

azh_htt_zll_a1000_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 750$ GeV)",
    id=1000011,
)

azh_htt_zll_a1000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 800$ GeV)",
    id=1000012,
)

azh_htt_zll_a1000_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 850$ GeV)",
    id=1000013,
)

azh_htt_zll_a1000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1000$ GeV, $m_H = 900$ GeV)",
    id=1000014,
)

azh_htt_zll_a1050_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 330$ GeV)",
    id=1000015,
)

azh_htt_zll_a1050_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 350$ GeV)",
    id=1000016,
)

azh_htt_zll_a1050_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 400$ GeV)",
    id=1000017,
)

azh_htt_zll_a1050_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 450$ GeV)",
    id=1000018,
)

azh_htt_zll_a1050_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 500$ GeV)",
    id=1000019,
)

azh_htt_zll_a1050_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 550$ GeV)",
    id=1000020,
)

azh_htt_zll_a1050_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 600$ GeV)",
    id=1000021,
)

azh_htt_zll_a1050_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 700$ GeV)",
    id=1000022,
)

azh_htt_zll_a1050_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 750$ GeV)",
    id=1000023,
)

azh_htt_zll_a1050_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 800$ GeV)",
    id=1000024,
)

azh_htt_zll_a1050_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 850$ GeV)",
    id=1000025,
)

azh_htt_zll_a1050_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 900$ GeV)",
    id=1000026,
)

azh_htt_zll_a1050_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1050_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1050$ GeV, $m_H = 950$ GeV)",
    id=1000027,
)

azh_htt_zll_a1100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 1000$ GeV)",
    id=1000028,
)

azh_htt_zll_a1100_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 330$ GeV)",
    id=1000029,
)

azh_htt_zll_a1100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 350$ GeV)",
    id=1000030,
)

azh_htt_zll_a1100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 400$ GeV)",
    id=1000031,
)

azh_htt_zll_a1100_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 450$ GeV)",
    id=1000032,
)

azh_htt_zll_a1100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 500$ GeV)",
    id=1000033,
)

azh_htt_zll_a1100_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 550$ GeV)",
    id=1000034,
)

azh_htt_zll_a1100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 600$ GeV)",
    id=1000035,
)

azh_htt_zll_a1100_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 650$ GeV)",
    id=1000036,
)

azh_htt_zll_a1100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 700$ GeV)",
    id=1000037,
)

azh_htt_zll_a1100_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 750$ GeV)",
    id=1000038,
)

azh_htt_zll_a1100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 800$ GeV)",
    id=1000039,
)

azh_htt_zll_a1100_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 850$ GeV)",
    id=1000040,
)

azh_htt_zll_a1100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 900$ GeV)",
    id=1000041,
)

azh_htt_zll_a1100_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1100_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1100$ GeV, $m_H = 950$ GeV)",
    id=1000042,
)

azh_htt_zll_a1150_h1050 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h1050",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 1050$ GeV)",
    id=1000043,
)

azh_htt_zll_a1150_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 330$ GeV)",
    id=1000044,
)

azh_htt_zll_a1150_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 350$ GeV)",
    id=1000045,
)

azh_htt_zll_a1150_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 450$ GeV)",
    id=1000046,
)

azh_htt_zll_a1150_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 550$ GeV)",
    id=1000047,
)

azh_htt_zll_a1150_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 650$ GeV)",
    id=1000048,
)

azh_htt_zll_a1150_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 750$ GeV)",
    id=1000049,
)

azh_htt_zll_a1150_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 850$ GeV)",
    id=1000050,
)

azh_htt_zll_a1150_h950 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1150_h950",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1150$ GeV, $m_H = 950$ GeV)",
    id=1000051,
)

azh_htt_zll_a1200_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1000$ GeV)",
    id=1000052,
)

azh_htt_zll_a1200_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 1100$ GeV)",
    id=1000053,
)

azh_htt_zll_a1200_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 330$ GeV)",
    id=1000054,
)

azh_htt_zll_a1200_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 350$ GeV)",
    id=1000055,
)

azh_htt_zll_a1200_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 400$ GeV)",
    id=1000056,
)

azh_htt_zll_a1200_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 500$ GeV)",
    id=1000057,
)

azh_htt_zll_a1200_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 600$ GeV)",
    id=1000058,
)

azh_htt_zll_a1200_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 700$ GeV)",
    id=1000059,
)

azh_htt_zll_a1200_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 800$ GeV)",
    id=1000060,
)

azh_htt_zll_a1200_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 850$ GeV)",
    id=1000061,
)

azh_htt_zll_a1200_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1200_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1200$ GeV, $m_H = 900$ GeV)",
    id=1000062,
)

azh_htt_zll_a1300_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1000$ GeV)",
    id=1000063,
)

azh_htt_zll_a1300_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1100$ GeV)",
    id=1000064,
)

azh_htt_zll_a1300_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 1200$ GeV)",
    id=1000065,
)

azh_htt_zll_a1300_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 350$ GeV)",
    id=1000066,
)

azh_htt_zll_a1300_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 400$ GeV)",
    id=1000067,
)

azh_htt_zll_a1300_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 500$ GeV)",
    id=1000068,
)

azh_htt_zll_a1300_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 600$ GeV)",
    id=1000069,
)

azh_htt_zll_a1300_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 700$ GeV)",
    id=1000070,
)

azh_htt_zll_a1300_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 800$ GeV)",
    id=1000071,
)

azh_htt_zll_a1300_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1300_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1300$ GeV, $m_H = 900$ GeV)",
    id=1000072,
)

azh_htt_zll_a1400_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1000$ GeV)",
    id=1000073,
)

azh_htt_zll_a1400_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1100$ GeV)",
    id=1000074,
)

azh_htt_zll_a1400_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1200$ GeV)",
    id=1000075,
)

azh_htt_zll_a1400_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 1300$ GeV)",
    id=1000076,
)

azh_htt_zll_a1400_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 350$ GeV)",
    id=1000077,
)

azh_htt_zll_a1400_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 400$ GeV)",
    id=1000078,
)

azh_htt_zll_a1400_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 500$ GeV)",
    id=1000079,
)

azh_htt_zll_a1400_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 600$ GeV)",
    id=1000080,
)

azh_htt_zll_a1400_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 700$ GeV)",
    id=1000081,
)

azh_htt_zll_a1400_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 800$ GeV)",
    id=1000082,
)

azh_htt_zll_a1400_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1400_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1400$ GeV, $m_H = 900$ GeV)",
    id=1000083,
)

azh_htt_zll_a1500_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1000$ GeV)",
    id=1000084,
)

azh_htt_zll_a1500_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1100$ GeV)",
    id=1000085,
)

azh_htt_zll_a1500_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1200$ GeV)",
    id=1000086,
)

azh_htt_zll_a1500_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1300$ GeV)",
    id=1000087,
)

azh_htt_zll_a1500_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 1400$ GeV)",
    id=1000088,
)

azh_htt_zll_a1500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 350$ GeV)",
    id=1000089,
)

azh_htt_zll_a1500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 400$ GeV)",
    id=1000090,
)

azh_htt_zll_a1500_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 500$ GeV)",
    id=1000091,
)

azh_htt_zll_a1500_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 600$ GeV)",
    id=1000092,
)

azh_htt_zll_a1500_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 700$ GeV)",
    id=1000093,
)

azh_htt_zll_a1500_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1500_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1500$ GeV, $m_H = 900$ GeV)",
    id=1000094,
)

azh_htt_zll_a1600_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1000$ GeV)",
    id=1000095,
)

azh_htt_zll_a1600_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1100$ GeV)",
    id=1000096,
)

azh_htt_zll_a1600_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1200$ GeV)",
    id=1000097,
)

azh_htt_zll_a1600_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1300$ GeV)",
    id=1000098,
)

azh_htt_zll_a1600_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1400$ GeV)",
    id=1000099,
)

azh_htt_zll_a1600_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 1500$ GeV)",
    id=1000100,
)

azh_htt_zll_a1600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 350$ GeV)",
    id=1000101,
)

azh_htt_zll_a1600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 400$ GeV)",
    id=1000102,
)

azh_htt_zll_a1600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 500$ GeV)",
    id=1000103,
)

azh_htt_zll_a1600_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 600$ GeV)",
    id=1000104,
)

azh_htt_zll_a1600_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1600_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1600$ GeV, $m_H = 900$ GeV)",
    id=1000105,
)

azh_htt_zll_a1700_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1000$ GeV)",
    id=1000106,
)

azh_htt_zll_a1700_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1100$ GeV)",
    id=1000107,
)

azh_htt_zll_a1700_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1200$ GeV)",
    id=1000108,
)

azh_htt_zll_a1700_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1300$ GeV)",
    id=1000109,
)

azh_htt_zll_a1700_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1400$ GeV)",
    id=1000110,
)

azh_htt_zll_a1700_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1500$ GeV)",
    id=1000111,
)

azh_htt_zll_a1700_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 1600$ GeV)",
    id=1000112,
)

azh_htt_zll_a1700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 350$ GeV)",
    id=1000113,
)

azh_htt_zll_a1700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 400$ GeV)",
    id=1000114,
)

azh_htt_zll_a1700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 500$ GeV)",
    id=1000115,
)

azh_htt_zll_a1700_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 600$ GeV)",
    id=1000116,
)

azh_htt_zll_a1700_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 700$ GeV)",
    id=1000117,
)

azh_htt_zll_a1700_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 800$ GeV)",
    id=1000118,
)

azh_htt_zll_a1700_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1700_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1700$ GeV, $m_H = 900$ GeV)",
    id=1000119,
)

azh_htt_zll_a1800_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1000$ GeV)",
    id=1000120,
)

azh_htt_zll_a1800_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1100$ GeV)",
    id=1000121,
)

azh_htt_zll_a1800_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1200$ GeV)",
    id=1000122,
)

azh_htt_zll_a1800_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1300$ GeV)",
    id=1000123,
)

azh_htt_zll_a1800_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1400$ GeV)",
    id=1000124,
)

azh_htt_zll_a1800_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1500$ GeV)",
    id=1000125,
)

azh_htt_zll_a1800_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1600$ GeV)",
    id=1000126,
)

azh_htt_zll_a1800_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 1700$ GeV)",
    id=1000127,
)

azh_htt_zll_a1800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 350$ GeV)",
    id=1000128,
)

azh_htt_zll_a1800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 400$ GeV)",
    id=1000129,
)

azh_htt_zll_a1800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 500$ GeV)",
    id=1000130,
)

azh_htt_zll_a1800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 600$ GeV)",
    id=1000131,
)

azh_htt_zll_a1800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 700$ GeV)",
    id=1000132,
)

azh_htt_zll_a1800_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 800$ GeV)",
    id=1000133,
)

azh_htt_zll_a1800_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1800_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1800$ GeV, $m_H = 900$ GeV)",
    id=1000134,
)

azh_htt_zll_a1900_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1000$ GeV)",
    id=1000135,
)

azh_htt_zll_a1900_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1100$ GeV)",
    id=1000136,
)

azh_htt_zll_a1900_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1200$ GeV)",
    id=1000137,
)

azh_htt_zll_a1900_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1300$ GeV)",
    id=1000138,
)

azh_htt_zll_a1900_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1400$ GeV)",
    id=1000139,
)

azh_htt_zll_a1900_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1500$ GeV)",
    id=1000140,
)

azh_htt_zll_a1900_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1600$ GeV)",
    id=1000141,
)

azh_htt_zll_a1900_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1700$ GeV)",
    id=1000142,
)

azh_htt_zll_a1900_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 1800$ GeV)",
    id=1000143,
)

azh_htt_zll_a1900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 350$ GeV)",
    id=1000144,
)

azh_htt_zll_a1900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 400$ GeV)",
    id=1000145,
)

azh_htt_zll_a1900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 500$ GeV)",
    id=1000146,
)

azh_htt_zll_a1900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 600$ GeV)",
    id=1000147,
)

azh_htt_zll_a1900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 700$ GeV)",
    id=1000148,
)

azh_htt_zll_a1900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 800$ GeV)",
    id=1000149,
)

azh_htt_zll_a1900_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a1900_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 1900$ GeV, $m_H = 900$ GeV)",
    id=1000150,
)

azh_htt_zll_a2000_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1000$ GeV)",
    id=1000151,
)

azh_htt_zll_a2000_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1100$ GeV)",
    id=1000152,
)

azh_htt_zll_a2000_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1200$ GeV)",
    id=1000153,
)

azh_htt_zll_a2000_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1300$ GeV)",
    id=1000154,
)

azh_htt_zll_a2000_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1400$ GeV)",
    id=1000155,
)

azh_htt_zll_a2000_h1600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1600$ GeV)",
    id=1000156,
)

azh_htt_zll_a2000_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1700$ GeV)",
    id=1000157,
)

azh_htt_zll_a2000_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1800$ GeV)",
    id=1000158,
)

azh_htt_zll_a2000_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 1900$ GeV)",
    id=1000159,
)

azh_htt_zll_a2000_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 350$ GeV)",
    id=1000160,
)

azh_htt_zll_a2000_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 400$ GeV)",
    id=1000161,
)

azh_htt_zll_a2000_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 500$ GeV)",
    id=1000162,
)

azh_htt_zll_a2000_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 600$ GeV)",
    id=1000163,
)

azh_htt_zll_a2000_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 700$ GeV)",
    id=1000164,
)

azh_htt_zll_a2000_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 800$ GeV)",
    id=1000165,
)

azh_htt_zll_a2000_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2000_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2000$ GeV, $m_H = 900$ GeV)",
    id=1000166,
)

azh_htt_zll_a2100_h1000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1000$ GeV)",
    id=1000167,
)

azh_htt_zll_a2100_h1100 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1100",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1100$ GeV)",
    id=1000168,
)

azh_htt_zll_a2100_h1200 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1200",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1200$ GeV)",
    id=1000169,
)

azh_htt_zll_a2100_h1300 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1300",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1300$ GeV)",
    id=1000170,
)

azh_htt_zll_a2100_h1400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1400$ GeV)",
    id=1000171,
)

azh_htt_zll_a2100_h1500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1500$ GeV)",
    id=1000172,
)

azh_htt_zll_a2100_h1700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1700$ GeV)",
    id=1000173,
)

azh_htt_zll_a2100_h1800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1800$ GeV)",
    id=1000174,
)

azh_htt_zll_a2100_h1900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h1900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 1900$ GeV)",
    id=1000175,
)

azh_htt_zll_a2100_h2000 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h2000",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 2000$ GeV)",
    id=1000176,
)

azh_htt_zll_a2100_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 350$ GeV)",
    id=1000177,
)

azh_htt_zll_a2100_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 400$ GeV)",
    id=1000178,
)

azh_htt_zll_a2100_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 500$ GeV)",
    id=1000179,
)

azh_htt_zll_a2100_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 600$ GeV)",
    id=1000180,
)

azh_htt_zll_a2100_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 700$ GeV)",
    id=1000181,
)

azh_htt_zll_a2100_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 800$ GeV)",
    id=1000182,
)

azh_htt_zll_a2100_h900 = azh_htt_zll.add_process(
    name="azh_htt_zll_a2100_h900",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 2100$ GeV, $m_H = 900$ GeV)",
    id=1000183,
)

azh_htt_zll_a430_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a430_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 430$ GeV, $m_H = 330$ GeV)",
    id=1000184,
)

azh_htt_zll_a450_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 330$ GeV)",
    id=1000185,
)

azh_htt_zll_a450_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a450_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 450$ GeV, $m_H = 350$ GeV)",
    id=1000186,
)

azh_htt_zll_a500_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 330$ GeV)",
    id=1000187,
)

azh_htt_zll_a500_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 350$ GeV)",
    id=1000188,
)

azh_htt_zll_a500_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 370$ GeV)",
    id=1000189,
)

azh_htt_zll_a500_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a500_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 500$ GeV, $m_H = 400$ GeV)",
    id=1000190,
)

azh_htt_zll_a550_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 330$ GeV)",
    id=1000191,
)

azh_htt_zll_a550_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 350$ GeV)",
    id=1000192,
)

azh_htt_zll_a550_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 400$ GeV)",
    id=1000193,
)

azh_htt_zll_a550_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a550_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 550$ GeV, $m_H = 450$ GeV)",
    id=1000194,
)

azh_htt_zll_a600_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 330$ GeV)",
    id=1000195,
)

azh_htt_zll_a600_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 350$ GeV)",
    id=1000196,
)

azh_htt_zll_a600_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 400$ GeV)",
    id=1000197,
)

azh_htt_zll_a600_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 450$ GeV)",
    id=1000198,
)

azh_htt_zll_a600_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a600_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 600$ GeV, $m_H = 500$ GeV)",
    id=1000199,
)

azh_htt_zll_a650_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 330$ GeV)",
    id=1000200,
)

azh_htt_zll_a650_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 350$ GeV)",
    id=1000201,
)

azh_htt_zll_a650_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 400$ GeV)",
    id=1000202,
)

azh_htt_zll_a650_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 450$ GeV)",
    id=1000203,
)

azh_htt_zll_a650_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 500$ GeV)",
    id=1000204,
)

azh_htt_zll_a650_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a650_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 650$ GeV, $m_H = 550$ GeV)",
    id=1000205,
)

azh_htt_zll_a700_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 330$ GeV)",
    id=1000206,
)

azh_htt_zll_a700_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 350$ GeV)",
    id=1000207,
)

azh_htt_zll_a700_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 370$ GeV)",
    id=1000208,
)

azh_htt_zll_a700_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 400$ GeV)",
    id=1000209,
)

azh_htt_zll_a700_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 450$ GeV)",
    id=1000210,
)

azh_htt_zll_a700_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 500$ GeV)",
    id=1000211,
)

azh_htt_zll_a700_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a700_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 700$ GeV, $m_H = 550$ GeV)",
    id=1000212,
)

azh_htt_zll_a750_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 330$ GeV)",
    id=1000213,
)

azh_htt_zll_a750_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 350$ GeV)",
    id=1000214,
)

azh_htt_zll_a750_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 400$ GeV)",
    id=1000215,
)

azh_htt_zll_a750_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 450$ GeV)",
    id=1000216,
)

azh_htt_zll_a750_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 500$ GeV)",
    id=1000217,
)

azh_htt_zll_a750_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 550$ GeV)",
    id=1000218,
)

azh_htt_zll_a750_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 600$ GeV)",
    id=1000219,
)

azh_htt_zll_a750_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a750_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 750$ GeV, $m_H = 650$ GeV)",
    id=1000220,
)

azh_htt_zll_a800_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 330$ GeV)",
    id=1000221,
)

azh_htt_zll_a800_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 350$ GeV)",
    id=1000222,
)

azh_htt_zll_a800_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 400$ GeV)",
    id=1000223,
)

azh_htt_zll_a800_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 450$ GeV)",
    id=1000224,
)

azh_htt_zll_a800_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 500$ GeV)",
    id=1000225,
)

azh_htt_zll_a800_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 550$ GeV)",
    id=1000226,
)

azh_htt_zll_a800_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 600$ GeV)",
    id=1000227,
)

azh_htt_zll_a800_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 650$ GeV)",
    id=1000228,
)

azh_htt_zll_a800_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a800_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 800$ GeV, $m_H = 700$ GeV)",
    id=1000229,
)

azh_htt_zll_a850_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 330$ GeV)",
    id=1000230,
)

azh_htt_zll_a850_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 350$ GeV)",
    id=1000231,
)

azh_htt_zll_a850_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 400$ GeV)",
    id=1000232,
)

azh_htt_zll_a850_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 450$ GeV)",
    id=1000233,
)

azh_htt_zll_a850_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 500$ GeV)",
    id=1000234,
)

azh_htt_zll_a850_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 550$ GeV)",
    id=1000235,
)

azh_htt_zll_a850_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 600$ GeV)",
    id=1000236,
)

azh_htt_zll_a850_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 650$ GeV)",
    id=1000237,
)

azh_htt_zll_a850_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 700$ GeV)",
    id=1000238,
)

azh_htt_zll_a850_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a850_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 850$ GeV, $m_H = 750$ GeV)",
    id=1000239,
)

azh_htt_zll_a900_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 330$ GeV)",
    id=1000240,
)

azh_htt_zll_a900_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 350$ GeV)",
    id=1000241,
)

azh_htt_zll_a900_h370 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h370",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 370$ GeV)",
    id=1000242,
)

azh_htt_zll_a900_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 400$ GeV)",
    id=1000243,
)

azh_htt_zll_a900_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 450$ GeV)",
    id=1000244,
)

azh_htt_zll_a900_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 550$ GeV)",
    id=1000245,
)

azh_htt_zll_a900_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 500$ GeV)",
    id=1000246,
)

azh_htt_zll_a900_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 600$ GeV)",
    id=1000247,
)

azh_htt_zll_a900_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 650$ GeV)",
    id=1000248,
)

azh_htt_zll_a900_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 700$ GeV)",
    id=1000249,
)

azh_htt_zll_a900_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 750$ GeV)",
    id=1000250,
)

azh_htt_zll_a900_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a900_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 900$ GeV, $m_H = 800$ GeV)",
    id=1000251,
)

azh_htt_zll_a950_h330 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h330",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 330$ GeV)",
    id=1000252,
)

azh_htt_zll_a950_h350 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h350",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 350$ GeV)",
    id=1000253,
)

azh_htt_zll_a950_h400 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h400",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 400$ GeV)",
    id=1000254,
)

azh_htt_zll_a950_h450 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h450",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 450$ GeV)",
    id=1000255,
)

azh_htt_zll_a950_h500 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h500",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 500$ GeV)",
    id=1000256,
)

azh_htt_zll_a950_h550 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h550",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 550$ GeV)",
    id=1000257,
)

azh_htt_zll_a950_h600 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h600",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 600$ GeV)",
    id=1000258,
)

azh_htt_zll_a950_h650 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h650",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 650$ GeV)",
    id=1000259,
)

azh_htt_zll_a950_h700 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h700",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 700$ GeV)",
    id=1000260,
)

azh_htt_zll_a950_h750 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h750",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 750$ GeV)",
    id=1000261,
)

azh_htt_zll_a950_h800 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h800",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 800$ GeV)",
    id=1000262,
)

azh_htt_zll_a950_h850 = azh_htt_zll.add_process(
    name="azh_htt_zll_a950_h850",  # h = heavy Higgs boson (not SM Higgs)
    label=rf"{azh_htt_zll.label} ($m_A = 950$ GeV, $m_H = 850$ GeV)",
    id=1000263,
)
