# cmsdb

[![Lint and test](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml)
[![License](https://img.shields.io/github/license/uhh-cms/cmsdb.svg)](https://github.com/uhh-cms/cmsdb/blob/master/LICENSE)

Database of physics processes, cross sections and scientific constants as well as CMS-related campaign information on datasets.

## Campaign names and descriptions

| Name                                                                                   | Postfix  | Tags                        |
| -------------------------------------------------------------------------------------- | -------- | --------------------------- |
| [`run2_2016_HIPM_nano_uhh_v12`](./cmsdb/campaigns/run2_2016_HIPM_nano_uhh_v12)         | `"APV"`  | `{"preVFP", "APV", "HIPM"}` |
| [`run2_2016_nano_uhh_v12`](./cmsdb/campaigns/run2_2016_nano_uhh_v12)                   | `""`     | `{"postVFP"}`               |
| [`run2_2017_nano_v9`](./cmsdb/campaigns/run2_2017_nano_v9)                             | `""`     | `{}`                        |
| [`run2_2017_JMEnano_v9`](./cmsdb/campaigns/run2_2017_JMEnano_v9)                       | `""`     | `{}`                        |
| [`run2_2017_nano_uhh_v11`](./cmsdb/campaigns/run2_2017_nano_uhh_v11)                   | `""`     | `{}`                        |
| [`run2_2018_nano_v9`](./cmsdb/campaigns/run2_2018_nano_v9)                             | `""`     | `{}`                        |
| [`run2_2018_JMEnano_v9`](./cmsdb/campaigns/run2_2018_JMEnano_v9)                       | `""`     | `{}`                        |
| [`run2_2018_nano_uhh_v11`](./cmsdb/campaigns/run2_2018_nano_uhh_v11)                   | `""`     | `{}`                        |
| [`run2_2018_nano_uhh_v12`](./cmsdb/campaigns/run2_2018_nano_uhh_v12)                   | `""`     | `{}`                        |
| [`run3_2022_preEE_nano_v11`](./cmsdb/campaigns/run3_2022_preEE_nano_v11)               | `""`     | `{"preEE"}`                 |
| [`run3_2022_preEE_nano_v12`](./cmsdb/campaigns/run3_2022_preEE_nano_v12)               | `""`     | `{"preEE"}`                 |
| [`run3_2022_preEE_nano_uhh_v12`](./cmsdb/campaigns/run3_2022_preEE_nano_uhh_v12)       | `""`     | `{"preEE"}`                 |
| [`run3_2022_postEE_nano_v11`](./cmsdb/campaigns/run3_2022_postEE_nano_v11)             | `"EE"`   | `{"postEE", "EE"}`          |
| [`run3_2022_postEE_nano_v12`](./cmsdb/campaigns/run3_2022_postEE_nano_v12)             | `"EE"`   | `{"postEE", "EE"}`          |
| [`run3_2022_postEE_nano_uhh_v12`](./cmsdb/campaigns/run3_2022_postEE_nano_uhh_v12)     | `"EE"`   | `{"postEE", "EE"}`          |
| [`run3_2023_preBPix_nano_v13`](./cmsdb/campaigns/run3_2023_preBPix_nano_v13)           | `""`     | `{"preBPix"}`               |
| [`run3_2023_postBPix_nano_v13`](./cmsdb/campaigns/run3_2023_postBPix_nano_v13)         | `"BPix"` | `{"postBPix", "BPix"}`      |
| [`run3_2023_preBPix_nano_uhh_v14`](./cmsdb/campaigns/run3_2023_preBPix_nano_uhh_v14)   | `""`     | `{"preBPix"}`               |
| [`run3_2023_postBPix_nano_uhh_v14`](./cmsdb/campaigns/run3_2023_postBPix_nano_uhh_v14) | `"BPix"` | `{"postBPix", "BPix"}`      |
| [`run3_2024_nano_v15`](./cmsdb/campaigns/run3_2024_nano_v15)                           | `""`     | `{}`                        |

## Dependencies

- [order](https://github.com/riga/order) is used to model the relations between physics meta data containers (datasets, processes, systematics, ...).
- [scinum](https://github.com/riga/scinum)'s `Number` is the basis for numeric values with multiple sources of systematic uncertainties attributed to them.
