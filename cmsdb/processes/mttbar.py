# coding: utf-8

"""
m(ttbar) line search signal process definitions
"""

__all__ = [
    "zprime_tt",
    "zprime_tt_m400_w40",
    "zprime_tt_m400_w120",
    "zprime_tt_m400_w4",
    "zprime_tt_m500_w50",
    "zprime_tt_m500_w150",
    "zprime_tt_m500_w5",
    "zprime_tt_m600_w60",
    "zprime_tt_m600_w180",
    "zprime_tt_m600_w6",
    "zprime_tt_m700_w70",
    "zprime_tt_m700_w210",
    "zprime_tt_m700_w7",
    "zprime_tt_m800_w80",
    "zprime_tt_m800_w240",
    "zprime_tt_m800_w8",
    "zprime_tt_m900_w90",
    "zprime_tt_m900_w270",
    "zprime_tt_m900_w9",
    "zprime_tt_m1000_w100",
    "zprime_tt_m1000_w300",
    "zprime_tt_m1000_w10",
    "zprime_tt_m1200_w120",
    "zprime_tt_m1200_w360",
    "zprime_tt_m1200_w12",
    "zprime_tt_m1400_w140",
    "zprime_tt_m1400_w420",
    "zprime_tt_m1400_w14",
    "zprime_tt_m1600_w160",
    "zprime_tt_m1600_w480",
    "zprime_tt_m1600_w16",
    "zprime_tt_m1800_w180",
    "zprime_tt_m1800_w540",
    "zprime_tt_m1800_w18",
    "zprime_tt_m2000_w200",
    "zprime_tt_m2000_w600",
    "zprime_tt_m2000_w20",
    "zprime_tt_m2500_w250",
    "zprime_tt_m2500_w750",
    "zprime_tt_m2500_w25",
    "zprime_tt_m3000_w300",
    "zprime_tt_m3000_w900",
    "zprime_tt_m3000_w30",
    "zprime_tt_m3500_w350",
    "zprime_tt_m3500_w1050",
    "zprime_tt_m3500_w35",
    "zprime_tt_m4000_w400",
    "zprime_tt_m4000_w1200",
    "zprime_tt_m4000_w40",
    "zprime_tt_m4500_w450",
    "zprime_tt_m4500_w1350",
    "zprime_tt_m4500_w45",
    "zprime_tt_m5000_w500",
    "zprime_tt_m5000_w1500",
    "zprime_tt_m5000_w50",
    "zprime_tt_m6000_w600",
    "zprime_tt_m6000_w1800",
    "zprime_tt_m6000_w60",
    "zprime_tt_m7000_w700",
    "zprime_tt_m7000_w2100",
    "zprime_tt_m7000_w70",
    "zprime_tt_m8000_w800",
    "zprime_tt_m8000_w2400",
    "zprime_tt_m8000_w80",
    "zprime_tt_m9000_w900",
    "zprime_tt_m9000_w2700",
    "zprime_tt_m9000_w90",
    "hscalar_tt",
    "hscalar_tt_sl",
    "hscalar_tt_sl_m365_w91p25",
    "hscalar_tt_sl_m365_w91p25_res",
    "hscalar_tt_sl_m365_w91p25_int",
    "hscalar_tt_sl_m400_w100p0",
    "hscalar_tt_sl_m400_w100p0_res",
    "hscalar_tt_sl_m400_w100p0_int",
    "hscalar_tt_sl_m500_w125p0",
    "hscalar_tt_sl_m500_w125p0_res",
    "hscalar_tt_sl_m500_w125p0_int",
    "hscalar_tt_sl_m600_w150p0",
    "hscalar_tt_sl_m600_w150p0_res",
    "hscalar_tt_sl_m600_w150p0_int",
    "hscalar_tt_sl_m800_w200p0",
    "hscalar_tt_sl_m800_w200p0_res",
    "hscalar_tt_sl_m800_w200p0_int",
    "hscalar_tt_sl_m1000_w250p0",
    "hscalar_tt_sl_m1000_w250p0_res",
    "hscalar_tt_sl_m1000_w250p0_int",
    "hscalar_tt_sl_m365_w36p5",
    "hscalar_tt_sl_m365_w36p5_res",
    "hscalar_tt_sl_m365_w36p5_int",
    "hscalar_tt_sl_m400_w40p0",
    "hscalar_tt_sl_m400_w40p0_res",
    "hscalar_tt_sl_m400_w40p0_int",
    "hscalar_tt_sl_m500_w50p0",
    "hscalar_tt_sl_m500_w50p0_res",
    "hscalar_tt_sl_m500_w50p0_int",
    "hscalar_tt_sl_m600_w60p0",
    "hscalar_tt_sl_m600_w60p0_res",
    "hscalar_tt_sl_m600_w60p0_int",
    "hscalar_tt_sl_m800_w80p0",
    "hscalar_tt_sl_m800_w80p0_res",
    "hscalar_tt_sl_m800_w80p0_int",
    "hscalar_tt_sl_m1000_w100p0",
    "hscalar_tt_sl_m1000_w100p0_res",
    "hscalar_tt_sl_m1000_w100p0_int",
    "hscalar_tt_sl_m365_w9p125",
    "hscalar_tt_sl_m365_w9p125_res",
    "hscalar_tt_sl_m365_w9p125_int",
    "hscalar_tt_sl_m400_w10p0",
    "hscalar_tt_sl_m400_w10p0_res",
    "hscalar_tt_sl_m400_w10p0_int",
    "hscalar_tt_sl_m500_w12p5",
    "hscalar_tt_sl_m500_w12p5_res",
    "hscalar_tt_sl_m500_w12p5_int",
    "hscalar_tt_sl_m600_w15p0",
    "hscalar_tt_sl_m600_w15p0_res",
    "hscalar_tt_sl_m600_w15p0_int",
    "hscalar_tt_sl_m800_w20p0",
    "hscalar_tt_sl_m800_w20p0_res",
    "hscalar_tt_sl_m800_w20p0_int",
    "hscalar_tt_sl_m1000_w25p0",
    "hscalar_tt_sl_m1000_w25p0_res",
    "hscalar_tt_sl_m1000_w25p0_int",
    "hpseudo_tt",
    "hpseudo_tt_sl",
    "hpseudo_tt_sl_m365_w91p25",
    "hpseudo_tt_sl_m365_w91p25_res",
    "hpseudo_tt_sl_m365_w91p25_int",
    "hpseudo_tt_sl_m400_w100p0",
    "hpseudo_tt_sl_m400_w100p0_res",
    "hpseudo_tt_sl_m400_w100p0_int",
    "hpseudo_tt_sl_m500_w125p0",
    "hpseudo_tt_sl_m500_w125p0_res",
    "hpseudo_tt_sl_m500_w125p0_int",
    "hpseudo_tt_sl_m600_w150p0",
    "hpseudo_tt_sl_m600_w150p0_res",
    "hpseudo_tt_sl_m600_w150p0_int",
    "hpseudo_tt_sl_m800_w200p0",
    "hpseudo_tt_sl_m800_w200p0_res",
    "hpseudo_tt_sl_m800_w200p0_int",
    "hpseudo_tt_sl_m1000_w250p0",
    "hpseudo_tt_sl_m1000_w250p0_res",
    "hpseudo_tt_sl_m1000_w250p0_int",
    "hpseudo_tt_sl_m365_w36p5",
    "hpseudo_tt_sl_m365_w36p5_res",
    "hpseudo_tt_sl_m365_w36p5_int",
    "hpseudo_tt_sl_m400_w40p0",
    "hpseudo_tt_sl_m400_w40p0_res",
    "hpseudo_tt_sl_m400_w40p0_int",
    "hpseudo_tt_sl_m500_w50p0",
    "hpseudo_tt_sl_m500_w50p0_res",
    "hpseudo_tt_sl_m500_w50p0_int",
    "hpseudo_tt_sl_m600_w60p0",
    "hpseudo_tt_sl_m600_w60p0_res",
    "hpseudo_tt_sl_m600_w60p0_int",
    "hpseudo_tt_sl_m800_w80p0",
    "hpseudo_tt_sl_m800_w80p0_res",
    "hpseudo_tt_sl_m800_w80p0_int",
    "hpseudo_tt_sl_m1000_w100p0",
    "hpseudo_tt_sl_m1000_w100p0_res",
    "hpseudo_tt_sl_m1000_w100p0_int",
    "hpseudo_tt_sl_m365_w9p125",
    "hpseudo_tt_sl_m365_w9p125_res",
    "hpseudo_tt_sl_m365_w9p125_int",
    "hpseudo_tt_sl_m400_w10p0",
    "hpseudo_tt_sl_m400_w10p0_res",
    "hpseudo_tt_sl_m400_w10p0_int",
    "hpseudo_tt_sl_m500_w12p5",
    "hpseudo_tt_sl_m500_w12p5_res",
    "hpseudo_tt_sl_m500_w12p5_int",
    "hpseudo_tt_sl_m600_w15p0",
    "hpseudo_tt_sl_m600_w15p0_res",
    "hpseudo_tt_sl_m600_w15p0_int",
    "hpseudo_tt_sl_m800_w20p0",
    "hpseudo_tt_sl_m800_w20p0_res",
    "hpseudo_tt_sl_m800_w20p0_int",
    "hpseudo_tt_sl_m1000_w25p0",
    "hpseudo_tt_sl_m1000_w25p0_res",
    "hpseudo_tt_sl_m1000_w25p0_int",
    "rsgluon_tt",
    "rsgluon_tt_m500",
    "rsgluon_tt_m1000",
    "rsgluon_tt_m1500",
    "rsgluon_tt_m2000",
    "rsgluon_tt_m2500",
    "rsgluon_tt_m3000",
    "rsgluon_tt_m3500",
    "rsgluon_tt_m4000",
    "rsgluon_tt_m4500",
    "rsgluon_tt_m5000",
    "rsgluon_tt_m5500",
    "rsgluon_tt_m6000",
]

