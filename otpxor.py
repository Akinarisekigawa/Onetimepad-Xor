#One Time Pad XOR by @Sekigawaakinari
class OTP:
    def __init__(self, aKey):
        self.key = aKey
        self.crc = 0    
        for x in self.key:
            intX = ord(x)
            self.crc = self.crc ^ intX

    def Crypt(self, aString):
        kIdx = 0
        cryptStr = ""  
        for x in range(len(aString)):
            cryptStr = cryptStr + \
                       chr( ord(aString[x]) ^ ord(self.key[kIdx]))
            kIdx = (kIdx + 1) % len(self.key)

        return cryptStr

if __name__ == "__main__":

    def strkehex(aString):
        hexStr = ""
        for x in aString:
            hexStr = hexStr + "%02X " % ord(x)

        return hexStr

    print "\nTesting OTP!"
    print "----------------\n"

    Kunci = "initest"
    tesString = "test"

    print "\nString : ", tesString
    print "dalam hex : ", strkehex(tesString)
    print "kunci    : ", Kunci

    pe = OTP(Kunci)
    
    #print "\nOTP CRC = %02X" % pe.crc

    tesString = pe.Crypt(tesString)
    print "\nEnkripsi string"
    print "Ascii  : ", tesString
    print "Hex    : ", strkehex(tesString)

    tesString = pe.Crypt(tesString)
    print "\nDeskripsi string"
    print "Ascii  : ", tesString
    print "Hex    : ", strkehex(tesString)