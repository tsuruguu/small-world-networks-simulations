"""
Symulacja modelu Wattsa–Strogatza.
Liczy znormalizowane C(p)/C(0) i L(p)/L(0) dla różnych p (dane do wykresu „L spada dużo wcześniej niż C”)
oraz wartości dla siatki (p = 0) i grafu losowego (p = 1) ze slajdu „Dwa skrajne grafy”.

Wymaga: pip install networkx
"""
import statistics as st
import networkx as nx

N, K = 1000, 10          # liczba wierzchołków, liczba sąsiadów (parzysta)
POWTORZENIA = 3          # ile losowań uśredniamy dla każdego p
P = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1]

# siatka pierścieniowa (p = 0)
g0 = nx.watts_strogatz_graph(N, K, 0, seed=1)
C0 = nx.average_clustering(g0)
L0 = nx.average_shortest_path_length(g0)
print(f"Siatka: C(0) = {C0:.3f} (wzór: {3*(K-2)/(4*(K-1)):.3f}), L(0) = {L0:.2f}")

print("\n    p       C/C0    L/L0     C       L")
for p in P:
    cs, ls = [], []
    for s in range(POWTORZENIA):
        # wersja "connected" losuje ponownie, jeśli graf się rozspójni
        g = nx.connected_watts_strogatz_graph(N, K, p, seed=10 + s)
        cs.append(nx.average_clustering(g))
        ls.append(nx.average_shortest_path_length(g))
    C, L = st.mean(cs), st.mean(ls)
    print(f"{p:<8} {C/C0:6.3f}  {L/L0:6.3f}  {C:6.3f}  {L:6.2f}")

# porównanie ze wzorem Barrata–Weigta: C(p) ≈ C(0)·(1 − p)^3
print("\nWzór Barrata–Weigta (1 − p)^3:")
for p in [0.01, 0.1, 0.3]:
    print(f"  p = {p}: {(1 - p) ** 3:.3f}")
