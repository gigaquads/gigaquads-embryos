# Python Project Embryo
Common components for use when building python projects

## Overview
- `base`, the base python project application, sets you up with a place to start developing
- `cli`, command-line interface into the app
- `setup`, a nice wrapper for setuptools that gets you started with a pypi-ready package

## Usage
Sub-embryo | Command
-----|------
base | `embryo hatch python-project/base --name LameProject`
cli | `embryo hatch python-project/cli`
setup | `embryo hatch python-project/setup --name LameProject --version  1337 --classifiers python3`
