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

import serial
ser = serial.Serial('/dev/ttyACM0',baudrate=9600, timeout=3.0)



# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#LED Set Up
def LED_SET_UP():
                
        GPIO.setup(6, GPIO.OUT)         #Red LED
        return

#RED LED ON
def RED_ON():
        GPIO.output(6,GPIO.HIGH)
        return
#RED LED OFF
def RED_OFF():
        GPIO.output(6,GPIO.LOW)
        return



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


heading=GYRO_HEADING()
bheading=heading
RED_ON()
time.sleep(10)#başlama süresi
yon=1 #düz
distance=ULTRASONIC_DISTANCE()

nheading=0
MOTOR.dcCONFIG(0,2,'cw',70.0,0)
MOTOR.dcCONFIG(0,3,'cw',70.0,0)
print("başlangıç",bheading)
while True:
        MOTOR.dcCONFIG(0,2,'cw',70.0,0)
        MOTOR.dcCONFIG(0,3,'cw',70.0,0)
        #print("mesafe",distance)
        distance=ULTRASONIC_DISTANCE()
        heading=GYRO_HEADING()
        nheading=heading
        print(nheading)
        if distance>25:
                heading=GYRO_HEADING()
                nheading=heading

                if bheading+10>nheading>bheading-10:
                                MOTOR.dcSPEED(0,3,40.0)
                                MOTOR.dcSPEED(0,2,40.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)
                                
                if nheading>bheading:#sağa döndün sola dön
                        MOTOR.dcSPEED(0,2,50.0)
                        MOTOR.dcSPEED(0,3,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+5>nheading>bheading-5:
                                MOTOR.dcSPEED(0,3,40.0)
                                MOTOR.dcSPEED(0,2,40.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)
                        
                        
                                #time.sleep(5)
                if nheading<bheading:#sola döndün sağa dön
                        MOTOR.dcSPEED(0,3,50.0)
                        MOTOR.dcSPEED(0,2,10.0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        if bheading+5>nheading>bheading-5:
                                MOTOR.dcSPEED(0,2,40.0)
                                MOTOR.dcSPEED(0,3,40.0)
                                MOTOR.dcSTART(0,2)
                                MOTOR.dcSTART(0,3)
                                #time.sleep(5)
        distance=ULTRASONIC_DISTANCE()
        #print("mesafe",distance)
        if distance<25:
                heading=GYRO_HEADING()
                nheading=heading
                distance=ULTRASONIC_DISTANCE()
                #print("mesafe",distance)
                MOTOR.dcSTOP(0,2)
                MOTOR.dcSTOP(0,3)
                MOTOR.dcCONFIG(0,2,'ccw',40.0,0)
                MOTOR.dcCONFIG(0,3,'ccw',40.0,0)
                MOTOR.dcSTART(0,2) 
                MOTOR.dcSTART(0,3)
                time.sleep(1)
                MOTOR.dcSTOP(0,2)
                MOTOR.dcSTOP(0,3)
                heading=GYRO_HEADING()
                nheading=heading
                distance=ULTRASONIC_DISTANCE()        
                if distance>30:
                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)
                        MOTOR.dcCONFIG(0,2,'cw',40.0,0)
                        MOTOR.dcCONFIG(0,3,'cw',40.0,0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        time.sleep(1)
                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)

                        distance=ULTRASONIC_DISTANCE()
                        print("mesafe",distance)
                               
                if 30>distance>15:
                        heading=GYRO_HEADING()
                        nheading=heading
                        #print(nheading)
                        print(nheading)
                        if bheading+10>nheading>bheading-10:
                                MOTOR.dcSPEED(0,3,40.0)
                                MOTOR.dcSPEED(0,2,40.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)

                                if 30>distance>15:
                                        MOTOR.dcSTOP(0,2)
                                        MOTOR.dcSTOP(0,3)
                                        break
                                
                        if nheading>bheading:#sağa döndün sola dön
                                MOTOR.dcSPEED(0,2,40.0)
                                MOTOR.dcSPEED(0,3,10.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)

                                
                                if bheading+5>nheading>bheading-5:
                                        MOTOR.dcSPEED(0,3,40.0)
                                        MOTOR.dcSPEED(0,2,40.0)
                                        MOTOR.dcSTART(0,2) 
                                        MOTOR.dcSTART(0,3)
                                        
                        
                        
                                        #time.sleep(5)
                        if nheading<bheading:#sola döndün sağa dön
                                MOTOR.dcSPEED(0,3,40.0)
                                MOTOR.dcSPEED(0,2,10.0)
                                MOTOR.dcSTART(0,2) 
                                MOTOR.dcSTART(0,3)
                                if bheading+5>nheading>bheading-5:
                                        MOTOR.dcSPEED(0,2,40.0)
                                        MOTOR.dcSPEED(0,3,40.0)
                                        MOTOR.dcSTART(0,2)
                                        MOTOR.dcSTART(0,3)
                       

###########################################################
time.sleep(1.5)        
MOTOR.dcCONFIG(0,2,'ccw',40.0,0)
MOTOR.dcCONFIG(0,3,'ccw',40.0,0)
heading=GYRO_HEADING()
heading=GYRO_HEADING()
nheading=heading
print(nheading)
print(bheading)
if nheading>bheading:#sağa döndün sola dön
        MOTOR.dcSPEED(0,2,10.0)
        MOTOR.dcSPEED(0,3,40.0)
        MOTOR.dcSTART(0,2) 
        MOTOR.dcSTART(0,3)
        time.sleep(1)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)                                
                        
                        
                                        #time.sleep(5)
