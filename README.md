# Gridworld-Reinforcement-Learning
## Updates regarding project



### Updates on 6th Jan, 2020:
1. I have applied our model on UP100 dataset. The dimension of the gridworld is 102*64. The files can be found under UP100/Figure/2020-01-04/15/0.0050 .
2. **Problem**: As the gridworld size is large, the agents are not able to move from one place to a very different part of the state-space. So, the agents are not able to stay in places where crime rate is high. 
3. **Idea**: 
  *  Can we randomly explore the state space for some amount of time before using the learned model?
  *  Can we use some intelligent initialization so that our agents gets initialized near the crime location? 



### Updates on 09th Dec, 2019:
1. I have plotted the data for car movement on Kanpur map. There are total of 105 cars. All the movements can be found under ./UP100/Figure/2019-12-09/
![](./UP100/Figure/2019-12-09/Agent_KNC0455.png)



### Updates on 05th Dec, 2019:
1. I have done two experiments. One for visualizing the average distance of the nearest agent from the reward states and the other is for visualizing the total coverage, under different types of reward.

Average_Distance_from_Reward_States vs Num_of_Agents            |  Coverage vs Num_of_Agents
:-------------------------:|:-------------------------:
![](./Figure/2019-12-05/Average_Distance_from_Reward_States_vs_numAgents_proximity_instant_reward.png)  |  ![](./Figure/2019-12-05/coverage_vs_numAgents.png)


### Updates on 29th Nov, 2019:
1. I have changed the reward a little bit and nice behaviour is emerging. 
2. Reward is available only at certain states and those are decaying with time. Rewards emerge randomly at some specific states (I have taken number of reward states = number of agents).
3. Total_Reward = Proximity_Reward + Instant_Reward. Proximity_Reward is calculated from distance to other agents as before and Instant_Reward is awarded when an agent reaches a reward state and reward is available at that point in time.
4. **Observation**: The agents are maintaining distance between them and they are hovering around the reward states. So, there is always some agent available near the reward states and total state exploration is also high.
5. The behavior of the agents can be found at ./GIF/2019-11-29/ and ./Figure/2019-11-29/
![](./GIF/2019-11-29/8/0.5000.gif)




### Updates on 27th Nov, 2019:
1. I have created reward which drops off with time and distance from the agent, i.e, with time the random reward goes to zero and nearer agents gets more reward.
2. Reward: proximity_reward + instant_reward. proximity reward as before and instant_reward = 1000 * reward_parameter * exp(-beta * distance) where reward parameter decayes with time. Reward states are getting generated randomly.
3. **Observation**: Sometimes an agent is staying in a place for a long time, near an instant reward state and not moving in any direction. May be because other action has less Q-values associated with it and it is not able to learn that moving in the direction of reward state will give it higher rewards. 
4. Below is behaviour of when number of agents = 11. Rest can be found at ./GIF/2019-11-26/. White boxes shows reward states and their strengths.

![](./GIF/2019-11-26/11/0.5000.gif)




### Updates on 26th Nov, 2019:
1. I have plotted coverage vs k/n for k = 11 and n = (5*5) to (50 * 50). I have plotted the values in both linear and log scale.

Linear x-scale             |  Log x-scale
:-------------------------:|:-------------------------:
![](./Figure/2019-11-25/coverage_vs_k_by_n.png)  |  ![](./Figure/2019-11-25/coverage_vs_k_by_n_logScale.png)



### Updates on 25th Nov, 2019:
1. I have plotted a graph alpha vs coverage. Where alpha is learning rate in the following equation.

![](./Figure/Q_Learning.png)

2. All the figures for different number of agents can be found under ./Figure/2019-11-23/ . I have shown the graph for 11 agents.

![](./Figure/2019-11-23/11/coverage_vs_alpha.png)

3.  Alpha = 0 means that no update is happening and the agent is moving as per its initial policy. And alpha = 1 means that only the recent update is considered. Our initial policy is a random policy. And surprisingly for any number of agent(2-12), the RL algorithm is doing worse than random.



