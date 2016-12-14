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

titles = {'\textbf{Random}','\textbf{Back to front}','\textbf{Outside in}', '\textbf{Flying carpet}'};

colorsJet = jet;
colors = colorsJet(1:16:end,:);
colors(4,:) = [1 1 0.2];

bins = 60:120:max(max(data))+20;
nBins = length(bins);

for iType = 1:nTypes
    firstBoarding = (iType - 1)*nIterationsPerType + 1;
    lastBoarding = iType*nIterationsPerType;
    
    firstLine = find(data(:,1) == firstBoarding , 1);
    lastLine = find(data(:,1) == lastBoarding , 1, 'last');
    
    subplot(2,2,iType)
    hist(data(firstLine:lastLine,2),bins)
    set(get(gca,'child'),'FaceColor',colors(iType,:),'EdgeColor','k');
    axis([-5 max(max(data))*(1+1/nBins) 0 30*nIterationsPerType+2000])
    title(titles{iType},'Interpreter','LaTex','FontSize',18)
    ax = gca;
    ax.XTick = bins;
    ax.XTickLabel  ={'1' '3' '5' '7' '9' '11' '13' '15' '17'};
    yticklabels = ax.YTick/ nIterationsPerType;
    ax.YTickLabel = yticklabels;
    set(gca,'FontSize',14)
    xlabel('Time [min]','Interpreter','LaTex','FontSize',16)
    ylabel('Passengers','Interpreter','LaTex','FontSize',16)
    
end

%saveas(gcf,'waitingTimeDist.eps','epsc')
saveas(gcf,'waitingTimeDist.png','png')

%% Playing  with histograms to see if we can get them shaded

