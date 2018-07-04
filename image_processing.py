import numpy as np
import cv2

# Setting up framework for determining radius of skittles

def loadImage(filepath):
	 return cv2.imread(filepath)

def convertHSV(frame=None):
	return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

def GaussianBlur(frame=None):
	return cv2.blur(frame, (10, 10))

# Not currently being used.
def BinaryThreshold(frame=None):
	ret, thresh = cv2.threshold(frame, 127, 255, cv2.THRESH_BIN) # Use THRESH_TRUN?
	return thresh

def findCircles(frame=None):
	circles = None

	# Tweak these parameters
	circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=40, maxRadius=100)
	return circles


if __name__ == "__main__":

	filepath = "/home/cswain/Documents/skittles.jpg"
	img = loadImage(filepath)
	
	# Convert from BGR color channels to HSV
	hsv_img = convertHSV(img)

	# Split HSV image into different color channels
	h, s, v = cv2.split(hsv_img)

	# Apply Gaussian Blur to value
	smooth_img = GaussianBlur(s)

	circles = findCircles(smooth_img)

	print("There are: " + str(len(circles[0])) + " circles.")
	print("There are 26 skittles in the image")

	if circles.any():
		for i in circles[0,:]:
			# Draw outer circle
			cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 4)

			#Draw center of circle
			cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 4)

	# Resize images to fit on screen
	img = cv2.resize(img, (0,0), None, .25, .25) 
	s = cv2.resize(s, (0,0), None, .25, .25)
	smooth_img = cv2.resize(smooth_img, (0,0), None, .25, .25)

	# Can't concatenate img because it has 3 color dimensions
	horizontal_img_concat = np.concatenate((s, smooth_img), axis=1) 

	cv2.imshow("Original photo", img)
	cv2.imshow("Horizontal Concatenation", horizontal_img_concat)
	cv2.waitKey(0)
	# cv2.imshow(hsv_img)

	cv2.destroyAllWindows()