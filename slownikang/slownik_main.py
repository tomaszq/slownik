import os
slownik = {}

N = 3 #ilosc slow
for a in xrange(N):
    polskie = raw_input("podaj polskie slowo")
    angielskie = raw_input("podaj angielskie slowo")
    slownik[angielskie] = polskie
    
print slownik


with open("slow","w") as plik:
    for k, w in slownik.items():
        linia = k + ":" + w
        plik.write(linia+"\n")
