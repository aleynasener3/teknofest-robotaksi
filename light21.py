import RPi.GPIO as GPIO
import time
import serial
ser = serial.Serial('/dev/ttyACM0',baudrate=9600, timeout=3.0)

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
i=3
for x in range(0,i):#harf sayısı - üç olmalı
    print(i)
    m=["","","","","","","","","","","","","","",""]
    k=0
    for j in range(0,10): #bir harfin saniyesi
    
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
                durum="sil"
                k=k+1
                m[k]="sil"
                print(durum)
                i=i+1
                print(i)
                
        
#print(m)
   
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi"and m[4]=="çizgi" and m[5]=="sil" and m[6]=="":
        harf=" "
        
        kelime[hh]=" "
        print(harf)
        hh=hh-1
        m=["","","","","","","","","","","","","","",""]



    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta"and m[4]=="çizgi" and m[5]=="":
        harf="a"
        hh=hh+1
        kelime[hh]="a"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="":
        harf="b"
        hh=hh+1
        kelime[hh]="b"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="":
        harf="c"
        hh=hh+1
        kelime[hh]="c"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="":
        harf="d"
        hh=hh+1
        kelime[hh]="d"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="":
        harf="e"
        hh=hh+1
        kelime[hh]="e"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        k=0
        print(i)
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="nokta"  and m[7]=="":
        harf="f"
        hh=hh+1
        kelime[hh]="f"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="":
        harf="g"
        hh=hh+1
        kelime[hh]="g"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
    
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta"  and m[5]=="":
        harf="h"
        hh=hh+1
        kelime[hh]="h"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta"  and m[3]=="":
        harf="ı"
        hh=hh+1
        kelime[hh]="ı"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="":
        harf="j"
        hh=hh+1
        kelime[hh]="j"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="":
        harf="k"
        hh=hh+1
        kelime[hh]="k"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="":
        harf="l"
        hh=hh+1
        kelime[hh]="l"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="":
        harf="m"
        hh=hh+1
        kelime[hh]="m"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="":
        harf="n"
        hh=hh+1
        kelime[hh]="n"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi" and m[10]=="":
        harf="o"
        hh=hh+1
        kelime[hh]="o"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="":
        harf="p"
        hh=hh+1
        kelime[hh]="p"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="" :
        harf="q"
        hh=hh+1
        kelime[hh]="q"
        print(harf)
        m=["","","","","","","","","","","","","","",""]


    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta"  and m[6]=="":
        harf="r"
        hh=hh+1
        kelime[hh]="r"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="":
        harf="s"
        hh=hh+1
        kelime[hh]="s"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="":
        harf="t"
        hh=hh+1
        kelime[hh]="t"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="" :
        harf="u"
        hh=hh+1
        kelime[hh]="u"
        print(harf)
        m=["","","","","","","","","","","","","","",""]


    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="":
        harf="v"
        hh=hh+1
        kelime[hh]="v"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="":
        harf="w"
        hh=hh+1
        kelime[hh]="w"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="" :
        harf="x"
        hh=hh+1
        kelime[hh]="x"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="" :
        harf="y"
        hh=hh+1
        kelime[hh]="y"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[8]=="":
        harf="z"
        hh=hh+1
        kelime[hh]="z"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    print(kelime)        
            
harf1=kelime[1]
harf2=kelime[2]
harf3=kelime[3]
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


#############################

if harf2=="a":
    ser.write(b'A')

if harf2=="b":
    ser.write(b'B')

if harf2=="c":
    ser.write(b'C')

if harf2=="d":
    ser.write(b'D')

if harf2=="e":
    ser.write(b'e')
if harf2=="f":
    ser.write(b'F')

if harf2=="g":
    ser.write(b'G')

if harf2=="h":
    ser.write(b'H')

if harf2=="ı":
    ser.write(b'I')

if harf2=="j":
    ser.write(b'J')

if harf2=="k":
    ser.write(b'K')

if harf2=="l":
    ser.write(b'L')

if harf2=="m":
    ser.write(b'M')

if harf2=="n":
    ser.write(b'N')

if harf2=="o":
    ser.write(b'O')
if harf2=="p":
    ser.write(b'P')

if harf2=="r":
    ser.write(b'R')

if harf2=="s":
    ser.write(b'S')

if harf2=="u":
    ser.write(b'u')

if harf2=="v":
    ser.write(b'V')

if harf2=="x":
    ser.write(b'X')

if harf2=="y":
    ser.write(b'Y')

if harf2=="z":
    ser.write(b'Z')

if harf2=="q":
    ser.write(b'Q')

if harf2=="t":
    ser.write(b'T')

if harf2=="w":
    ser.write(b'W')

###############################


if harf3=="a":
    ser.write(b'A')

if harf3=="b":
    ser.write(b'B')

if harf3=="c":
    ser.write(b'C')

if harf3=="d":
    ser.write(b'D')

if harf3=="e":
    ser.write(b'e')
if harf3=="f":
    ser.write(b'F')

if harf3=="g":
    ser.write(b'G')

if harf3=="h":
    ser.write(b'H')

if harf3=="ı":
    ser.write(b'I')

if harf3=="j":
    ser.write(b'J')

if harf3=="k":
    ser.write(b'K')

if harf3=="l":
    ser.write(b'L')

if harf3=="m":
    ser.write(b'M')

if harf3=="n":
    ser.write(b'N')

if harf3=="o":
    ser.write(b'O')
if harf3=="p":
    ser.write(b'P')

if harf3=="r":
    ser.write(b'R')

if harf3=="s":
    ser.write(b'S')

if harf3=="u":
    ser.write(b'U')

if harf3=="v":
    ser.write(b'V')

if harf3=="x":
    ser.write(b'X')

if harf3=="y":
    ser.write(b'Y')

if harf3=="z":
    ser.write(b'Z')

if harf3=="q":
    ser.write(b'Q')

if harf3=="t":
    ser.write(b'T')

if harf3=="w":
    ser.write(b'W')
