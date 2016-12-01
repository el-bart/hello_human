#!/usr/bin/env python
import sys
import cv2
import Servo

def drawRectangles(faces, img):
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0xff,0), 6)

def centerROI(faces):
    return (100,100)

lineDrv  = LineDriver('/dev/ttyUSB0')
position = Position(lineDrv, 'l', 'f')


faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frameGrabber = cv2.VideoCapture(0)

while True:
    try:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sys.stderr.write('#')

        ret, img = frameGrabber.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.3, 5)
        # TODO: move camera
        position.set(+0.15, +0.5)                       
        drawRectangles(faces, img)
        cv2.imshow('Video', img)
    except Exception as ex:
        sys.stderr.write('!')
        sys.stderr.write( "\n" + sys.argv[0] + ": ERROR: " + str(ex) + "\n" )

sys.stderr.write('\n')
video_capture.release()
cv2.destroyAllWindows()
