import RFIDBasicAuth_functions
import serial

# Main program sequence

# Setup serial port - remember to change this port name...
serial = serial.Serial("/dev/slave", baudrate=9600, timeout=None)
id12 = RFIDBasicAuth_functions.ID12(serial)

print "Waiting For RFID Tag..."

# Main reader loop
while True:

    # Read only 1 byte - to look for ASCII STX
    initialData = serial.read(1)
    currentTag = ""

    # Wait for start of tag, an STX byte
    if initialData == chr(0x02):
        currentTag = id12.getTag()

        # Check size of data, should be 10 ASCII chars (with no 2 char checksum)
        if len(currentTag) == 10:
            print "RFID Tag Read: " + currentTag

            # Check if tag is in Allowed People List
            if currentTag in open('AllowedPeopleList.csv').read():
                print "Welcome Authorised User..."
                # ToDo: Send RPi GPIO line High/Low for period of time to switch solenoid lock circuit

            # Else check if tag is in Asset List
            elif currentTag in open('AssetList.csv').read():
                print "Known Asset Identified!"
                # ToDo: Log asset state and date/time somewhere (e.g. expanded csv file with commas/lines for 2D table array??)

            # Not on either list.. unrecognised tag!
            else:
                print "RFID Tag Unrecognised!"

        else:
            print "Read Data Length Is Invalid!"

        print "\r\nWaiting for RFID tag..."

