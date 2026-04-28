import numpy as np
from Opgave10 import random_surf
from Opgave12 import random_surf_damp

d = 0.85

# Netværkene fra opgave 11
W1 = {
    "LinkA": ["LinkB", "LinkC"],
    "LinkB": ["LinkC"],
    "LinkC": []
}

W2 = {
    "LinkA": ["LinkB"],
    "LinkB": ["LinkA"],
    "LinkC": ["LinkA", "LinkB"]
}

# Samme n-værdier som i opgave 11
n_values = np.array([100, 1000, 10000])

print("W1:")
for n in n_values:
    print("n =", n)
    print("uden dæmpning:", random_surf(W1, int(n)))
    print("med dæmpning :", random_surf_damp(W1, int(n), d))
    print()

print("W2:")
for n in n_values:
    print("n =", n)
    print("uden dæmpning:", random_surf(W2, int(n)))
    print("med dæmpning :", random_surf_damp(W2, int(n), d))
    print()

# Stabilitetstest for n omkring 100 og 10000
print("W1 omkring n = 100:")
for n in np.arange(100, 106):
    print("n =", n, random_surf_damp(W1, int(n), d))

print()

print("W2 omkring n = 10000:")
for n in np.arange(10000, 10006):
    print("n =", n, random_surf_damp(W2, int(n), d))