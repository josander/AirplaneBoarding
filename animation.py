import airplane
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np

# Animates the boarding process for the airplane model specified below. Saves animation to filename
# Equal spacing between all frames makes time spacing irregular since we don't work with continuous time.
# Don't know if a fix is necessary
# Program stops through crashing due to construction of Airplane.proceedBoarding()

nRows = 20
nSeatsPerRow = 3
myAirplane = airplane.Airplane(nRows, nSeatsPerRow)
filename = 'test.mp4'

# Basic figure properties
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis([-0.5, 2*myAirplane.nSeatsPerRow + 0.5, -0.5, myAirplane.nRows - 0.5])
ax.set_aspect((2*myAirplane.nSeatsPerRow + 1.0)/myAirplane.nRows)

# Sets tick labels to corresponding row and seat numbers and
xTickPositions = range(2*myAirplane.nSeatsPerRow+1)
xTicks = list(reversed(range(myAirplane.nSeatsPerRow))) + ['Aisle'] + range(myAirplane.nSeatsPerRow)
plt.xticks(xTickPositions, xTicks)
yTickPositions = range(myAirplane.nRows)
plt.yticks(yTickPositions)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
pos = ax.get_position()
ax.set_position([pos.x0 - 0.1, pos.y0, pos.width, pos.height])

# Adds grid lines
for x in np.arange(0.5, 2*myAirplane.nSeatsPerRow, 1.0):
    ax.axvline(x,color = 'k')
for y in np.arange(0.5,myAirplane.nRows, 1.0):
    ax.plot([-0.5,myAirplane.nSeatsPerRow-0.5],[y,y], '-k')
    ax.plot([myAirplane.nSeatsPerRow+0.5, 2*myAirplane.nSeatsPerRow+0.5], [y,y], '-k')

def getPositions():
    # Returns positions of seated passengers and passengers in aisle
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
    packingSpots = []
    for iSpot, spot in enumerate(myAirplane.aisle):
        if not spot == '':
            if spot.status == 'walking':
                spots.append(iSpot)
            else:
                packingSpots.append(iSpot)
    return rows, seats, spots, packingSpots

# Instantiate line objects holding positions of passengers. Red for passengers in aisle, green for seated passengers
rows, seats, spots, packingSpots = getPositions()
line1, = ax.plot(myAirplane.nSeatsPerRow*np.ones(len(spots)), spots, 'or', ms = 15, label='Walking')
line2, = ax.plot(myAirplane.nSeatsPerRow*np.ones(len(packingSpots)),packingSpots, 'ob', ms = 15, label='Packing')
line3, = ax.plot(seats, rows, 'og', ms=15, label='Seated')

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), numpoints = 1)

def updatefig(*args):
    myAirplane.proceedBoarding()
    rows, seats, spots, packingSpots = getPositions()
    line1.set_xdata(myAirplane.nSeatsPerRow*np.ones(len(spots)))
    line1.set_ydata(spots)
    line2.set_xdata(myAirplane.nSeatsPerRow*np.ones(len(packingSpots)))
    line2.set_ydata(packingSpots)
    line3.set_xdata(seats)
    line3.set_ydata(rows)

    fig.suptitle('Elapsed time = %.2f seconds'%(myAirplane.tBoarding))
    return line1, line2, line3


Writer = anim.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

a = anim.FuncAnimation(fig, updatefig, interval = 50, save_count = 1500, blit = True)
a.save(filename, writer=writer)
