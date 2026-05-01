import numpy as np
from Opgave5 import make_web
from Opgave35 import matrix_PageRank


def find_convergence(web, d, tol=1e-6, max_power=100):
    previous = None

    for power in range(1, max_power + 1):
        ranking = matrix_PageRank(web, power, d)

        pages = list(ranking)
        current = np.array([ranking[p] for p in pages])

        if previous is not None:
            diff = np.abs(current - previous).sum()
            if diff < tol:
                return power, ranking
        previous = current

    return max_power, ranking

web = make_web(2000, 10, 0)
d_values = [0.5, 0.75, 0.85, 0.9]
top5_for_all = {}

for d in d_values:
    power, ranking = find_convergence(web, d)
    print("\nd =", d)
    print("Konvergerer efter:", power)

    sorted_pages = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    print("Top 5 sider:")
    top5 = []

    for i in range(5):
        page, value = sorted_pages[i]
        print((page, value))
        top5.append(page)
    top5_for_all[d] = top5


print("\nSammenligning af top 5:")
for d in d_values:
    print("d =", d, ":", top5_for_all[d])