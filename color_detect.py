# importing packages
import numpy as np
import argparse
import cv2

# constructing and using arugment parse (chpt. 3)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())

# loading image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# cv2.waitKey(0)

# converting to HSV colorspace
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)                            # converting image to the HSV color space (chpt. 6)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Green 
low_green = np.array([36, 50, 70])             
high_green = np.array([89, 255, 255])            
green_mask = cv2.inRange(hsv, low_green, high_green)
green = cv2.bitwise_and(image, image, mask = green_mask)
#cv2.imshow("Green Mask", green_mask)
#cv2.imshow("Green", green)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Red 1
low_red1 = np.array([159, 50, 70])             
high_red1 = np.array([180, 255, 255])            
red1_mask = cv2.inRange(hsv, low_red1, high_red1)
red1 = cv2.bitwise_and(image, image, mask = red1_mask)
#cv2.imshow("Red 1 Mask", red1_mask)
#cv2.imshow("Red 1", red1)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Red 2
low_red2 = np.array([0, 50, 70])             
high_red2 = np.array([9, 255, 255])            
red2_mask = cv2.inRange(hsv, low_red2, high_red2)
red2 = cv2.bitwise_and(image, image, mask = red2_mask)
#cv2.imshow("Red 2 Mask", red2_mask)
#cv2.imshow("Red 2", red2)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Blue
low_blue = np.array([90, 50, 70])             
high_blue = np.array([128, 255, 255])            
blue_mask = cv2.inRange(hsv, low_blue, high_blue)
blue = cv2.bitwise_and(image, image, mask = blue_mask)
#cv2.imshow("Blue Mask", blue_mask)
#cv2.imshow("Blue", blue)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking White
low_white = np.array([0, 0, 231])             
high_white = np.array([180, 18, 255])            
white_mask = cv2.inRange(hsv, low_white, high_white)
white = cv2.bitwise_and(image, image, mask = white_mask)
#cv2.imshow("White Mask", white_mask)
#cv2.imshow("White", white)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Black
low_black = np.array([180, 255, 30])             
high_black = np.array([0, 0, 0])            
black_mask = cv2.inRange(hsv, low_black, high_black)
black = cv2.bitwise_and(image, image, mask = black_mask)
#cv2.imshow("Black Mask", black_mask)
#cv2.imshow("Black", black)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Yellow
low_yellow = np.array([25, 50, 70])             
high_yellow = np.array([35, 255, 255])            
yellow_mask = cv2.inRange(hsv, low_yellow, high_yellow)
yellow = cv2.bitwise_and(image, image, mask = yellow_mask)
#cv2.imshow("Yellow Mask", yellow_mask)
#cv2.imshow("Yellow", yellow)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Purple
low_purple = np.array([129, 50, 70])             
high_purple = np.array([158, 255, 255])            
purple_mask = cv2.inRange(hsv, low_purple, high_purple)
purple = cv2.bitwise_and(image, image, mask = purple_mask)
#cv2.imshow("Purple Mask", purple_mask)
#cv2.imshow("Purple", purple)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Orange
low_orange = np.array([10, 50, 70])             
high_orange = np.array([24, 255, 255])            
orange_mask = cv2.inRange(hsv, low_orange, high_orange)
orange = cv2.bitwise_and(image, image, mask = orange_mask)
#cv2.imshow("Orange Mask", orange_mask)
#cv2.imshow("Orange", orange)

#-------------------------------------------------------------------------------------------------------------------------------#
# assigning and masking Gray
low_gray = np.array([0, 0, 40])             
high_gray = np.array([180, 18, 230])            
gray_mask = cv2.inRange(hsv, low_gray, high_gray)
gray = cv2.bitwise_and(image, image, mask = gray_mask)
#cv2.imshow("Gray Mask", gray_mask)
#cv2.imshow("Gray", gray)

#-------------------------------------------------------------------------------------------------------------------------------#
# user input (THIS PART DOESN'T WORK AND IDK WHY...ONLY SHOWS GREEN)
#"""
color_search = input(str("What color are you looking for: "))
print(color_search)

if color_search == "green" or color_search == "Green":
    cv2.imshow("Green Mask", green_mask)
    cv2.imshow("Green", green)
elif color_search == "red" or  color_search == "Red":
    cv2.imshow("Red 1 Mask", red1_mask)
    cv2.imshow("Red 1", red1)
elif color_search == "red" or  color_search == "Red":
    cv2.imshow("Red 2 Mask", red2_mask)
    cv2.imshow("Red 2", red2)
elif color_search == "blue" or  color_search == "Blue":
    cv2.imshow("Blue Mask", blue_mask)
    cv2.imshow("Blue", blue)
elif color_search == "black" or  color_search == "Black":
    cv2.imshow("Black Mask", black_mask)
    cv2.imshow("Black", black)
elif color_search == "white" or color_search == "White":
    cv2.imshow("White Mask", white_mask)
    cv2.imshow("White", white)
elif color_search == "yellow" or color_search == "Yellow":
    cv2.imshow("Yellow Mask", yellow_mask)
    cv2.imshow("Yellow", yellow)
elif color_search == "purple" or color_search == "Purple":  
    cv2.imshow("Purple Mask", purple_mask)
    cv2.imshow("Purple", purple)
elif color_search == "orange" or  color_search == "Orange":
    cv2.imshow("Orange Mask", orange_mask)
    cv2.imshow("Orange", orange)
elif color_search == "gray" or  color_search == "Gray":
    cv2.imshow("Gray Mask", gray_mask)
    cv2.imshow("Gray", gray)
#"""

cv2.waitKey(0)
