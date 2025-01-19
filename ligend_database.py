import subprocess
from pathlib import Path

# Define the paths
ligend_data = '/home/imran/meet-u/files/PubChem_compound_smiles_similarity_C1=CC(=NC=C1C(=O)N)N_records.sdf'
ligend_database_folder = '/home/imran/meet-u/ligends_database'

# Make sure the output directory exists
Path(ligend_database_folder).mkdir(parents=True, exist_ok=True)

# Construct the obabel command
obabel_command = [
    "obabel", "-isdf", ligend_data, "-osdf", "-O", f"{ligend_database_folder}/%s.sdf", "--split"
]

# Run the command using subprocess
try:
    subprocess.run(obabel_command, check=True)
    print(f"Successfully converted {ligend_data} to individual SDF files in {ligend_database_folder}")
except subprocess.CalledProcessError as e:
    print(f"Error during conversion: {e}")
