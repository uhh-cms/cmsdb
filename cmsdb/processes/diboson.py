# coding: utf-8

"""
Diboson process definitions.
"""

__all__ = [
    "vv", "ww", "zz", "wz",
    "vv_4l", "vv_2l2nu", "vv_2l2q", "vv_2nu2q", "vv_4nu", "vv_4q", "vv_lnu2q", "vv_3lnu", "vv_l3nu",
    "zz_4l", "zz_2l2nu", "zz_2l2q", "zz_2nu2q", "zz_4nu", "zz_4q",
    "wz_3lnu", "wz_l3nu", "wz_lnu2q", "wz_2l2q", "wz_2nu2q", "wz_4q",
    "ww_2l2nu", "ww_lnu2q", "ww_4q",
]

from functools import partial

from order import Process
from scinum import Number

import cmsdb.constants as const

from cmsdb.util import DotDict, add_xsecs, add_decay_process

add_vv_decay_process = partial(
    add_decay_process,
    name_func=lambda parent_name, decay_name: f"{parent_name}_{decay_name}",
    label_func=lambda parent_label, decay_label: f"${parent_label} \rightarrow {decay_label}$",
)

vv_decay_map = DotDict.wrap({
    "4l": {  # ZZ
        "name": "4l",
        "id": 10,
        "label": r"4\ell",
        "br": -1,
    },
    "2l2nu": {  # ZZ, WW
        "name": "2l2nu",
        "id": 20,
        "label": r"2\ell 2\nu",
        "br": -1,
    },
    "2l2q": {  # ZZ, WZ
        "name": "2l2q",
        "id": 30,
        "label": r"2\ell 2q",
        "br": -1,
    },
    "2nu2q": {  # ZZ, WZ
        "name": "2nu2q",
        "id": 40,
        "label": r"2\nu 2q",
        "br": -1,
    },
    "4nu": {  # ZZ
        "name": "4nu",
        "id": 50,
        "label": r"4\nu",
        "br": -1,
    },
    "4q": {  # ZZ, WW, WZ
        "name": "4q",
        "id": 60,
        "label": r"4q",
        "br": -1,
    },
    "lnu2q": {  # WW, WZ
        "name": "lnu2q",
        "id": 70,
        "label": r"\ell\nu 2q",
        "br": -1,
    },
    "3lnu": {  # WZ
        "name": "3lnu",
        "id": 80,
        "label": r"3\ell\nu",
        "br": -1,
    },
    "l3nu": {  # WZ
        "name": "l3nu",
        "id": 90,
        "label": r"\ell 3\nu",
        "br": -1,
    },
})

zz_decay_map = {
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("4l", "2l2nu", "2l2q", "2nu2q", "4nu", "4q")
}
zz_decay_map["4l"]["br"] = const.br_zz.llll
zz_decay_map["2l2nu"]["br"] = const.br_zz.llnunu
zz_decay_map["2l2q"]["br"] = const.br_zz.llqq
zz_decay_map["2nu2q"]["br"] = const.br_zz.qqnunu
zz_decay_map["4nu"]["br"] = const.br_zz.nunununu
zz_decay_map["4q"]["br"] = const.br_zz.qqqq

ww_decay_map = {
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("2l2nu", "lnu2q", "4q")
}
ww_decay_map["2l2nu"]["br"] = const.br_ww.dl
ww_decay_map["lnu2q"]["br"] = const.br_ww.sl
ww_decay_map["4q"]["br"] = const.br_ww.fh

wz_decay_map = {
    final_state: vv_decay_map[final_state].copy()
    for final_state in ("3lnu", "l3nu", "lnu2q", "2l2q", "2nu2q", "4q")
}
wz_decay_map["3lnu"]["br"] = const.br_wz["3lnu"]
wz_decay_map["l3nu"]["br"] = const.br_wz["l3nu"]
wz_decay_map["lnu2q"]["br"] = const.br_wz["lnu2q"]
wz_decay_map["2l2q"]["br"] = const.br_wz["2l2q"]
wz_decay_map["2nu2q"]["br"] = const.br_wz["2nu2q"]
wz_decay_map["4q"]["br"] = const.br_wz["4q"]

#
# Di-boson
#

vv = Process(
    name="vv",
    id=8000,
    label="VV",
)

vv_4l = add_vv_decay_process(vv, vv_decay_map["4l"], add_production_mode_parent=False)
vv_2l2nu = add_vv_decay_process(vv, vv_decay_map["2l2nu"], add_production_mode_parent=False)
vv_2l2q = add_vv_decay_process(vv, vv_decay_map["2l2q"], add_production_mode_parent=False)
vv_2nu2q = add_vv_decay_process(vv, vv_decay_map["2nu2q"], add_production_mode_parent=False)
vv_4nu = add_vv_decay_process(vv, vv_decay_map["4nu"], add_production_mode_parent=False)
vv_4q = add_vv_decay_process(vv, vv_decay_map["4q"], add_production_mode_parent=False)
vv_lnu2q = add_vv_decay_process(vv, vv_decay_map["lnu2q"], add_production_mode_parent=False)
vv_3lnu = add_vv_decay_process(vv, vv_decay_map["3lnu"], add_production_mode_parent=False)
vv_l3nu = add_vv_decay_process(vv, vv_decay_map["l3nu"], add_production_mode_parent=False)

