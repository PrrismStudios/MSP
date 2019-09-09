import serial, struct

class MultiWii:
    def __init__(self, SerialPort:str, BaudRate:int=115200):
        """
        Initialise Serial communication with Flight Controller
        Takes Serial Port address(required) and Baud Rate (defaults to 115200) as parameters 
        """
        self.com = serial.Serial(SerialPort, BaudRate, timeout=1)

    def send(self, command, data:list=[]):
        size = 2 * ((len(data)) & 0xFF)
        senddata = ['$'.encode('utf-8'), 'M'.encode('utf-8'), command['direction'].encode('utf-8'), size, command['message_id']] + data
        checksum = 0
        for i in senddata[3: len(senddata)]:
            checksum ^= i
        senddata.append(checksum)
        self.com.write(struct.pack('<3c3B', *senddata))
        return True

    def crc(self, command, data):
        size = 2 * ((len(data)) & 0xFF)
        checksum = size ^ command['message_id']
        

    def receive(self):
        while True:
            header = self.com.read().decode('utf-8')
            if header == '$':
                header += self.com.read(2).decode('utf-8')
                break
        datalength = struct.unpack('<b', self.com.read())[0]
        print("datalength: "+str(datalength))
        code = struct.unpack('<b', self.com.read())
        print('code: '+str(code))
        data = self.com.read(datalength)
        received = struct.unpack('<'+'h'*int(datalength/2),data)
        self.com.flushInput()
        self.com.flushOutput()
        return received