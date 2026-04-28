import numpy as np
from Opgave17 import modified_link_matrix

def eigenvector_PageRank(web, d=0.85):
    
    ranking = dict()
    
    pagelist = list(web.keys())
    
    M = modified_link_matrix(web, pagelist, d)
    
    eigvals, eigvecs = np.linalg.eig(M)
    
    i = np.argmin(np.abs(eigvals - 1))
    
    v = eigvecs[:, i]
    
    v = np.real(v)
    v = np.abs(v)
    
    v = v / np.sum(v)
    
    for j in range(len(pagelist)):
        ranking[pagelist[j]] = v[j]
    
    return ranking