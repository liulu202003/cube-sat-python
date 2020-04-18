import sys
import os

FSK = 0
BPSK = 1
AFSK = 2

mode = FSK
cycle = False

if __name__ == "__main__":
#    print(f"Arguments count: {len(sys.argv)}")
#    for i, arg in enumerate(sys.argv):
#        print(f"Argument {i:>6}: {arg}")
#
    if (len(sys.argv)) > 0:
#        print("There are arguments!")
        if ('a' in sys.argv[1]):
            mode = AFSK
            print("AFSK") 
        if (sys.argv[1][0] == 'f'):
            mode = FSK
            print("FSK") 
        if (sys.argv[1][0] == 'b'):
            mode = BPSK
            print("BPSK")
        if (sys.argv[1][0] == 'c'):
            cycle = True 
            print("Cycle mode on!")
#
# check for SPI
stream = os.popen('ls /dev/spidev0.* 2>&1')
output = stream.read()

print 'Output: ', output

# expected failure string is ls: cannot access '/dev/spidev0.*': No such file or directory

if ('cannot access' in output):
    print "SPI is not present!"
 


