module servoMountLock()
{
  difference()
  {
    translate([-14-5, -10-10, 0])
      cube([2*(14+5), 2*(10+10), 4.5]);
    // screw holes
    for(dx = [-1, +1])
      for(dy = [-1, +1])
        translate([dx*14, dy*10, -2])
          cylinder(r=(3+1)/2, $fs=1.5, h=4.5+4);
    // main rod mounting hole
    translate([-(7.5+1)/2, -(30+1)/2, 4.5-(2+0.5)])
      cube([7.5+1, 30+1, 2+0.5]);
    // center, thicker part
    translate([-(10+1)/2, -(10+1)/2, 4.5-(3.5+0.5)])
      cube([10+1, 10+1, 3.5+0.5]);
    translate([0, 0, -1])
      cylinder(r=(9+1)/2, h=6, $fs=0.0);
  }
}

for(i=[0:1])
  translate([0, i*45, 0])
    servoMountLock();
