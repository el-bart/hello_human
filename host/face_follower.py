#!/usr/bin/env python
import sys
import cv2
import Servo
import Tracker

def drawRectangles(faces, img):
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0xff,0), 6)

def imageCenter(img):
    h,w,channels = img.shape
    return (w/2, h/2)

lineDrv  = Servo.LineDriver('/dev/ttyUSB0')
position = Servo.Position(lineDrv, 'l', 'f')
tracker  = Tracker.Tracker(position)


faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frameGrabber = cv2.VideoCapture(0)

ret    = 0
errors = 0

while True:
    try:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, img = frameGrabber.read()
        gray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        center   = imageCenter(img)
        faces    = faceDetector.detectMultiScale(gray, 1.3, 5)
        drawRectangles(faces, img)
        cv2.imshow('Video', img)

        tracker.updatePositionForFaces(faces, center)
        sys.stderr.write('#')
        errors = 0

    except Exception as ex:
        raise                       
        errors += 1
        sys.stderr.write('!')
        sys.stderr.write( "\n" + sys.argv[0] + ": ERROR: " + str(ex) + "\n" )
        if errors > 20:
            sys.stderr.write("\n" + sys.argv[0] + ": TOO MANY ERRORS IN A ROW - SHUTTING DOWN...\n")
            ret = 42
            break

sys.stderr.write('\n')
frameGrabber.release()
cv2.destroyAllWindows()
sys.exit(ret)
