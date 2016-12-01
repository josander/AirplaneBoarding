%% Analyze boarding data

data = dlmread('boardingData.txt');

planeDim = data(1:5:end,:);
nbrRows = planeDim(1:end/2,1);

randomBoarding = data(2:5:end,:);
backToFrontBoarding = data(3:5:end,:);
outsideInBoarding = data(4:5:end,:);
flyingCarpetBoarding = data(5:5:end,:);

figure(1)
clf
plot(nbrRows,randomBoarding(1:end/2,1))
hold on
plot(nbrRows,backToFrontBoarding(1:end/2,1))
plot(nbrRows,outsideInBoarding(1:end/2,1))
plot(nbrRows,flyingCarpetBoarding(1:end/2,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time')
xlabel('Rows')

figure(2)
clf
plot(nbrRows,randomBoarding(end/2+1:end,1))
hold on
plot(nbrRows,backToFrontBoarding(end/2+1:end,1))
plot(nbrRows,outsideInBoarding(end/2+1:end,1))
plot(nbrRows,flyingCarpetBoarding(end/2+1:end,1))
legend('Random','Back to front','Outside in','Flying carpet');
ylabel('Time')
xlabel('Rows')
