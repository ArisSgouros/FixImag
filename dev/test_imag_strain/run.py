import numpy as np
import sys
sys.path.append("../../source/")
from box import Box
from evaluate import Run

# instantiate a Box object
box = Box()

# orth coord
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,50.5/14.0,0.0],[0.0,0.0,0.0]])
ri          = np.array([ 0.0, 0.0,  0.0])
rj          = np.array([ 0.0, 14.0, 0.0])
remap_box   = False
remap_point = True
steps       = 1
case_name   = "1.orth_coord"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri coord
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 25.0/14.0, 0.0],[0.0,25.0/14.0,0.0],[0.0,0.0,0.0]])
ri          = np.array([ 0.0, 0.0,  0.0])
rj          = np.array([ 0.0, 14.0, 0.0])
remap_box   = False
remap_point = True
steps       = 1
case_name   = "2.tri_coord"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# orth deform remap no
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
steps     = 1
remap_box   = True
remap_point = False
case_name = "3.orth_deform_remap_no"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# orth deform remap yes
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
steps     = 1
remap_box   = True
remap_point = True
case_name = "4.orth_deform_remap_yes"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri deform remap no
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.4, 0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
steps     = 1
remap_box   = True
remap_point = False
case_name = "5.tri_deform_remap_no"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri deform remap yes
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.4, 0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 14.0, 0.0])
steps     = 1
remap_box   = True
remap_point = True
case_name = "6.tri_deform_remap_yes"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)
