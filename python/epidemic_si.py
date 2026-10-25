"""
SI (susceptible -> infected) epidemic on Watts–Strogatz networks.

At every time step each infected vertex infects each susceptible neighbour with
probability BETA. Shows how a few shortcuts (p = 0.01 or 0.1) make an epidemic
spread far faster than on the regular ring lattice (p = 0).

Results are also written to results/epidemic_si.csv (used by plots.py).

Usage:
    python epidemic_si.py
"""
import csv
import os
import random

import networkx as nx

N, K = 1000, 10
BETA = 0.5          # infection probability per contact per step
STEPS = 60
P_VALUES = [0, 0.01, 0.1]


def simulate_si(g, beta=BETA, steps=STEPS, seed=0):
    """Return the infected percentage at t = 0..steps, starting from vertex 0."""
    rng = random.Random(seed)
    infected = {0}
    history = [len(infected)]
    for _ in range(steps):
        new = set()
        for u in infected:
            for v in g[u]:
                if v not in infected and rng.random() < beta:
                    new.add(v)
        infected |= new
        history.append(len(infected))
    return [100 * x / g.number_of_nodes() for x in history]


def main():
    curves = {}
    for p in P_VALUES:
        g = nx.connected_watts_strogatz_graph(N, K, p, seed=5)
        curves[p] = simulate_si(g)
        half = next((t for t, x in enumerate(curves[p]) if x >= 50), None)
        print(f"p = {p:<5} half of the network infected after {half} steps")

    os.makedirs("results", exist_ok=True)
    with open("results/epidemic_si.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["t"] + [f"p={p}" for p in P_VALUES])
        for t in range(STEPS + 1):
            w.writerow([t] + [f"{curves[p][t]:.1f}" for p in P_VALUES])
    print("Saved results/epidemic_si.csv")


if __name__ == "__main__":
    main()
