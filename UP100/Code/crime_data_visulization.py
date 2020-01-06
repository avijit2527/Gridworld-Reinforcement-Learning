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
#print(df.date)

lat_long = df[["LATITUDE","LONGITUDE","date"]]



lat_long = lat_long.dropna()
#df = df.dropna()

lat_long = lat_long[lat_long['LATITUDE'].str.contains('26.', regex=False) & lat_long['LONGITUDE'].str.contains('80.', regex=False)]

lat_long['LATITUDE'] = lat_long['LATITUDE'].str.slice(0, 7)
lat_long['LONGITUDE'] = lat_long['LONGITUDE'].str.slice(0, 7)
lat_long['date'] = pd.to_datetime(lat_long['date'],format = "%Y-%m-%dT%H:%M:%S.000Z")

lat_long =  lat_long[~lat_long['LATITUDE'].str.contains('-', regex=False) & ~lat_long['LATITUDE'].str.contains('\..*\.', regex=True) & ~lat_long['LONGITUDE'].str.contains('-', regex=False) & ~lat_long['LONGITUDE'].str.contains('\..*\.', regex=True)]


convert_dict = {'LATITUDE': float, 
                'LONGITUDE': float
               } 
lat_long = lat_long.astype(convert_dict) 


height,width = ut.lat_long_to_grid(lat_long["LATITUDE"],lat_long["LONGITUDE"],102,64)
crime_grid_array = []
crime_grid_array_for_unique = []
for a,b in zip(height,width):
    crime_grid_array.append([a,b])
    crime_grid_array_for_unique.append((a,b))
    #print(a,b)
    
unique_crime_grid_array = set(crime_grid_array_for_unique)
print(len(unique_crime_grid_array))
np.save("location_in_grid.npy", crime_grid_array)

hour_list = []
day_list = []
for x in  lat_long['date']:
    hour_list.append(x.hour)
    day_list.append(x.date())


plt.hist(hour_list,bins=np.arange(25))
plt.show()

for loc in unique_crime_grid_array:
    temp_hour_list = []
    for hour, grid in zip(hour_list, crime_grid_array_for_unique):
        if loc == grid:
            temp_hour_list.append(hour)


    plt.hist(temp_hour_list,bins=np.arange(25))
    plt.title(str(loc))
    plt.show()
    plt.close()

