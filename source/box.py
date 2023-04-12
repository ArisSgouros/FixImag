import sys
import numpy as np

class Box:
   def __init__(self):
      self.size = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
      self.orig = np.array([0.0, 0.0, 0.0])
      self.vec = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
      self.bounds = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0],[0.0, 0.0, 0.0]])
      self.xlo = 0.0
      self.ylo = 0.0
      self.zlo = 0.0
      self.xhi = 0.0
      self.yhi = 0.0
      self.zhi = 0.0
      self.lx = 0.0
      self.ly = 0.0
      self.lz = 0.0
      self.xy = 0.0
      self.xz = 0.0
      self.yz = 0.0
      return
   def FromVec(self, vec, orig):
      if vec[0][1] > 0.0 or vec[0][2] > 0.0 or vec[1][2] > 0.0:
         print("Box::FromVec: unsupported vector:\n", vec)
         sys.exit
      self.lx = vec[0][0]
      self.ly = vec[1][1]
      self.lz = vec[2][2]
      self.xy = vec[1][0]
      self.xz = vec[2][0]
      self.yz = vec[2][1]
      self.xy -= self.lx*round(self.xy/self.lx)
      self.xz -= self.lx*round(self.xz/self.lx)
      self.yz -= self.ly*round(self.yz/self.ly)

      self.xlo = orig[0]
      self.ylo = orig[1]
      self.zlo = orig[2]
      self.xhi = self.xlo + self.lx
      self.yhi = self.ylo + self.ly
      self.zhi = self.zlo + self.lz
      self.Recompute()
      return
   def FromBound(self, xlo, xhi, ylo, yhi, zlo, zhi, xy, xz, yz):
      self.xlo = xlo
      self.ylo = ylo
      self.zlo = zlo
      self.xhi = xhi
      self.yhi = yhi
      self.zhi = zhi
      self.xy = xy
      self.xz = xz
      self.yz = yz
      self.lx = xhi - xlo
      self.ly = yhi - ylo
      self.lz = zhi - zlo
      self.Recompute()
      return
   def Recompute(self):
      self.size = np.array([[ self.lx , self.xy , self.xz ], \
                            [ 0.0, self.ly , self.yz ], \
                            [ 0.0, 0.0, self.lz]])

      self.orig = np.array([self.xlo, self.ylo, self.zlo])

      self.vec = np.array([[ self.lx, 0.0, 0.0 ], \
                           [ self.xy, self.ly , 0.0 ], \
                           [ self.xz, self.yz , self.lz  ]])
      self.bounds = np.array([[self.xlo + min(0.0,self.xy,self.xz,self.xy+self.xz), self.xhi + max(0.0,self.xy,self.xz,self.xy+self.xz), self.xy], \
                             [self.ylo + min(0.0,self.yz),                         self.yhi + max(0.0,self.yz),                         self.xz], \
                             [self.zlo,                                            self.zhi,                                            self.yz]])
      return
