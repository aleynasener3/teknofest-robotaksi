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
            
