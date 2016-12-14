import airplane
import numpy as np

nIterations = 500

# Dimensions of airplane
nSeatsPerSide = [3]
nRows = [30]
listBlocks = [2, 4, 6, 8, 10, 12, 14]
fracFilled = 1.0
fracLuggage = 1.0
threshold = 6000

# File to print data
filename = 'boardingDataBlocks500.txt'
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

            print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f \t Fraction filled: %.0f \t Fraction luggage: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks], fracFilled, fracLuggage) )
            print '___________________________________________________________'
            print('Boarding strategy \t Mean \t\t Std')
            print('Random boarding \t %.2f \t %.2f' % (np.mean(timeRandom),np.std(timeRandom)) )
            print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeBackToFront),np.std(timeBackToFront)) )
            print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeOutsideIn),np.std(timeOutsideIn)) )
            print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeFlyingCarpet),np.std(timeFlyingCarpet)) )
            print ' '


            # Print to file
            f.write('%.0f \t %.0f \t %.0f \t %.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], listBlocks[iBlocks], fracFilled, fracLuggage) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeRandom),np.std(timeRandom)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeBackToFront),np.std(timeBackToFront)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeOutsideIn),np.std(timeOutsideIn)) )
            f.write('%.2f \t %.2f \n' % (np.mean(timeFlyingCarpet),np.std(timeFlyingCarpet)))



f.close()
