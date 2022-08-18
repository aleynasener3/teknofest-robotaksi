
import math
enkucuk=0
xkonum=[0,10,15,0,5,15,0,10]

ykonum=[0,0,10,15,20,20,25,25]

komsusayi=[1,3,3,2,4,4,3,2]

birincikomsu=[2,1,2,2,3,3,5,6]

ilkkomsuuzaklik=[10,10,26.1,18,14,10,7,7]

ilkkomsuaci=[180,180,116.57,56.31,45.4,90,45,45]

ikincikomsu=[9999,3,5,5,4,5,6,7]

ikicikomsuuzaklik=[9999,26.1,14.1,7,7,10,12.2,10]

ikincikomsuaci=[9999,296.27,206.56,314.73,135,180,22.5,180]

ucuncukomsu=[9999,4,6,9999,6,7,8,9999]

ucuncukomsuuzaklik=[9999,18,10,9999,10,12.2,10,9999]

ucuncukomsuaci=[9999,236.31,251.56,9999,360,202.5,360,9999]

dorduncukomsu=[9999,9999,9999,9999,7,8,9999,9999]

dorduncukomsuuzaklik=[9999,9999,9999,9999,7,7,9999,9999]

dorduncukomsuaci=[9999,9999,9999,9999,225,225,9999,9999]

#math.sqrt(((x**2-durakx**2) + (y**2-duraky**2) )      
durakx=int(input("durakx"))
print(durakx-5)
duraky=int(input("duraky"))
durak=[durakx,duraky]

sonuc1=math.sqrt(int((xkonum[0]-durakx)**2+(ykonum[0]-duraky)**2))
sonuc2=math.sqrt(int((xkonum[1]-durakx)**2+(ykonum[1]-duraky)**2))
sonuc3=math.sqrt(int((xkonum[2]-durakx)**2+(ykonum[2]-duraky)**2))
sonuc4=math.sqrt(int((xkonum[3]-durakx)**2+(ykonum[3]-duraky)**2))
sonuc5=math.sqrt(int((xkonum[4]-durakx)**2+(ykonum[4]-duraky)**2))
sonuc6=math.sqrt(int((xkonum[5]-durakx)**2+(ykonum[5]-duraky)**2))
sonuc7=math.sqrt(int((xkonum[6]-durakx)**2+(ykonum[6]-duraky)**2))
sonuc8=math.sqrt(int((xkonum[7]-durakx)**2+(ykonum[7]-duraky)**2))

#print(sonuc1)print(sonuc2)print(sonuc3)print(sonuc4)print(sonuc5)print(sonuc6)print(sonuc7)print(sonuc8)
enkucuk==sonuc1
if sonuc1>sonuc2:
    enkucuk==sonuc2
    if sonuc2>sonuc1:
        enkucuk==sonuc1

if enkucuk>sonuc3:
    enkucuk==sonuc3
    if sonuc3>enkucuk:
        enkucuk==enkucuk

        
if enkucuk>sonuc4:
    enkucuk==sonuc4
    if sonuc4>enkucuk:
        enkucuk==enkucuk

if enkucuk>sonuc5:
    enkucuk==sonuc5
    if sonuc5>enkucuk:
        enkucuk==enkucuk        


if enkucuk>sonuc6:
    enkucuk==sonuc6
    if sonuc6>enkucuk:
        enkucuk==enkucuk        
    
    
if enkucuk>sonuc7:
    enkucuk==sonuc7
    if sonuc7>enkucuk:
        enkucuk==enkucuk
               

if enkucuk>sonuc8:
    enkucuk==sonuc8
    if sonuc8>enkucuk:
        enkucuk==enkucuk    
    
print(enkucuk)









