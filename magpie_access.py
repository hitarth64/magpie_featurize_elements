# Directory named data_files must be present in the same directory as this file.

import os
import json
import six
import abc
import numpy as np
import pandas as pd
from glob import glob
from pymatgen import Element
from pymatgen.core.periodic_table import _pt_data

class MagpieData():

    def __init__(self):
        self.all_elemental_props = dict()
        available_props = []
        self.data_dir = os.path.join(module_dir, "data_files",
                                     'magpie_elementdata')

        # Make a list of available properties
        for datafile in glob(os.path.join(self.data_dir, "*.table")):
            available_props.append(
                os.path.basename(datafile).replace('.table', ''))
        
        # List of all the properties present in Magpie
        self.props = available_props
        
        # parse and store elemental properties
        for descriptor_name in available_props:
            with open(os.path.join(self.data_dir,
                                   '{}.table'.format(descriptor_name)),
                      'r') as f:
                self.all_elemental_props[descriptor_name] = dict()
                lines = f.readlines()
                for atomic_no in range(1, len(_pt_data) + 1):  # max Z=103
                    try:
                        if descriptor_name in ["OxidationStates"]:
                            prop_value = [float(i) for i in
                                          lines[atomic_no - 1].split()]
                        else:
                            prop_value = float(lines[atomic_no - 1])
                    except ValueError:
                        prop_value = float("NaN")
                    self.all_elemental_props[descriptor_name][
                        Element.from_Z(atomic_no).symbol] = prop_value
   
        list_of_dfs = []
        for i in self.all_elemental_props.keys():
            if i!='OxidationStates':
              list_of_dfs.append(pd.DataFrame.from_dict(self.all_elemental_props[i],orient='index'))
              list_of_dfs[-1] = list_of_dfs[-1].rename(columns={0:i})
            else:
              tmp = pd.DataFrame.from_dict(mpg.all_elemental_props['OxidationStates'], orient='index').index.values
              list_of_dfs.append(pd.DataFrame([[[j for j in k if str(j)!='nan']] for k in pd.DataFrame.from_dict(mpg.all_elemental_props['OxidationStates'],orient='index').values.tolist()], index=tmp, columns=[i])) 
        self.dfp = pd.concat(list_of_dfs,axis=1)

    def get_elemental_property(self, elem, property_name):
        return self.all_elemental_props[property_name][elem]

    def get_oxidation_states(self, elem):
        return self.all_elemental_props["OxidationStates"][elem]
