# coding: utf-8

"""
m(ttbar) line search signal process definitions
"""

__all__ = [
    "zprime_tt",
    "zprime_tt_m_400_w_40",
    "zprime_tt_m_400_w_120",
    "zprime_tt_m_400_w_4",
    "zprime_tt_m_500_w_50",
    "zprime_tt_m_500_w_150",
    "zprime_tt_m_500_w_5",
    "zprime_tt_m_600_w_60",
    "zprime_tt_m_600_w_180",
    "zprime_tt_m_600_w_6",
    "zprime_tt_m_700_w_70",
    "zprime_tt_m_700_w_210",
    "zprime_tt_m_700_w_7",
    "zprime_tt_m_800_w_80",
    "zprime_tt_m_800_w_240",
    "zprime_tt_m_800_w_8",
    "zprime_tt_m_900_w_90",
    "zprime_tt_m_900_w_270",
    "zprime_tt_m_900_w_9",
    "zprime_tt_m_1000_w_100",
    "zprime_tt_m_1000_w_300",
    "zprime_tt_m_1000_w_10",
    "zprime_tt_m_1200_w_120",
    "zprime_tt_m_1200_w_360",
    "zprime_tt_m_1200_w_12",
    "zprime_tt_m_1400_w_140",
    "zprime_tt_m_1400_w_420",
    "zprime_tt_m_1400_w_14",
    "zprime_tt_m_1600_w_160",
    "zprime_tt_m_1600_w_480",
    "zprime_tt_m_1600_w_16",
    "zprime_tt_m_1800_w_180",
    "zprime_tt_m_1800_w_540",
    "zprime_tt_m_1800_w_18",
    "zprime_tt_m_2000_w_200",
    "zprime_tt_m_2000_w_600",
    "zprime_tt_m_2000_w_20",
    "zprime_tt_m_2500_w_250",
    "zprime_tt_m_2500_w_750",
    "zprime_tt_m_2500_w_25",
    "zprime_tt_m_3000_w_300",
    "zprime_tt_m_3000_w_900",
    "zprime_tt_m_3000_w_30",
    "zprime_tt_m_3500_w_350",
    "zprime_tt_m_3500_w_1050",
    "zprime_tt_m_3500_w_35",
    "zprime_tt_m_4000_w_400",
    "zprime_tt_m_4000_w_1200",
    "zprime_tt_m_4000_w_40",
    "zprime_tt_m_4500_w_450",
    "zprime_tt_m_4500_w_1350",
    "zprime_tt_m_4500_w_45",
    "zprime_tt_m_5000_w_500",
    "zprime_tt_m_5000_w_1500",
    "zprime_tt_m_5000_w_50",
    "zprime_tt_m_6000_w_600",
    "zprime_tt_m_6000_w_1800",
    "zprime_tt_m_6000_w_60",
    "zprime_tt_m_7000_w_700",
    "zprime_tt_m_7000_w_2100",
    "zprime_tt_m_7000_w_70",
    "zprime_tt_m_8000_w_800",
    "zprime_tt_m_8000_w_2400",
    "zprime_tt_m_8000_w_80",
    "zprime_tt_m_9000_w_900",
    "zprime_tt_m_9000_w_2700",
    "zprime_tt_m_9000_w_90",
    "hscalar_tt",
    "hscalar_tt_sl",
    "hscalar_tt_sl_m_365_w_91p25",
    "hscalar_tt_sl_m_365_w_91p25_res",
    "hscalar_tt_sl_m_365_w_91p25_int",
    "hscalar_tt_sl_m_400_w_100p0",
    "hscalar_tt_sl_m_400_w_100p0_res",
    "hscalar_tt_sl_m_400_w_100p0_int",
    "hscalar_tt_sl_m_500_w_125p0",
    "hscalar_tt_sl_m_500_w_125p0_res",
    "hscalar_tt_sl_m_500_w_125p0_int",
    "hscalar_tt_sl_m_600_w_150p0",
    "hscalar_tt_sl_m_600_w_150p0_res",
    "hscalar_tt_sl_m_600_w_150p0_int",
    "hscalar_tt_sl_m_800_w_200p0",
    "hscalar_tt_sl_m_800_w_200p0_res",
    "hscalar_tt_sl_m_800_w_200p0_int",
    "hscalar_tt_sl_m_1000_w_250p0",
    "hscalar_tt_sl_m_1000_w_250p0_res",
    "hscalar_tt_sl_m_1000_w_250p0_int",
    "hscalar_tt_sl_m_365_w_36p5",
    "hscalar_tt_sl_m_365_w_36p5_res",
    "hscalar_tt_sl_m_365_w_36p5_int",
    "hscalar_tt_sl_m_400_w_40p0",
    "hscalar_tt_sl_m_400_w_40p0_res",
    "hscalar_tt_sl_m_400_w_40p0_int",
    "hscalar_tt_sl_m_500_w_50p0",
    "hscalar_tt_sl_m_500_w_50p0_res",
    "hscalar_tt_sl_m_500_w_50p0_int",
    "hscalar_tt_sl_m_600_w_60p0",
    "hscalar_tt_sl_m_600_w_60p0_res",
    "hscalar_tt_sl_m_600_w_60p0_int",
    "hscalar_tt_sl_m_800_w_80p0",
    "hscalar_tt_sl_m_800_w_80p0_res",
    "hscalar_tt_sl_m_800_w_80p0_int",
    "hscalar_tt_sl_m_1000_w_100p0",
    "hscalar_tt_sl_m_1000_w_100p0_res",
    "hscalar_tt_sl_m_1000_w_100p0_int",
    "hscalar_tt_sl_m_365_w_9p125",
    "hscalar_tt_sl_m_365_w_9p125_res",
    "hscalar_tt_sl_m_365_w_9p125_int",
    "hscalar_tt_sl_m_400_w_10p0",
    "hscalar_tt_sl_m_400_w_10p0_res",
    "hscalar_tt_sl_m_400_w_10p0_int",
    "hscalar_tt_sl_m_500_w_12p5",
    "hscalar_tt_sl_m_500_w_12p5_res",
    "hscalar_tt_sl_m_500_w_12p5_int",
    "hscalar_tt_sl_m_600_w_15p0",
    "hscalar_tt_sl_m_600_w_15p0_res",
    "hscalar_tt_sl_m_600_w_15p0_int",
    "hscalar_tt_sl_m_800_w_20p0",
    "hscalar_tt_sl_m_800_w_20p0_res",
    "hscalar_tt_sl_m_800_w_20p0_int",
    "hscalar_tt_sl_m_1000_w_25p0",
    "hscalar_tt_sl_m_1000_w_25p0_res",
    "hscalar_tt_sl_m_1000_w_25p0_int",
    "hpseudo_tt",
    "hpseudo_tt_sl",
    "hpseudo_tt_sl_m_365_w_91p25",
    "hpseudo_tt_sl_m_365_w_91p25_res",
    "hpseudo_tt_sl_m_365_w_91p25_int",
    "hpseudo_tt_sl_m_400_w_100p0",
    "hpseudo_tt_sl_m_400_w_100p0_res",
    "hpseudo_tt_sl_m_400_w_100p0_int",
    "hpseudo_tt_sl_m_500_w_125p0",
    "hpseudo_tt_sl_m_500_w_125p0_res",
    "hpseudo_tt_sl_m_500_w_125p0_int",
    "hpseudo_tt_sl_m_600_w_150p0",
    "hpseudo_tt_sl_m_600_w_150p0_res",
    "hpseudo_tt_sl_m_600_w_150p0_int",
    "hpseudo_tt_sl_m_800_w_200p0",
    "hpseudo_tt_sl_m_800_w_200p0_res",
    "hpseudo_tt_sl_m_800_w_200p0_int",
    "hpseudo_tt_sl_m_1000_w_250p0",
    "hpseudo_tt_sl_m_1000_w_250p0_res",
    "hpseudo_tt_sl_m_1000_w_250p0_int",
    "hpseudo_tt_sl_m_365_w_36p5",
    "hpseudo_tt_sl_m_365_w_36p5_res",
    "hpseudo_tt_sl_m_365_w_36p5_int",
    "hpseudo_tt_sl_m_400_w_40p0",
    "hpseudo_tt_sl_m_400_w_40p0_res",
    "hpseudo_tt_sl_m_400_w_40p0_int",
    "hpseudo_tt_sl_m_500_w_50p0",
    "hpseudo_tt_sl_m_500_w_50p0_res",
    "hpseudo_tt_sl_m_500_w_50p0_int",
    "hpseudo_tt_sl_m_600_w_60p0",
    "hpseudo_tt_sl_m_600_w_60p0_res",
    "hpseudo_tt_sl_m_600_w_60p0_int",
    "hpseudo_tt_sl_m_800_w_80p0",
    "hpseudo_tt_sl_m_800_w_80p0_res",
    "hpseudo_tt_sl_m_800_w_80p0_int",
    "hpseudo_tt_sl_m_1000_w_100p0",
    "hpseudo_tt_sl_m_1000_w_100p0_res",
    "hpseudo_tt_sl_m_1000_w_100p0_int",
    "hpseudo_tt_sl_m_365_w_9p125",
    "hpseudo_tt_sl_m_365_w_9p125_res",
    "hpseudo_tt_sl_m_365_w_9p125_int",
    "hpseudo_tt_sl_m_400_w_10p0",
    "hpseudo_tt_sl_m_400_w_10p0_res",
    "hpseudo_tt_sl_m_400_w_10p0_int",
    "hpseudo_tt_sl_m_500_w_12p5",
    "hpseudo_tt_sl_m_500_w_12p5_res",
    "hpseudo_tt_sl_m_500_w_12p5_int",
    "hpseudo_tt_sl_m_600_w_15p0",
    "hpseudo_tt_sl_m_600_w_15p0_res",
    "hpseudo_tt_sl_m_600_w_15p0_int",
    "hpseudo_tt_sl_m_800_w_20p0",
    "hpseudo_tt_sl_m_800_w_20p0_res",
    "hpseudo_tt_sl_m_800_w_20p0_int",
    "hpseudo_tt_sl_m_1000_w_25p0",
    "hpseudo_tt_sl_m_1000_w_25p0_res",
    "hpseudo_tt_sl_m_1000_w_25p0_int",
    "rsgluon_tt",
    "rsgluon_tt_m_500",
    "rsgluon_tt_m_1000",
    "rsgluon_tt_m_1500",
    "rsgluon_tt_m_2000",
    "rsgluon_tt_m_2500",
    "rsgluon_tt_m_3000",
    "rsgluon_tt_m_3500",
    "rsgluon_tt_m_4000",
    "rsgluon_tt_m_4500",
    "rsgluon_tt_m_5000",
    "rsgluon_tt_m_5500",
    "rsgluon_tt_m_6000",
]


