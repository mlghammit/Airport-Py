from Airport import *

class Flight:
   
    def __init__(self, flightNo, origAirport, destAirport):
        if not (isinstance(origAirport, Airport) and isinstance(destAirport, Airport)):
            raise TypeError("The origin and destination must be Airport objects")
        
        if not (isinstance(flightNo, str) or len(flightNo) !=  6 or not flightNo[:3].isalpha() or not flightNo[3:].isdigit()):
            raise TypeError("The flight number format is incorrect")
        
        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport

      

    def __repr__(self):
        domesticOrInternational = "[domestic]" if self.isDomesticFlight() else "[international]"
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} {domesticOrInternational}"
    
    def __eq__(self, other):
        if isinstance(other, Flight):
            return self._origin == other._origin and self._destination == other._destination
        else:
            return False


    def getFlightNumber(self):
         return self._flightNo
    
    def getOrigin(self):
         return self._origin

    def getDestination(self):
         return self._destination

    def isDomesticFlight(self):
         return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
            if not isinstance(origin, Airport):
                 raise TypeError("The origin must be an Airport object")
            
            self._origin = origin

    def setDestination(self, destination):
         if not isinstance(destination, Airport):
              raise TypeError("The destination must be an Airport object")
         self._destination = destination