### Updates on 20th Nov, 2019:
1. I have regenerated the coverage vs num_of_agents curve by averaging over 100 runs. Std. deviation is shown by shaded portion.

![](./Figure/2019-11-20/coverage_vs_numAgents.png)

2. As there is no clear sweet point for number of agents, I have plotted another graph, i.e., coverage_per_agent vs num_of_agents. Which shows how much each agent is exploring the grid. Initially the value of this metric is high but the total exploration is low. But around 11 agents, the value of this metric is high as well as the toatal exploration.

![](./Figure/2019-11-20/coverage_per_agent_vs_numAgents.png)

3. **Traffic Control Problem Formulation Using  RL:**
   * We will create roads in a grid with different probabilities of vehicles taking a turn (Like, a vechicle is more likely to take a highway when it reaches the highway, rather then crossing it).
   * Reward can be movement movement of agent per time unit globally plus a small negative reward for congestion locally.
   * Evaluation Metric: We can compare our model with a round robin solution to check the mobility of the entire grid.

### Updates on 17th Nov, 2019:
1. Created a variable sized gridworld with variable number of agents
2. Implemented the coverage metric
3. Added a new action: 's' (remain in the same state)
4. Beta = 2.5
5. k = 50 for calculating coverage

![](./Figure/2019-11-17/CoverageVsNumOfAgents.png)   ![](./GIF/2019-11-17/6/2.5000.gif)

### Updates on 16th Nov, 2019:

1. Changed the state representation to the state value.
2. Created animation to see the behavior of the agent under different beta value.
3. **Observation**: After changing the state representation, the average distance between the agents increases with the increase in beta value. Shown in graph:

![](./Figure/2019-11-16/Average_Distance_per_Beta_Value.png)

4. For Beta Value = 11.8367 the agents are behaving int he following way (Rest can be found inside GIF folder):

![](./GIF/2019-11-16/11.8367.gif)




### Updates on 12th Nov, 2019:

1. I have calculated the average distance per iteration.
2. Plotted the graph for the distance vs number of iterations for every beta value(Can be found at Figure/2019-11-12 folder).
3. Calculated and plotted the average distance per beta value.
4. **Observation**: The two agents remain in the same state as the distance between the distance between the two agents is constant and they take the same action.

![](./Figure/2019-11-12/Average_Distance_per_Beta_Value.png)




### Updates on 1st Oct, 2019:

1. I tried giving rewards for proximity as **exp(beta\*distance)**.
2. I tried beta with values from -20 to +20. I used 50 values, linearly spaced among them.
3. I used a metric unique_states_traversed. Which counts the number of unique states visited by the agent in an epoch. The details are given below.
4. Hyperparameters:
    *  Epoch Length: 500
    *  Number of Epochs: 100
    *  Reward States: (3,3) and (3,4) with zero indexing having rewards drawn from Normal(101,101) and Normal(102,102)
5. I have plotted graphs of unique_states_traversed for each value of beta for 100 iterations. Red line shows the mean value of unique_states_traversed for each beta value. Graphs can be found at "./Figure/01_Oct_2019/" folder.
6. **Observation**: As we increase the beta value the mean value of unique_states_traversed is decreasing. But as there is no negetive reward for steps the agent is roaming around the entire gridworld. Also when the reward is really high for maintaing distance, it does not roam around the reward states very often.
7. Graph Naming Convention: Agent_NameHere_BetaValue_ValueHere




### Updates on 26th Sept, 2019:

**Using proximity as state representation**
1. When I did not give proximity reward, agents were exploring the entire grid and one agent was roaming around the award states.
2. When I gave reward as -distance, the agents were stuck at both corners near starting points and never crossing each other. They are also showing signs of maintaing distance.

Colour represents the direction of the max Q-value(i.e action corresponding to the maximum Q value). 

In plots:

Purple -> Left;  Cyan -> Right;  Yellow -> Up; Red -> Down


