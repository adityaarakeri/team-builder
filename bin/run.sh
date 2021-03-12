#!/usr/bin/env bash

for arg in "$@"
do
    if [ "$arg" == "--help" ] || [ "$arg" == "-h" ] || [ "$arg" == "" ]
    then
        echo "Usage:"
        echo ""
        echo "./bin/run.sh options"
        echo ""
        echo "run options:"
        echo "-i, --index    : create an index file"
    fi
    if [ "$arg" == "-i" ] || [ "$arg" == "--index" ]
    then
        echo "Creating an index file"
        echo ""
        pipenv run python builder.py > index.html
    fi
done