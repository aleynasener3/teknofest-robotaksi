import time                                  
import piplates.MOTORplate as MOTOR
import RPi.GPIO as GPIO 

#MOTOR.dcCONFIG(0,2,'ccw',50.0,2.5)
#MOTOR.dcSTART(0,2) 
#MOTOR.dcCONFIG(0,1,'ccw',50.0,2.5)#
#MOTOR.dcSTART(0,1
#MOTOR.dcSTOP(0,2)
MOTOR.dcCONFIG(0,2,'cw',60.0,2.5)
MOTOR.dcCONFIG(0,3,'ccw',60.0,2.5)

a=0
led ="false"

GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True: # Run forever
    MOTOR.dcSTART(0,2)
    MOTOR.dcSTART(0,3)
    if GPIO.input(21) == GPIO.LOW:
        led="true"

    if GPIO.input(21) == GPIO.HIGH:
        if led=="true":
            a+=1
            print(a)
            led="false"
    if a==35:
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)
        break


