#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:05:31 2023
master variables for pipeline scripts. 
In general uppercase = Matlab, and Python = lowercase


commented out in scripts as (## or %%) -> settings.py 


@author: brandon
"""
import os

#  data files direcotry:
STORAGE_WD='/media/brandon/data_drive/tc_argo_data'

# Python scripts variables:
## directories

script_d= os.getcwd() #script working directory
main_wd=os.path.dirname(script_d) # use in matlab and python main WD


data_wd=main_wd+'Data/' #dir for intermediate script products in WD
tracks_d=STORAGE_WD+'tracks/'

# Matlab scripts variables:

## directories
MAIN_WD=main_wd
ARGO_D=STORAGE_WD+'dac/'
TRACK_D=STORAGE_WD +'tracks/'
DATA_D=data_wd



## variables
OCEAN_BASIN= '_EasternPacific'
# OCEAN_BASIN= '_WesternPacific'
# OCEAN_BASIN= '_NorthAtlantic'
# OCEAN_BASIN= '_AllBasins'


GRID_LOWER='10'
GRID_UPPER='200'
WINDOW_SIZE='8'
MIN_OBS='20'
GP_WINDOW_SIZE='8'
CENTER_MONTH='9'
START_YEAR='2007'
END_YEAR='2018'


YEARS_LIST = [
        '2007_2010',
        '2011_2014',
        '2015_2016',
        '2017_2018',
]

'''
YEARS_LIST = [
        '2007_2010',
        '2011_2014',
        '2015_2016',
        '2017_2018',
        '2018_2019',
        '2019_2020',
        '2020_2021',
        '2021_2022',
        '2022_2023',       
]

'''

'''reduncay of variables is for backwards compatibiliy
with AD's work. lowercase is python usage uppercase for passing tp matlab'''

start_year= START_YEAR
end_year=END_YEAR
window_size=WINDOW_SIZE
window_size_gp=GP_WINDOW_SIZE
center_month=CENTER_MONTH


# scripts used; B0
year_pairs = (
        (2007, 2010),
        (2011, 2014),
        (2015, 2016),
        (2017, 2018),
    )

''' To DO/ADD variables

#B27 -RGB color schemes for all of varibales of interest
'''