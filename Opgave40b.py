import time
from Opgave5 import make_web
from Opgave35 import matrix_PageRank
from Opgave12 import random_surf_damp 


def test_damping(web, d_values, n_steps=100000):
    for d in d_values:
        print("="*40)
        print(f"Dæmpning d = {d}")
        
        # 1. Matrix PageRank
        start = time.time()
        ranks_matrix = matrix_PageRank(web, power=50, d=d)
        tid_matrix = time.time() - start
        
        print("Matrix metode:")
        print("Tid:", round(tid_matrix, 4), "sekunder")
        
        top_matrix = sorted(ranks_matrix.items(), key=lambda x: x[1], reverse=True)[:5]
        print("Top 5:", [(p, round(s, 6)) for p, s in top_matrix])
        
        
        # 2. Random surfer (Opgave 12)
        start = time.time()
        ranks_surf = random_surf_damp(web, n_steps, d)
        tid_surf = time.time() - start
        
        print("\nRandom surfer:")
        print("Tid:", round(tid_surf, 4), "sekunder")
        
        top_surf = sorted(ranks_surf.items(), key=lambda x: x[1], reverse=True)[:5]
        print("Top 5:", [(p, round(s, 6)) for p, s in top_surf])
        
        print()
        

# -----------------------------
# Kør test
# -----------------------------
print("Genererer netværk...\n")
web = make_web(2000, 10)

test_damping(web, [0.5, 0.75, 0.85, 0.9])