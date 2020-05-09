import numpy as np


def rakovetkezo(vege,ah,fh):
    if ah > fh:
        print('Az also hatar nem lehet nagyobb, mint a felso')
    vektor=np.arange(0,vege)
    for i in range(len(vektor)):
        vektor[i]=np.random.randint(ah,fh+1)

    rakov=0
    if len(vektor)==0 or len(vektor)==1:
        return ' A vektorban nincsenek rakovetkezo elemek.'
    else:
        for i in range (0,len(vektor)):
            for j in range(i+1,len(vektor)):
                if i<j and vektor[i]<vektor[j]:
                    rakov+=1
                if i>=j:
                    break
    return (f'{vektor}\n{rakov} rakovetkezo elem van a vektorban.')

hossz = int(input('Add meg a vektor nagysagat: '))
vah = int(input('Add meg a vektor legkisebb lehetseges erteket: '))
vfh = int(input('Add meg a vektor legnagyobb lehetseges erteket: '))
print(rakovetkezo(hossz,vah,vfh))
