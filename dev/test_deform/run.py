import sys
import numpy as np
from numpy.random import rand

sys.path.append("../../source/")
from box import Box
from grid import GenerateGrid
from export import ExportSnapshot
from def_grad import DeformGradGen, DeformGradConstraint, DeformGradAnalyt

export_name = "0.test_deform.lammpstrj"

box_init = Box()
box_last = Box()

#                  xlo xhi  yho yhi  zlo zhi  xy  yz  yz
box_init.FromBound(0., 10., 0., 10., 0., 10., 0., 0., 0.)
box_last.FromBound(0., 10., 0., 10., 0., 10., 5., -6., 2.)

print("\nCreate two boxes:")
print("   Box_init edge vector:")
for ii in box_init.vec:
   print("      ", ii)
print("   Box_last edge vector:")
for ii in box_last.vec:
   print("      ", ii)

n_point = [5, 5, 5]
print("\nPopulate the boxes with a particle grid:")
print("   ", n_point)
points1 = GenerateGrid(box_init.vec, box_init.orig, n_point)
points2 = GenerateGrid(box_last.vec, box_last.orig, n_point)

print("\nExport Snapshots of init and last box")
ExportSnapshot(box_init.bounds, points1, export_name, 'w')
ExportSnapshot(box_last.bounds, points2, export_name, 'a')

print("\nCompute the deformation gradient with different schemes:")
def_grad_gen        = DeformGradGen(box_init.vec, box_last.vec)
def_grad_constraint = DeformGradConstraint(box_init.vec, box_last.vec)
def_grad_analyt     = DeformGradAnalyt(box_init.vec, box_last.vec)

print("   generic:")
for ii in def_grad_gen:
   print("      ", ii)
print("   constraint:")
for ii in def_grad_constraint:
   print("      ", ii)
print("   analytical:")
for ii in def_grad_analyt:
   print("      ", ii)

print("\nEdge vector of box_init after the deformation:")
box_init_vec_deform   = np.array( [def_grad_gen.dot(box_init.vec[ii]) for ii in range(3)] )
for ii in box_init_vec_deform:
   print("      ", ii)

if not np.isclose(def_grad_gen, def_grad_constraint).all():
   print("   def_grad_gen != def_grad_constraint")
if not np.isclose(def_grad_gen, def_grad_analyt).all():
   print("   def_grad_gen != def_grad_analyt")
if not np.isclose(box_last.vec, box_init_vec_deform).all():
   print("   box_init.vec after deform != box_last.vec")

print("\nApply the deformation gradient to box_init grid")
points2_def = []
for ii in range(len(points1)):
   aux = def_grad_analyt.dot(points1[ii])
   points2_def.append(aux)
   if not np.isclose(points2[ii], points2_def[ii]).all():
      print(points2[ii], points2_def[ii])
      print("   box_init.vec after deform != box_last.vec")

print("\nExport Snapshot of init box after deformation")
ExportSnapshot(box_last.bounds, points2_def, export_name, 'a')
