% Greedy search in the global e-mail experiment: share of senders choosing the next
% recipient because they are "closer geographically" vs "have a similar occupation",
% at each step of the chain.
% Data: Dodds, Muhamad & Watts (2003), Science 301, 827-829, Table 2.
step       = 1:7;
location   = [33 40 37 33 27 21 16];
occupation = [16 19 26 31 38 42 46];

blue   = [0 0.4470 0.7410];
orange = [0.8500 0.3250 0.0980];

figure('Color','w'); hold on;
plot(step, location,   '-o',  'Color', blue,   'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', blue);
plot(step, occupation, '--s', 'Color', orange, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', orange);
hold off;

xlim([0.8 7.2]); ylim([0 50]);
set(gca, 'XTick', 1:7, 'YTick', 0:10:50);
grid on; box on;
xlabel('step in chain'); ylabel('share of choices [%]');
legend('closer geographically', 'similar occupation', 'Location', 'northwest');
