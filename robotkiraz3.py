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

#LED Set Up
def LED_SET_UP():
        GPIO.setup(13, GPIO.OUT)        #Green LED
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
#GREEN LED ON
def GREEN_ON():
        GPIO.output(13,GPIO.HIGH)
        return
#GREEN LED OFF
def GREEN_OFF():
        GPIO.output(13,GPIO.LOW)
        return
   
def blink_LEDs():
        RED_ON()
        GREEN_OFF()
        time.sleep(1)
        RED_OFF()
        GREEN_ON()
        time.sleep(1)
        return

#STARTER Set Up
def STARTER_SET_UP():
        GPIO.setup(20, GPIO.IN)
        return
#STARTER Status
def STARTER_STATUS():
        Start_Status = GPIO.input(20)
        print("Start_Status: ", Start_Status)
        if Start_Status==1:
                Start_Stop = 1
        else:
                Start_Stop =0
        return Start_Stop
#MOTOR Set Up
def MOTOR_SET_UP():
        MOTOR.dcCONFIG(0,2,'ccw',40.0,0)
        MOTOR.dcCONFIG(0,3,'cw',40.0,0)
        return

#tachometer set up
def TACHO_SET_UP():
        GPIO.setup(21, GPIO.IN)
        return



def counterPlus(channel):
    global tacho_counter
    if GPIO.input(channel) > 0.5:
        tacho_counter += 1
    else:
        tacho_counter += 0
        
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
        print ( "Olculuyor...")
        time.sleep(2)

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


def TAKE_PHOTO():
        camera = PiCamera()
        camera.resolution = (2592, 1944)
        camera.framerate = 15
        camera.capture('gorsel1.jpg')
        return

#TEMPLATE MATCHİNG
def TEMP_MATCH(template):
    img = cv2.imread('img.jpg',0)
    img2 = img.copy()
    
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF_NORMED']

    for meth in methods:
        
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img,top_left, bottom_right, 255, 2)
        print("min val: ", min_val, "max val: ", max_val)
        print("min loc: ", min_loc, "max loc: ", max_loc)
        print(top_left)
        print(bottom_right)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        #plt.show()
    return max_val

#beyazı belirleme
def COLOR_MATCH():
    image = cv2.imread("gorsel1.jpg")
    boundaries = [([102, 102, 102],[255, 255, 255])] #beyaz

    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
        
        cv2.imwrite("img.jpg",output)
    return output

#karar verme
def KARAR(max_val1):
        if max_val1>0.35:
                durum="kavsak"
        else:
                durum="duz"
        return durum


# Camera Setup
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15

#LED_SET_UP()
STARTER_SET_UP()
MOTOR_SET_UP()
TACHO_SET_UP()
bno = GYRO_SET_UP()
ULTRASONIC_SET_UP()

tacho_counter=0
#tacho interrupt detection
GPIO.add_event_detect(21, GPIO.RISING, callback = counterPlus, bouncetime = 3)

#robot ilk çalıştığında başlangıç noktasına baksın
heading_initial = GYRO_HEADING()
print("heading initial", heading_initial)

# start (+) uzaktan kumanda tuşuna basılana kadar bekle
Start_Stop = 0;
while Start_Stop==0:
        Start_Stop = STARTER_STATUS()
        
heading_start = GYRO_HEADING()
print("heading start ", heading_start)

#robotu ilk ayarladığınız yere göre araç sola yerleştirilirse heading küçük 180 derece
#robotu ilk ayarladığınız yere göre araç sağa yerleştirilirse heading büyük 180 derece

#if heading_start > 180:
  #      arac_nerede = 'sağda'
#else:
   #     arac_nerede = 'solda'

#print("araç nerede ? ", arac_nerede)
        
#################################
#    1  sağ              2  sol #
#########              ########## 
#    3                   4      #
#########              ##########
#    5                   6      #
##############   ################
            #     #
          #          #


# PATİKA


## 1 ##
mesafe1 = 830 #cm
derece1 = 35    #derece

adim = 50
adim_sayisi_float = mesafe1 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe1 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece1
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe1)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
## 2 ##
mesafe2 = 54 #cm
derece2 = 305    #derece

adim = 50
adim_sayisi_float = mesafe2 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe2 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece2
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe2)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 3 ##
mesafe3 = 565 #cm
derece3 = 270    #derece

adim = 50
adim_sayisi_float = mesafe3 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe3 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece3
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe3)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 4 ##
mesafe4 = 200 #cm
derece4 = 180    #derece

adim = 50
adim_sayisi_float = mesafe4 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe4 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece4
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe4)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 5 ##
mesafe5 = 203 #cm
derece5 = 182    #derece

adim = 50
adim_sayisi_float = mesafe5 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe5 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece5
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe5)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


## 6 ##
mesafe6 = 25 #cm
derece6 = 190    #derece

adim = 50
adim_sayisi_float = mesafe6 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe6 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece6
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe6)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 7 ##
mesafe7 = 20 #cm
derece7 = 220    #derece

adim = 50
adim_sayisi_float = mesafe7 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe7 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece7
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe7)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


## 8 ##
mesafe8 = 285 #cm
derece8 = 185    #derece

adim = 50
adim_sayisi_float = mesafe8 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe8 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece8
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe8)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
## 9 ##
mesafe9 = 10 #cm
derece9 = 183    #derece

adim = 50
adim_sayisi_float = mesafe9 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe9 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece9
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe9)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 11 ##
mesafe11 = 10 #cm
derece11 = 180    #derece

adim = 50
adim_sayisi_float = mesafe11 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe11 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece11
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe11)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################



################
# PARK ETME
################

## 10 ##
mesafe10 = 45 #cm
derece10 = 270    #derece

adim = 50
adim_sayisi_float = mesafe10 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe10 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        derece=derece10
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        MOTOR_SET_UP()
        MOTOR_run(mesafe10)
        
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


GPIO.cleanup()
