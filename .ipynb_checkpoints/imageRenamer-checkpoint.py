import os

path = "D:\Sonic-Frontiers-Dataset"
count = 1
for image in os.listdir(path):
	fileName = os.path.join(path, image)
	file = "SonicFrontiers" + str(count) + ".jpg"
	newFileName = os.path.join(path, file)
	os.rename(fileName, newFileName)
	count += 1