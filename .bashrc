#!/usr/bin/env bash

# known embryo paths
export EMBRYO_PATH="$EMBRYO_PATH:$HOME/code/gigaquads-embryos/stable"
export EMBRYO_PATH="$EMBRYO_PATH:$HOME/code/axial-embryos"
export EMBRYO_PATH="$EMBRYO_PATH:$HOME/code/track-me-track-you/track_me_track_you/embryos"

EMBRYO_BIN_NAME='embryo'

for addon in $EMBRYO_BIN_NAME
do
  thisbin=`which $addon`
  declare "THIS_$addon=$thisbin"
  if [ $thisbin ]
  then
    printf ", +$addon"
    
  else
    printf ", -$addon"
  fi
done


if [ $THIS_embryo ]
then
  # support embryo convenience

  # generic project
  alias projbase="embryo hatch project/base --project.name"
  alias projenv="embryo hatch project/env"

  # for python-project
  alias pybase="embryo hatch python-project/base"
  alias pylicense="embryo hatch python-project/license --author"
  alias pysetup="embryo hatch python-project/setup --refresh_scripts True"

  # pybiz-project
  alias bizapi="embryo hatch pybiz-project/api --api.name"
  alias bizbase="embryo hatch pybiz-project/base"
  alias bizbiz="embryo hatch pybiz-project/biz --biz.name"
  alias bizcli="embryo hatch pybiz-project/cli"
  alias bizdao="embryo hatch pybiz-project/dao --dao.type yaml --dao.name"
  alias bizenv="embryo hatch pybiz-project/env"
  alias bizresource="embryo hatch pybiz-project/resource --resource.name"
  alias bizsvc="embryo hatch pybiz-project/svc"
  alias bizuwsgi="embryo hatch pybiz-project/uwsgi"

  # git
  alias emgit="embryo hatch git-project"

  # embryo
  alias emembryo="embryo hatch embryo --name"

  # docker
  alias dockproj="embryo hatch docker/base"

  dockproj_notdsk() {
    dockproj \
      --build.repo.server gitlab \
      --build.repo.org notdsk \
      --build.repo.gitlab_host https://code.lib.land \
      $@
  }

  # helm
  alias emhelm="embryo hatch helm/chart --chart.name"

  # drone
  alias emdrone="embryo hatch drone"
fi
