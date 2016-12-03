module cameraFrame()
{
  difference()
  {
    cube([42+2*14, 36+2*5, 2]);
    // center window
    translate([((42+2*14)-(43-6))/2, ((36+2*5)-36)/2, 0])
      cube([43-6, 36, 2]);
    // mount holes
    translate([42+2*14, 36+2*5, 0]/2)
      for(dx=[-1, +1])
        for(dy=[-1, +1])
          translate([dx*((42+2*14)/2-5), dy*(36/2-8), -1])
            cylinder(r=(3+1)/2, h=2+2, $fs=1);
  }
  // support shelfs
  for(dy=[0, 36+2*5-4.5])
    translate([0, dy, 2])
      cube([42+2*14, 4.5, 1.5]);
  
}


for(i=[0:1])
  translate([0, i*48, 0])
    cameraFrame();
