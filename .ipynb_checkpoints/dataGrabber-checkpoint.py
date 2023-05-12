import time
import psutil
from PIL import ImageGrab

bounds = (440, 0, 3000, 1440)
imgs = []

while "SonicFrontiers.exe" in (i.name() for i in psutil.process_iter()):
	screenshot = ImageGrab.grab(bounds)
	imgs.append(screenshot)
	time.sleep(1)

imgs[5].save("SonicFrontiers.jpg")