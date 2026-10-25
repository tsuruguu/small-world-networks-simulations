"""
Model SI (podatny -> zarażony) na sieci Wattsa–Strogatza.
W każdym kroku każdy zarażony zaraża każdego zdrowego sąsiada z prawdopodobieństwem BETA.
Wynik: odsetek zarażonych w czasie dla p = 0, 0,01 i 0,1 oraz liczba kroków do zarażenia połowy sieci.

Wymaga: pip install networkx
"""
import random
import networkx as nx

N, K = 1000, 10
BETA = 0.5       # prawdopodobieństwo zarażenia sąsiada w jednym kroku
KROKI = 60


def symuluj_si(g, beta=BETA, kroki=KROKI, seed=0):
    rnd = random.Random(seed)
    zarazeni = {0}                       # start: jeden zarażony wierzchołek
    historia = [len(zarazeni)]
    for _ in range(kroki):
        nowi = set()
        for u in zarazeni:
            for v in g[u]:
                if v not in zarazeni and rnd.random() < beta:
                    nowi.add(v)
        zarazeni |= nowi
        historia.append(len(zarazeni))
    return [100 * x / len(g) for x in historia]   # w procentach


for p in [0, 0.01, 0.1]:
    g = nx.connected_watts_strogatz_graph(N, K, p, seed=5)
    krzywa = symuluj_si(g)
    polowa = next((t for t, x in enumerate(krzywa) if x >= 50), None)
    print(f"p = {p}: połowa sieci zarażona po {polowa} krokach")
    print("  " + " ".join(f"{x:.1f}" for x in krzywa))
