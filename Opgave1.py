import numpy as np
import matplotlib.pyplot as plt


V_1 = ['p1', 'p2', 'p3', 'p4', 'p5']

E_1 = [
    ('p1', 'p3'), ('p1', 'p5'),
    ('p2', 'p4'), ('p2', 'p5'),
    ('p3', 'p1'),
    ('p4', 'p1'), ('p4', 'p2'), ('p4', 'p5')
]

positions = { #Her har vi valgt "random" positioner, da ingen var givet i opgaven.
    'p1': np.array([0, 1]),
    'p2': np.array([1, 1]),
    'p3': np.array([0, 0]),
    'p4': np.array([1, 0]),
    'p5': np.array([0.5, -0.5])
}

plt.figure(figsize=(6,6))

for V_1, pos in positions.items():
    plt.scatter(pos[0], pos[1])
    plt.text(pos[0] + 0.02, pos[1] + 0.02, V_1)

for start, end in E_1:
    p1 = positions[start]
    p2 = positions[end]
    
    dx, dy = p2 - p1
    
    plt.arrow(p1[0], p1[1], dx, dy, length_includes_head=True, head_width=0.05, head_length=0.08, fc='black', ec='black')

plt.title("Graf W₁")
plt.grid()
plt.axis('equal')
plt.show()