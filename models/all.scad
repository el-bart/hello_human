use <servoMountLock.scad>
use <tiltMountBase.scad>

for(dy=[0,45])
  translate([0, dy, 0])
    servoMountLock();

translate([0, -45, 0])
  tiltMountBase();

