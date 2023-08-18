#!usr/bin/sudo bash 
set -e   

# (1) copies scipts into wd direcotry
# (2) runs pipeline, using seetings.py
# (3) moves files into runs direcotry with log files
# (4) clears wd



 # to do: add integrated or gridded varible to python script
 #https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/
 
start=$(date +%m)
source /home/brandon/anaconda3/etc/profile.d/conda.sh
conda activate argo

dir=$PWD
parentdir="$(dirname "$dir")"

## creating and mounting esxtrenal HD
storagedir='/media/brandon/data_drive/tc_argo_data'

#sudo mkdir -p /media/brandon/data_drive
#sudo mount -a /dev/sdb /media/brandon/data_drive

#cd /media/brandon/data_drive/tc_argo_data/
#sudo chmod -R -v 777 *

# note need to change permissions for matlab to access HD


# runs direcory in wd choose one
#rundir=$parentdir/runs/run_$(date +"%Y%m%d"_"%H%M")

# runs in external HD
#rundir=$storagedir/runs/run_$(date +"%Y%m%d"_"%H%M")
rundir=run_$(date +"%Y%m%d"_"%H%M")



mkdir $rundir

## define directory and  choose current, comment out other:
#current='../original/pipeline-gridded/'
current='../scripts/tc_ocean_methods/pipeline-gridded/'
arg1="gridded"
impl='../scripts/tc_ocean_methods/implementations'




#current='../scripts/tc_ocean_methods/pipeline-integrated/'
#arg1="integrated"

mkdir current_scripts
mkdir Data
mkdir Data/Monthly
mkdir Data/Extended
mkdir Results
mkdir Masks
mkdir Estimates
mkdir Output
mkdir Output/Figures_TPS_ThreePanel

printf "run time start: " > log.txt
date >> log.txt

# need to copy symbolic links as real files wil be redundant for some scripts
cp -RL $impl implementations
cp -RTL $current current_scripts

cp implementations/tools.py current_scripts/tools.py

cp current_settings.py current_scripts/settings.py
cp current_pipeline.py current_scripts/pipeline.py

cp current_settings.py  $rundir/settings_`date +%Y%m%d`.py
cp current_pipeline.py  $rundir/pipeline_`date +%Y%m%d`.py

cd current_scripts

echo "started pipeline at:" 
date


python pipeline.py $arg1
cd $dir

printf "run time end: " >> log.txt
date >> log.txt
end=$(date +%m)
echo "Elapsed Time: $(($end-$start)) minutes" >> log.txt

mv log.txt $rundir/log_`date +%Y%m%d`.txt
mv Output $rundir
mv Data $rundir
mv Results $rundir

mv -T $rundir $storagedir/runs/$rundir 


rm -R -- */
shopt -s extglob
rm -v !('setup_current_run.sh')


echo "finished at:"
date 

exit 0
