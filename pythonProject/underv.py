"""
This is to calculate the time for the under voltage element to operate
It takes in a few arguments
-D = delay setting
-V = actual average phase to phase voltage/test voltage in kV eg. 10.8kV
-Vnom = the nominal voltage say 11kV
-P = pickup setting for undervoltage.

A usage example is:

"""

import math
import argparse

parser =argparse.ArgumentParser(description='Calculale the time for undervoltage trip')

parser.add_argument('-D', '--delay', type=float, metavar=' ', required=True, help='delay setting')
parser.add_argument('-V', '--voltage', type=float, metavar='', required=True, help='test voltage in kV')
parser.add_argument('-P', '--pickup', type=float, metavar='', required=True, help='Undervoltage pickup setting p-p primary voltage in kv')

args = parser.parse_args()

def trip_time (delay, voltage, pickup):

    if voltage>pickup:
        x=(voltage/pickup)-1
        y=delay/x
        time_to_trip = y
    else:
        time_to_trip =-1
        print('No Trip return -1')
    return time_to_trip

if __name__ == '__main__':

    print(f'The under voltage trip time is: {round(trip_time(args.delay, args.voltage, args.pickup),3)}')
