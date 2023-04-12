# Description
The directory calculates the deformation gradient from input reference and deformed boxes.

# Organization
The directory includes:
 - README.md -> current file
 - run.py -> python script which conducts the tests
 - clean.sh -> bash script which removes the output files
 - LOG_LIST -> text file containing the names of the validated output files
 - .gitignore -> text file containing the names of files and directories to be ignored by the git version control system
 - REF/ -> directory containing the validated output files of each experiment

# How to run
python run.py

# Output
For code outputs:
 - 0.test_deform.lammpstrj -> LAMMPS trajectory file includes
 - screen -> vectors of the reference and deformed boxes and the corresponding deformation gradients
