#!/usr/bin/env python
# coding: utf-8
# @author Avijit Roy

# In[1]:


import random
import pickle
import random
import time
import pprint
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


class GridWorld:
    def __init__(self,epsilon=0.2,alpha=0.3,gamma=0.9):
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
        
        
        
        
        


# In[3]:


class RunAgents:
    def __init__(self, training = False):
        self.grid = [' '] * 81
        
        self.done = False
        self.computer_1 = None
        self.computer_2 = None
        
        self.training = training
        self.agent1 = None
        self.agent2 = None
        self.reward_states = [30,31]
        self.max_iter = 500
        
        
        
    def reset(self):
        if(self.training):
            self.grid = [' '] * 81
            self.grid[0] = 'A'
            self.grid[80] = 'B'
            return
        
        
        
    def evaluate(self, ch):
        '''if (self.grid[8] == 'A' and self.grid[72] == 'B'):
            return 5.0, True
        if (self.grid[8] == 'A'):
            return 1.0, False
        if (self.grid[72] == 'B'):
            return 1.0, False'''
        
        
        location_A, location_B = self.find_location()
        
        if ch == 'A':
            location = location_A
        else:
            location = location_B
        i = 0
        for x in self.reward_states:
            i += 1
            if location == x:
                return ((np.random.randn()*i)+i), False
            
        return -1, False
     
        
    def find_location(self):
        iterator = 0
        location_A = 0
        location_B = 0
        for i,char in enumerate(self.grid):
            if char == 'A':
                location_A = i
            if char == 'B':
                location_B = i
            iterator += 1
        return location_A,location_B
        
        
    
    def proximity_reward(self):
        location_A,location_B = self.find_location()
        dist = abs(location_A - location_B)
        vertical_dist = int(dist/9)
        horizontal_dist = dist % 9
        return  -5/(vertical_dist + horizontal_dist  )



        
    def possible_moves(self, ch):
        location_A,location_B = self.find_location()
        remove = None
        return_value = None
        if ch == 'A':
            location = location_A
            if ((location_A + 1) == location_B) and (int(location_A/9) == int(location_B/9)):
                remove = 'r'
            elif ((location_A - 1) == location_B) and (int(location_A/9) == int(location_B/9)):
                remove = 'l'
            elif ((location_A + 9) == location_B):
                remove = 'd'
            elif ((location_A - 9) == location_B):
                remove = 'u'
                
                
        else:
            location = location_B
            if ((location_B + 1) == location_A) and (int(location_A/9) == int(location_B/9)):
                remove = 'r'
            elif ((location_B - 1) == location_A) and (int(location_A/9) == int(location_B/9)):
                remove = 'l'
            elif ((location_B + 9) == location_A):
                remove = 'd'
            elif ((location_B - 9) == location_A):
                remove = 'u'
                
                
         
        
        if location == 0:
            return_value = ['r','d']
        elif location == 8:
            return_value = ['l','d']
        elif location == 72:
            return_value = ['u','r']
        elif location == 80:
            return_value = ['u','l']
        elif location in [1,2,3,4,5,6,7]:
            return_value = ['d','r','l']
        elif location in [73,74,75,76,77,78,79]:
            return_value = ['u','r','l']
        elif location in [9,18,27,36,45,54,63]:
            return_value = ['u','d','r']
        elif location in [17,26,35,44,53,62,71]:
            return_value = ['u','d','l']
        else:
            return_value = ['u','d','l','r']
        if remove != None and (remove in return_value):
            return_value.remove(remove)
        #print(return_value)   
        return return_value
        
        
        
    def is_legal(self,location, move):
        if location == 0:
            if move not in ['r','d']:
                return False
        elif location == 8:
            if move not in ['l','d']:
                return False
        elif location == 72:
            if move not in ['u','r']:
                return False
        elif location == 80:
            if move not in ['u','l']:
                return False
        elif location in [1,2,3,4,5,6,7]:
            if move not in ['d','r','l']:
                return False
        elif location in [73,74,75,76,77,78,79]:
            if move not in ['u','r','l']:
                return False
        elif location in [9,18,27,36,45,54,63]:
            if move not in ['u','d','r']:
                return False
        elif location in [17,26,35,44,53,62,71]:
            if move not in ['u','d','l']:
                return False
        else:
            if move not in ['u','d','l','r']:
                return False
        return True
    
    
    
        
    def step(self, isA, move):
        location_A,location_B = self.find_location()

        if(isA):
            ch = "A"
            location = location_A
        else:
            ch = 'B'
            location = location_B
        if(not self.is_legal(location, move)):
            print("Illegal")
            return -10, True

        
        self.grid[location] = ' '
        if move == 'r' and isA:
            self.grid[location+1] = 'A'
        elif move == 'r':
            self.grid[location+1] = 'B'
        if move == 'l' and isA:
            self.grid[location-1] = 'A'
        elif move == 'l':
            self.grid[location-1] = 'B'
        if move == 'u' and isA:
            self.grid[location-9] = 'A'
        elif move == 'u':
            self.grid[location-9] = 'B'
        if move == 'd' and isA:
            self.grid[location+9] = 'A'
        elif move == 'd':
            self.grid[location+9] = 'B'
        if isA:    
            reward, done = self.evaluate('A')
        else:
            reward, done = self.evaluate('B')
            
        location_A,location_B = self.find_location()
        if location_A == location_B:  #Illegal
            print("Same Location Not Permitted!")
            return -10, True
            
        return reward, done
            
        
        
        
        
    def startTraining(self, agent1, agent2):
        if(isinstance(agent1,GridWorld) and isinstance(agent2,GridWorld)):
            self.training = True
            self.agent1 = agent1
            self.agent2 = agent2
            
        
    
    
    def train(self, iterations):
        start_time = time.time()
        last_time = time.time()
        if(self.training):
            reward_array = []
            for i in range(iterations):
                total_reward = 0
                '''if i%5000 == 0:
                    start_time = time.time()
                    print("Time Taken")
                    print(start_time - last_time)
                    last_time = start_time
                    print(i)'''

                self.agent1.game_begin()
                self.agent2.game_begin()
                self.reset()
                #print(self.grid)
                done = False
                isA = random.choice([True, False])
                episode_length = 0
                while (not done) and episode_length < self.max_iter :
                    '''if i%1 == 0:
                        print(episode_length)
                        self.showGrid(self.grid)
                        time.sleep(1)'''
                    episode_length += 1
                    #self.showGrid(self.grid)
                    if isA:
                        move = self.agent1.epsilon_greedy(self.grid, self.possible_moves('A'))
                    else:
                        move = self.agent2.epsilon_greedy(self.grid, self.possible_moves('B'))

                    #print(self.grid)
                    #print(move,isA) 
                    reward, done = self.step(isA,move)
                    if(isA):
                        total_reward += reward
                    #print("Reward: ",reward)
                    if (reward == -1):
                        if(isA):
                            self.agent1.updateQ(reward, self.grid, self.possible_moves('A'))
                        else:
                            self.agent2.updateQ(reward, self.grid, self.possible_moves('B'))
                        
   
                    elif (reward == -10):
                        if(isA):
                            self.agent1.updateQ(reward, self.grid, self.possible_moves('A'))
                        else:
                            self.agent2.updateQ(reward, self.grid, self.possible_moves('B'))
                            
                    else:
                        if(isA):
                            self.agent1.updateQ(reward, self.grid, self.possible_moves('A'))
                        else:
                            self.agent2.updateQ(reward, self.grid, self.possible_moves('B'))
                    
                   
                    isA = not isA

                reward_array.append(total_reward)                      
                #print("End of Epoch")
            plt.scatter(range(len(reward_array)),reward_array)
            plt.show()
               
    
    
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


                
        
    
    
        
        
    def playComputer(self, agent1, agent2):
        self.computer_1 = agent1
        self.computer_2 = agent2
        self.loadStates()
        self.computer_1.game_begin()
        self.computer_2.game_begin()
        self.reset()
        done = False
        isA = random.choice([True, False])
        episode_length = 0
        while (not done) and episode_length < self.max_iter :
            print(episode_length)
            self.showGrid(self.grid)
            time.sleep(1)
            episode_length += 1
            if isA:
                move = self.computer_1.epsilon_greedy(self.grid,self.possible_moves('A'))
            else:
                move = self.computer_2.epsilon_greedy(self.grid,self.possible_moves('B'))
            reward, done = self.step(isA,move)
            isA = not isA
                
                
                

    def saveStates(self):
        self.agent1.saveQtable("agent1states")
        self.agent2.saveQtable("agent2states")    
        
        
        #save Qtables
    def loadStates(self):
        self.computer_1.loadQtable("agent1states")
        self.computer_2.loadQtable("agent2states")

        


# In[4]:


game = RunAgents(True)
agent1 = GridWorld(epsilon = 0.2)
agent2 = GridWorld(epsilon = 0.2)
game.startTraining(agent1,agent2)
game.train(50) #train for 200,000 iterations
game.saveStates() 


# In[ ]:



agent1 = GridWorld(epsilon = 0.0)
agent2 = GridWorld(epsilon = 0.0)
game.playComputer(agent1,agent2)




