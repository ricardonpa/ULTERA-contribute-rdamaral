# %% Snippet for converting wieight percent to atomic percent
from pymatgen.core import Composition

def weight_to_atomic_percent(weight_percent):
    # Convert weight percent to composition
    comp = Composition.from_weight_dict(weight_percent)

    # Get atomic percent
    atomic_percent = comp.fractional_composition.get_el_amt_dict()

    return atomic_percent

alloys = [{"Ni": 61.5, "W": 9.4, "Co": 9.3, "Cr": 8.1, "Al": 5.7, "Ta": 3.3, "Hf": 1.4, "Ti": 0.4, "Mo": 0.5, "C": 0.07, "B": 0.017, "Zr": 0.007},
          {"Ni": 63.8, "Co": 6.5, "Cr": 7.8, "Mo": 2, "W": 5.7, "Al": 5.2, "Ti": 1.1, "Ta": 7.9},
          {"Ni": 70.3, "Cr": 4, "Mo": 1, "W": 5, "Re": 4, "Ru": 4, "Al": 6, "Ti": 0.5, "Ta": 5, "Si": 0.1, "Hf": 0.1},
          {"Ta": 97.141, "W": 2.5, "Nb": 0.15, "O": 0.004, "N": 0.002, "C": 0.003, "Fe": 0.19, "Mo": 0.009, "Zr": 0.001},
          {"Ti": 58.5, "Al": 32.04, "W": 9.11, "Si": 0.35},
          {"Ti": 50.14, "Al": 28.29, "Nb": 21.57},
          {"Ti": 42, "Al": 22.78, "Nb": 33.36, "Cr": 1.86},
          {"Ti": 60.01, "Al": 32.55, "W": 4.77, "Si": 2.67},
          {"Ti": 82.95, "Al": 6, "Sn": 4, "Zr": 4, "Mo": 0.8, "Nb": 1, "W": 1, "Si": 0.25},
          {"V": 92, "Cr": 4, "Ti": 4},
          {"W": 96.07, "Re": 3.6, "Zr": 0.29, "C": 0.04},
          {"Cr":6.5, "Co": 9.6, "W": 6.4, "Re":3, "Mo": 0.6, "Al": 5.6, "Ti": 1, "Ta": 6.5, "Hf": 0.1, "Ni": 60.7}]

for alloy in alloys:
    print({k: round(v, 4) for k, v in weight_to_atomic_percent(alloy).items()})