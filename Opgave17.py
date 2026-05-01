import numpy as np

def modified_link_matrix(web, pages, d=0.85):
    n = len(pages)
    
    # Laver et tomt link matrix A
    A = np.zeros((n, n))
    
    # Mapping fra side til indeks
    page_index = {page: i for i, page in enumerate(pages)}
    
    for j, page in enumerate(pages):
        links = web[page]
        
        if not links:
            # Hvis siden ikke linker til noget
            A[j, :] = 1 / n
        else:
            prob = 1 / len(links)
            for link in links:
                A[j, page_index[link]] = prob
    
    # Den givne formel for M
    M = d * A.T + (1 - d) / n * np.ones((n, n))
    
    return M


# Test data
W1 = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}
W2 = {0: {1}, 1: {2}, 2: {0}, 3: {4}, 4: {5}, 5: {3}}

M1 = modified_link_matrix(W1, list(W1), d=0.85)
M2 = modified_link_matrix(W2, list(W2), d=0.85)

print("M1:\n", M1, "\n")
print("M2:\n", M2, "\n")

print("M1 sum:", M1.sum(axis=0))
print("M2 sum:", M2.sum(axis=0))