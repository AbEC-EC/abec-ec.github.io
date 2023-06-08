from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.ticker import LinearLocator
'''
plt.rcParams["figure.figsize"] = (20, 8)
plt.style.use("dark_background")
plt.rcParams["axes.facecolor"] = "#1c1c1c"
plt.rcParams["axes.facecolor"] = "cornsilk"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "#1c1c1c"
plt.rcParams["savefig.facecolor"] = "white"
plt.rcParams['grid.color'] = "dimgrey"
'''
plt.style.use("dark_background")
plt.rcParams["axes.facecolor"] = "#1c1c1c"
plt.rcParams["savefig.facecolor"] = "#1c1c1c"
plt.rcParams["figure.figsize"] = (16, 9)




#plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)
#Z = 5*X*np.exp(- ( ((X)**2) + ((Y)**2) )/4)
#Z = 0.8*(3.5*X/np.exp((X**2+Y**2))-Y/np.exp((X**2+Y**2))+0.7*np.sin(X*Y)*1.5*np.cos(2*X))
#Z = 1*np.log(1*X**2 + 3*Y**2)
Z =(10*X**2)*(10*Y**2)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z, vmin=Z.min(), cmap="viridis", linewidth=2, antialiased=True )
ax.set_zlim(4, 5)

ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=10)


ax.w_xaxis.set_pane_color((0.28,0.28,0.28,0.28))
ax.w_xaxis.set_pane_color((0.28,0.28,0.28,0))
ax.w_yaxis.set_pane_color((0.28,0.28,0.28,0))
ax.w_zaxis.set_pane_color((0.28,0.28,0.28,0))


plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(1)
plt.grid(which="major", color="dimgrey", linewidth=5)
plt.grid(which="minor", color="dimgrey", linestyle=":", linewidth=0.5)


#ax.set(xticklabels=[],
 #      yticklabels=[],
  #     zticklabels=[])
plt.savefig(f"surfaceFitFunction.png", format="png")
plt.show()
