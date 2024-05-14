from PIL import Image
import numpy as np

img = Image.open('voronoi.bmp')
rgb_img = img.convert('L')
array = np.array(rgb_img)

print(array)