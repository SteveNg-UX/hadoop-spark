import csv
import matplotlib.pyplot as plt

u = []
v = []
w = []
x = []
y = []
z = []

with open('csv/series_offres_difusees-Contrat.csv', 'r') as data:
    plots = csv.DictReader(data, delimiter=',')
    for col in plots:
        if col['Année'] == '2023':
            u.append(col["Mois"])
            v.append(col["CDI"])
            w.append(col["CDD de plus de 6 mois"])
            x.append(col["CDD de 1 à 6 mois"])
            y.append(col["CDD de moins d'un mois"])
            z.append(col["Autres contrats (intérim, saisonniers, ...)"])

bar_width = 0.15

positions = range(len(u))

plt.figure(figsize=(10, 6))
plt.bar(positions, v, label='CDI', color='b', width=bar_width)
plt.bar([p + bar_width for p in positions], w, label='CDD > 6 mois', color='g', width=bar_width)
plt.bar([p + 2 * bar_width for p in positions], x, label='CDD 1 à 6 mois', color='r', width=bar_width)
plt.bar([p + 3 * bar_width for p in positions], y, label='CDD < 1 mois', color='y', width=bar_width)
plt.bar([p + 4 * bar_width for p in positions], z, label='Autres contrats', color='m', width=bar_width)

plt.xlabel('Mois')
plt.ylabel("Nombre d'emplois")
plt.title('Emplois diffusés par mois en fonction des contrats')
plt.xticks([p + 2 * bar_width for p in positions], u)  # Afficher uniquement certains mois
plt.legend()
plt.tight_layout()
plt.savefig('graph-output/output.png')
