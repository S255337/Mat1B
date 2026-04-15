import numpy as np

def modified_link_matrix(web, pagelist, d=0.85):

    N = len(pagelist)

    A = np.zeros((N, N))  
    index = {page: i for i, page in enumerate(pagelist)}

    for j, page in enumerate(pagelist):

        links = web[page]

        if len(links) == 0:
            A[j, :] = 1 / N 
            for target in links:
                i = index[target]
                A[j, i] = 1 / len(links)

    E = np.ones((N, N))

    M = d * A.T + (1 - d) * E / N

    return M
#Uden W'erne test