import airplane
import numpy as np


nIterations = 20


# Dimensions of airplane
nSeatsPerSide = [2]
nRows = [30]
listBlocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


timeForRandom = [nIterations]
timeForBackToFront = [nIterations]
timeForOutsideIn = [nIterations]
timeForFlyingCarpet = [nIterations]

# File to print data
filename = 'boardingDataBlockSize.txt'
f = open(filename,'w')

for iBlocks in range(len(listBlocks)):
    for iSeatsPerSide in range(len(nSeatsPerSide)):
        for iRows in range(len(nRows)):

            # Random boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random', listBlocks[iBlocks])
                myAirplane.board()
                timeForRandom.append(myAirplane.tBoarding)

            # Back to front boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront', listBlocks[iBlocks])
                myAirplane.board()
                timeForBackToFront.append(myAirplane.tBoarding)

            # Outside in boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn', listBlocks[iBlocks])
                myAirplane.board()
                timeForOutsideIn.append(myAirplane.tBoarding)

            # Flying carpet boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet', listBlocks[iBlocks])
                myAirplane.board()
                timeForFlyingCarpet.append(myAirplane.tBoarding)


            print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks]) )
            print '___________________________________________________________'
            print('Boarding strategy \t Mean \t\t Std')
            print('Random boarding \t %.2f \t %.2f' % (np.mean(timeForRandom),np.std(timeForRandom)) )
            print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
            print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
            print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)) )
            print ' '

            # Print to file
            f.write('%.0f \t %.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks]) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForRandom),np.std(timeForRandom)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)))


f.close()