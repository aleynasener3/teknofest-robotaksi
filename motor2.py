import piplates.MOTORplate as MOTOR 
import time
MOTOR.dcSTART(0,2)
time.sleep(5.0)
MOTOR.dcSPEED(0,2,100.0)                     
time.sleep(10)
MOTOR.dcSTOP(0,2)
time.sleep(2.5) 

while True:
    durum=input("harf")
    if durum==a:
        MOTOR.dcCONFIG(0,2,'ccw',20.0,2.5)
        MOTOR.dcCONFIG(0,3,'ccw',65.0,2.5)
        MOTOR.dcSTART(0,2)
        MOTOR.dcSTART(0,3)
        time.sleep(0.5)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)

    if durum==w:
        MOTOR.dcCONFIG(0,2,'cw',65.0,2.5)
        MOTOR.dcCONFIG(0,3,'ccw',65.0,2.5)
        MOTOR.dcSTART(0,2)
        MOTOR.dcSTART(0,3)
        time.sleep(0.5)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)

    if durum==d:
        MOTOR.dcCONFIG(0,2,'ccw',65.0,2.5)
        MOTOR.dcCONFIG(0,3,'ccw',20.0,2.5)
        MOTOR.dcSTART(0,2)
        MOTOR.dcSTART(0,3)
        time.sleep(0.5)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)

    if durum==s:
        MOTOR.dcCONFIG(0,2,'ccw',65.0,2.5)
        MOTOR.dcCONFIG(0,3,'cw',65.0,2.5)
        MOTOR.dcSTART(0,2)
        MOTOR.dcSTART(0,3)
        time.sleep(0.5)
        MOTOR.dcSTOP(0,2)
        MOTOR.dcSTOP(0,3)


        
