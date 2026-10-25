"""
Wszystkie wykresy do prezentacji w stylu MATLAB-a (bez podpisów osi i legend).
Tworzy pliki: wykres_ws.png, kleinberg_siatka.png, kleinberg_alfa.png, epidemia.png, zachlanna.png

Wymaga: pip install matplotlib numpy
Dane liczbowe pochodzą z symulacja_ws.py, symulacja_epidemii.py oraz Tabeli 2 z Dodds i in. (2003).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# domyślne kolory MATLAB-a
NIEB = (0, 0.4470, 0.7410)
POM = (0.8500, 0.3250, 0.0980)
ZOLTY = (0.9290, 0.6940, 0.1250)
CIEMNY = (0.15, 0.15, 0.15)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True, "axes.linewidth": 0.6,
})


def styl(ax, siatka=True):
    if siatka:
        ax.grid(True, color=CIEMNY, alpha=0.15, lw=0.5)
    for s in ax.spines.values():
        s.set_color(CIEMNY)
    ax.tick_params(colors=CIEMNY, which="both")


def zapisz(fig, nazwa):
    fig.tight_layout()
    fig.savefig(nazwa, dpi=200, facecolor="white")
    plt.close(fig)


# 1. C(p)/C(0) i L(p)/L(0) ------------------------------------------------------
p = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1]
C = [1.000, 1.000, 0.998, 0.991, 0.973, 0.919, 0.741, 0.363, 0.015]
L = [1.000, 0.991, 0.655, 0.305, 0.180, 0.121, 0.088, 0.072, 0.065]
fig, ax = plt.subplots(figsize=(7, 5.25))
ax.semilogx(p, C, "-o", color=NIEB, lw=1.5, ms=6, mfc=NIEB)
ax.semilogx(p, L, "--s", color=POM, lw=1.5, ms=6, mfc=POM)
ax.set_xlim(1e-4, 1); ax.set_ylim(0, 1.05)
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.grid(True, which="major", color=CIEMNY, alpha=0.15, lw=0.5)
ax.grid(True, which="minor", color=CIEMNY, alpha=0.08, lw=0.4, ls=":")
styl(ax, siatka=False)
zapisz(fig, "wykres_ws.png")


# 2. Siatka Kleinberga ze ścieżką zachłanną ----------------------------------------
def bezier(P0, P1, P2, n=100):
    t = np.linspace(0, 1, n)[:, None]
    P0, P1, P2 = map(np.array, (P0, P1, P2))
    pts = (1 - t) ** 2 * P0 + 2 * (1 - t) * t * P1 + t ** 2 * P2
    return pts[:, 0], pts[:, 1]


SZARY = (0.6, 0.6, 0.6)
fig, ax = plt.subplots(figsize=(6.2, 5.8))
for i in range(6):
    ax.plot([0, 5], [i, i], "-", color=SZARY, lw=1)
    ax.plot([i, i], [0, 5], "-", color=SZARY, lw=1)
X, Y = np.meshgrid(range(6), range(6))
ax.plot(X.ravel(), Y.ravel(), "o", color=SZARY, ms=5, mfc="white", mew=1)
for a, c, d in [((1, 4), (3.25, 3.5), (4, 1)), ((5, 1), (3.8, 0.4), (2, 0)), ((0, 4), (0.25, 2.25), (2, 2))]:
    ax.plot(*bezier(a, c, d), "--", color=CIEMNY, lw=1)          # pozostałe skróty
ax.plot(*bezier((0, 0), (0.75, 2.5), (3, 3)), "-", color=POM, lw=2)  # skrót użyty przez ścieżkę
ax.plot([3, 4, 4, 5, 5], [3, 3, 4, 4, 5], "-", color=POM, lw=2)
ax.plot([3, 4, 4, 5], [3, 3, 4, 4], "o", color=NIEB, ms=7, mfc=NIEB)
ax.plot(0, 0, "s", color=NIEB, ms=9, mfc=NIEB)    # start s
ax.plot(5, 5, "s", color=POM, ms=9, mfc=POM)      # cel t
ax.set_aspect("equal"); ax.set_xlim(-0.5, 5.5); ax.set_ylim(-0.5, 5.5)
ax.set_xticks(range(6)); ax.set_yticks(range(6))
styl(ax, siatka=False)
zapisz(fig, "kleinberg_siatka.png")


# 3. Przejście fazowe Kleinberga: wykładnik c w T ~ n^c ---------------------------
fig, ax = plt.subplots(figsize=(7, 5.25))
a1, a2 = np.linspace(0, 2, 200), np.linspace(2, 4, 200)
ax.plot(a1, (2 - a1) / 3, "-", color=NIEB, lw=1.5)               # α < 2
ax.plot(a2, (a2 - 2) / (a2 - 1), "-", color=NIEB, lw=1.5)        # α > 2
m1, m2 = np.arange(0, 2.01, 0.5), np.arange(2.5, 4.01, 0.5)
ax.plot(m1, (2 - m1) / 3, "o", color=NIEB, ms=6, mfc=NIEB)
ax.plot(m2, (m2 - 2) / (m2 - 1), "o", color=NIEB, ms=6, mfc=NIEB)
ax.plot([2, 2], [-0.05, 0.75], "--", color=POM, lw=1.5)
ax.plot(2, 0, "s", color=POM, ms=7, mfc=POM)                     # α = 2: O(log² n)
ax.set_xlim(0, 4); ax.set_ylim(-0.05, 0.75)
ax.set_xticks(np.arange(0, 4.01, 0.5)); ax.set_yticks(np.arange(0, 0.71, 0.1))
styl(ax)
zapisz(fig, "kleinberg_alfa.png")


# 4. Epidemia SI (dane z symulacja_epidemii.py) ------------------------------------
t = np.arange(61)
I0 = [0.1, 0.6, 1.6, 2.6, 3.6, 4.3, 5.3, 6.0, 6.8, 7.8, 8.7, 9.8, 10.6, 11.4, 12.3, 13.2, 14.3, 15.3, 15.9, 16.8,
      17.8, 18.8, 19.6, 20.6, 21.5, 22.3, 23.1, 24.0, 25.0, 26.0, 26.7, 27.6, 28.3, 29.5, 30.3, 31.1, 32.1, 33.0,
      34.1, 34.9, 35.7, 36.6, 37.2, 38.1, 39.0, 40.0, 40.8, 41.7, 42.8, 43.6, 44.4, 45.6, 46.5, 47.5, 48.3, 49.1,
      50.0, 50.8, 51.8, 52.6, 53.4]
I1 = [0.1, 0.6, 1.6, 2.6, 3.6, 5.9, 9.3, 14.1, 21.2, 27.9, 35.6, 45.0, 55.4, 66.9, 78.2, 87.5, 91.4, 95.7, 98.7,
      99.6] + [100.0] * 41
I2 = [0.1, 0.6, 1.9, 4.0, 11.1, 26.3, 55.4, 87.3, 97.5, 99.8] + [100.0] * 51
fig, ax = plt.subplots(figsize=(7, 5.25))
ax.plot(t, I0, "-o", color=NIEB, lw=1.5, ms=6, mfc=NIEB, markevery=5)    # p = 0
ax.plot(t, I1, "--s", color=POM, lw=1.5, ms=6, mfc=POM, markevery=5)     # p = 0,01
ax.plot(t, I2, ":d", color=ZOLTY, lw=1.5, ms=6, mfc=ZOLTY, markevery=5)  # p = 0,1
ax.set_xlim(0, 60); ax.set_ylim(0, 105)
ax.set_xticks(range(0, 61, 10)); ax.set_yticks(range(0, 101, 20))
styl(ax)
zapisz(fig, "epidemia.png")


# 5. Strategia zachłanna: lokalizacja vs zawód (Dodds i in. 2003, Tabela 2) ----------
krok = [1, 2, 3, 4, 5, 6, 7]
lokalizacja = [33, 40, 37, 33, 27, 21, 16]
zawod = [16, 19, 26, 31, 38, 42, 46]
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(krok, lokalizacja, "-o", color=NIEB, lw=1.5, ms=6, mfc=NIEB)
ax.plot(krok, zawod, "--s", color=POM, lw=1.5, ms=6, mfc=POM)
ax.set_xlim(0.8, 7.2); ax.set_ylim(0, 50)
ax.set_xticks(krok); ax.set_yticks(range(0, 51, 10))
styl(ax)
zapisz(fig, "zachlanna.png")

print("Gotowe: wykres_ws.png, kleinberg_siatka.png, kleinberg_alfa.png, epidemia.png, zachlanna.png")
