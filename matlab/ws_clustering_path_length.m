% Watts-Strogatz model: normalised clustering C(p)/C(0) and path length L(p)/L(0)
% as functions of the rewiring probability p (log scale).
% Data: python/ws_simulation.py, N = 1000, K = 10, mean of 3 realisations.

p = [1e-4 3e-4 1e-3 3e-3 1e-2 3e-2 1e-1 3e-1 1];
C = [1.000 1.000 0.998 0.991 0.973 0.919 0.741 0.363 0.015];
L = [1.000 0.991 0.655 0.305 0.180 0.121 0.088 0.072 0.065];

blue   = [0 0.4470 0.7410];
orange = [0.8500 0.3250 0.0980];

figure('Color','w');
semilogx(p, C, '-o',  'Color', blue,   'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', blue);
hold on;
semilogx(p, L, '--s', 'Color', orange, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', orange);
hold off;

xlim([1e-4 1]); ylim([0 1.05]);
grid on; box on;
% xlabel('p'); ylabel('normalised value'); legend('C(p)/C(0)', 'L(p)/L(0)');
