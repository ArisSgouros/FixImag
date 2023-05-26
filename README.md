# FixImag
This is the repository of the FixImag code.
This is an open-source code, distributed under the terms of the accompanying LICENSE.

# Authors
- Dr. Aristotelis P. Sgouros (arissgouros@gmail.com)
- Prof. Doros N. Theodorou (doros@central.ntua.gr)

# Description
The code implements the Fix Image Convention (FIC); details regarding the mathematical formulation are reported in Ref [1]

# Organization
The FixImag repository includes the following:
 - README.md -> current file
 - LICENSE -> GNU General Public License of the code (GPL)
 - .gitignore -> contains all files and directories to be ignored by the git version control system
 - source/ -> directory containing the source files of the project
 - dev/ -> directory containing tests for the evaluation of the integrity of the code for development purposes
 - example/ -> files for conducting the experiments shown in Table 1 of Ref [1]

# Installation/prerequisites
No installation is required.
The scripts can be evaluated with Python3.

# Note
In this implementation:
 - the minimum image convention is referred to as MIN (instead of MIC [1])
 - the fixed image convention is referred to as FIX (instead of FIC [1])

# References
[1] Sgouros, A.P.; Theodorou, D.N.; "Addressing the Folding of Intermolecular Springs in Particle Simulations: Fixed Image Convention". Computation 2023, 11(6), 106; https://doi.org/10.3390/computation11060106.
