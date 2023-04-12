import numpy as np

def MinImagOrth(rr, LL):
   return np.array([ rr[0] - LL[0][0]*round(rr[0]/LL[0][0]), \
                     rr[1] - LL[1][1]*round(rr[1]/LL[1][1]), \
                     rr[2] - LL[2][2]*round(rr[2]/LL[2][2]) ])


def MinImag(rr, LL):
   rr_cor = np.array([ rr[0] - LL[0][1]*round(rr[1]/LL[1][1]) - LL[0][2]*round(rr[2]/LL[2][2]), \
                       rr[1] - LL[1][2]*round(rr[2]/LL[2][2]), \
                       rr[2] ])
   return MinImagOrth(rr_cor, LL)
