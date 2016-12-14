%% Staple diagrams

clc
clear all

figure(1)
clf

dataBoarding = dlmread('boardingData500.txt');

randomBoarding = dataBoarding(2:5:end,1:2)/60;
backToFrontBoarding = dataBoarding(3:5:end,1:2)/60;
outsideInBoarding = dataBoarding(4:5:end,1:2)/60;
flyingCarpetBoarding = dataBoarding(5:5:end,1:2)/60;

meanTime = [randomBoarding(:,1) backToFrontBoarding(:,1) outsideInBoarding(:,1) flyingCarpetBoarding(:,1)];
stdTime = [randomBoarding(:,2) backToFrontBoarding(:,2) outsideInBoarding(:,2) flyingCarpetBoarding(:,2)];

colorsJet = jet;
colors = colorsJet(1:16:end,:);

colors(4,:) = [1 1 0.2];
errorbar_groups(meanTime',stdTime','FigID',1,'bar_names',{'4 seats in one row','6 seats in one row'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet','Location','northwest')
ylabel('Time [min]','Interpreter','LaTex','FontSize',16)
title('Full airplane, 100\% cabin baggage','Interpreter','LaTex','FontSize',18)
ylim([0 14])

%% 

clear all
clc

dataBoarding = dlmread('boardingData50Filled500.txt');

planeDim = dataBoarding(1:5:end,:);

nSeats = unique(planeDim(1:end,2));
nRows = planeDim(1:end/length(nSeats),1);

randomBoarding = dataBoarding(2:5:end,1:2)/60;
backToFrontBoarding = dataBoarding(3:5:end,1:2)/60;
outsideInBoarding = dataBoarding(4:5:end,1:2)/60;
flyingCarpetBoarding = dataBoarding(5:5:end,1:2)/60;

meanTime = [randomBoarding(:,1) backToFrontBoarding(:,1) outsideInBoarding(:,1) flyingCarpetBoarding(:,1)];
stdTime = [randomBoarding(:,2) backToFrontBoarding(:,2) outsideInBoarding(:,2) flyingCarpetBoarding(:,2)];

colorsJet = jet;
colors = colorsJet(1:16:end,:);

colors(4,:) = [1 1 0.2];
errorbar_groups(meanTime',stdTime','FigID',2,'bar_names',{'4 seats in one row','6 seats in one row'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet','Location','northwest')
ylabel('Time [min]','Interpreter','LaTex','FontSize',16)
title('Half full airplane, 100\% cabin baggage','Interpreter','LaTex','FontSize',18)
ylim([0 14])

%% 

clear all
clc

dataBoarding = dlmread('boardingData50Luggage500.txt');

planeDim = dataBoarding(1:5:end,:);

nSeats = unique(planeDim(1:end,2));
nRows = planeDim(1:end/length(nSeats),1);

randomBoarding = dataBoarding(2:5:end,1:2)/60;
backToFrontBoarding = dataBoarding(3:5:end,1:2)/60;
outsideInBoarding = dataBoarding(4:5:end,1:2)/60;
flyingCarpetBoarding = dataBoarding(5:5:end,1:2)/60;

meanTime = [randomBoarding(:,1) backToFrontBoarding(:,1) outsideInBoarding(:,1) flyingCarpetBoarding(:,1)];
stdTime = [randomBoarding(:,2) backToFrontBoarding(:,2) outsideInBoarding(:,2) flyingCarpetBoarding(:,2)];

colorsJet = jet;
colors = colorsJet(1:16:end,:);

colors(4,:) = [1 0.98 0.2];
errorbar_groups(meanTime',stdTime','FigID',3,'bar_names',{'4 seats in one row','6 seats in one row'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet','Location','northwest')
ylabel('Time [min]','Interpreter','LaTex','FontSize',16)
title('Full airplane, 50\% cabin baggage','Interpreter','LaTex','FontSize',18)
ylim([0 14])