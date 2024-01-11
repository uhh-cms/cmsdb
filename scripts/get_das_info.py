# coding: utf-8

# USAGE: python GetDASinfo.py -d das_string
# e.g. /JetHT/Run2018C-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD

from __future__ import annotations

import subprocess
import json
from argparse import ArgumentParser

import law


def convert_to_desired_structure(data: dict) -> str:
    return f"""cpn.add_dataset(
    name="PLACEHOLDER",
    id={data['dataset_id']},
    processes=[procs.PLACEHOLDER],
    keys=[
        "{data['name']}",  # noqa
    ],
    n_files={data['nfiles']},
    n_events={data['nevents']},
)"""


def print_das_info(das_strings: list[str], keys_of_interest: tuple | None = None):
    for das_string in das_strings:
        # set default keys of interest
        keys_of_interest = keys_of_interest or (
            "name", "dataset_id", "nfiles", "nevents",
        )

        wildcard = "*" in das_string
        datasets = []
        if not wildcard:
            # keep consisting structure
            datasets.append(das_string)
        else:
            # using a wildcard leads to a different structer in json format
            cmd = f"dasgoclient -query='dataset={das_string}' -json"
            code, out, _ = law.util.interruptable_popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                executable="/bin/bash",
            )
            if code != 0:
                raise Exception(f"dasgoclient query failed:\n{out}")
            infos = json.loads(out)
            for info in infos:
                dataset_name = info.get("dataset", [])[0].get("name", "")
                datasets.append(dataset_name)

        for dataset in datasets:
            # call dasgoclient command
            cmd = f"dasgoclient -query='dataset={dataset}' -json"
            code, out, _ = law.util.interruptable_popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                executable="/bin/bash",
            )
            if code != 0:
                raise Exception(f"dasgoclient query failed:\n{out}")
            infos = json.loads(out)
            info_of_interest = {"name": dataset}
            for info in infos:
                dataset_info = info["dataset"][0]
                # Get json format of single das_string gives multiple dictornaries with different info
                # Avoid to print multiple infos twice and ask specificly for the kew of interest
                if "dataset_info" in info["das"]["services"][0]:
                    info_of_interest["dataset_id"] = dataset_info.get("dataset_id", "")
                elif "filesummaries" in info["das"]["services"][0]:
                    info_of_interest["nfiles"] = dataset_info.get("nfiles", "")
                    info_of_interest["nevents"] = dataset_info.get("nevents", "")

            desired_output = convert_to_desired_structure(info_of_interest)
            print(desired_output)
            print()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--dataset", dest="dataset", nargs="+", help="das name")
    args = parser.parse_args()
    print_das_info(args.dataset)
