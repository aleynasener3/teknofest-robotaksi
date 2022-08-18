import RPi.GPIO as GPIO
import time
import piplates.MOTORplate as MOTOR
import logging
import sys
from Adafruit_BNO055 import BNO055
from picamera import PiCamera
import cv2
import numpy as np
from matplotlib import pyplot as plt

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#MOTOR Set Up
def MOTOR_SET_UP():
        MOTOR.dcCONFIG(0,2,'ccw',70.0,0)
        MOTOR.dcCONFIG(0,3,'cw',70.0,0)
        return


        
#Motor istenen mesafeye cm cinsinden gidecek
def MOTOR_run(mesafe):
        tacho_counter_now = tacho_counter
        print(tacho_counter_now)
        MOTOR.dcSTART(0,2)
        MOTOR.dcSTART(0,3)
        while True:
            fark_tacho_counter = tacho_counter-tacho_counter_now    
            print("fark tacho counter ", fark_tacho_counter)            
            if fark_tacho_counter >= (mesafe/1.02): #/1.15 denemeyle bulunan düzeltme oranı
                MOTOR.dcSTOP(0,2)
                MOTOR.dcSTOP(0,3)
                print("stop")   
                break
        return
        
#BNO055 Initialization


def GYRO_SET_UP():
        import sys
        bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
        if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
                logging.basicConfig(level=logging.DEBUG)

        if not bno.begin():
                raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

        status, self_test, error = bno.get_system_status()
        print('System status: {0}'.format(status))
        print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
        # Print out an error if system status is in error mode.
        if status == 0x01:
                print('System error: {0}'.format(error))
                print('See datasheet section 4.3.59 for the meaning.')

        #Print BNO055 software revision and other diagnostic data.
        sw, bl, accel, mag, gyro = bno.get_revision()
        print('Software version:   {0}'.format(sw))
        print('Bootloader version: {0}'.format(bl))
        print('Accelerometer ID:   0x{0:02X}'.format(accel))
        print('Magnetometer ID:    0x{0:02X}'.format(mag))
        print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

        print('Reading BNO055 data, press Ctrl-C to quit...')
        return bno
#End of BNO055 Initialization

def GYRO_HEADING():
        heading, roll, pitch = bno.read_euler()
        sys, gyro, accel, mag = bno.get_calibration_status()
        return heading

def ROTATE(heading,derece):
        fark = derece - heading
        print("derece ", derece, "heading ", heading, "fark ", fark)
        if fark >= 0 and abs(fark) >= 180:
                donus_yonu = "sol"
        if fark < 0 and abs(fark) >= 180:
                donus_yonu = "sag"
        if fark >= 0 and abs(fark) < 180:
                donus_yonu = "sag"
        if fark < 0 and abs(fark) < 180:
                donus_yonu = "sol"
        print("donus yonu ", donus_yonu)
        if donus_yonu=="sol":
                MOTOR.dcCONFIG(0,2,'Cw',50.0,0)
                MOTOR.dcCONFIG(0,3,'cw',80.0,0)
                MOTOR.dcSTART(0,2) 
                MOTOR.dcSTART(0,3)
        if donus_yonu=="sag":
                MOTOR.dcCONFIG(0,2,'ccw',80.0,0)
                MOTOR.dcCONFIG(0,3,'ccw',40.0,0)
                MOTOR.dcSTART(0,2)
                MOTOR.dcSTART(0,3)

        while True:
                heading = GYRO_HEADING()
                print("heading ", heading)     
                if heading+2>derece>heading-2:
                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)
                        break                             
                    
        
        return 

def ULTRASONIC_SET_UP():
        TRIG = 23
        ECHO = 24

        print ("HC-SR04 mesafe sensoru")

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        return


def ULTRASONIC_DISTANCE():
        TRIG = 23
        ECHO = 24

        print ("HC-SR04 mesafe sensoru")


        GPIO.output(TRIG, False)
        #print ( "Olculuyor...")
        #time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
                pulse_start = time.time()

        while GPIO.input(ECHO)==1:
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance > 2 and distance < 400:
                print ("Mesafe:",distance - 0.5,"cm")
        else:
                print ("Menzil asildi")

        return distance





MOTOR_SET_UP()
bno = GYRO_SET_UP()
ULTRASONIC_SET_UP()





#robot ilk çalıştığında başlangıç noktasına baksın
heading_initial = GYRO_HEADING()
print("heading initial", heading_initial)


yon=1 #düz
distance=ULTRASONIC_DISTANCE()
heading=GYRO_HEADING()
bheading=180
nheading=0
MOTOR.dcCONFIG(0,2,'cw',70.0,0)
MOTOR.dcCONFIG(0,3,'cw',70.0,0)
print("başlangıç",bheading)
while True:
        MOTOR.dcCONFIG(0,2,'cw',70.0,0)
        MOTOR.dcCONFIG(0,3,'cw',70.0,0)
        print("mesafe",distance)
        distance=ULTRASONIC_DISTANCE()
        heading=GYRO_HEADING()
        if distance>10:
                heading=GYRO_HEADING()
                if 180>heading>0:
                        nheading=heading+180
                        #print(nheading)
                
                if 360>heading>180:
                        nheading=heading-180
                        #print(nheading)
                if nheading>bheading:#sağa döndün sola dön
                        MOTOR.dcSPEED(0,2,50.0)
                        MOTOR.dcSPEED(0,3,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+2>nheading>bheading-2:
                                MOTOR.dcSPEED(0,3,60.0)
                                MOTOR.dcSPEED(0,2,60.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)
                        
                        
                                #time.sleep(5)
                if nheading<bheading:#sola döndün sağa dön
                        MOTOR.dcSPEED(0,3,50.0)
                        MOTOR.dcSPEED(0,2,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+2>nheading>bheading-2:
                                MOTOR.dcSPEED(0,2,60.0)
                                MOTOR.dcSPEED(0,3,60.0)
                                MOTOR.dcSTART(0,2)
                                MOTOR.dcSTART(0,3)
                                #time.sleep(5)
        
        else:
                MOTOR.dcSTOP(0,2)
                MOTOR.dcSTOP(0,3)
                MOTOR.dcCONFIG(0,2,'ccw',40.0,0)
                MOTOR.dcCONFIG(0,3,'ccw',40.0,0)
                MOTOR.dcSTART(0,2) 
                MOTOR.dcSTART(0,3)
                heading=GYRO_HEADING()
                if 180>heading>0:
                        nheading=heading+180
                        #print(nheading)
                
                if 360>heading>180:
                        nheading=heading-180
                        #print(nheading)
                if nheading>bheading:#sağa döndün sola dön
                        MOTOR.dcSPEED(0,2,50.0)
                        MOTOR.dcSPEED(0,3,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+2>nheading>bheading-2:
                                MOTOR.dcSPEED(0,3,50.0)
                                MOTOR.dcSPEED(0,2,50.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)
                        
                        
                                #time.sleep(5)
                if nheading<bheading:#sola döndün sağa dön
                        MOTOR.dcSPEED(0,3,50.0)
                        MOTOR.dcSPEED(0,2,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+2>nheading>bheading-2:
                                MOTOR.dcSPEED(0,2,50.0)
                                MOTOR.dcSPEED(0,3,50.0)
                                MOTOR.dcSTART(0,2)
                                MOTOR.dcSTART(0,3)
                                #time.sleep(5)
                if 15>distance>10:
                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)  
               

 





  
GPIO.cleanup()
