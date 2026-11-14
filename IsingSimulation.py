import numpy as np
import json
import pathlib


with open(pathlib.Path(__file__).parent / "Setup.json") as jf:
    params = json.load(jf)
#params is structured as : {ferromagnetic: 0/1, width : int, height : int, variable_J : 0/1, h : 0/1, "seed" : int}
# ferromagnetic is assumed to be 1 if true, 0 if anti ferromagnetic
# width / height determine the size of your lattice grid, m x n matrix corresponds to h x w
# seed is used to set the rng generator

rng = np.random.default_rng(params["seed"])
#remove the params["seed"] if you want automatic random seeds without editing the Setup.json file
 
def neighbor_sum(lattice, i, j):
    h, w = lattice.shape
    neighbor_sum = (lattice[(i-1) % h, j] + lattice[(i+1) % h, j] 
                    + lattice[i, (j-1) % w] + lattice[i, (j+1) % w])
    return neighbor_sum


def net_spin(lattice,i,j):
    net_spin = lattice[i,j] * neighbor_sum(lattice,i,j)
    return net_spin

def total_energy(lattice):
    return

def magnetism(lattice):
    return

lattice = rng.choice([-1, 1], size=(params["height"], params["width"]))

positive = np.where(lattice > 0)
negative = np.where(lattice < 0)

print(lattice)
print(neighbor_sum(lattice,2,2))