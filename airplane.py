import numpy as np
import random

class Passenger():
    nPassenger = 0  # Class variable keeping track of the number of passengers in total
    def __init__(self, seat, speed):
        self.seat = seat    # Of form {'side':'L', 'row':0, 'number': 0}. row 0 is by entrance, number 0 is by aisle
        self.speed = speed
        self.i = self.nPassenger    # Assigning unique index for every passenger
        self.nPassenger += 1
        self.status = 'waiting'     # Statuses 'waiting', 'walking', 'packing', 'sitting'

class Airplane():
    def __init__(self, nRows, nSeatsPerSide):
        self.nRows = nRows
        self.nSeatsPerRow = nSeatsPerSide
        self.tBoarding = 0
        self.status = 'empty'

        # Create a list of all seats available in the flight
        leftSeatList = [{'side':'L', 'row':iRow, 'number':iNumber} for iRow, iNumber in np.ndindex((nRows,nSeatsPerSide))]
        rightSeatList = [{'side':'R', 'row':iRow, 'number':iNumber} for iRow, iNumber in np.ndindex((nRows,nSeatsPerSide))]
        seatList = leftSeatList + rightSeatList

        # Creating a Passenger for each seat and assigns the seat for them. Passengers to be kept in this list
        self.passengers = [ Passenger(iSeat, 0.5) for iSeat in seatList ]
        # Copies list of passengers into waiting list. Same objects kept in both list (elements fo lists works as pointers)
        # TODO: implement different ways of ordering passengers
        self.waitingList = list(self.passengers)

        self.aisle = ['' for iRows in range(nRows)]
        self.leftHandSeats = [[ '' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.rightHandSeats = [['' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.nPassengers = len(self.passengers)
        self.nSeatedPassengers = 0

    # To be removed. Functionality implemented in function board()
    def moveForward(self, aislePosition):
        # Moves the passenger in aislePosition one step forward if next position is empty
        if self.aisle[aislePosition + 1] == '':
            self.aisle[aislePosition + 1] = self.aisle[aislePosition]
            self.aisle[aislePosition] = ''

    def board(self):
        # Start boarding
        self.status = 'boarding'
        while self.nSeatedPassengers < self.nPassengers:
            self.proceedBoarding()
        self.status = 'boarded'
        print self.rightHandSeats
        print self.leftHandSeats
        print self.tBoarding


    def proceedBoarding(self):
        tNextEvent = 100000     # Large number, used to calculate next event
        iNextEvent = 0
        # Move first person in waiting list into empty spot in aisle if not occupied
        if self.aisle[0] == '' and (not self.waitingList == []):
            self.aisle[0] = self.waitingList.pop(0)
            self.aisle[0].status = 'walking'
            self.aisle[0].t = random.random()

        for iAisleSpot, aisleSpot in enumerate(self.aisle):

            # Check if by their seat row, if so start packing
            if (not aisleSpot == '') and aisleSpot.seat['row'] == iAisleSpot and aisleSpot.status == 'walking':
                aisleSpot.status = 'packing'
                aisleSpot.t = random.random()   # TODO: Packing time distribution should be changed

            # Check if they account for next event to occur, if so set the time to elapse (tNextEvent) to their time t
            if ((not aisleSpot == '') and aisleSpot.t < tNextEvent
                and (self.aisle[np.minimum(iAisleSpot + 1, self.nRows-1)] == '' or not aisleSpot.status == 'walking')):
                tNextEvent = aisleSpot.t
                iNextEvent = iAisleSpot

        # Elapse time until next event
        self.tBoarding += tNextEvent
        for aisleSpot in self.aisle:
            if not aisleSpot == '':
                aisleSpot.t -= tNextEvent

        actingAgent = self.aisle[iNextEvent]    # Passenger accounting for next event

        # Move passenger to next spot in aisle
        if actingAgent.status == 'walking':
            actingAgent.t = random.random()  #Random time to walk one row # TODO: distribution for walking times, include speed?
            self.aisle[iNextEvent + 1] = actingAgent
            self.aisle[iNextEvent] = ''
        # Passenger sits down
        elif actingAgent.status == 'packing':
            if actingAgent.seat['side'] == 'L':
                self.leftHandSeats[actingAgent.seat['row']][actingAgent.seat['number']] = actingAgent
            else:
                self.rightHandSeats[actingAgent.seat['row']][actingAgent.seat['number']] = actingAgent
            actingAgent.status = 'seated'
            self.aisle[iNextEvent] = ''
            self.nSeatedPassengers += 1

airplane = Airplane(20,3)
airplane.board()