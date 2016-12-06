import airplane
import numpy as np


nIterations = 100


# Dimensions of airplane
nSeatsPerSide = [2, 3]
rowList = range(41) # 41 to get 40 rows as well
nRows = rowList[10::2]


# File to print data
filename = 'boardingDataVaryingBlocks.txt'
f = open(filename,'w')

filename = 'waitingTime.txt'
waitingFile = open(filename,'w')

for iSeatsPerSide in range(len(nSeatsPerSide)):
    for iRows in range(len(nRows)):

        nBlocks = nSeatsPerSide[iSeatsPerSide] * 2

        timeForRandom = []
        timeForBackToFront = []
        timeForOutsideIn = []
        timeForFlyingCarpet = []


        # Random boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random', nBlocks)
            myAirplane.board()
            timeForRandom.append(myAirplane.tBoarding)

        # Back to front boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront', nBlocks)
            myAirplane.board()
            timeForBackToFront.append(myAirplane.tBoarding)

        # Outside in boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn', nBlocks)
            myAirplane.board()
            timeForOutsideIn.append(myAirplane.tBoarding)

        # Flying carpet boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet', nBlocks)
            myAirplane.board()
            timeForFlyingCarpet.append(myAirplane.tBoarding)


        print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks) )
        print '___________________________________________________________'
        print('Boarding strategy \t Mean \t\t Std')
        print('Random boarding \t %.2f \t %.2f' % (np.mean(timeForRandom),np.std(timeForRandom)) )
        print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
        print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
        print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)) )
        print ' '

        # Print to file
        f.write('%.0f \t %.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForRandom),np.std(timeForRandom)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)))


f.close()
waitingFile.close()


