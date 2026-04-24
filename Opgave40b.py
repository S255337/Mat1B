import time
from Opgave5 import make_web
from Opgave35 import matrix_PageRank


def test_damping(web, d_values):
    for d in d_values:
        print(f"Dæmpning d = {d}")
        
        start = time.time()
        ranks = matrix_PageRank(web, power=50, d=d)
        tid = time.time() - start
        
        print("Tid:", round(tid, 4), "sekunder")
        
        top = sorted(ranks.items(), key=lambda x: x[1], reverse=True)[:5]
        print("Top 5 sider:", top)


#Samme netværk
web = make_web(2000, 10)

#Test forskellige d
test_damping(web, [0.5, 0.75, 0.85, 0.9])