from settings import *
import os
import h5py
import numpy as np
import pandas as pd
import pickle as pkl
from processing import Processor

os.chdir(main_wd)



def process_hurricanes(fn, prefix):
    # Read hurricane track data
    dataframe = pd.read_csv(fn)
    del dataframe['Unnamed: 0']

    # Specify hurricane to examine
    ## todo->settings/macro. var below
    hurricanes = list(set(np.array(dataframe[
            # dataframe['SEASON'] >= 2007
            dataframe['SEASON'] >= start_year
        ]['ID'])))
    hurricanes.sort()
    n = len(hurricanes)
    '''
    year_pairs = (
            (2007, 2010),
            (2011, 2014),
            (2015, 2016),
            (2017, 2018),
        )
    '''
    df_lst = []
    for sy, ey in year_pairs:
        f = h5py.File(prefix + f'Argo_data_aggr_{sy}_{ey}.mat')

        # Specify hurricane to examine
        hurricanes = list(set(np.array(dataframe[
                (dataframe['SEASON'] >= sy)
                &
                (dataframe['SEASON'] <= ey)
                ]['ID'])))
        hurricanes.sort()
        n = len(hurricanes)

        print(f'Processing years {sy} - {ey}...')

        for idx, h_id in enumerate(hurricanes):
            hurricane_df = dataframe[dataframe['ID'] == h_id]
            name = np.array(hurricane_df['NAME'])[0]
            season = np.array(hurricane_df['SEASON'])[0]
            num = np.array(hurricane_df['NUM'])[0]
            print(f'Processing {idx+1} of {n}: {name} of {season} ({h_id}).')
            P = Processor(hurricane_df, f)
            P.generate_before_floats()
            if P.float_df.shape[0] == 0:
                print('No before floats')
                continue
            P.add_after_floats()
            pair_df = P.create_pair_df()
            if pair_df is not None:
                df_lst.append(pair_df.assign(HurricaneID=h_id))

    df = pd.concat(df_lst
            ).sort_values('before_t', ascending=False
            ).drop_duplicates('after_t').reset_index(drop=True)
    df['profile_dt'] = df['after_t'] - df['before_t']
    df['hurricane_dt'] = df['after_t'] - df['proj_t']
    df = df.assign(signed_angle=lambda r:
            - r.sign * r.angle)
    return df

Basins = [
        ('AL', 'HURDAT_ATLANTIC'),
        ('EP', 'HURDAT_PACFIC'),
        ('WP', 'JTWC_WESTPACIFIC'),
        ('IO', 'JTWC_INDIANOCEAN'),
        ('SH', 'JTWC_SOUTHERNHEMISPHERE'),
        ]

df_list = []
for bs, fi in Basins:
    df = process_hurricanes(f'./Tracks/{fi}.csv',
            '/run/media/addison/BackupsSSD/ocean/Data/')
    pkl.dump(df, open(f'./Data/{bs}_PairDF.pkl', 'wb'))
    df_list.append(df)


pkl.dump(pd.concat(df_list), open('./Data/AllBasin_PairDF.pkl', 'wb'))
