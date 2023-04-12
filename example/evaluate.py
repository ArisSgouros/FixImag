import sys
import copy as cp
import numpy as np
from imag import MinImag
from box import Box
from def_grad import DeformGradAnalyt
from export import ExportSnapshot

def Run(box, ri, rj, strain, steps, remap_box, remap_point, case_name):

   # Set the filenames
   data_csv     = case_name + ".csv"
   dump_min_log = case_name + "_min.lammpstrj"
   dump_fix_log = case_name + "_fix.lammpstrj"

   # Calculate the deformation gradient and strain rate
   strain_rate  = strain / steps
   def_grad     = strain + np.identity(3)

   # Calculate the initial seperation vector and min imag
   rr_abs       = rj - ri
   rr_min       = MinImag(rr_abs, box.size)
   rr_shift     = rr_min - rr_abs
   rr_fix       = rr_abs + rr_shift

   # Store the reference lengths
   ri_ref       = cp.deepcopy(ri)
   rj_ref       = cp.deepcopy(rj)
   box_ref      = cp.deepcopy(box)
   rr_shift_ref = cp.deepcopy(rr_shift)

   # Export initial log to case file
   with open(data_csv, "w") as foo:
      arg = ("step", \
              "exx"    , "eyy"    , "exy", \
              "rix"    , "riy"    ,  \
              "rjx"    , "rjy"    ,  \
              "rr_absx", "rr_absy",  "rr_abs", \
              "rr_minx", "rr_miny",  "rr_min", \
              "rr_fixx", "rr_fixy",  "rr_fix", \
              "v1x"    , "v1y"    ,  \
              "v2x"    , "v2y"    ,  \
              "Lx"     , "Ly"     , "Dxy")
      fmt = (case_name + "_%s,")*len(arg) + "\n"
      foo.write(fmt % arg)

      arg = (0, \
             0, 0, 0, \
             ri[0]    , ri[1]    , \
             rj[0]    , rj[1]    , \
             rr_abs[0], rr_abs[1], np.linalg.norm(rr_abs), \
             rr_min[0], rr_min[1], np.linalg.norm(rr_min), \
             rr_fix[0], rr_fix[1], np.linalg.norm(rr_fix), \
             box.vec[0][0] , box.vec[0][1] , \
             box.vec[1][0] , box.vec[1][1] , \
             box.lx, box.ly, box.xy)
      fmt = "%f,"*len(arg) + "\n"
      foo.write(fmt % arg)

   with open("table_1.csv", "a") as fileobj:
      fileobj.write("%-7s,%-7.3f,%-7.3f,%-7d,%-7d," % (case_name, strain[1][1], strain[0][1], int(remap_box), int(remap_point)))
      fileobj.write("%-7.3f,"*5 % (box.ly, box.xy, np.linalg.norm(rr_abs), np.linalg.norm(rr_min), np.linalg.norm(rr_fix)))

   # Export initial snapshots
   ExportSnapshot(box.bounds, [np.array([0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([10.0, 0.0, 0.0])], dump_min_log, 'w') # dummy snapshot
   ExportSnapshot(box.bounds, [np.array([0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([10.0, 0.0, 0.0])], dump_fix_log, 'w') # dummy snapshot
   ExportSnapshot(box.bounds, [ri, ri + rr_min, rj], dump_min_log, 'a')
   ExportSnapshot(box.bounds, [ri, ri + rr_fix, rj], dump_fix_log, 'a')

   # Conduct the test
   for step in range(1, steps+1):
      # Apply box deformation
      strain_step   = strain_rate*step
      def_grad_step = strain_step + np.identity(3)
      if remap_box:
         box_vec_def   = np.array( [def_grad_step.dot(box_ref.vec[ii]) for ii in range(3)] )
         box.FromVec(box_vec_def, box_ref.orig)
      if remap_point:
         ri       = def_grad_step.dot(ri_ref)
         rj       = def_grad_step.dot(rj_ref)
      if remap_box and remap_point:
         rr_shift = def_grad_step.dot(rr_shift_ref)

      # Calculate the separation vector
      rr_abs = rj - ri
      rr_min = MinImag(rr_abs, box.size)
      rr_fix = rr_abs + rr_shift

      # Export logs and snapshots
      with open(data_csv, "a") as foo:
         arg = (step, \
                strain_step[0][0], strain_step[1][1], strain_step[0][1], \
                ri[0]    , ri[1]    , \
                rj[0]    , rj[1]    , \
                rr_abs[0], rr_abs[1], np.linalg.norm(rr_abs), \
                rr_min[0], rr_min[1], np.linalg.norm(rr_min), \
                rr_fix[0], rr_fix[1], np.linalg.norm(rr_fix), \
                box.vec[0][0] , box.vec[0][1] , \
                box.vec[1][0] , box.vec[1][1] , \
                box.lx, box.ly, box.xy)
         fmt = " %-7.4f,"*len(arg) + "\n"
         foo.write(fmt % arg)

      ExportSnapshot(box.bounds, [ri, ri + rr_min, rj], dump_min_log, 'a')
      ExportSnapshot(box.bounds, [ri, ri + rr_fix, rj], dump_fix_log, 'a')

   with open("table_1.csv", "a") as fileobj:
      fileobj.write("%-7.3f,"*5 % (box.ly, box.xy, np.linalg.norm(rr_abs), np.linalg.norm(rr_min), np.linalg.norm(rr_fix)))
      fileobj.write("\n")

   return
