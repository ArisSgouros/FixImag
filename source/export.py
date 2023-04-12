import numpy as np

def ExportSnapshot(bounds, points, filename, status):
   foo = open(filename, status)
   foo.write("ITEM: TIMESTEP\n")
   foo.write("0\n")
   foo.write("ITEM: NUMBER OF ATOMS\n")
   foo.write("%d\n" % (len(points)))
   foo.write("ITEM: BOX BOUNDS xy xz yz\n")
   foo.write("%f %f %f\n" % (bounds[0][0], bounds[0][1], bounds[0][2]))
   foo.write("%f %f %f\n" % (bounds[1][0], bounds[1][1], bounds[1][2]))
   foo.write("%f %f %f\n" % (bounds[2][0], bounds[2][1], bounds[2][2]))
   foo.write("ITEM: ATOMS id xu yu zu\n")
   id = 1
   for point in points:
      foo.write("%d %f %f %f\n" % (id, point[0], point[1], point[2]))
      id += 1
   return
