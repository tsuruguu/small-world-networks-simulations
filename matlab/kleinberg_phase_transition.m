% Kleinberg (2000): expected number of greedy-routing steps T ~ n^c on an n x n lattice (d = 2)
% where long-range links have length r with probability ~ r^(-alpha).
%   alpha < 2:  c = (2 - alpha)/3
%   alpha > 2:  c = (alpha - 2)/(alpha - 1)
%   alpha = 2:  T = O(log^2 n)
blue   = [0 0.4470 0.7410];
orange = [0.8500 0.3250 0.0980];

a1 = linspace(0, 2, 200);  c1 = (2 - a1) / 3;
a2 = linspace(2, 4, 200);  c2 = (a2 - 2) ./ (a2 - 1);
m1 = 0:0.5:2;              m2 = 2.5:0.5:4;

figure('Color','w'); hold on;
plot(a1, c1, '-', 'Color', blue, 'LineWidth', 1.5);
plot(a2, c2, '-', 'Color', blue, 'LineWidth', 1.5);
plot(m1, (2 - m1)/3, 'o', 'Color', blue, 'MarkerSize', 6, 'MarkerFaceColor', blue);
plot(m2, (m2 - 2)./(m2 - 1), 'o', 'Color', blue, 'MarkerSize', 6, 'MarkerFaceColor', blue);
plot([2 2], [-0.05 0.75], '--', 'Color', orange, 'LineWidth', 1.5);
plot(2, 0, 's', 'Color', orange, 'MarkerSize', 7, 'MarkerFaceColor', orange);
hold off;

xlim([0 4]); ylim([-0.05 0.75]);
set(gca, 'XTick', 0:0.5:4, 'YTick', 0:0.1:0.7);
grid on; box on;
% xlabel('\alpha'); ylabel('c in T \sim n^c');
