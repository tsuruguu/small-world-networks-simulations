"""
Reproduces the key result of Watts & Strogatz (1998): as the rewiring probability p grows,
the average path length L(p) collapses long before the clustering coefficient C(p) does.

Prints C(p)/C(0) and L(p)/L(0) for a range of p, the values for the two extreme graphs
(ring lattice, p = 0, and random graph, p = 1), and a comparison with the
Barrat–Weigt approximation C(p) ≈ C(0) (1 - p)^3.

Results are also written to results/ws_curves.csv (used by plots.py).

Usage:
    python ws_simulation.py
"""
import csv
import os
import statistics as st

import networkx as nx

N, K = 1000, 10          # vertices, ring neighbours (even)
REPEATS = 3              # realisations averaged for each p
P_VALUES = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]


def main():
    g0 = nx.watts_strogatz_graph(N, K, 0, seed=1)
    C0 = nx.average_clustering(g0)
    L0 = nx.average_shortest_path_length(g0)
    print(f"Ring lattice: C(0) = {C0:.3f} (theory 3(K-2)/(4(K-1)) = {3 * (K - 2) / (4 * (K - 1)):.3f}), "
          f"L(0) = {L0:.2f}")

    rows = []
    print("\n      p     C/C0    L/L0       C       L")
    for p in P_VALUES:
        cs, ls = [], []
        for s in range(REPEATS):
            # the "connected" variant re-samples if rewiring disconnects the graph
            g = nx.connected_watts_strogatz_graph(N, K, p, seed=10 + s)
            cs.append(nx.average_clustering(g))
            ls.append(nx.average_shortest_path_length(g))
        C, L = st.mean(cs), st.mean(ls)
        rows.append((p, C / C0, L / L0, C, L))
        print(f"{p:<8} {C / C0:6.3f}  {L / L0:6.3f}  {C:6.3f}  {L:6.2f}")

    print("\nBarrat–Weigt approximation (1 - p)^3 vs simulation:")
    for p, c_norm, *_ in rows:
        if p in (0.01, 0.1, 0.3):
            print(f"  p = {p:<5}  formula {(1 - p) ** 3:.3f}   simulation {c_norm:.3f}")

    os.makedirs("results", exist_ok=True)
    with open("results/ws_curves.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["p", "C_over_C0", "L_over_L0", "C", "L"])
        w.writerows(rows)
    print("\nSaved results/ws_curves.csv")


if __name__ == "__main__":
    main()
