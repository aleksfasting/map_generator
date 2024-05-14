import numpy as np
import matplotlib.pyplot as plt

def generate_random_points(num_points, size=1):
    points = np.random.rand(num_points, 2) * size
    return points

def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

def find_closest_point(points, grid_point):
    min_distance = float('inf')
    closest_point_index = -1
    for i, point in enumerate(points):
        dist = euclidean_distance(point, grid_point)
        if dist < min_distance:
            min_distance = dist
            closest_point_index = i
    return closest_point_index

def create_voronoi_diagram(points, grid_size, resolution=500):
    voronoi_grid = np.zeros((resolution, resolution))
    x = np.linspace(0, grid_size, resolution)
    y = np.linspace(0, grid_size, resolution)
    xv, yv = np.meshgrid(x, y)
    
    for i in range(resolution):
        for j in range(resolution):
            grid_point = np.array([xv[i, j], yv[i, j]])
            voronoi_grid[i, j] = find_closest_point(points, grid_point)
    
    return voronoi_grid

def plot_voronoi_diagram(voronoi_grid, points, grid_size):
    plt.imshow(voronoi_grid, extent=(0, grid_size, 0, grid_size), origin='lower', cmap='tab20')
    plt.colorbar()
    plt.title('Voronoi Diagram')
    plt.show()

# Parameters
num_points = 200
grid_size = 1
resolution = 200

# Generate points and create Voronoi diagram
points = generate_random_points(num_points, grid_size)

voronoi_grid = create_voronoi_diagram(points, grid_size, resolution)

# Plot the Voronoi diagram
plot_voronoi_diagram(voronoi_grid, points, grid_size)