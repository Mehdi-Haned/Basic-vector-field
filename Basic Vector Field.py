
import numpy as np
import matplotlib.pyplot as plt
import cmath

plt.style.use(["science", "notebook"])


x = np.linspace(-4, 4, 15)
y = np.linspace(-4, 4, 15)

x,y = np.meshgrid(x,y)

x_shape = x.shape

y2 = np.zeros(x_shape)
x2 = np.zeros(x_shape)

for i in range(x_shape[0]):
    for j in range(x_shape[1]):
        X = x[i,j]
        Y = y[i,j]
        x2[i,j] = np.cos(Y)
        y2[i,j] = np.sin(X)

fig, ax = plt.subplots()

ax.plot(x,y, marker='.', color='k', linestyle='none')
q = ax.quiver(x, y, x2, y2, units='xy' ,scale = 1.5, color='red')

ax.grid()

ax.set_aspect('equal', 'box')
ax.set_ylim(-5,5)
ax.set_xlim(-5,5)

plt.show()
