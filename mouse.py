import cv2
import numpy as np


def mouse_callback(event, x, y, flags, user_dat):
    print(event, x, y, flags, user_dat)


if __name__ == "__main__":
    window_name = "mouse"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 360)
    cv2.setMouseCallback(window_name, mouse_callback, "123")

    trackbar_name = "trackbar"
    cv2.createTrackbar(trackbar_name, window_name, 10, 100, lambda x:None)
    print(cv2.getTrackbarPos(trackbar_name, window_name))

    img = np.zeros((360, 640, 3), dtype=np.uint8)
    while True:
        cv2.imshow("mouse", img)
        key = cv2.waitKey(1)
        if key & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()
