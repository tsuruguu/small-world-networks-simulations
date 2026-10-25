"""
All figures in a MATLAB-like style, without titles, legends or axis labels
(those were added by hand on the slides).

Writes to ../figures/:
    ws_clustering_path_length.png   C(p)/C(0) and L(p)/L(0) vs p
    kleinberg_grid.png              Kleinberg lattice with a greedy path s -> t
    kleinberg_phase_transition.png  exponent c in T ~ n^c vs alpha
    si_epidemic.png                 infected share over time, p = 0 / 0.01 / 0.1
    greedy_search_dodds.png         "closer geographically" vs "similar occupation" per step

If results/ws_curves.csv or results/epidemic_si.csv exist (from ws_simulation.py and
epidemic_si.py), they are used; otherwise the values from the original run are used.

Usage:
    python plots.py
"""
import csv
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

# MATLAB default colour order
BLUE = (0, 0.4470, 0.7410)
ORANGE = (0.8500, 0.3250, 0.0980)
YELLOW = (0.9290, 0.6940, 0.1250)
DARK = (0.15, 0.15, 0.15)
GREY = (0.6, 0.6, 0.6)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True, "axes.linewidth": 0.6,
})


def style(ax, grid=True):
    if grid:
        ax.grid(True, color=DARK, alpha=0.15, lw=0.5)
    for s in ax.spines.values():
        s.set_color(DARK)
    ax.tick_params(colors=DARK, which="both")


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=200, facecolor="white")
    plt.close(fig)


def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))


# 1. Watts–Strogatz: C(p)/C(0) and L(p)/L(0) ------------------------------------------
def plot_ws():
    if os.path.exists("results/ws_curves.csv"):
        rows = read_csv("results/ws_curves.csv")
        p = [float(r["p"]) for r in rows]
        C = [float(r["C_over_C0"]) for r in rows]
        L = [float(r["L_over_L0"]) for r in rows]
    else:  # N = 1000, K = 10, mean of 3 realisations
        p = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1]
        C = [1.000, 1.000, 0.998, 0.991, 0.973, 0.919, 0.741, 0.363, 0.015]
        L = [1.000, 0.991, 0.655, 0.305, 0.180, 0.121, 0.088, 0.072, 0.065]
    fig, ax = plt.subplots(figsize=(7, 5.25))
    ax.semilogx(p, C, "-o", color=BLUE, lw=1.5, ms=6, mfc=BLUE)
    ax.semilogx(p, L, "--s", color=ORANGE, lw=1.5, ms=6, mfc=ORANGE)
    ax.set_xlim(1e-4, 1)
    ax.set_ylim(0, 1.05)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.grid(True, which="major", color=DARK, alpha=0.15, lw=0.5)
    ax.grid(True, which="minor", color=DARK, alpha=0.08, lw=0.4, ls=":")
    style(ax, grid=False)
    save(fig, "ws_clustering_path_length.png")


