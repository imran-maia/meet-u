import subprocess
import os

# Define the paths
docking_result_path = "/home/imran/meet-u/docking_results"
docking_result_subset_path = "/home/imran/meet-u/best_ligends_subset"

best_computed_ids = [
    58337908, 137244900, 43167671, 65529981, 68653568, 114169636, 73885319, 112727037, 18986587, 141455651,
    3031415, 71368267, 67324828, 43598821, 43599315, 172272034, 21521575, 30756033, 139729466, 130249255,
    80347887, 140330855, 130219421, 142116037, 3031427, 3031429, 55037128, 62160972, 129673238, 62072664,
    144395811, 168788211, 144395622, 62072944, 62074657, 252926, 79040504, 144625229, 17860847, 3039699,
    91205842, 114272094, 31076517, 68653608, 21221050, 114384359, 54943559, 58772630, 112722808, 15073511,
    71213782, 79033942, 23119574, 140330856, 113823510, 79099278, 54341013, 68522357, 66887686, 62073111,
    162719178, 55041948, 20339465, 62155126, 154234780, 23574357, 22028988, 113461543, 20215035, 91664313,
    141839417, 602287, 20321104, 22271454, 54238195, 171037195, 261592, 83187, 20517052, 115486570, 17893016,
    68459150, 2405731, 36834371, 170568765, 53334734, 91311755, 87555284, 91735308, 43317132, 69479878,
    141113237, 114169848, 89050714, 62073107, 53833611, 17856504, 58337917, 130478104, 21330884, 142987271,
    62160659, 21472602, 140671083, 62160515, 113966362, 55037403, 29048197, 113328065, 901914, 91381381,
    58772603, 20321194, 171638145
]


# List to hold formatted output (ID and SMILES)
output_list = []

# Iterate through each best computed ID to process docking results
for compound_id in best_computed_ids:
    # Build the PDBQT file path
    docking_result = os.path.join(docking_result_path, f"{compound_id}_output.pdbqt")
    
    # Build the SMILES file path
    docking_result_smile = os.path.join(docking_result_subset_path, f"{compound_id}.smi")
    
    # Check if the docking result file exists
    if os.path.exists(docking_result):
        # Run the OpenBabel conversion command using subprocess
        command = ["obabel", docking_result, "-O", docking_result_smile]
        
        # Execute the command
        subprocess.run(command, check=True)

        # Read the SMILES string from the generated file
        with open(docking_result_smile, 'r') as smi_file:
            smiles = smi_file.readline().strip()  # Read the first line (SMILES string)
            # Append the formatted result to the output list
            output_list.append(f"{smiles}")

# Print all results at once
if output_list:
    print("\n".join(output_list))
else:
    print("No SMILES were processed. Please check the input files.")