from order import Process


#
# Z prime
#

zprime = Process(
    name="zprime",
    label=r"Z'",
    id=60000,
)


zprime_tt = zprime.add_process(
    name="zprime_tt",
    label=rf"{zprime.label} $\rightarrow t\bar{{t}}$",
    id=61000,
)

# width / mass = 10%

zprime_tt_m400_w40 = zprime_tt.add_process(
    name="zprime_tt_m400_w40",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=61001,
)


zprime_tt_m400_w120 = zprime_tt.add_process(
    name="zprime_tt_m400_w120",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 30\%$)",
    id=61002,
)


zprime_tt_m400_w4 = zprime_tt.add_process(
    name="zprime_tt_m400_w4",
    label=rf"{zprime_tt.label} ($m = 400$ GeV, $\Gamma/m = 1\%$)",
    id=61003,
)

# width / mass = 10%

zprime_tt_m500_w50 = zprime_tt.add_process(
    name="zprime_tt_m500_w50",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=61004,
)


zprime_tt_m500_w150 = zprime_tt.add_process(
    name="zprime_tt_m500_w150",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 30\%$)",
    id=61005,
)


zprime_tt_m500_w5 = zprime_tt.add_process(
    name="zprime_tt_m500_w5",
    label=rf"{zprime_tt.label} ($m = 500$ GeV, $\Gamma/m = 1\%$)",
    id=61006,
)

# width / mass = 10%

zprime_tt_m600_w60 = zprime_tt.add_process(
    name="zprime_tt_m600_w60",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=61007,
)


zprime_tt_m600_w180 = zprime_tt.add_process(
    name="zprime_tt_m600_w180",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 30\%$)",
    id=61008,
)


zprime_tt_m600_w6 = zprime_tt.add_process(
    name="zprime_tt_m600_w6",
    label=rf"{zprime_tt.label} ($m = 600$ GeV, $\Gamma/m = 1\%$)",
    id=61009,
)

# width / mass = 10%

zprime_tt_m700_w70 = zprime_tt.add_process(
    name="zprime_tt_m700_w70",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 10\%$)",
    id=61010,
)


zprime_tt_m700_w210 = zprime_tt.add_process(
    name="zprime_tt_m700_w210",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 30\%$)",
    id=61011,
)


zprime_tt_m700_w7 = zprime_tt.add_process(
    name="zprime_tt_m700_w7",
    label=rf"{zprime_tt.label} ($m = 700$ GeV, $\Gamma/m = 1\%$)",
    id=61012,
)

# width / mass = 10%

zprime_tt_m800_w80 = zprime_tt.add_process(
    name="zprime_tt_m800_w80",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=61013,
)


zprime_tt_m800_w240 = zprime_tt.add_process(
    name="zprime_tt_m800_w240",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 30\%$)",
    id=61014,
)


