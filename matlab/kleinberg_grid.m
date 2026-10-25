% Kleinberg model: 6x6 lattice with long-range links and a greedy path s -> t.
% One long-range link plus 4 lattice steps: 5 steps instead of 10.
n = 6;
blue   = [0 0.4470 0.7410];
orange = [0.8500 0.3250 0.0980];
grey   = [0.6 0.6 0.6];
dark   = [0.15 0.15 0.15];

t = linspace(0, 1, 100);
bez = @(P0,P1,P2) deal((1-t).^2*P0(1) + 2*(1-t).*t*P1(1) + t.^2*P2(1), ...
                       (1-t).^2*P0(2) + 2*(1-t).*t*P1(2) + t.^2*P2(2));   % quadratic Bezier

figure('Color','w'); hold on;

% lattice edges and vertices
for k = 0:n-1
    plot([0 n-1], [k k], '-', 'Color', grey, 'LineWidth', 1);
    plot([k k], [0 n-1], '-', 'Color', grey, 'LineWidth', 1);
end
[X, Y] = meshgrid(0:n-1, 0:n-1);
plot(X(:), Y(:), 'o', 'Color', grey, 'MarkerSize', 5, 'MarkerFaceColor', 'w');

% other long-range links
[x,y] = bez([1 4],[3.25 3.5],[4 1]);   plot(x, y, '--', 'Color', dark, 'LineWidth', 1);
[x,y] = bez([5 1],[3.8 0.4],[2 0]);    plot(x, y, '--', 'Color', dark, 'LineWidth', 1);
[x,y] = bez([0 4],[0.25 2.25],[2 2]);  plot(x, y, '--', 'Color', dark, 'LineWidth', 1);

% greedy path
[x,y] = bez([0 0],[0.75 2.5],[3 3]);   plot(x, y, '-', 'Color', orange, 'LineWidth', 2);
plot([3 4 4 5 5], [3 3 4 4 5], '-', 'Color', orange, 'LineWidth', 2);
plot([3 4 4 5], [3 3 4 4], 'o', 'Color', blue, 'MarkerSize', 7, 'MarkerFaceColor', blue);
plot(0, 0, 's', 'Color', blue,   'MarkerSize', 9, 'MarkerFaceColor', blue);     % source s
plot(5, 5, 's', 'Color', orange, 'MarkerSize', 9, 'MarkerFaceColor', orange);   % target t
hold off;

axis equal;
xlim([-0.5 n-0.5]); ylim([-0.5 n-0.5]);
set(gca, 'XTick', 0:n-1, 'YTick', 0:n-1);
box on;
text(0.15, -0.35, 's', 'FontSize', 14, 'FontWeight', 'bold', 'Color', blue);
text(4.65, 5.15, 't', 'FontSize', 14, 'FontWeight', 'bold', 'Color', orange);
xlabel('lattice column'); ylabel('lattice row');
