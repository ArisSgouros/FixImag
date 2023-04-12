import numpy as np
from numpy.linalg import inv

def DeformGradGen(X, x):
   mm_mat = np.array([[X[0][0], X[0][1], X[0][2], 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , X[0][0], X[0][1], X[0][2], 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , X[0][0], X[0][1], X[0][2]],\
                      [X[1][0], X[1][1], X[1][2], 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , X[1][0], X[1][1], X[1][2], 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , X[1][0], X[1][1], X[1][2]],\
                      [X[2][0], X[2][1], X[2][2], 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , X[2][0], X[2][1], X[2][2], 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , 0.0    , 0.0    , 0.0    , X[2][0], X[2][1], X[2][2]],\
                     ])
   x_vec  = x.flatten()
   ff_vec = inv(mm_mat).dot(x_vec)
   ff_mat = np.array([[ff_vec[0], ff_vec[1], ff_vec[2]],\
                      [ff_vec[3], ff_vec[4], ff_vec[5]],\
                      [ff_vec[6], ff_vec[7], ff_vec[8]]])
   #print(X[0], x[0], ff_mat.dot(X[0]))
   #print(X[1], x[1], ff_mat.dot(X[1]))
   #print(X[2], x[2], ff_mat.dot(X[2]))
   return ff_mat

def DeformGradConstraint(X, x):
   mm_mat = np.array([[X[0][0], 0.0    , 0.0    , 0.0    , 0.0    , 0.0    ],\
                      [X[1][0], X[1][1], 0.0    , 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , X[1][1], 0.0    , 0.0    ],\
                      [X[2][0], X[2][1], X[2][2], 0.0    , 0.0    , 0.0    ],\
                      [0.0    , 0.0    , 0.0    , X[2][1], X[2][2], 0.0    ],\
                      [0.0    , 0.0    , 0.0    , 0.0    , 0.0    , X[2][2]],\
                     ])
   x_vec  = np.array([x[0][0], x[1][0], x[1][1], x[2][0], x[2][1], x[2][2]])
   ff_vec = inv(mm_mat).dot(x_vec)
   ff_mat = np.array([[ff_vec[0], ff_vec[1], ff_vec[2]],\
                      [0.0      , ff_vec[3], ff_vec[4]],\
                      [0.0      , 0.0      , ff_vec[5]]])
   #print(X[0], x[0], ff_mat.dot(X[0]))
   #print(X[1], x[1], ff_mat.dot(X[1]))
   #print(X[2], x[2], ff_mat.dot(X[2]))
   return ff_mat

def DeformGradAnalyt(X, x):
   f11 = x[0][0] / X[0][0]
   f22 = x[1][1] / X[1][1]
   f33 = x[2][2] / X[2][2]
   f12 = (x[1][0] - X[1][0]*f11)/X[1][1]
   f13 = (x[2][0] - X[2][0]*f11 - X[2][1]*f12) / X[2][2]
   f23 = (x[2][1] - X[2][1]*f22) / X[2][2]

   ff_mat = np.array([[f11, f12, f13],\
                      [0.0, f22, f23],\
                      [0.0, 0.0, f33]])
   #print(X[0], x[0], ff_mat.dot(X[0]))
   #print(X[1], x[1], ff_mat.dot(X[1]))
   #print(X[2], x[2], ff_mat.dot(X[2]))
   return ff_mat
