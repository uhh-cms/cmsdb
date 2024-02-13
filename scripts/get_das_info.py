# coding: utf-8

# USAGE: python get_das_info.py -d das_string
# e.g. /JetHT/Run2018C-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD

from __future__ import annotations

import subprocess
import json
from argparse import ArgumentParser

import law


def convert_default(data: dict) -> str:
    """
    Function that converts dataset info into one order Dataset per query
    """
    return f"""cpn.add_dataset(
    name="PLACEHOLDER",
    id={data['dataset_id']},
    processes=[procs.PLACEHOLDER],
    keys=[
        "{data['name']}",  # noqa
    ],
    n_files={data['nfiles']},
    n_events={data['nevents']},
)
"""


identifier_map = {
    "_TuneCP5Down_": "tune_down",
    "_TuneCP5Up_": "tune_up",
    "_TuneCP5CR1_": "cr_1",
    "_TuneCP5CR2_": "cr_2",
    "_Hdamp-158_": "hdamp_down",
    "_Hdamp-418_": "hdamp_up",
    "_MT-171p5_": "mtop_down",
    "_MT-173p5_": "mtop_up",
    # dataset types that I have no use for but want to keep anyways
    "_MT-166p5_": "comment",
    "_MT-169p5_": "comment",
    "_MT-175p5_": "comment",
    "_MT-178p5_": "comment",
    "_DS_TuneCP5_": "comment",
    "_TuneCP5_ERDOn_": "comment",
    "_TuneCH3_": "comment",
    # dataset types that I want to skip completely
    # "example_key": "ignore",
    # nominal entry as the last one such that other dataset types get priority
    "_TuneCP5_": "nominal",
}


def convert_top(data: dict) -> str:
    """
    Function that converts dataset info into either an order Datset for nominal datasets
    or to a DatasetInfo for variations of datasets such as tune or mtop.

    Exemplary usage:
    python get_das_info.py -c convert_top -d "/TTtoLNu2Q*/Run3Summer22EENanoAODv12-130X_*/NANOAODSIM"
    """
    dataset_type = None

    for identifier in identifier_map:
        if identifier in data["name"]:
            dataset_type = identifier_map[identifier]
            break

    if not dataset_type:
        return f"""
        #####
        #####ERROR! Did not manage to determine type of dataset {data['name']}
        #####
        """

    if dataset_type == "nominal":
        return f"""cpn.add_dataset(
    name="PLACEHOLDER",
    id={data['dataset_id']},
    processes=[procs.PLACEHOLDER],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "{data['name']}",  # noqa
            ],
            n_files={data['nfiles']},
            n_events={data['nevents']},
        ),
    ),
)"""
    elif dataset_type == "comment":
        # comment out this dataset
        return f"""        # {dataset_type}=DatasetInfo(
        #     keys=[
        #         "xxx",  # noqa
        #     ],
        #     n_files={data['nfiles']},
        #     n_events={data['nevents']},
        # ),"""
    elif dataset_type == "ignore":
        return ""
    else:
        # some known variation of the dataset
        return f"""        {dataset_type}=DatasetInfo(
            keys=[
                "{data['name']}",  # noqa
            ],
            n_files={data['nfiles']},
            n_events={data['nevents']},
        ),"""


convert_functions = {
    "default": convert_default,
    "top": convert_top,
}


def print_das_info(
    das_strings: list[str],
    keys_of_interest: tuple | None = None,
    convert_function_str: str | None = None,
):
    # get the requested convert function
    convert_function = convert_functions[convert_function_str]

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

            desired_output = convert_function(info_of_interest)
            print(desired_output)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--dataset", dest="dataset", nargs="+", help="das name")
    parser.add_argument(
        "-c",
        "--convert",
        dest="convert",
        help="function that converts info into code",
        default="default",
        choices=list(convert_functions),
    )
    args = parser.parse_args()
    print_das_info(args.dataset, convert_function_str=args.convert)
