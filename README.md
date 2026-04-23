# 2D Ising Model & Monte Carlo Simulation

This computational physics project explores the thermodynamics of ferromagnetism using the **2D Ising Model**. By implementing the **Metropolis-Hastings Monte Carlo algorithm**, the project simulates the microscopic spin dynamics of a lattice and analyzes macroscopic properties such as magnetization and phase transitions.

## Project Overview

The Ising model is a mathematical model of ferromagnetism in statistical mechanics. The system consists of discrete magnetic dipole moments (spins) arranged on a 2D square lattice, which can be in one of two states (+1 or -1). 

This repository contains scripts to simulate the time evolution of these spins at a given temperature, visualize the domain formation, and compute the average magnetization across a range of temperatures to observe the critical phase transition (Curie temperature).

## Repository Structure

* **`01_Ising_Metropolis.py`**: The core simulation script. It initializes a 32x32 spin lattice and runs the Metropolis algorithm at a fixed temperature, exporting the lattice state at each time step to a text file.
* **`02_Ising_Animation.py`**: A visualization tool that reads the generated dataset and creates an animation using `matplotlib`, allowing the user to observe the physical evolution and clustering of the spin states.
* **`03_Phase_Transition.py`**: An advanced analytical script that calculates the system's average magnetization across a temperature range (T = 1.5 to 3.5) to locate the phase transition. **It uses the `numba` library for Just-In-Time (JIT) compilation and multi-threading**, significantly accelerating the nested Monte Carlo loops.

## Technologies Used

* **Python 3**
* **NumPy**: For efficient matrix operations and state management.
* **Matplotlib**: For rendering the spin lattice animation and plotting results.
* **Numba**: For high-performance JIT compilation and parallelization in the magnetization analysis.
