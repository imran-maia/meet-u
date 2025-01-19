import subprocess

# Define the path of the input SMILES text file
input_file = "/home/imran/meet-u/results/autogrow_optimized_ligends_smile.txt"

# Define the output directory
output_dir = "/home/imran/meet-u/autogrow_optimized_ligends_files/"

# Read the SMILES strings from the input text file
with open(input_file, 'r') as file:
    smiles_list = file.readlines()

# Loop through each SMILES string and process them
for i, smiles in enumerate(smiles_list, 1):
    smiles = smiles.strip()  # Remove leading/trailing whitespaces or newlines

    # Specify the output PDBQT file name
    output_pdbqt_file = f"{output_dir}autogrow_optimized_ligends_{i}.pdbqt"

    # Open Babel conversion command for a single SMILES string
    command = [
        "obabel",  # Open Babel command
        f"-:{smiles}",  # Input SMILES string
        "-O", output_pdbqt_file,  # Output PDBQT file path
        "--addhydrogens",  # Add hydrogens
        "--gen3d",  # Generate 3D coordinates
        "--partialcharge"  # Calculate partial charges
    ]

    # Execute the Open Babel command
    subprocess.run(command, check=True)

    # Print the status
    print(f"Successfully converted SMILES {i} to {output_pdbqt_file}")
