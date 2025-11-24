import cv2 

fc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
ec = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cp = cv2.VideoCapture(0)
if not cp.isOpened():
    print("Error")
    exit()

while True:
    rt, fr = cp.read()
    if not rt:
        break

    gy = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)

    fs = fc.detectMultiScale(gy, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in fs:
        cv2.rectangle(fr, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rg = gy[y:y + h, x:x + w]
        rc = fr[y:y + h, x:x + w]

        es = ec.detectMultiScale(rg)

        for (ex, ey, ew, eh) in es:
            cv2.rectangle(rc, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    cv2.imshow('Detector', fr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cp.release()
cv2.destroyAllWindows()