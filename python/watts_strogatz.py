"""
Watts–Strogatz small-world model implemented from scratch (no NetworkX),
together with the two quantities that define a small world:

    C  - average clustering coefficient
    L  - average shortest path length (computed with BFS)

Usage:
    python watts_strogatz.py
"""
import random
from collections import deque


def watts_strogatz(n, k, p, seed=None):
    """Return an adjacency dict of a Watts–Strogatz graph.

    n    number of vertices
    k    each vertex is joined to its k nearest ring neighbours (k even)
    p    rewiring probability
    """
    if k % 2:
        raise ValueError("k must be even")
    rng = random.Random(seed)
    adj = {i: set() for i in range(n)}

    # Step 1: regular ring lattice
    for i in range(n):
        for j in range(1, k // 2 + 1):
            v = (i + j) % n
            adj[i].add(v)
            adj[v].add(i)

    # Step 2: rewiring, lap by lap (nearest neighbours first, as in the original paper)
    for j in range(1, k // 2 + 1):
        for i in range(n):
            v = (i + j) % n
            if rng.random() < p and v in adj[i]:
                # no self-loops and no duplicate edges
                candidates = [w for w in range(n) if w != i and w not in adj[i]]
                if not candidates:
                    continue
                w = rng.choice(candidates)
                adj[i].discard(v)
                adj[v].discard(i)
                adj[i].add(w)
                adj[w].add(i)
    return adj


def clustering_coefficient(adj):
    """Average local clustering coefficient C = mean of 2 e_v / (k_v (k_v - 1))."""
    total = 0.0
    for v, nbrs in adj.items():
        nbrs = list(nbrs)
        kv = len(nbrs)
        if kv < 2:
            continue
        ev = sum(1 for a in range(kv) for b in range(a + 1, kv) if nbrs[b] in adj[nbrs[a]])
        total += 2 * ev / (kv * (kv - 1))
    return total / len(adj)


def average_path_length(adj):
    """Average shortest path length over all reachable pairs (one BFS per vertex)."""
    total, pairs = 0, 0
    for source in adj:
        dist = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        total += sum(dist.values())
        pairs += len(dist) - 1
    return total / pairs


if __name__ == "__main__":
    N, K = 300, 10
    print(f"N = {N}, K = {K}")
    for p in [0, 0.01, 0.1, 1]:
        g = watts_strogatz(N, K, p, seed=1)
        print(f"p = {p:<5}  C = {clustering_coefficient(g):.3f}  L = {average_path_length(g):.2f}")
