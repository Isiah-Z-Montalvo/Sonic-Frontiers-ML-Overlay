import time
import multiprocessing
from PIL import ImageGrab

def takeScreenshot():
	bounds = (0, 143, 2736, 1683)
	count = 0
	time.sleep(5)
	
	while True:
		screenshot = ImageGrab.grab(bounds)
		screenshot = screenshot.resize((1333, 800))
		screenshot.save("D:\\Sonic-Frontiers-Dataset\\SonicFrontiers (" + str(count) + ").jpg")
		count += 1
		time.sleep(1)

if __name__ == '__main__': 
	function = multiprocessing.Process(target = takeScreenshot, name = "TakeScreenshot")
	function.start()

	time.sleep(31163)

	function.terminate()
	function.join()