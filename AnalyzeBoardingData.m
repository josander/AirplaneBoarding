%% Analyze boarding data

clc

data = dlmread('boardingData.txt');

planeDim = data(1:5:end,:);
nbrRows = planeDim(1:end/2,1);

randomBoarding = data(2:5:end,:);
backToFrontBoarding = data(3:5:end,:);
outsideInBoarding = data(4:5:end,:);
flyingCarpetBoarding = data(5:5:end,:);

figure(1)
clf
subplot(2,1,1)
plot(nbrRows,randomBoarding(1:end/2,1))
hold on
plot(nbrRows,backToFrontBoarding(1:end/2,1))
plot(nbrRows,outsideInBoarding(1:end/2,1))
plot(nbrRows,flyingCarpetBoarding(1:end/2,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time')
xlabel('Rows')
title('Two seats on one side')

subplot(2,1,2)
plot(nbrRows,randomBoarding(end/2+1:end,1))
hold on
plot(nbrRows,backToFrontBoarding(end/2+1:end,1))
plot(nbrRows,outsideInBoarding(end/2+1:end,1))
plot(nbrRows,flyingCarpetBoarding(end/2+1:end,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time')
xlabel('Rows')
title('Three seats on one side')

%%

clc

data = dlmread('boardingDataBlockSize.txt');

nBlocks = data(1:5:end,3);

randomBoarding = data(2:5:end,:);
backToFrontBoarding = data(3:5:end,:);
outsideInBoarding = data(4:5:end,:);
flyingCarpetBoarding = data(5:5:end,:);

figure(2)
clf
plot(nBlocks,randomBoarding(1:end,1))
hold on
plot(nBlocks,backToFrontBoarding(1:end,1))
plot(nBlocks,outsideInBoarding(1:end,1))
plot(nBlocks,flyingCarpetBoarding(1:end,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time')
xlabel('Blocks')
title('Three seats on one side')