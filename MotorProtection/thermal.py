"""
This is to calculate a typical thermal time to trip for an old relay called the RAMDE
But most motor curves follow should follow the same algo. we are using the calculation to calculate and test
an modern ABB REM615 that is replacing that relay
It takes in a few arguments

-tau = the thermal time constant of a motor
-i = actual current injected
-ip = previous current - running at that for longer than 5 x tau so that the temperature is stable .
-ib = the rated current of the motor, the name plate current / ct ratio
-k = security factor, set to 1.02 if not sepecified

A usage example is:

In our example we have chosen a thermal time constant of 120s
The motor is a 132A motor and the cell has a CT ratio of 200, so 0.67
we will do the calculation with no pre load so a cold motor defaults to Ip = 0 if not specified

python thermal.py -tau 120 -ip 0 -ib 0.67 -k 1.02

"""

import math
import argparse

parser =argparse.ArgumentParser(description='Calculale the time to trip for a thermal curve')

parser.add_argument('-tau', '--tau', type=float, metavar=' ', required=True, help='thermal time constant')
parser.add_argument('-ip', '--iprev', type=float, metavar='', default=0, required=False, help='previous current')
parser.add_argument('-i', '--injected', type=float, metavar='', required=True, help='current injected')
parser.add_argument('-ib', '--rated', type=float, metavar='', required=True, help='full load rated secondary current')
parser.add_argument('-k', '--security', type=float, metavar='', default=1.02, required=False, help='security factor')


args = parser.parse_args()

def trip_time (tau, injected, iprev, rated, securityFactor):
    """This method calculated trip times
    it takes in
        tau: which is the set temperature constant for the system
        iprev: is the previous current that was flowing for more than 5 x tau in the system
        injected: is the secondary current value injected
        rated: is the secondary current value that is equivalent to the primary full load current
        securityFactor: is the value above full load that the element will operated eventually.

        It returns a time in seconds
    """
    w = injected**2 - iprev**2
    x = injected**2 - (securityFactor*rated)**2
    y = w/x
    z = math.log(math.e)
    time_to_trip = tau * (z * y)

    return time_to_trip

if __name__ == '__main__':

    print(f'The thermal trip time is: {round(trip_time(args.tau, args.injected, args.iperv, args.rated, args.security),3)}')
