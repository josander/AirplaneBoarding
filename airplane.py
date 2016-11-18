import numpy as np

class Passenger():
    nPassenger = 0  # Class variable keeping track of the number of passengers in total
    def __init__(self, seat, speed):
        self.seat = seat    # Of form {'side':'L', 'row':0, 'number': 0}. row 0 is by entrance, number 0 is by aisle
        self.speed = speed
        self.i = self.nPassenger    # Assigning unique index for every passenger
        self.nPassenger += 1

class Airplane():
    def __init__(self, nRows, nSeatsPerSide):
        self.nRows = nRows
        self.nSeatsPerRow = nSeatsPerSide

        # Create a list of all seats available in the flight
        seatList = [{'side':'L', 'row':iRow, 'number':iNumber} for iRow, iNumber in np.ndindex((nRows,nSeatsPerSide))]

        # Creating a Passenger for each seat and assigns the seat for them. Passengers to be kept in this list
        self.passengers = [ Passenger(iSeat, 0.5) for iSeat in seatList ]
        # Copies list of passengers into waiting list. Same objects kept in both list (elements fo lists works as pointers)
        self.waitingList = list(self.passengers)

        self.aisle = ['' for iRows in range(nRows)]
        self.leftHandSeats = [[ '' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.rightHandSeats = [['' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]

    def moveForward(self, aislePosition):
        # Moves the passenger in aislePosition one step forward if next position is empty
        if self.aisle[aislePosition + 1] == '':
            self.aisle[aislePosition + 1] = self.aisle[aislePosition]
            self.aisle[aislePosition] = ''


airplane = Airplane(5, 2)
