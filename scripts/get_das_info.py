# coding: utf-8

# USAGE: python get_das_info.py -d das_string
# e.g. /JetHT/Run2018C-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD

from __future__ import annotations

import subprocess
import json
from argparse import ArgumentParser


def get_generator_name(name: str) -> str:
    """
    Function that returns the generator name of a dataset
    """
    if "powheg" in name:
        return "_powheg"
    elif "madgraph" in name:
        return "_madgraph"
    elif "amcatnlo" in name:
        return "_amcatnlo"
    elif "pythia8" in name:
        return "_pythia8"
    else:
        return ""


def get_broken_files_str(data: dict, n_spaces: int = 20) -> str:
    """
    Function that returns a string represenatation of broken files
    """

    broken_files_list = [
        f'"{d}",  # broken  # noqa: E501' for d in data["broken_files"]
    ] + [
        f'"{d}",  # empty  # noqa: E501' for d in data["empty_files"] if d not in data["broken_files"]
    ]

    if not broken_files_list:
        return ""
    else:
        return (
            f"\n{' '* n_spaces}" +
            f"\n{' '* n_spaces}".join(broken_files_list) +
            f"\n{' '* (n_spaces - 4)}"
        )


def convert_default(data: dict, placeholder="PLACEHOLDER") -> str:
    """
    Function that converts dataset info into one order Dataset per query
    """
    generator = get_generator_name(data["name"])

    return f"""cpn.add_dataset(
    name="{placeholder}{generator}",
    id={data['dataset_id']},
    processes=[procs.{placeholder}],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "{data['name']}",  # noqa: E501
            ],
            aux={{
                "broken_files": [{get_broken_files_str(data)}],
            }},
            n_files={data['nfiles_good']},  # {data["nfiles"]}-{data["nfiles_bad"]}
            n_events={data['nevents']},
        ),
    ),
)
"""


identifier_map = {
    "_CP5TuneDown_": "tune_down",
    "_CP5TuneUp_": "tune_up",
    "_TuneCP5Down_": "tune_down",
    "_TuneCP5Up_": "tune_up",
    "_TuneCP5CR1_": "cr_1",
    "_TuneCP5CR2_": "cr_2",
    "_Hdamp-158_": "hdamp_down",
    "_Hdamp-418_": "hdamp_up",
    "_MT-171p5_": "mtop_down",
    "_MT-173p5_": "mtop_up",
    "_withDipoleRecoil_": "with_dipole_recoil",
    "_dipoleRecoilOn_": "dipole_recoil_on",
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
    "ext1": "extension",
    "_TuneCP5_": "nominal",
    "_CP5_": "nominal",
}


def convert_top(data: dict, placeholder="PLACEHOLDER") -> str:
    """
    Function that converts dataset info into either an order Datset for nominal datasets
    or to a DatasetInfo for variations of datasets such as tune or mtop.

    Exemplary usage:
    python get_das_info.py -c top -d "/TTtoLNu2Q*/Run3Summer22EENanoAODv12-130X_*/NANOAODSIM"
    """
    generator = get_generator_name(data["name"])
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
    name="{placeholder}{generator}",
    id={data['dataset_id']},
    processes=[procs.{placeholder}],
    info=dict(
        nominal=DatasetInfo(
            keys=[
                "{data['name']}",  # noqa: E501
            ],
            aux={{
                "broken_files": [{get_broken_files_str(data)}],
            }},
            n_files={data['nfiles_good']},  # {data["nfiles"]}-{data["nfiles_bad"]}
            n_events={data['nevents']},
        ),
    ),
)"""
    elif dataset_type == "comment":
        # comment out this dataset
        return f"""        # {identifier}=DatasetInfo(
        #     keys=[
        #         "{data['name']}",  # noqa: E501
        #     ],
        #     aux={{
        #         "broken_files": [{get_broken_files_str(data)}],
        #     }},
        #     n_files={data['nfiles_good']},  # {data["nfiles"]}-{data["nfiles_bad"]}
        #     n_events={data['nevents']},
        # ),"""
    elif dataset_type == "ignore":
        return ""
    else:
        # some known variation of the dataset
        return f"""        {dataset_type}=DatasetInfo(
            keys=[
                "{data['name']}",  # noqa: E501
            ],
            aux={{
                "broken_files": [{get_broken_files_str(data)}],
            }},
            n_files={data['nfiles_good']},  # {data["nfiles"]}-{data["nfiles_bad"]}
            n_events={data['nevents']},
        ),"""


def convert_keys(data: dict) -> str:
    """
    Function that only returns the dataset key.
    """
    return f"""{data['name']}"""


def convert_minimal(data: dict) -> str:
    """
    Function that only returns the dataset key + number of events.
    """
    return f"""{data['name']}\nFiles: {data['nfiles_good']}\nEvents: {data['nevents']}\n"""


