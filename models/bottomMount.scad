use <servo.scad>
use <servoMountLock.scad>
use <cammera.scad>
use <tiltMountBase.scad>
use <cameraFrame.scad>

module bottomMount()
{
  // base
  difference()
  {
    // main board
    translate([-50, -20, 0])
      cube([2*50, 30+10, 2]);
    // hole for servo's mount screw
    translate([0,0,-1])
      cylinder(r=5/2+1, $fs=1.5, h=4);
    // holes
    for(dx=[-1,1])
      for(dy=[-1,1])
        translate([dx*14, dy*10, -1])
          cylinder(r=(3+1)/2, $fs=1.5, h=4);
  }

  // side wall for
  difference()
  {
    // wall
    translate([-50, -20, 0])
      cube([5, 53+2*3, 40]);
    // holes
    for(dz=[-5, 5])
      for(dy=[3, 3+47])
        translate([-50-1, -20+dy, 30+1+dz])
          rotate([0, 90, 0])
            cylinder(r=(3+1)/2, $fs=1.5, h=7);
    // place for servo motor
    translate([-50-1, -20+3+3, 30-10])
      cube([7, 40+1, 20+1]);
  }

  // side wall's anty-vibration support
  // TODO...
}


bottomMount();

%translate([-71, -13.5, 21])
{
  rotate([0,90,0])
    rotate([0,0,90])
    {
      servo();
      translate([13/2+3.5, 20/2, 36+3.2])
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

%translate([10, -10, -44])
  rotate([0,0,90])
  {
    servo();
    translate([13/2+3.5, 20/2, 36+3.2])
      rotate([0, 0, 90])
        servoMountLock();
  }
