#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:05:31 2023
master vairbles for pipeleline scripts. 
In general uppcase = matlab, lowercase
commented out in scripts as (## or %%) -> settings.py 


@author: brandon
"""
#  data files direcotry:
STORAGE_WD='/media/brandon/data_drive/tc_argo_data'

# Python scripts variables:
## directories

script_d= os.getcwd() #script working directory
main_wd=os.path.dirname(script_d) # us in matlab and python

data_wd=main_wd='Data/'
tracks_d=STORAGE_WD+'tracks/'

# Matlab scripts variables:

## directories
MAIN_WD=main_wd
ARGO_D=STORAGE_WD+'dac/'
TRACK_D=STORAGE_WD +'tracks/'



## variables

# matlab
GRID_LOWER='10'
GRID_UPPER='200'
WINDOW_SIZE='8'

#START_YEAR=2007


YEARS_LIST = [
        '2007_2010',
        '2011_2014',
        '2015_2016',
        '2017_2018',
]


# python

# scripts used; B0
year_pairs = (
        (2007, 2010),
        (2011, 2014),
        (2015, 2016),
        (2017, 2018),
    )