import time
import multiprocessing
from PIL import ImageGrab

def takeScreenshot():
	bounds = (450, 0, 3000, 1440)
	count = 0
	time.sleep(5)
	
	while True:
		screenshot = ImageGrab.grab(bounds)
		#screenshot = screenshot.resize((1333, 800))
		screenshot.save("E:\\Sonic-Frontiers-Dataset\\SonicFrontiers(" + str(count) + ").jpg")
		count += 1
		time.sleep(1)

if __name__ == '__main__': 
	function = multiprocessing.Process(target = takeScreenshot, name = "TakeScreenshot")
	function.start()

	time.sleep(40850)

	function.terminate()
	function.join()