# importing packages
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt
import PIL
from sklearn.cluster import KMeans


def show_img_compar(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10,10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') 
    ax[1].axis('off')
    f.tight_layout()
    plt.show(block = False)

def palette(clusters):
    width=300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_): 
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette

def color_palette(image):
    clt50 = KMeans(n_clusters = 50)
    clt = KMeans(n_clusters = 5)
    clt_1 = clt.fit((image.reshape(-1, 3)))
    clt_2 = clt50.fit((image.reshape(-1, 3)))
    palImg = cv2.cvtColor(palette(clt_1), cv2.COLOR_BGR2RGB)
    color_data = clt50.cluster_centers_
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # show_img_compar(image, palImg)
    return(color_data)
 
def read_file():
    file = open('colorData.txt','r')
    named_list = []
    for line in file:
        line = line.strip()
        line = line.split(", ")
        line[4], line[5] = line[5], line[4]
        named_list.append(line)
    # print(named_list)
    return(named_list)

def color_compare(data):
    named_list = read_file()
    compare_list = []

    RdiffTotal = 0
    GdiffTotal = 0
    BdiffTotal = 0

    for col in data:
        diff_list = []
        pic_b = int(col[0])
        pic_g = int(col[1])
        pic_r = int(col[2])
        for color in named_list:
            diff = 0
            Rdiff = abs(pic_r - int(color[3]))
            diff += Rdiff
            if Rdiff > RdiffTotal:
                RdiffTotal = Rdiff

            Gdiff = abs(pic_g - int(color[4]))
            diff += Gdiff
            if Gdiff > GdiffTotal:
                GdiffTotal = Gdiff

            Bdiff = abs(pic_b - int(color[5]))
            diff += Bdiff
            if Bdiff > BdiffTotal:
                BdiffTotal = Bdiff


            diff_list.append(diff)
        diff = min(diff_list)
        # print(diff)
        index = diff_list.index(diff)
        # print(index)
        category = named_list[index][0]
        name = named_list[index][1]
        hex = named_list[index][2]
        r_named = int(named_list[index][3])
        g_named = int(named_list[index][4])
        b_named = int(named_list[index][5])
        compare_list.append([category, name, hex, r_named, g_named, b_named])
    val = 1
    for cols in compare_list:
        #print("%i. Name: %s, Hex Value: %s, R: %i, G: %i, B: %i, Category: %s" % (val, cols[1], cols[2], cols[3], cols[4], cols[5], cols[0]))
        val += 1
    return compare_list, RdiffTotal, GdiffTotal, BdiffTotal          # [category, name, hex, r-val, g-val, b-val]
    
def color_extrapolate(image, data):
    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 1
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
    
def getColorDisability():



    return


