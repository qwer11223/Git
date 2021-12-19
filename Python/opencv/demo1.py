from cv2 import cv2 as cv


def faceDetect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier(
        'opencv-4.5.3-openvino-2021.4.2/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 255, 0), thickness=2)
    cv.imshow('face', img)


img = cv.imread('face2.jpeg')
img = cv.resize(img,(1200,700))
faceDetect(img)

# 获取摄像头
# cap = cv.VideoCapture(0)

while True:
    # flag, frame = cap.read()
    # if flag:
    #     faceDetect(frame)
    # else:
    #     break

    if ord('q') == cv.waitKey(0):
        break

cap.release()
cv.destroyAllWindows()
