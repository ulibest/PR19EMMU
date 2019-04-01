# Podatkovno rudarjenje: #
## Vmesno poročilo o opravljenem delu ##

### Avtorji: ###
* Erazem Bršar ()
* Marjan Mohar ()
* Miha Petrišič (63170400)
* Urban Lipovž ()

## Množica podatkov ##
Množica podatkov katere bomo analizirali je zbrana in dostopna na spletnem naslovu:
https://podatki.gov.si/dataset/evidenca-registriranih-vozil-presek-stanja?fbclid=IwAR3tk-7tfb6D0-MFjl5d2yLmr50A359rMPq5nalTZSxpR3ToOh-O3R-TV0g

Objavljena je bila s strani ministrstva za infrastrukturo in vključuje evidence registriranih vozil po letih
v Sloveniji. Množica vsebuje različne podatke o samem vozilu (karakteristike, izvor, naziv ipd.) ter tudi
atribute o samem uporabniku vozila.

Zastavili smo si cilj prikazati podatke na čim bolj preprost ter pregleden način za tiste, ki se zanimajo
za takšno statistiko. Namen je prikazat kakšna vozila vozijo Slovenci ter spreminjanje nekaterih navad
kupovanja vozil skozi čas (npr. ali skozi čas narašča priljubljenost bolj okoljevarstvenih vozil ipd.).
Statistiko bomo poskušali prikazati s pomočjo različnih vizualizacijskih tehnik.  Poleg že obstoječih
običajnih tehnik, bomo poskušali uporabiti tudi nekatere nove (npr. 'heatmap' Slovenije glede na nek
atribut).

## Atributi ##
Nekateri zanimivi atributi, ki jih nameravamo prikazati so:
- Starost in spol voznikov
- Občine uporabnikov vozila
- Starost in država izvora vozila
- Vrsta goriva
- Izpust CO2 ter drugih emisij ter okoljevarstvena oznaka vozil
- Kategorija in vrsta vozila

Poskušali bomo prikazati samo statistiko posameznih atributov in korelacije med določenimi atributi.

## Branje podatkov ##
Naši podatki se nahajajo v .csv datoteki. Ker nekaterih atributov ne bomo potrebovali smo najprej
preoblikovali datoteko tako, da smo se znebili odvečnih stolpcev/atributov.

Koda za branje datoteke:
```python
dict_reader = DictReader(open('podatki2CUT1.csv', "r", encoding="ISO-8859-2"), skipinitialspace=True, delimiter=";")
```
Datoteko beremo s pomočjo razreda DictReader iz knjižnice csv. Parametri podani za najučinkovitejšo branje datoteke so:
* naslov same datoteke oz. pot do nje
* parameter "r" nam pove, da želimo datoteko prebrati
* encoding="ISO-8859-2" parameter omogoče branje večine znakov v naši datoteki
* skipinitialspace=True ignorira beli prostor po razdelilnem znaku
* delimiter=";" pa določa razdelilni znak
 
## Vizualizacija podatkov ##

