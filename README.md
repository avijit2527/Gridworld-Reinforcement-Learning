# Gridworld-Reinforcement-Learning
Updates regarding project

Colour represents the direction of the max Q-value(i.e action corresponding to the maximum Q value). 

In plots:

Purple -> Left

Cyan -> Right

Yellow -> Up

Red -> Down


### Update on 26th Sept:

*Using proximity as state representation*
1. When I did not give proximity reward, agents were exploring the entire grid and one agent was roaming around the awerd states.
2. When I gave reward as -distance, the agents were stuck at both corners near starting points and never crossing each other. They are also showing signs of maintaing distance.
