import airplane
import numpy as np


nIterations = 20


nSeatsPerSide = [2, 3]
nRows = [10, 20]

timeForRandom = [nIterations]
timeForBackToFront = [nIterations]
timeForOutsideIn = [nIterations]
timeForFlyingCarpet = [nIterations]

for iSeatsPerSide in range(len(nSeatsPerSide)):
    for iRows in range(len(nRows)):

        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random')
            myAirplane.board()
            timeForRandom.append(myAirplane.tBoarding)

        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront')
            myAirplane.board()
            timeForBackToFront.append(myAirplane.tBoarding)

        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn')
            myAirplane.board()
            timeForOutsideIn.append(myAirplane.tBoarding)

        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet')
            myAirplane.board()
            timeForFlyingCarpet.append(myAirplane.tBoarding)

        # TODO: Fix nicer print outs
        print('Nbr of rows:', nRows[iRows], 'Seats per side:', nSeatsPerSide[iSeatsPerSide])
        print('Boarding strategy','Mean','Std')
        print('Random boarding',np.mean(timeForRandom),np.std(timeForRandom))
        print('Back to front',np.mean(timeForBackToFront),np.std(timeForBackToFront))
        print('Outside in',np.mean(timeForOutsideIn),np.std(timeForOutsideIn))
        print('Flying carpet',np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet))
        print ' '




