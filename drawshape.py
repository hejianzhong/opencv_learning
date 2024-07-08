import cv2
import numpy as np


def mouse_callback(event, x, y, flags, user_data):
    print(event, x, y, flags, user_data)


curshape = 0

if __name__ == "__main__":
    window_name = "window"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 640, 480)

    img = np.zeros((480, 640, 3), dtype=np.uint8)
    cv2.setMouseCallback(window_name, mouse_callback, "123")
    while True:
        cv2.imshow(window_name, img)
        key = cv2.waitKey(10)
        if key & 0xff == ord("q"):
            break
        elif key & 0xff == ord("r"):
            curshape = 0
        elif key & 0xff == ord("l"):
            curshape = 1
        elif key & 0xff == ord("c"):
            curshape = 2
