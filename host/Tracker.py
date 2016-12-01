#!/usr/bin/env python
import math
import time
import serial

class Tracker:
    def __init__(self, pos):
        self.__pos  = pos
        self.__pan  = 0.0
        self.__tilt = -0.2
        self.__silentPeriodEnd = time.time()
        # some "constants" (read: hardcodes)
        self.__inactivity = 0.21            # give some time for camera to steady, after each move
        self.__centeredRange = 50           # that many pixels between ROI and an image center is considered "ok"
        self.__panPix2OffCoef  = 0.1/160    # how mux pan-servo should move per 1 pixel change
        self.__tiltPix2OffCoef = 0.1/160    # how mux tilt-servo should move per 1 pixel change
        # setup some initial positions
        self.__setPosition(self.__pan, self.__tilt)

    def updatePositionForFaces(self, faces, center):
        now = time.time()
        if now < self.__silentPeriodEnd:
            return
        p, t = self.__findNewROI(faces, center)
        if self.__alreadyCentered(p,t, center):
            #print "\nalready centered"              
            return
        #print "\nNOT centered"              
        dp, dt = self.__positionToMotionOffset(center, p, t)
        self.__updatePosition(dp, dt)
        self.__silentPeriodEnd = now + self.__inactivity

    def __findNewROI(self, faces, center):
        face = self.__findBiggestFace(faces)
        if face is None:
            return center
        (x,y,w,h) = face
        #print "\n " + str(x) + " ; " + str(y) + " (" + str(center) + ")\n"                    
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

    def __alreadyCentered(self, p,t, center):
        dx = center[0] - p
        dy = center[1] - t
        distance = math.sqrt( dx*dx + dy*dy )
        #print( "dist: " + str(distance) )                   
        return distance <= self.__centeredRange

    def __positionToMotionOffset(self, center, p, t):
        dpPix = p - center[0]
        dtPix = t - center[1]
        return (dpPix*self.__panPix2OffCoef, dtPix*self.__tiltPix2OffCoef)

    def __updatePosition(self, dp, dt):
        self.__setPosition( self.__pan + dp, self.__tilt + dt )

    def __setPosition(self, pan, tilt):
        print("\nsetting: \t" + str(pan) + " ; \t" + str(tilt) )             
        #return                              
        self.__pan  = self.__normalizePan(pan)
        self.__tilt = self.__normalizeTilt(tilt)
        self.__pos.set(self.__pan, -1*self.__tilt)

    def __normalizePan(self, pan):
        # TODO: verify
        if pan > 0.9:
            return 0.9
        if pan < -0.9:
            return -0.9
        return pan

    def __normalizeTilt(self, tilt):
        if tilt > 0.1:
            return 0.1
        if tilt < -0.4:
            return -0.4
        return tilt
