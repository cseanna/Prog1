import random

kitevo = random.randint(1,15)
csapatok = list(range(1, (2 ** kitevo) + 1))
print(csapatok)
elso_kor = []
nyertes=0

def elso (csapatok):

    for i in range (len(csapatok)//2):

        meccsek = random.sample(csapatok, k=2)
        csapatok = list(set(csapatok)-set(meccsek))
        elso_kor.append(meccsek)

    tobbi_kor(elso_kor)

def tobbi_kor(elso_kor):
    global nyertes
    hossz=len(elso_kor)
    if hossz!=1:
        osszlista=[]
        print(elso_kor)
        for i in range (0,hossz,2):
            nyero1=random.choice(elso_kor[i])
            nyero2=random.choice(elso_kor[i+1])
            nyertesek=[nyero1,nyero2]
            osszlista.append(nyertesek)
        print(osszlista)
        if len(osszlista)!=1:
            tobbi_kor(osszlista)
        else:

             nyertes = random.choice(osszlista[0])

    else:

        nyertes = random.choice(elso_kor[0])

elso(csapatok)
print(nyertes)
