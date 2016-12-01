use <servo.scad>

module base()
{
  // main suport elements
  for(rot=[-45, +45])
    rotate([0, 0, rot])
      translate([-180/2, -30/2, 0])
        cube([180, 30, 3]);
  // side screw mounts
  difference()
  {
    for(dy=[-(20+1+3+2), 20+1])
      translate([-40/2, dy, 0])
        cube([40, 3+2, 3+26]);
    // screw-access cut-in
    translate([-25/2, -60/2, 3+26-4-10])
      cube([25, 60, 10]);
    // screw holes
    #for(dx=[-1, +1])
      for(dy=[-1, +1])
        translate([dx*5, dy*23.5, 22])
          cylinder(r=(3+1)/2, h=10, $fs=1);
  }
}

base();

%translate([20/2, -40/2, 3])
  rotate([0,0,90])
    servo();
