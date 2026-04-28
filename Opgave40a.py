import numpy as np
import time

from Opgave5 import make_web
from Opgave12 import random_surf_damp
from Opgave15 import recursive_PageRank
from Opgave24 import eigenvector_PageRank
from Opgave35 import matrix_PageRank


# Her sætter vi et netværk op. 
web = make_web(2000, 10, 0) #Vi har valgt 2000, for at det skulle være på et stort netværk.

d = 0.85


# 1: Random surfer med dæmpning
start = time.time()
ranking1 = random_surf_damp(web, 10000, d)
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
#Power=50 er et rimeligt valg for at sikre konvergens.
ranking4 = matrix_PageRank(web, power=50, d=d) 
end = time.time()
print("matrix_PageRank:", end - start, "sekunder")
