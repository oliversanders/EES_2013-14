import serial

# Route via virtual COM ports master/slave using com0com (Win), Pty (Linux) or VirtualSerialPortApp (OSX)
serial = serial.Serial("/dev/master", baudrate=9600)

print "Note: STX, CR, LF and ETX bytes are added for you..."
var = raw_input("Enter Tag ASCII-Hex To Send (with/without Checksum): ")

serial.write(chr(0x02))
serial.write(var)
serial.write('\r\n')
serial.write(chr(0x03))
serial.flush()

print "Sent Tag: " + var

serial.close()

