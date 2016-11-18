import numpy as np

class Passenger():
    def __init__(self, seat, speed):
        self.seat = seat
        self.speed = speed

class Airplane():
    def __init__(self, nRows, nSeatsPerSide, nPassengers):
        self.nRows = nRows
        self.nSeatsPerRow = nSeatsPerSide
        self.waitingList = [ Passenger('3', 0.5) for iPassenger in range(nPassengers)]
        self.aisle = ['e' for iRows in range(nRows)]
        self.leftHandSeats = [[ 'e' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]
        self.rightHandSeats = [['e' for iSeats in range(nSeatsPerSide)] for iRows in range(nRows)]

airplane = Airplane(5, 2, 10)
print airplane.waitingList