import airplane
import numpy as np
import math


nIterations = 500


# Dimensions of airplane
nSeatsPerSide = [2, 3]
nRows = [30]
fracFilled = 1.0
fracLuggage = 0.5
nBlocks = 1         # Will be changed later in the code
threshold = 6000


# File to print data
filename = 'boardingData50Luggage.txt'
f = open(filename,'w')

for iSeatsPerSide in range(len(nSeatsPerSide)):
    for iRows in range(len(nRows)):

        timeForRandom = []
        timeForBackToFront = []
        timeForOutsideIn = []
        timeForFlyingCarpet = []


        # Random boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random', nBlocks, fracFilled, fracLuggage)
            myAirplane.board()
            timeForRandom.append(myAirplane.tBoarding)

        # Back to front boarding
        nBlocks = 2
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront', nBlocks, fracFilled, fracLuggage)
            myAirplane.board()
            timeForBackToFront.append(myAirplane.tBoarding)

        # Outside in boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn', nBlocks, fracFilled, fracLuggage)
            myAirplane.board()
            timeForOutsideIn.append(myAirplane.tBoarding)

        # Flying carpet boarding
        nBlocks = int(math.ceil(nSeatsPerSide[iSeatsPerSide] * 2 * fracFilled))
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet', nBlocks, fracFilled, fracLuggage)
            myAirplane.board()
            timeForFlyingCarpet.append(myAirplane.tBoarding)


        # Threshold out outlayers
        timeRandom = []
        timeBackToFront = []
        timeOutsideIn = []
        timeFlyingCarpet = []

        for iIteration in range(nIterations):
            if timeForRandom[iIteration] < threshold:
                timeRandom.append(timeForRandom[iIteration])
            if timeForBackToFront[iIteration] < threshold:
                timeBackToFront.append(timeForBackToFront[iIteration])
            if timeForOutsideIn[iIteration] < threshold:
                timeOutsideIn.append(timeForOutsideIn[iIteration])
            if timeForFlyingCarpet[iIteration] < threshold:
                timeFlyingCarpet.append(timeForFlyingCarpet[iIteration])


        print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f \t Fraction filled: %.2f \t Fraction luggage: %.2f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks, fracFilled, fracLuggage) )
        print '___________________________________________________________'
        print('Boarding strategy \t Mean \t\t Std')
        print('Random boarding \t %.2f \t %.2f' % (np.mean(timeRandom),np.std(timeRandom)) )
        print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeBackToFront),np.std(timeBackToFront)) )
        print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeOutsideIn),np.std(timeOutsideIn)) )
        print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeFlyingCarpet),np.std(timeFlyingCarpet)) )
        print ' '

        # Print to file
        f.write('%.0f \t %.0f \t %.0f \t %.2f \t %.2f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks, fracFilled, fracLuggage) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeRandom),np.std(timeRandom)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeBackToFront),np.std(timeBackToFront)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeOutsideIn),np.std(timeOutsideIn)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeFlyingCarpet),np.std(timeFlyingCarpet)))


f.close()


