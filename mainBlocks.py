import airplane
import numpy as np



nIterations = 2000






# Dimensions of airplane
nSeatsPerSide = [3]
nRows = [30]
listBlocks = [2, 4, 6, 8, 10, 12]


# File to print data
filename = 'boardingDataBlocks2000its.txt'
f = open(filename,'w')

for iBlocks in range(len(listBlocks)):
    for iSeatsPerSide in range(len(nSeatsPerSide)):
        for iRows in range(len(nRows)):

            timeForRandom = []
            timeForBackToFront = []
            timeForOutsideIn = []
            timeForFlyingCarpet = []

            # Random boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random', listBlocks[iBlocks], fracFilled, fracLuggage)
                myAirplane.board()
                timeForRandom.append(myAirplane.tBoarding)

            # Back to front boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront', listBlocks[iBlocks], fracFilled, fracLuggage)
                myAirplane.board()
                timeForBackToFront.append(myAirplane.tBoarding)

            # Outside in boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn', listBlocks[iBlocks], fracFilled, fracLuggage)
                myAirplane.board()
                timeForOutsideIn.append(myAirplane.tBoarding)

            # Flying carpet boarding
            for iIteration in range(nIterations):
                myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet', listBlocks[iBlocks], fracFilled, fracLuggage)
                myAirplane.board()
                timeForFlyingCarpet.append(myAirplane.tBoarding)


            print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f \t Fraction filled: %.0f \t Fraction luggage: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks], fracFilled, fracLuggage) )
            print '___________________________________________________________'
            print('Boarding strategy \t Mean \t\t Std')
            print('Random boarding \t %.2f \t %.2f' % (np.mean(timeForRandom),np.std(timeForRandom)) )
            print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
            print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
            print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)) )
            print ' '
            print len(timeForFlyingCarpet)
            print ' '


            # Print to file
            f.write('%.0f \t %.0f \t %.0f \t %.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks], fracFilled, fracLuggage) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForRandom),np.std(timeForRandom)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)))

print len(timeForFlyingCarpet)


f.close()
