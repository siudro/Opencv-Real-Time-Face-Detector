import cv2

face_cascade = cv2.CascadeClassifier('<PATH>/haarcascade_frontalface_default.xml')
# put the exact path for the haarcascade_frontalface_default.xml file between <>
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    ret, img = webcam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(imgGray, 2, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        face_gray = imgGray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]

    cv2.imshow('Face Detector', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()