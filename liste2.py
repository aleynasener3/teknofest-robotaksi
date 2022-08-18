import numpy as np

a=0
xkonum=[0,10,15,0,5,15,0,10]

ykonum=[0,0,10,15,20,20,25,25]

komsusayı=[1,3,3,2,4,4,3,2]

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

      
durakx=int(input("durakx"))
print(durakx-5)
duraky=int(input("duraky"))
durak=[durakx,duraky]

while True:
    if xkonum[0] == durakx:
        a+=1
        continue
    else:
        a+=1
    
    if xkonum[1] == durakx:
        a+=1
        continue
    else:
        a+=1
    if xkonum[2] == durakx:
        a+=1
        continue
    else:
        a+=1
    if xkonum[3] == durakx:
        a+=1
        continue
    else:
        a+=1

    if xkonum[4] == durakx:
        a+=1
        continue
    else:
         a+=1
      
    if xkonum[5] == durakx:
        a+=1
        continue
    else:
         a+=1
    if xkonum[6] == durakx:
        a+=1
        continue
    else:
         a+=1
    if xkonum[7] == durakx:
        a+=1
        continue
    else:
         a+=1

print(a)







