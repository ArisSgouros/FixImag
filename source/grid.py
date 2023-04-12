import numpy as np

def GenerateGrid(vector, orig, n_point):
   basis = [np.divide(vector[0], n_point[0]-1), np.divide(vector[1], n_point[1]-1),np.divide(vector[2], n_point[2]-1)]
   points = []
   for ii in range(n_point[0]):
      for jj in range(n_point[1]):
         for kk in range(n_point[2]):
            rr = ii*basis[0] + jj*basis[1] + kk*basis[2]
            rr += orig
            points.append(np.array(rr))
   return points
