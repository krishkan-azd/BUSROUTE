#!/usr/bin/env python3
# Usage :  
# python .\nextbus.py 'Metro Blue Line' 'Target Field Station Platform 2' 'South'
#  The next bus leaves in 03 minute
# python .\nextbus.py 'Metro Blue Line' 'Target Field Station Platform 2' 'South'
#  The next bus leaves in 09 minute
# python .\nextbus.py 'Metro Blue Line' 'U.S. Bank Stadium Station' 'South'
#  The next bus leaves in 03 minute

import sys
from nextripv2 import NextBus

def main():
    next_bus = NextBus()
    bus_route = next_bus.get_route_id(sys.argv[1])
    direction = next_bus.get_direction_id(sys.argv[3])
    bus_stop = next_bus.get_stop_code(sys.argv[2], bus_route, direction)
    get_nex_trip = next_bus.get_nextrip_dept_time(bus_route, direction, bus_stop)
    mins = next_bus.parse_time(get_nex_trip)

    if (int(mins) >= 1):
        print('The next bus leaves in ' + mins + ' minutes')
    else:
        print('No busses found at this time')


if __name__ == '__main__':
    main()