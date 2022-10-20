if color_search == "green" or color_search == "Green":
    cv2.imshow("Green Mask", green_mask)
    cv2.imshow("Green", green)

    greenOverlay = cv2.bitwise_not(green)
    cv2.imshow("green overlay", greenOverlay)

    cv2.imshow("red", red1)
    redOverlay = cv2.bitwise_not(red1)
    cv2.imshow("red overlay", redOverlay)

    withGreenOverlay = cv2.bitwise_and(image, greenOverlay)
    withBothOverlays = cv2.bitwise_and(withGreenOverlay, redOverlay)

    #cv2.imshow("final", withBothOverlays)

    image[green_mask > 0] = (255, 0, 0)
    image[gray_mask > 0] = (255, 0, 0)
    image[purple_mask > 0] = (255, 0, 0)

    image[red1_mask > 0] = (0, 0, 255)
    image[red2_mask > 0] = (0, 0, 255)
    cv2.imshow("red Mask", image)



    image[green_mask > 0] = (255, 255, 255)
    image[gray_mask > 0] = (255, 255, 255)
    image[purple_mask > 0] = (255, 255, 255)

    image[red1_mask > 0] = (0, 0, 0)
    image[red2_mask > 0] = (0, 0, 0)
    cv2.imshow("final", image)