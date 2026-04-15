from Opgave12 import random_surf_damp

d = 0.85

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

print("W1:")
print(random_surf_damp(W1, 100, d))
print(random_surf_damp(W1, 1000, d))
print(random_surf_damp(W1, 10000, d))

print("\nW2:")
print(random_surf_damp(W2, 100, d))
print(random_surf_damp(W2, 1000, d))
print(random_surf_damp(W2, 10000, d))