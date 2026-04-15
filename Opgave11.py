from Opgave10 import random_surf

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

print("W1 af n:")
for n in range(100, 106, 1):
    print(n, random_surf(W1, n))

print("\nW2 af n:")
for n in range(10000, 10006, 1):
    print(n, random_surf(W2, n))


