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


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# In[ ]:
coverage_array = []


# In[ ]:

class GridWorld:

    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.Q = {}
        self.last_grid = None
        self.q_last = 0.0
        self.state_action_last = None

        
        
            
    def game_begin(self):
        self.last_grid = None
        self.q_last  = 0.0
        self.state_action_last = None
    
    
    
    def epsilon_greedy(self, state, possible_moves):
        self.last_grid = tuple(state)
        if(random.random() < self.epsilon):
            move = random.choice(possible_moves)
            self.state_action_last = (self.last_grid,move)
            return move
        else:
            Q_list = []
            for action in possible_moves:
                Q_list.append(self.getQ(self.last_grid,action))
            maxQ = max(Q_list)
            
            if Q_list.count(maxQ) > 1:
                best_options = [i for i in range(len(possible_moves)) if Q_list[i] == maxQ]
                i = random.choice(best_options)
            else:
                i = Q_list.index(maxQ)
            self.state_action_last = (self.last_grid, possible_moves[i])
            self.q_last = self.getQ(self.last_grid, possible_moves[i])
            return possible_moves[i]
            
           
           
              
    def getQ(self, state, action):
        if(self.Q.get((state,action))) is None:
            self.Q[(state,action)] = 1.0
        return self.Q.get((state,action))      
            
            
        
    def updateQ(self, reward, state, possible_moves):
        q_list = []
        for moves in possible_moves:
            q_list.append(self.getQ(tuple(state), moves))
        if q_list:
            max_q_next = max(q_list)
        else:
            max_q_next = 0.0
        self.Q[self.state_action_last] = self.q_last + self.alpha * ((reward + self.gamma*max_q_next) - self.q_last)
        
            
            
                    
    def saveQtable(self, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(self.Q, handle, protocol = pickle.HIGHEST_PROTOCOL)
        
        
      
    def loadQtable(self, file_name):
        with open(file_name, 'rb') as handle:
            self.Q = pickle.load(handle)
        
        
        
            
# In[ ]:


class RunAgents:
    #width and height are the width and height of the gridworld
    def __init__(self, width = 10, height=10, num_agents = 2, training = False,beta = -5):
        self.width = width
        self.height = height
        self.num_agents = num_agents
        self.beta = beta
        
        self.grid = -1 * np.ones(shape=(self.width,self.height), dtype=int)
        
        self.done = False
        self.agents = np.empty([num_agents],dtype = GridWorld)
        self.reward_states = [[3,3],[3,4]]
        self.max_iter = 500
        
        x = datetime.datetime.now()
        self.time = str(x)[0:10]
        
        self.visited_states = []
        self.k_coverage = 50       #last k steps to calculate coverage
            
      
      
    def createAllPossibleIndex(self,x,y):
        result = []
        for i in range(x):
            for j in range(y):
                result.append([i,j])  
        return result
            
            
            
    def reset(self):
        if(self.training):
            self.grid = -1 * np.ones(shape=(self.width,self.height), dtype=int)
            indices = random.sample(self.createAllPossibleIndex(self.width,self.height),self.num_agents)
            for i in range(self.num_agents):
                x = indices[i][0]
                y = indices[i][1]
                self.grid[x][y] = i
                self.visited_states.append([x,y])
            return
            
           
           
    def evaluate(self, ch):             
        location = self.find_location(ch)
        distance = self.proximity(ch) 
        proximity_reward = math.exp(self.beta * distance)  
        i = 100
        for x in self.reward_states:
            i += 1
            if location[0] == x[0] and location[1] == x[1]:
                proximity_reward = 100 + proximity_reward   
        return proximity_reward , False 
            
        
        
            
    def find_location(self,ch):
        temp = np.where(self.grid == ch)
        location = [temp[0][0], temp[1][0]]
        
        return np.array(location)



    def proximity(self,ch):
        location_ch = self.find_location(ch)
        result = 0
        for x in range(self.num_agents):
            temp_location = self.find_location(x)
            result += np.linalg.norm(location_ch - temp_location)

        return  result

    
            
        
    def possible_moves(self, ch):  
        location = self.find_location(ch)
        remove = None
        return_value = ['d','l','u','r','s']
        if (location[0] == (self.height - 1))  or (self.grid[location[0]+1][location[1]] != -1):
            return_value.remove('d')
        if (location[1] == 0)  or (self.grid[location[0]][location[1]-1] != -1):
            return_value.remove('l')
        if (location[0] == 0)  or (self.grid[location[0]-1][location[1]] != -1):
            return_value.remove('u')
        if (location[1] == (self.width - 1))  or (self.grid[location[0]][location[1]+1] != -1):
            return_value.remove('r')
        return return_value
            
            
            
            
    def step(self, agent, move):
        location = self.find_location(agent)
        new_location_x = location[0]
        new_location_y = location[1]
        if move != 's':
            self.grid[location[0]][location[1]] = -1
        if move == 'd':
            new_location_x += 1
        if move == 'l':
            new_location_y -= 1
        if move == 'u':
            new_location_x -= 1
        if move == 'r':
            new_location_y += 1

        
        self.grid[new_location_x][new_location_y] = agent
        self.visited_states.append([new_location_x,new_location_y])
        reward, done = self.evaluate(agent)

        return reward, done
            
            
            
            
        
    def startTraining(self, agents):
        self.training = True
        for i in range(self.num_agents):
            if(isinstance(agents[i],GridWorld)):
                self.agents[i] = agents[i]

            
            
            
    
    def train(self, iterations):
        if(self.training):
            for i in range(iterations):
                for j in range(self.num_agents):
                    self.agents[j].game_begin()
                
                self.reset()
                done = False
                agent = 0
                episode_length = 0
                while (not done) and episode_length < self.max_iter :
                    if i%100 == 99:
                        #print(episode_length)
                        self.showGrid(self.grid,episode_length)
                        #time.sleep(1)
                    episode_length += 1
                    move = self.agents[agent].epsilon_greedy(self.find_location(agent), self.possible_moves(agent))
                    reward, done = self.step(agent,move)
                    self.agents[agent].updateQ(reward, self.find_location(agent), self.possible_moves(agent))
                    agent = (agent + 1) % self.num_agents
                    
            coverage = self.calculate_coverage(self.k_coverage)   
            coverage_array.append([self.num_agents,coverage])                 
                    
                    
                    
    
    def showGrid(self, grid_main,iteration):
        grid = grid_main.copy()

        fig,ax = plt.subplots()
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        self.mat = ax.matshow(grid)
        plt.colorbar(self.mat)
        for (i, j), z in np.ndenumerate(grid):
            ax.text(j, i, ' ', ha='center', va='center', color = 'g',
                    bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.4'),size = 11)        


        if not os.path.exists("./Figure/%s/%d/%4.4f"%(self.time,self.num_agents,self.beta)):
            os.makedirs("./Figure/%s/%d/%4.4f"%(self.time,self.num_agents,self.beta))
        plt.savefig("./Figure/%s/%d/%4.4f/%.4d.png"%(self.time,self.num_agents,self.beta,iteration))
        plt.close()
            
     
    def calculate_coverage(self, k):
         last_k = np.array(self.visited_states[-k:])
         last_k_T = last_k.T
         last_k = list(zip(last_k_T[0],last_k_T[1]))    #from 2d array to 1d array of tuple
         print(k,last_k)
         coverage = len(set(last_k))
         return coverage/(self.width*self.height)
     
            
            
    def saveStates(self):
        for i in range(self.num_agents):
            self.agents[i].saveQtable("agent%dstates"%(i))

        
        
        #save Qtables
    def loadStates(self):
        for i in range(self.num_agents):
            self.agents[i].loadQtable("agent%dstates"%(i))

            
            
            
            
            
     

num_agents_array = [3,4,5,6,7,8,9,10]
for num_agents in num_agents_array:
    beta_array = [2.5] #np.linspace(-20,20,num=50)
    for beta in beta_array:
        print(beta,num_agents)
        agents = np.empty([num_agents],dtype = GridWorld) 
        game = RunAgents(10,10,num_agents,True,beta)   
        for i in range(num_agents):
            agents[i] = GridWorld(epsilon = 0.2)
        game.startTraining(agents)
        game.train(100)
        game.saveStates()
        #Creating GIF for visulization
        x = datetime.datetime.now()
        now = str(x)[0:10]
        fp_in = "./Figure/%s/%d/%4.4f/*.png"%(now,num_agents,beta)
        if not os.path.exists("./GIF/%s/%d"%(now,num_agents)):
                os.makedirs("./GIF/%s/%d"%(now,num_agents))
        fp_out = "./GIF/%s/%d/%4.4f.gif"%(now,num_agents,beta)

        img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
        img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True, duration=300, loop=0)
       
            
            
            
#Plotting coverage vs number of agents
coverage_array = np.array(coverage_array)
fig, ax = plt.subplots()
ax.plot(coverage_array.T[0],coverage_array.T[1])
plt.show()            
            
            
            
            
            
            
            
            
            
            
            
            
