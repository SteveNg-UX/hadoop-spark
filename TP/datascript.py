import matplotlib.pyplot as plt
import csv

dep_data = []

with open('parcoursup.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        try:
            dep = int(row['dep'])
            dep_data.append(dep)
        except ValueError:
            print("Ignoring line {}: invalid value for dep".format(reader.line_num))

plt.hist(dep_data, bins=50, color='blue', alpha=0.7)
plt.xlabel('Département')
plt.ylabel('Nombre de candidats')
plt.title('Répartition des candidats par département')
plt.grid(True)

plt.savefig('output.png')

plt.show()
