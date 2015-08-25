import numpy as np

N = 250

tabc = [np.random.randint(2) for i in range(N)]
markers = [np.random.randint(2) for i in range(N)]

def inv(x):
    if x == 1:
        return 0
    elif x == 0:
        return 1

def step(tabc, markers):
    res = [0]*N

    for i in range(N):
       if markers[i] == 1:
            res[(i+1)%N] = inv(tabc[i])
       elif markers[i] == 0:
            res[(i+1)%N] = tabc[i]
    return res 

def nstep(tabc, markers, k):
    for i in range(k):
        tabc=step(tabc,markers)
    return tabc

def av(tabc):
    return np.sum(tabc)

for i in range(2*N):
    tabc=step(tabc,markers)
    print(str(i)+" , "+str(av(tabc)))