if nheading<bheading:#sola döndün sağa dön
        MOTOR.dcSPEED(0,3,10.0)
        MOTOR.dcSPEED(0,2,40.0)
        MOTOR.dcSTART(0,2) 
        MOTOR.dcSTART(0,3)
        time.sleep(1)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)                       
                        
                        
                
                     
               

 #############################################################



GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
a=0
durum=100
cizgi=0
nokta=0
k=0
m=["","","","","","","","","","","","","","",""]
kelime=["","","",""]
harf=0
hh=0
i=0
durum=1
ab=1
while True:#harf sayısı - üç olmalı
    if ab==1:
        harf1=kelime[hh]
        if harf1=="a":
            ser.write(b'A')

        if harf1=="b":
            ser.write(b'B')

        if harf1=="c":
            ser.write(b'C')

        if harf1=="d":
            ser.write(b'D')

        if harf1=="e":
            ser.write(b'e')
            
        if harf1=="f":
            ser.write(b'F')

        if harf1=="g":
            ser.write(b'G')

        if harf1=="h":
            ser.write(b'H')

        if harf1=="ı":
            ser.write(b'I')

        if harf1=="j":
            ser.write(b'J')

        if harf1=="k":
            ser.write(b'K')

        if harf1=="l":
            ser.write(b'L')

        if harf1=="m":
            ser.write(b'M')

        if harf1=="n":
            ser.write(b'N')

        if harf1=="o":
            ser.write(b'O')
        if harf1=="p":
            ser.write(b'P')

        if harf1=="r":
            ser.write(b'R')

        if harf1=="s":
            ser.write(b'S')

        if harf1=="u":
            ser.write(b'u')

        if harf1=="v":
            ser.write(b'V')

        if harf1=="x":
            ser.write(b'X')

        if harf1=="y":
            ser.write(b'Y')

        if harf1=="z":
            ser.write(b'Z')

        if harf1=="q":
            ser.write(b'Q')

        if harf1=="t":
            ser.write(b'T')

        if harf1=="w":
            ser.write(b'W')


    print(i)
    if i==3:
            break

        
    m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
    k=0
    for j in range(0,25): #bir harfin saniyesi
    
        print (GPIO.input(27))
        time.sleep(1)
        if GPIO.input(27)==1:
            a=0 #karanlık
        if GPIO.input(27)==0:
                
            a=a+1#ışık
            #print(a)
            if 3>a>0:
                durum="nokta"
                k=k+1
                m[k]="nokta"
                print(durum)
                nokta=nokta+1
            if 5>a>2:
                durum="çizgi"
                k=k+1
                m[k]="çizgi"
                print(durum)
                cizgi=cizgi+1

            if 7>a>4:
                durum="karakter"
                k=k+1
                m[k]="karakter"
                print(durum)
                
                

            if 8>a>6:
                durum="sil"
                k=k+1
                m[k]="sil"
                print(durum)
                i=i-1
                print(i)
        
    ab=0
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi"and m[4]=="çizgi" and m[5]=="karakter" and m[6]=="karakter" and m[7]=="sil" and m[8]=="":
        harf=" "
        
        kelime[hh]=" "
        print(harf)
        hh=hh-1
        m=["","","","","","","","","","","","","","",""]
        ab=1


    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta"and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi"and m[8]=="çizgi" and m[9]=="karakter" and m[10]=="":
        harf="a"
        hh=hh+1
        kelime[hh]="a"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="karakter" and m[12]=="":
        harf="b"
        hh=hh+1
        kelime[hh]="b"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="nokta" and m[11]=="çizgi"and m[12]=="çizgi" and m[13]=="karakter" and m[14]=="":
        harf="c"
        hh=hh+1
        kelime[hh]="c"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="çizgi"and m[9]=="çizgi" and m[10]=="karakter" and m[10]=="":
        harf="d"
        hh=hh+1
        kelime[hh]="d"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi"and m[5]=="çizgi" and m[6]=="karakter" and m[7]=="":
        harf="e"
        hh=hh+1
        kelime[hh]="e"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        k=0
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="nokta"  and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="karakter" and m[12]=="":
        harf="f"
        hh=hh+1
        kelime[hh]="f"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi"and m[11]=="çizgi" and m[12]=="karakter" and m[13]=="":
        harf="g"
        hh=hh+1
        kelime[hh]="g"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta"  and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi"and m[8]=="çizgi" and m[9]=="karakter" and m[10]=="":
        harf="h"
        hh=hh+1
        kelime[hh]="h"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta"  and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi"and m[6]=="çizgi" and m[7]=="karakter" and m[8]=="":
        harf="ı"
        hh=hh+1
        kelime[hh]="ı"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi"and m[14]=="çizgi" and m[15]=="karakter" and m[16]=="":
        harf="j"
        hh=hh+1
        kelime[hh]="j"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi"and m[11]=="çizgi" and m[12]=="karakter" and m[13]=="":
        harf="k"
        hh=hh+1
        kelime[hh]="k"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="karakter" and m[12]=="":
        harf="l"
        hh=hh+1
        kelime[hh]="l"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="karakter" and m[12]=="":
        harf="m"
        hh=hh+1
        kelime[hh]="m"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi"and m[8]=="çizgi" and m[9]=="karakter" and m[10]=="":
        harf="n"
        hh=hh+1
        kelime[hh]="n"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi" and m[10]==""and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi" and m[14]=="çizgi" and m[15]=="karakter" and m[16]=="":
        harf="o"
        hh=hh+1
        kelime[hh]="o"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="nokta" and m[11]=="çizgi"and m[12]=="çizgi" and m[13]=="karakter" and m[14]=="":
        harf="p"
        hh=hh+1
        kelime[hh]="p"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi" and m[14]=="çizgi" and m[15]=="karakter" and m[16]=="":
        harf="q"
        hh=hh+1
        kelime[hh]="q"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta"  and m[6]=="nokta" and m[7]=="nokta" and m[8]=="çizgi"and m[9]=="çizgi" and m[10]=="karakter" and m[11]=="":
        harf="r"
        hh=hh+1
        kelime[hh]="r"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi"and m[7]=="çizgi" and m[8]=="karakter" and m[9]=="":
        harf="s"
        hh=hh+1
        kelime[hh]="s"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi"and m[7]=="çizgi" and m[8]=="karakter" and m[9]=="":
        harf="t"
        hh=hh+1
        kelime[hh]="t"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="çizgi"and m[9]=="çizgi" and m[10]=="karakter" and m[11]=="":
        harf="u"
        hh=hh+1
        kelime[hh]="u"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="karakter" and m[12]=="":
        harf="v"
        hh=hh+1
        kelime[hh]="v"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi"and m[11]=="çizgi" and m[12]=="karakter" and m[13]=="":
        harf="w"
        hh=hh+1
        kelime[hh]="w"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="çizgi" and m[9]=="nokta" and m[10]=="nokta" and m[11]=="çizgi"and m[12]=="çizgi" and m[13]=="karakter" and m[14]=="":
        harf="x"
        hh=hh+1
        kelime[hh]="x"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi"and m[14]=="çizgi" and m[15]=="karakter" and m[16]=="":
        harf="y"
        hh=hh+1
        kelime[hh]="y"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="nokta" and m[11]=="çizgi"and m[12]=="çizgi" and m[13]=="karakter" and m[14]=="":
        harf="z"
        hh=hh+1
        kelime[hh]="z"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        i=i+1
        ab=1
        
    print(kelime)       
            ##########################################################





