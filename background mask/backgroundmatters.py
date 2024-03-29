import cv2
import numpy as np

cap = cv2.VideoCapture(0)

image = cv2.imread("image.jpg")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    l_black = np.array([0, 0, 0])
    u_black = np.array([50, 50, 50])

    mask = cv2.inRange(frame, l_black, u_black)

    masked_frame = np.where(mask[:, :, np.newaxis] == 0, frame, image)

    cv2.imshow('Real Video', frame)
    cv2.imshow('Masked Video', masked_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()