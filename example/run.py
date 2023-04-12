import numpy as np
import sys
sys.path.append("../source/")
from box import Box
from evaluate import Run

# Write the header of table 1
with open("table_1.csv", "w") as foo:
   fmt = "%-s,"*15
   foo.write(fmt % ("A/A"   , "eyy"    , "exy"       , "domain"    , "coord"     , \
                    "Ly_ref", "Dxy_ref", "rr_abs_ref", "rr_min_ref", "rr_fix_ref", \
                    "Ly"    , "Dxy"    , "rr_abs"    , "rr_min"    , "rr_fix"    ,))
   foo.write("\n")

# instantiate a Box object
box = Box()

# orth coord
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri          = np.array([ 0.0, 0.0,  0.0])
rj          = np.array([ 0.0, 12.5, 0.0])
remap_box   = False
remap_point = True
steps       = 100
case_name   = "A"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri coord
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 4.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri          = np.array([ 0.0, 0.0,  0.0])
rj          = np.array([ 0.0, 12.5, 0.0])
remap_box   = False
remap_point = True
steps       = 100
case_name   = "B"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# orth deform remap no
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 12.5, 0.0])
steps     = 100
remap_box   = True
remap_point = False
case_name = "C"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# orth deform remap yes
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 0.0, 0.0],[0.0,1.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 12.5, 0.0])
steps     = 100
remap_box   = True
remap_point = True
case_name = "D"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri deform remap no
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 1.0, 0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 12.5, 0.0])
steps     = 100
remap_box   = True
remap_point = False
case_name = "E"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)

# tri deform remap yes
box.FromBound(0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 0.0, 0.0)
strain_tensor = np.array([[0.0, 1.0, 0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])
ri        = np.array([ 0.0, 0.0 , 0.0])
rj        = np.array([ 0.0, 12.5, 0.0])
steps     = 100
remap_box   = True
remap_point = True
case_name = "F"
Run(box, ri, rj, strain_tensor, steps, remap_box, remap_point, case_name)
