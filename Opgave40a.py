import numpy as np
import time

from Opgave5 import make_web
from Opgave12 import random_surf_damp
from Opgave15 import recursive_PageRank
from Opgave24 import eigenvector_PageRank
from Opgave35 import matrix_PageRank


#Vi har valgt 2000, for at det skulle være på et stort netværk.
web = make_web(2000, 10, 0) 

d = 0.85


# 1: Random surfer med dæmpning
start = time.time()
ranking1 = random_surf_damp(web, 1000000, d)
end = time.time()
print("random_surf_damp:", end - start, "sekunder")


# 2: Rekursiv PageRank
start = time.time()
ranking2, iters = recursive_PageRank(web, d=d)
end = time.time()
print("recursive_PageRank:", end - start, "sekunder")


# 3: Eigenvector metode
start = time.time()
ranking3 = eigenvector_PageRank(web, d)
end = time.time()
print("eigenvector_PageRank:", end - start, "sekunder")


# 4: Matrix metode
start = time.time()
ranking4 = matrix_PageRank(web, power=30, d=d) 
end = time.time()
print("matrix_PageRank:", end - start, "sekunder")


# Laver sammenligning af resultaterne ved at beregne den samlede absolutte forskel mellem hver metode og eigenvector (som reference). Jo mindre forskel, jo tættere er metoden på eigenvector-resultatet.
pages = list(web.keys())

# Laver arrays for hver ranking, så vi kan beregne forskelle
r1 = np.array([ranking1[p] for p in pages])
r2 = np.array([ranking2[p] for p in pages])
r3 = np.array([ranking3[p] for p in pages])  # reference (eigenvector)
r4 = np.array([ranking4[p] for p in pages])

# Her beregner vi den samlede absolutte forskel mellem hver metode og eigenvector-resultatet
diff1 = np.sum(np.abs(r1 - r3))
diff2 = np.sum(np.abs(r2 - r3))
diff4 = np.sum(np.abs(r4 - r3))

print("\nAfvigelse fra eigenvector:")
print("random_surf:", diff1)
print("recursive:", diff2)
print("matrix:", diff4)
