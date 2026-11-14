import numpy as np
import json
import pathlib


with open(pathlib.Path(__file__).parent / "setup.json") as jf:
    params = json.load(jf)
#params is structured as : {ferromagnetic: 0/1, width : int, height : int, variable_J : 0/1, h : 0/1, "seed" : seed}
# ferromagnetic is assumed to be 1 if true, 0 if anti ferromagnetic
# width / height determine the size of your lattice grid, m x n matrix corresponds to h x w
# if variable_J is 0, all interactions are assumed to be equal strength with J = 
# if h is 0, its assumed you have no external magnetic field, which simplifies hamiltonian calculations
# seed is used to set the rng generator

rng = np.random.default_rng(params["seed"])

def neighbor_sum(lattice, i, j):
    h, w = lattice.shape
    return (lattice[(i-1) % h, j] + lattice[(i+1) % h, j] + lattice[i, (j-1) % w] + lattice[i, (j+1) % w])
        



lattice = rng.choice([-1, 1], size=(params["height"], params["width"]))


positive = np.where(lattice > 0)
negative = np.where(lattice < 0)

print(lattice)
print(neighbor_sum(lattice,2,2))