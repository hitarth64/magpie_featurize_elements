from ase.io import read, vasp
import numpy as np
from ase.eos import EquationOfState

# Input file or geometry
x = read('POSCAR')

# Generate different geometries with different volumes
# Relax all these with ISIF=4
count = 0
for a in np.linspace(8.9,9.4,5):
	for c in np.linspace(9.2,9.6,5):
		x.set_cell([a, a, c])
		vasp.write_vasp(str(count)+'/POSCAR',x,direct=True,long_format=False)
		count += 1


# Parse the DFT results 
from ase.units import kJ
from pymatgen.io.vasp import Vasprun
from ase.io import read, vasp

recs = {}
for i in range(25):
	try:
		vrun = Vasprun(str(i)+'/vasprun.xml')
		x = read(str(i)+'/CONTCAR')
		recs[x.get_volume()] = vrun.final_energy
	except:
		pass

volumes = list(recs.keys())
energies = list(recs.values())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(B / kJ * 1.0e24, 'GPa')
