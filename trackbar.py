import cv2
import numpy as np


def trackbar_callback(input):
    pass

if __name__ == "__main__":

    window_name = "trackbar"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)
    img = np.zeros((480, 640, 3), np.uint8)

    cv2.createTrackbar("R", window_name, 0, 255, lambda x: None)
    cv2.createTrackbar("G", window_name, 0, 255, trackbar_callback)
    cv2.createTrackbar("B", window_name, 0, 255, trackbar_callback)

    while True:
        channel_r = cv2.getTrackbarPos("R", window_name)
        channel_g = cv2.getTrackbarPos("G", window_name)
        channel_b = cv2.getTrackbarPos("B", window_name)

        img[:] = [channel_b, channel_g, channel_r]
        cv2.imshow(window_name, img)

        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()