zprime_tt_m800_w8 = zprime_tt.add_process(
    name="zprime_tt_m800_w8",
    label=rf"{zprime_tt.label} ($m = 800$ GeV, $\Gamma/m = 1\%$)",
    id=61015,
)

# width / mass = 10%

zprime_tt_m900_w90 = zprime_tt.add_process(
    name="zprime_tt_m900_w90",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 10\%$)",
    id=61016,
)


zprime_tt_m900_w270 = zprime_tt.add_process(
    name="zprime_tt_m900_w270",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 30\%$)",
    id=61017,
)


zprime_tt_m900_w9 = zprime_tt.add_process(
    name="zprime_tt_m900_w9",
    label=rf"{zprime_tt.label} ($m = 900$ GeV, $\Gamma/m = 1\%$)",
    id=61018,
)

# width / mass = 10%

zprime_tt_m1000_w100 = zprime_tt.add_process(
    name="zprime_tt_m1000_w100",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=61019,
)


zprime_tt_m1000_w300 = zprime_tt.add_process(
    name="zprime_tt_m1000_w300",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 30\%$)",
    id=61020,
)


zprime_tt_m1000_w10 = zprime_tt.add_process(
    name="zprime_tt_m1000_w10",
    label=rf"{zprime_tt.label} ($m = 1000$ GeV, $\Gamma/m = 1\%$)",
    id=61021,
)

# width / mass = 10%

zprime_tt_m1200_w120 = zprime_tt.add_process(
    name="zprime_tt_m1200_w120",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 10\%$)",
    id=61022,
)


zprime_tt_m1200_w360 = zprime_tt.add_process(
    name="zprime_tt_m1200_w360",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 30\%$)",
    id=61023,
)


zprime_tt_m1200_w12 = zprime_tt.add_process(
    name="zprime_tt_m1200_w12",
    label=rf"{zprime_tt.label} ($m = 1200$ GeV, $\Gamma/m = 1\%$)",
    id=61024,
)

# width / mass = 10%

zprime_tt_m1400_w140 = zprime_tt.add_process(
    name="zprime_tt_m1400_w140",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 10\%$)",
    id=61025,
)


zprime_tt_m1400_w420 = zprime_tt.add_process(
    name="zprime_tt_m1400_w420",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 30\%$)",
    id=61026,
)


zprime_tt_m1400_w14 = zprime_tt.add_process(
    name="zprime_tt_m1400_w14",
    label=rf"{zprime_tt.label} ($m = 1400$ GeV, $\Gamma/m = 1\%$)",
    id=61027,
)

# width / mass = 10%

zprime_tt_m1600_w160 = zprime_tt.add_process(
    name="zprime_tt_m1600_w160",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 10\%$)",
    id=61028,
)


zprime_tt_m1600_w480 = zprime_tt.add_process(
    name="zprime_tt_m1600_w480",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 30\%$)",
    id=61029,
)


zprime_tt_m1600_w16 = zprime_tt.add_process(
    name="zprime_tt_m1600_w16",
    label=rf"{zprime_tt.label} ($m = 1600$ GeV, $\Gamma/m = 1\%$)",
    id=61030,
)

# width / mass = 10%

zprime_tt_m1800_w180 = zprime_tt.add_process(
    name="zprime_tt_m1800_w180",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 10\%$)",
    id=61031,
)


zprime_tt_m1800_w540 = zprime_tt.add_process(
    name="zprime_tt_m1800_w540",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 30\%$)",
    id=61032,
)


zprime_tt_m1800_w18 = zprime_tt.add_process(
    name="zprime_tt_m1800_w18",
    label=rf"{zprime_tt.label} ($m = 1800$ GeV, $\Gamma/m = 1\%$)",
    id=61033,
)

# width / mass = 10%

zprime_tt_m2000_w200 = zprime_tt.add_process(
    name="zprime_tt_m2000_w200",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 10\%$)",
    id=61034,
)


zprime_tt_m2000_w600 = zprime_tt.add_process(
    name="zprime_tt_m2000_w600",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 30\%$)",
    id=61035,
)


zprime_tt_m2000_w20 = zprime_tt.add_process(
    name="zprime_tt_m2000_w20",
    label=rf"{zprime_tt.label} ($m = 2000$ GeV, $\Gamma/m = 1\%$)",
    id=61036,
)

# width / mass = 10%

zprime_tt_m2500_w250 = zprime_tt.add_process(
    name="zprime_tt_m2500_w250",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 10\%$)",
    id=61037,
)


zprime_tt_m2500_w750 = zprime_tt.add_process(
    name="zprime_tt_m2500_w750",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 30\%$)",
    id=61038,
)


zprime_tt_m2500_w25 = zprime_tt.add_process(
    name="zprime_tt_m2500_w25",
    label=rf"{zprime_tt.label} ($m = 2500$ GeV, $\Gamma/m = 1\%$)",
    id=61039,
)

# width / mass = 10%

zprime_tt_m3000_w300 = zprime_tt.add_process(
    name="zprime_tt_m3000_w300",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 10\%$)",
    id=61040,
)


zprime_tt_m3000_w900 = zprime_tt.add_process(
    name="zprime_tt_m3000_w900",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 30\%$)",
    id=61041,
)


zprime_tt_m3000_w30 = zprime_tt.add_process(
    name="zprime_tt_m3000_w30",
    label=rf"{zprime_tt.label} ($m = 3000$ GeV, $\Gamma/m = 1\%$)",
    id=61042,
)

# width / mass = 10%

zprime_tt_m3500_w350 = zprime_tt.add_process(
    name="zprime_tt_m3500_w350",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 10\%$)",
    id=61043,
)


zprime_tt_m3500_w1050 = zprime_tt.add_process(
    name="zprime_tt_m3500_w1050",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 30\%$)",
    id=61044,
)


zprime_tt_m3500_w35 = zprime_tt.add_process(
    name="zprime_tt_m3500_w35",
    label=rf"{zprime_tt.label} ($m = 3500$ GeV, $\Gamma/m = 1\%$)",
    id=61045,
)

# width / mass = 10%

zprime_tt_m4000_w400 = zprime_tt.add_process(
    name="zprime_tt_m4000_w400",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 10\%$)",
    id=61046,
)


zprime_tt_m4000_w1200 = zprime_tt.add_process(
    name="zprime_tt_m4000_w1200",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 30\%$)",
    id=61047,
)


