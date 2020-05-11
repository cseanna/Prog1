def abrazolasMod(n,k,r):
    db=0
    if r<k:
        return 'Az also hatar nem lehet nagyobb, mint a felso.'
    if n>r+k:
        return 'A keresett szam tul nagy a megadott hatarokhoz.'
    for i in range (k,r+1):
        for j in range(k,r+1):
            if i>j:                     #ahogy a kisebb mertekben novekvo szam nagyobb lesz mint a masik 1) duplan kezdenenk el szamolni es 2) megborulna a feladat kikotese, miszerint k<=A<=b<=B<=r
                continue
            if j+i == n:
                db += 1
    return (f'{db%(10**9+7)} db modon alakithatjuk ki a keresett szamot.')


while True:
    try:
        also_hatar = int(input('Add meg az also hatart: '))
        felso_hatar = int(input('Add meg a felso hatart: '))
        szam = int(input('Adj meg egy szamot: '))
        print(abrazolasMod(szam,also_hatar,felso_hatar))
        break
    except ValueError:
        print('Kerlek egesz szamot adj meg!')


