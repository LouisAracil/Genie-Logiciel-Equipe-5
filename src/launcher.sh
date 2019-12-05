#!/usr/bin/env bash

for file in ls $1/*.pdf
do
	python3 main.py $file
done
