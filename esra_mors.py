import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
a=0
durum=100
cizgi=0
k=0
m=["","","","","","","","","","","","","","",""]
kelime=["","","",""]
harf=0
hh=0
i=3
while GPIO.input(27)==1:
    print("karanlık")
for x in range(0,i):#harf sayısı - üç olmalı
    m=["","","","","","","","","","","","","","",""]
    k=0
    for i in range(0,5): #bir harfin saniyesi
    
        print (GPIO.input(27))
        time.sleep(1)
        if GPIO.input(27)==1:
            a=0 #karanlık
        if GPIO.input(27)==0:
            a=a+1#ışık
            #print(a)
            if 3>a>0:
                m[k]="0"
                k=k+1
        
            if 5>a>2:
                m[k]="1"
                k=k+1
            if 8>a>6:
                m[k]="3"
                k=k+1
                
#print(m)
    if m[1]=="0" and m[2]=="0" and m[3]=="0"and m[4]=="1" and m[5]=="":
        harf="a"
        hh=hh+1
        kelime[hh]="a"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="0" and m[7]=="":
        harf="b"
        hh=hh+1
        kelime[hh]="b"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="0" and m[9]=="":
        harf="c"
        hh=hh+1
        kelime[hh]="c"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="":
        harf="d"
        hh=hh+1
        kelime[hh]="d"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="":
        harf="e"
        hh=hh+1
        kelime[hh]="e"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        k=0

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="0" and m[5]=="1" and m[6]=="0"  and m[7]=="":
        harf="f"
        hh=hh+1
        kelime[hh]="f"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="0" and m[8]=="":
        harf="g"
        hh=hh+1
        kelime[hh]="g"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
    
    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="0"  and m[5]=="":
        harf="h"
        hh=hh+1
        kelime[hh]="h"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0"  and m[3]=="":
        harf="ı"
        hh=hh+1
        kelime[hh]="ı"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="1" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="0" and m[9]=="0" and m[10]=="1" and m[11]=="":
        harf="j"
        hh=hh+1
        kelime[hh]="j"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="":
        harf="k"
        hh=hh+1
        kelime[hh]="k"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="1" and m[5]=="0" and m[6]=="0" and m[7]=="":
        harf="l"
        hh=hh+1
        kelime[hh]="l"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="":
        harf="m"
        hh=hh+1
        kelime[hh]="m"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="":
        harf="n"
        hh=hh+1
        kelime[hh]="n"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="0" and m[8]=="0" and m[9]=="1" and m[10]=="":
        harf="o"
        hh=hh+1
        kelime[hh]="o"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="1" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="0" and m[9]=="":
        harf="p"
        hh=hh+1
        kelime[hh]="p"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    
    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="0" and m[8]=="0" and m[9]=="0" and m[10]=="1" and m[11]=="" :
        harf="q"
        hh=hh+1
        kelime[hh]="q"
        print(harf)
        m=["","","","","","","","","","","","","","",""]


    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="1" and m[5]=="0"  and m[6]=="":
        harf="r"
        hh=hh+1
        kelime[hh]="r"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="":
        harf="s"
        hh=hh+1
        kelime[hh]="s"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="":
        harf="t"
        hh=hh+1
        kelime[hh]="t"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="0" and m[5]=="1" and m[6]=="" :
        harf="u"
        hh=hh+1
        kelime[hh]="u"
        print(harf)
        m=["","","","","","","","","","","","","","",""]


    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="":
        harf="v"
        hh=hh+1
        kelime[hh]="v"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="0" and m[4]=="1" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="":
        harf="w"
        hh=hh+1
        kelime[hh]="w"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="0" and m[7]=="0" and m[8]=="" :
        harf="x"
        hh=hh+1
        kelime[hh]="x"
        print(harf)
        m=["","","","","","","","","","","","","","",""]
        

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="0" and m[7]=="1" and m[8]=="0" and m[9]=="0" and m[10]=="1" and m[11]=="" :
        harf="y"
        hh=hh+1
        kelime[hh]="y"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    if m[1]=="0" and m[2]=="0" and m[3]=="1" and m[4]=="0" and m[5]=="0" and m[6]=="1" and m[7]=="0" and m[8]=="0" and m[8]=="":
        harf="z"
        hh=hh+1
        kelime[hh]="z"
        print(harf)
        m=["","","","","","","","","","","","","","",""]

    print(kelime)        
            
        
