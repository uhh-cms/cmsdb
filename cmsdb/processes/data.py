# coding: utf-8

"""
Data process definitions.
"""

__all__ = [
    "data", "data_e", "data_mu",
    "data_tau", "data_met", "data_pho",
    "data_egamma", "data_muoneg", "data_jetht", "data_jethtmet", "data_doublemu", "data_vbf",
]

from order import Process


#
# data
# (ids up to 999)
#

data = Process(
    name="data",
    id=1,
    is_data=True,
    label="Data",
)

data_e = data.add_process(
    name="data_e",
    id=10,
    is_data=True,
    label=r"Data $e$",
)

data_mu = data.add_process(
    name="data_mu",
    id=20,
    is_data=True,
    label=r"Data $\mu$",
)

data_tau = data.add_process(
    name="data_tau",
    id=30,
    is_data=True,
    label=r"Data $\tau$",
)

data_met = data.add_process(
    name="data_met",
    id=40,
    is_data=True,
    label=r"Data MET",
)

data_pho = data.add_process(
    name="data_pho",
    id=50,
    is_data=True,
    label=r"Data $\gamma$",
)

data_egamma = data.add_process(
    name="data_egamma",
    id=60,
    is_data=True,
    label=r"Data $e/\gamma$",
)

data_muoneg = data.add_process(
    name="data_muoneg",
    id=70,
    is_data=True,
    label=r"Data $\mu e/\gamma$",
)

data_doublemu = data.add_process(
    name="data_doublemu",
    id=80,
    is_data=True,
    label=r"Data $\mu$",
)

data_jetht = data.add_process(
    name="data_jetht",
    id=100,
    is_data=True,
    label=r"Data JetHT",
)

data_jethtmet = data.add_process(
    name="data_jethtmet",
    id=140,
    is_data=True,
    label=r"Data JetHT/MET",
)

data_vbf = data.add_process(
    name="data_vbf",
    id=150,
    is_data=True,
    label=r"Data VBF",
)
