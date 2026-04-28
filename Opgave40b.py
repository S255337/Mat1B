import numpy as np
from Opgave5 import make_web
from Opgave35 import matrix_PageRank


def find_convergence(web, d, tolerance=1e-6, max_power=100):

    old_rank = None

    for power in range(1, max_power + 1):

        rank_dict = matrix_PageRank(web, power, d)

        pages = list(rank_dict.keys())
        new_rank = np.array([rank_dict[p] for p in pages])

        if old_rank is not None:
            diff = np.sum(np.abs(new_rank - old_rank))

            if diff < tolerance:
                return power, rank_dict

        old_rank = new_rank

    return max_power, rank_dict

web = make_web(2000, 10, 0)

d_values = [0.5, 0.75, 0.85, 0.9]

# Gemmer top 5 for hver d (så vi kan sammenligne)
top5_all = {}

for d in d_values:
    iterations, ranking = find_convergence(web, d)

    print("\nDæmpning d =", d)
    print("Antal iterationer før konvergens:", iterations)

    sorted_pages = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    print("Top 5 sider (side, værdi):")

    top5 = []  # Gemmer top 5 sider, så vi kan sammenligne senere

    for i in range(5):
        print(sorted_pages[i])
        top5.append(sorted_pages[i][0])

    top5_all[d] = top5

print("Sammenligning af top 5 sider:")

for d in d_values:
    print("d =", d, ":", top5_all[d])