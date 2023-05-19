 #!/bin/bash    
 # shell script 
start=$(date +%m)

source /home/brandon/anaconda3/etc/profile.d/conda.sh
conda activate argo

dir=$PWD
parentdir="$(dirname "$dir")"
logdir=$parentdir/log_history

# define directory, choose current, commet out other:
current='../original/pipeline-gridded/'
#current='../original/pipeline-integrated/'


printf "run time start: " >> log.txt
date >> log.txt

cp current_settings.py $current settings.py
cp current_pipeline.py $current pipeline.py

cp current_settings.py  $logdir/settings_`date +%Y%m%d`.py
cp current_pipeline.py  $logdir/pipeline_`date +%Y%m%d`.py

cat

cd $current

#run pipeline

cd $dir

printf "run time end: " >> log.txt
date >> log.txt
end=$(date +%m)
echo "Elapsed Time: $(($end-$start)) minutes" >> log.txt




cp log.txt $logdir/log_`date +%Y%m%d`.txt
   

 
 
 
 

