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


x = datetime.datetime.now()
now = str(x)[0:10] 





df = pd.read_excel("../Dataset/KNC-Gps-23july.xlsx",names = ['Unit_ID', 'Latitude', 'Longitude', 'Date_Time', 'Date', 'Time'])
print(df.head())

print(df.size)
#df = df.dropna()
df.drop_duplicates(keep=False,inplace=True)
print(df.size)

BBox = ((df.Longitude.min(), df.Longitude.max(), df.Latitude.min(), df.Latitude.max()))

print(BBox)         
   
 
#print(df.loc[df['Unit ID'] == 'KNC0406', 'Longitude']) 
agents = (df.Unit_ID.unique())
print("Number of Agents: %d"%(len(agents)) )
  
ruh_m = plt.imread('../Figure/map.png')

latitude_difference = []
longitude_difference = []

for agent in agents:
    
    latitude = df.loc[(df['Unit_ID'] == agent),'Latitude']
    longitude = df.loc[(df['Unit_ID'] == agent),'Longitude']
    #print("Max_latitude: %f Min_latitude: %f Max_longitude: %f Min_longitude: %f Var_latitude: %f Var_longitude: %f"%(latitude.max(),latitude.min(),longitude.max(),longitude.min(),latitude.var(),longitude.var()))
    latitude_difference.append(latitude.max() - latitude.min())
    longitude_difference.append(longitude.max() - longitude.min())
    
     
    time_series = df.loc[df['Unit_ID'] == agent, 'Date_Time']
   
            
    fig, ax = plt.subplots(figsize = (8,7))
    print(df.loc[(df['Unit_ID'] == agent), 'Longitude'],df.loc[(df['Unit_ID'] == agent) , 'Latitude'])
    ax.scatter(df.loc[(df['Unit_ID'] == agent) , 'Longitude'],df.loc[(df['Unit_ID'] == agent) , 'Latitude'] , zorder=1, alpha= 1, c='b', s=10)
    ax.set_title('Plotting Spatial Data on Kanpur Map')
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
    if not os.path.exists("../Figure/%s"%(now)):
        os.makedirs("../Figure/%s"%(now))
    
    plt.savefig("../Figure/%s/Agent_%s"%(now,agent))
    

    #print(longitude_diff_in_every_five_minutes)
    #print(latiitude_diff_in_every_five_minutes)
    plt.close()
    

'''
latitude_difference = np.array(latitude_difference)
longitude_difference = np.array(longitude_difference)


print("Latitude_Mean: %f Latitude_Max: %f Latitude_Min: %f Longitude_Mean: %f Longitude_Max: %f Longitude_Min: %f"%(latitude_difference.mean(),latitude_difference.max(),latitude_difference.min(),longitude_difference.mean(),longitude_difference.max(),longitude_difference.min()))
'''

