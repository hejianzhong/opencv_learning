import cv2

if __name__ == "__main__":
    window_name, trackbar_name = "color", "curcolor"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    im = cv2.imread("./data/img/lena.png")

    color_space = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA,
                   cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL,
                   cv2.COLOR_BGR2YUV]
    cv2.createTrackbar(trackbar_name, window_name, 0, len(color_space) - 1, lambda x:None)

    while True:
        v = cv2.getTrackbarPos(trackbar_name, window_name)

        cvt_img = cv2.cvtColor(im, color_space[v])
        cv2.imshow(window_name, cvt_img)
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()