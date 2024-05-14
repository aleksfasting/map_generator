import numpy as np
from PIL import Image
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

def create_voronoi_diagram(points, resolution=500):
    voronoi_grid = np.zeros((resolution, resolution))
    x = np.linspace(0, 1, resolution)
    y = np.linspace(0, 1, resolution)
    xv, yv = np.meshgrid(x, y)
    
    for i in range(resolution):
        for j in range(resolution):
            grid_point = np.array([xv[i, j], yv[i, j]])
            voronoi_grid[i, j] = find_closest_point(points, grid_point)
    
    return voronoi_grid

def plot_voronoi_diagram(voronoi_grid, points):
    plt.imshow(voronoi_grid, extent=(0, 1, 0, 1), origin='lower', cmap='tab20')
    plt.colorbar()
    plt.title('Voronoi Diagram')
    plt.show()

def create_varanoi():
    num_points = 200
    resolution = 200
    points = generate_random_points(num_points)

    voronoi_grid = create_voronoi_diagram(points, resolution)

    plot_voronoi_diagram(voronoi_grid, points)

def getCoordinates():
    img = Image.open('voronoi.bmp')
    return np.array(img)

def getCoordinateToProvinceMapping()->dict:
    array = getCoordinates()
    
    coordinateToProvince = {}

    provinceID = 0
    for row in array:
        for coordinate in row:
            if (coordinate in coordinateToProvince.keys()):
                continue
            coordinateToProvince[coordinate] = provinceID
            provinceID += 1
            
    return coordinateToProvince

def inverseMap(mapping: dict)->dict:
    return {v: k for k,v in mapping.items()}
    

def get_neighbors_for_province(array, target_ID, coordinateToProvinceMapping):
    height, width = array.shape
    
    target_pixels = np.where(array == inverseMap(coordinateToProvinceMapping)[target_ID])
    target_pixels = list(zip(target_pixels[0], target_pixels[1]))

    neighbor_IDs = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for pixel in target_pixels:
        y, x = pixel
        for direction in directions:
            ny, nx = y + direction[0], x + direction[1]
            if 0 <= ny < height and 0 <= nx < width:
                neighbor = coordinateToProvinceMapping[array[ny, nx]]
                if neighbor != target_ID and neighbor not in neighbor_IDs:
                    neighbor_IDs.append(neighbor)
    
    return neighbor_IDs

def get_neighborlists() -> list:
    coordinateToProvinceMapping = getCoordinateToProvinceMapping()
    neighborList = []
    
    for i in range(200):
        neighborList.append([])
    
    for ID in range(200):
        neighbor_provinces = get_neighbors_for_province(getCoordinates(), ID, coordinateToProvinceMapping)
        neighborList[ID] = neighbor_provinces
        
    return neighborList