# 2. Kleinberg lattice with a greedy path ---------------------------------------------
def bezier(p0, p1, p2, n=100):
    t = np.linspace(0, 1, n)[:, None]
    p0, p1, p2 = map(np.array, (p0, p1, p2))
    pts = (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2
    return pts[:, 0], pts[:, 1]


def plot_kleinberg_grid():
    fig, ax = plt.subplots(figsize=(6.2, 5.8))
    for i in range(6):
        ax.plot([0, 5], [i, i], "-", color=GREY, lw=1)
        ax.plot([i, i], [0, 5], "-", color=GREY, lw=1)
    X, Y = np.meshgrid(range(6), range(6))
    ax.plot(X.ravel(), Y.ravel(), "o", color=GREY, ms=5, mfc="white", mew=1)
    # other long-range links
    for a, c, d in [((1, 4), (3.25, 3.5), (4, 1)), ((5, 1), (3.8, 0.4), (2, 0)), ((0, 4), (0.25, 2.25), (2, 2))]:
        ax.plot(*bezier(a, c, d), "--", color=DARK, lw=1)
    # greedy path: one long-range link, then lattice steps
    ax.plot(*bezier((0, 0), (0.75, 2.5), (3, 3)), "-", color=ORANGE, lw=2)
    ax.plot([3, 4, 4, 5, 5], [3, 3, 4, 4, 5], "-", color=ORANGE, lw=2)
    ax.plot([3, 4, 4, 5], [3, 3, 4, 4], "o", color=BLUE, ms=7, mfc=BLUE)
    ax.plot(0, 0, "s", color=BLUE, ms=9, mfc=BLUE)      # source s
    ax.plot(5, 5, "s", color=ORANGE, ms=9, mfc=ORANGE)  # target t
    ax.set_aspect("equal")
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_xticks(range(6))
    ax.set_yticks(range(6))
    style(ax, grid=False)
    save(fig, "kleinberg_grid.png")


# 3. Kleinberg phase transition: T ~ n^c ------------------------------------------------
def plot_kleinberg_alpha():
    # 2D lattice (d = 2): c = (2 - a)/3 for a < 2, c = (a - 2)/(a - 1) for a > 2, O(log^2 n) at a = 2
    fig, ax = plt.subplots(figsize=(7, 5.25))
    a1, a2 = np.linspace(0, 2, 200), np.linspace(2, 4, 200)
    ax.plot(a1, (2 - a1) / 3, "-", color=BLUE, lw=1.5)
    ax.plot(a2, (a2 - 2) / (a2 - 1), "-", color=BLUE, lw=1.5)
    m1, m2 = np.arange(0, 2.01, 0.5), np.arange(2.5, 4.01, 0.5)
    ax.plot(m1, (2 - m1) / 3, "o", color=BLUE, ms=6, mfc=BLUE)
    ax.plot(m2, (m2 - 2) / (m2 - 1), "o", color=BLUE, ms=6, mfc=BLUE)
    ax.plot([2, 2], [-0.05, 0.75], "--", color=ORANGE, lw=1.5)
    ax.plot(2, 0, "s", color=ORANGE, ms=7, mfc=ORANGE)
    ax.set_xlim(0, 4)
    ax.set_ylim(-0.05, 0.75)
    ax.set_xticks(np.arange(0, 4.01, 0.5))
    ax.set_yticks(np.arange(0, 0.71, 0.1))
    style(ax)
    save(fig, "kleinberg_phase_transition.png")


# 4. SI epidemic ----------------------------------------------------------------------
def plot_epidemic():
    if os.path.exists("results/epidemic_si.csv"):
        rows = read_csv("results/epidemic_si.csv")
        keys = [k for k in rows[0] if k != "t"]
        t = [int(r["t"]) for r in rows]
        I0, I1, I2 = ([float(r[k]) for r in rows] for k in keys)
    else:  # N = 1000, K = 10, beta = 0.5
        t = list(range(61))
        I0 = [0.1, 0.6, 1.6, 2.6, 3.6, 4.3, 5.3, 6.0, 6.8, 7.8, 8.7, 9.8, 10.6, 11.4, 12.3, 13.2, 14.3, 15.3,
              15.9, 16.8, 17.8, 18.8, 19.6, 20.6, 21.5, 22.3, 23.1, 24.0, 25.0, 26.0, 26.7, 27.6, 28.3, 29.5,
              30.3, 31.1, 32.1, 33.0, 34.1, 34.9, 35.7, 36.6, 37.2, 38.1, 39.0, 40.0, 40.8, 41.7, 42.8, 43.6,
              44.4, 45.6, 46.5, 47.5, 48.3, 49.1, 50.0, 50.8, 51.8, 52.6, 53.4]
        I1 = [0.1, 0.6, 1.6, 2.6, 3.6, 5.9, 9.3, 14.1, 21.2, 27.9, 35.6, 45.0, 55.4, 66.9, 78.2, 87.5, 91.4,
              95.7, 98.7, 99.6] + [100.0] * 41
        I2 = [0.1, 0.6, 1.9, 4.0, 11.1, 26.3, 55.4, 87.3, 97.5, 99.8] + [100.0] * 51
    fig, ax = plt.subplots(figsize=(7, 5.25))
    ax.plot(t, I0, "-o", color=BLUE, lw=1.5, ms=6, mfc=BLUE, markevery=5)        # p = 0
    ax.plot(t, I1, "--s", color=ORANGE, lw=1.5, ms=6, mfc=ORANGE, markevery=5)   # p = 0.01
    ax.plot(t, I2, ":d", color=YELLOW, lw=1.5, ms=6, mfc=YELLOW, markevery=5)    # p = 0.1
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 105)
    ax.set_xticks(range(0, 61, 10))
    ax.set_yticks(range(0, 101, 20))
    style(ax)
    save(fig, "si_epidemic.png")


# 5. Greedy search in the 2003 e-mail experiment ------------------------------------------
def plot_greedy():
    # Dodds, Muhamad & Watts (2003), Science 301, Table 2: reasons for choosing the next recipient (%)
    step = [1, 2, 3, 4, 5, 6, 7]
    location = [33, 40, 37, 33, 27, 21, 16]
    occupation = [16, 19, 26, 31, 38, 42, 46]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(step, location, "-o", color=BLUE, lw=1.5, ms=6, mfc=BLUE)
    ax.plot(step, occupation, "--s", color=ORANGE, lw=1.5, ms=6, mfc=ORANGE)
    ax.set_xlim(0.8, 7.2)
    ax.set_ylim(0, 50)
    ax.set_xticks(step)
    ax.set_yticks(range(0, 51, 10))
    style(ax)
    save(fig, "greedy_search_dodds.png")


if __name__ == "__main__":
    plot_ws()
    plot_kleinberg_grid()
    plot_kleinberg_alpha()
    plot_epidemic()
    plot_greedy()
    print(f"Figures saved to {os.path.normpath(OUT)}")
