# MartingaleStrategy

Overview
The Martingale Betting Strategy Simulator is a Python script that allows users to explore and analyze the Martingale betting strategy in a controlled and interactive environment. The Martingale strategy is a popular gambling technique that involves doubling the bet after each losing wager in an attempt to recover losses and potentially make a profit. This script provides a valuable tool for studying the strategy's dynamics and its potential risks.

Features
Simulation Parameters: The script allows users to customize various parameters to conduct simulations according to their preferences. These parameters include the initial bet size, the maximum number of rounds to play, and the betting limit to mitigate potential losses.

Simulation Results: After running a simulation, the script provides detailed results, including the number of rounds played, the total amount wagered, total losses, and whether the strategy resulted in a profit or led to bankruptcy. This information helps users understand the implications and outcomes of employing the Martingale strategy.

Data Visualization: The script includes data visualization capabilities, such as line charts, to illustrate the betting progression and outcomes. Visualizing the strategy's performance can assist users in gaining insights into its effectiveness and risk management.

Run the script using Python providing 4 sys arguments: # of Iterations, max # of Bets, Principal, and starting Bet Amount

Ex: python3 martingale.py 20 15 1000 100 (20 iterations of 15 bets beggining at $100)

Analyze the results to gain insights into how the Martingale strategy behaves under different conditions.
