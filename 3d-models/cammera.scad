module cammera()
{
  cube([43, 1, 34.5]);
  translate([43/2, 0, 34.5/2])
    rotate([90, 0, 0])
      cylinder(r=14.5/2, h=22);
  translate([(43-12)/2, 1])
    cube([12, 15, 4.5]);
}

cammera();
