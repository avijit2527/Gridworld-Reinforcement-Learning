#!/usr/bin/env python
# coding: utf-8
# @author Avijit Roy


# In[ ]:

#Importing the required module
import numpy as np
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
from Utilities import Utilities as ut


x = datetime.datetime.now()
now = str(x)[0:10] 





df = pd.read_csv("../Dataset/Kanpur_city_fir_data_full.csv")
#print(df.head())

lat_long = df[["LATITUDE","LONGITUDE","date"]]



lat_long = lat_long.dropna()
#df = df.dropna()

lat_long = lat_long[lat_long['LATITUDE'].str.contains('26.', regex=False) & lat_long['LONGITUDE'].str.contains('80.', regex=False)]

lat_long['LATITUDE'] = lat_long['LATITUDE'].str.slice(0, 7)
lat_long['LONGITUDE'] = lat_long['LONGITUDE'].str.slice(0, 7)

lat_long =  lat_long[~lat_long['LATITUDE'].str.contains('-', regex=False) & ~lat_long['LATITUDE'].str.contains('\..*\.', regex=True) & ~lat_long['LONGITUDE'].str.contains('-', regex=False) & ~lat_long['LONGITUDE'].str.contains('\..*\.', regex=True)]


convert_dict = {'LATITUDE': float, 
                'LONGITUDE': float
               } 
lat_long = lat_long.astype(convert_dict) 


height,width = ut.lat_long_to_grid(lat_long["LATITUDE"],lat_long["LONGITUDE"],100,100)
crime_grid_array = []
for a,b in zip(height,width):
    crime_grid_array.append([a,b])
    print(a,b)
    
print(zip(height,width))
np.save("location_in_grid.npy", crime_grid_array)
#print(len(lat_long))

#BBox = ((df.LONGITUDE.min(), df.LONGITUDE.max(), df.LATITUDE.min(), df.LATITUDE.max()))

#print(BBox)         
   

