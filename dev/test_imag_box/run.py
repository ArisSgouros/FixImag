import numpy as np
import sys
sys.path.append("../../source/")
from box import Box
from evaluate import Run

# instantiate Box objects
box_init = Box()
box_last = Box()

# orth coord
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
ri        = np.array([ 0.0, 0.0,  0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
dr        = np.array([ 0.0, 50.5, 0.0])
remap     = False
steps     = 1
case_name = "1.orth_coord"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)

# tri coord
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
ri        = np.array([ 0.0 , 0.0 , 0.0 ])
rj        = np.array([ 0.0 , 14.0, 0.0 ])
dr        = np.array([ 25.0, 25.0, 0.0 ])
remap     = False
steps     = 1
case_name = "2.tri_coord"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)

# orth deform remap no
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 20.0, 0.0, 10.0, 0.0, 0.0, 0.0)
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
dr        = np.array([ 0.0, 0.0 , 0.0])
steps     = 1
remap     = False
case_name = "3.orth_deform_remap_no"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)

# orth deform remap yes
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 20.0, 0.0, 10.0, 0.0, 0.0, 0.0)
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
dr        = np.array([ 0.0, 0.0 , 0.0])
steps     = 1
remap     = True
case_name = "4.orth_deform_remap_yes"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)

# tri deform remap no
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
dr        = np.array([ 0.0, 0.0 , 0.0])
steps     = 1
remap     = False
case_name = "5.tri_deform_remap_no"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)

# tri deform remap yes
box_init.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
box_last.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
dr        = np.array([ 0.0, 0.0 , 0.0])
steps     = 1
remap     = True
case_name = "6.tri_deform_remap_yes"
Run(box_init, box_last, ri, rj, dr, steps, remap, case_name)
