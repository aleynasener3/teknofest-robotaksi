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
        MOTOR.dcCONFIG(0,2,'ccw',45.0,0)
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

if heading_start > 180:
        arac_nerede = 'sağda'
else:
        arac_nerede = 'solda'

print("araç nerede ? ", arac_nerede)
        
#################################
#    1  sağ              2  sol #
#########              ########## 
#    3                   4      #
#########              ##########
#    5                   6      #
##############   ################
            #     #
          #          #




if arac_nerede == 'sağda':
        #araç sağda ve 1 nolu park yerinde
        arac_boyu = 26
        hat1 = 135 #!!!
        heading_reference = GYRO_HEADING()
        MOTOR_run(hat1 - arac_boyu)
        heading=GYRO_HEADING()
        derece=270
        ROTATE(heading,derece)
        while True:
                camera.capture('gorsel1.jpg')
                COLOR_MATCH()
                template = cv2.imread('aTDIK.png',0)
                max_val1=float(TEMP_MATCH(template))
                print("max val", max_val1)
                durum = KARAR(max_val1)
                print(durum)
                if durum == 'duz':
                        mesafe = 2
                        MOTOR_SET_UP()
                        MOTOR_run(mesafe)
                else:                           #kavsak
                        break
        mesafe = 46
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        heading=GYRO_HEADING()
        print("heading ", heading)
        print('kavsak bulundu')

        mesafe = 50 #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        mesafe = 50 #!!!        
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()  
        ROTATE(heading,derece)
        mesafe = 50  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        print("Here is ORIGIN")

if arac_nerede == 'solda':
        #araç solda ve 4 nolu park yerinde
        arac_boyu = 26
        hat1 = 135 #!!!
        heading_reference = GYRO_HEADING()
        MOTOR_run(hat1 - arac_boyu)
        heading=GYRO_HEADING()
        derece=90
        ROTATE(heading,derece)
        while True:
                camera.capture('gorsel1.jpg')
                COLOR_MATCH()
                template = cv2.imread('aTDIK.png',0)
                max_val1=float(TEMP_MATCH(template))
                print("max val", max_val1)
                durum = KARAR(max_val1)
                print(durum)
                if durum == 'duz':
                        mesafe = 2
                        MOTOR_SET_UP()
                        MOTOR_run(mesafe)
                else:                           #kavsak
                        break
        mesafe = 46
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        heading=GYRO_HEADING()
        print("heading ", heading)
        print('kavsak bulundu')

        mesafe = 30 #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        mesafe = 30 #!!!        
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()  
        ROTATE(heading,derece)
        mesafe = 30  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        print("Here is ORIGIN")


# PATİKA

## 2 ##
mesafe2 = 260 #cm
derece2 = 30    #derece

adim = 50
adim_sayisi_float = mesafe2 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe2 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece2
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 3 ##
mesafe3 = 290  #cm
derece3 = 30    #derece

adim = 50
adim_sayisi_float = mesafe3 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe3 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece3
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
## 4 ##
mesafe4 = 329  #cm
derece4 = 22    #derece

adim = 50
adim_sayisi_float = mesafe4 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe4 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece4
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
## 5 ##
mesafe5 = 263  #cm
derece5 = 25    #derece

adim = 50
adim_sayisi_float = mesafe5 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe5 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece5
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
## 6 ##
mesafe6 = 509  #cm
derece6 = 18    #derece

adim = 50
adim_sayisi_float = mesafe6 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe6 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece6
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 7 ##
mesafe7 = 261  #cm
derece7 = 20   #derece

adim = 50
adim_sayisi_float = mesafe7 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe7 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece7
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


## 8 ##
mesafe8 = 518  #cm
derece8 = 16    #derece

adim = 50
adim_sayisi_float = mesafe8 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe8 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece8
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 9 ##
mesafe9 = 320  #cm
derece9 = 16    #derece

