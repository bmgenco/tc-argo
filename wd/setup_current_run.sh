#!/bin/bash 
set -e 

dir=$PWD
parentdir="$(dirname "$dir")"
scripts=$parentdir/scripts/current_runs

cp -RT $scripts $dir

exit 0