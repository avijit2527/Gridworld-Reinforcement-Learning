#!/usr/bin/env python
# coding: utf-8
# @author Avijit Roy


# In[ ]:

#Importing the required module
import random
import pickle
import time
import os
import math
import numpy as np
import datetime
import glob
from PIL import Image

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



   
   
   
   
   

x = datetime.datetime.now()
now = str(x)[0:10] 



distance_from_reward_states_array_over_multiple_runs_proximity = np.load("./graph_data/Average_Distance_from_Reward_States_vs_numAgents_proximity.npy")
distance_from_reward_states_array_over_multiple_runs_proximity_instant = np.load("./graph_data/Average_Distance_from_Reward_States_vs_numAgents_proximity_instant_reward.npy")
distance_from_reward_states_array_over_multiple_runs_proximity_instant_step = np.load("./graph_data/Average_Distance_from_Reward_States_vs_numAgents_proximity_instant_step_reward.npy")
distance_from_reward_states_array_over_multiple_runs_random_agent = np.load("./graph_data/Average_Distance_from_Reward_States_vs_numAgents_random_agent.npy")


mean_distance_from_reward_states_array_proximity = np.mean(distance_from_reward_states_array_over_multiple_runs_proximity, axis = 0)
mean_distance_from_reward_states_array_proximity_instant = np.mean(distance_from_reward_states_array_over_multiple_runs_proximity_instant, axis = 0)
mean_distance_from_reward_states_array_proximity_instant_step = np.mean(distance_from_reward_states_array_over_multiple_runs_proximity_instant_step, axis = 0)
mean_distance_from_reward_states_array_random_agent = np.mean(distance_from_reward_states_array_over_multiple_runs_random_agent, axis = 0)


#Plotting coverage vs number of agents
fig, ax = plt.subplots()
ax.plot(mean_distance_from_reward_states_array_proximity.T[0],mean_distance_from_reward_states_array_proximity.T[1], c='r',label = "proximity_reward")
ax.plot(mean_distance_from_reward_states_array_proximity_instant.T[0],mean_distance_from_reward_states_array_proximity_instant.T[1], c='g',label = "proximity_reward + instant_reward")
ax.plot(mean_distance_from_reward_states_array_proximity_instant_step.T[0],mean_distance_from_reward_states_array_proximity_instant_step.T[1], c='y',label = "proximity_reward + instant_reward + step_penalty")
ax.plot(mean_distance_from_reward_states_array_random_agent.T[0],mean_distance_from_reward_states_array_random_agent.T[1], c='b',label = "random_agent")

plt.title("Average_Distance_from_Reward_States vs Num_of_Agents")
plt.xlabel("Num_of_Agents")
plt.ylabel("Average_Distance_from_Reward_States")
plt.legend()

if not os.path.exists("../Figure/%s"%(now)):
    os.makedirs("../Figure/%s"%(now))
plt.savefig("../Figure/%s/Average_Distance_from_Reward_States_vs_numAgents_proximity_instant_reward.png"%(now))
plt.close()
   




