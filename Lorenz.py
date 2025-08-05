import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation
from matplotlib import cm


def lorenz(xyz, *, s=10, r=28, b=2.667):
    x,y,z = xyz
    x_dot = s*(y-x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

dt = 0.001
num_steps = 100000

xyzs = np.empty((num_steps +1, 3))
xyzs[0] = (0., 1., 1.05)

for i in range(num_steps):
    xyzs[i+1] = xyzs[i] + lorenz(xyzs[i])*dt

colors = cm.plasma(np.linspace(0,1,num_steps))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
line, = ax.plot([], [], [], lw=0.8)

ax.set_xlim((np.min(xyzs[:, 0]), np.max(xyzs[:, 0])))
ax.set_ylim((np.min(xyzs[:, 1]), np.max(xyzs[:, 1])))
ax.set_zlim((np.min(xyzs[:, 2]), np.max(xyzs[:, 2])))

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor - Animated")

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def update(frame):
    line.set_data(xyzs[:frame, 0], xyzs[:frame, 1])
    line.set_3d_properties(xyzs[:frame, 2])
    line.set_color(colors[frame])
    return line,

ani = FuncAnimation(fig, update, frames=num_steps, init_func=init, blit = True, interval = 1)

plt.show()