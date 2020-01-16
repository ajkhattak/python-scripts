import numpy as np
import os, sys
import h5py

import matplotlib.pyplot as plt
import pandas as pd

den = 1000./0.0180153

def ReadSingleFile(infile):
    data = []
    time = []

    with open(infile, 'r') as file:
        for f in file:
            if not f.startswith('#'):
                line = f.split()
                t1 = float(line[:][0])
                d1 = float(line[:][1])
                data.append(d1)
                time.append(t1)
                
    dic = dict(time= time, data=data)
    
    return dic


def WaterContentOneFile(file, var):
    var1 = var + '.cell.0'
    with h5py.File(file, 'r') as hf:
        keys = list(hf.keys())
        keys = list(hf[keys[0]].keys())
        keys = sorted(keys, key=int)
        Data = []
        for i in range(len(keys)):
            d = np.sum(hf[var1][keys[i]][:])
            Data.append(d/den)
    dat = dict()
    
    dat ["%s"%var] = Data
    
    return dat

def GetSurfVarFromVis(file, var, cellid):
    var1 = var + '.cell.0'
    with h5py.File(file, 'r') as hf:
        keys = list(hf.keys())
        keys = list(hf[keys[0]].keys())
        keys = sorted(keys, key=int)
        Data = []
        for i in range(len(keys)):
            d = hf[var1][keys[i]][cellid]
            Data.append(float(d))
    dat = dict()
    dat["%s"%var] = Data
    return dat

def GetSurfVarFromVis_All(file, var,suffix='.cell.0'):
    var1 = var + suffix
    with h5py.File(file, 'r') as hf:
        keys = list(hf.keys())
        keys = list(hf[keys[0]].keys())
        keys = sorted(keys, key=int)
        Data = []
        ncells = 0
        
        for i in range(len(keys)):
            d = hf[var1][keys[i]][:]
            d = [float(i) for i in d]
            Data.append([d])
            ncells = len(d)
    dat = dict()
    dat["%s"%var] = np.reshape(Data,(-1,ncells))
    return dat

def GetSumSurfVarFromVis(file, var):
    var1 = var + '.cell.0'
    with h5py.File(file, 'r') as hf:
        keys = list(hf.keys())
        keys = list(hf[keys[0]].keys())
        keys = sorted(keys, key=int)
        Data = []
        for i in range(len(keys)):
            d = hf[var1][keys[i]][:]
            d = np.sum(d)
            Data.append(float(d))
    dat = dict()
    dat["%s"%var] = Data
    return dat

def GetSurfVarFromVis_Moles(path,file, var):
    var1 = var + '.cell.0'
    mld = 'surface-molar_density_liquid.cell.0'
    cell_vol = 'surface-cell_volume.cell.0'
    snow_flag = False
    if 'snow' in file:
        snow_flag = True
        
    with h5py.File(file, 'r') as hf:
        keys = list(hf.keys())
        keys = list(hf[keys[0]].keys())
        keys = sorted(keys, key=int)
        Data = []
        for i in range(len(keys)):
            d_v = hf[var1][keys[i]][:]
            if (snow_flag):
                mld_v = get_density( path + 'visdump_surface_data.h5',keys[i],mld)
                area = get_density( path + 'visdump_surface_data.h5',keys[i],cell_vol)
            else:
                mld_v = hf[mld][keys[i]][:]
                area = hf[cell_vol][keys[i]][:]
            d = [x*y*z for x,y,z in zip(d_v,mld_v,area)]
            d = np.sum(d)
            Data.append(float(d))
    dat = dict()
    dat["%s"%var] = Data
    return dat

def get_density(file,key,var):
    mld = 'surface-molar_density_liquid.cell.0'
    mld_v = []
    with h5py.File(file,'r') as hf:
        mld_v = hf[var][key][:]
    return mld_v
        
def ReadExcelFile(infile):
    #read = pd.ExcelFile(infile)
    print ('ExcelFile')
    
def Plot(Data):
    plt.plot(Data['time'], Data['data'])
    plt.show()
    
