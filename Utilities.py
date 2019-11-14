#!/usr/bin/env python
# coding: utf-8
# @author Avijit Roy

# In[1]:

#Importing the necessary modules

import random
import pickle
import random
import time
import pprint
import math
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


class Utilities:
    def __init__(self):
        pass
    
    def showQ(self,Q,iteration_number):
        actions = ['l','r','u','d']
        max_val_array = np.zeros((81))
        max_act_array = np.zeros((81))
        for x in range(81):
            max_val = []
            for act in actions:
                #print(Q.get((x,act)))
                if Q.get((x,act)):
                    max_val.append(Q.get((x,act)))
                else:
                    max_val.append(0.0)
            if len(max_val) > 0:
                max_val_array[x] = max(max_val)
                max_act_array[x] = np.argmax(np.array(max_val))

        #print(np.reshape(max_act_array,(9,9)))
        fig, ax = plt.subplots(figsize = (50,50))
        plt.title("Q-Values " + str(iteration_number))
        ax.matshow(np.reshape(max_act_array,(9,9)), cmap='rainbow')

        location_A = self.find_location('A')
        location_B = self.find_location('B')
        print(location_A)


        for (i, j), z in np.ndenumerate(np.reshape(max_val_array,(9,9))):
            ax.text(j, i, '%2.2f'%(z), ha='center', va='center', color = 'g',
                    bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.4'),size = 11)

        #ax.text(location_A%9, int(location_A/9), 'A', ha='center', va='top', color = 'g', bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'),size = 11)

        #plt.savefig("Figure/Q-Values " + str(iteration_number))
        #plt.draw()
               
 

    def plot_unique_states_visited(self,array,mean,ch):
        plt.clf()
        plt.plot(array)
        plt.axhline(y=mean,c="red")
        plt.title("Number of Unique States Visited by Agent " + ch +" and Beta:" + str(self.beta))
        plt.ylabel("Number of States")
        plt.xlabel("Episode Number")
        plt.savefig("./Figure/01_Oct_2019/Agent_"+ ch +"_BetaValue_" + str(self.beta) + ".png")
        



    
    def showGrid(self, grid):
        print("------------------------------------")
        print("------------------------------------")
        pprint.pprint(grid[0:9])
        pprint.pprint(grid[9:18])
        pprint.pprint(grid[18:27])
        pprint.pprint(grid[27:36])
        pprint.pprint(grid[36:45])
        pprint.pprint(grid[45:54])
        pprint.pprint(grid[54:63])
        pprint.pprint(grid[63:72])
        pprint.pprint(grid[72:81])
        print("------------------------------------")
        print("------------------------------------")


        #plt.show()  







