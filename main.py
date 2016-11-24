import airplane
import numpy as np


nIterations = 20

nSeatsPerSide = [2, 3]
nRows = [10, 20, 30]


timeForRandom = [nIterations]
timeForBackToFront = [nIterations]
timeForOutsideIn = [nIterations]
timeForFlyingCarpet = [nIterations]

# File to print data
filename = 'boardingData.txt'
f = open(filename,'w')

for iSeatsPerSide in range(len(nSeatsPerSide)):
    for iRows in range(len(nRows)):

        # Random boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random')
            myAirplane.board()
            timeForRandom.append(myAirplane.tBoarding)

        # Back to front boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront')
            myAirplane.board()
            timeForBackToFront.append(myAirplane.tBoarding)

        # Outside in boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn')
            myAirplane.board()
            timeForOutsideIn.append(myAirplane.tBoarding)

        # Flying carpet boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet')
            myAirplane.board()
            timeForFlyingCarpet.append(myAirplane.tBoarding)


        print('Nbr of rows: %.0f \t Seats per side: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide]) )
        print '___________________________________________'
        print('Boarding strategy \t Mean \t\t Std')
        print('Random boarding \t %.2f \t %.2f' % (np.mean(timeForRandom),np.std(timeForRandom)) )
        print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
        print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
        print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)) )
        print ' '

        # Print to file
        f.write('%.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide]) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForRandom),np.std(timeForRandom)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
        f.write('%.2f \t %.2f \n' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)))


f.close()

