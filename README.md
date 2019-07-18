# Q-Learning
Simple pygame implementation of a Q-Learning algorithm for the *Robot in a Room* problem.
![Reference Slide](https://i.imgur.com/FDIkIPu.png)
*Slide from Lex Fridman's MIT 6.S091: Introduction to Deep Reinforcement Learning (Deep RL)*
[Full Video Here](https://www.youtube.com/watch?v=zR11FLZ-O9M&t=836s)

## What This Is
This program uses Q-Learning to find the optimal policy for a robot in a room that is comprised of 12 spaces. The robot has an 80% chance of going where you want it to go, a 10% of going to the right of that, and a 10% of going to the left of it. It's trying to find its way to the block with a +1 reward while avoiding the one that has a -1 reward. Every time it moves, it is penalized with a reward of -0.04.

Q-Learning enables it to find the expected values of taking any action in any state, assuming that it follows its policy of taking the move with the greatest expected value.