zprime_tt_m4000_w40 = zprime_tt.add_process(
    name="zprime_tt_m4000_w40",
    label=rf"{zprime_tt.label} ($m = 4000$ GeV, $\Gamma/m = 1\%$)",
    id=61048,
)

# width / mass = 10%

zprime_tt_m4500_w450 = zprime_tt.add_process(
    name="zprime_tt_m4500_w450",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 10\%$)",
    id=61049,
)


zprime_tt_m4500_w1350 = zprime_tt.add_process(
    name="zprime_tt_m4500_w1350",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 30\%$)",
    id=61050,
)


zprime_tt_m4500_w45 = zprime_tt.add_process(
    name="zprime_tt_m4500_w45",
    label=rf"{zprime_tt.label} ($m = 4500$ GeV, $\Gamma/m = 1\%$)",
    id=61051,
)

# width / mass = 10%

zprime_tt_m5000_w500 = zprime_tt.add_process(
    name="zprime_tt_m5000_w500",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 10\%$)",
    id=61052,
)


zprime_tt_m5000_w1500 = zprime_tt.add_process(
    name="zprime_tt_m5000_w1500",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 30\%$)",
    id=61053,
)


zprime_tt_m5000_w50 = zprime_tt.add_process(
    name="zprime_tt_m5000_w50",
    label=rf"{zprime_tt.label} ($m = 5000$ GeV, $\Gamma/m = 1\%$)",
    id=61054,
)

# width / mass = 10%

zprime_tt_m6000_w600 = zprime_tt.add_process(
    name="zprime_tt_m6000_w600",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 10\%$)",
    id=61055,
)


zprime_tt_m6000_w1800 = zprime_tt.add_process(
    name="zprime_tt_m6000_w1800",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 30\%$)",
    id=61056,
)


zprime_tt_m6000_w60 = zprime_tt.add_process(
    name="zprime_tt_m6000_w60",
    label=rf"{zprime_tt.label} ($m = 6000$ GeV, $\Gamma/m = 1\%$)",
    id=61057,
)

# width / mass = 10%

zprime_tt_m7000_w700 = zprime_tt.add_process(
    name="zprime_tt_m7000_w700",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 10\%$)",
    id=61058,
)


zprime_tt_m7000_w2100 = zprime_tt.add_process(
    name="zprime_tt_m7000_w2100",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 30\%$)",
    id=61059,
)


zprime_tt_m7000_w70 = zprime_tt.add_process(
    name="zprime_tt_m7000_w70",
    label=rf"{zprime_tt.label} ($m = 7000$ GeV, $\Gamma/m = 1\%$)",
    id=61060,
)

# width / mass = 10%

zprime_tt_m8000_w800 = zprime_tt.add_process(
    name="zprime_tt_m8000_w800",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 10\%$)",
    id=61061,
)


zprime_tt_m8000_w2400 = zprime_tt.add_process(
    name="zprime_tt_m8000_w2400",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 30\%$)",
    id=61062,
)


zprime_tt_m8000_w80 = zprime_tt.add_process(
    name="zprime_tt_m8000_w80",
    label=rf"{zprime_tt.label} ($m = 8000$ GeV, $\Gamma/m = 1\%$)",
    id=61063,
)

# width / mass = 10%

zprime_tt_m9000_w900 = zprime_tt.add_process(
    name="zprime_tt_m9000_w900",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 10\%$)",
    id=61064,
)


zprime_tt_m9000_w2700 = zprime_tt.add_process(
    name="zprime_tt_m9000_w2700",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 30\%$)",
    id=61065,
)


zprime_tt_m9000_w90 = zprime_tt.add_process(
    name="zprime_tt_m9000_w90",
    label=rf"{zprime_tt.label} ($m = 9000$ GeV, $\Gamma/m = 1\%$)",
    id=61066,
)


#
# Scalar heavy Higgs
#

hscalar_tt = Process(
    name="hscalar_tt",
    label=r"H $\rightarrow t\bar{t}$",
    id=70000,
)


hscalar_tt_sl = hscalar_tt.add_process(
    name="hscalar_tt_sl",
    label=rf"{hscalar_tt.label} $\rightarrow \ell\nu + \mathrm{{jets}}$",
    id=70100,
)

# width / mass = 25%

hscalar_tt_sl_m365_w91p25 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m365_w91p25",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 25\%$)",
    id=70101,
)

hscalar_tt_sl_m365_w91p25_res = hscalar_tt_sl_m365_w91p25.add_process(
    name="hscalar_tt_sl_m365_w91p25_res",
    label=rf"{hscalar_tt_sl_m365_w91p25.label}, res",
    id=70102,
)

hscalar_tt_sl_m365_w91p25_int = hscalar_tt_sl_m365_w91p25.add_process(
    name="hscalar_tt_sl_m365_w91p25_int",
    label=rf"{hscalar_tt_sl_m365_w91p25.label}, int",
    id=70103,
)

hscalar_tt_sl_m400_w100p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m400_w100p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 25\%$)",
    id=70104,
)

hscalar_tt_sl_m400_w100p0_res = hscalar_tt_sl_m400_w100p0.add_process(
    name="hscalar_tt_sl_m400_w100p0_res",
    label=rf"{hscalar_tt_sl_m400_w100p0.label}, res",
    id=70105,
)

hscalar_tt_sl_m400_w100p0_int = hscalar_tt_sl_m400_w100p0.add_process(
    name="hscalar_tt_sl_m400_w100p0_int",
    label=rf"{hscalar_tt_sl_m400_w100p0.label}, int",
    id=70106,
)

hscalar_tt_sl_m500_w125p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m500_w125p0",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 25\%$)",
    id=70107,
)

hscalar_tt_sl_m500_w125p0_res = hscalar_tt_sl_m500_w125p0.add_process(
    name="hscalar_tt_sl_m500_w125p0_res",
    label=rf"{hscalar_tt_sl_m500_w125p0.label}, res",
    id=70108,
)

hscalar_tt_sl_m500_w125p0_int = hscalar_tt_sl_m500_w125p0.add_process(
    name="hscalar_tt_sl_m500_w125p0_int",
    label=rf"{hscalar_tt_sl_m500_w125p0.label}, int",
    id=70109,
)

# width / mass = 25%

hscalar_tt_sl_m600_w150p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m600_w150p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 25\%$)",
    id=70110,
)

