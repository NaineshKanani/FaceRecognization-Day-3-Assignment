import cv2

cap = cv2.VideoCapture(0)
image = cv2.imread("Bckground.jpg")
while True:
    flag, frame = cap.read()
    if not flag:
        print("Could not access the camera")
        break

    image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
    blended_image = cv2.addWeighted(frame, 0.7, image, 0.3, gamma=0.1)
    cv2.imshow("Blended Frame", blended_image)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()