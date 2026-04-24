import time
from Opgave15 import recursive_PageRank
from Opgave25 import pagerank_numpy
from Opgave5 import make_web
from Opgave35 import matrix_PageRank
from Opgave24 import eigenvector_PageRank


def test_all(web, tol):
    print("Tester med tolerance:", tol)
    
    # 1. Recursive PageRank
    print("Kører Recursive PageRank:")
    start = time.time()
    
    resultat = recursive_PageRank(web, stopvalue=tol)
    antal_iterationer = resultat[1]
    
    tid = time.time() - start
    print("Tid:", round(tid, 4), "sekunder")
    print("Antal iterationer:", antal_iterationer, "\n")
    
    
    # 2. NumPy PageRank
    print("Kører NumPy PageRank")
    start = time.time()
    
    pagerank_numpy(web, tolerance=tol)
    
    tid = time.time() - start
    print("Tid:", round(tid, 4), "sekunder\n")
    
    
    # 3. Eigenvector PageRank
    print("Kører Eigenvector PageRank")
    start = time.time()
    
    eigenvector_PageRank(web)
    
    tid = time.time() - start
    print("Tid:", round(tid, 4), "sekunder\n")
    
    
    # 4. Matrix power PageRank
    print("Kører Matrix Power PageRank")
    start = time.time()
    
    matrix_PageRank(web, power=50)
    
    tid = time.time() - start
    print("Tid:", round(tid, 4), "sekunder\n")
    
    
    return 


# Lav ét stort netværk
print("Genererer et stort netværk\n")
web = make_web(2000, 10)

# Test med forskellige præcisioner
for tol in [1e-3, 1e-6, 1e-9]:
    test_all(web, tol)