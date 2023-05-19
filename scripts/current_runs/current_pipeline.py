rom datetime import datetime
import sys
import os
import subprocess
from tools import replace

# need to come up with standard setting import
#from settings import *
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

# run scripts in squentail order gird only?
#

# 1. B00
# 2. B01
    ##3. A00 ->>> not in original pipile infe file
# 14. A01
# 5. A02
# 6. A03
# 7. A04
# 8. B02
# 9. B03
# 10. A05
# 11. A06
# 12. A07
# 13. A08
# 14. A09
    ## A10 -> in Pipeline but not running order pdf
# 15. A11
# 16. A12
# 17. B04
# 18. B05
# 19. B06
# 20. B08
# 21. B09
# 22. B10
# 23. B32
# 24. B35
# 25. B34
# 26. B36
# 27. B21
# 28. B22
# 29. B23
# 30. B24
# 31. B25
# 32. B27

os.system('B00_SlimHurricaneDatabase.py')
os.system('B01_MarkHurricaneProfiles.py')

## A00
#matlab_run('A00_processDACdata.m') # not in orignal pipelinee in script

## A01
for YEARS in YEARS_LIST:
    matlab_run('A01_pchipIntegration.m', {
        '<PY:YEARS>': f'{YEARS}',
        '<PY:DATA_LOC>': '$HOME/',
        '<PY:GRID_LOWER>': '10',
        '<PY:GRID_UPPER>': '200',
    })

## A02
matlab_run('A02_concatenateArrays.m')

'''
## A03
matlab_run('A03_createDataMask.m', {
    '<PY:WINDOW_SIZE>': '8',
})
'''

## A04
matlab_run('A04_filterUsingMasks.m', {
    '<PY:WINDOW_SIZE>': '8',
})

os.system('B02_CreateHurricaneMask.py')
os.system('B03_HurricanePairs.py')

## A05: Hurricane profiles
matlab_run('A05_splitHurricaneProfiles.m', {
    '<PY:GRID_TEMP_FN>': './Data/gridTempProfHurricane_',
    '<PY:MASK_VALUE>': '0',
    '<PY:MASK_NAME>': 'NoHurMask.csv',
    '<PY:WINDOW_SIZE>': '8',
})

