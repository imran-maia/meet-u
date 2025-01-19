import os
from pathlib import Path
import subprocess
from Bio.PDB import PDBParser
import numpy as np
import sys


import subprocess
from pathlib import Path
from tqdm import tqdm  # Importing tqdm for the progress bar

# Define the path to the ligands directory
ligands_path = Path.home() / "meet-u/ligends_database"

# Get all .sdf files in the ligands directory
sdf_files = list(ligands_path.glob("*.sdf"))

# Initialize the progress bar with the total number of files
for sdf_file in tqdm(sdf_files, desc="Converting ligands", unit="file"):
    # Define the output path for each .pdbqt file
    pdbqt_file = ligands_path / f"{sdf_file.stem}.pdbqt"
    
    # Build the obabel command
    obabel_command = [
        "obabel", str(sdf_file), "-opdbqt", "-O", str(pdbqt_file)
    ]
    
    # Run the command to convert .sdf to .pdbqt
    try:
        subprocess.run(obabel_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {sdf_file}: {e}")
