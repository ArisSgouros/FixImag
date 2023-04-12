import sys
import copy as cp
import numpy as np
from imag import MinImag
from box import Box
from def_grad import DeformGradAnalyt
from export import ExportSnapshot

def ExportLog(step, ri, rj, rr_abs, rr_min, rr_fix, vv, LL, fmt):
   fmt_all = (fmt + " ") * 34
   string = fmt_all %(step, ri[0], ri[1], ri[2], \
                      rj[0], rj[1], rj[2], \
                      rr_abs[0], rr_abs[1], rr_abs[2], np.linalg.norm(rr_abs), \
                      rr_min[0], rr_min[1], rr_min[2], np.linalg.norm(rr_min), \
                      rr_fix[0], rr_fix[1], rr_fix[2], np.linalg.norm(rr_fix), \
                      vv[0][0], vv[0][1], vv[0][2], \
                      vv[1][0], vv[1][1], vv[1][2], \
                      vv[2][0], vv[2][1], vv[2][2], \
                      LL[0][0], LL[1][1], LL[2][2], LL[0][1], LL[0][2], LL[1][2] )
   return string

def Run(box, box_def, ri, rj, dr, steps, remap, case_name):

   # Set the filenames
   file_log     = case_name + ".log"
   dump_min_log = case_name + "_min.lammpstrj"
   dump_fix_log = case_name + "_fix.lammpstrj"

   # Deal with the displacement rate
   dr_step      = dr / steps

   # Store the reference lengths
   ri_ref       = cp.deepcopy(ri)
   rj_ref       = cp.deepcopy(rj)
   box_ref      = cp.deepcopy(box)

   # Calculate the deformation gradient and strain rate
   def_grad     = DeformGradAnalyt(box_ref.vec, box_def.vec)
   strain_tens  = def_grad - np.identity(3)
   strain_rate  = strain_tens / steps

   # Calculate the initial seperation vector and min imag
   rr_abs       = rj - ri
   rr_min       = MinImag(rr_abs, box.size)
   rr_shift_ref = rr_min - rr_abs
   rr_shift     = rr_min - rr_abs
   rr_fix       = rr_abs + rr_shift

   # Export initial log to case file
   string = ExportLog(0, ri, rj, rr_abs, rr_min, rr_fix, box.vec, box.size, '%-7.4f')
   foo = open(file_log,"w")
   foo.write(string+"\n")

   # Print initial log to screen
   print(string + " " + case_name)

   with open("table1.csv", "a") as fileobj:
      fileobj.write("%7.3f,%7.3f," % (strain_tens[1][1], strain_tens[0][1]))
      fileobj.write("%7.3f,"*5 % (box.ly, box.xy, np.linalg.norm(rr_abs), np.linalg.norm(rr_min), np.linalg.norm(rr_fix)))

   # Export initial snapshots
   ExportSnapshot(box.bounds, [np.array([0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([10.0, 0.0, 0.0])], dump_min_log, 'w') # dummy snapshot
   ExportSnapshot(box.bounds, [np.array([0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), np.array([10.0, 0.0, 0.0])], dump_fix_log, 'w') # dummy snapshot
   ExportSnapshot(box.bounds, [ri, ri + rr_min, rj], dump_min_log, 'a')
   ExportSnapshot(box.bounds, [ri, ri + rr_fix, rj], dump_fix_log, 'a')

   # Conduct the test
   for step in range(1, steps+1):

      # Apply displacement
      rj += dr_step

      # Apply box deformation
      def_grad_step = strain_rate*step + np.identity(3)
      box_vec_def   = np.array( [def_grad_step.dot(box_ref.vec[ii]) for ii in range(3)] )
      box.FromVec(box_vec_def, box_ref.orig)

      # Remap if specified
      if remap:
         ri       = def_grad_step.dot(ri_ref)
         rj       = def_grad_step.dot(rj_ref)
         rr_shift = def_grad_step.dot(rr_shift_ref)

      # Calculate the separation vector
      rr_abs = rj - ri
      rr_min = MinImag(rr_abs, box.size)
      rr_fix = rr_abs + rr_shift

      # Export logs and snapshots
      string = ExportLog(step, ri, rj, rr_abs, rr_min, rr_fix, box.vec, box.size, '%-7.4f')
      foo.write(string+"\n")
      ExportSnapshot(box.bounds, [ri, ri + rr_min, rj], dump_min_log, 'a')
      ExportSnapshot(box.bounds, [ri, ri + rr_fix, rj], dump_fix_log, 'a')
   foo.close()

   # Print last log to screen
   print(string + " " + case_name)

   with open("table1.csv", "a") as fileobj:
      fileobj.write("%7.3f,"*5 % (box.ly, box.xy, np.linalg.norm(rr_abs), np.linalg.norm(rr_min), np.linalg.norm(rr_fix)))
      fileobj.write("%7s\n" % (case_name))

   return
