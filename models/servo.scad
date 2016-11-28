module servo()
{
  cube([40, 20, 36]);
  // mount shelf
  difference()
  {
    translate([-13/2, 0, 26])
      cube([53, 20, 3]);
    // holes
    #for(dx=[-1, +1])
      for(dy=[-1, +1])
        translate([53/2-13/2+dx*47/2, 20/2+dy*(6-1), 26-4])
          cylinder(r=4/2, $fs=1, h=10);
  }
  // rotor bottom
  translate([13/2+3.5, 20/2, 36])
  {
    cylinder(r=13/2, h=2);
    // rotor itself
    translate([0,0,2])
    {
      cylinder(r=9/2, h=2.5);
      // center part
      translate([-10/2, -10/2, 2.5])
      {
        cube([10, 10, 3.2]);
        // side bars
        translate([-10, (10-7.2)/2, 1.2])
          cube([30, 7.2, 2]);
      }
    }
  }
}

servo();
