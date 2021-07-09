#!/bin/bash

function install_modules {
pip install pandas
pip install dash
pip install dash-core-components
pip install dash-html-components
pip install dash-table
pip install plotly
pip install dash-bootstrap-components
}

install_modules
cd "src"	
read -p "URLs validation takes so much time. Also a DBpedia SPARQL instance is necessary.
However, files resulting from validation are already in the repository so it is not necessary to validate URLs.
Do you want to validate URLs anyway? [y/n] " validate
if [[ $validate == [yY] ]]; then
	echo "Getting raw dashboard data"
	./get_resources.sh
	echo "Validating URLs"
	./validate.sh
	echo "Generating stats again"
	./stats.sh
fi
echo "Launching dashboard"
python dashboard.py
