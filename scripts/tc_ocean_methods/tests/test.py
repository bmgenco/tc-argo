#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:16:30 2023

@author: brandon
"""
import os
import sys
from datetime import datetime
import subprocess

# os.chdir(os.path.dirname(os.getcwd()))
os.chdir(os.getcwd())
# sys.path.append("../pipeline-integrated/")
# sys.path.append(os.path.abspath('../pipeline-integrated/'))

from settings import *
from tools import replace

print(MAIN_WD)

print(STORAGE_WD)

print(OCEAN_BASIN)
print(os.getcwd())

# print(pwd)

subprocess.run(["python", "inner_test.py"])