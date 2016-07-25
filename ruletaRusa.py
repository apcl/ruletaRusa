#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import random

while True:
    nuez = int (input ('tamaño de la nuez: ')) - 1
    balas = int (input ('balas en la nuez: ')) - 1
    count = 0
    scount = 0
    tcount = 0
    vect = []
    while count <= nuez:
        vect.append (0)
        count = count + 1
    while scount <= balas:
        rv = random.randrange (0,nuez,1)
        if (vect [rv] != 1):
            vect [rv] = 1
        else:
            continue
        scount = scount +1
    
    while tcount <= nuez:
        yes = str(input ('desea disparar?(y o n)'))
        if (yes == 'y'):
            if (vect [tcount] == 1):
                print ('Perdiste!')
            else:
                print ('Te salvaste...')
        elif (yes == 'n'):
            print ('pussy...')
            break
        else:
            print ('WTF!!')
        tcount = tcount + 1
    print ('Asi estaba la nuez ' + str (vect))
    print ('VAMOS, NUEVAMENTE!')
