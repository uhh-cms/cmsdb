# coding: utf-8

"""
Data process definitions.
"""

__all__ = [
    "data", "data_e", "data_mu", "data_tau", "data_met",
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