adim = 50
adim_sayisi_float = mesafe9 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe9 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece9
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 103 ##
mesafe103 = 545  #cm
derece103 = 279    #derece

adim = 50
adim_sayisi_float = mesafe103 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe103 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece103
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 104 ##
mesafe104 = 150  #cm
derece104 = 249    #derece

adim = 50
adim_sayisi_float = mesafe104 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe104 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece104
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


## 105 ##
mesafe105 = 149  #cm
derece105 = 246    #derece

adim = 50
adim_sayisi_float = mesafe105 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe105 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece105
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################


## 106 ##
mesafe106 = 199  #cm
derece106 = 243    #derece

adim = 50
adim_sayisi_float = mesafe106 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe106 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece106
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################



## 107 ##
mesafe107 = 311  #cm
derece107 = 250    #derece

adim = 50
adim_sayisi_float = mesafe107 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe107 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece107
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 108 ##
mesafe108 = 119  #cm
derece108 = 258    #derece

adim = 50
adim_sayisi_float = mesafe108 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe108 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece108
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 109 ##
mesafe109 = 111  #cm
derece109 = 258    #derece

adim = 50
adim_sayisi_float = mesafe109 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe109 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece109
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 110 ##
mesafe110 = 204  #cm
derece110 = 241    #derece

adim = 50
adim_sayisi_float = mesafe110 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe110 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece110
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 88 ##
mesafe88 = 1132  #cm
derece88 = 223    #derece

adim = 50
adim_sayisi_float = mesafe88 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe88 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece88
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 89 ##
mesafe89 = 345  #cm
derece89 = 134    #derece

adim = 50
adim_sayisi_float = mesafe89 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe89 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece89
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 90 ##
mesafe90 = 508  #cm
derece90 = 133    #derece

adim = 50
adim_sayisi_float = mesafe90 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe90 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece90
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 91 ##
mesafe91 = 200  #cm
derece91 = 127    #derece

adim = 50
adim_sayisi_float = mesafe91 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe91 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece91
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 92 ##
mesafe92 = 353  #cm
derece92 = 131    #derece

adim = 50
adim_sayisi_float = mesafe92 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe92 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece92
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 93 ##
mesafe93 = 217  #cm
derece93 = 134    #derece

adim = 50
adim_sayisi_float = mesafe93 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe93 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece93
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################

## 1 ##
mesafe93 = 388  #cm
derece93 = 134    #derece

adim = 50
adim_sayisi_float = mesafe93 / adim
adim_sayisi = int(adim_sayisi_float)
kalan_mesafe = mesafe93 - adim_sayisi*adim
for i in range(0, adim_sayisi):
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=derece93
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
MOTOR_SET_UP()
MOTOR_run(kalan_mesafe)

################
# PARK ETME
################


if arac_nerede == 'sağda':
        #araç sağdaki  1 nolu park yerine park edecek
        heading=GYRO_HEADING()
        derece=180
        ROTATE(heading,derece)
        mesafe = 50 #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        mesafe = 50 #!!!        
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()  
        ROTATE(heading,derece)
        mesafe = 50  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)

        heading=GYRO_HEADING()
        derece=90
        ROTATE(heading,derece)

        mesafe = 135  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)

        
if arac_nerede == 'solda':
        #araç soldaki  4 nolu park yerine park edecek
        heading=GYRO_HEADING()
        derece=180
        ROTATE(heading,derece)
        mesafe = 30 #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()
        ROTATE(heading,derece)
        mesafe = 30 #!!!        
        MOTOR_SET_UP()
        MOTOR_run(mesafe)
        derece=0
        heading=GYRO_HEADING()  
        ROTATE(heading,derece)
        mesafe = 30  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)

        heading=GYRO_HEADING()
        derece=270
        ROTATE(heading,derece)

        mesafe = 135  #!!!
        MOTOR_SET_UP()
        MOTOR_run(mesafe)



GPIO.cleanup()
