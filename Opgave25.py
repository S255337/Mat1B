import time

from Opgave5 import make_web
from Opgave24 import eigenvector_PageRank

# Laver netværket som bedt om i opgaveskrivelsen
web = make_web(5000, 10, 0)

ranking = eigenvector_PageRank(web)

# Her måler vi tiden det tager at beregne PageRank for dette netværk ved hjælp af eigenvector metoden
start = time.time()

end = time.time()

# Vi primterer tiden det tog at beregne PageRank
print("Det tager", end - start, "sekunder at beregne PageRanken")