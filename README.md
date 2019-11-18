# python_featurize_elements
Python module to generate chemistry representations of the elements. 

Features borrowed from Magpie library which is Java based (https://bitbucket.org/wolverton/magpie/src). 
Code structure borrowed from [matminer](https://github.com/hackingmaterials/matminer)

Clone the repository and you can access 65 different chemical properties for elements with atomic numbers up to 103. Aim is to enable researchers doing material informatics get easy access to elemental descriptors. 

Will add more databases for properties with time. 

Sample code to access Magpie based properties:

```python
from magpie_access import MagpieData
mgd = MagpieData()

# Get dataframe of properties for all the elements
dfp = mgd.dfp

# Access individual property for an element (Pb for example)
print(mgd.all_elemental_props['ShearModulus']['Pb'])

```
