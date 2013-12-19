# A set of common functions grouped into related classes for use within the main RFID application.
#   This should be imported at the start of the python file using 'import RFIDBasicAuth_functions'

class ID12:
    def __init__(self, extSerial):
        self.serial = extSerial

    def getTag(self):

        tagData = ''
        # Loop until broken
        while True:
            byteData = self.serial.read(1)

            # Break loop on CR
            if byteData == '\r':
                break
            else:
                tagData = tagData + byteData

        print("Raw Serial Data: " + tagData)
        return tagData[:10] # Return only the first 10 ASCII chars, forget 2 char checksum

# Example second class stub...
class OtherFunctions:
    def __init__(self, inVar):
        self.localVar = inVar

    def foo(self, bar):
        return bar + self.localVar;