zz = vv.add_process(
    name="zz",
    id=8100,
    label="ZZ",
    xsecs={
        # https://link.springer.com/article/10.1007/JHEP03(2019)070#preview, table 3, nNNLO
        13: Number(24.97, {"scale": (0.029j, 0.027j)}),
        # no theory prediction found yet, so take accurate value at 13 TeV and scale by the ratio
        # of XSDB values at https://xsdb-temp.app.cern.ch/xsdb/?columns=67108863&currentPage=0&pageSize=40&searchQuery=process_name%3D%5EZZ_TuneCP5_13.%2Bpythia8%24  # noqa
        13.6: Number(24.97, {"scale": (0.029j, 0.027j)}) * (12.75 / 12.14),
    },
    aux={"production_mode_parent": "vv"},
)

zz_4l = add_vv_decay_process(zz, zz_decay_map["4l"])
zz_2l2nu = add_vv_decay_process(zz, zz_decay_map["2l2nu"])
zz_2l2q = add_vv_decay_process(zz, zz_decay_map["2l2q"])
zz_2nu2q = add_vv_decay_process(zz, zz_decay_map["2nu2q"])
zz_4nu = add_vv_decay_process(zz, zz_decay_map["4nu"])
zz_4q = add_vv_decay_process(zz, zz_decay_map["4q"])

# WZ xsec values at NLO from https://arxiv.org/pdf/1105.0020.pdf v1
wp_z_xsec = {
    13: Number(28.55, {"scale": (0.041j, 0.032j)}),
}

wm_z_xsec = {
    13: Number(18.19, {"scale": (0.041j, 0.033j)}),
}

# old value before update:
# https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/197 (v3) Number(25.56) (LO)
wz = vv.add_process(
    name="wz",
    id=8200,
    label="WZ",
    xsecs={
        # as a remark, the W cross section calculation from
        # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV?rev=28
        # shows a permille difference in the values calculated directly and the ones added from w+ and w-
        13: wp_z_xsec[13] + wm_z_xsec[13],
        # no 13.6 theory prediction found yet, so take accurate value at 13 TeV and scale by the ratio of XSDB values
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?searchQuery=DAS%3DWZ_TuneCP5_13TeV-pythia
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?searchQuery=DAS%3DWZ_TuneCP5_13p6TeV-pythia
        13.6: (wp_z_xsec[13] + wm_z_xsec[13]) * 29.12 / 27.59,
    },
    aux={"production_mode_parent": "vv"},
)

wz_3lnu = add_vv_decay_process(wz, wz_decay_map["3lnu"])
wz_l3nu = add_vv_decay_process(wz, wz_decay_map["l3nu"])
wz_lnu2q = add_vv_decay_process(wz, wz_decay_map["lnu2q"])
wz_2l2q = add_vv_decay_process(wz, wz_decay_map["2l2q"])
wz_2nu2q = add_vv_decay_process(wz, wz_decay_map["2nu2q"])
wz_4q = add_vv_decay_process(wz, wz_decay_map["4q"])

ww = vv.add_process(
    name="ww",
    id=8300,
    label="WW",
    xsecs={
        13: Number(118.7, {"scale": (0.025j, 0.022j)}),
        # no 13.6 theory prediction found yet, so take accurate value at 13 TeV and scale by the ratio of XSDB values
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?searchQuery=DAS=WW_TuneCP5_13TeV-pythia
        # https://xsecdb-xsdb-official.app.cern.ch/xsdb/?searchQuery=DAS=WW_TuneCP5_13p6TeV-pythia
        13.6: Number(118.7, {"scale": (0.025j, 0.022j)}) * 80.42 / 75.95,
    },
    aux={"production_mode_parent": "vv"},
)

ww_2l2nu = add_vv_decay_process(ww, ww_decay_map["2l2nu"])
ww_lnu2q = add_vv_decay_process(ww, ww_decay_map["lnu2q"])
ww_4q = add_vv_decay_process(ww, ww_decay_map["4q"])

# update vv cross section
vv.xsecs = add_xsecs(ww, wz, zz)
vv_4l.xsecs = add_xsecs(zz_4l)
vv_2l2nu.xsecs = add_xsecs(zz_2l2nu, ww_2l2nu)
vv_2l2q.xsecs = add_xsecs(zz_2l2q, wz_2l2q)
vv_2nu2q.xsecs = add_xsecs(zz_2nu2q, wz_2nu2q)
vv_4nu.xsecs = add_xsecs(zz_4nu)
vv_4q.xsecs = add_xsecs(zz_4q, ww_4q, wz_4q)
vv_lnu2q.xsecs = add_xsecs(ww_lnu2q, wz_lnu2q)
vv_3lnu.xsecs = add_xsecs(wz_3lnu)
vv_l3nu.xsecs = add_xsecs(wz_l3nu)
