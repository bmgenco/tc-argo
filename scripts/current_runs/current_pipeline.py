import os
# os.chdir(os.getcwd())

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import sys
from datetime import datetime
import subprocess

from settings import *
from tools import replace

# need to come up with standard setting import
# from settings import *
# import settings

def matlab_run(script: str, replacement_dict: dict = {}):
    timestamp = datetime.now()
    f_out = f"temp_matlab_{datetime.now().strftime('%Y%m%d_%H%M%S')}.m"
    replace(script, f_out, replacement_dict)
    proc=subprocess.run([
        'matlab',
        '-nodisplay',
        '-nosplash',
        '-nodesktop',
        f'-r "run(\'{f_out}\');exit;"'
        ])
    if proc.returncode != 0:
        raise RuntimeError(f'Subprocess {f_out} exited with non-zero return '
                'status.')
    # cleanup
    os.remove(f_out)
    return 

# run scripts in sequential order grid only?
#

# 1. B00 
# 2. B01
# 3. A00 
# 4  A01
# 5. A02
# 6. A03
# 7. A04
# 8. B02
# 9. B03
# 10. A05
# 11. A06
# 12. A07 twice
# 13. A08
# 14. A09
## 15 A10 -> in Pipeline but not running order pdf/redme
# 16. A11
# 17. A12
# 18. B04
# 19. B05
# 20. B06
# 21. B08
# 22. B09
# 23. B10
# 24. B32
# 25. B35
# 26. B34
# 27. B36
# 28. B21
# 29 B22
# 30. B23
# 31. B24
# 32. B25
# 33. B27

# run pipeline

## A00
matlab_run('A00_processDACdata.m', {
    '<PY:ARGO_D>': ARGO_D,
    '<PY:MAIN_WD>': MAIN_WD,
    '<PY:START_YEAR>': START_YEAR,
    '<PY:END_YEAR>': END_YEAR,
    }) 


# ## B0 & B01
# subprocess.run(["python", 'B00_SlimHurricaneDatabase.py'])
# subprocess.run(["python",'B01_MarkHurricaneProfiles.py'])


# ## A01
# for YEARS in YEARS_LIST:
#     matlab_run('A01_pchipIntegration.m', {
#         '<PY:YEARS>': f'{YEARS}',
#         '<PY:DATA_LOC>': '$HOME/',
#         '<PY:GRID_LOWER>': GRID_LOWER,
#         '<PY:GRID_UPPER>': GRID_UPPER,
#     })

# ## A02
# matlab_run('A02_concatenateArrays.m')


# # should run a03 AH did not.  'years' variable to be dynamic


# ## A03
# matlab_run('A03_createDataMask.m', {
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     'PY:MIN_OBS>': MIN_OBS,
# })


# ## A04
# matlab_run('A04_filterUsingMasks.m', {
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     'PY:MIN_OBS>': MIN_OBS,
# })

# ## B02 & B03
# subprocess.run(["python",'B02_CreateHurricaneMask.py'])
# subprocess.run(["python",'B03_HurricanePairs.py'])

# ## A05: Hurricane profiles
# matlab_run('A05_splitHurricaneProfiles.m', {
#     '<PY:GRID_TEMP_FN>': './Data/gridTempProfHurricane_',
#     '<PY:MASK_VALUE>': '0',
#     '<PY:MASK_NAME>': 'NoHurMask.csv',
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     'PY:MIN_OBS>': MIN_OBS,
# })

# ## A05: Non-hurricane profiles
# matlab_run('A05_splitHurricaneProfiles.m', {
#     '<PY:GRID_TEMP_FN>': './Data/gridTempProfNonHurricane_',
#     '<PY:MASK_VALUE>': '1',
#     '<PY:MASK_NAME>': 'NoHurMask.csv',
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     'PY:MIN_OBS>': MIN_OBS,
# })

# ## A06
# matlab_run('A06_estimateMeanField.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
# })


# ''' Plotting matlab
# matlab_run('A13_plotMeanField.m', {
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
# })
# '''

# # A07: subtractMean for hurricanes
# matlab_run('A07_subtractMean.m', {
#     '<PY:GRID_TEMP_FN>':        './Data/gridTempProfFiltered_',
#     '<PY:RES_TEMP_FN>':         './Data/gridTempRes_',
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
# })


# ## A07: subtractMean for non-hurricanes
# matlab_run('A07_subtractMean.m', {
#     '<PY:GRID_TEMP_FN>':        './Data/gridTempProfNonHurricane_',
#     '<PY:RES_TEMP_FN>':         './Data/gridTempResNonHurricane_',
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
# })

# ## A08
# matlab_run('A08_divideDataToMonths.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
# })

# ## A09
# matlab_run('A09_extendedData.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
# })


# ## A10: EP
# # SHOULD  SWITCH CENTER MONTH HERE. claculate based on TC season east pacific
# matlab_run('A10_filterLocalMLESpaceTime.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
#     '<PY:CENTER_MONTH>':CENTER_MONTH,
#     '<PY:OCEAN_BASIN>': '_EastPacific',
# })

