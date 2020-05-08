import random

kitevo = random.randint(2,6)
csapatok = list(range(1, (2 ** kitevo) + 1))

elso_kor = []
nyertes=0

def elso (csapatok):
    elsosor=''
    for i in range (len(csapatok)//2):

        meccsek = random.sample(csapatok, k=2)
        csapatok = list(set(csapatok)-set(meccsek))
        elso_kor.append(meccsek)
        elsosor+='| {0}    {1} |'.format(meccsek[0],meccsek[1])
    tobbi_kor(elso_kor)

    print('{0:^{x}}'.format(nyertes,x=len(csapatok)))


def tobbi_kor(elso_kor):
    global nyertes
    global formazottnyertes
    hossz = len(elso_kor)
    if hossz!=1:
        osszlista=[]
        sztringsor=''
        for i in range (0,hossz,2):
            nyero1=random.choice(elso_kor[i])
            nyero2=random.choice(elso_kor[i+1])
            nyertesek=[nyero1,nyero2]
            osszlista.append(nyertesek)
            sztringsor+= '| {0}    {1} |'.format(nyero1,nyero2)
        print('{0:^{x}}'.format(sztringsor,x=len(csapatok)))

        if len(osszlista)!=1:
            tobbi_kor(osszlista)
        else:
            nyertes  = '| {0} |'.format(random.choice(osszlista[0]))

    else:
        nyertes = '| {0} |'.format(random.choice(osszlista[0]))

elso(csapatok)

