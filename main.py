import sys
import os

FSK = 0
BPSK = 1
AFSK = 2

mode = FSK
cycle = False
cw_id = True

if __name__ == "__main__":
#    print(f"Arguments count: {len(sys.argv)}")
#    for i, arg in enumerate(sys.argv):
#        print(f"Argument {i:>6}: {arg}")
#
    print 'Length: ', len(sys.argv)
    
    if (len(sys.argv)) > 1:
#        print("There are arguments!")
        if (('a' == sys.argv[1]) or ('afsk' in sys.argv[1])):
            mode = AFSK
            print("AFSK") 
        elif (('f' == sys.argv[1]) or ('fsk' in sys.argv[1])):
            mode = FSK
            print("FSK") 
        elif (('b' == sys.argv[1]) or ('bpsk' in sys.argv[1])):
            mode = BPSK
            print("BPSK")
        elif (('c' == sys.argv[1]) or ('cycle' in sys.argv[1])):
            cycle = True 
            print("Cycle mode on!")
    if (len(sys.argv)) > 2:
        str = sys.argv[2]
        print "Str: ", str
#        print ("isnumeric: ", str.isnumeric()
        if (str.isnumeric() == True):
            loop = int(sys.argv[2])
            print "Loop: ", loop
    if (len(sys.argv)) > 3:
        if (('n' in sys.argv[3]) or ('no' in sys.argv[3])):
            cw_id = False
            print ("No CW ID")
        else:
            cw_id = True
            print ("CW ID")            

#
# check for SPI
stream = os.popen('ls /dev/spidev0.* 2>&1')
output = stream.read()

print 'Output: ', output

# expected failure string is ls: cannot access '/dev/spidev0.*': No such file or directory

if ('cannot access' in output):
    print "SPI is not present!"
 


