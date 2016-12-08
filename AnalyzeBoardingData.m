%% Analyze boarding data

clc
clear all

data = dlmread('boardingDataVaryingBlocks.txt');

planeDim = data(1:5:end,:);

showEvery = 4;
nSeats = unique(planeDim(1:end,2));
nRows = planeDim(1:end/length(nSeats),1);
nBlocks = unique(data(:,3));

randomBoarding = data(2:5:end,:)/60;
backToFrontBoarding = data(3:5:end,:)/60;
outsideInBoarding = data(4:5:end,:)/60;
flyingCarpetBoarding = data(5:5:end,:)/60;

figure(1)
clf
figure(2)
clf
for iDifferentSeats = 1:length(nSeats)
  
  figure(iDifferentSeats)
  elements = (iDifferentSeats-1)*length(randomBoarding)/length(nSeats)+1:iDifferentSeats*length(randomBoarding)/length(nSeats);
  %plot(nRows,randomBoarding(elements,1))
  errorbar(nRows(1:showEvery:end),randomBoarding(elements(1:showEvery:end),1),randomBoarding(elements(1:showEvery:end),2))
  hold on
  %plot(nRows,backToFrontBoarding(elements,1))
  errorbar(nRows(1:showEvery:end),backToFrontBoarding(elements(1:showEvery:end),1),backToFrontBoarding(elements(1:showEvery:end),2))
  %plot(nRows,outsideInBoarding(elements,1))
  errorbar(nRows(1:showEvery:end),outsideInBoarding(elements(1:showEvery:end),1),outsideInBoarding(elements(1:showEvery:end),2))
  
  %plot(nRows,flyingCarpetBoarding(elements,1))
  errorbar(nRows(1:showEvery:end),flyingCarpetBoarding(elements(1:showEvery:end),1),flyingCarpetBoarding(elements(1:showEvery:end),2))
  legend('Random','Back to front','Outside in','Flying carpet');
  ylabel('Time [min]','Interpreter','LaTex')
  xlabel('Rows','Interpreter','LaTex')
  text = strcat(num2str(nSeats(iDifferentSeats)),' seats on one side,~',num2str(nBlocks(iDifferentSeats+1)),' blocks');
  title(text,'Interpreter','LaTex')
  
end

%%

clc

data = dlmread('boardingDataBlocks2000its.txt');

nBlocks = data(1:5:end,3);
nSeats = data(1,2);
nRows = data(1,1);

randomBoarding = data(2:5:end,:)/60;
backToFrontBoarding = data(3:5:end,:)/60;
outsideInBoarding = data(4:5:end,:)/60;
flyingCarpetBoarding = data(5:5:end,:)/60;


figure(3)
clf
plot(nBlocks,randomBoarding(1:end,1))
hold on
plot(nBlocks,backToFrontBoarding(1:end,1))
plot(nBlocks,outsideInBoarding(1:end,1))
plot(nBlocks,flyingCarpetBoarding(1:end,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time','Interpreter','LaTex')
xlabel('Blocks','Interpreter','LaTex')
text = strcat(num2str(nSeats),' seats on one side,~',num2str(nRows),' rows');
title(text,'Interpreter','LaTex')


%% waiting times

clear all
close all
clc

data = dlmread('waitingTimes.txt');

nIterationsPerType = 100;

nBoardings = max(data(:,1));
nTypes = nBoardings / nIterationsPerType;

for iType = 1:nTypes
    firstBoarding = (iType - 1)*nIterationsPerType + 1;
    lastBoarding = iType*nIterationsPerType;
    
    firstLine = find(data(:,1) == firstBoarding , 1);
    lastLine = find(data(:,1) == lastBoarding , 1, 'last');
    
    figure(iType)
    hist(data(firstLine:lastLine,2))
    axis([0 max(max(data)) 0 30*nIterationsPerType])
end
