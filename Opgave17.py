import numpy as np

def modified_link_matrix(web, pagelist, d=0.85):
    
    N = len(pagelist)
    
    A = np.zeros((N, N))
    
    # Her laver vi en index-dictionary for at kunne finde kolonnerne i matrixen
    index = {}
    for i in range(N):
        index[pagelist[i]] = i
    
    # I denne loop fylder vi matrixen A ud baseret på links i webben
    for j in range(N):
        page = pagelist[j]
        links = web[page]
        
        if len(links) == 0:
            # Hvis der ingen links er, så er sandsynligheden ligeligt fordelt
            A[j, :] = 1 / N
        else:
            for link in links:
                i = index[link]
                A[j, i] = 1 / len(links)
    
    # Maxtrix E med alle elementer 1
    E = np.ones((N, N))
    
    # Beregn den modificerede link matrix M
    M = d * A.T + (1 - d) * E / N
    
    return M