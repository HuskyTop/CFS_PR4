import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Параметри моделі Лоренца
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Початкові умови
x, y, z = 1.0, 1.0, 1.0
dt = 0.01
num_steps = 10000

# Масиви для координат
xs, ys, zs = [], [], []

# Симуляція методом Ейлера
for _ in range(num_steps):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * dt
    y += dy * dt
    z += dz * dt
    xs.append(x)
    ys.append(y)
    zs.append(z)

# Анімація Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], lw=0.5)

ax.set_xlim((min(xs), max(xs)))
ax.set_ylim((min(ys), max(ys)))
ax.set_zlim((min(zs), max(zs)))
ax.set_title("Симуляція атрактора Лоренца")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")


def update(num):
    line.set_data(xs[:num], ys[:num])
    line.set_3d_properties(zs[:num])
    return line,

# Для тестів


def lorenz_step(x, y, z, sigma, rho, beta, dt):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * dt
    y += dy * dt
    z += dz * dt
    return x, y, z


def simulate_lorenz(x0, y0, z0, sigma, rho, beta, dt, num_steps):
    xs, ys, zs = [], [], []
    x, y, z = x0, y0, z0
    for _ in range(num_steps):
        x, y, z = lorenz_step(x, y, z, sigma, rho, beta, dt)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs, ys, zs


ani = animation.FuncAnimation(
    fig, update, frames=len(xs), interval=1, blit=True)
plt.show()
