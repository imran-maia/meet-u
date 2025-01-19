import os
from pathlib import Path
import subprocess
from Bio.PDB import PDBParser
import numpy as np
import sys


# Define masses for center of mass calculation
masses = {
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "H": 1.008,
    "S": 32.06
}

# Define the path
singlepath = Path.home() / "meet-u/target_receptor"


# Check if the path exists, create if not
if not singlepath.exists():
    os.makedirs(singlepath)
    print(f"Path '{singlepath}' was successfully created")
else:
    print(f"Path '{singlepath}' already exists")
    

# Specify the protein name
protein = sys.argv[1] #get the pdb name form the main file

# Download the PDB file
print('Downloading the PDB..................')
print('-------------------------------------')
os.system(f'wget https://files.rcsb.org/view/{protein} -O {protein}')

# Process the PDB file and save it in the target directory
target_file = singlepath / protein
with open(target_file, "w") as g:
    with open(protein, 'r') as f:
        for line in f:
            row = line.split()
            if row[0] == "ATOM":
                g.write(line)
            elif row[0] == "TER":
                g.write("TER\n")
    g.write("END\n")
print(f"\nFile '{protein}' successfully created in '{singlepath}'")
print('-------------------------------------')

# Parameterize the receptor using pdb2pqr
pqr_path = singlepath / f"{protein.replace('.pdb', '_prot.pqr')}"
pdb2pqr_command = [
    "pdb2pqr30",
    "--ff", "AMBER",
    "--keep-chain",
    "--titration-state-method", "propka",
    "--with-ph", "7.4",
    str(target_file),
    str(pqr_path)
]

print("\nRunning pdb2pqr to parameterize the receptor...")
subprocess.run(pdb2pqr_command, check=True)
print(f"Receptor parameterized and saved as '{pqr_path}'")

# Convert the .pqr file to a .pdbqt file using prepare_receptor4.py
prepare_receptor_script = "/home/imran/anaconda3/envs/meet-u/bin/prepare_receptor4.py"
pdbqt_path = singlepath / f"{protein.replace('.pdb', '_prot.pdbqt')}"
prepare_receptor_command = [
    "python2", prepare_receptor_script,
    "-r", str(pqr_path),
    "-o", str(pdbqt_path),
    "-C",
    "-U", "nphs_lps",
    "-v"
]

print("Converting .pqr to .pdbqt using prepare_receptor4.py...")
subprocess.run(prepare_receptor_command, check=True)
print(f"Receptor prepared and saved as '{pdbqt_path}'")

# Function to calculate the center of mass
def calculate_total_center_of_mass(chain, residues_of_interest=None):
    total_mass = 0.0
    center_of_mass = np.array([0.0, 0.0, 0.0])

    for residue in chain:
        if residues_of_interest is None or residue.id[1] in residues_of_interest:
            for atom in residue:
                element = atom.element
                if element in masses:
                    mass = masses[element]
                    coord = atom.coord
                    center_of_mass += mass * coord
                    total_mass += mass

    if total_mass == 0:
        return None
    return center_of_mass / total_mass

# Calculate the center of mass for specific residues
pdb_parser = PDBParser(QUIET=True)
structure = pdb_parser.get_structure("protein", str(target_file))

model = structure[0]
chain = model['A']

residues = [132, 133, 135, 140, 142]
com_selected = calculate_total_center_of_mass(chain, residues_of_interest=residues)
print(f"-----------------------------------------------------------")
print(f"\n\nCenter of mass for residues {residues}: {com_selected}")
print('\n')

def fix_pdbqt_atom_type(pdbqt_file, output_file):

    with open(pdbqt_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line[:17]+' '+line[18:])

# Usar el script
pdbqt_file  = Path.home() / "meet-u/target_receptor/4YPX_prot.pdbqt"
output_file = Path.home() / "meet-u/target_receptor/4YPX_prot_fixed.pdbqt"
fix_pdbqt_atom_type(pdbqt_file, output_file)