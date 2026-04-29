import numpy as np
import time

from Opgave5 import make_web
from Opgave12 import random_surf_damp
from Opgave15 import recursive_PageRank
from Opgave24 import eigenvector_PageRank
from Opgave35 import matrix_PageRank

web = make_web(2000, 10, 0)

d = 0.85

# 1: random_surf
start = time.time()
ranking1 = random_surf_damp(web, 2000000, d)
t_random = time.time() - start
print("random_surf_damp:", t_random)

# 2: recursive_PageRank
start = time.time()
ranking2, _ = recursive_PageRank(web, d=d)
t_recursive = time.time() - start
print("recursive_PageRank:", t_recursive)

# 3: eigenvector_PageRank
start = time.time()
ranking3 = eigenvector_PageRank(web, d)
t_eigen = time.time() - start
print("eigenvector_PageRank:", t_eigen)

# 4: Matrix_PageRank
start = time.time()
ranking4 = matrix_PageRank(web, power=30, d=d)
t_matrix = time.time() - start
print("matrix_PageRank:", t_matrix)

# Sammenligning af resultater
pages = list(web.keys())

# Arrays for PageRank værdier   
r1 = np.array([ranking1[p] for p in pages])
r2 = np.array([ranking2[p] for p in pages])
r3 = np.array([ranking3[p] for p in pages])  # reference
r4 = np.array([ranking4[p] for p in pages])

# Beregning af afvigelse fra eigenvector_PageRank
diff1 = np.sum(np.abs(r1 - r3))
diff2 = np.sum(np.abs(r2 - r3))
diff4 = np.sum(np.abs(r4 - r3))

# Sammenligning af PageRank værdier 
print("\nAfvigelse fra eigenvector:")
print("random_surf:", diff1)
print("recursive:", diff2)
print("matrix:", diff4)

# Sammenligning af tider
print("\n Sammenligning af tider")
print("random_surf_damp:", round(t_random, 6), "sek")
print("recursive:", round(t_recursive, 6), "sek")
print("eigenvector:", round(t_eigen, 6), "sek")
print("matrix:", round(t_matrix, 6), "sek")

print("\nTid i forhold til eigenvector:")

print("random - eigen :", round(t_random - t_eigen, 6), "sek")
print("recursive - eigen :", round(t_recursive - t_eigen, 6), "sek")
print("matrix - eigen :", round(t_matrix - t_eigen, 6), "sek")