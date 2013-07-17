 #!/usr/bin/python
###############################################################################
#@@@@ Serial Port AT / Motorola-EX116-COM /redcod3 -python2.7.3 version @@@@@@#
###############################################################################


import serial
import time

###############Settings serial port###############################
ser = serial.Serial()
ser.port = "/dev/serial/by-id/usb-Motorola_MOTO-if01" #Serial Port
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = True     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = True       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

############# verify Open Serial Port ############################
try:
    ser.open()

except Exception, e:
    print "error open serial port: " + str(e)
    exit()

if ser.isOpen():
    try:
        ser.flushInput() #verify read input
        ser.flushOutput() #verify read output
        print "[+]Device connect on Serial Port :"+ser.port
        numero = raw_input('Phone Number: ') #Phone number
        print '[+]Call Number : '+numero
        time.sleep(5) #Time waiting for Call
        ser.write('atd'+numero+'\r')
        response = ser.readline()
        time.sleep(4) #Time waiting for Close
        ser.write('ath\r')
        print 'Call terminate'

    except Exception, e1:
        print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "

print 'conexion terminada'
