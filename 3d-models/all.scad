use <bottomMount.scad>
use <servoMountLock.scad>
use <tiltMountBase.scad>
use <cameraFrame.scad>

use <servo.scad>
use <cammera.scad>


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


%translate([0, 100, 0])
{
  bottomMount();

  translate([-71, -13.5, 21])
  {
    rotate([0,90,0])
      rotate([0,0,90])
      {
        servo();
        translate([13/2+3.5, 20/2, 36+3.2-0.5])
          rotate([0, 0, 90])
            servoMountLock();
      }
    translate([50, 10, -7])
    {
      translate([13, 0, 0])
        cammera();
      translate([-1, 2, -6])
        rotate([90, 0, 0])
          cameraFrame();
      translate([70-1, -5, -6])
        rotate([90, 0, 180])
          cameraFrame();
    }
    translate([44, 10, 10])
      rotate([0, 90, 0])
        tiltMountBase();
  }

  translate([10, -10, -44])
    rotate([0,0,90])
    {
      servo();
      translate([13/2+3.5, 20/2, 36+3.2-0.5])
        rotate([0, 0, 90])
          servoMountLock();
    }
}
