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

class Utilities:
    def __init__(self):
        pass
    
    @staticmethod
    def lat_long_to_grid(df_lat,df_long, width, height):
        _, hist_lat = np.histogram(df_lat, bins = height)
        _, hist_long = np.histogram(df_long, bins = width)
        #print(np.digitize(df_long, hist_long))
        return np.digitize(df_lat, hist_lat), np.digitize(df_long, hist_long)
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