hscalar_tt_sl_m600_w150p0_res = hscalar_tt_sl_m600_w150p0.add_process(
    name="hscalar_tt_sl_m600_w150p0_res",
    label=rf"{hscalar_tt_sl_m600_w150p0.label}, res",
    id=70111,
)

hscalar_tt_sl_m600_w150p0_int = hscalar_tt_sl_m600_w150p0.add_process(
    name="hscalar_tt_sl_m600_w150p0_int",
    label=rf"{hscalar_tt_sl_m600_w150p0.label}, int",
    id=70112,
)

hscalar_tt_sl_m800_w200p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m800_w200p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 25\%$)",
    id=70113,
)

hscalar_tt_sl_m800_w200p0_res = hscalar_tt_sl_m800_w200p0.add_process(
    name="hscalar_tt_sl_m800_w200p0_res",
    label=rf"{hscalar_tt_sl_m800_w200p0.label}, res",
    id=70114,
)

hscalar_tt_sl_m800_w200p0_int = hscalar_tt_sl_m800_w200p0.add_process(
    name="hscalar_tt_sl_m800_w200p0_int",
    label=rf"{hscalar_tt_sl_m800_w200p0.label}, int",
    id=70115,
)

hscalar_tt_sl_m1000_w250p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m1000_w250p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 25\%$)",
    id=70116,
)

hscalar_tt_sl_m1000_w250p0_res = hscalar_tt_sl_m1000_w250p0.add_process(
    name="hscalar_tt_sl_m1000_w250p0_res",
    label=rf"{hscalar_tt_sl_m1000_w250p0.label}, res",
    id=70117,
)

hscalar_tt_sl_m1000_w250p0_int = hscalar_tt_sl_m1000_w250p0.add_process(
    name="hscalar_tt_sl_m1000_w250p0_int",
    label=rf"{hscalar_tt_sl_m1000_w250p0.label}, int",
    id=70118,
)

# width / mass = 10%

hscalar_tt_sl_m365_w36p5 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m365_w36p5",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 10\%$)",
    id=70119,
)

hscalar_tt_sl_m365_w36p5_res = hscalar_tt_sl_m365_w36p5.add_process(
    name="hscalar_tt_sl_m365_w36p5_res",
    label=rf"{hscalar_tt_sl_m365_w36p5.label}, res",
    id=70120,
)

hscalar_tt_sl_m365_w36p5_int = hscalar_tt_sl_m365_w36p5.add_process(
    name="hscalar_tt_sl_m365_w36p5_int",
    label=rf"{hscalar_tt_sl_m365_w36p5.label}, int",
    id=70121,
)

hscalar_tt_sl_m400_w40p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m400_w40p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=70122,
)

hscalar_tt_sl_m400_w40p0_res = hscalar_tt_sl_m400_w40p0.add_process(
    name="hscalar_tt_sl_m400_w40p0_res",
    label=rf"{hscalar_tt_sl_m400_w40p0.label}, res",
    id=70123,
)

hscalar_tt_sl_m400_w40p0_int = hscalar_tt_sl_m400_w40p0.add_process(
    name="hscalar_tt_sl_m400_w40p0_int",
    label=rf"{hscalar_tt_sl_m400_w40p0.label}, int",
    id=70124,
)

hscalar_tt_sl_m500_w50p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m500_w50p0",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=70125,
)

hscalar_tt_sl_m500_w50p0_res = hscalar_tt_sl_m500_w50p0.add_process(
    name="hscalar_tt_sl_m500_w50p0_res",
    label=rf"{hscalar_tt_sl_m500_w50p0.label}, res",
    id=70126,
)

hscalar_tt_sl_m500_w50p0_int = hscalar_tt_sl_m500_w50p0.add_process(
    name="hscalar_tt_sl_m500_w50p0_int",
    label=rf"{hscalar_tt_sl_m500_w50p0.label}, int",
    id=70127,
)

# width / mass = 10%

hscalar_tt_sl_m600_w60p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m600_w60p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=70128,
)

hscalar_tt_sl_m600_w60p0_res = hscalar_tt_sl_m600_w60p0.add_process(
    name="hscalar_tt_sl_m600_w60p0_res",
    label=rf"{hscalar_tt_sl_m600_w60p0.label}, res",
    id=70129,
)

hscalar_tt_sl_m600_w60p0_int = hscalar_tt_sl_m600_w60p0.add_process(
    name="hscalar_tt_sl_m600_w60p0_int",
    label=rf"{hscalar_tt_sl_m600_w60p0.label}, int",
    id=70130,
)

hscalar_tt_sl_m800_w80p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m800_w80p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=70131,
)

hscalar_tt_sl_m800_w80p0_res = hscalar_tt_sl_m800_w80p0.add_process(
    name="hscalar_tt_sl_m800_w80p0_res",
    label=rf"{hscalar_tt_sl_m800_w80p0.label}, res",
    id=70132,
)

hscalar_tt_sl_m800_w80p0_int = hscalar_tt_sl_m800_w80p0.add_process(
    name="hscalar_tt_sl_m800_w80p0_int",
    label=rf"{hscalar_tt_sl_m800_w80p0.label}, int",
    id=70133,
)

hscalar_tt_sl_m1000_w100p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m1000_w100p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=70134,
)

hscalar_tt_sl_m1000_w100p0_res = hscalar_tt_sl_m1000_w100p0.add_process(
    name="hscalar_tt_sl_m1000_w100p0_res",
    label=rf"{hscalar_tt_sl_m1000_w100p0.label}, res",
    id=70135,
)

hscalar_tt_sl_m1000_w100p0_int = hscalar_tt_sl_m1000_w100p0.add_process(
    name="hscalar_tt_sl_m1000_w100p0_int",
    label=rf"{hscalar_tt_sl_m1000_w100p0.label}, int",
    id=70136,
)

# width / mass = 2.5%

hscalar_tt_sl_m365_w9p125 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m365_w9p125",
    label=rf"{hscalar_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 2\%$)",
    id=70137,
)

hscalar_tt_sl_m365_w9p125_res = hscalar_tt_sl_m365_w9p125.add_process(
    name="hscalar_tt_sl_m365_w9p125_res",
    label=rf"{hscalar_tt_sl_m365_w9p125.label}, res",
    id=70138,
)

hscalar_tt_sl_m365_w9p125_int = hscalar_tt_sl_m365_w9p125.add_process(
    name="hscalar_tt_sl_m365_w9p125_int",
    label=rf"{hscalar_tt_sl_m365_w9p125.label}, int",
    id=70139,
)

