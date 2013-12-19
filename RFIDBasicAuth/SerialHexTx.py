import serial
serial = serial.Serial("/dev/master", baudrate=9600)

var = raw_input("Enter Hex To Send: ")
serial.write(var.decode('hex'))
print "Sent Hex: 0x", var
print "Sent Raw:", var.decode('hex')
