import numpy as np

def modified_link_matrix(web, pagelist, d=0.85):
    
    N = len(pagelist)
    
    A = np.zeros((N, N))
    
    # Vi laver et index for at kunne finde positionen af hver side i matrixen
    index = {}
    for i in range(N):
        index[pagelist[i]] = i
    
    # Her i dette for loop laver vi matrix A, hvor A[j, i] er sandsynligheden for at gå fra side j til side i
    for j in range(N):
        page = pagelist[j]
        links = web[page]
        
        if len(links) == 0:
            # Hvis der ikke er nogen links, så bliver sandsynligheden fordelt ligeligt
            A[j, :] = 1 / N
        else:
            for link in links:
                i = index[link]
                A[j, i] = 1 / len(links)
    
    # Her laver vi en NxN matrix E, hvor alle elementer er 1
    E = np.ones((N, N))
    
    # Så beregner vi den modificerede link matrix M ved at bruge givende formel fra opgaven
    M = d * A.T + (1 - d) * E / N
    
    return M

W1 = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}
W2 = {0: {1}, 1: {2}, 2: {0}, 3: {4}, 4:{5}, 5: {3}}  

pagelist_W1 = list(W1.keys())
pagelist_W2 = list(W2.keys())

M1 = modified_link_matrix(W1, pagelist_W1, d=0.85)
M2 = modified_link_matrix(W2, pagelist_W2, d=0.85)

print("M1:\n", M1)
print()
print("M2:\n", M2)
print()

print("M1 sum:", M1.sum(axis=0))
print("M2 sum:", M2.sum(axis=0))