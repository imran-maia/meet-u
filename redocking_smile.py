import subprocess
import os

# Define the paths
docking_result_path = "/home/imran/meet-u/redocking_results"
docking_result_subset_path = "/home/imran/meet-u/best_ligends_subset"

best_computed_ids = ['autogrow_optimized_ligends_27',
                        'autogrow_optimized_ligends_18',
                        'autogrow_optimized_ligends_6',
                        'autogrow_optimized_ligends_11',
                        'autogrow_optimized_ligends_34',
                        'autogrow_optimized_ligends_19',
                        'autogrow_optimized_ligends_43',
                        'autogrow_optimized_ligends_49',
                        'autogrow_optimized_ligends_10',
                        'autogrow_optimized_ligends_46',
                        'autogrow_optimized_ligends_14',
                        'autogrow_optimized_ligends_20',
                        'autogrow_optimized_ligends_86',
                        'autogrow_optimized_ligends_31',
                        'autogrow_optimized_ligends_66',
                        'autogrow_optimized_ligends_29',
                        'autogrow_optimized_ligends_62',
                        'autogrow_optimized_ligends_78',
                        'autogrow_optimized_ligends_76',
                        'autogrow_optimized_ligends_47',
                        'autogrow_optimized_ligends_2',
                        'autogrow_optimized_ligends_38',
                        'autogrow_optimized_ligends_64',
                        'autogrow_optimized_ligends_73',
                        'autogrow_optimized_ligends_60',
                        'autogrow_optimized_ligends_61',
                        'autogrow_optimized_ligends_72',
                        'autogrow_optimized_ligends_21',
                        'autogrow_optimized_ligends_15',
                        'autogrow_optimized_ligends_54',
                        'autogrow_optimized_ligends_67',
                        'autogrow_optimized_ligends_35',
                        'autogrow_optimized_ligends_59',
                        'autogrow_optimized_ligends_28',
                        'autogrow_optimized_ligends_32',
                        'autogrow_optimized_ligends_45',
                        'autogrow_optimized_ligends_85',
                        'autogrow_optimized_ligends_42',
                        'autogrow_optimized_ligends_5',
                        'autogrow_optimized_ligends_52',
                        'autogrow_optimized_ligends_84',
                        'autogrow_optimized_ligends_3',
                        'autogrow_optimized_ligends_33',
                        'autogrow_optimized_ligends_83',
                        'autogrow_optimized_ligends_65',
                        'autogrow_optimized_ligends_69',
                        'autogrow_optimized_ligends_44',
                        'autogrow_optimized_ligends_70',
                        'autogrow_optimized_ligends_81',
                        'autogrow_optimized_ligends_82',
                        'autogrow_optimized_ligends_48',
                        'autogrow_optimized_ligends_16',
                        'autogrow_optimized_ligends_13',
                        'autogrow_optimized_ligends_79',
                        'autogrow_optimized_ligends_57',
                        'autogrow_optimized_ligends_7',
                        'autogrow_optimized_ligends_55',
                        'autogrow_optimized_ligends_51',
                        'autogrow_optimized_ligends_40',
                        'autogrow_optimized_ligends_23',
                        'autogrow_optimized_ligends_4',
                        'autogrow_optimized_ligends_12',
                        'autogrow_optimized_ligends_37',
                        'autogrow_optimized_ligends_17',
                        'autogrow_optimized_ligends_25',
                        'autogrow_optimized_ligends_88',
                        'autogrow_optimized_ligends_39',
                        'autogrow_optimized_ligends_58',
                        'autogrow_optimized_ligends_8',
                        'autogrow_optimized_ligends_41',
                        'autogrow_optimized_ligends_50',
                        'autogrow_optimized_ligends_71',
                        'autogrow_optimized_ligends_63',
                        'autogrow_optimized_ligends_77',
                        'autogrow_optimized_ligends_94',
                        'autogrow_optimized_ligends_89',
                        'autogrow_optimized_ligends_91',
                        'autogrow_optimized_ligends_95',
                        'autogrow_optimized_ligends_1',
                        'autogrow_optimized_ligends_74',
                        'autogrow_optimized_ligends_56',
                        'autogrow_optimized_ligends_53',
                        'autogrow_optimized_ligends_36',
                        'autogrow_optimized_ligends_87',
                        'autogrow_optimized_ligends_26',
                        'autogrow_optimized_ligends_90',
                        'autogrow_optimized_ligends_68',
                        'autogrow_optimized_ligends_93',
                        'autogrow_optimized_ligends_92',
                        'autogrow_optimized_ligends_22',
                        'autogrow_optimized_ligends_9',
                        'autogrow_optimized_ligends_75',
                        'autogrow_optimized_ligends_30',
                        'autogrow_optimized_ligends_96',
                        'autogrow_optimized_ligends_24']


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
