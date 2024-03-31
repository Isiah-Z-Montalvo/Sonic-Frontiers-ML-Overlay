import os
from PIL import Image

path = "D:\Sonic-Frontiers-Dataset-Images"
count = 1
for image in os.listdir(path):
	originalImage = Image.open(os.path.join(path, image))
	width, height = originalImage.size
	
	x = 0.37 * width
	y = 0.40 * height
	x2 = x + 700
	y2 = y + 700

	croppedImage = originalImage.crop((x, y, x2, y2))

	croppedImage.save("D:\\Sonic-Frontiers-Dataset\\SonicFrontiers(" + str(count) + ").jpg")
	count += 1
