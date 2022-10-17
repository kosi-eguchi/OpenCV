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
    ax[0].axis('off') #hide the axis
    ax[1].axis('off')
    f.tight_layout()
    plt.show()


def palette(clusters):
    width=300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width/clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_): 
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette


def color_palette(image):
    clt = KMeans(n_clusters=5)
    clt_1 = clt.fit((image.reshape(-1, 3)))
    color_data = clt.cluster_centers_
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    palImg = cv2.cvtColor(palette(clt_1), cv2.COLOR_BGR2RGB)
    show_img_compar(image, palImg)
    return(color_data)


def read_file():
    file = open('color_data.txt','r')
    named_list = []
    for line in file:
        line = line.strip()
        line = line.split(", ")
        named_list.append(line)
    # print(named_list)
    return(named_list)

def color_compare(data):
    named_list = read_file()
    compare_list = []
    for col in data:
        # print(col)
        diff_r = 256
        diff_g = 256
        diff_b = 256
        name = ""
        hex = ""
        r_named = 256
        g_named = 256
        b_named = 256
        pic_b = int(col[0])
        pic_g = int(col[1])
        pic_r = int(col[2])
        for color in named_list:
            new_name = color[0]
            new_hex = color[1]
            new_r_named = int(color[2])
            new_g_named = int(color[3])
            new_b_named = int(color[4])
            new_diff_r = abs(pic_r - new_r_named)
            new_diff_g = abs(pic_g - new_g_named)
            new_diff_b = abs(pic_b - new_b_named)
            # print(new_r_named, new_g_named, new_b_named, new_diff_r, new_diff_g, new_diff_b)
            if new_diff_r <= diff_r and new_diff_g <= diff_g and new_diff_b <= diff_b:
                diff_r = new_diff_r
                diff_g = new_diff_g
                diff_b = new_diff_b
                r_named = new_r_named
                g_named = new_g_named
                b_named = new_b_named
                name = new_name
                hex = new_hex
        print("diff: %i, %i, %i" % (diff_r, diff_g, diff_b))
        print("named: %s, %s, %i, %i, %i" % (name, hex, r_named, g_named, b_named))
        compare_list.append([name, hex, r_named, g_named, b_named])
    print(compare_list)

            

def color_extrapolate(image, data):
    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 1
    # converting to HSV colorspace
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)                            # converting image to the HSV color space (chpt. 6)

    #-------------------------------------------------------------------------------------------------------------------------------#
    low1 = np.array([data[0][2] -  50, data[0][1] -  50, data[0][0] -  50])             
    high1 = np.array([data[0][2] +  50, data[0][1] +  50, data[0][0] +  50])             
    mask1 = cv2.inRange(hsv, low1, high1)
    extrapolate_color1 = cv2.bitwise_and(image, image, mask = mask1)
    cv2.imshow("Mask Color 1", mask1)
    cv2.imshow("One", extrapolate_color1)

    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 2
    low2 = np.array([data[1][2] -  50, data[1][1] -  50, data[1][0] -  50])             
    high2 = np.array([data[1][2] +  50, data[1][1] +  50, data[1][0] +  50])            
    mask2 = cv2.inRange(hsv, low2, high2)
    extrapolate_color2 = cv2.bitwise_and(image, image, mask = mask2)
    cv2.imshow("Mask Color 2", mask2)
    cv2.imshow("Two", extrapolate_color2)

    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 3
    low3 = np.array([data[2][2] -  50, data[2][1] -  50, data[2][0] -  50])             
    high3 = np.array([data[2][2] +  50, data[2][1] +  50, data[2][0] +  50])            
    mask3 = cv2.inRange(hsv, low3, high3)
    extrapolate_color3 = cv2.bitwise_and(image, image, mask = mask3)
    cv2.imshow("Mask Color 3", mask3)
    cv2.imshow("Three", extrapolate_color3)

    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 4
    low4 = np.array([data[3][2] -  50, data[3][1] -  50, data[3][0] -  50])              
    high4 = np.array([data[3][2] +  50, data[3][1] +  50, data[3][0] +  50])            
    mask4 = cv2.inRange(hsv, low4, high4)
    extrapolate_color4 = cv2.bitwise_and(image, image, mask = mask4)
    cv2.imshow("Mask Color 4", mask4)
    cv2.imshow("Four", extrapolate_color4)

    #-------------------------------------------------------------------------------------------------------------------------------#
    # assigning and masking color 5
    low5 = np.array([data[4][2] -  50, data[4][1] -  50, data[4][0] -  50])              
    high5 = np.array([data[4][2] +  50, data[4][1] +  50, data[4][0] + 50])            
    mask5 = cv2.inRange(hsv, low5, high5)
    extrapolate_color5 = cv2.bitwise_and(image, image, mask = mask5)
    cv2.imshow("Mask Color 5", mask5)
    cv2.imshow("Five", extrapolate_color5)

    #-------------------------------------------------------------------------------------------------------------------------------#
    """
    color_search = input(str("What color are you looking for: "))
    print(color_search)

    if color_search == "one" or color_search == "One":
        cv2.imshow("Mask Color 1", mask1)
        cv2.imshow("One", extrapolate_color1)
    elif color_search == "two" or  color_search == "Two":
        cv2.imshow("Mask Color 2", mask2)
        cv2.imshow("Two", extrapolate_color2)
    elif color_search == "three" or  color_search == "Three":
        cv2.imshow("Mask Color 3", mask3)
        cv2.imshow("Three", extrapolate_color3)
    elif color_search == "four" or  color_search == "Four":
        cv2.imshow("Mask Color 4", mask4)
        cv2.imshow("%s" % Four, extrapolate_color4)
    elif color_search == "five" or color_search == "Five":
        cv2.imshow("Mask Color 5", mask5)
        cv2.imshow("%s" % Five, extrapolate_color5)
    """
    cv2.waitKey(0)
    
def main():
    # constructing and using arugment parse (chpt. 3)
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to image")
    args = vars(ap.parse_args())

    # loading image
    image = cv2.imread(args["image"])
    cv2.imshow("Original", image)
    # cv2.waitKey(0)

    data = color_palette(image)
    print(data)
    color_compare(data)
    # color_extrapolate(image, data)

main()
