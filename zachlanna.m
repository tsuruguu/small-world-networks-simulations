% Strategia zachlanna: odsetek wyborow "blizej geograficznie" vs "podobny zawod"
% w kolejnych krokach lancucha. Dane: Dodds, Muhamad, Watts (2003), Science 301, Tabela 2.
krok        = 1:7;
lokalizacja = [33 40 37 33 27 21 16];
zawod       = [16 19 26 31 38 42 46];

niebieski = [0 0.4470 0.7410];
pomarancz = [0.8500 0.3250 0.0980];

figure('Color','w'); hold on;
plot(krok, lokalizacja, '-o',  'Color', niebieski, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', niebieski);
plot(krok, zawod,       '--s', 'Color', pomarancz, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', pomarancz);
hold off;

xlim([0.8 7.2]); ylim([0 50]);
set(gca, 'XTick', 1:7, 'YTick', 0:10:50);
grid on; box on;
