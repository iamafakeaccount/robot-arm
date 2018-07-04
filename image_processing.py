import numpy as np
import cv2

# Setting up framework for determining radius of skittles

def load_image(filepath):
	 return cv2.imread(filepath)

def convert_hsv(frame=None):
	return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

def GaussianBlur(frame=None):
	return cv2.blur(frame, (10, 10))

def binary_thresholding(frame=None):
	#implement this
	return None

def find_circles(frame=None):
	circles = None

	# Tweak these parameters
	circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=40, maxRadius=100)
	return circles

if __name__ == "__main__":
	filepath = "/home/cswain/Documents/skittles.jpg"
	img = load_image(filepath)
	hsv_img = convert_hsv(img)

	cv2.imshow("img", img)
	cv2.waitKey(0)
	# cv2.imshow(hsv_img)

	cv2.destroyAllWindows()