MOTOR.dcSTOP(0,2)
MOTOR.dcSTOP(0,3)
MOTOR.dcCONFIG(0,2,'ccw',40.0,0)
MOTOR.dcCONFIG(0,3,'ccw',40.0,0)
MOTOR.dcSTART(0,2) 
MOTOR.dcSTART(0,3)
time.sleep(1)
MOTOR.dcSTOP(0,2)
MOTOR.dcSTOP(0,3)
MOTOR.dcCONFIG(0,2,'cw',40.0,0)
MOTOR.dcCONFIG(0,3,'cw',40.0,0)
bheading=bheading+70
#distance=ULTRASONIC_DISTANCE()
heading=GYRO_HEADING()
nheading=heading
print("b",bheading)
print("n",nheading)
while True:
        if bheading >nheading:
                heading=GYRO_HEADING()
                nheading=heading
                print("n",nheading)
                MOTOR.dcSTOP(0,2)
                MOTOR.dcSTOP(0,3)
                MOTOR.dcCONFIG(0,2,'ccw',35.0,0)
                MOTOR.dcCONFIG(0,3,'cw',50.0,0)
                MOTOR.dcSTART(0,2) 
                MOTOR.dcSTART(0,3)
                heading=GYRO_HEADING()
                nheading=heading
                print("b",bheading)
                print("n",nheading)
                if nheading>bheading:
                        heading=GYRO_HEADING()
                        nheading=heading
                       # print("b",bheading)
                        print("n",nheading)

                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)
                        MOTOR.dcCONFIG(0,2,'cw',60.0,0)
                        MOTOR.dcCONFIG(0,3,'cw',40.0,0)
                        MOTOR.dcSTART(0,2) 
                        MOTOR.dcSTART(0,3)
                        time.sleep(5)
                        MOTOR.dcSTOP(0,2)
                        MOTOR.dcSTOP(0,3)
                        break
                   

    






GPIO.cleanup()
