import numpy as np
import json
import scipy

rng = np.random.default_rng()

def check_nodes(current_index, edge):
    if edge == True:
        pass
    else:
        neighbors = [[current_index[0],current_index[1]-1],
                     [current_index[0],current_index[1]+1],
                     [current_index[0]+1,current_index[1]],
                     [current_index[0]-1,current_index[1]],
                     ]
        spin_sum = 0
        for element in neighbors:
            if element[0] in positive and element[1] in positive:
                spin_sum += 1
            else:
                spin_sum -= 1
        net_spin = graph[current_index] * spin_sum
    return net_spin
        


#fix filepath later
with open("/home/jax/montecarloengine/Monte_Carlo_Engine/setup.json") as jf:
    params = json.load(jf)
#params is structured as : {ferromagnetic: 0/1, width : int, height : int, variable_J : 0/1, h : 0/1}
# ferromagnetic is assumed to be 1 if true, 0 if anti ferromagnetic
# width / height determine the size of your lattice grid, m x n matrix corresponds to h x w
# if variable_J is 0, all interactions are assumed to be equal strength with J = 
# if h is 0, its assumed you have no external magnetic field, which simplifies hamiltonian calculations

graph = np.zeros((params["height"],params["width"]))

# operates under the assumption that spin up and spin down are equally as likely
spins = np.array(rng.standard_normal(params["height"] * params["width"]))
spins[np.where(spins > 0.5)] = 1
spins[np.where(spins <= 0.5)] = -1

for i in range(0,params["height"]):
    for j in range(0,params["width"]):
        graph[i,j] = spins[i + j]

print(graph)

positive = np.where(graph > 0)
negative = np.where(graph < 0)

print(check_nodes((1,1),False))
