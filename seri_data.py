import serial
import time
data = '321'
ser = serial.Serial('/dev/ttyACM0',baudrate=9600, timeout=3.0)
time.sleep(5)
ser.write(b'A')
ser.write(b'B')
