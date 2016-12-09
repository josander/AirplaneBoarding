%% Staple diagrams

clc
clear all

figure(1)
clf

dataBoarding = dlmread('boardingData200.txt');

randomBoarding = dataBoarding(2:5:end,1:2)/60;
backToFrontBoarding = dataBoarding(3:5:end,1:2)/60;
outsideInBoarding = dataBoarding(4:5:end,1:2)/60;
flyingCarpetBoarding = dataBoarding(5:5:end,1:2)/60;

meanTime = [randomBoarding(:,1) backToFrontBoarding(:,1) outsideInBoarding(:,1) flyingCarpetBoarding(:,1)];
stdTime = [randomBoarding(:,2) backToFrontBoarding(:,2) outsideInBoarding(:,2) flyingCarpetBoarding(:,2)];

colorsJet = jet;
colors = colorsJet(1:16:end,:);

colors(4,:) = [1 1 0.2];
errorbar_groups(meanTime',stdTime','FigID',1,'bar_names',{'2 seats on one side','3 seats on one side'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet')
ylabel('Time [min]','Interpreter','LaTex')
title('Full airplane, 100\% carry luggage','Interpreter','LaTex','FontSize',14)
ylim([0 16])

%% 

clear all
clc

dataBoarding = dlmread('boardingData50Filled.txt');

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
errorbar_groups(meanTime',stdTime','FigID',2,'bar_names',{'2 seats on one side','3 seats on one side'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet')
ylabel('Time [min]','Interpreter','LaTex')
title('Half full airplane, 100\% carry luggage','Interpreter','LaTex','FontSize',14)

%% 

clear all
clc

dataBoarding = dlmread('boardingData50Luggage200.txt');

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
errorbar_groups(meanTime',stdTime','FigID',3,'bar_names',{'2 seats on one side','3 seats on one side'},'bar_colors',colors);
legend('Random','Back to front','Outside in','Flying carpet')
ylabel('Time [min]','Interpreter','LaTex')
title('Full airplane, 50\% carry luggage','Interpreter','LaTex','FontSize',14)
ylim([0 14])