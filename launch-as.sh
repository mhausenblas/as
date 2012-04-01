#!/bin/sh
if [ "$1" == "create" ]; then
	python fill_datastore.py as-input.csv https://dequilibrium.cloudant.com as
fi
python proxy_as.py