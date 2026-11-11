import numpy as np
import json
import scipy

rng = np.random.default_rng()

#get this params to work later
#params = json.load("setup.json")

params = {"height": 4, "width" : 4}

graph = np.zeros((params["height"],params["width"]))

# Right now this is operating under the assumption that spin up and spin down are equally as likely
spins = np.array(rng.standard_normal(params["height"] * params["width"]))

spins[np.where(spins > 0.5)] = 1
spins[np.where(spins <= 0.5)] = -1

for i in range(0,params["height"]):
    for j in range(0,params["width"]):
        graph[i,j] = spins[i + j]

print(graph)