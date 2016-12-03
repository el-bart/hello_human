use <servo.scad>

module __holder()
{
  l = 20+20;
  t = 2;
  difference()
  {
    union()
    {
      cube([l, 7.5, t]);
      rotate([90, 0, 0])
        cube([l, 20, t]);
    }
    // vertival drills
    for(dx=[-1, +1])
      translate([l/2 + dx*5, 7.5/2, -2])
        cylinder(r=(3+1)/2, h=5, $fs=1);
    // horizontal drills
    for(dx=[-1, +1])
      translate([l/2 + dx*15, 1, 15])
        rotate([90, 0, 0])
          cylinder(r=(3+1)/2, h=5, $fs=1);
  }
}

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
    for(dy=[-(20+1+3+3.5), 20+0.5])
      translate([-40/2, dy, 0])
        cube([40, 3+4, 3+15]);
    // screw holes
    for(dx=[-1, +1])
      for(dy=[-1, +1])
        translate([dx*15, dy*25+8, 14])
          rotate([90, 0, 0])
            cylinder(r=(3+1)/2, h=15, $fs=1);
    // some extra space for cables
    translate([-(20+2)/2, -60/2, 3])
      cube([20+2, 60, 15]);
  }
  %translate([-20, 27.5, 29])
    rotate([180, 0, 0])
      __holder();
  %translate([20, -27.5, 29])
    rotate([0, 0, 180])
      rotate([180, 0, 0])
        __holder();
}

base();

for(i=[0:1])
  translate([-20, 50+i*15, 0])
    __holder();


%translate([20/2, -40/2, 3])
  rotate([0,0,90])
    servo();
