.SECONDARY:

SCADS  += bottomMount.scad
SCADS  += servoMountLock.scad
SCADS  += tiltMountBase.scad
SCADS  += cameraFrame.scad
SCADS  += base.scad
SCADS  += all.scad
STLS   := $(wildcard *.stl) $(SCADS:.scad=.stl)
GCODES := $(STLS:.stl=.gcode)
CONFIG := $(wildcard *.ini)

.PHONY: all
all: $(GCODES)

$(STLS) $(SCADS) $(GCODES): Makefile $(CONFIG)

%.gcode: %.stl
	slic3r --load "$(CONFIG)" "$<"

%.stl: %.scad
	openscad -o "$@" "$<"

.PHONY: clean
clean:
	rm -fv $(GCODES) $(SCADS:.scad=.stl)
