use <bottomMount.scad>
use <servoMountLock.scad>
use <tiltMountBase.scad>
use <cameraFrame.scad>

for(dy=[0,45])
  translate([0, dy, 0])
    servoMountLock();

translate([0, -45, 0])
  tiltMountBase();

translate([-73, -52, 0])
  rotate([0, 0, 180])
    bottomMount();

for(dy=[0, 50])
  translate([-95, -30+dy, 0])
    cameraFrame();
