#!/usr/bin/env python
import time
import serial


class LineDriver:
    def __init__(self, dev, timeout = 0.250):
        self._io = serial.Serial(port=dev, baudrate=38400, timeout=0)
        if not self._io.isOpen():
            raise Expception("cannot open serial port: " + dev)
        self._timeout = timeout

    def sendCmd(self, cmd):
        self._io.write(cmd + "\n")

    def readResponse(self):
        return self.__readLine()

    def __readLine(self):
        deadline = time.time() + self._timeout
        line = ''
        while time.time() <= deadline:
            c = self._io.read(1)
            if c == '\r' or c == '\n':
                return line
            line += c
        raise Exception("timeout whilre reading from serial port")


# set [-1; +1] range to servo position
class Position:
    def __init__(self, line, panLine, tiltLine):
        self._line     = line
        self._panLine  = panLine
        self._tiltLine = tiltLine


    def set(self, pan, tilt):
        self.__set(self._panLine, pan)
        self.__set(self._tiltLine, tilt)

    def __set(self, axis, value):
        self._line.sendCmd( axis + 's' + self.__value2hex(value) + '?' )
        resp = self._line.readResponse()
        if resp != axis + "-ok":
            raise Exception("error response from servo controler: " + resp)

    def __value2hex(self, value):
        if value < -1.0 or 1.0 < value:
            raise Exception("value '" + str(value) + "' out of [-1; +1] range")
        norm = (value+1.0)/2 * 255;
        i    = int( round(norm, 0) )
        return "%0.2x" % i
