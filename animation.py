import airplane
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

myAirplane = airplane.Airplane(10,3)
ax.axis([-0.5, 2*myAirplane.nSeatsPerRow + 0.5, -0.5, myAirplane.nRows - 0.5])
ax.set_aspect((2*myAirplane.nSeatsPerRow + 1.0)/myAirplane.nRows)

def getPositions():
    rows = []
    seats = []
    for iRow, row in enumerate(myAirplane.leftHandSeats):
        for iSeat, seat in enumerate(row):
            if not seat == '':
                rows.append(iRow)
                seats.append((myAirplane.nSeatsPerRow - 1) - iSeat)
    for iRow, row in enumerate(myAirplane.rightHandSeats):
        for iSeat, seat in enumerate(row):
            if not seat == '':
                rows.append(iRow)
                seats.append((myAirplane.nSeatsPerRow + 1) + iSeat)

    spots = []
    for iSpot, spot in enumerate(myAirplane.aisle):
        if not spot == '':
            spots.append(iSpot)
    return rows, seats, spots

rows, seats, spots = getPositions()

line1, = ax.plot(seats, rows, 'og', ms=15)
line2, = ax.plot(myAirplane.nSeatsPerRow*np.ones(len(spots)), spots, 'or', ms = 15)

def updatefig(*args):
    myAirplane.proceedBoarding()
    rows, seats, spots = getPositions()
    line1.set_xdata(seats)
    line1.set_ydata(rows)
    line2.set_xdata(myAirplane.nSeatsPerRow*np.ones(len(spots)))
    line2.set_ydata(spots)
    return line1, line2

a = anim.FuncAnimation(fig, updatefig, interval = 100, blit = True)
plt.show()