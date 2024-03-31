import shutil
import os
import random

oldPath = "D:\Sonic-Frontiers-Dataset"
newPath = "D:\Sonic-Frontiers-Subset"
values = []
for i in range(5000):
	element = random.randrange(0, len(os.listdir(oldPath)) - 1)
	while element in values:
		element = random.randrange(0, len(os.listdir(oldPath)) - 1)
	image = os.listdir(oldPath)[element]
	opath = os.path.join(oldPath, image)
	npath = os.path.join(newPath, image)
	shutil.move(opath, npath)
	values.append(element)