from order import Process
from scinum import Number

#
# Z prime
#

zprime = Process(
    name="zprime",
    label=r"Z'",
    id=60000,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt = zprime.add_process(
    name="zprime_tt",
    label=rf"{zprime.label} $\rightarrow t\bar{{t}}$",
    id=61000,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_400_w_40 = zprime_tt.add_process(
    name="zprime_tt_m_400_w_40",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=61001,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_400_w_120 = zprime_tt.add_process(
    name="zprime_tt_m_400_w_120",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 30\%$)",
    id=61002,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_400_w_4 = zprime_tt.add_process(
    name="zprime_tt_m_400_w_4",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 1\%$)",
    id=61003,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_500_w_50 = zprime_tt.add_process(
    name="zprime_tt_m_500_w_50",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=61004,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_500_w_150 = zprime_tt.add_process(
    name="zprime_tt_m_500_w_150",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 30\%$)",
    id=61005,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_500_w_5 = zprime_tt.add_process(
    name="zprime_tt_m_500_w_5",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 1\%$)",
    id=61006,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_600_w_60 = zprime_tt.add_process(
    name="zprime_tt_m_600_w_60",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=61007,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_600_w_180 = zprime_tt.add_process(
    name="zprime_tt_m_600_w_180",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 30\%$)",
    id=61008,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_600_w_6 = zprime_tt.add_process(
    name="zprime_tt_m_600_w_6",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 1\%$)",
    id=61009,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_700_w_70 = zprime_tt.add_process(
    name="zprime_tt_m_700_w_70",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 10\%$)",
    id=61010,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_700_w_210 = zprime_tt.add_process(
    name="zprime_tt_m_700_w_210",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 30\%$)",
    id=61011,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_700_w_7 = zprime_tt.add_process(
    name="zprime_tt_m_700_w_7",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 1\%$)",
    id=61012,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_800_w_80 = zprime_tt.add_process(
    name="zprime_tt_m_800_w_80",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=61013,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_800_w_240 = zprime_tt.add_process(
    name="zprime_tt_m_800_w_240",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 30\%$)",
    id=61014,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_800_w_8 = zprime_tt.add_process(
    name="zprime_tt_m_800_w_8",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 1\%$)",
    id=61015,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_900_w_90 = zprime_tt.add_process(
    name="zprime_tt_m_900_w_90",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 10\%$)",
    id=61016,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_900_w_270 = zprime_tt.add_process(
    name="zprime_tt_m_900_w_270",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 30\%$)",
    id=61017,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_900_w_9 = zprime_tt.add_process(
    name="zprime_tt_m_900_w_9",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 1\%$)",
    id=61018,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_1000_w_100 = zprime_tt.add_process(
    name="zprime_tt_m_1000_w_100",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=61019,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1000_w_300 = zprime_tt.add_process(
    name="zprime_tt_m_1000_w_300",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 30\%$)",
    id=61020,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1000_w_10 = zprime_tt.add_process(
    name="zprime_tt_m_1000_w_10",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 1\%$)",
    id=61021,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_1200_w_120 = zprime_tt.add_process(
    name="zprime_tt_m_1200_w_120",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 10\%$)",
    id=61022,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1200_w_360 = zprime_tt.add_process(
    name="zprime_tt_m_1200_w_360",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 30\%$)",
    id=61023,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1200_w_12 = zprime_tt.add_process(
    name="zprime_tt_m_1200_w_12",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 1\%$)",
    id=61024,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_1400_w_140 = zprime_tt.add_process(
    name="zprime_tt_m_1400_w_140",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 10\%$)",
    id=61025,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1400_w_420 = zprime_tt.add_process(
    name="zprime_tt_m_1400_w_420",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 30\%$)",
    id=61026,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1400_w_14 = zprime_tt.add_process(
    name="zprime_tt_m_1400_w_14",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 1\%$)",
    id=61027,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_1600_w_160 = zprime_tt.add_process(
    name="zprime_tt_m_1600_w_160",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 10\%$)",
    id=61028,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1600_w_480 = zprime_tt.add_process(
    name="zprime_tt_m_1600_w_480",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 30\%$)",
    id=61029,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1600_w_16 = zprime_tt.add_process(
    name="zprime_tt_m_1600_w_16",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 1\%$)",
    id=61030,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_1800_w_180 = zprime_tt.add_process(
    name="zprime_tt_m_1800_w_180",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 10\%$)",
    id=61031,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1800_w_540 = zprime_tt.add_process(
    name="zprime_tt_m_1800_w_540",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 30\%$)",
    id=61032,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_1800_w_18 = zprime_tt.add_process(
    name="zprime_tt_m_1800_w_18",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 1\%$)",
    id=61033,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_2000_w_200 = zprime_tt.add_process(
    name="zprime_tt_m_2000_w_200",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 10\%$)",
    id=61034,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_2000_w_600 = zprime_tt.add_process(
    name="zprime_tt_m_2000_w_600",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 30\%$)",
    id=61035,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_2000_w_20 = zprime_tt.add_process(
    name="zprime_tt_m_2000_w_20",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 1\%$)",
    id=61036,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_2500_w_250 = zprime_tt.add_process(
    name="zprime_tt_m_2500_w_250",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 10\%$)",
    id=61037,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_2500_w_750 = zprime_tt.add_process(
    name="zprime_tt_m_2500_w_750",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 30\%$)",
    id=61038,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_2500_w_25 = zprime_tt.add_process(
    name="zprime_tt_m_2500_w_25",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 1\%$)",
    id=61039,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_3000_w_300 = zprime_tt.add_process(
    name="zprime_tt_m_3000_w_300",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 10\%$)",
    id=61040,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_3000_w_900 = zprime_tt.add_process(
    name="zprime_tt_m_3000_w_900",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 30\%$)",
    id=61041,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_3000_w_30 = zprime_tt.add_process(
    name="zprime_tt_m_3000_w_30",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 1\%$)",
    id=61042,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_3500_w_350 = zprime_tt.add_process(
    name="zprime_tt_m_3500_w_350",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 10\%$)",
    id=61043,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_3500_w_1050 = zprime_tt.add_process(
    name="zprime_tt_m_3500_w_1050",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 30\%$)",
    id=61044,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_3500_w_35 = zprime_tt.add_process(
    name="zprime_tt_m_3500_w_35",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 1\%$)",
    id=61045,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_4000_w_400 = zprime_tt.add_process(
    name="zprime_tt_m_4000_w_400",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 10\%$)",
    id=61046,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_4000_w_1200 = zprime_tt.add_process(
    name="zprime_tt_m_4000_w_1200",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 30\%$)",
    id=61047,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_4000_w_40 = zprime_tt.add_process(
    name="zprime_tt_m_4000_w_40",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 1\%$)",
    id=61048,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_4500_w_450 = zprime_tt.add_process(
    name="zprime_tt_m_4500_w_450",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 10\%$)",
    id=61049,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_4500_w_1350 = zprime_tt.add_process(
    name="zprime_tt_m_4500_w_1350",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 30\%$)",
    id=61050,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_4500_w_45 = zprime_tt.add_process(
    name="zprime_tt_m_4500_w_45",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 1\%$)",
    id=61051,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_5000_w_500 = zprime_tt.add_process(
    name="zprime_tt_m_5000_w_500",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 10\%$)",
    id=61052,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_5000_w_1500 = zprime_tt.add_process(
    name="zprime_tt_m_5000_w_1500",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 30\%$)",
    id=61053,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_5000_w_50 = zprime_tt.add_process(
    name="zprime_tt_m_5000_w_50",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 1\%$)",
    id=61054,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_6000_w_600 = zprime_tt.add_process(
    name="zprime_tt_m_6000_w_600",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 10\%$)",
    id=61055,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_6000_w_1800 = zprime_tt.add_process(
    name="zprime_tt_m_6000_w_1800",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 30\%$)",
    id=61056,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_6000_w_60 = zprime_tt.add_process(
    name="zprime_tt_m_6000_w_60",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 1\%$)",
    id=61057,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_7000_w_700 = zprime_tt.add_process(
    name="zprime_tt_m_7000_w_700",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 10\%$)",
    id=61058,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_7000_w_2100 = zprime_tt.add_process(
    name="zprime_tt_m_7000_w_2100",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 30\%$)",
    id=61059,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_7000_w_70 = zprime_tt.add_process(
    name="zprime_tt_m_7000_w_70",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 1\%$)",
    id=61060,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_8000_w_800 = zprime_tt.add_process(
    name="zprime_tt_m_8000_w_800",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 10\%$)",
    id=61061,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_8000_w_2400 = zprime_tt.add_process(
    name="zprime_tt_m_8000_w_2400",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 30\%$)",
    id=61062,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_8000_w_80 = zprime_tt.add_process(
    name="zprime_tt_m_8000_w_80",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 1\%$)",
    id=61063,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

zprime_tt_m_9000_w_900 = zprime_tt.add_process(
    name="zprime_tt_m_9000_w_900",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 10\%$)",
    id=61064,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_9000_w_2700 = zprime_tt.add_process(
    name="zprime_tt_m_9000_w_2700",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 30\%$)",
    id=61065,
    xsecs={13: Number(0.1)},  # TODO
)


zprime_tt_m_9000_w_90 = zprime_tt.add_process(
    name="zprime_tt_m_9000_w_90",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 1\%$)",
    id=61066,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Scalar heavy Higgs
#

hscalar_tt = Process(
    name="hscalar_tt",
    label=r"H $\rightarrow t\bar{t}$",
    id=70000,
    xsecs={13: Number(0.1)},  # TODO
)


hscalar_tt_sl = hscalar_tt.add_process(
    name="hscalar_tt_sl",
    label=rf"{hscalar_tt.label} $\rightarrow \ell\nu + \mathrm{{jets}}$",
    id=70100,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 25%

hscalar_tt_sl_m_365_w_91p25 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_365_w_91p25",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 25\%$)",
    id=70101,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_91p25_res = hscalar_tt_sl_m_365_w_91p25.add_process(
    name="hscalar_tt_sl_m_365_w_91p25_res",
    label=rf"{hscalar_tt_sl_m_365_w_91p25.label}, res",
    id=70102,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_91p25_int = hscalar_tt_sl_m_365_w_91p25.add_process(
    name="hscalar_tt_sl_m_365_w_91p25_int",
    label=rf"{hscalar_tt_sl_m_365_w_91p25.label}, int",
    id=70103,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_100p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_400_w_100p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 25\%$)",
    id=70104,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_100p0_res = hscalar_tt_sl_m_400_w_100p0.add_process(
    name="hscalar_tt_sl_m_400_w_100p0_res",
    label=rf"{hscalar_tt_sl_m_400_w_100p0.label}, res",
    id=70105,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_100p0_int = hscalar_tt_sl_m_400_w_100p0.add_process(
    name="hscalar_tt_sl_m_400_w_100p0_int",
    label=rf"{hscalar_tt_sl_m_400_w_100p0.label}, int",
    id=70106,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_125p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_500_w_125p0",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 25\%$)",
    id=70107,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_125p0_res = hscalar_tt_sl_m_500_w_125p0.add_process(
    name="hscalar_tt_sl_m_500_w_125p0_res",
    label=rf"{hscalar_tt_sl_m_500_w_125p0.label}, res",
    id=70108,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_125p0_int = hscalar_tt_sl_m_500_w_125p0.add_process(
    name="hscalar_tt_sl_m_500_w_125p0_int",
    label=rf"{hscalar_tt_sl_m_500_w_125p0.label}, int",
    id=70109,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 25%

hscalar_tt_sl_m_600_w_150p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_600_w_150p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 25\%$)",
    id=70110,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_150p0_res = hscalar_tt_sl_m_600_w_150p0.add_process(
    name="hscalar_tt_sl_m_600_w_150p0_res",
    label=rf"{hscalar_tt_sl_m_600_w_150p0.label}, res",
    id=70111,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_150p0_int = hscalar_tt_sl_m_600_w_150p0.add_process(
    name="hscalar_tt_sl_m_600_w_150p0_int",
    label=rf"{hscalar_tt_sl_m_600_w_150p0.label}, int",
    id=70112,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_200p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_800_w_200p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 25\%$)",
    id=70113,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_200p0_res = hscalar_tt_sl_m_800_w_200p0.add_process(
    name="hscalar_tt_sl_m_800_w_200p0_res",
    label=rf"{hscalar_tt_sl_m_800_w_200p0.label}, res",
    id=70114,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_200p0_int = hscalar_tt_sl_m_800_w_200p0.add_process(
    name="hscalar_tt_sl_m_800_w_200p0_int",
    label=rf"{hscalar_tt_sl_m_800_w_200p0.label}, int",
    id=70115,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_250p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_1000_w_250p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 25\%$)",
    id=70116,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_250p0_res = hscalar_tt_sl_m_1000_w_250p0.add_process(
    name="hscalar_tt_sl_m_1000_w_250p0_res",
    label=rf"{hscalar_tt_sl_m_1000_w_250p0.label}, res",
    id=70117,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_250p0_int = hscalar_tt_sl_m_1000_w_250p0.add_process(
    name="hscalar_tt_sl_m_1000_w_250p0_int",
    label=rf"{hscalar_tt_sl_m_1000_w_250p0.label}, int",
    id=70118,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

hscalar_tt_sl_m_365_w_36p5 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_365_w_36p5",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 10\%$)",
    id=70119,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_36p5_res = hscalar_tt_sl_m_365_w_36p5.add_process(
    name="hscalar_tt_sl_m_365_w_36p5_res",
    label=rf"{hscalar_tt_sl_m_365_w_36p5.label}, res",
    id=70120,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_36p5_int = hscalar_tt_sl_m_365_w_36p5.add_process(
    name="hscalar_tt_sl_m_365_w_36p5_int",
    label=rf"{hscalar_tt_sl_m_365_w_36p5.label}, int",
    id=70121,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_40p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_400_w_40p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=70122,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_40p0_res = hscalar_tt_sl_m_400_w_40p0.add_process(
    name="hscalar_tt_sl_m_400_w_40p0_res",
    label=rf"{hscalar_tt_sl_m_400_w_40p0.label}, res",
    id=70123,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_40p0_int = hscalar_tt_sl_m_400_w_40p0.add_process(
    name="hscalar_tt_sl_m_400_w_40p0_int",
    label=rf"{hscalar_tt_sl_m_400_w_40p0.label}, int",
    id=70124,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_50p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_500_w_50p0",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=70125,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_50p0_res = hscalar_tt_sl_m_500_w_50p0.add_process(
    name="hscalar_tt_sl_m_500_w_50p0_res",
    label=rf"{hscalar_tt_sl_m_500_w_50p0.label}, res",
    id=70126,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_50p0_int = hscalar_tt_sl_m_500_w_50p0.add_process(
    name="hscalar_tt_sl_m_500_w_50p0_int",
    label=rf"{hscalar_tt_sl_m_500_w_50p0.label}, int",
    id=70127,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

hscalar_tt_sl_m_600_w_60p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_600_w_60p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=70128,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_60p0_res = hscalar_tt_sl_m_600_w_60p0.add_process(
    name="hscalar_tt_sl_m_600_w_60p0_res",
    label=rf"{hscalar_tt_sl_m_600_w_60p0.label}, res",
    id=70129,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_60p0_int = hscalar_tt_sl_m_600_w_60p0.add_process(
    name="hscalar_tt_sl_m_600_w_60p0_int",
    label=rf"{hscalar_tt_sl_m_600_w_60p0.label}, int",
    id=70130,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_80p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_800_w_80p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=70131,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_80p0_res = hscalar_tt_sl_m_800_w_80p0.add_process(
    name="hscalar_tt_sl_m_800_w_80p0_res",
    label=rf"{hscalar_tt_sl_m_800_w_80p0.label}, res",
    id=70132,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_80p0_int = hscalar_tt_sl_m_800_w_80p0.add_process(
    name="hscalar_tt_sl_m_800_w_80p0_int",
    label=rf"{hscalar_tt_sl_m_800_w_80p0.label}, int",
    id=70133,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_100p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_1000_w_100p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=70134,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_100p0_res = hscalar_tt_sl_m_1000_w_100p0.add_process(
    name="hscalar_tt_sl_m_1000_w_100p0_res",
    label=rf"{hscalar_tt_sl_m_1000_w_100p0.label}, res",
    id=70135,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_100p0_int = hscalar_tt_sl_m_1000_w_100p0.add_process(
    name="hscalar_tt_sl_m_1000_w_100p0_int",
    label=rf"{hscalar_tt_sl_m_1000_w_100p0.label}, int",
    id=70136,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 2.5%

hscalar_tt_sl_m_365_w_9p125 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_365_w_9p125",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 2\%$)",
    id=70137,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_9p125_res = hscalar_tt_sl_m_365_w_9p125.add_process(
    name="hscalar_tt_sl_m_365_w_9p125_res",
    label=rf"{hscalar_tt_sl_m_365_w_9p125.label}, res",
    id=70138,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_365_w_9p125_int = hscalar_tt_sl_m_365_w_9p125.add_process(
    name="hscalar_tt_sl_m_365_w_9p125_int",
    label=rf"{hscalar_tt_sl_m_365_w_9p125.label}, int",
    id=70139,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_10p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_400_w_10p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 2\%$)",
    id=70140,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_10p0_res = hscalar_tt_sl_m_400_w_10p0.add_process(
    name="hscalar_tt_sl_m_400_w_10p0_res",
    label=rf"{hscalar_tt_sl_m_400_w_10p0.label}, res",
    id=70141,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_400_w_10p0_int = hscalar_tt_sl_m_400_w_10p0.add_process(
    name="hscalar_tt_sl_m_400_w_10p0_int",
    label=rf"{hscalar_tt_sl_m_400_w_10p0.label}, int",
    id=70142,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_12p5 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_500_w_12p5",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 2\%$)",
    id=70143,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_12p5_res = hscalar_tt_sl_m_500_w_12p5.add_process(
    name="hscalar_tt_sl_m_500_w_12p5_res",
    label=rf"{hscalar_tt_sl_m_500_w_12p5.label}, res",
    id=70144,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_500_w_12p5_int = hscalar_tt_sl_m_500_w_12p5.add_process(
    name="hscalar_tt_sl_m_500_w_12p5_int",
    label=rf"{hscalar_tt_sl_m_500_w_12p5.label}, int",
    id=70145,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 2.5%

hscalar_tt_sl_m_600_w_15p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_600_w_15p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 2\%$)",
    id=70146,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_15p0_res = hscalar_tt_sl_m_600_w_15p0.add_process(
    name="hscalar_tt_sl_m_600_w_15p0_res",
    label=rf"{hscalar_tt_sl_m_600_w_15p0.label}, res",
    id=70147,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_600_w_15p0_int = hscalar_tt_sl_m_600_w_15p0.add_process(
    name="hscalar_tt_sl_m_600_w_15p0_int",
    label=rf"{hscalar_tt_sl_m_600_w_15p0.label}, int",
    id=70148,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_20p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_800_w_20p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 2\%$)",
    id=70149,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_20p0_res = hscalar_tt_sl_m_800_w_20p0.add_process(
    name="hscalar_tt_sl_m_800_w_20p0_res",
    label=rf"{hscalar_tt_sl_m_800_w_20p0.label}, res",
    id=70150,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_800_w_20p0_int = hscalar_tt_sl_m_800_w_20p0.add_process(
    name="hscalar_tt_sl_m_800_w_20p0_int",
    label=rf"{hscalar_tt_sl_m_800_w_20p0.label}, int",
    id=70151,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_25p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m_1000_w_25p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 2\%$)",
    id=70152,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_25p0_res = hscalar_tt_sl_m_1000_w_25p0.add_process(
    name="hscalar_tt_sl_m_1000_w_25p0_res",
    label=rf"{hscalar_tt_sl_m_1000_w_25p0.label}, res",
    id=70153,
    xsecs={13: Number(0.1)},  # TODO
)

hscalar_tt_sl_m_1000_w_25p0_int = hscalar_tt_sl_m_1000_w_25p0.add_process(
    name="hscalar_tt_sl_m_1000_w_25p0_int",
    label=rf"{hscalar_tt_sl_m_1000_w_25p0.label}, int",
    id=70154,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Pseudoscalar heavy Higgs
#

hpseudo_tt = Process(
    name="hpseudo_tt",
    label=r"A $\rightarrow t\bar{t}$",
    id=71000,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl = hpseudo_tt.add_process(
    name="hpseudo_tt_sl",
    label=rf"{hpseudo_tt.label} $\rightarrow \ell\nu + \mathrm{{jets}}$",
    id=71100,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 25%

hpseudo_tt_sl_m_365_w_91p25 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_365_w_91p25",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 25\%$)",
    id=71101,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_91p25_res = hpseudo_tt_sl_m_365_w_91p25.add_process(
    name="hpseudo_tt_sl_m_365_w_91p25_res",
    label=rf"{hpseudo_tt_sl_m_365_w_91p25.label}, res",
    id=71102,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_91p25_int = hpseudo_tt_sl_m_365_w_91p25.add_process(
    name="hpseudo_tt_sl_m_365_w_91p25_int",
    label=rf"{hpseudo_tt_sl_m_365_w_91p25.label}, int",
    id=71103,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_100p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_400_w_100p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 25\%$)",
    id=71104,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_100p0_res = hpseudo_tt_sl_m_400_w_100p0.add_process(
    name="hpseudo_tt_sl_m_400_w_100p0_res",
    label=rf"{hpseudo_tt_sl_m_400_w_100p0.label}, res",
    id=71105,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_100p0_int = hpseudo_tt_sl_m_400_w_100p0.add_process(
    name="hpseudo_tt_sl_m_400_w_100p0_int",
    label=rf"{hpseudo_tt_sl_m_400_w_100p0.label}, int",
    id=71106,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_125p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_500_w_125p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 25\%$)",
    id=71107,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_125p0_res = hpseudo_tt_sl_m_500_w_125p0.add_process(
    name="hpseudo_tt_sl_m_500_w_125p0_res",
    label=rf"{hpseudo_tt_sl_m_500_w_125p0.label}, res",
    id=71108,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_125p0_int = hpseudo_tt_sl_m_500_w_125p0.add_process(
    name="hpseudo_tt_sl_m_500_w_125p0_int",
    label=rf"{hpseudo_tt_sl_m_500_w_125p0.label}, int",
    id=71109,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 25%

hpseudo_tt_sl_m_600_w_150p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_600_w_150p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 25\%$)",
    id=71110,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_150p0_res = hpseudo_tt_sl_m_600_w_150p0.add_process(
    name="hpseudo_tt_sl_m_600_w_150p0_res",
    label=rf"{hpseudo_tt_sl_m_600_w_150p0.label}, res",
    id=71111,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_150p0_int = hpseudo_tt_sl_m_600_w_150p0.add_process(
    name="hpseudo_tt_sl_m_600_w_150p0_int",
    label=rf"{hpseudo_tt_sl_m_600_w_150p0.label}, int",
    id=71112,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_200p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_800_w_200p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 25\%$)",
    id=71113,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_200p0_res = hpseudo_tt_sl_m_800_w_200p0.add_process(
    name="hpseudo_tt_sl_m_800_w_200p0_res",
    label=rf"{hpseudo_tt_sl_m_800_w_200p0.label}, res",
    id=71114,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_200p0_int = hpseudo_tt_sl_m_800_w_200p0.add_process(
    name="hpseudo_tt_sl_m_800_w_200p0_int",
    label=rf"{hpseudo_tt_sl_m_800_w_200p0.label}, int",
    id=71115,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_250p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_1000_w_250p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 25\%$)",
    id=71116,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_250p0_res = hpseudo_tt_sl_m_1000_w_250p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_250p0_res",
    label=rf"{hpseudo_tt_sl_m_1000_w_250p0.label}, res",
    id=71117,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_250p0_int = hpseudo_tt_sl_m_1000_w_250p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_250p0_int",
    label=rf"{hpseudo_tt_sl_m_1000_w_250p0.label}, int",
    id=71118,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

hpseudo_tt_sl_m_365_w_36p5 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_365_w_36p5",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 10\%$)",
    id=71119,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_36p5_res = hpseudo_tt_sl_m_365_w_36p5.add_process(
    name="hpseudo_tt_sl_m_365_w_36p5_res",
    label=rf"{hpseudo_tt_sl_m_365_w_36p5.label}, res",
    id=71120,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_36p5_int = hpseudo_tt_sl_m_365_w_36p5.add_process(
    name="hpseudo_tt_sl_m_365_w_36p5_int",
    label=rf"{hpseudo_tt_sl_m_365_w_36p5.label}, int",
    id=71121,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_40p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_400_w_40p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=71122,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_40p0_res = hpseudo_tt_sl_m_400_w_40p0.add_process(
    name="hpseudo_tt_sl_m_400_w_40p0_res",
    label=rf"{hpseudo_tt_sl_m_400_w_40p0.label}, res",
    id=71123,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_40p0_int = hpseudo_tt_sl_m_400_w_40p0.add_process(
    name="hpseudo_tt_sl_m_400_w_40p0_int",
    label=rf"{hpseudo_tt_sl_m_400_w_40p0.label}, int",
    id=71124,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_50p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_500_w_50p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=71125,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_50p0_res = hpseudo_tt_sl_m_500_w_50p0.add_process(
    name="hpseudo_tt_sl_m_500_w_50p0_res",
    label=rf"{hpseudo_tt_sl_m_500_w_50p0.label}, res",
    id=71126,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_50p0_int = hpseudo_tt_sl_m_500_w_50p0.add_process(
    name="hpseudo_tt_sl_m_500_w_50p0_int",
    label=rf"{hpseudo_tt_sl_m_500_w_50p0.label}, int",
    id=71127,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 10%

hpseudo_tt_sl_m_600_w_60p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_600_w_60p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=71128,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_60p0_res = hpseudo_tt_sl_m_600_w_60p0.add_process(
    name="hpseudo_tt_sl_m_600_w_60p0_res",
    label=rf"{hpseudo_tt_sl_m_600_w_60p0.label}, res",
    id=71129,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_60p0_int = hpseudo_tt_sl_m_600_w_60p0.add_process(
    name="hpseudo_tt_sl_m_600_w_60p0_int",
    label=rf"{hpseudo_tt_sl_m_600_w_60p0.label}, int",
    id=71130,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_80p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_800_w_80p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=71131,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_80p0_res = hpseudo_tt_sl_m_800_w_80p0.add_process(
    name="hpseudo_tt_sl_m_800_w_80p0_res",
    label=rf"{hpseudo_tt_sl_m_800_w_80p0.label}, res",
    id=71132,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_80p0_int = hpseudo_tt_sl_m_800_w_80p0.add_process(
    name="hpseudo_tt_sl_m_800_w_80p0_int",
    label=rf"{hpseudo_tt_sl_m_800_w_80p0.label}, int",
    id=71133,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_100p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_1000_w_100p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=71134,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_100p0_res = hpseudo_tt_sl_m_1000_w_100p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_100p0_res",
    label=rf"{hpseudo_tt_sl_m_1000_w_100p0.label}, res",
    id=71135,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_100p0_int = hpseudo_tt_sl_m_1000_w_100p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_100p0_int",
    label=rf"{hpseudo_tt_sl_m_1000_w_100p0.label}, int",
    id=71136,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 2.5%

hpseudo_tt_sl_m_365_w_9p125 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_365_w_9p125",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 2\%$)",
    id=71137,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_9p125_res = hpseudo_tt_sl_m_365_w_9p125.add_process(
    name="hpseudo_tt_sl_m_365_w_9p125_res",
    label=rf"{hpseudo_tt_sl_m_365_w_9p125.label}, res",
    id=71138,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_365_w_9p125_int = hpseudo_tt_sl_m_365_w_9p125.add_process(
    name="hpseudo_tt_sl_m_365_w_9p125_int",
    label=rf"{hpseudo_tt_sl_m_365_w_9p125.label}, int",
    id=71139,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_10p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_400_w_10p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 2\%$)",
    id=71140,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_10p0_res = hpseudo_tt_sl_m_400_w_10p0.add_process(
    name="hpseudo_tt_sl_m_400_w_10p0_res",
    label=rf"{hpseudo_tt_sl_m_400_w_10p0.label}, res",
    id=71141,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_400_w_10p0_int = hpseudo_tt_sl_m_400_w_10p0.add_process(
    name="hpseudo_tt_sl_m_400_w_10p0_int",
    label=rf"{hpseudo_tt_sl_m_400_w_10p0.label}, int",
    id=71142,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_12p5 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_500_w_12p5",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 2\%$)",
    id=71143,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_12p5_res = hpseudo_tt_sl_m_500_w_12p5.add_process(
    name="hpseudo_tt_sl_m_500_w_12p5_res",
    label=rf"{hpseudo_tt_sl_m_500_w_12p5.label}, res",
    id=71144,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_500_w_12p5_int = hpseudo_tt_sl_m_500_w_12p5.add_process(
    name="hpseudo_tt_sl_m_500_w_12p5_int",
    label=rf"{hpseudo_tt_sl_m_500_w_12p5.label}, int",
    id=71145,
    xsecs={13: Number(0.1)},  # TODO
)

# width / mass = 2.5%

hpseudo_tt_sl_m_600_w_15p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_600_w_15p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 2\%$)",
    id=71146,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_15p0_res = hpseudo_tt_sl_m_600_w_15p0.add_process(
    name="hpseudo_tt_sl_m_600_w_15p0_res",
    label=rf"{hpseudo_tt_sl_m_600_w_15p0.label}, res",
    id=71147,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_600_w_15p0_int = hpseudo_tt_sl_m_600_w_15p0.add_process(
    name="hpseudo_tt_sl_m_600_w_15p0_int",
    label=rf"{hpseudo_tt_sl_m_600_w_15p0.label}, int",
    id=71148,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_20p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_800_w_20p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 2\%$)",
    id=71149,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_20p0_res = hpseudo_tt_sl_m_800_w_20p0.add_process(
    name="hpseudo_tt_sl_m_800_w_20p0_res",
    label=rf"{hpseudo_tt_sl_m_800_w_20p0.label}, res",
    id=71150,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_800_w_20p0_int = hpseudo_tt_sl_m_800_w_20p0.add_process(
    name="hpseudo_tt_sl_m_800_w_20p0_int",
    label=rf"{hpseudo_tt_sl_m_800_w_20p0.label}, int",
    id=71151,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_25p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m_1000_w_25p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 2\%$)",
    id=71152,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_25p0_res = hpseudo_tt_sl_m_1000_w_25p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_25p0_res",
    label=rf"{hpseudo_tt_sl_m_1000_w_25p0.label}, res",
    id=71153,
    xsecs={13: Number(0.1)},  # TODO
)

hpseudo_tt_sl_m_1000_w_25p0_int = hpseudo_tt_sl_m_1000_w_25p0.add_process(
    name="hpseudo_tt_sl_m_1000_w_25p0_int",
    label=rf"{hpseudo_tt_sl_m_1000_w_25p0.label}, int",
    id=71154,
    xsecs={13: Number(0.1)},  # TODO
)


#
# Kaluza-Klein gluon
#

rsgluon_tt = Process(
    name="rsgluon_tt",
    label=r"$g_\mathrm{KK}$",
    id=80000,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_500",
    label=rf"{rsgluon_tt.label} ($m = 500$ GeV)",
    id=80001,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_1000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_1000",
    label=rf"{rsgluon_tt.label} ($m = 1000$ GeV)",
    id=80002,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_1500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_1500",
    label=rf"{rsgluon_tt.label} ($m = 1500$ GeV)",
    id=80003,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_2000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_2000",
    label=rf"{rsgluon_tt.label} ($m = 2000$ GeV)",
    id=80004,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_2500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_2500",
    label=rf"{rsgluon_tt.label} ($m = 2500$ GeV)",
    id=80005,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_3000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_3000",
    label=rf"{rsgluon_tt.label} ($m = 3000$ GeV)",
    id=80006,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_3500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_3500",
    label=rf"{rsgluon_tt.label} ($m = 3500$ GeV)",
    id=80007,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_4000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_4000",
    label=rf"{rsgluon_tt.label} ($m = 4000$ GeV)",
    id=80008,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_4500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_4500",
    label=rf"{rsgluon_tt.label} ($m = 4500$ GeV)",
    id=80009,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_5000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_5000",
    label=rf"{rsgluon_tt.label} ($m = 5000$ GeV)",
    id=80010,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_5500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_5500",
    label=rf"{rsgluon_tt.label} ($m = 5500$ GeV)",
    id=80011,
    xsecs={13: Number(0.1)},  # TODO
)


rsgluon_tt_m_6000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m_6000",
    label=rf"{rsgluon_tt.label} ($m = 6000$ GeV)",
    id=80012,
    xsecs={13: Number(0.1)},  # TODO
)