hscalar_tt_sl_m400_w10p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m400_w10p0",
    label=rf"{hscalar_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 2\%$)",
    id=70140,
)

hscalar_tt_sl_m400_w10p0_res = hscalar_tt_sl_m400_w10p0.add_process(
    name="hscalar_tt_sl_m400_w10p0_res",
    label=rf"{hscalar_tt_sl_m400_w10p0.label}, res",
    id=70141,
)

hscalar_tt_sl_m400_w10p0_int = hscalar_tt_sl_m400_w10p0.add_process(
    name="hscalar_tt_sl_m400_w10p0_int",
    label=rf"{hscalar_tt_sl_m400_w10p0.label}, int",
    id=70142,
)

hscalar_tt_sl_m500_w12p5 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m500_w12p5",
    label=rf"{hscalar_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 2\%$)",
    id=70143,
)

hscalar_tt_sl_m500_w12p5_res = hscalar_tt_sl_m500_w12p5.add_process(
    name="hscalar_tt_sl_m500_w12p5_res",
    label=rf"{hscalar_tt_sl_m500_w12p5.label}, res",
    id=70144,
)

hscalar_tt_sl_m500_w12p5_int = hscalar_tt_sl_m500_w12p5.add_process(
    name="hscalar_tt_sl_m500_w12p5_int",
    label=rf"{hscalar_tt_sl_m500_w12p5.label}, int",
    id=70145,
)

# width / mass = 2.5%

hscalar_tt_sl_m600_w15p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m600_w15p0",
    label=rf"{hscalar_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 2\%$)",
    id=70146,
)

hscalar_tt_sl_m600_w15p0_res = hscalar_tt_sl_m600_w15p0.add_process(
    name="hscalar_tt_sl_m600_w15p0_res",
    label=rf"{hscalar_tt_sl_m600_w15p0.label}, res",
    id=70147,
)

hscalar_tt_sl_m600_w15p0_int = hscalar_tt_sl_m600_w15p0.add_process(
    name="hscalar_tt_sl_m600_w15p0_int",
    label=rf"{hscalar_tt_sl_m600_w15p0.label}, int",
    id=70148,
)

hscalar_tt_sl_m800_w20p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m800_w20p0",
    label=rf"{hscalar_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 2\%$)",
    id=70149,
)

hscalar_tt_sl_m800_w20p0_res = hscalar_tt_sl_m800_w20p0.add_process(
    name="hscalar_tt_sl_m800_w20p0_res",
    label=rf"{hscalar_tt_sl_m800_w20p0.label}, res",
    id=70150,
)

hscalar_tt_sl_m800_w20p0_int = hscalar_tt_sl_m800_w20p0.add_process(
    name="hscalar_tt_sl_m800_w20p0_int",
    label=rf"{hscalar_tt_sl_m800_w20p0.label}, int",
    id=70151,
)

hscalar_tt_sl_m1000_w25p0 = hscalar_tt_sl.add_process(
    name="hscalar_tt_sl_m1000_w25p0",
    label=rf"{hscalar_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 2\%$)",
    id=70152,
)

hscalar_tt_sl_m1000_w25p0_res = hscalar_tt_sl_m1000_w25p0.add_process(
    name="hscalar_tt_sl_m1000_w25p0_res",
    label=rf"{hscalar_tt_sl_m1000_w25p0.label}, res",
    id=70153,
)

hscalar_tt_sl_m1000_w25p0_int = hscalar_tt_sl_m1000_w25p0.add_process(
    name="hscalar_tt_sl_m1000_w25p0_int",
    label=rf"{hscalar_tt_sl_m1000_w25p0.label}, int",
    id=70154,
)


#
# Pseudoscalar heavy Higgs
#

hpseudo_tt = Process(
    name="hpseudo_tt",
    label=r"A $\rightarrow t\bar{t}$",
    id=71000,
)

hpseudo_tt_sl = hpseudo_tt.add_process(
    name="hpseudo_tt_sl",
    label=rf"{hpseudo_tt.label} $\rightarrow \ell\nu + \mathrm{{jets}}$",
    id=71100,
)

# width / mass = 25%

hpseudo_tt_sl_m365_w91p25 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m365_w91p25",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 25\%$)",
    id=71101,
)

hpseudo_tt_sl_m365_w91p25_res = hpseudo_tt_sl_m365_w91p25.add_process(
    name="hpseudo_tt_sl_m365_w91p25_res",
    label=rf"{hpseudo_tt_sl_m365_w91p25.label}, res",
    id=71102,
)

hpseudo_tt_sl_m365_w91p25_int = hpseudo_tt_sl_m365_w91p25.add_process(
    name="hpseudo_tt_sl_m365_w91p25_int",
    label=rf"{hpseudo_tt_sl_m365_w91p25.label}, int",
    id=71103,
)

hpseudo_tt_sl_m400_w100p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m400_w100p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 25\%$)",
    id=71104,
)

hpseudo_tt_sl_m400_w100p0_res = hpseudo_tt_sl_m400_w100p0.add_process(
    name="hpseudo_tt_sl_m400_w100p0_res",
    label=rf"{hpseudo_tt_sl_m400_w100p0.label}, res",
    id=71105,
)

hpseudo_tt_sl_m400_w100p0_int = hpseudo_tt_sl_m400_w100p0.add_process(
    name="hpseudo_tt_sl_m400_w100p0_int",
    label=rf"{hpseudo_tt_sl_m400_w100p0.label}, int",
    id=71106,
)

hpseudo_tt_sl_m500_w125p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m500_w125p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 25\%$)",
    id=71107,
)

hpseudo_tt_sl_m500_w125p0_res = hpseudo_tt_sl_m500_w125p0.add_process(
    name="hpseudo_tt_sl_m500_w125p0_res",
    label=rf"{hpseudo_tt_sl_m500_w125p0.label}, res",
    id=71108,
)

hpseudo_tt_sl_m500_w125p0_int = hpseudo_tt_sl_m500_w125p0.add_process(
    name="hpseudo_tt_sl_m500_w125p0_int",
    label=rf"{hpseudo_tt_sl_m500_w125p0.label}, int",
    id=71109,
)

# width / mass = 25%

hpseudo_tt_sl_m600_w150p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m600_w150p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 25\%$)",
    id=71110,
)

