import os
from pathlib import Path
import subprocess

# Define the paths
dock_path = Path.home() / "meet-u/redocking_config_files"      # Your docking folder path /doc_config
ligend_folder_path = Path.home() / "meet-u/autogrow_optimized_ligends_files"     # Folder containing the ligands /ligends
receptor_path = "/home/imran/meet-u/target_receptor/4YPX_prot.pdbqt"  # Receptor path for docking
docking_results_path = Path.home() / "meet-u/redocking_results"  # /docking_result

# Full path to vina executable
vina_path = "/home/imran/vina/vina_1.2.5_linux_x86_64"

# Loop through all .pdbqt files in the ligend folder (ignore .sdf files)
for ligand_file in ligend_folder_path.glob("*.pdbqt"):
    # Define the configuration file path for each ligand
    config_path = dock_path / f"config_{ligand_file.stem}.txt"

    # Create the configuration file for the ligand
    with open(config_path, "w") as f:
        f.write("#CONFIGURATION FILE (options not used are commented) \n")
        f.write("\n")
        f.write("#INPUT OPTIONS \n")
        f.write(f"receptor = {receptor_path} \n")
        f.write(f"ligand = /home/imran/meet-u/autogrow_optimized_ligends_files/{ligand_file.name} \n")  # Write ligand path /ligneds
        f.write("#flex = [flexible residues in receptor in pdbqt format] \n")
        f.write("\n")
        f.write("#SEARCH SPACE CONFIGURATIONS \n")
        f.write("center_x = -22.22717809\n")
        f.write("center_y = 40.82374374\n")
        f.write("center_z = -5.66712301\n")
        f.write("size_x = 30 \n")
        f.write("size_y = 30 \n")
        f.write("size_z = 30 \n")
        f.write("\n")
        f.write("#OUTPUT OPTIONS \n")
        
        # Set the output file name to include the ligand ID, and save it to the docking_results folder
        output_filename = docking_results_path / f"{ligand_file.stem}_output.pdbqt"
        f.write(f"out = {output_filename}\n")


        
        f.write("\n")
        f.write("#OTHER OPTIONS \n")
        f.write("num_modes = 5\n")
        f.write("#cpu =  \n")
        f.write("#exhaustiveness = \n")
        f.write("#energy_range = \n")
        f.write("#seed = ")

    print(f"Configuration file for {ligand_file.name} created at {config_path}")

 # Define the log file path
    log_filename = docking_results_path / f"{ligand_file.stem}_vina_out.log"

    # Run AutoDock Vina with the full path to the executable, redirecting output to both the terminal and log file
    try:
        # Use 'tee' to display the status in terminal and write the output to the log file
        with open(log_filename, "w") as log_file:
            subprocess.run(
                f"{vina_path} --config {config_path} | tee {log_filename}",
                shell=True,
                check=True
            )
        print(f"Docking completed for {ligand_file.name}")
    except subprocess.CalledProcessError as e:
        print(f"Error during docking for {ligand_file.name}: {e}")