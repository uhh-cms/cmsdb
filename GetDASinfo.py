# coding: utf-8

# USAGE: python GetDASinfo.py -d das_string
# e.g. /JetHT/Run2018C-UL2018_MiniAODv2_JMENanoAODv9-v1/NANOAOD

from __future__ import annotations

import subprocess
import json
from optparse import OptionParser
import law

def get_das_info(das_string: str, keys_of_interest: tuple | None = None):

    # set default keys of interest
    keys_of_interest = keys_of_interest or (
        "name", "dataset_id", "nfiles", "nevents",
    )

    # call dasgoclient command
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
    # json file from dataset contains 4 dictonaries, containing different infos (ids, files, etc.)
    info_of_interest = {'name': das_string}
    for info in infos:
        dataset_info = info["dataset"][0]
    
        # check that all keys of interest are there
        # if not set(keys_of_interest).issubset(dataset_info.keys()):
        #     continue
        
        if "dataset_info" in info["das"]["services"][0]:
            info_of_interest["dataset_id"] = dataset_info.get("dataset_id", "")
        elif "filesummaries" in info["das"]["services"][0]:
            info_of_interest["nfiles"] = dataset_info.get("nfiles", "")
            info_of_interest["nevents"] = dataset_info.get("nevents", "")
    
    print(json.dumps(info_of_interest, indent=4))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-d', '--dataset', dest='dataset', help='das name')
    (options,args) = parser.parse_args()

    get_das_info(options.dataset)
