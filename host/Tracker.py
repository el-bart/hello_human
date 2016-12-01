#!/usr/bin/env python
import time
import serial

class Tracker:
    def __init__(self, pos):
        self.__pos  = pos
        self.__pan  = 0.0
        self.__tilt = 0.0
        self.__silentPeriodEnd = time.time()
        # some "constants" (read: hardcodes)
        self.__inactivity = 0.35    # give some time for camera to steady, after each move
        self.__centeredRange = 50   # that many pixels between ROI and an image center is considered "ok"
        # TODO...
        self.__setPosition(self.__pan, self.__tilt)

    def updatePositionForFaces(self, faces, center):
        now = time.time()
        if self.__silentPeriodEnd > now:
            return
        p,   t = self.__findNewROI(faces, center)
        dp, dt = self.__positionToMotionOffset(center, p, t)
        self.__updatePosition(dp, dt)
        self.__silentPeriodEnd = now + self.__inactivity

    def __findNewROI(self, faces, center):
        face = self.__findBiggestFace(faces)
        if face is None:
            return center
        (x,y,w,h) = face
        print "\n " + str(x) + " ; " + str(y) + "\n"                    
        return (x+w/2, y+h/2)

    def __findBiggestFace(self, faces):
        if len(faces) < 1:
            return None
        out = None
        for (x,y,w,h) in faces:
            if out is None or self.__faceSize((x,y,w,h)) > self.__faceSize(out):
                out = (x,y,w,h)
        return out

    def __faceSize(self, face):
        x,y,w,h = face
        return w*h


    def __positionToMotionOffset(self, center, p, t):
        # TODO: translate position on the image, to servo offset
        return (0.0, 0.0)

    def __updatePosition(self, dp, dt):
        self.__setPosition( self.__pan + dp, self.__tilt + dt )

    def __setPosition(self, pan, tilt):
        return                              
        self.__pan  = self.__normalizePan(pan)
        self.__tilt = self.__normalizeTilt(tilt)
        self.__pos.set(self.__pan, self.__tilt)

    def __normalizePan(self, pan):
        # TODO: verify
        if pan > 0.9:
            return 0.9
        if pan < -0.9:
            return -0.9
        return pan

    def __normalizeTilt(self, tilt):
        # TODO: verify
        if tilt > 0.4:
            return 0.4
        if tilt < -0.2:
            return -0.2
        return tilt