convert_functions = {
    "default": convert_default,
    "keys": convert_keys,
    "top": convert_top,
    "minimal": convert_minimal,
}


def load_das_info(dataset: str, add_file_info: bool = False) -> dict:
    from law.util import interruptable_popen

    # call dasgoclient command
    cmd = f"dasgoclient -query='{'file ' if add_file_info else ''}dataset={dataset}' -json"
    code, out, _ = interruptable_popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        executable="/bin/bash",
    )
    if code != 0:
        raise Exception(f"dasgoclient query failed:\n{out}")
    infos = json.loads(out)

    return infos


def get_das_info(
    dataset: str,
    add_file_info: bool = False,
) -> dict:
    infos = load_das_info(dataset, add_file_info=False)

    info_of_interest = {"name": dataset}
    for info in infos:
        dataset_info = info["dataset"][0]
        if "files_via_dataset" in info["das"]["services"][0]:
            print("should not be called")
            empty_files = list(filter(lambda x: x["file"][0]["nevents"] == 0, info))
            broken_files = list(filter(lambda x: x["file"][0]["is_file_valid"] == 0, info))

        # Get json format of single das_string gives multiple dictornaries with different info
        # Avoid to print multiple infos twice and ask specificly for the kew of interest
        if "dataset_info" in info["das"]["services"][0]:
            info_of_interest["dataset_id"] = dataset_info.get("dataset_id", "")
        elif "filesummaries" in info["das"]["services"][0]:
            info_of_interest["nfiles"] = dataset_info.get("nfiles", "")
            info_of_interest["nevents"] = dataset_info.get("nevents", "")

    if add_file_info:
        file_infos = load_das_info(dataset, add_file_info=True)

        empty_files = [
            info["file"][0]["name"]
            for info in filter(lambda info: info["file"][0]["nevents"] == 0, file_infos)
        ]
        broken_files = [
            info["file"][0]["name"]
            for info in filter(lambda info: info["file"][0]["is_file_valid"] == 0, file_infos)
        ]
        info_of_interest["empty_files"] = empty_files
        info_of_interest["broken_files"] = broken_files
    else:
        info_of_interest["empty_files"] = "UNKNOWN"
        info_of_interest["broken_files"] = "UNKNOWN"

    return info_of_interest


def new_get_das_info(dataset: str) -> dict:
    info_of_interest = {"name": dataset}

    file_infos = load_das_info(dataset, add_file_info=True)

    info_of_interest["dataset_id"] = file_infos[0]["file"][0]["dataset_id"]

    empty_files_filter = lambda info: info["file"][0]["nevents"] == 0
    broken_files_filter = lambda info: info["file"][0]["is_file_valid"] == 0

    good_files = list(filter(lambda x: not broken_files_filter(x) and not empty_files_filter(x), file_infos))

    dataset_id = {info["file"][0]["dataset_id"] for info in good_files}
    if len(dataset_id) == 1:
        info_of_interest["dataset_id"] = dataset_id.pop()
    else:
        raise ValueError(f"Multiple dataset IDs ({dataset_id}) found for dataset {dataset}")

    info_of_interest["nfiles"] = len(file_infos)
    info_of_interest["nfiles_good"] = len(good_files)
    info_of_interest["nevents"] = sum(info["file"][0]["nevents"] for info in good_files)

    empty_files = [
        info["file"][0]["name"]
        for info in filter(empty_files_filter, file_infos)
    ]
    broken_files = [
        info["file"][0]["name"]
        for info in filter(broken_files_filter, file_infos)
    ]
    info_of_interest["empty_files"] = empty_files
    info_of_interest["broken_files"] = broken_files

    info_of_interest["nfiles_bad"] = len(set(empty_files + broken_files))

    return info_of_interest


def print_das_info(
    das_strings: list[str],
    keys_of_interest: tuple | None = None,
    convert_function_str: str | None = None,
):
    # get the requested convert function
    convert_function = convert_functions[convert_function_str]

    for das_string in das_strings:
        # set default keys of interest
        # NOTE: this attribute is currently not used
        keys_of_interest = keys_of_interest or (
            "name", "dataset_id", "nfiles", "nevents", "empty_files", "broken_files",
        )

        wildcard = "*" in das_string
        datasets = []
        if not wildcard:
            # keep consisting structure
            datasets.append(das_string)
        else:
            # using a wildcard leads to a different structer in json format
            infos = load_das_info(das_string, add_file_info=False)
            for info in infos:
                dataset_name = info.get("dataset", [])[0].get("name", "")
                datasets.append(dataset_name)

        for dataset in datasets:
            info_of_interest = new_get_das_info(dataset)
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
