% Model Wattsa-Strogatza: C(p)/C(0) i L(p)/L(0)
% Dane z symulacji: N = 1000, K = 10, srednia z 3 losowan (NetworkX)

p  = [1e-4 3e-4 1e-3 3e-3 1e-2 3e-2 1e-1 3e-1 1];
C  = [1.000 1.000 0.998 0.991 0.973 0.919 0.741 0.363 0.015];
L  = [1.000 0.991 0.655 0.305 0.180 0.121 0.088 0.072 0.065];

figure('Color','w');
semilogx(p, C, '-o', 'LineWidth', 1.5, 'MarkerSize', 6, ...
         'MarkerFaceColor', [0 0.4470 0.7410]);
hold on;
semilogx(p, L, '--s', 'LineWidth', 1.5, 'MarkerSize', 6, ...
         'MarkerFaceColor', [0.8500 0.3250 0.0980]);
hold off;

xlim([1e-4 1]);
ylim([0 1.05]);
grid on;
box on;
