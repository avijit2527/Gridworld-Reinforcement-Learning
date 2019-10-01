# Gridworld-Reinforcement-Learning
Updates regarding project

Colour represents the direction of the max Q-value(i.e action corresponding to the maximum Q value). 

In plots:

Purple -> Left

Cyan -> Right

Yellow -> Up

Red -> Down


### Updates on 26th Sept, 2019:

**Using proximity as state representation**
1. When I did not give proximity reward, agents were exploring the entire grid and one agent was roaming around the awerd states.
2. When I gave reward as -distance, the agents were stuck at both corners near starting points and never crossing each other. They are also showing signs of maintaing distance.


### Updates on 1st Oct, 2019:

1. I tried giving rewards for proximity as **exp(beta\*distance)**.
2. I tried beta with values from -20 to +20. I used 50 values, linearly spaced among them.
3. I used a metric unique_states_traversed. Which counts the number of unique states visited by the agent in an epoch. The details are given below.
4. Hyperparameters:
    i. Epoch Length: 500
    ii. Number of Epochs: 100
    iii. Reward States: (3,3) and (3,4) with zero indexing having rewards drawn from Normal(101,101) and Normal(102,102)
5. I have plotted graphs of unique_states_traversed for each value of beta for 100 iterations. Red line shows the mean value of unique_states_traversed for each beta value. Graphs can be found at "./Figure/01_Oct_2019/" folder.
6. **Observation**: As we increase the beta value the mean value of unique_states_traversed is decreasing. But as there is no negetive reward for steps the agent is roaming around the entire gridworld. Also when the reward is really high for maintaing distance, it does not roam around the reward states very often.
7. Graph Naming Convention: Agent_NameHere_BetaValue_ValueHere