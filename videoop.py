import cv2


fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("./data/video/hello.avi", fourcc, 25, (640, 480))
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("video", frame)
        writer.write(frame)
        key = cv2.waitKey(10)
        if (key & 0xff) == ord("q"):
            break

cap.release()
writer.release()
cv2.destroyAllWindows()
