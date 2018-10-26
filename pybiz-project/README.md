# Pybiz Project

## Overview
This embryo contains the following sub-embryos:
- `api`, API endpoints
- `base`, Base elements necessary for other layers
- `biz`, Business object and related structure
- `cli`, Command-line interface into the application
- `dao`, Dao object and related structure
- `resource`, Convenience to simultaneously construct biz+dao+api objects by name
- `svc`, Service object and related structure
- `uwsgi`, Bootstrap your application with uwsgi

## Usage
Sub-embryo | Command
-----|------
api | `embryo create pybiz-project/api --api.name my-lame-api`
base | `embryo create pybiz-project/base --project.name my-lame-project`
biz | `embryo create pybiz-project/biz --biz.name my-lame-biz`
cli | `embryo hatch python-project/cli`
dao | `embryo create pybiz-project/dao --dao.name my-lame-dao --dao.type yaml`
resource | `embryo create pybiz-project/resource --resource.name my-lame-resource`
svc | `embryo create pytbiz-project/svc`
uwsgi | `embryo create pybiz-project/uwsgi`
