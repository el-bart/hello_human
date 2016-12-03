use <servoMountLock.scad>

module tiltMountBase()
{
  difference()
  {
    translate([-14-5, -10-10, 0])
      cube([2*(14+5), 2*(10+10), 4]);
    // screw holes
    for(dx = [-1, +1])
      for(dy = [-1, +1])
        translate([dx*14, dy*10, -2])
          cylinder(r=(3+1)/2, $fs=1.5, h=4+4);
    // servo's screw space
    translate([0, 0, -1])
      cylinder(r=(9+1)/2, h=6, $fs=1);
  }
  // screw mounting field
  difference()
  {
    translate([-(2*(14+5))/2, -7, 4])
      cube([2*(14+5), 2, 15]);
    // screws
    for(dx=[-10, +10])
      translate([dx, -4, 10])
        rotate([90, 0, 0])
          cylinder(r=(3+1)/2, h=4, $fs=1);
    
  }
}

tiltMountBase();

%translate([0, 0, -0.5])
  rotate([180, 0, 0])
    servoMountLock();
