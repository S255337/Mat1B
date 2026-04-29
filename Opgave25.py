import time

from Opgave5 import make_web
from Opgave24 import eigenvector_PageRank

web = make_web(5000, 10, 0)

start = time.time()
eigenvector_PageRank(web)

end = time.time()

print("Det tager", round(end - start, 6), "sekunder at beregne PageRanken")