hpseudo_tt_sl_m600_w150p0_res = hpseudo_tt_sl_m600_w150p0.add_process(
    name="hpseudo_tt_sl_m600_w150p0_res",
    label=rf"{hpseudo_tt_sl_m600_w150p0.label}, res",
    id=71111,
)

hpseudo_tt_sl_m600_w150p0_int = hpseudo_tt_sl_m600_w150p0.add_process(
    name="hpseudo_tt_sl_m600_w150p0_int",
    label=rf"{hpseudo_tt_sl_m600_w150p0.label}, int",
    id=71112,
)

hpseudo_tt_sl_m800_w200p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m800_w200p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 25\%$)",
    id=71113,
)

hpseudo_tt_sl_m800_w200p0_res = hpseudo_tt_sl_m800_w200p0.add_process(
    name="hpseudo_tt_sl_m800_w200p0_res",
    label=rf"{hpseudo_tt_sl_m800_w200p0.label}, res",
    id=71114,
)

hpseudo_tt_sl_m800_w200p0_int = hpseudo_tt_sl_m800_w200p0.add_process(
    name="hpseudo_tt_sl_m800_w200p0_int",
    label=rf"{hpseudo_tt_sl_m800_w200p0.label}, int",
    id=71115,
)

hpseudo_tt_sl_m1000_w250p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m1000_w250p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 25\%$)",
    id=71116,
)

hpseudo_tt_sl_m1000_w250p0_res = hpseudo_tt_sl_m1000_w250p0.add_process(
    name="hpseudo_tt_sl_m1000_w250p0_res",
    label=rf"{hpseudo_tt_sl_m1000_w250p0.label}, res",
    id=71117,
)

hpseudo_tt_sl_m1000_w250p0_int = hpseudo_tt_sl_m1000_w250p0.add_process(
    name="hpseudo_tt_sl_m1000_w250p0_int",
    label=rf"{hpseudo_tt_sl_m1000_w250p0.label}, int",
    id=71118,
)

# width / mass = 10%

hpseudo_tt_sl_m365_w36p5 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m365_w36p5",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 10\%$)",
    id=71119,
)

hpseudo_tt_sl_m365_w36p5_res = hpseudo_tt_sl_m365_w36p5.add_process(
    name="hpseudo_tt_sl_m365_w36p5_res",
    label=rf"{hpseudo_tt_sl_m365_w36p5.label}, res",
    id=71120,
)

hpseudo_tt_sl_m365_w36p5_int = hpseudo_tt_sl_m365_w36p5.add_process(
    name="hpseudo_tt_sl_m365_w36p5_int",
    label=rf"{hpseudo_tt_sl_m365_w36p5.label}, int",
    id=71121,
)

hpseudo_tt_sl_m400_w40p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m400_w40p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 10\%$)",
    id=71122,
)

hpseudo_tt_sl_m400_w40p0_res = hpseudo_tt_sl_m400_w40p0.add_process(
    name="hpseudo_tt_sl_m400_w40p0_res",
    label=rf"{hpseudo_tt_sl_m400_w40p0.label}, res",
    id=71123,
)

hpseudo_tt_sl_m400_w40p0_int = hpseudo_tt_sl_m400_w40p0.add_process(
    name="hpseudo_tt_sl_m400_w40p0_int",
    label=rf"{hpseudo_tt_sl_m400_w40p0.label}, int",
    id=71124,
)

hpseudo_tt_sl_m500_w50p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m500_w50p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 10\%$)",
    id=71125,
)

hpseudo_tt_sl_m500_w50p0_res = hpseudo_tt_sl_m500_w50p0.add_process(
    name="hpseudo_tt_sl_m500_w50p0_res",
    label=rf"{hpseudo_tt_sl_m500_w50p0.label}, res",
    id=71126,
)

hpseudo_tt_sl_m500_w50p0_int = hpseudo_tt_sl_m500_w50p0.add_process(
    name="hpseudo_tt_sl_m500_w50p0_int",
    label=rf"{hpseudo_tt_sl_m500_w50p0.label}, int",
    id=71127,
)

# width / mass = 10%

hpseudo_tt_sl_m600_w60p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m600_w60p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 10\%$)",
    id=71128,
)

hpseudo_tt_sl_m600_w60p0_res = hpseudo_tt_sl_m600_w60p0.add_process(
    name="hpseudo_tt_sl_m600_w60p0_res",
    label=rf"{hpseudo_tt_sl_m600_w60p0.label}, res",
    id=71129,
)

hpseudo_tt_sl_m600_w60p0_int = hpseudo_tt_sl_m600_w60p0.add_process(
    name="hpseudo_tt_sl_m600_w60p0_int",
    label=rf"{hpseudo_tt_sl_m600_w60p0.label}, int",
    id=71130,
)

hpseudo_tt_sl_m800_w80p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m800_w80p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 10\%$)",
    id=71131,
)

hpseudo_tt_sl_m800_w80p0_res = hpseudo_tt_sl_m800_w80p0.add_process(
    name="hpseudo_tt_sl_m800_w80p0_res",
    label=rf"{hpseudo_tt_sl_m800_w80p0.label}, res",
    id=71132,
)

hpseudo_tt_sl_m800_w80p0_int = hpseudo_tt_sl_m800_w80p0.add_process(
    name="hpseudo_tt_sl_m800_w80p0_int",
    label=rf"{hpseudo_tt_sl_m800_w80p0.label}, int",
    id=71133,
)

hpseudo_tt_sl_m1000_w100p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m1000_w100p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 10\%$)",
    id=71134,
)

hpseudo_tt_sl_m1000_w100p0_res = hpseudo_tt_sl_m1000_w100p0.add_process(
    name="hpseudo_tt_sl_m1000_w100p0_res",
    label=rf"{hpseudo_tt_sl_m1000_w100p0.label}, res",
    id=71135,
)

hpseudo_tt_sl_m1000_w100p0_int = hpseudo_tt_sl_m1000_w100p0.add_process(
    name="hpseudo_tt_sl_m1000_w100p0_int",
    label=rf"{hpseudo_tt_sl_m1000_w100p0.label}, int",
    id=71136,
)

# width / mass = 2.5%

hpseudo_tt_sl_m365_w9p125 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m365_w9p125",
    label=rf"{hpseudo_tt_sl.label} ($m = 365$ GeV, $\Gamma/m = 2\%$)",
    id=71137,
)

hpseudo_tt_sl_m365_w9p125_res = hpseudo_tt_sl_m365_w9p125.add_process(
    name="hpseudo_tt_sl_m365_w9p125_res",
    label=rf"{hpseudo_tt_sl_m365_w9p125.label}, res",
    id=71138,
)

