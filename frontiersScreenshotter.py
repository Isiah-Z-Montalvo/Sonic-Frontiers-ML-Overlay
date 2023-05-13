import time
import psutil
from PIL import ImageGrab

bounds = (440, 0, 3000, 1440)
count = 0
while "SonicFrontiers.exe" in (i.name() for i in psutil.process_iter()):
	screenshot = ImageGrab.grab(bounds)
	screenshot.save("E:\\Sonic-Frontiers-Dataset\\SonicFrontiers" + str(count) + ".jpg")
	count += 1
	time.sleep(1)