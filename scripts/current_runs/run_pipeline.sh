#!/bin/bash 
set -e   

 # to do: add integrated or gridded varible to python script
 #https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/
 

start=$(date +%m)
source /home/brandon/anaconda3/etc/profile.d/conda.sh
conda activate argo

dir=$PWD
parentdir="$(dirname "$dir")"
logdir=$parentdir/log_history

## define directory and  choose current, commet out other:
current='../original/pipeline-gridded/'
arg1="gridded"

#current='../original/pipeline-integrated/'
#arg1="integrated"


printf "run time start: " > log.txt
date >> log.txt

cp current_settings.py $current/settings.py
cp current_pipeline.py $current/pipeline.py

cp current_settings.py  $logdir/settings_`date +%Y%m%d`.py
cp current_pipeline.py  $logdir/pipeline_`date +%Y%m%d`.py


cd $current

echo "started pipeline at:" 
date

python pipeline.py $arg1
cd $dir

printf "run time end: " >> log.txt
date >> log.txt
end=$(date +%m)
echo "Elapsed Time: $(($end-$start)) minutes" >> log.txt

mv log.txt $logdir/log_`date +%Y%m%d`.txt

echo "finished at:"
date     

exit 0