hpseudo_tt_sl_m365_w9p125_int = hpseudo_tt_sl_m365_w9p125.add_process(
    name="hpseudo_tt_sl_m365_w9p125_int",
    label=rf"{hpseudo_tt_sl_m365_w9p125.label}, int",
    id=71139,
)

hpseudo_tt_sl_m400_w10p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m400_w10p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 400$ GeV, $\Gamma/m = 2\%$)",
    id=71140,
)

hpseudo_tt_sl_m400_w10p0_res = hpseudo_tt_sl_m400_w10p0.add_process(
    name="hpseudo_tt_sl_m400_w10p0_res",
    label=rf"{hpseudo_tt_sl_m400_w10p0.label}, res",
    id=71141,
)

hpseudo_tt_sl_m400_w10p0_int = hpseudo_tt_sl_m400_w10p0.add_process(
    name="hpseudo_tt_sl_m400_w10p0_int",
    label=rf"{hpseudo_tt_sl_m400_w10p0.label}, int",
    id=71142,
)

hpseudo_tt_sl_m500_w12p5 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m500_w12p5",
    label=rf"{hpseudo_tt_sl.label} ($m = 500$ GeV, $\Gamma/m = 2\%$)",
    id=71143,
)

hpseudo_tt_sl_m500_w12p5_res = hpseudo_tt_sl_m500_w12p5.add_process(
    name="hpseudo_tt_sl_m500_w12p5_res",
    label=rf"{hpseudo_tt_sl_m500_w12p5.label}, res",
    id=71144,
)

hpseudo_tt_sl_m500_w12p5_int = hpseudo_tt_sl_m500_w12p5.add_process(
    name="hpseudo_tt_sl_m500_w12p5_int",
    label=rf"{hpseudo_tt_sl_m500_w12p5.label}, int",
    id=71145,
)

# width / mass = 2.5%

hpseudo_tt_sl_m600_w15p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m600_w15p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 600$ GeV, $\Gamma/m = 2\%$)",
    id=71146,
)

hpseudo_tt_sl_m600_w15p0_res = hpseudo_tt_sl_m600_w15p0.add_process(
    name="hpseudo_tt_sl_m600_w15p0_res",
    label=rf"{hpseudo_tt_sl_m600_w15p0.label}, res",
    id=71147,
)

hpseudo_tt_sl_m600_w15p0_int = hpseudo_tt_sl_m600_w15p0.add_process(
    name="hpseudo_tt_sl_m600_w15p0_int",
    label=rf"{hpseudo_tt_sl_m600_w15p0.label}, int",
    id=71148,
)

hpseudo_tt_sl_m800_w20p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m800_w20p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 800$ GeV, $\Gamma/m = 2\%$)",
    id=71149,
)

hpseudo_tt_sl_m800_w20p0_res = hpseudo_tt_sl_m800_w20p0.add_process(
    name="hpseudo_tt_sl_m800_w20p0_res",
    label=rf"{hpseudo_tt_sl_m800_w20p0.label}, res",
    id=71150,
)

hpseudo_tt_sl_m800_w20p0_int = hpseudo_tt_sl_m800_w20p0.add_process(
    name="hpseudo_tt_sl_m800_w20p0_int",
    label=rf"{hpseudo_tt_sl_m800_w20p0.label}, int",
    id=71151,
)

hpseudo_tt_sl_m1000_w25p0 = hpseudo_tt_sl.add_process(
    name="hpseudo_tt_sl_m1000_w25p0",
    label=rf"{hpseudo_tt_sl.label} ($m = 1000$ GeV, $\Gamma/m = 2\%$)",
    id=71152,
)

hpseudo_tt_sl_m1000_w25p0_res = hpseudo_tt_sl_m1000_w25p0.add_process(
    name="hpseudo_tt_sl_m1000_w25p0_res",
    label=rf"{hpseudo_tt_sl_m1000_w25p0.label}, res",
    id=71153,
)

hpseudo_tt_sl_m1000_w25p0_int = hpseudo_tt_sl_m1000_w25p0.add_process(
    name="hpseudo_tt_sl_m1000_w25p0_int",
    label=rf"{hpseudo_tt_sl_m1000_w25p0.label}, int",
    id=71154,
)


#
# Kaluza-Klein gluon
#

rsgluon_tt = Process(
    name="rsgluon_tt",
    label=r"$g_\mathrm{KK}$",
    id=80000,
)


rsgluon_tt_m500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m500",
    label=rf"{rsgluon_tt.label} ($m = 500$ GeV)",
    id=80001,
)


rsgluon_tt_m1000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m1000",
    label=rf"{rsgluon_tt.label} ($m = 1000$ GeV)",
    id=80002,
)


rsgluon_tt_m1500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m1500",
    label=rf"{rsgluon_tt.label} ($m = 1500$ GeV)",
    id=80003,
)


rsgluon_tt_m2000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m2000",
    label=rf"{rsgluon_tt.label} ($m = 2000$ GeV)",
    id=80004,
)


rsgluon_tt_m2500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m2500",
    label=rf"{rsgluon_tt.label} ($m = 2500$ GeV)",
    id=80005,
)


rsgluon_tt_m3000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m3000",
    label=rf"{rsgluon_tt.label} ($m = 3000$ GeV)",
    id=80006,
)


rsgluon_tt_m3500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m3500",
    label=rf"{rsgluon_tt.label} ($m = 3500$ GeV)",
    id=80007,
)


rsgluon_tt_m4000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m4000",
    label=rf"{rsgluon_tt.label} ($m = 4000$ GeV)",
    id=80008,
)


rsgluon_tt_m4500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m4500",
    label=rf"{rsgluon_tt.label} ($m = 4500$ GeV)",
    id=80009,
)


rsgluon_tt_m5000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m5000",
    label=rf"{rsgluon_tt.label} ($m = 5000$ GeV)",
    id=80010,
)


rsgluon_tt_m5500 = rsgluon_tt.add_process(
    name="rsgluon_tt_m5500",
    label=rf"{rsgluon_tt.label} ($m = 5500$ GeV)",
    id=80011,
)


rsgluon_tt_m6000 = rsgluon_tt.add_process(
    name="rsgluon_tt_m6000",
    label=rf"{rsgluon_tt.label} ($m = 6000$ GeV)",
    id=80012,
)
