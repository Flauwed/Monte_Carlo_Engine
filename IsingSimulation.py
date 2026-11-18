import numpy as np
import json
import pathlib


with open(pathlib.Path(__file__).parent / "Setup.json") as jf:
    params = json.load(jf)
#params is structured as : {ferromagnetic: 0/1, width : int, height : int, variable_J : 0/1, h : 0/1, "seed" : int}
# ferromagnetic is assumed to be 1 if true, 0 if anti ferromagnetic
# width / height determine the size of your lattice grid, m x n matrix corresponds to h x w
# seed is used to set the rng generator

def create_lattice(seed=None,height=3,width=3):
    rng = np.random.default_rng(seed)
    lattice = rng.choice([-1, 1], size=(height, width))
    return lattice
# lattice will now default to a random 3x3 if no seed, width, or height is automatically passed


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

lattice = create_lattice(params["seed"],params["height"],params["width"])
#lattice = create_lattice()
# if nothing is passed, defaults to random 3x3, otherwise follow the above syntax to pull from the json file

positive = np.where(lattice > 0)
negative = np.where(lattice < 0)

print(lattice)
print(neighbor_sum(lattice,2,2))