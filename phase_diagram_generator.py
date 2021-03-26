#Hitarth Choubisa
#https://github.com/hitarth64/magpie_featurize_elements

from pymatgen import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import *
from pymatgen.io.ase import *
from pymatgen.io.vasp import Vasprun
from ase.io import read

MAPI_KEY = 'your_mapi_key'
mpr = MPRester(MAPI_KEY)

compat = MaterialsProjectCompatibility()

system = ["C","H","N","Cl"]
unprocessed_entries = mpr.get_entries_in_chemsys(system)
processed_entries = compat.process_entries(unprocessed_entries)
pd = PhaseDiagram(processed_entries)
vrun = Vasprun('vasprun.xml')
struct = AseAtomsAdaptor.get_structure(read('POSCAR'))
obj = PDEntry(struct.composition, energy=vrun.final_energy)

pd.get_form_energy_per_atom(obj)
pd.get_decomp_and_e_above_hull(obj)
