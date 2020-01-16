
import numpy as np
import os, sys
import h5py
import pandas as pd
import matplotlib.pyplot as plt

import readdata as rd

import datetime
time_origin = datetime.datetime(2010,1,1,0,0,0)
sys.path.append('/Users/ajc/Desktop/ATS/ats-repo/ats/tools/utils/')
import plot_water_table2D

# 2012
# Well C37
def getData_2012():
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC37XL = xl.parse(sheet_name='C37',skiprows=4) #Area C, transect B
    xl.close()

    keys = DataC37XL.keys()
    DataC37_2012 = dict()
    elevation = 4.72
    wl_init = 0.10 + elevation
    mid_value = (4.9581 + 4.9101)/2.0

    # Read Time
    DataC37_2012[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC37XL[u'Date 2012']])
    DataC37_2012[u'time'] =  np.array([t/(86400.) for t in DataC37_2012[u'time'] if not np.isnan(t)])
    lenC37_2012 =  len(DataC37_2012[u'time'])

    #print lenC37_2012, lenC37_2012%96
    # Read WL
    DataC37_2012['water_level']= np.array([wl for wl in DataC37XL['Water Level 2012'][:lenC37_2012]])
    DataC37_2012['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC37_2012['water_level']])
    DataC37_2012['water_level'] = np.array([d - elevation*0 for d in DataC37_2012['water_level']])

    LC37=len(DataC37_2012['water_level'])/96
    #print (len(DataC37_2012['water_level'])/96, DataC37_2012['water_level'].shape)
    DataC37_2012['water_level_day'] = DataC37_2012['water_level'].reshape((LC37, 96)).mean(axis=1) #96 number of days
    DataC37_2012['time_day'] = DataC37_2012['time'].reshape((LC37, 96)).mean(axis=1) #96 number of days


    #C39
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC39XL = xl.parse(sheet_name='C39',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC39_2012 = dict()
    DataC39_2012[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC39XL[u'Date 2012']])
    DataC39_2012[u'time'] =  np.array([d for d in DataC39_2012[u'time'] if not np.isnan(d)])
    lenC39_2012 =  len(DataC39_2012[u'time']) - len(DataC39_2012[u'time']) %96
    #print lenC39_2012, lenC39_2012%96

    DataC39_2012['time']= np.array([t/(86400.) for t in DataC39_2012['time'][:lenC39_2012]])
    DataC39_2012['water_level']= np.array([wl for wl in DataC39XL['Water Level 2012'][:lenC39_2012]])
    DataC39_2012['water_level'] = np.array([100. if np.isnan(d) else d for d in DataC39_2012['water_level']])
    DataC39_2012['water_level'] = np.array([d - elevation*0 for d in DataC39_2012['water_level']])

    LC39=len(DataC39_2012['water_level'])/96

    DataC39_2012['water_level_day'] = DataC39_2012['water_level'].reshape((LC39, 96)).mean(axis=1) #96 number of days
    DataC39_2012['time_day'] = DataC39_2012['time'].reshape((LC39, 96)).mean(axis=1) #96 number of days


    #C40
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC40XL = xl.parse(sheet_name='C40',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC40_2012 = dict()
    DataC40_2012[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC40XL[u'Date 2012']])
    DataC40_2012[u'time'] =  np.array([d for d in DataC40_2012[u'time'] if not np.isnan(d)])
    lenC40_2012 =  len(DataC40_2012[u'time']) - len(DataC40_2012[u'time']) %96
    #print lenC40_2012, lenC40_2012%96

    DataC40_2012['time']= np.array([t/(86400.) for t in DataC40_2012['time'][:lenC40_2012]])
    DataC40_2012['water_level']= np.array([wl for wl in DataC40XL['Water Level 2012'][:lenC40_2012]])
    DataC40_2012['water_level'] = np.array([100. if np.isnan(d) else d for d in DataC40_2012['water_level']])
    DataC40_2012['water_level'] = np.array([d - elevation*0 for d in DataC40_2012['water_level']])

    LC40=len(DataC40_2012['water_level'])/96
    #print (len(DataC40_2012['water_level'])/96, DataC40_2012['water_level'].shape)
    DataC40_2012['water_level_day'] = DataC40_2012['water_level'].reshape((LC40, 96)).mean(axis=1) #96 number of days
    DataC40_2012['time_day'] = DataC40_2012['time'].reshape((LC40, 96)).mean(axis=1) #96 number of days

    DataA = dict()
    DataA['water_level_C37'] = DataC37_2012['water_level_day']
    DataA['water_level_C39'] = DataC39_2012['water_level_day']
    DataA['water_level_C40'] = DataC40_2012['water_level_day']
    DataA['time_C37'] = DataC37_2012['time_day']
    DataA['time_C39'] = DataC39_2012['time_day']
    DataA['time_C40'] = DataC40_2012['time_day']


    return DataA


# 2013
# Well C37
def getData_2013():
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC37XL = xl.parse(sheet_name='C37',skiprows=4) #Area C, transect B
    xl.close()

    keys = DataC37XL.keys()
    DataC37_2013 = dict()
    elevation = 4.72
    wl_init = 0.10 + elevation
    mid_value = (4.9581 + 4.9101)/2.0

    # Read Time
    DataC37_2013[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC37XL[u'Date 2013']])
    DataC37_2013[u'time'] =  np.array([t/86400. for t in DataC37_2013[u'time'] if not np.isnan(t)])
    lenC37_2013 =  len(DataC37_2013[u'time'])

    #print lenC37_2013, lenC37_2013%96
    # Read WL
    DataC37_2013['water_level']= np.array([wl for wl in DataC37XL['Water Level 2013'][:lenC37_2013]])
    DataC37_2013['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC37_2013['water_level']])
    DataC37_2013['water_level'] = np.array([d - elevation*0 for d in DataC37_2013['water_level']])

    LC37=len(DataC37_2013['water_level'])/96
    #print (len(DataC37_2013['water_level'])/96, DataC37_2013['water_level'].shape)
    DataC37_2013['water_level_day'] = DataC37_2013['water_level'].reshape((LC37, 96)).mean(axis=1) #96 number of days
    DataC37_2013['time_day'] = DataC37_2013['time'].reshape((LC37, 96)).mean(axis=1) #96 number of days

    #print DataC37_2013['time_day']

    #C39
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC39XL = xl.parse(sheet_name='C39',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC39_2013 = dict()
    DataC39_2013[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC39XL[u'Date 2013']])
    DataC39_2013[u'time'] =  np.array([d for d in DataC39_2013[u'time'] if not np.isnan(d)])
    lenC39_2013 =  len(DataC39_2013[u'time']) - len(DataC39_2013[u'time']) %96
    #print lenC39_2013, lenC39_2013%96

    DataC39_2013['time']= np.array([t/86400. for t in DataC39_2013['time'][:lenC39_2013]])
    DataC39_2013['water_level']= np.array([d for d in DataC39XL['Water Level 2013'][:lenC39_2013]])
    DataC39_2013['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC39_2013['water_level']])
    DataC39_2013['water_level'] = np.array([d - elevation*0 for d in DataC39_2013['water_level']])

    LC39=len(DataC39_2013['water_level'])/96
    #print (len(DataC37_2013['water_level'])/96, DataC37_2013['water_level'].shape)
    DataC39_2013['water_level_day'] = DataC39_2013['water_level'].reshape((LC39, 96)).mean(axis=1) #96 number of days
    DataC39_2013['time_day'] = DataC39_2013['time'].reshape((LC39, 96)).mean(axis=1) #96 number of days


    #C40
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC40XL = xl.parse(sheet_name='C40',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC40_2013 = dict()
    DataC40_2013[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC40XL[u'Date 2013']])
    DataC40_2013[u'time'] =  np.array([t for t in DataC40_2013[u'time'] if not np.isnan(t)])
    lenC40_2013 =  len(DataC40_2013[u'time']) - len(DataC40_2013[u'time']) %96
    #print lenC40_2013, lenC40_2013%96

    DataC40_2013['time']= np.array([t/86400. for t in DataC40_2013['time'][:lenC40_2013]])
    DataC40_2013['water_level']= np.array([wl for wl in DataC40XL['Water Level 2013'][:lenC40_2013]])
    DataC40_2013['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC40_2013['water_level']])
    DataC40_2013['water_level'] = np.array([d - elevation*0 for d in DataC40_2013['water_level']])

    LC40=len(DataC40_2013['water_level'])/96
    #print (len(DataC40_2013['water_level'])/96, DataC40_2013['water_level'].shape)
    DataC40_2013['water_level_day'] = DataC40_2013['water_level'].reshape((LC40, 96)).mean(axis=1) #96 number of days
    DataC40_2013['time_day'] = DataC40_2013['time'].reshape((LC40, 96)).mean(axis=1) #96 number of days

    DataA = dict()
    DataA['water_level_C37'] = DataC37_2013['water_level_day']
    DataA['water_level_C39'] = DataC39_2013['water_level_day']
    DataA['water_level_C40'] = DataC40_2013['water_level_day']
    DataA['time_C37'] = DataC37_2013['time_day']
    DataA['time_C39'] = DataC39_2013['time_day']
    DataA['time_C40'] = DataC40_2013['time_day']

    return DataA



# 2014 Well C37
def getData_2014():
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC37XL = xl.parse(sheet_name='C37',skiprows=4) #Area C, transect B
    xl.close()

    keys = DataC37XL.keys()
    DataC37_2014 = dict()
    elevation = 4.72
    wl_init = 0.10 + elevation
    mid_value = (4.9581 + 4.9101)/2.0

    # Read Time
    DataC37_2014[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC37XL[u'Date 2014']])
    DataC37_2014[u'time'] =  np.array([t/86400. for t in DataC37_2014[u'time'] if not np.isnan(t)])
    lenC37_2014 =  len(DataC37_2014[u'time'])

    #print lenC37_2014, lenC37_2014%96
    # Read WL
    DataC37_2014['water_level']= np.array([wl for wl in DataC37XL['Water Level 2014'][:lenC37_2014]])
    DataC37_2014['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC37_2014['water_level']])
    DataC37_2014['water_level'] = np.array([d - elevation*0 for d in DataC37_2014['water_level']])

    LC37=len(DataC37_2014['water_level'])/96
    #print (len(DataC37_2014['water_level'])/96, DataC37_2014['water_level'].shape)
    DataC37_2014['water_level_day'] = DataC37_2014['water_level'].reshape((LC37, 96)).mean(axis=1) #96 number of days
    DataC37_2014['time_day'] = DataC37_2014['time'].reshape((LC37, 96)).mean(axis=1) #96 number of days

    #C39
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC39XL = xl.parse(sheet_name='C39',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC39_2014 = dict()
    DataC39_2014[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC39XL[u'Date 2014']])
    DataC39_2014[u'time'] =  np.array([d for d in DataC39_2014[u'time'] if not np.isnan(d)])
    lenC39_2014 =  len(DataC39_2014[u'time']) - len(DataC39_2014[u'time']) %96
    #print lenC39_2014, lenC39_2014%96

    DataC39_2014['time']= np.array([t/86400. for t in DataC39_2014['time'][:lenC39_2014]])
    DataC39_2014['water_level']= np.array([d for d in DataC39XL['Water Level 2014'][:lenC39_2014]])
    DataC39_2014['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC39_2014['water_level']])
    DataC39_2014['water_level'] = np.array([d - elevation*0 for d in DataC39_2014['water_level']])

    LC39=len(DataC39_2014['water_level'])/96
    DataC39_2014['water_level_day'] = DataC39_2014['water_level'].reshape((LC39, 96)).mean(axis=1) #96 number of days
    DataC39_2014['time_day'] = DataC39_2014['time'].reshape((LC39, 96)).mean(axis=1) #96 number of days

    #C40
    xl = pd.ExcelFile('/Users/ajc/Desktop/ATS/barrow-polygon-data/water_table/NGEE_wells/RevisedNEAR-FINAL-WaterLevels-NGEESiteCNorthPolygon-AC01_29_2015.xlsx')
    xl.sheet_names
    #print (xl.sheet_names)
    DataC40XL = xl.parse(sheet_name='C40',skiprows=4) #Area C, transect B
    xl.close()

    # Read WL
    DataC40_2014 = dict()
    DataC40_2014[u'time'] = np.array([(t - time_origin).total_seconds() for t in DataC40XL[u'Date 2014']])
    DataC40_2014[u'time'] =  np.array([t for t in DataC40_2014[u'time'] if not np.isnan(t)])
    lenC40_2014 =  len(DataC40_2014[u'time']) - len(DataC40_2014[u'time']) %96
    #print lenC40_2014, lenC40_2014%96

    DataC40_2014['time']= np.array([t/86400. for t in DataC40_2014['time'][:lenC40_2014]])
    DataC40_2014['water_level']= np.array([wl for wl in DataC40XL['Water Level 2014'][:lenC40_2014]])
    DataC40_2014['water_level'] = np.array([mid_value if np.isnan(d) else d for d in DataC40_2014['water_level']])
    DataC40_2014['water_level'] = np.array([d - elevation*0 for d in DataC40_2014['water_level']])

    LC40=len(DataC40_2014['water_level'])/96
    #print (len(DataC40_2014['water_level'])/96, DataC40_2014['water_level'].shape)
    DataC40_2014['water_level_day'] = DataC40_2014['water_level'].reshape((LC40, 96)).mean(axis=1) #96 number of days
    DataC40_2014['time_day'] = DataC40_2014['time'].reshape((LC40, 96)).mean(axis=1) #96 number of days


    DataA = dict()
    DataA['water_level_C37'] = DataC37_2014['water_level_day']
    DataA['water_level_C39'] = DataC39_2014['water_level_day']
    DataA['water_level_C40'] = DataC40_2014['water_level_day']
    DataA['time_C37'] = DataC37_2014['time_day']
    DataA['time_C39'] = DataC39_2014['time_day']
    DataA['time_C40'] = DataC40_2014['time_day']


    return DataA
