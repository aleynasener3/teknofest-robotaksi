import time                                  
import piplates.MOTORplate as MOTOR
import RPi.GPIO as GPIO 
MOTOR.dcCONFIG(0,2,'Cw',80.0,0)
MOTOR.dcCONFIG(0,3,'cw',80.0,0)
MOTOR.dcSTART(0,3) 

time.sleep(2)
MOTOR.dcSTOP(0,3)


MOTOR.dcSTOP(0,2)

5
