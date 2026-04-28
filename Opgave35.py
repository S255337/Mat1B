import numpy as np
from Opgave17 import modified_link_matrix

def matrix_PageRank(web, power, d=0.85):

    ranking = dict()
    
    pagelist = list(web.keys())
    N = len(pagelist)
    
    # Her laver vi den modificerede link matrix M
    M = modified_link_matrix(web, pagelist, d)
    
    # Vi ganger M med sig selv power gange
    M_power = np.linalg.matrix_power(M, power)
    
    # Startvektor med lige sandsynlighed for alle sider
    v = np.ones(N) / N
    
    # Vi ganger M_power med startvektoren v
    v = M_power @ v
    
    # normaliser så summen bliver 1
    v = v / np.sum(v)
    
    # lav dictionary som output
    for i in range(N):
        ranking[pagelist[i]] = v[i]
    
    return ranking