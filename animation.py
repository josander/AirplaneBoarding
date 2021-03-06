import matplotlib
matplotlib.use('TKAgg')

import airplane
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np


# Animates the boarding process for the airplane model specified below. Saves animation to filename
# Equal spacing between all frames makes time spacing irregular since we don't work with continuous time.
# Don't know if a fix is necessary
# Program stops through crashing due to construction of Airplane.proceedBoarding()

class animatedAirplane(airplane.Airplane):
    def getPositions(self):
        # Returns positions of seated passengers and passengers in aisle
        rows = []
        seats = []
        for iRow, row in enumerate(self.leftHandSeats):
            for iSeat, seat in enumerate(row):
                if not seat == '':
                    rows.append(iRow)
                    seats.append((self.nSeatsPerRow - 1) - iSeat)
        for iRow, row in enumerate(self.rightHandSeats):
            for iSeat, seat in enumerate(row):
                if not seat == '':
                    rows.append(iRow)
                    seats.append((self.nSeatsPerRow + 1) + iSeat)
        spots = []
        interferingSpots = []
        packingSpots = []
        for iSpot, spot in enumerate(self.aisle):
            if not spot == '':
                if spot.status == 'walking':
                    spots.append(iSpot)
                elif spot.status == 'interfering':
                    interferingSpots.append(iSpot)
                else:
                    packingSpots.append(iSpot)
        return rows, seats, spots, interferingSpots, packingSpots


    def updatefig(self, *args):

        if self.nSeatedPassengers < self.nPassengers:
            self.proceedBoarding()

            rows, seats, spots, interferingSpots, packingSpots = self.getPositions()
            self.line1.set_xdata(self.nSeatsPerRow*np.ones(len(spots)))
            self.line1.set_ydata(spots)
            self.line2.set_xdata(self.nSeatsPerRow*np.ones(len(packingSpots)))
            self.line2.set_ydata(packingSpots)
            self.line3.set_xdata(self.nSeatsPerRow*np.ones(len(interferingSpots)))
            self.line3.set_ydata(interferingSpots)
            self.line4.set_xdata(seats)
            self.line4.set_ydata(rows)

            self.txt.set_text('Elapsed time = %.2f seconds'%(self.tBoarding))

        return self.line1, self.line2, self.line3, self.line4

    def animate(self, filename):
        # Basic figure properties
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.axis([-0.5, 2*self.nSeatsPerRow + 0.5, -0.5, self.nRows - 0.5])
        ax.set_aspect((2*self.nSeatsPerRow + 1.0)/self.nRows)
        self.txt = fig.suptitle('Elapsed time = %.2f seconds'%(self.tBoarding))

        # Sets tick labels to corresponding row and seat numbers and
        xTickPositions = range(2*self.nSeatsPerRow+1)
        xTicks = list(reversed(range(self.nSeatsPerRow))) + ['Aisle'] + range(self.nSeatsPerRow)
        plt.xticks(xTickPositions, xTicks)
        yTickPositions = range(self.nRows)
        plt.yticks(yTickPositions)
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        pos = ax.get_position()
        ax.set_position([pos.x0 - 0.1, pos.y0, pos.width, pos.height])

        # Adds grid lines
        for x in np.arange(0.5, 2*self.nSeatsPerRow, 1.0):
            ax.axvline(x,color = 'k')
        for y in np.arange(0.5,self.nRows, 1.0):
            ax.plot([-0.5,self.nSeatsPerRow-0.5],[y,y], '-k')
            ax.plot([self.nSeatsPerRow+0.5, 2*self.nSeatsPerRow+0.5], [y,y], '-k')
        # Instantiate line objects holding positions of passengers. Red for passengers in aisle, green for seated passengers
        rows, seats, spots, interferingSpots, packingSpots = self.getPositions()
        self.line1, = ax.plot(self.nSeatsPerRow*np.ones(len(spots)), spots, 'or', ms = 15, label='Walking')
        self.line2, = ax.plot(self.nSeatsPerRow*np.ones(len(packingSpots)),packingSpots, 'ob', ms = 15, label='Packing')
        self.line3, = ax.plot(self.nSeatsPerRow*np.ones(len(interferingSpots)), interferingSpots, 'oy', ms=15, label='Interfering')
        self.line4, = ax.plot(seats, rows, 'og', ms=15, label='Seated')

        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), numpoints = 1)

        Writer = anim.writers['ffmpeg']
        writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)

        a = anim.FuncAnimation(fig, self.updatefig, interval = 25, save_count = 200, blit = True)
        a.save(filename, writer=writer)

nRows = 10
nSeatsPerRow = 2
nBlocks = 6
fracFilled = 1.0
fracLuggage = 1.0


#airplane1 = animatedAirplane(nRows, nSeatsPerRow, 'random', nBlocks, fracFilled, fracLuggage)
#airplane1.animate('random.mp4')
#print('Random \t %.2f s' % (airplane1.tBoarding) )
#airplane2 = animatedAirplane(nRows, nSeatsPerRow, 'backToFront', nBlocks, fracFilled, fracLuggage)
#airplane2.animate('backToFront.mp4')
#print('Back to front \t %.2f s' % (airplane2.tBoarding) )
#airplane3 = animatedAirplane(nRows, nSeatsPerRow, 'outsideIn', nBlocks, fracFilled, fracLuggage)
#airplane3.animate('outsideIn.mp4')
#print('Outside in \t %.2f s' % (airplane3.tBoarding) )
airplane4 = animatedAirplane(nRows, nSeatsPerRow, 'flyingCarpet', nBlocks, fracFilled, fracLuggage)
airplane4.animate('flyingCarpet.mp4')
print('Flying carpet \t %.2f s' % (airplane4.tBoarding) )