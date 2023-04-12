# Description
Compares the MIC and FIC for an input reference box and a strain tensor.

# Organization
The directory includes:
 - README.md -> current file
 - evaluate.py -> python script which conducts each experiment
 - run.py -> python script which includes the parameters of each experiment
 - clean.sh -> bash script which removes the output files
 - LOG_LIST -> text file containing the names of the validated output files
 - .gitignore -> text file containing the names of files and directories to be ignored by the git version control system
 - REF/ -> directory containing the validated output files of each experiment

# How to run
python run.py

# Output
For each one of the experiments the code outputs:
 - *.lammpstrj -> LAMMPS trajectory file
 - *.log -> log file
 - table1.csv -> CSV file including the output from all experiments
