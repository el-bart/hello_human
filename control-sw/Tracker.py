#!/usr/bin/env python
import math
import time
import serial

class Tracker:
    def __init__(self, pos):
        self.__pos  = pos
        self.__pan  = 0.0
        self.__tilt = 0.0
        self.__silentPeriodEnd = time.time()
        self.__lastFace        = time.time()
        # some "constants" (read: hardcodes)
        self.__inactivity = 0.00            # give some time for camera to steady, after each move
        self.__centeredRange = 20           # that many pixels between ROI and an image center is considered "ok"
        self.__panPix2OffCoef  = 0.02/160    # how mux pan-servo should move per 1 pixel change
        self.__tiltPix2OffCoef = 0.02/160    # how mux tilt-servo should move per 1 pixel change
        self.__backToStartAfterNoFaces = 7  # timeout for no faces, before returning to a default position
        # and finally... ;)
        self.__moveToDefaultPosition()

    def updatePositionForFaces(self, faces, center):
        now = time.time()
        if now < self.__silentPeriodEnd:
            return
        p, t = self.__findNewROI(faces, center)
        if self.__tooLongWithoutFaces():
            self.__moveToDefaultPosition()
            return
        if self.__alreadyCentered(p,t, center):
            return
        dp, dt = self.__positionToMotionOffset(center, p, t)
        self.__updatePosition(dp, dt)
        self.__silentPeriodEnd = now + self.__inactivity

    def __moveToDefaultPosition(self):
        self.__setPosition(0.0, -0.2)
        self.__lastFace = time.time()

    def __findNewROI(self, faces, center):
        face = self.__findBiggestFace(faces)
        if face is None:
            return center
        self.__lastFace = time.time()
        (x,y,w,h) = face
        return (x+w/2, y+h/2)

    def __findBiggestFace(self, faces):
        if len(faces) < 1:
            return None
        out = faces[0]
        for (x,y,w,h) in faces:
            if out is None or self.__faceSize((x,y,w,h)) > self.__faceSize(out):
                out = (x,y,w,h)
        return out

    def __faceSize(self, face):
        x,y,w,h = face
        return w*h

    def __tooLongWithoutFaces(self):
        return self.__lastFace + self.__backToStartAfterNoFaces < time.time()

    def __alreadyCentered(self, p,t, center):
        dx = center[0] - p
        dy = center[1] - t
        distance = math.sqrt( dx*dx + dy*dy )
        return distance <= self.__centeredRange

    def __positionToMotionOffset(self, center, p, t):
        dpPix = p - center[0]
        dtPix = t - center[1]
        return (dpPix*self.__panPix2OffCoef, dtPix*self.__tiltPix2OffCoef)

    def __updatePosition(self, dp, dt):
        self.__setPosition( self.__pan + dp, self.__tilt + dt )

    def __setPosition(self, pan, tilt):
        pp = self.__normalizePan(pan)
        pt = self.__normalizeTilt(tilt)
        retries = 3
        while True:
            try:
                self.__pos.set(pp, -1*pt)
                break
            except:
                retries -= 1
                if retries == 0:
                    raise

        self.__pan  = pp
        self.__tilt = pt

    def __normalizePan(self, pan):
        if pan > 0.8:
            return 0.8
        if pan < -0.8:
            return -0.8
        return pan

    def __normalizeTilt(self, tilt):
        if tilt > 0.1:
            return 0.1
        if tilt < -0.4:
            return -0.4
        return tilt
