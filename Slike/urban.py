from csv import DictReader
from warnings import catch_warnings

import numpy as np
import matplotlib.pyplot as plt



def drzava_porekla():
    # drzave
    drzava = dict()
    neveljavne = ['-1', '1968', '1598', '1461', '1197']
    for row in dict_reader:
        try:
            int(row["D.4.2-Drzava (koda)"])
            continue
        except ValueError:
            pass
        except TypeError:
            pass
        if row["D.4.2-Drzava (koda)"] == None or row["D.4.2-Drzava (koda)"] != row["D.4.2-Drzava (koda)"].upper():
            continue
        if row["D.4.2-Drzava (koda)"] in drzava:
            drzava[row["D.4.2-Drzava (koda)"]] += 1
        else:
            drzava[row["D.4.2-Drzava (koda)"]] = 0

    z = sorted(drzava, key=drzava.get, reverse=True)[:20]
    zx, zy = list(), list()
    for a in z:
        zx.append(a)
        zy.append(drzava[a])
    zx = zx[::-1]
    zy = zy[::-1]

    y_pos = np.arange(len(zx))

    plt.barh(y_pos, zy, align='center', color='b')
    plt.yticks(y_pos, zx)
    plt.title('Države proizvodnje (kratice)')
    plt.rc('ytick', labelsize=20)
    plt.xlabel("Število avtomobilov")
    plt.tick_params(axis='x', which='major', labelsize=8)

    plt.show()



#BRANJE DATOTEKE
dict_reader = DictReader(open('podatki2CUT1.csv', "r", encoding="ISO-8859-2", newline=''), skipinitialspace=True, delimiter=";", quotechar=";")

drzava_porekla()
