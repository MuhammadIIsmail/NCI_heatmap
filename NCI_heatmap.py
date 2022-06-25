# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:53:08 2022

@author: ismail
"""

import os
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def get_csv_filenames():
    '''
    Returns a list containing names of csv files in the current working directory
    '''
    files=[] #creating an empty list to which file names are appended
    cwd = os.getcwd() #getting the current working directory
    for filename in os.listdir(cwd): #iterating over all files in cwd
        if filename.endswith('.csv'): #checking if the file is a csv file
            with open(filename, 'r', newline='') as csvfile: #opening the csv file in reading mode
                df = pd.read_csv(csvfile) #creating a pandas dataframe for csv file tabular data
                if 'CELLNAME' in df.columns.values and 'GIPRCNT' in df.columns.values: #checking if the csv file contains these columns (if the files are NCI data files)
                    files.append(filename) #appending the file name in the list
    return files #returning the list with function call

def check_CELLNAME(csv_file):
    '''
    Returns a pandas dataframe containing the CELLNAME and GIPRCNT columns from the NCI csv file 
    '''
    global CELLNAME
    CELLNAME = ['CCRF-CEM', 'HL-60(TB)', 'K-562', 'MOLT-4', 'RPMI-8226', 'SR', 'A549/ATCC', 
                'EKVX', 'HOP-62', 'HOP-92', 'NCI-H226', 'NCI-H23', 'NCI-H322M', 'NCI-H460', 
                'NCI-H522', 'COLO 205', 'HCC-2998', 'HCT-116', 'HCT-15', 'HT29', 'KM12', 'SW-620', 
                'SF-268', 'SF-295', 'SF-539', 'SNB-19', 'SNB-75', 'U251', 'LOX IMVI', 'MALME-3M', 
                'M14', 'MDA-MB-435', 'SK-MEL-2', 'SK-MEL-28', 'SK-MEL-5', 'UACC-257', 'UACC-62', 
                'IGROV1', 'OVCAR-3', 'OVCAR-4', 'OVCAR-5', 'OVCAR-8', 'NCI/ADR-RES', 'SK-OV-3', 
                '786-0', 'A498', 'ACHN', 'CAKI-1', 'RXF 393', 'SN12C', 'TK-10', 'UO-31', 'PC-3', 
                'DU-145', 'MCF7', 'MDA-MB-231/ATCC', 'HS 578T', 'BT-549', 'T-47D', 'MDA-MB-468']
    
    df = pd.read_csv(csv_file)
    df = df[['CELLNAME', 'GIPRCNT']]
    for i in range(len(df)):
        if df['CELLNAME'][i] != CELLNAME[i]:
            df2 = pd.DataFrame(np.insert(df.values, i, values=[str(CELLNAME[i]), 'nan'], axis=0), columns=df.columns)
            df = df2
        df.rename(columns = {'GIPRCNT':csv_file.split('.')[0]}, inplace = True)
    return df

def merge_NCI_data(files):
    dfn = check_CELLNAME(files[0])
    for file in files[1:]:            
        df1 = check_CELLNAME(file)
        dfn = pd.merge(dfn, df1)
    dfn.to_csv('out.csv', index=False)
    dfn.set_index('CELLNAME', inplace=True)
    dfn_t = dfn.transpose()
    print(dfn_t)
    dfn_t.to_csv('out_t.csv')
    return dfn_t
        
def plot_data():
    data = pd.read_csv('out.csv', index_col='CELLNAME')
    data_transpose = data.transpose()
    plt.figure(figsize=(len(get_csv_filenames())*0.56,len(get_csv_filenames())*0.25))
    sb.heatmap(data=data_transpose, cmap="YlGnBu_r")
    
    plt.xlabel('CELLNAME')
    plt.ylabel('COMPOUNDS')
    
    plt.savefig('NCI_heatmap.png', dpi=300, bbox_inches='tight')
    #plt.show()

def main():
    merge_NCI_data(get_csv_filenames())
    plot_data()
    
if __name__ == '__main__':
    main()
    