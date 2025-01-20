# main.py

# Import libraries
import subprocess

# Specify the PDB file name
target_pdb = '4YPX.pdb'

# Select the task
target_preparation    = False
ligend_database       = False
ligend_preparation    = False
docking_simulation    = False
subset_converstion    = False
autogrow_optimization = False  
redocking_simulation  = False
redocking_smile       = True


# Target preparation
if target_preparation == True:
    subprocess.run(["python", "target_preparation.py", target_pdb])

# Create ligend database
if ligend_database == True:
    subprocess.run(["python", "ligend_database.py"])

# Ligend preparation
if ligend_preparation == True:
    subprocess.run(["python", "ligend_preparation.py"])

# Simulate docking 
if docking_simulation == True:
    subprocess.run(["python", "simulate_docking.py"])

# Convert docking results subset into simile
if subset_converstion == True:
    subprocess.run(["python", "docking_subset_smile.py"])

# Run the bash script for AutoGrow simulation
if autogrow_optimization == True:
    subprocess.run(["/bin/bash", "./run_autogrow.sh"])

# Simulate redocking after autogrow optimization
if redocking_simulation == True:
    subprocess.run(["python", "simulate_redocking.py"])

# Convert docking results subset into simile
if redocking_smile == True:
    subprocess.run(["python", "redocking_smile.py"])

