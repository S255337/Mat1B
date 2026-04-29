from Opgave10 import random_surf
from Opgave12 import random_surf_damp

d = 0.85
W1 = {0: {1, 2}, 1: {2}, 2: {0}, 3: set()}
W2 = {0: {1}, 1: {2}, 2: {3}, 3: {0}}

# W1 med n = 100-106
for n in range(100, 106):
    print("Uden dæmpning:")
    print(random_surf(W1, n))
    print("Med dæmpning:")
    print(random_surf_damp(W1, n, d))

# W1 med n = 1000-1006
for n in range(1000, 1006):
    print("Uden dæmpning:")
    print(random_surf(W1, n))
    print("Med dæmpning:")
    print(random_surf_damp(W1, n, d))
    print()

# W1 med n = 10000-10006
for n in range(10000, 10006):
    print("Uden dæmpning:")
    print(random_surf(W1, n))
    print("Med dæmpning:")
    print(random_surf_damp(W1, n, d))
    print()

# W2 med n = 100-106
for n in range(100, 106):
    print("Uden dæmpning:")
    print(random_surf(W2, n))
    print("Med dæmpning:")
    print(random_surf_damp(W2, n, d))
    print()

# W2 med n = 1000-1006
for n in range(1000, 1006):
    print("Uden dæmpning:")
    print(random_surf(W2, n))
    print("Med dæmpning:")
    print(random_surf_damp(W2, n, d))
    print()

# W2 med n = 10000-10006
for n in range(10000, 10006):
    print("Uden dæmpning:")
    print(random_surf(W2, n))
    print("Med dæmpning:")
    print(random_surf_damp(W2, n, d))
    print()

