import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('csv/series_offres_diffusees-Total.csv', 'r') as data:
	plots = csv.DictReader(data, delimiter=';')
	for col in plots:
		x.append(col["Année"])
		y.append(col["Nombre d'offres diffusées"])

fig, ax = plt.subplots()
ax.bar(x, y)

ax.set_ylabel("nombre d'offre")
ax.set_title("Nombre d'offres en fonction de l'année")
ax.legend()

plt.savefig('graph/output.png')
