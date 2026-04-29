import numpy as np
from Opgave5 import make_web
from Opgave35 import matrix_PageRank

def find_convergence(web, d, tolerance=1e-6, max_power=100):

    old_rank = None

    for power in range(1, max_power + 1):

        ranking = matrix_PageRank(web, power, d)

        pages = list(ranking.keys())
        new_rank = np.array([ranking[p] for p in pages])

        if old_rank is not None:
            diff = np.sum(np.abs(new_rank - old_rank))

            if diff < tolerance:
                return power, ranking

        old_rank = new_rank

    return max_power, ranking

web = make_web(2000, 10, 0)

d_values = [0.5, 0.75, 0.85, 0.9]

top5_all = {}

for d in d_values:

    power, ranking = find_convergence(web, d)

    print("\nd =", d)
    print("Konvergerer efter:", power)

    # Vi sorterer siderne efter deres PageRank værdi for at finde de top 5 sider
    sorted_pages = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("Top 5 sider:")
    
    top5 = []
    for i in range(5):
        print(sorted_pages[i])
        top5.append(sorted_pages[i][0])

    top5_all[d] = top5

print("\nSammenligning af top 5:")
for d in d_values:
    print("d =", d, ":", top5_all[d])