# ''' run these after foucs on etnp
# ## A10: WP
# # SHOULD  SWITCH CENTER MONTH HERE. claculate based on TC season west pacific
# matlab_run('A10_filterLocalMLESpaceTime.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
#     '<PY:CENTER_MONTH>':CENTER_MONTH,
#     '<PY:OCEAN_BASIN>': '_WestPacific',
# })

# ## add A10: AS '_ArabianSea'

# ## A10: NA
#  #Centerend on September

# matlab_run('A10_filterLocalMLESpaceTime.m', {
#     '<PY:START_YEAR>': START_YEAR,
#     '<PY:END_YEAR>': END_YEAR,
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
#     '<PY:MIN_OBS>': MIN_OBS,
#     '<PY:CENTER_MONTH>': '9',
#     '<PY:OCEAN_BASIN>': '_NorthAtlantic',
# })
# '''
# # A11
# OB = [
#     # ('_NorthAtlantic', 'meshgrid(0.5:70.5,261.5:360.5)'),
#     # ('_WestPacific',   'meshgrid(0.5:65.5,105.5:187.5)'),
#     # ('_AllBasins',     'meshgrid(linspace(-89.5,89.5,180),linspace(20.5,379.5,360))'),
#     # ('_EestPacific',   ?????,
# ]


# fn = 'Results/localMLESpaceTime_Depth_{d:03d}_{ws}_20_{window_size_gp}_{cm:02d}_{sy}_{ey}{ob}.mat'
# for ob, ob_mesh in OB:
#     if not os.path.exists(fn.format(
#         ws=window_size,
#         cm=int(center_month),
#         sy=start_year,
#         ey=end_year,
#         ob=ob)):
#         print(ob)
#         matlab_run('A11_localMLESpaceTime.m', {
#             '<PY:START_YEAR>': start_year,
#             '<PY:END_YEAR>': end_year,
#             '<PY:WINDOW_SIZE>': window_size,
#             '<PY:WINDOW_SIZE_GP>': window_size_gp,
#             '<PY:CENTER_MONTH>': center_month,
#             '<PY:OCEAN_BASIN>': ob,
#             '<PY:OB_MESHGRID>': ob_mesh,
#         })

# # A12 - EP
# OB = [
#     # ('_NorthAtlantic', 'meshgrid(0.5:70.5,261.5:360.5)'),
#      # ('_WestPacific',   'meshgrid(0.5:65.5,105.5:187.5)'),
#     #('_AllBasins',     'meshgrid(linspace(-89.5,89.5,180),linspace(20.5,379.5,360))'),
#     # ('_EestPacific',   ?????,
# ]


# fn = 'Results/localMLESpaceTime_Depth_{d:03d}_{ws}_20_{window_size_gp}_{cm:02d}_{sy}_{ey}{ob}.mat'
# for ob, ob_mesh in OB:
#     print(ob)
#     matlab_run('A12_fitLocalMLESpaceTime.m', {
#         '<PY:GRID_TEMP_FN>': './Data/gridTempProfHurricane_',
#         '<PY:START_YEAR>': start_year,
#         '<PY:END_YEAR>': end_year,
#         '<PY:WINDOW_SIZE>': window_size,
#         '<PY:MIN_OBS>': MIN_OBS,
#         '<PY:WINDOW_SIZE_GP>': window_size_gp,
#         '<PY:CENTER_MONTH>': center_month,
#         '<PY:N_PARPOOL>': '8',
#         '<PY:OCEAN_BASIN>': ob,
#         '<PY:OB_MESHGRID>': ob_mesh,
#     })


# # files in both
# subprocess.run(["python",'B04_ProfileDict.py'])
# subprocess.run(["python",'B05_AttachTemps.py'])
# subprocess.run(["python",'B06_KernelSmoothedEstimates.py'])
# subprocess.run(["python",'B08_CreateMleCoefficientDF.py'])
# subprocess.run(["python",'B09_DiagonalCovariance.py'])
# subprocess.run(["python",'B10_BlockCovariance.py'])
# subprocess.run(["python",'B32_TpsLoocvExtended.py'])
# subprocess.run(["python",'B35_TpsLoocvExtended.py'])
# subprocess.run(["python",'B34_AnalyzeLoocv.py'])
# subprocess.run(["python",'B36_TpsLoocvEstimates.py'])
# subprocess.run(["python",'B21_TPS_ThreePanel.py'])
# subprocess.run(["python",'B22_KS_ThreePanel.py'])

# # plotting
# ## files in gridded only (perhaps a lopp will or settings varible will need to be defined)

# if sys.argv[1] == "gridded":
#     os.system('B23_VerticalMixing_ThreePanel.py')
#     os.system('B24_TimeDepth_ThreePanel.py')
#     os.system('B25_DepthCrosstrack_ThreePanel.py')
#     os.system('B27_PlotTpsIsosurface.py')
# else:
#     os.system('C00_IntegratedThreePanel.py')




# # ploting integrated
    
# # other plotiing

# '''
# # need to adjust figure direcoty for
# matlab_run('A13_plotMeanField.m', {    
#     '<PY:WINDOW_SIZE>': WINDOW_SIZE,
# })
# '''  
