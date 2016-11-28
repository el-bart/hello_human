use <servo.scad>

module bottomMount()
{
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
  rotate([0,90,0])
    rotate([0,0,90])
      servo();