def main():
    # constructing and using arugment parse (chpt. 3)
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to image")
    args = vars(ap.parse_args())

    # loading image
    image = cv2.imread(args["image"])
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("Original", image)
    # cv2.waitKey(0)

    # assigning and masking color 1
    # converting to HSV colorspace
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)                            # converting image to the HSV color space (chpt. 6)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
   
    data = color_palette(image)
    print(data)
    frequent_data, RdiffTotal, GdiffTotal, BdiffTotal = color_compare(data)
    
    #color_extrapolate(image, data)

    blackFiltered = blueFiltered = greenFiltered = redFiltered = brownFiltered = orangeFiltered = violetFiltered = whiteFiltered = yellowFiltered = cv2.imread(args["image"])

    for color in frequent_data:
        print(color)
        if color[0] == "Shades of Black and Gray (see also Gray vs Grey)":
            offset = 25

            low_black = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_black = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            black_mask = cv2.inRange(image, low_black, high_black)
            black = cv2.bitwise_and(image, image, mask = black_mask)
            #cv2.imshow("Black Mask", black_mask)
            #cv2.imshow("Black", black)
            #cv2.waitKey(0)
            
            blackFiltered[black_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Blue":
            offset = 75

            low_blue = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_blue = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            blue_mask = cv2.inRange(image, low_blue, high_blue)
            blue = cv2.bitwise_and(image, image, mask = blue_mask)
            #cv2.imshow("Blue Mask", blue_mask)
            #cv2.imshow("Blue", blue)
            #cv2.waitKey(0)
            
            blueFiltered[blue_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Green":
            offset = 60

            low_green = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_green = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            green_mask = cv2.inRange(image, low_green, high_green)
            green = cv2.bitwise_and(image, image, mask = green_mask)
            #cv2.imshow("Green Mask", green_mask)
            #cv2.imshow("Green", green)
            #cv2.waitKey(0)
            
            greenFiltered[green_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Red":
            offset = 100

            low_red = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_red = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            red_mask = cv2.inRange(image, low_red, high_red)
            red = cv2.bitwise_and(image, image, mask = red_mask)
            #cv2.imshow("Red Mask", red_mask)
            #cv2.imshow("Red", red)
            #cv2.waitKey(0)
            
            redFiltered[red_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Brown":
            offset = 90

            low_brown = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_brown = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            brown_mask = cv2.inRange(image, low_brown, high_brown)
            brown = cv2.bitwise_and(image, image, mask = brown_mask)
            #cv2.imshow("Brown Mask", brown_mask)
            #cv2.imshow("Brown", brown)
            #cv2.waitKey(0)
            
            brownFiltered[brown_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Orange":
            offset = 100

            low_orange = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_orange = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            orange_mask = cv2.inRange(image, low_orange, high_orange)
            orange = cv2.bitwise_and(image, image, mask = orange_mask)
            #cv2.imshow("Orange Mask", orange_mask)
            #cv2.imshow("Orange", orange)
            #cv2.waitKey(0)
            
            orangeFiltered[orange_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of Violet":
            offset = 50

            low_violet = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_violet = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            violet_mask = cv2.inRange(image, low_violet, high_violet)
            violet = cv2.bitwise_and(image, image, mask = violet_mask)
            #cv2.imshow("Violet Mask", violet_mask)
            #cv2.imshow("Violet", violet)
            #cv2.waitKey(0)
            
            violetFiltered[violet_mask > 0] = (0, 0, 0)
        elif color[0] == "Shades of White":
            offset = 50

            low_white = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_white = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            white_mask = cv2.inRange(image, low_white, high_white)
            white = cv2.bitwise_and(image, image, mask = white_mask)
            #cv2.imshow("White Mask", white_mask)
            #cv2.imshow("White", white)
            #cv2.waitKey(0)
            
            whiteFiltered[white_mask > 0] = (0, 0, 0)
        """
        elif color[0] == "Shades of Yellow":
            offset = 100

            low_yellow = np.array([int(color[3]) - offset, int(color[4]) - offset, int(color[5]) - offset])
            print(color[3], color[4], color[5])
            high_yellow = np.array([int(color[3]) + offset, int(color[4]) + offset, int(color[5]) + offset])
            yellow_mask = cv2.inRange(image, low_yellow, high_yellow)
            yellow = cv2.bitwise_and(image, image, mask = yellow_mask)
            cv2.imshow("Yellow Mask", yellow_mask)
            cv2.imshow("Yellow", yellow)
            cv2.waitKey(0)
            
            yellowFiltered[yellow_mask > 0] = (0, 0, 0)
        """
    cv2.imshow("Black Filter", blackFiltered)
    cv2.imshow("Blue Filter", blueFiltered)
    cv2.imshow("Green Filter", greenFiltered)
    cv2.imshow("Red Filter", redFiltered)
    cv2.imshow("Brown Filter", brownFiltered)
    cv2.imshow("Orange Filter", orangeFiltered)
    cv2.imshow("Violet Filter", violetFiltered)
    cv2.imshow("White Filter", whiteFiltered)
    cv2.imshow("Red Filter", redFiltered)
    cv2.waitKey(0)

    print(RdiffTotal, BdiffTotal, GdiffTotal)

main()