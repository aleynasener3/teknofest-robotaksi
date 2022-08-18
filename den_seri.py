import serial

ser = serial.Serial('/dev/ttyACM1', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
while 1:
    ser.write(b'23')