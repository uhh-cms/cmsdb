# cmsdb

[![Lint and test](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml/badge.svg)](https://github.com/uhh-cms/cmsdb/actions/workflows/lint_and_test.yaml)
[![License](https://img.shields.io/github/license/uhh-cms/cmsdb.svg)](https://github.com/uhh-cms/cmsdb/blob/master/LICENSE)

Database of physics processes, cross sections and scientific constants as well as CMS-related campaign information on datasets.


#### Dependencies

- [order](https://github.com/riga/order) is used to model the relations between physics meta data containers (datasets, processes, systematics, ...).
- [scinum](https://github.com/riga/scinum)'s `Number` is the basis for numeric values with multiple sources of systematic uncertainties attributed to them.
