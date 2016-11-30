module servoMountLock()
{
  space=[0.5, 0.5, 0.5];
  difference()
  {
    translate([-14-5, -10-10, 0])
      cube([2*(14+5), 2*(10+10), 4.5]);
    // screw holes
    for(dx = [-1, +1])
      for(dy = [-1, +1])
        translate([dx*14, dy*10, -2])
          cylinder(r=(3+1)/2, $fs=1.5, h=4.5+4);
    translate([0, 0, 1])
    {
      // main rod mounting hole
      translate([-(7.5+space[0])/2, -(30+space[1])/2, 4.5-(2+space[2])])
        cube([7.5, 30, 2] + space);
      // center, thicker part
      translate([-(10+space[0])/2, -(10+space[1])/2, 4.5-(3.5+space[2])])
        cube([10, 10, 3.5] + space);
    }
    // servo's screw space
    translate([0, 0, -1])
      cylinder(r=(9+1)/2, h=6, $fs=1);
  }
}

for(i=[0:1])
  translate([0, i*45, 0])
    servoMountLock();
