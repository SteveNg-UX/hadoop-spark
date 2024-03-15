import csv
import matplotlib.pyplot as plt
import numpy as np

u = []
v = []
w = []
x = []
y = []
z = []

with open('csv/series_offres_diffusees-Contrats.csv', 'r') as data:
	plots = csv.DictReader(data, delimiter=',')
	for col in plots:
		if col['Année'] == '2023':
			u.append(col["Mois"])
			v.append(col["CDI"])
			w.append(col["CDD de plus de 6 mois"])
			x.append(col["CDD de 1 à 6 mois"])
			y.append(col["CDD de moins d'un mois"])
			z.append(col["Autres contrats (intérim, saisonniers, ...)"])

penguin_means = {
    'CDI': v,
    'CDD de plus de 6 mois': w,
    'CDD de 1 à 6 mois': x,
    'CDD de moins d\'un mois': y,
    'Autres contrats (intérim, saisonniers, ...)': z,
}

i = np.arange(len(u))
width = 0.15
multiplier = 0

#fig, ax = plt.subplots(layout='constrained')
fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(i + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_ylabel("Offres d'emploi")
ax.set_title("Nombre d'offre d'emploie par type de contrat")
ax.set_xticks(i + width, u)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 55)

plt.savefig('graph/output.png')
