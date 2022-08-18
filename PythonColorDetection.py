# import the necessary packages
import numpy as np
import cv2
# load the image
image = cv2.imread("yolll4.jpg")
# define the list of boundaries
boundaries = [
	([191, 191, 191],[255, 255, 255]), 
	([86, 31, 4], [220, 88, 50]),
	([0, 57, 77], [77, 207, 255]), 
	([103, 86, 65], [145, 133, 128])
]

#sarı [0, 162, 186], [46, 242, 255] unutma
#sol koyu sağ açık
#[0, 57, 77], [77, 207, 255] loş ortamda görsel1.jpg
#[37, 119, 167], [163, 208, 235] aydınlık ortamda --görsel11.jpg
#bize verilen kod [247, 181, 0] --ters
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
