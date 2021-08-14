
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

plt.style.use(["science", "notebook"])


x = np.linspace(-4, 4, 15)
y = np.linspace(-4, 4, 15)

x,y = np.meshgrid(x,y)

def f(a,b):
    return np.cos(b) * a

def g(a,b):
    return np.sin(a) * b

fig, ax = plt.subplots()

r = ( f(x,y)**2 + g(x,y)**2 )**(1/2)

ax.plot(x,y, marker='.', color='k', linestyle='none')

Q  = ax.quiver( x, y, f(x,y)/r, g(x,y)/r, r,
                scale = 20, cmap = 'bwr',
                norm = colors.Normalize( vmin = r.min(),vmax = r.max()) )

fig.colorbar(Q,extend='max')


#Q  = ax.quiver(x, y, f(x,y)/r, g(x,y)/r, r,
#               scale = 20, cmap = 'coolwarm',
#               norm=colors.Normalize(vmin=r.min(),vmax=r.max())
#               )
#for if you dont want a vector field with only unit vectors


ax.grid()

ax.set_aspect('equal', 'box')
ax.set_ylim(-5,5)
ax.set_xlim(-5,5)

plt.show()
