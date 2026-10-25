% Model Kleinberga: wykladnik c w T ~ n^c w zaleznosci od alfa (siatka n x n, d = 2)
% alfa < 2: c = (2 - alfa)/3,   alfa > 2: c = (alfa - 2)/(alfa - 1),   alfa = 2: T = O(log^2 n)
niebieski = [0 0.4470 0.7410];
pomarancz = [0.8500 0.3250 0.0980];

a1 = linspace(0, 2, 200);  c1 = (2 - a1) / 3;
a2 = linspace(2, 4, 200);  c2 = (a2 - 2) ./ (a2 - 1);
m1 = 0:0.5:2;              m2 = 2.5:0.5:4;

figure('Color','w'); hold on;
plot(a1, c1, '-', 'Color', niebieski, 'LineWidth', 1.5);
plot(a2, c2, '-', 'Color', niebieski, 'LineWidth', 1.5);
plot(m1, (2 - m1)/3, 'o', 'Color', niebieski, 'MarkerSize', 6, 'MarkerFaceColor', niebieski);
plot(m2, (m2 - 2)./(m2 - 1), 'o', 'Color', niebieski, 'MarkerSize', 6, 'MarkerFaceColor', niebieski);
plot([2 2], [-0.05 0.75], '--', 'Color', pomarancz, 'LineWidth', 1.5);
plot(2, 0, 's', 'Color', pomarancz, 'MarkerSize', 7, 'MarkerFaceColor', pomarancz);
hold off;

xlim([0 4]); ylim([-0.05 0.75]);
set(gca, 'XTick', 0:0.5:4, 'YTick', 0:0.1:0.7);
grid on; box on;
