import airplane
import numpy as np


nIterations = 100

# Dimensions of airplane
nSeatsPerSide = [3]
rowList = range(10) # 41 to get 40 rows as well
nRows = rowList[7::1]
nRows = [30]

# Nbr of blocks to board
nBlocks = 1

timeForRandom = [nIterations]
timeForBackToFront = [nIterations]
timeForOutsideIn = [nIterations]
timeForFlyingCarpet = [nIterations]

# File to print data
filename = 'boardingData3Blocks.txt'
#f = open(filename,'w')
times = open('waitingTimes.txt','w')

boardingID = 0

for iSeatsPerSide in range(len(nSeatsPerSide)):
    for iRows in range(len(nRows)):

        nBlocks = 2
        # Random boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'random', nBlocks)
            myAirplane.board()
#            timeForRandom.append(myAirplane.reportWaitingTimes())
            boardingID += 1
            for waitTime in myAirplane.reportWaitingTimes():
                times.write("%d, %.2f\n" % (boardingID, waitTime))
        # Back to front boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'backToFront', nBlocks)
            myAirplane.board()
            boardingID += 1
            for waitTime in myAirplane.reportWaitingTimes():
                times.write("%d, %.2f\n" % (boardingID, waitTime))

        # Outside in boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'outsideIn', nBlocks)
            myAirplane.board()
            boardingID += 1
            for waitTime in myAirplane.reportWaitingTimes():
                times.write("%d, %.2f\n" % (boardingID, waitTime))

        nBlocks = nSeatsPerSide[0]*2
        # Flying carpet boarding
        for iIteration in range(nIterations):
            myAirplane = airplane.Airplane(nRows[iRows], nSeatsPerSide[iSeatsPerSide], 'flyingCarpet', nBlocks)
            myAirplane.board()
            boardingID += 1
            for waitTime in myAirplane.reportWaitingTimes():
                times.write("%d, %.2f\n" % (boardingID, waitTime))


#        print('Nbr of rows: %.0f \t Seats per side: %.0f \t Nbr of blocks: %.0f' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks) )
        print '___________________________________________________________'
#        print('Boarding strategy \t Mean \t\t Std')
#        print('Random boarding \t %.2f \t %.2f' % (np.mean(timeForRandom),np.std(timeForRandom)) )
#        print('Back to front \t\t %.2f \t %.2f' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
#        print('Outside in \t\t\t %.2f \t %.2f' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
#        print('Flying carpet \t\t %.2f \t %.2f' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)) )
        print ' '

        # Print to file
#        f.write('%.0f \t %.0f \t %.0f \n' % (nRows[iRows], nSeatsPerSide[iSeatsPerSide], nBlocks) )
#        f.write('%.2f \t %.2f \n' % (np.mean(timeForRandom),np.std(timeForRandom)) )
#        f.write('%.2f \t %.2f \n' % (np.mean(timeForBackToFront),np.std(timeForBackToFront)) )
#        f.write('%.2f \t %.2f \n' % (np.mean(timeForOutsideIn),np.std(timeForOutsideIn)) )
#        f.write('%.2f \t %.2f \n' % (np.mean(timeForFlyingCarpet),np.std(timeForFlyingCarpet)))

        print(len(timeForFlyingCarpet))


times.close()
#f.close()





