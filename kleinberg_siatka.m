% Model Kleinberga: siatka 6x6, skroty i sciezka zachlanna s -> t
n = 6;
niebieski = [0 0.4470 0.7410];
pomarancz = [0.8500 0.3250 0.0980];
szary     = [0.6 0.6 0.6];
ciemny    = [0.15 0.15 0.15];

t = linspace(0, 1, 100);
bez = @(P0,P1,P2) deal((1-t).^2*P0(1) + 2*(1-t).*t*P1(1) + t.^2*P2(1), ...
                       (1-t).^2*P0(2) + 2*(1-t).*t*P1(2) + t.^2*P2(2));

figure('Color','w'); hold on;

% siatka i wszystkie wierzcholki
for k = 0:n-1
    plot([0 n-1], [k k], '-', 'Color', szary, 'LineWidth', 1);
    plot([k k], [0 n-1], '-', 'Color', szary, 'LineWidth', 1);
end
[X, Y] = meshgrid(0:n-1, 0:n-1);
plot(X(:), Y(:), 'o', 'Color', szary, 'MarkerSize', 5, 'MarkerFaceColor', 'w');

% pozostale skroty
[x,y] = bez([1 4],[3.25 3.5],[4 1]);   plot(x, y, '--', 'Color', ciemny, 'LineWidth', 1);
[x,y] = bez([5 1],[3.8 0.4],[2 0]);    plot(x, y, '--', 'Color', ciemny, 'LineWidth', 1);
[x,y] = bez([0 4],[0.25 2.25],[2 2]);  plot(x, y, '--', 'Color', ciemny, 'LineWidth', 1);

% sciezka zachlanna
[x,y] = bez([0 0],[0.75 2.5],[3 3]);   plot(x, y, '-', 'Color', pomarancz, 'LineWidth', 2);
plot([3 4 4 5 5], [3 3 4 4 5], '-', 'Color', pomarancz, 'LineWidth', 2);
plot([3 4 4 5], [3 3 4 4], 'o', 'Color', niebieski, 'MarkerSize', 7, 'MarkerFaceColor', niebieski);
plot(0, 0, 's', 'Color', niebieski, 'MarkerSize', 9, 'MarkerFaceColor', niebieski);
plot(5, 5, 's', 'Color', pomarancz, 'MarkerSize', 9, 'MarkerFaceColor', pomarancz);
hold off;

axis equal;
xlim([-0.5 n-0.5]); ylim([-0.5 n-0.5]);
set(gca, 'XTick', 0:n-1, 'YTick', 0:n-1);
box on;
