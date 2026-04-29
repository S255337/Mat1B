import numpy as np
from Opgave9 import surf_step
from Opgave10 import random_surf

# Vi sætter to webs op, W1 og W2, som vi bruger til at teste vores random_surf funktion
W1 = {0: {1, 2},1: {2},2: {0},3: set()
}

W2 = {0: {1},1: {2},2: {3},3: {0}
}

# Her laver vi et for loop for at teste til 100-106
for n in range(100, 106, 1):
    print(random_surf(W1, n))

# W1 med n = 1000-1006
for n in range(1000, 1006, 1):
    print(random_surf(W1, n))

# W1 med n = 10000-10006
for n in range(10000, 10006, 1):
    print(random_surf(W1, n))

# W2 med n = 100-106
for n in range(100, 106, 1):
    print(random_surf(W2, n))

# W2 med n = 1000-1006
for n in range(1000, 1006, 1):
    print(random_surf(W2, n))

# W2 med n = 10000-10006
for n in range(10000, 10006, 1):
    print(random_surf(W2, n))