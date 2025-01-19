#!/bin/bash

# Deactivate previous conda environment if it's activated
conda deactivate

# Activate the new conda environment
conda activate autogrow

# Change directory
cd /home/imran/autogrow4/

# Run the following command
python run_autogrow.py \
    --filename_of_receptor /home/imran/autogrow4/tutorial/PARP/4YPX_prot_fixed.pdbqt \
    --center_x -22.22717809 --center_y  40.82374374 --center_z -5.66712301 \
    --size_x 30.0 --size_y 30.0 --size_z 30.0 \
    --source_compound_file /home/imran/autogrow4/source_compounds/smiles.smi \
    --root_output_folder /home/imran/ \
    --number_of_mutants_first_generation 50 \
    --number_of_crossovers_first_generation 50 \
    --number_of_mutants 50 \
    --number_of_crossovers 50 \
    --top_mols_to_seed_next_generation 50 \
    --number_elitism_advance_from_previous_gen 50 \
    --number_elitism_advance_from_previous_gen_first_generation 10 \
    --diversity_mols_to_seed_first_generation 10 \
    --diversity_seed_depreciation_per_gen 10 \
    --num_generations 5 \
    --mgltools_directory /home/imran/mgltools_x86_64Linux2_1.5.6/ \
    --mgl_python /home/imran/mgltools_x86_64Linux2_1.5.6/bin/mgltools_python \
    --obabel_path /usr/bin/obabel/ \
    --prepare_ligand4.py /home/imran/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py \
    --prepare_receptor4.py /home/imran/mgltools_x86_64Linux2_1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py \
    --mgl_python /home/imran/mgltools_x86_64Linux2_1.5.6/bin/pythonsh \
    --number_of_processors -1 \
    --scoring_choice VINA \
    --LipinskiLenientFilter \
    --start_a_new_run \
    --rxn_library click_chem_rxns \
    --selector_choice Rank_Selector \
    --dock_choice VinaDocking \
    --max_variants_per_compound 5 \
    --redock_elite_from_previous_gen False \
    --generate_plot True \
    --reduce_files_sizes True \
    --use_docked_source_compounds True \
    >  /home/imran/text_file.txt 2>  /home/imran/text_errormessage_file.txt
