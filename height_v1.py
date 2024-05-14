from PIL import Image
import numpy as np

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

def get_neighbor_colors_for_province(image_array, target_color):
    height, width = image_array.shape()
    
    target_pixels = np.where((image_array == target_color))
    target_pixels = list(zip(target_pixels[0], target_pixels[1]))

    neighbor_colors = []
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for pixel in target_pixels:
        y, x = pixel
        for direction in directions:
            ny, nx = y + direction[0], x + direction[1]
            if 0 <= ny < height and 0 <= nx < width:
                neighbor_color = image_array[ny, nx]
                if neighbor_color != target_color:
                    neighbor_colors.append(neighbor_color)
    
    return neighbor_colors

def get_neighborlists():
    coordinateToProvinceMapping = getCoordinateToProvinceMapping()
    neighborList = []
    
    for i in range(200):
        neighborList.append([])
    
    for color in range(256):
        if (color not in coordinateToProvinceMapping.keys()):
            continue
        neighbor_provinces = get_neighbor_colors_for_province(getCoordinates(), color)
        neighborList[coordinateToProvinceMapping[color]] = neighbor_provinces
        
    return neighborList

neighborList = get_neighborlists()