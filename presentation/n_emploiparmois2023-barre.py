import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('csv/series_offres_diffusees-Total.csv','r') as data:
	plots = csv.DictReader(data, delimiter = ';')
	for col in plots:
		x.append(col["Année"])
		y.append(col["Nombre d'offres diffusées"])

plt.bar(x, y, color = 'g', width = 0.5, label = "nombre d'emplois diffuse")
plt.xlabel('Annee')
plt.ylabel('Emplois')
plt.title('Nombre d\'emplois diffuses par annees')
plt.legend()
plt.savefig('graph-output/emplois_annee.png')