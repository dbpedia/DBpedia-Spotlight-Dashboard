#!/bin/bash

status="$?"
python -c "import pandas"
if [ "$status" != 0 ]; then
	pip install pandas
fi
python -c "import dash"
if [ "$status" != 0 ]; then
	pip install dash
fi

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
