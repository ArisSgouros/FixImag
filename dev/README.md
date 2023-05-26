# Description
The directory includes tests which evaluate the integrity of the code.

# Organization
The directory includes:
 - README.md -> current file
 - test_deform/ -> computes the deformation gradient from input reference and deformed boxes
 - test_imag_box/ -> compares the MIC and FIC with input reference and deformed boxes
 - test_imag_strain/ -> compares the MIC and FIC for an input reference box and a strain tensor
 - test_integrity.sh -> bash script which conducts an automatic test

# How to run
The integrity of the code can be evaluated in Linux by running the bash script:
./test_integrity.sh

The script runs the tests one-by-one and compares the output of the current version of the code with validated output files in the folder "example"/REF/
In case that the outputs are/aren't the same the script will issue a success/fail message.

# References
[1] Sgouros, A.P.; Theodorou, D.N.; "Addressing the Folding of Intermolecular Springs in Particle Simulations: Fixed Image Convention". Computation 2023, 11(6), 106; https://doi.org/10.3390/computation11060106.
