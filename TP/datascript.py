import matplotlib.pyplot as plt
import numpy as np
import sys

result=[]
cpt=0
# input comes from STDIN
for line in sys.stdin:
    niveau, formation, filiere, inscrit = line.split(',')
    result.append((filiere, int(inscrit)))
    print(cpt, niveau, formation, filiere)
    cpt= cpt +1
  
print(result)
plt.rcdefaults()
fig, ax = plt.subplots(figsize=(100,50))
# Example data
header = tuple(i[0] for i in result)
y_pos = np.arange(len(header))
error = 0
ax.barh(y_pos, tuple(i[1] for i in result), xerr=error, align='center')
plt.subplots_adjust(left=0.306)
ax.set_yticks(y_pos, labels=header)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Nbr inscrits')
ax.set_title('Filières les plus demandées:')
plt.show()
