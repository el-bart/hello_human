#!/usr/bin/env python
import sys
import cv2
import time
import getopt
import Servo
import Tracker


def parseCmdLine():
    opts, args = getopt.getopt(sys.argv[1:], "hpns:v:", ["help", "preview", "no-preview", "serial=", "video="])
    if len(args) > 0:
        raise Exception("unknown argument: '" + args[0] + "'")
    preview = None
    serialDevice = None
    videoDevice = None
    for opt, arg in opts:
        if opt == "-h" or opt == "--help":
            sys.stdout.write(sys.argv[0] + " --video /dev/videoX --serial /dev/ttyUSBY {--help|--preview|--no-preview}\n")
            sys.exit(0)
        if opt == "-p" or opt == "--preview":
            preview = True
            continue
        if opt == "-n" or opt == "--no-preview":
            preview = False
            continue
        if opt == "-s" or opt == "--serial":
            serialDevice = arg
            continue
        if opt == "-v" or opt == "--video":
            videoDevice = arg
            continue
    if preview is None:
        raise Exception("preview must be explicitly enabled or disabled")
    if serialDevice is None:
        raise Exception("serial device name must be xplicitly provided")
    if videoDevice is None:
        raise Exception("video device name must be xplicitly provided")
    return preview, serialDevice, videoDevice


def drawRectangles(faces, img):
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0xff,0), 6)

def imageCenter(img):
    h,w,channels = img.shape
    return (w/2, h/2)

previewWindow, serialDevice, videoDevice = parseCmdLine()

lineDrv = Servo.LineDriver(serialDevice)
position = Servo.Position(lineDrv, 'l', 'f')
tracker = Tracker.Tracker(position)
fullscreen = False


faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
frameGrabber = cv2.VideoCapture( int(videoDevice[-1]) )

if previewWindow:
    if fullscreen:
        cv2.namedWindow("preview", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("preview", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    else:
        cv2.namedWindow("preview", cv2.WINDOW_NORMAL)

ret    = 0
errors = 0
frameCount = 0
lastFpsPrint = time.time();

while True:
    try:
        frameCount += 1
        if frameCount > 20:
            now = time.time()
            timeElapsed = now - lastFpsPrint
            sys.stderr.write('\nFPS=' + str(frameCount / float(timeElapsed)) + '\n')
            frameCount = 0
            lastFpsPrint = now

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        ret, img = frameGrabber.read()
        gray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        center   = imageCenter(img)
        faces    = faceDetector.detectMultiScale(gray, 1.3, 5)
        if previewWindow:
            drawRectangles(faces, img)
            cv2.imshow("preview",img)

        tracker.updatePositionForFaces(faces, center)
        sys.stderr.write('#')
        errors = 0

    except Exception as ex:
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
