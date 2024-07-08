import cv2

img = cv2.imread("data/img/dog.jpeg")
cv2.imshow("dog", img)

while 1 :
    key = cv2.waitKey(0)
    if key & 0xff == ord('q'):
        break
    elif key & 0xff == ord("s"):
        cv2.imwrite("data/img/dog_bck.jpeg", img)
    else:
        print(key)

cv2.destroyAllWindows()

