##
# command line function called cubesatsim with three arguments separated by spaces
# 1. afsk or fsk or bpsk  (or first letter only a or f or b)
# 2. integer loop count
# 3. y or n parameter.
#
# Examples:
#
# cubesatsim fsk
# cubesatsim afsk 3
# cubesatsim a 4
# cubesatsim bpsk 3 n
#
##
# open a tex configuration file called sim.cfg
# if the file doesn't exist, create it
# the first field is a callsign (up to 6 characters)
# next a reset count integer
# increment the count modulo 16 bit
# save the sim.cfg file
#
##
# execute a bash shell script and get the results
# e.g. execute ls /dev/spidev0.* 2>&1
#
##
# store this binary number into a variable 1000111110011010010000101011101
#
##
# create an array of 2 byte (16 bit) values
# 
# create a 2 dimensional array of 1 byte (8 bit) values
#
