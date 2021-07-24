#!/bin/bash

DIR=$(pwd)
BASE_DIR=${DIR//"/src"/}
RESOURCES_DIR="$BASE_DIR/resources"
ES="es"
DASHBOARD="dashboard_data"

function check_packages {
REQUIRED_PKG=$1
PKG_OK=$(dpkg-query -W --showformat='${Status}\n' $REQUIRED_PKG|grep "install ok installed")
echo Checking for $REQUIRED_PKG: $PKG_OK
if [ "" = "$PKG_OK" ]; then
  echo "No $REQUIRED_PKG. Setting up $REQUIRED_PKG."
  sudo apt-get --yes install $REQUIRED_PKG 
fi
}

function check_modules {
REQUIRED_MODULE=$1
MODULE_OK=$(pip3 list --format=columns | grep $REQUIRED_MODULE)
if [ -z "$MODULE_OK" ]
then
      pip3 install $REQUIRED_MODULE
else
      echo "$REQUIRED_MODULE is already installed"
fi
}

check_packages "python3"
check_packages "python3-pip"
check_modules "pandas"
check_modules "dash"
check_modules "dash-core-components"
check_modules "dash-html-components"
check_modules "dash-table"
check_modules "plotly"
check_modules "dash-bootstrap-components"
cd "src"
# echo ""	
# read -p "URLs validation takes so much time. Also a DBpedia SPARQL instance is necessary.
# However, files resulting from validation are already in the repository so it is not necessary to validate URLs.
# Do you want to validate URLs anyway? [y/n] " validate
# if [[ $validate == [yY] ]]; then
#	echo "Getting raw dashboard data"
#	./get_resources.sh
#	echo "Validating URLs"
#	./validate.sh
#	echo "Generating stats again"
#	./stats.sh
#	echo "Getting instance-types version stats"
#	./versions.sh
#fi

echo "Loading dashboard..."
python3 dashboard.py
