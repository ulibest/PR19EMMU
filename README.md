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

### Najpopularnejša znamka vozila v Sloveniji ###

```python
znamka = dict()
for row in dict_reader:
    if row["D.1-Znamka"] in znamka:
        znamka[row["D.1-Znamka"]] += 1
    else:
        znamka[row["D.1-Znamka"]] = 0

z = sorted(znamka, key=znamka.get, reverse=True)[:20]
zx, zy = list(), list()
for a in z:
    zx.append(a)
    zy.append(znamka[a])
zx = zx[::-1]
zy = zy[::-1]
y_pos = np.arange(len(zx))

plt.barh(y_pos, zy, align='center', color='yrmgb')
plt.yticks(y_pos, zx)
plt.title('Najpopolarnejše znamke vozil v Sloveniji')
plt.rc('ytick', labelsize=20)
plt.tick_params(axis='y', which='major', labelsize=8)
plt.show()
```

![Znamke](PR19EMMU/Slike/najpop_znamka.png)

### Spol voznikov ###

```python
razmerje = [0,0]   #index 0 je za moske index 1 za zenske
ime_stolpca = "C-Spol uporabnika (ce gre za fizicno osebo)"

for row in dict_reader:
    if row[ime_stolpca] == "M":
        razmerje[0] += 1
    elif row[ime_stolpca] == "Z":
        razmerje[1] += 1

labels = 'Moški', 'Ženske'
colors = ['blue', 'yellow']
explode = (0.1, 0)

plt.pie(razmerje, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
```
![SpolVoznikov](images/spolvoznikov.png)

### Okoljevarstvena oznaka ###
```python
oznake = dict()
s = 0
mozne = ["EURO 0", "EURO 1", "EURO 2", "EURO 3", "EURO 4", "EURO 5", "EURO 6"]
for m in mozne:
    oznake[m] = 0
for row in dict_reader:
    if row[name] in mozne:
        s += 1
        oznake[row[name]] += 1

data = []
for m in mozne:
    data.append(oznake[m])

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', "red", "blue", "green"]

patches, texts = plt.pie(data, colors=colors, startangle=140)

all = sum([i for i in oznake.values()])
labels = []

for key in oznake.keys():
    s = str(round(((oznake[key] / all) * 100), 1))
    st = key + " (" + s + " %)"
    labels.append(st)

plt.title('Porazdelitev okoljevarstvenih oznak')
plt.legend(patches, labels, loc="best")

plt.axis('equal')
plt.show()
```
![okoljevarstvenaOznaka](images/oznaka.png)

### Države proizvodnje ###
```python

```
![drzava](images/drzave.png)





