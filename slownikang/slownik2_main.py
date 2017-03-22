#! /usr/bin/env python

import os.path #modul udostepniajacy funkcje isfile()

print """podaj dane w formacie: wyraz obct: znaczenie1, znaczenie2
    Aby Zakonczyc wprowadzanie danych, podaj 0 """

sFile = "slownik.txt"
slownik = {}

def otworz(plik):
    if os.path.isfile(sFile):
        with open(sFile, "r") as sTxt:
            for line in sTxt:
                t=line.split(":")
                wobcy = t[0]
                znaczenia = t[1].replace("\n","")
                znaczenia = znaczenia.split(",")
                slownik[wobcy] = znaczenia
    return len(slownik)

def zapisz(slownik):
    file1 = open(sFile, "w")
    for wobcy in slownik:
        znaczenia = ",".join(slownik[wobcy])
        linia = ":".join([wobcy,znaczenia])
        print >>file1, linia
    file1.close()

def oczysc(str):
    str = str.strip() #usun poczatkowe, koncowe znaki
    str = str.lower()
    return str

def printSlownik(slownik1):
    print "="*50
    print "{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia")
    print "="*50
    for wobcy in slownik1:
        print "{0: <15}{1: <40}".format(wobcy, ",".join(slownik1[wobcy]))

nowy = False
ileWyrazow = otworz(sFile)
printSlownik(slownik)
print "Wpisow w bazie:", ileWyrazow

while True:
    dane = raw_input("Podaj dane: ")
    t = dane.split(":")
    wobcy = t[0].strip().lower()
    if wobcy == "koniec":
        break
    elif wobcy == "usun":
        usunklucz = raw_input("podaj angielskie slowo do usuniecia")
        nowy = True
        del slownik[usunklucz]
    elif dane.count(":") == 1:
        if wobcy in slownik:
            print "wyraz", wobcy, " i jego znaczenia sa juz w slowniku."
            op = raw_input("zastapic wpis (t/n)? ")
        if wobcy not in slownik or op == "t":
            znaczenia = t[1].split(",")
            znaczenia = map(oczysc, znaczenia)
            slownik[wobcy] = znaczenia
            nowy = True
    else:
        print "bledny format!"

if nowy:
    zapisz(slownik)

printSlownik(slownik)

while True:
    dane = raw_input("wlaczyc tryb nauki? (t/n)?")
    if dane == "n":
        break;
    else:
        for a, b in slownik.items():
            print "podaj tlumaczenie slowa: ", a
            if raw_input() in b:
                print "dobrze"
            else:
                print "zle!"
