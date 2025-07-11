# Monte Carlo Betting Strategy Simulator

This project simulates and analyzes various betting strategies using Monte Carlo methods. It evaluates how different wagering systems perform over many simulated bets, tracking profits, losses, and bust rates. The results can be visualized using plots and saved for further analysis.

---

## Overview

The simulation models multiple betting strategies, including:

- **Simple Betting**: Constant wager size regardless of win/loss.
- **D'Alembert Strategy**: Increase wager by one unit after a loss, decrease by one unit after a win.
- **Martingale Strategy (Doubler Bettor)**: Double the wager after each loss.
- **Multiple Bettor**: Attempts to find optimal multiples for doubling down based on simulation.

Each strategy simulates rolling a virtual dice (50/50 win or loss chance) and adjusts the player's funds accordingly.

---

## Features

- Simulate thousands of betting rounds using different strategies.
- Track bust rates (how often the player loses all funds).
- Track profit rates (how often the player ends up with more money than they started).
- Plot the progression of funds over time.
- Save simulation results to CSV files for later graphing or analysis.
- Adjustable many parameters for initial funds, wager size, wager count, and multiples.

---
