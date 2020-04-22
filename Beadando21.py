import math


def abrazolasMod(n,k,r):
    db=0
    for i in range (k,r+1):
        for j in range(k,r+1):
            if i>j:                     #ahogy a kisebb mertekben novekvo szam nagyobb lesz mint a masik 1) duplan kezdenenk el szamolni es 2) megborulna a feladat kikotese, miszerint k<=A<=b<=B<=r
                continue
            if j+i == n:
                db += 1
    return db

print(abrazolasMod(3,-2,2))