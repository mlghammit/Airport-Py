from pathlib import Path
from Flight import *
from Airport import *

HOME = Path(__file__).parent
class Aviation:
    def __init__(self):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}

    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries

    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights

    def getAllCountries(self):
        return self._allCountries

    def loadData(self, airportFile, flightFile, countriesFile):
        try:

            # with open(HOME / countriesFile, 'r', encoding='utf8') as countriesFileName:
            #     for line in countriesFileName:
            #         continent, country = map(str.strip, line.split(','))
            #         self._allCountries[country] = continent

            # with open (HOME / airportFile, 'r', encoding='utf8') as airportFileName:
            #     for line in airportFileName:
            #         code, country, city = map(str.strip, line.split(','))
            #         airport = Airport(code, country, city)
            #         self._allAirports.append(airport)

            # with open(HOME /flightFile, 'r', encoding='utf8') as flightsFileName:
            #     for line in flightsFileName:
            #         flightNo, origin, destination = map(str.strip, line.split(','))
            #         flight = Flight(flightNo, self.getAirportByCode(origin), self.getAirportByCode(destination))
            #         if origin not in self._allFlights:
            #             self._allFlights[origin] = []
            #         self._allFlights[origin].append(flight)

        #     with open(HOME / airportFile, "r", encoding='utf8') as airportFileName:
        #         for line in airportFileName:
        #             line = line.strip().split(",")
        #             airport = Airport(line[0].strip(), line[1].strip(), line[2].strip())
        #             airport.setContinent(self._allCountries[airport.getCountry()])
        #             self._allAirports.append(airport)

        #     with open(HOME / flightFile, "r", encoding='utf8') as flightFileName:
        #         for line in flightFileName:
        #             flight = Flight(line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip(), line[4].strip(), line[5].strip(), line[6].strip())
        #             if flight.getOrigin() not in self._allFlights:
        #                 self._allFlights[flight.getOrigin()] = [flight]
        #             else:
        #                 self._allFlights[flight.getOrigin()].append(flight)
        #             origAirport = self.getAirportByCode(line[1].strip())
        #             destAirport = self.getAirportByCode(line[2].strip())
        #             flight = Flight(line[0].strip(), origAirport, destAirport, line[3].strip(), line[4].strip(), line[5].strip(), line[6].strip())
        #             if flight.getOrigin() not in self._allFlights:
        #                 self._allFlights[flight.getOrigin()] = [flight]
        #             else:
        #                 self._allFlights[flight.getOrigin()].append(flight)


        #     with open(HOME /  countriesFile, "r", encoding='utf8') as countriesFileName:
        #         for line in countriesFileName:
        #             line = line.strip().split(",")
        #             self._allCountries[line[0].strip()] = line[1].strip()
        #     return True

        # except FileNotFoundError as e:
        #     print(e)
        #     return False

        #    with open(countriesFile, 'r', encoding='utf8') as f:
        #        for line in f:
        #            continent, country = map(str.strip, line.split(','))
        #            self._allCountries[country] = continent


        #    # Loading airports
        #    with open(airportFile, 'r', encoding='utf8') as f:
        #        for line in f:
        #            code, name, country = map(str.strip, line.split(','))
        #            airport = Airport(code, name, country, self._allCountries[country])
        #            self._allAirports.append(airport)


        #    # Loading flights
        #    with open(flightFile, 'r', encoding='utf8') as f:
        #        for line in f:


        #            flightNo, origin, destination = map(str.strip, line.split(','))
        #            flight = Flight(flightNo, self.getAirportByCode(origin), self.getAirportByCode(destination))
        #            if origin not in self._allFlights:
        #                self._allFlights[origin] = []
        #            self._allFlights[origin].append(flight)

            with open(countriesFile, 'r', encoding='utf8') as f:
                for line in f:
                    country,continent = line.strip().split(',')
                    self._allCountries[country.strip()] = continent.strip()
            
            with open(airportFile, 'r', encoding='utf8') as f:
                for line in f:
                    airport_info = line.strip().split(',')
                    code = airport_info[0].strip()
                    name = airport_info[1].strip()
                    country = airport_info[2].strip()
                    continent = self._allCountries[country]
                    airport = Airport(code, name, country, continent)
                    self._allAirports.append(airport)
            
            with open(flightFile, 'r', encoding='utf8') as f:

                flight_info = line.strip().split(',')
                flightNo = flight_info[0].strip()
                origin = flight_info[1].strip
                destination = flight_info[2].strip()
                
                flight = Flight(flightNo, origin, destination)
                if origin in self._allFlights:
                    self._allAirports[origin].append(flight)
                else:
                    self._allFlights[origin] = [flight]
            

            return True


        except Exception as e:
            print("Error: " + (str(e)))
            return False
        
    def getAirportByCode(self, code):
        for airport in self._allAirports:
            if airport.getCode() == code:
                return airport
        return -1

    def findAllCityFlights(self, city):
        flights = []
        for flightList in self._allFlights.values():
            for flight in self._allFlights[city.strip()]:
                if flight.getOrigin().getCity() ==  city or flight.getDestination().getCity() == city.strip():
                    flights.append(flight)
            
            return flights

    def findFlightByNo(self, flightNo):
        for flightList in self._allFlights.values():
            for flight in flightList:
                if flight.getFlightNumber() == flightNo:
                    return flight
        return -1

    def findAllCountryFlights(self, country):
        country_flights = []
        for flight_list in self._allFlights.values():
            for flight in flight_list:
                if flight.getDestinationCountry() == country or flight.getOriginCountry() == country:
                    country_flights.append(flight)
        return country_flights
        #         if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country:
                
        # return flights

    def findFlightBetween(self, origAirport, destAirport):
        for flight_list in self._allFlights.get(origAirport.getCode(), []):
            if flight_list.getDestination() == destAirport.getCode():
                return f"Direct Flight({flight_list.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"

        connecting_airports = set()
        for flight_list in self._allFlights.get(origAirport.getCode(), []):
            connecting_airport = self.getAirport(flight_list.getDestination())
            connecting_airports.add(connecting_airport)

        for connecting_airport in connecting_airports:
            if self.hasDirectFlight(connecting_airport, destAirport):
                return f"Connecting Flight: {origAirport.getCode()} to {connecting_airport.getCode()} to {destAirport.getCode()}"

        return "No flights available between these airports."


    def findReturnFlight(self, firstFlight):
        dest = firstFlight.getDestination()
        orig = firstFlight.getOrigin()
        
        for flight_list in self._allFlights.get(dest, []):
            if flight_list.getDestination() == orig:
                return flight_list
            
        return -1
    
    def findFlightsAcross(self, ocean):
        green_zone = {"US", "Canada", "Mexico", "Brazil", "Argentina"}
        red_zone = {"China", "Japan", "Australia"}
        blue_zone = {"France", "Germany", "Spain", "Italy", "UK"}
        
        if ocean == "Atlantic":
            return_flights = set()
            for dest in blue_zone:
                for flight_list in self._allFlights.get(dest, []):
                    if flight_list.getOrigin() in green_zone:
                        return_flights.add(flight_list.getFlightNumber())
            for orig in green_zone:
                for flight_list in self._allFlights.get(orig, []):
                    if flight_list.getDestination() in blue_zone:
                        return_flights.add(flight_list.getFlightNumber())
            if not return_flights:
                return -1
            return return_flights
        
        elif ocean == "Pacific":
            return_flights = set()
            for dest in red_zone:
                for flight_list in self._allFlights.get(dest, []):
                    if flight_list.getOrigin() in green_zone:
                        return_flights.add(flight_list.getFlightNumber())
            for orig in green_zone:
                for flight_list in self._allFlights.get(orig, []):
                    if flight_list.getDestination() in red_zone:
                        return_flights.add(flight_list.getFlightNumber())
            if not return_flights:
                return -1
            return return_flights
        
        else:
            return -1

    loadData(' ' ,'/Users/hamzakhamissa/Desktop/Comp sci 1026B/Assignment 4/Airport.py', '/Users/hamzakhamissa/Desktop/Comp sci 1026B/Assignment 4/flights.txt', '/Users/hamzakhamissa/Desktop/Comp sci 1026B/Assignment 4/countries.txt')
