% Model SI na sieci Wattsa-Strogatza: odsetek zarazonych [%] w kolejnych krokach
% N = 1000, K = 10, zarazenie sasiada z prawdopodobienstwem 0.5 na krok (symulacja NetworkX)
t = 0:60;
I0 = [0.1 0.6 1.6 2.6 3.6 4.3 5.3 6.0 6.8 7.8 8.7 9.8 10.6 11.4 12.3 13.2 14.3 15.3 15.9 16.8 ...
      17.8 18.8 19.6 20.6 21.5 22.3 23.1 24.0 25.0 26.0 26.7 27.6 28.3 29.5 30.3 31.1 32.1 33.0 ...
      34.1 34.9 35.7 36.6 37.2 38.1 39.0 40.0 40.8 41.7 42.8 43.6 44.4 45.6 46.5 47.5 48.3 49.1 ...
      50.0 50.8 51.8 52.6 53.4];                                        % p = 0
I1 = [0.1 0.6 1.6 2.6 3.6 5.9 9.3 14.1 21.2 27.9 35.6 45.0 55.4 66.9 78.2 87.5 91.4 95.7 98.7 99.6 ...
      100*ones(1,41)];                                                   % p = 0.01
I2 = [0.1 0.6 1.9 4.0 11.1 26.3 55.4 87.3 97.5 99.8 100*ones(1,51)];    % p = 0.1

niebieski = [0 0.4470 0.7410];
pomarancz = [0.8500 0.3250 0.0980];
zolty     = [0.9290 0.6940 0.1250];

figure('Color','w'); hold on;
plot(t, I0, '-o',  'Color', niebieski, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', niebieski, 'MarkerIndices', 1:5:61);
plot(t, I1, '--s', 'Color', pomarancz, 'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', pomarancz, 'MarkerIndices', 1:5:61);
plot(t, I2, ':d',  'Color', zolty,     'LineWidth', 1.5, 'MarkerSize', 6, 'MarkerFaceColor', zolty,     'MarkerIndices', 1:5:61);
hold off;

xlim([0 60]); ylim([0 105]);
set(gca, 'XTick', 0:10:60, 'YTick', 0:20:100);
grid on; box on;