## A05: Non-hurricane profiles
matlab_run('A05_splitHurricaneProfiles.m', {
    '<PY:GRID_TEMP_FN>': './Data/gridTempProfNonHurricane_',
    '<PY:MASK_VALUE>': '1',
    '<PY:MASK_NAME>': 'NoHurMask.csv',
    '<PY:WINDOW_SIZE>': '8',
}

## A06
matlab_run('A06_estimateMeanField.m', {
    '<PY:START_YEAR>': '2007',
    '<PY:END_YEAR+1>': '2019',
    '<PY:WINDOW_SIZE>': '8',
})


## A07: subtractMean for non-hurricanes
matlab_run('A07_subtractMean.m', {
    '<PY:GRID_TEMP_FN>':        './Data/gridTempProfNonHurricane_',
    '<PY:RES_TEMP_FN>':         './Data/gridTempResNonHurricane_',
    '<PY:WINDOW_SIZE>': '8',
})

## A08
matlab_run('A08_divideDataToMonths.m', {
    '<PY:START_YEAR>': '2007',
    '<PY:END_YEAR>': '2018',
    '<PY:WINDOW_SIZE>': '8',
})

## A09
matlab_run('A09_extendedData.m', {
    '<PY:START_YEAR>': '2007',
    '<PY:END_YEAR>': '2018',
    '<PY:WINDOW_SIZE>': '8',
})


## A10: WP
matlab_run('A10_filterLocalMLESpaceTime.m', {
    '<PY:START_YEAR>': '2007',
    '<PY:END_YEAR>': '2018',
    '<PY:WINDOW_SIZE>': '8',
    '<PY:CENTER_MONTH>': '9',
    '<PY:OCEAN_BASIN>': '_WestPacific',
})

## add '_ArabianSea


# ## A10: NA
# matlab_run('A10_filterLocalMLESpaceTime.m', {
#     '<PY:START_YEAR>': '2007',
#     '<PY:END_YEAR>': '2018',
#     '<PY:WINDOW_SIZE>': '8',
#     '<PY:CENTER_MONTH>': '9',
#     '<PY:OCEAN_BASIN>': '_NorthAtlantic',
# })

# A11
OB = [
    # ('_NorthAtlantic', 'meshgrid(0.5:70.5,261.5:360.5)'),
    # ('_WestPacific',   'meshgrid(0.5:65.5,105.5:187.5)'),
    ('_AllBasins',     'meshgrid(linspace(-89.5,89.5,180),linspace(20.5,379.5,360))'),
]

start_year = '2007'
end_year = '2018'
window_size = '8'
window_size_gp = '8'
center_month = '9'
fn = 'Results/localMLESpaceTime_Depth_{d:03d}_{ws}_20_{window_size_gp}_{cm:02d}_{sy}_{ey}{ob}.mat'
for ob, ob_mesh in OB:
    if not os.path.exists(fn.format(
        ws=window_size,
        cm=int(center_month),
        sy=start_year,
        ey=end_year,
        ob=ob)):
        print(ob)
        matlab_run('A11_localMLESpaceTime.m', {
            '<PY:START_YEAR>': start_year,
            '<PY:END_YEAR>': end_year,
            '<PY:WINDOW_SIZE>': window_size,
            '<PY:WINDOW_SIZE_GP>': window_size_gp,
            '<PY:CENTER_MONTH>': center_month,
            '<PY:OCEAN_BASIN>': ob,
            '<PY:OB_MESHGRID>': ob_mesh,
        })

# A12 - NA
OB = [
    # ('_NorthAtlantic', 'meshgrid(0.5:70.5,261.5:360.5)'),
    # ('_WestPacific',   'meshgrid(0.5:65.5,105.5:187.5)'),
    ('_AllBasins',     'meshgrid(linspace(-89.5,89.5,180),linspace(20.5,379.5,360))'),
]

start_year = '2007'
end_year = '2018'
window_size = '8'
window_size_gp = '8'
center_month = '9'
fn = 'Results/localMLESpaceTime_Depth_{d:03d}_{ws}_20_{window_size_gp}_{cm:02d}_{sy}_{ey}{ob}.mat'
for ob, ob_mesh in OB:
    print(ob)
    matlab_run('A12_fitLocalMLESpaceTime.m', {
        '<PY:GRID_TEMP_FN>': './Data/gridTempProfHurricane_',
        '<PY:START_YEAR>': start_year,
        '<PY:END_YEAR>': end_year,
        '<PY:WINDOW_SIZE>': window_size,
        '<PY:WINDOW_SIZE_GP>': window_size_gp,
        '<PY:CENTER_MONTH>': center_month,
        '<PY:N_PARPOOL>': '8',
        '<PY:OCEAN_BASIN>': ob,
        '<PY:OB_MESHGRID>': ob_mesh,
    })


# files in both
os.system('B04_ProfileDict.py')
os.system('B05_AttachTemps.py')
os.system('B06_KernelSmoothedEstimates.py')
os.system('B08_CreateMleCoefficientDF.py')
os.system('B09_DiagonalCovariance.py')
os.system('B10_BlockCovariance.py')
os.system('B32_TpsLoocvExtended.py')
os.system('B35_TpsLoocvExtended.py')
os.system('B34_AnalyzeLoocv.py')
os.system('B36_TpsLoocvEstimates.py')
os.system('B21_TPS_ThreePanel.py')
os.system('B22_KS_ThreePanel.py')

# plotting
## files in gridded only (perhaps a lopp will or settings varible will need to be defined)

if sys.argv[1] == "gridded"

    os.system('B23_VerticalMixing_ThreePanel.py')
    os.system('B24_TimeDepth_ThreePanel.py')
    os.system('B25_DepthCrosstrack_ThreePanel.py')
    os.system('B27_PlotTpsIsosurface.py')
else:
    os.system('C00_IntegratedThreePanel.py')

# ploting integrated
    

    
