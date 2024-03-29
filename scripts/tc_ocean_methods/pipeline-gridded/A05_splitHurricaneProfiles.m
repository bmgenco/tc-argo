close all;
clear;

%% -> settings.py
cd(<PY:MAIN_WD>)
addpath(genpath(pwd))
minNumberOfObs = <PY:MIN_OBS>;
windowSize = <PY:WINDOW_SIZE>;


load(['./Data/gridTempProfFiltered_',num2str(windowSize), '_',num2str(minNumberOfObs),'.mat']);
HurMask = readmatrix('./Masks/<PY:MASK_NAME>')';

% prefix='./Data/gridTempProfHurricane_'
prefix = '<PY:GRID_TEMP_FN>'
mask = (HurMask == <PY:MASK_VALUE>)';

profLatAggrSel      = profLatAggrSel(mask);
profLongAggrSel     = profLongAggrSel(mask);
profYearAggrSel     = profYearAggrSel(mask);
profJulDayAggrSel   = profJulDayAggrSel(mask);
profFloatIDAggrSel  = profFloatIDAggrSel(mask);
profCycleNumberAggrSel = profCycleNumberAggrSel(mask);
gridTempProf        = gridTempProf(mask, :);
save([prefix,num2str(windowSize), '_', ...
        num2str(minNumberOfObs),'.mat'],...
    'profLatAggrSel','profLongAggrSel','profYearAggrSel','profJulDayAggrSel','profFloatIDAggrSel','profCycleNumberAggrSel','gridTempProf','intStart','intEnd','presGrid','-v7.3');

exit;
