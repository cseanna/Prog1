import random

mego = open('megoldas.txt','w+')

kitevo = random.randint(2,5)
csapatok = list(range(1, (2 ** kitevo) + 1))                                   #csapatok szama

elso_kor = []                                                                  #
nyertes=0                                                                      #globalis valtozok inicializalasa
kiirando=''                                                                    #

def elso (csapatok):
    global kiirando
    global kitevo
    elsosor=''

    for i in range (len(csapatok)//2):                                        #elso kor felosztasa

        meccsek = random.sample(csapatok, k=2)
        csapatok = list(set(csapatok)-set(meccsek))
        elso_kor.append(meccsek)
        elsosor+='  |{0:^4} {1:^4}|  '.format(meccsek[0],meccsek[1])          #bracket formazas

    print('\n{0:^{x}}\n'.format(elsosor,x=240),file=mego)

    tobbi_kor(elso_kor)                                                       #tobbi kor felosztasanak es formazasanak hivasa

    print('\n{0:^{x}}\n'.format(nyertes,x=240),file=mego)                     #nyertes formazasa


def tobbi_kor(elso_kor):
    global nyertes
    global kiirando
    global kitevo

    hossz = len(elso_kor)
    osszlista=[]

    if hossz!=1:

        sztringsor=''
        for i in range (0,hossz,2):                                         #kovetkezo kor felosztasa

            nyero1=random.choice(elso_kor[i])
            nyero2=random.choice(elso_kor[i+1])
            nyertesek=[nyero1,nyero2]
            osszlista.append(nyertesek)
            sztringsor+= '  |{0:^4} {1:^4}|  '.format(nyero1,nyero2)        #bracket formazas

        print('\n{0:^{x}}\n'.format(sztringsor,x=240),file=mego)            #sor formazas + a sor fajlba irasa

        if len(osszlista)!=1:
            tobbi_kor(osszlista)                                            #rekurzio ha tobb mint egy meccs van meg hatra

        else:
            nyertes  = '| {0} |'.format(random.choice(osszlista[0]))       #ha egy meccs van hatra es a versenyzok szama nem ketto

    else:
        nyertes = '| {0} |'.format(random.choice(osszlista[0]))            #ha osszesen ket csapat nevezett


elso(csapatok)                                                             #futtatas teszi lehetove a fajlba irast
mego.close()