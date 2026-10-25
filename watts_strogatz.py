"""
Implementacja modelu Wattsa–Strogatza wprost z pseudokodu ze slajdu (bez NetworkX),
plus liczenie C i L, żeby sprawdzić wynik.
"""
import random
from collections import deque


def watts_strogatz(N, K, p, seed=None):
    rnd = random.Random(seed)
    E = {i: set() for i in range(N)}

    # Krok 1: pierścień regularny
    for i in range(N):
        for j in range(1, K // 2 + 1):
            v = (i + j) % N
            E[i].add(v); E[v].add(i)

    # Krok 2: przepinanie (najpierw najbliżsi sąsiedzi, potem dalsi)
    for j in range(1, K // 2 + 1):
        for i in range(N):
            v = (i + j) % N
            if rnd.random() < p and v in E[i]:
                kandydaci = [w for w in range(N) if w != i and w not in E[i]]   # bez pętli i duplikatów
                if not kandydaci:
                    continue
                w = rnd.choice(kandydaci)
                E[i].discard(v); E[v].discard(i)
                E[i].add(w); E[w].add(i)
    return E


def wsp_grupowania(E):
    suma = 0.0
    for v, sasiedzi in E.items():
        s = list(sasiedzi); k = len(s)
        if k < 2:
            continue
        e = sum(1 for a in range(k) for b in range(a + 1, k) if s[b] in E[s[a]])
        suma += 2 * e / (k * (k - 1))
    return suma / len(E)


def srednia_sciezka(E):
    suma, pary = 0, 0
    for zrodlo in E:
        dist = {zrodlo: 0}; q = deque([zrodlo])
        while q:                                   # BFS
            u = q.popleft()
            for w in E[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1; q.append(w)
        suma += sum(dist.values()); pary += len(dist) - 1
    return suma / pary


if __name__ == "__main__":
    for p in [0, 0.01, 0.1, 1]:
        G = watts_strogatz(300, 10, p, seed=1)
        print(f"p = {p:<5} C = {wsp_grupowania(G):.3f}  L = {srednia_sciezka(G):.2f}")
