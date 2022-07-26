import requests
import json
import constants
import datetime


class NextBus(object):

    def __init__(self):
        pass

    def get_route_id(self, bus_route):
    #This method calls /NexTripv2/Routes and return Route Id which is the route code for the given bus route string
    #http://svc.metrotransit.org/NexTripv2/Routes?format=json

        bus_route = bus_route.lower()
        url = '{}NexTripv2/Routes?format=json'.format(constants.ENDPOINT)
        response = requests.get(url=url)
        data = json.loads(response.text)
        route = str('')
        route_id = 0

    #Returns a list of Transit routes that are in service on the current day.
        for i in range(0, len(data)):
            route_label = data[i]['route_label'].lower()

            if (route_label == bus_route):
                route_id = data[i]['route_id']

        if (route_id == 0):
            print('No route found!')
            exit()
        return route_id

    def get_direction_id(self, direction):
    # verifies the direction and if found matched direction return the valid ID
        dir = [value for key, value in constants.DIRECTIONS.items() if direction.lower() in  key]
        if not dir: # exit if not 1 = South, 2 = East, 3 = West, 4 = North
            print('You have entered an invalid direction')
            exit()
        return dir[0]

    def get_stop_code(self, bus_stop, bus_route, direction):
    #Returns the stop location short code for the given Route/Direction
    # Example url : http://svc.metrotransit.org/NexTripv2/Stops/901/1/?format=json
        url = '{}NexTripv2/Stops/{}/{}?format=json'.format(constants.ENDPOINT, bus_route, direction)
        resp = requests.get(url=url)
        data = json.loads(resp.text)

        for i in range(len(data)):
            if (bus_stop == data[i]['description'] or bus_stop == data[i]['place_code']):
                stop = data[i]['place_code'] 

        if (len(stop) == 0):
          print('No buses found for this direction')
          exit()
        return stop

    def get_nextrip_dept_time(self, bus_route, direction, bus_stop):
    # Returns the scheduled departures for a selected route, direction and timepoint stop.
    # Example url : http://svc.metrotransit.org/NexTripv2/Stops/901/1/TF2?format=json
        url = '{}NexTripv2/{}/{}/{}?format=json'.format(constants.ENDPOINT, bus_route, direction, bus_stop)
        resp = requests.get(url=url)
        data = json.loads(resp.text)

        departures = data['departures']
        dept_time = data['departures'][0]['departure_time']
        return dept_time

    def parse_time(self, time):
    #datetime value of the departure time. Convert the time to readable format in mins
        bus_time = datetime.datetime.fromtimestamp(time)
        now = datetime.datetime.now()
        minutes = str(bus_time - now).split(":")[1] # get the minutes from the timestamps
        return minutes
