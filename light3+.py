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

while True:#harf sayısı - üç olmalı

    print(i)
    if i==3:
            break

        
    m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
    k=0
    for j in range(0,20): #bir harfin saniyesi
    
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
                
                print("i",i)

            if 9>a>6:
                durum="karakter"
                k=k+1
                m[k]="karakter"
                print(durum)
                i=i-1
                print("i",i)

            
#print(m)
   
   


    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="çizgi" and m[9]=="sil" and m[10]=="sil" and m[11]=="karakter" and m[12]==" ":
        harf="a"
        hh=hh+1
        kelime[hh]="a"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="nokta"and m[9]=="çizgi" and m[10]=="çizgi" and m[11]=="sil"and m[12]=="sil" and m[13]=="karakter" and m[14]==" ":
        harf="b"
        hh=hh+1
        kelime[hh]="b"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="nokta"and m[11]=="çizgi" and m[12]=="çizgi" and m[13]=="sil"and m[14]=="sil" and m[15]=="karakter" and m[16]==" ":
        harf="c"
        hh=hh+1
        kelime[hh]="c"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta"and m[8]=="çizgi" and m[9]=="çizgi" and m[10]=="sil"and m[11]=="sil" and m[12]=="karakter" and m[13]==" ":
        harf="d"
        hh=hh+1
        kelime[hh]="d"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta"and m[4]=="çizgi" and m[5]=="çizgi" and m[6]=="sil"and m[7]=="sil" and m[8]=="karakter" and m[9]==" ":
        harf="e"
        hh=hh+1
        kelime[hh]="e"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        k=0
        print(i)
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="nokta"  and m[7]=="nokta" and m[8]=="nokta"and m[9]=="çizgi" and m[10]=="çizgi" and m[11]=="sil"and m[12]=="sil" and m[13]=="karakter" and m[14]==" ":
        harf="f"
        hh=hh+1
        kelime[hh]="f"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
    
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta"and m[10]=="çizgi" and m[11]=="çizgi" and m[12]=="sil"and m[13]=="sil" and m[14]=="karakter" and m[15]==" ":
        harf="g"
        hh=hh+1
        kelime[hh]="g"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta"  and m[5]=="nokta" and m[6]=="nokta"and m[7]=="çizgi" and m[8]=="çizgi" and m[9]=="sil"and m[10]=="sil" and m[11]=="karakter" and m[1]==" ":
        harf="h"
        hh=hh+1
        kelime[hh]="h"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="çizgi" and m[7]=="sil" and m[8]=="sil" and m[9]=="karakter" and m[10]==" " :
        harf="ı"
        hh=hh+1
        kelime[hh]="ı"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi" and m[14]=="çizgi" and m[15]=="sil"and m[16]=="sil" and m[17]=="karakter" and m[18]==" ":
        harf="j"
        hh=hh+1
        kelime[hh]="j"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta"and m[10]=="çizgi" and m[11]=="çizgi" and m[12]=="sil"and m[13]=="sil" and m[14]=="karakter" and m[15]==" ":
        harf="k"
        hh=hh+1
        kelime[hh]="k"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="sil" and m[12]=="sil"and m[13]=="karakter" and m[14]==" ":
        harf="l"
        hh=hh+1
        kelime[hh]="l"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="sil" and m[12]=="sil"and m[13]=="karakter" and m[14]==" " :
        harf="m"
        hh=hh+1
        kelime[hh]="m"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta"and m[7]=="çizgi" and m[8]=="çizgi" and m[9]=="sil"and m[10]=="sil" and m[11]=="karakter" and m[12]==" ":
        harf="n"
        hh=hh+1
        kelime[hh]="n"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi" and m[10]=="nokta" and m[11]=="nokta"and m[12]=="çizgi" and m[13]=="çizgi" and m[14]=="sil"and m[15]=="sil" and m[16]=="karakter" and m[17]==" ":
        harf="o"
        hh=hh+1
        kelime[hh]="o"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="nokta"and m[11]=="çizgi" and m[12]=="çizgi" and m[13]=="sil"and m[14]=="sil" and m[15]=="karakter" and m[16]==" ":
        harf="p"
        hh=hh+1
        kelime[hh]="p"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
    
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi" and m[14]=="çizgi" and m[15]=="sil"and m[16]=="sil" and m[17]=="karakter" and m[18]==" ": 
        harf="q"
        hh=hh+1
        kelime[hh]="q"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta"  and m[6]=="nokta" and m[7]=="nokta"and m[8]=="çizgi" and m[9]=="çizgi" and m[10]=="sil"and m[11]=="sil" and m[12]=="karakter" and m[13]==" ":
        harf="r"
        hh=hh+1
        kelime[hh]="r"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="nokta"and m[6]=="çizgi" and m[7]=="çizgi" and m[8]=="sil"and m[9]=="sil" and m[10]=="karakter" and m[11]==" ":
        harf="s"
        hh=hh+1
        kelime[hh]="s"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta"and m[6]=="çizgi" and m[7]=="çizgi" and m[8]=="sil"and m[9]=="sil" and m[10]=="karakter" and m[11]==" ":
        harf="t"
        hh=hh+1
        kelime[hh]="t"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="çizgi" and m[6]=="nokta" and m[7]=="nokta"and m[8]=="çizgi" and m[9]=="çizgi" and m[10]=="sil"and m[11]=="sil" and m[12]=="karakter" and m[13]==" ":
        harf="u"
        hh=hh+1
        kelime[hh]="u"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="çizgi"and m[10]=="çizgi" and m[11]=="sil" and m[12]=="sil"and m[13]=="karakter" and m[14]==" " :
        harf="v"
        hh=hh+1
        kelime[hh]="v"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="nokta" and m[4]=="çizgi" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta"and m[10]=="çizgi" and m[11]=="çizgi" and m[12]=="sil"and m[13]=="sil" and m[14]=="karakter" and m[15]==" ":
        harf="w"
        hh=hh+1
        kelime[hh]="w"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="nokta" and m[8]=="nokta" and m[9]=="nokta"and m[10]=="çizgi" and m[11]=="çizgi" and m[12]=="sil"and m[13]=="sil" and m[14]=="karakter" and m[15]==" ":
        harf="x"
        hh=hh+1
        kelime[hh]="x"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="nokta" and m[7]=="çizgi" and m[8]=="nokta" and m[9]=="nokta" and m[10]=="çizgi" and m[11]=="nokta" and m[12]=="nokta" and m[13]=="çizgi" and m[14]=="çizgi" and m[15]=="sil"and m[16]=="sil" and m[17]=="karakter" and m[18]==" ":
        harf="y"
        hh=hh+1
        kelime[hh]="y"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1
        
    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="nokta" and m[5]=="nokta" and m[6]=="çizgi" and m[7]=="nokta" and m[8]=="nokta" and m[8]=="nokta" and m[9]=="nokta"and m[10]=="çizgi" and m[11]=="çizgi" and m[12]=="sil"and m[13]=="sil" and m[14]=="karakter" and m[15]==" ":
        harf="z"
        hh=hh+1
        kelime[hh]="z"
        print(harf)
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
        i=i+1

        

    if m[1]=="nokta" and m[2]=="nokta" and m[3]=="çizgi" and m[4]=="çizgi" and m[5]=="sil" and m[6]=="sil" and m[7]==" " and m[8]==" ":
        harf=" "
        i=i-2 
        kelime[hh]=" "
        print(harf)
        hh=hh-1
      
        m=["","","","","","","","","","","","","","","","","","","","","","","","","",""]
           
    print(kelime)        
            

