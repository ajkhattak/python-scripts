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

def ReadExcelFile(infile):
    #read = pd.ExcelFile(infile)
    print ('ExcelFile')
    
def Plot(Data):
    plt.plot(Data['time'], Data['data'])
    plt.show()
    
