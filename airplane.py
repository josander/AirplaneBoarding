import numpy as np
import random
import itertools


class Passenger():
    nPassenger = 0  # Class variable keeping track of the number of passengers in total
    speedMu = 0.8 # A: average passenger speed when walking unblocked in rows/second
    speedSigma = 0.2 # A: stddev
    def __init__(self, seat): # A: removed speed as an argument, as it's drawn from distribution below
        self.seat = seat    # Of form {'side':'L', 'row':0, 'number': 0}. row 0 is by entrance, number 0 is by aisle
        self.speed = random.gauss(self.speedMu, self.speedSigma)
        while self.speed < (self.speedMu - 2*self.speedSigma):
            self.speed = random.gauss(self.speedMu, self.speedSigma)
        self.i = self.nPassenger    # Assigning unique index for every passenger
        self.nPassenger += 1
        self.status = 'waiting'     # Statuses 'waiting', 'walking', 'packing', 'sitting'
        self.luggage = True         # Default value that passengers have luggage

class Airplane():
    def __init__(self, nRows, nSeatsPerSide, boardMethod, nBlocks=4, fracFilled = 1.0, fracLuggage=1.0):
        self.nRows = nRows
        self.nSeatsPerRow = nSeatsPerSide
        self.boardMethod = boardMethod
        self.tBoarding = 0
        self.status = 'empty'
        self.nBlocks = nBlocks
        self.passengersWaitingTime = 0
        self.satisfactionFactor = 10000
        self.methodSatisfactionPenalty = 1

        # Create a list of all seats available in the flight
        #leftSeatList = [{'side':'L', 'row':iRow, 'number':iNumber} for iRow, iNumber in np.ndindex((nRows,nSeatsPerSide))]
        #rightSeatList = [{'side':'R', 'row':iRow, 'number':iNumber} for iRow, iNumber in np.ndindex((nRows,nSeatsPerSide))]
        # A: I re-ordered seats to have all those on the same row together
        seatList = [{'side':iSide, 'row':iRow, 'number':iNumber} for iRow in range(nRows) for iSide in ['L','R']
                    for iNumber in range(nSeatsPerSide)]

        # Creating a Passenger for each seat and assigns the seat for them. Passengers to be kept in this list
        # A: changed because speed was removed as parameter self.passengers = [ Passenger(iSeat, 0.5) for iSeat in seatList ]
        self.passengers = [ Passenger(iSeat) for iSeat in seatList ]
        random.shuffle(self.passengers)
        self.passengers = self.passengers[0:int(fracFilled*2*self.nRows*self.nSeatsPerRow)]
        self.nPassengers = len(self.passengers)

        # Sets 'no luggage'
        for iPassenger in range(int((1.0-fracLuggage)*self.nPassengers)):
            self.passengers[iPassenger].luggage = False

        # A: different ways of ordering passengers
        # Same objects kept in both list (elements fo lists works as pointers)
        if self.boardMethod == 'random': # A: completely random boarding
            self.randomBoarding()
        elif self.boardMethod == 'backToFront': # A: the common boarding by zones, from back to front
            self.backToFrontBoarding()
        elif self.boardMethod == 'outsideIn': # A: 3 groups; windows first, then middle, then aisle, each group randomly
            self.methodSatisfactionPenalty = 0.9 # modify multiplier to account for a percentage of people in groups
                                            # not able to board together
            self.outsideInBoarding()
        elif self.boardMethod == 'flyingCarpet':
            self.flyingCarpetBoarding()
        else:
            self.waitingList = list(self.passengers)

        self.aisle = ['' for iRows in range(nRows)]
        self.leftHandSeats = [[ '' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.rightHandSeats = [['' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.nSeatedPassengers = 0

    def board(self):
        # Start boarding
        self.status = 'boarding'
        while self.nSeatedPassengers < self.nPassengers:
            self.proceedBoarding()
        self.status = 'boarded'
        self.customerSatisfaction = self.satisfactionFactor / self.passengersWaitingTime * self.methodSatisfactionPenalty


    def proceedBoarding(self):
        tNextEvent = 100000     # Large number, used to calculate next event
        iNextEvent = 0
        packMu = 7 # A: mean time and stdev [sec] to pack carry-on luggage
        packSigma = 2 # A: source: flight attendant friend :P
        interferenceMu = 4 # Extra time to get seated if there's a passenger in the way
        interferenceSigma = 2
        satisfactionFactor = 1
        # Move first person in waiting list into empty spot in aisle if not occupied
        if self.aisle[0] == '' and (not self.waitingList == []):
            self.aisle[0] = self.waitingList.pop(0)
            self.aisle[0].status = 'walking'
            self.aisle[0].t = random.random()

        for iAisleSpot, aisleSpot in reversed(list(enumerate(self.aisle))):

            # Check if by their seat row, if so take action
            if (not aisleSpot == '') and aisleSpot.seat['row'] == iAisleSpot and aisleSpot.status == 'walking':
                if aisleSpot.luggage:
                    aisleSpot.status = 'packing'
                    aisleSpot.t = random.gauss(packMu, packSigma)
                    aisleSpot.packingTime = aisleSpot.t
                else:
                    aisleSpot.t = 0
                    aisleSpot.packingTime = 0
                    if aisleSpot.seat['side'] == 'L':
                        for iSeat, seat in enumerate(self.leftHandSeats[aisleSpot.seat['row']]):
                            if (iSeat < aisleSpot.seat['number']) and (not (seat == '')):
                                aisleSpot.t += random.gauss(interferenceMu, interferenceSigma)
                                aisleSpot.status = 'interfering'

                    else:
                        for iSeat, seat in enumerate(self.rightHandSeats[aisleSpot.seat['row']]):
                            if (iSeat < aisleSpot.seat['number']) and (not (seat == '')):
                                aisleSpot.t += random.gauss(interferenceMu, interferenceSigma)
                                aisleSpot.status = 'interfering'
                    if not aisleSpot.status == 'interfering':
                        if aisleSpot.seat['side'] == 'L':
                            self.leftHandSeats[aisleSpot.seat['row']][aisleSpot.seat['number']] = aisleSpot
                        else:
                            self.rightHandSeats[aisleSpot.seat['row']][aisleSpot.seat['number']] = aisleSpot
                        aisleSpot.status = 'seated'
                        aisleSpot.totalWaitingTime = self.tBoarding - aisleSpot.seat["row"] / aisleSpot.speed - aisleSpot.packingTime  # A: accounts for waiting and interference times
                        self.passengersWaitingTime += aisleSpot.totalWaitingTime
                        self.aisle[iAisleSpot] = ''
                        aisleSpot = ''
                        self.nSeatedPassengers += 1

            # Check if they account for next event to occur, if so set the time to elapse (tNextEvent) to their time t
            if ((not aisleSpot == '') and aisleSpot.t < tNextEvent
                and (self.aisle[np.minimum(iAisleSpot + 1, self.nRows-1)] == '' or not aisleSpot.status == 'walking')):
                if aisleSpot.t < 0:
                    aisleSpot.t = 0
                tNextEvent = aisleSpot.t
                iNextEvent = iAisleSpot
        actingAgent = self.aisle[iNextEvent]  # Passenger accounting for next event
        if actingAgent == '':
            return 0
        # Elapse time until next event
        self.tBoarding += tNextEvent
        for aisleSpot in self.aisle:
            if not aisleSpot == '':
                aisleSpot.t -= tNextEvent


        # Move passenger to next spot in aisle
        if actingAgent.status == 'walking':
            actingAgent.t = 1/actingAgent.speed  # A: Time to walk one row
            self.aisle[iNextEvent + 1] = actingAgent
            self.aisle[iNextEvent] = ''
        # Passenger starts trying to sit down but interferes with already seated passengers
        elif actingAgent.status == 'packing':
            actingAgent.status = 'interfering'
            if actingAgent.seat['side'] == 'L':
                for iSeat, seat in enumerate(self.leftHandSeats[actingAgent.seat['row']]):
                    if (iSeat < actingAgent.seat['number']) and (not (seat == '')):
                        actingAgent.t += random.gauss(interferenceMu, interferenceSigma)

            else:
                for iSeat, seat in enumerate(self.rightHandSeats[actingAgent.seat['row']]):
                    if (iSeat < actingAgent.seat['number']) and (not (seat == '')):
                        actingAgent.t += random.gauss(interferenceMu, interferenceSigma)

        # Passenger sits down
        elif actingAgent.status == 'interfering':
            if actingAgent.seat['side'] == 'L':
                self.leftHandSeats[actingAgent.seat['row']][actingAgent.seat['number']] = actingAgent
            else:
                self.rightHandSeats[actingAgent.seat['row']][actingAgent.seat['number']] = actingAgent
            actingAgent.status = 'seated'
            actingAgent.totalWaitingTime = self.tBoarding - actingAgent.seat["row"] / actingAgent.speed - actingAgent.packingTime # A: accounts for waiting and interference times
            self.passengersWaitingTime += actingAgent.totalWaitingTime
            self.aisle[iNextEvent] = ''
            self.nSeatedPassengers += 1

    def randomBoarding(self):
        tempWaitingList = list(self.passengers)
        random.shuffle(tempWaitingList)
        self.waitingList = tempWaitingList

    def backToFrontBoarding(self):
        tempWaitingList = list(self.passengers)
        blocks = self.nBlocks  # A: number of blocks/zones to divide the passengers
        blockSize = self.nPassengers / blocks
        self.waitingList = []
        for iBlocks in range(blocks - 1):
            chunk = tempWaitingList[iBlocks * blockSize:(iBlocks + 1) * blockSize]
            random.shuffle(chunk)
            self.waitingList.append(chunk)
        chunk = tempWaitingList[
                (blocks - 1) * blockSize:]  # A: from the last block to the end, to account for nSeats%blocks~=0
        random.shuffle(chunk)
        self.waitingList.append(chunk)
        self.waitingList = list(itertools.chain.from_iterable(self.waitingList))
        self.waitingList.reverse()

    def outsideInBoarding(self):
        tempWaitingList = list(self.passengers)
        self.waitingList = []
        for iSeatNumber in range(self.nSeatsPerRow):
            chunk = [tempWaitingList[iOutside] for iOutside in range(self.nPassengers) if
                     tempWaitingList[iOutside].seat['number'] == iSeatNumber]
            random.shuffle(chunk)
            self.waitingList.append(chunk)
        self.waitingList = list(itertools.chain.from_iterable(self.waitingList))
        self.waitingList.reverse()

    def flyingCarpetBoarding(self):
        tempWaitingList = list(self.passengers)
        randomOrder = np.random.permutation(self.nPassengers)
        blocks = self.nBlocks  # A: number of blocks/zones to divide the passengers
        blockSize = self.nPassengers / blocks
        flyingCarpetOrder = []

        for iBlocks in range(blocks - 1):
            chunk = randomOrder[iBlocks * blockSize:(iBlocks + 1) * blockSize]
            chunk.sort()
            flyingCarpetOrder.extend(chunk)

        chunk = randomOrder[(blocks - 1) * blockSize:]  # A: from the last block to the end, to account for nSeats%blocks~=0
        chunk.sort()
        flyingCarpetOrder.extend(chunk)

        self.waitingList = [tempWaitingList[iOrder] for iOrder in flyingCarpetOrder]
        self.waitingList.reverse()

    def reportWaitingTimes(self):
        tempPassengerList = self.passengers
        return [tmp.totalWaitingTime for tmp in tempPassengerList]

# airplane = Airplane(10,3,'outsideIn', 4, 0.5, 0.5)
# airplane.board()
# print airplane.tBoarding, airplane.customerSatisfaction
